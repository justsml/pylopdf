"""Run isolated, resumable PDF structure experiments with complete local artifacts."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import platform
import re
import statistics
import subprocess
import time
import traceback
from collections import Counter
from datetime import datetime, timezone
from importlib import metadata
from typing import TYPE_CHECKING, Any

import pylopdf
from bench.feature_cases import ROOT
from bench.structure_cases import RECORD_REFERENCES, build_structure_cases
from bench.structure_core import (
    HtmlTables,
    geometry_tables,
    markdown_tables,
    render_tables,
    score_records,
    score_tables,
    source_agreement,
    validate_patch,
    visible_text,
)
from bench.structure_native import header_guided_records, native_records

if TYPE_CHECKING:
    from pathlib import Path

ARTIFACTS = ROOT / "bench/results/structure-artifacts"
REPORT = ROOT / "bench/results/structure-latest.json"
MODEL = "allenai/olmOCR-2-7B-1025"
QWEN_MODEL = "Qwen/Qwen2.5-VL-3B-Instruct"
_MAX_CROPS = 16
PATCH_PROMPT = (
    "Recover table structure from this page image and the positioned source words. Return ONLY JSON: "
    '{"tables":[{"rows":[[["p0w1"],["p0w2"]],[["p0w3"],[]]],"spans":[]}]} . '
    "Each cell is an ordered list of source word IDs, never newly transcribed text. Each ID may occur only once. "
    "Empty cells are []. Each span is [row, column, rowspan, colspan], zero based; covered cells must be empty. "
    "Preserve row/column relationships, wrapped cells, empty cells, and merged headers. "
    "Do not classify multicolumn prose as a table. Return an empty tables list if no table exists. "
    "Unassigned words will be preserved automatically outside the tables. "
    "Coordinates use the display image with a top-left origin. SOURCE_WORDS:\n"
)


def write_json(path: Path, value: Any) -> None:  # noqa: ANN401
    """Checkpoint complete JSON with an atomic local replacement."""
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def prepare() -> list[dict[str, Any]]:
    """Save input bytes, screenshots, and stable positioned-word identities."""
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    bundles = []
    for case in build_structure_cases():
        directory = ARTIFACTS / case.feature.name
        directory.mkdir(exist_ok=True)
        (directory / "input.pdf").write_bytes(case.feature.data)
        with pylopdf.open(stream=case.feature.data) as document:
            page = document[0]
            rect = page.rect
            dpi = 72 * 1288 / max(rect.width, rect.height)
            page.get_pixmap(dpi=dpi, background=(255, 255, 255)).save(directory / "page.png")
            rotation = page.rotation
            directions: Counter[tuple[int, int]] = Counter()
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    direction = (round(line["dir"][0]), round(line["dir"][1]))
                    directions[direction] += sum(len(span["text"]) for span in line["spans"])
            dominant = directions.most_common(1)[0][0] if directions else (1, 0)
            orientation = {(1, 0): 0, (0, 1): 90, (-1, 0): 180, (0, -1): 270}.get(dominant, 0)
            words = []
            for index, word in enumerate(page.get_text("words")):
                x0, y0, x1, y1 = word[:4]
                logical = {
                    0: (x0, y0, x1, y1),
                    90: (y0, rect.width - x1, y1, rect.width - x0),
                    180: (rect.width - x1, rect.height - y1, rect.width - x0, rect.height - y0),
                    270: (rect.height - y1, x0, rect.height - y0, x1),
                }[orientation]
                words.append(
                    {"id": f"p0w{index}", "bbox": list(word[:4]), "logical_bbox": list(logical), "text": word[4]}
                )
            bundle = {
                "name": case.feature.name,
                "sha256": hashlib.sha256(case.feature.data).hexdigest(),
                "source": case.feature.source,
                "notes": case.feature.notes,
                "page_count": len(document),
                "page": 0,
                "width": rect.width,
                "height": rect.height,
                "rotation": rotation,
                "orientation": orientation,
                "words": words,
                "expected_tables": case.tables,
                "expected_spans": case.spans,
                "expected_text": case.feature.expected_text,
                "expected_order": case.feature.expected_order,
                "baseline": page.to_markdown(),
                "text_tables": page.to_markdown(table_strategy="text"),
            }
        write_json(directory / "bundle.json", bundle)
        bundles.append(bundle)
    write_json(ARTIFACTS / "manifest.json", bundles)
    return bundles


class Engines:
    """Load one local GPU model at a time; no hosted requests are made."""

    def __init__(self, adapter: str, device: str) -> None:
        """Initialize only the model required by this intervention."""
        self.adapter = adapter
        self.device = device
        self.model: Any = None
        self.processor: Any = None
        self.model_path = None
        self.ocr = None
        start = time.perf_counter()
        if adapter.startswith("ocr"):
            model_root = ROOT / "models/pylopdf-ocr-models/src/pylopdf_ocr_models"
            self.ocr = pylopdf.OcrEngine(
                model_root / "PP-OCRv6_det_small.rten",
                model_root / "PP-OCRv6_rec_small.rten",
                model_root / "ppocrv6_dict.txt",
                threads=4,
            )
        elif adapter.startswith("yolo"):
            hub = importlib.import_module("huggingface_hub")
            self.model_path = hub.hf_hub_download("hantian/yolo-doclaynet", "yolo26m-doclaynet.pt")
            self.model = importlib.import_module("ultralytics").YOLO(self.model_path)
        elif adapter.startswith(("olmocr", "qwen")):
            transformers = importlib.import_module("transformers")
            torch = importlib.import_module("torch")
            self.model_path = QWEN_MODEL if adapter.startswith("qwen") else MODEL
            quantization = (
                transformers.BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_compute_dtype=torch.bfloat16,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_use_double_quant=True,
                )
                if "4bit" in adapter
                else None
            )
            self.model = transformers.Qwen2_5_VLForConditionalGeneration.from_pretrained(
                self.model_path,
                torch_dtype=torch.bfloat16,
                attn_implementation="sdpa",
                device_map=device,
                quantization_config=quantization,
            ).eval()
            self.processor = transformers.AutoProcessor.from_pretrained(self.model_path)
            if "lora" in adapter:
                self.model = (
                    importlib.import_module("peft")
                    .PeftModel.from_pretrained(
                        self.model,
                        ARTIFACTS / "training/adapter",
                    )
                    .eval()
                )
        self.initialization_seconds = time.perf_counter() - start

    def detect(self, bundle: dict[str, Any], directory: Path) -> list[dict[str, Any]]:
        """Keep complete layout predictions and map pixel boxes to display points."""
        image_module = importlib.import_module("PIL.Image")
        image = image_module.open(directory / "page.png")
        width, height = bundle["width"], bundle["height"]
        if "normalized" in self.adapter:
            image = image.rotate(bundle.get("orientation", bundle["rotation"]), expand=True)
            if bundle.get("orientation", bundle["rotation"]) in {90, 270}:
                width, height = height, width
        prediction = self.model.predict(image, device=self.device, imgsz=1024, conf=0.2, verbose=False)[0]
        predictions = []
        for box in prediction.boxes:
            xyxy = box.xyxy[0].tolist()
            predictions.append(
                {
                    "label": prediction.names[int(box.cls[0])],
                    "confidence": float(box.conf[0]),
                    "bbox": [
                        xyxy[i] * (width / image.width if i % 2 == 0 else height / image.height) for i in range(4)
                    ],
                }
            )
        write_json(directory / f"{self.adapter}-detections.json", predictions)
        prediction.save(filename=str(directory / f"{self.adapter}-detections.png"))
        return predictions

    def generate(self, image: Any, prompt: str, limit: int) -> tuple[str, dict[str, Any]]:  # noqa: ANN401
        """Use greedy local decoding and report whether output hit its token boundary."""
        torch = importlib.import_module("torch")
        messages = [{"role": "user", "content": [{"type": "image", "image": image}, {"type": "text", "text": prompt}]}]
        text = self.processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.processor(text=[text], images=[image], return_tensors="pt").to(self.device)
        torch.cuda.reset_peak_memory_stats()
        with torch.inference_mode():
            output = self.model.generate(**inputs, max_new_tokens=limit, do_sample=False)
        generated = output[0, inputs["input_ids"].shape[1] :]
        return self.processor.decode(generated, skip_special_tokens=True), {
            "input_tokens": inputs["input_ids"].shape[1],
            "output_tokens": len(generated),
            "truncated": len(generated) >= limit,
            "peak_cuda_allocated_bytes": torch.cuda.max_memory_allocated(),
        }


def run_adapter(bundle: dict[str, Any], engine: Engines, limit: int) -> dict[str, Any]:  # noqa: C901, PLR0911, PLR0912
    """Keep each intervention separate and retain rejected raw patches."""
    name = engine.adapter
    directory = ARTIFACTS / bundle["name"]
    words = bundle["words"]
    if name.startswith("retained"):
        original = json.loads((ROOT / "bench/results/features-models.json").read_text())
        case = next(case for case in original["cases"] if case["name"] == bundle["name"])
        if case["input_sha256"] != bundle["sha256"] or bundle["page_count"] != 1:
            msg = "retained model output requires identical single-page input"
            raise ValueError(msg)
        prior = next(row for row in case["results"] if row["adapter"] == name.removeprefix("retained-"))
        text = (ROOT / "bench/results/feature-outputs" / prior["raw_output"]).read_text()
        if hashlib.sha256(text.encode()).hexdigest() != prior["output_sha256"]:
            msg = "retained model output hash changed"
            raise ValueError(msg)
        return {
            "markdown": text,
            "tables": markdown_tables(text),
            "retained_result": prior,
            "retained_run": original["additional_runs"][prior["run_index"]],
        }
    if name.startswith("ocr"):
        with pylopdf.open(directory / "input.pdf") as document:
            recognized = document[0].apply_ocr(dpi=150, engine=engine.ocr)
            collected = document[0].get_text("words")
            ocr_words: list[dict[str, Any]] = [
                {"id": f"p0w{i}", "text": word[4], "bbox": list(word[:4]), "logical_bbox": list(word[:4])}
                for i, word in enumerate(collected)
            ]
            payload = {"tables": [{"rows": table} for table in geometry_tables(ocr_words, wrapped=True)]}
            matrices, consumed = validate_patch(payload, ocr_words)
            text = (
                render_tables(matrices)
                + "\n\n"
                + " ".join(word["text"] for word in ocr_words if word["id"] not in consumed)
            )
        write_json(directory / f"{name}-words.json", ocr_words)
        return {
            "markdown": text,
            "tables": matrices,
            "recognized_words": len(recognized),
            "ocr_policy": "150 dpi, skip_existing=True, four inference threads; geometry follows OCR display boxes",
        }
    if name in {"pylopdf", "pylopdf-text"}:
        text = bundle["baseline" if name == "pylopdf" else "text_tables"]
        return {"markdown": text, "tables": markdown_tables(text)}
    if name.startswith("native"):
        with pylopdf.open(directory / "input.pdf") as document:
            page = document[0]
            matrices = header_guided_records(page, words) if "header" in name else []
            guided = bool(matrices)
            if not guided:
                matrices = native_records(page)
            boxes = [table.bbox for table in page.find_tables()]
            outside = [
                word
                for word in words
                if not any(
                    box.x0 <= (word["bbox"][0] + word["bbox"][2]) / 2 <= box.x1
                    and box.y0 <= word["bbox"][1] <= (page.rect.y1 if guided else box.y1)
                    for box in boxes
                )
            ]
        return {
            "markdown": render_tables(matrices, bullets=True) + "\n\n" + " ".join(word["text"] for word in outside),
            "tables": matrices,
            "header_policy": "vector header or neutral column labels; continuation lines attach to prior record",
        }
    if name.startswith(("geometry", "yolo")):
        candidates = [words]
        if name.startswith("yolo"):
            detections = engine.detect(bundle, directory)
            candidates = []
            for region in detections:
                if region["label"].lower() != "table":
                    continue
                x0, y0, x1, y1 = region["bbox"]
                box_key = "logical_bbox" if "normalized" in name else "bbox"
                candidates.append(
                    [
                        word
                        for word in words
                        if x0 <= (word[box_key][0] + word[box_key][2]) / 2 <= x1
                        and y0 <= (word[box_key][1] + word[box_key][3]) / 2 <= y1
                    ]
                )
        payload = {
            "tables": [
                {"rows": table}
                for candidate in candidates
                for table in geometry_tables(candidate, wrapped="wrapped" in name)
            ]
        }
        matrices, consumed = validate_patch(payload, words)
        write_json(directory / f"{name}-patch.json", payload)
        remainder = " ".join(word["text"] for word in words if word["id"] not in consumed)
        return {
            "markdown": render_tables(matrices, bullets="bullets" in name) + "\n\n" + remainder,
            "tables": matrices,
            "source_ids_used": len(consumed),
            "source_ids_total": len(words),
            "header_policy": "first recovered row; may be wrong without semantic evidence",
        }
    image = importlib.import_module("PIL.Image").open(directory / "page.png").convert("RGB")
    prompt = (
        "Read this document page in natural reading order and return Markdown. Preserve exact text, numbers, "
        "punctuation, and empty table cells. Use HTML tables with rowspan/colspan for merged cells. "
        "Do not summarize or invent content. Preserve references and footnotes."
        if name.startswith("qwen")
        else importlib.import_module("olmocr.prompts").build_no_anchoring_v4_yaml_prompt()
    )
    if "normalized" in name:
        image = image.rotate(bundle.get("orientation", bundle["rotation"]), expand=True)
    source = json.dumps(
        {
            "width": bundle["width"],
            "height": bundle["height"],
            "words": [{k: v for k, v in word.items() if k != "logical_bbox"} for word in words],
        },
        ensure_ascii=False,
    )
    if "compact" in name:
        source = json.dumps(
            {
                "width": round(bundle["width"], 1),
                "height": round(bundle["height"], 1),
                "word_format": ["id", "x0", "y0", "x1", "y1", "text"],
                "words": [[word["id"], *[round(value, 1) for value in word["bbox"]], word["text"]] for word in words],
            },
            ensure_ascii=False,
            separators=(",", ":"),
        )
    if name.endswith("text"):
        prompt += (
            "\nAdditional extracted source words with top-left display coordinates. Preserve exact text and values "
        )
        prompt += "when legible; the image determines reading order and table structure:\n" + source
    elif name.endswith("patch"):
        prompt = PATCH_PROMPT + source
    (directory / f"{name}-prompt.txt").write_text(prompt)
    if name.endswith("crop"):
        return run_crops(bundle, engine, image, prompt, limit)
    raw, details = engine.generate(image, prompt, limit)
    (directory / f"{name}-raw.txt").write_text(raw)
    if name.endswith("patch"):
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip())
        payload = json.loads(cleaned)
        matrices, consumed = validate_patch(payload, words)
        remainder = " ".join(word["text"] for word in words if word["id"] not in consumed)
        text = render_tables(matrices, spans=[table.get("spans", []) for table in payload["tables"]])
        text += "\n\n" + remainder
        details.update({"source_ids_used": len(consumed), "source_ids_total": len(words)})
    else:
        text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.DOTALL)
        matrices = markdown_tables(text)
    return {"markdown": text, "tables": matrices, **details}


def run_crops(bundle: dict[str, Any], engine: Engines, image: Any, prompt: str, limit: int) -> dict[str, Any]:  # noqa: ANN401
    """Recognize reusable detected regions, preserving source text outside their boxes."""
    directory = ARTIFACTS / bundle["name"]
    if "geometry" in engine.adapter:
        tables = geometry_tables(bundle["words"], wrapped=True)
        source = {word["id"]: word for word in bundle["words"]}
        regions: list[dict[str, Any]] = []
        for table in tables:
            selected = [source[word_id] for row in table for cell in row for word_id in cell]
            regions.append(
                {
                    "label": "Table",
                    "bbox": [
                        min(w["bbox"][0] for w in selected),
                        min(w["bbox"][1] for w in selected),
                        max(w["bbox"][2] for w in selected),
                        max(w["bbox"][3] for w in selected),
                    ],
                }
            )
    else:
        regions = json.loads((directory / "yolo-geometry-detections.json").read_text())
    regions = [region for region in regions if region["label"].lower() == "table"]
    if not regions:
        raw, details = engine.generate(image, prompt, limit)
        (directory / f"{engine.adapter}-raw.txt").write_text(raw)
        text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.DOTALL)
        return {"markdown": text, "tables": markdown_tables(text), "crop_count": 0, **details}
    if len(regions) > _MAX_CROPS:
        msg = "crop candidate count exceeds 16"
        raise ValueError(msg)
    blocks = []
    matrices = []
    covered: set[str] = set()
    outputs = []
    for index, region in enumerate(regions):
        x0, y0, x1, y1 = region["bbox"]
        pixel_box = (
            max(0, x0 - 8) * image.width / bundle["width"],
            max(0, y0 - 8) * image.height / bundle["height"],
            min(bundle["width"], x1 + 8) * image.width / bundle["width"],
            min(bundle["height"], y1 + 8) * image.height / bundle["height"],
        )
        crop = image.crop(pixel_box)
        scale = 1288 / max(crop.size)
        crop = crop.resize((round(crop.width * scale), round(crop.height * scale)))
        crop.save(directory / f"{engine.adapter}-crop-{index}.png")
        raw, details = engine.generate(crop, prompt, limit)
        (directory / f"{engine.adapter}-crop-{index}-raw.txt").write_text(raw)
        text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", raw, flags=re.DOTALL)
        blocks.append(text)
        matrices.extend(markdown_tables(text))
        outputs.append(details)
        covered.update(
            word["id"]
            for word in bundle["words"]
            if x0 <= (word["bbox"][0] + word["bbox"][2]) / 2 <= x1
            and y0 <= (word["bbox"][1] + word["bbox"][3]) / 2 <= y1
        )
    blocks.append(" ".join(word["text"] for word in bundle["words"] if word["id"] not in covered))
    return {
        "markdown": "\n\n".join(blocks),
        "tables": matrices,
        "crop_count": len(regions),
        "crop_details": outputs,
        "truncated": any(output["truncated"] for output in outputs),
        "crop_policy": "replace centroid-covered words; append outside source in extraction order",
        "detection_cost": "reused YOLO predictions or geometry; excludes YOLO inference",
    }


def format_report(report: dict[str, Any]) -> str:
    """Publish observed content and relation checks without a composite quality score."""
    lines = [
        "# Structured PDF recovery experiments",
        "",
        f"Run: {report['metadata']['started_at']}",
        "",
        "Page 0 of each preserved input is evaluated. Full inputs, screenshots, positioned words, prompts,",
        "raw responses, validated patches, and errors are retained locally in `structure-artifacts/`.",
        "Reference cells are independent fixture definitions; corpus cells without a reference remain unscored.",
        "Source agreement is not ground truth, especially for missing Unicode, scans, or OCR corrections.",
        "Geometry bullet results score their underlying recovered cells, not reparsed bullet labels.",
        "Timing covers the adapter after preparation, excluding fixture extraction/rendering; prepared baselines",
        "are replayed, so their timing is not a conversion measurement. Process RSS is cumulative high-water RSS.",
        "Model repetitions include the first inference; initialization is reported separately. No throughput claims.",
        "",
        "| Case | Adapter | Exact grid | Cells | Relations recalled | Record cells | Seconds | Result |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- |",
    ]
    for result in report["results"]:
        score = result.get("score", {})
        cells = f"{score['correct_cells']}/{score['total_cells']}" if score.get("total_cells") else "—"
        relations = (
            f"{score['relationship_matches']}/{score['relationship_expected']}"
            if score.get("relationship_expected")
            else "—"
        )
        exact = str(score.get("exact", "unscored"))
        records = result.get("record_checks", {})
        record_cells = f"{records['correct']}/{records['total']}" if records.get("total") else "—"
        status = result.get("error", "truncated" if result.get("output", {}).get("truncated") else "ok")
        status = status.replace("\n", " ").replace("|", "\\|")[:140]
        lines.append(
            f"| {result['case']} | {result['adapter']} | {exact} | {cells} | {relations} | "
            f"{record_cells} | {result.get('median_seconds', 0):.3f} | {status} |"
        )
    lines.extend(["", "## Run provenance", "", "```json", json.dumps(report["metadata"], indent=2), "```", ""])
    return "\n".join(lines)


def rescore(report: dict[str, Any]) -> None:
    """Update observation code without regenerating or retiming any model output."""
    bundles = {bundle["name"]: bundle for bundle in json.loads((ARTIFACTS / "manifest.json").read_text())}
    for result in report["results"]:
        if "error" in result:
            continue
        bundle = bundles[result["case"]]
        if result["sha256"] != bundle["sha256"]:
            msg = f"refusing to rescore changed input: {result['case']}"
            raise ValueError(msg)
        text = (ARTIFACTS / result["case"] / f"{result['adapter']}.md").read_text()
        if hashlib.sha256(text.encode()).hexdigest() != result["output_sha256"]:
            msg = f"refusing to rescore changed output: {result['case']} / {result['adapter']}"
            raise ValueError(msg)
        visible = visible_text(text)
        if result["adapter"].startswith(("olmocr", "qwen", "pylopdf")):
            result["output"]["tables"] = markdown_tables(text)
        result["score"] = score_tables(result["output"]["tables"], bundle["expected_tables"])
        result["literal_checks"] = {value: value in visible for value in bundle["expected_text"]}
        result["source_agreement"] = source_agreement(text, bundle["words"])
        result["record_checks"] = score_records(result["output"]["tables"], RECORD_REFERENCES.get(bundle["name"], {}))
        span_parser = HtmlTables()
        span_parser.feed(text)
        result["merged_spans_exact"] = list(map(list, span_parser.spans)) == bundle["expected_spans"]
    report["metadata"]["observation_code_sha256"] = hashlib.sha256(
        (ROOT / "bench/structure_core.py").read_bytes(),
    ).hexdigest()
    write_json(REPORT, report)
    REPORT.with_suffix(".md").write_text(format_report(report))


def main() -> None:  # noqa: C901
    """Checkpoint every case so model failures cannot discard completed experiments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument(
        "--adapter",
        action="append",
        choices=[
            "pylopdf",
            "pylopdf-text",
            "geometry",
            "geometry-bullets",
            "geometry-wrapped",
            "geometry-wrapped-bullets",
            "native-bullets",
            "native-header-bullets",
            "ocr-geometry-wrapped",
            "retained-docling",
            "retained-docling-formulas",
            "retained-marker-fast",
            "yolo-geometry",
            "yolo-geometry-wrapped",
            "yolo-normalized-geometry-wrapped",
            "olmocr-image",
            "olmocr-text",
            "olmocr-compact-text",
            "olmocr-4bit-text",
            "olmocr-patch",
            "olmocr-normalized",
            "olmocr-yolo-crop",
            "olmocr-geometry-crop",
            "qwen-image",
            "qwen-text",
            "qwen-patch",
            "qwen-compact-text",
            "qwen-compact-patch",
            "qwen-4bit-compact-patch",
            "qwen-lora-4bit-compact-patch",
        ],
    )
    parser.add_argument("--case", action="append")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--rescore", action="store_true")
    args = parser.parse_args()
    if args.repetitions < 1 or args.max_tokens < 1:
        parser.error("repetitions and max-tokens must be positive")
    bundles: list[dict[str, Any]] = prepare() if args.prepare else json.loads((ARTIFACTS / "manifest.json").read_text())
    if args.case:
        unknown = set(args.case) - {bundle["name"] for bundle in bundles}
        if unknown:
            parser.error(f"unknown cases: {sorted(unknown)}")
        bundles = [bundle for bundle in bundles if bundle["name"] in args.case]
    report: dict[str, Any] = (
        json.loads(REPORT.read_text())
        if REPORT.exists()
        else {
            "metadata": {
                "started_at": datetime.now(timezone.utc).isoformat(),
                "environment": platform.platform(),
                "python": platform.python_version(),
                "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),  # noqa: S607
                "remote_spend_authorized_usd": 15,
                "remote_spend_usd": 0,
                "runs": [],
            },
            "results": [],
        }
    )
    if args.rescore:
        rescore(report)
        return
    for adapter in args.adapter or []:
        pending = [
            bundle
            for bundle in bundles
            if args.force
            or not any(
                row["case"] == bundle["name"] and row["adapter"] == adapter and row["sha256"] == bundle["sha256"]
                for row in report["results"]
            )
        ]
        if not pending:
            continue
        engine = Engines(adapter, args.device)
        run_index = len(report["metadata"]["runs"])
        report["metadata"]["runs"].append(
            {
                "adapter": adapter,
                "initialization_seconds": engine.initialization_seconds,
                "repetitions": args.repetitions,
                "device": args.device,
                "max_tokens": args.max_tokens,
                "model": engine.model_path,
                "versions": {dist.metadata["Name"]: dist.version for dist in metadata.distributions()},
                "source_files_sha256": {
                    path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                    for path in (ROOT / "bench").glob("structure*.py")
                },
                "started_at": datetime.now(timezone.utc).isoformat(),
            }
        )
        for bundle in pending:
            result = {"case": bundle["name"], "adapter": adapter, "sha256": bundle["sha256"], "run_index": run_index}
            start = time.perf_counter()
            try:
                outputs = []
                timings = []
                for _ in range(args.repetitions):
                    tick = time.perf_counter()
                    outputs.append(run_adapter(bundle, engine, args.max_tokens))
                    timings.append(time.perf_counter() - tick)
                output = outputs[0]
                visible = visible_text(output["markdown"])
                span_parser = HtmlTables()
                span_parser.feed(output["markdown"])
                (ARTIFACTS / bundle["name"] / f"{adapter}.md").write_text(output["markdown"])
                result.update(
                    {
                        "median_seconds": statistics.median(timings),
                        "seconds": timings,
                        "repeatable": all(item["markdown"] == output["markdown"] for item in outputs),
                        "score": score_tables(output["tables"], bundle["expected_tables"]),
                        "literal_checks": {text: text in visible for text in bundle["expected_text"]},
                        "source_agreement": source_agreement(output["markdown"], bundle["words"]),
                        "record_checks": score_records(output["tables"], RECORD_REFERENCES.get(bundle["name"], {})),
                        "merged_spans_exact": list(map(list, span_parser.spans)) == bundle["expected_spans"],
                        "output_sha256": hashlib.sha256(output["markdown"].encode()).hexdigest(),
                        "output": {key: value for key, value in output.items() if key != "markdown"},
                    }
                )
                if "retained_result" in output:
                    prior = output["retained_result"]
                    result.update(
                        {
                            "median_seconds": prior["median_ms"] / 1000,
                            "replay_seconds": timings,
                            "repeatable": prior["repeatable"],
                            "timing_provenance": "original CPU model run",
                        }
                    )
            except Exception as error:
                result.update(
                    {"error": f"{type(error).__name__}: {error}", "elapsed_seconds": time.perf_counter() - start}
                )
                (ARTIFACTS / bundle["name"] / f"{adapter}-error.txt").write_text(traceback.format_exc())
            result["process_peak_rss_kib"] = importlib.import_module("resource").getrusage(0).ru_maxrss
            report["results"] = [
                row for row in report["results"] if not (row["case"] == bundle["name"] and row["adapter"] == adapter)
            ] + [result]
            write_json(REPORT, report)
            REPORT.with_suffix(".md").write_text(format_report(report))
            print(f"{adapter}: {bundle['name']}: {result.get('score', result.get('error'))}", flush=True)
        del engine
        if adapter.startswith(("olmocr", "yolo", "qwen")):
            importlib.import_module("torch").cuda.empty_cache()


if __name__ == "__main__":
    main()

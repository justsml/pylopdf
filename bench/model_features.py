"""Run optional CPU model converters against the exact rich-feature inputs.

Use the isolated environment documented in bench/MODEL_BENCHMARKS.md.
Existing measurements are retained with their original run provenance.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import io
import json
import os
import platform
import subprocess
import time
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

from bench.feature_cases import ROOT, FeatureCase, build_cases
from bench.features import Adapter, format_report, run_case


def docling_converter(*, formulas: bool, threads: int) -> Any:  # noqa: ANN401
    """Initialize the public PDF pipeline before measured conversions."""
    accelerator_device = importlib.import_module("docling.datamodel.accelerator_options").AcceleratorDevice
    accelerator_options = importlib.import_module("docling.datamodel.accelerator_options").AcceleratorOptions
    input_format = importlib.import_module("docling.datamodel.base_models").InputFormat
    pdf_pipeline_options = importlib.import_module("docling.datamodel.pipeline_options").PdfPipelineOptions
    document_converter = importlib.import_module("docling.document_converter").DocumentConverter
    pdf_format_option = importlib.import_module("docling.document_converter").PdfFormatOption

    options = pdf_pipeline_options(
        do_ocr=False,
        do_formula_enrichment=formulas,
        generate_picture_images=True,
        accelerator_options=accelerator_options(device=accelerator_device.CPU, num_threads=threads),
    )
    converter = document_converter(format_options={input_format.PDF: pdf_format_option(pipeline_options=options)})
    converter.initialize_pipeline(input_format.PDF)
    return converter


def marker_converter() -> Any:  # noqa: ANN401
    """Use Marker's CPU fast mode with all OCR and hosted LLM calls disabled."""
    pdf_converter = importlib.import_module("marker.converters.pdf").PdfConverter
    create_model_dict = importlib.import_module("marker.models").create_model_dict

    return pdf_converter(
        artifact_dict=create_model_dict(),
        config={"mode": "fast", "disable_ocr": True, "use_llm": False, "disable_tqdm": True, "pdftext_workers": 1},
    )


def model_manifest() -> list[dict[str, Any]]:
    """Fingerprint cached model inputs without retaining weights in the repository."""
    hf_hub_cache = importlib.import_module("huggingface_hub.constants").HF_HUB_CACHE

    records = []
    for snapshot in sorted(Path(hf_hub_cache).glob("models--*/snapshots/*")):
        for path in sorted(snapshot.rglob("*")):
            if not path.is_file():
                continue
            digest = hashlib.sha256()
            with path.open("rb") as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    digest.update(chunk)
            records.append(
                {
                    "repository": snapshot.parent.parent.name.removeprefix("models--").replace("--", "/"),
                    "revision": snapshot.name,
                    "file": str(path.relative_to(snapshot)),
                    "bytes": path.stat().st_size,
                    "sha256": digest.hexdigest(),
                }
            )
    return records


def conversion_call(context: dict[str, Any]) -> Callable[[bytes], str]:
    """Bind one converter and retain its first complete result for artifacts."""
    name = context["name"]
    converter = context["converter"]
    initialization_error = context["error"]
    retained = context["retained"]

    def convert(data: bytes) -> str:
        if initialization_error:
            raise RuntimeError(initialization_error)
        if name == "marker-fast":
            text_from_rendered = importlib.import_module("marker.output").text_from_rendered

            rendered = converter(io.BytesIO(data))
            text, _, images = text_from_rendered(rendered)
            if not retained:
                retained.update({"images": images, "structured": rendered})
        else:
            document_stream = importlib.import_module("docling.datamodel.base_models").DocumentStream
            image_ref_mode = importlib.import_module("docling_core.types.doc").ImageRefMode

            result = converter.convert(document_stream(name="fixture.pdf", stream=io.BytesIO(data)))
            text = result.document.export_to_markdown(image_mode=image_ref_mode.EMBEDDED)
            if not retained:
                retained["structured"] = result.document
        return str(text)

    return convert


def retain_artifacts(result: dict[str, Any], retained: dict[str, Any], leaf: Path) -> None:
    """Serialize native structure and save referenced images outside conversion timing."""
    structured = retained["structured"]
    payload = (
        structured.model_dump_json(indent=2) if result["adapter"] == "marker-fast" else structured.export_to_dict()
    )
    serialized = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False, indent=2)
    structured_path = leaf / "structured.json"
    structured_path.write_text(serialized, encoding="utf-8")
    result["structured_output"] = str(Path(leaf.name) / structured_path.name)
    result["structured_sha256"] = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    result["image_assets"] = []
    for filename, image in retained.get("images", {}).items():
        if Path(filename).name != filename:
            message = f"Unexpected image filename: {filename}"
            raise RuntimeError(message)
        image_path = leaf / filename
        image.save(image_path)
        result["image_assets"].append(
            {
                "path": str(Path(leaf.name) / filename),
                "sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
            }
        )


def validate_inputs(report: dict[str, Any], cases: dict[str, FeatureCase]) -> None:
    """Reject different fixture bytes before starting any model pipeline."""
    for record in report["cases"]:
        case = cases[record["name"]]
        if hashlib.sha256(case.data).hexdigest() != record["input_sha256"]:
            message = f"Input differs from base report: {case.name}"
            raise RuntimeError(message)


def main() -> None:
    """Append model observations only after matching each source PDF hash."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=ROOT / "bench/results/features-latest.json")
    parser.add_argument("--output", type=Path, default=ROOT / "bench/results/features-models.json")
    parser.add_argument("--adapter", action="append", choices=["docling", "docling-formulas", "marker-fast"])
    parser.add_argument("--repetitions", type=int, default=3)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--case", action="append")
    args = parser.parse_args()
    if args.repetitions < 1 or args.threads < 1 or args.output.suffix != ".json":
        parser.error("use positive repetitions/threads and a .json output")
    os.environ["OMP_NUM_THREADS"] = str(args.threads)
    os.environ["MKL_NUM_THREADS"] = str(args.threads)
    os.environ["TORCH_DEVICE"] = "cpu"
    os.environ["FAST_LAYOUT_NUM_THREADS"] = str(args.threads)
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    torch = importlib.import_module("torch")

    torch.set_num_threads(args.threads)
    report = json.loads(args.base.read_text(encoding="utf-8"))
    names = args.adapter or ["docling", "docling-formulas", "marker-fast"]
    cases = {case.name: case for case in build_cases()}
    if args.case and set(args.case) - cases.keys():
        parser.error("unknown case name")
    if args.case:
        report["cases"] = [record for record in report["cases"] if record["name"] in args.case]
    validate_inputs(report, cases)
    output_dir = args.output.parent / "feature-outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()  # noqa: S607
    run = {
        "Run at": datetime.now(timezone.utc).isoformat(),
        "Source commit": commit,
        "Source dirty": bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)),  # noqa: S607
        "Environment": f"{platform.platform()} / Python {platform.python_version()}",
        "Versions": {distribution.metadata["Name"]: distribution.version for distribution in metadata.distributions()},
        "Repetitions": args.repetitions,
        "CPU threads": args.threads,
        "OCR": "disabled; Docling formula enrichment is separately enabled in docling-formulas",
        "Hosted LLM": "disabled",
    }
    report.setdefault("additional_runs", []).append(run)
    report["metadata"]["Additional model runs"] = "See additional_runs and per-result run_index in JSON"
    for name in names:
        start = time.perf_counter()
        try:
            converter = (
                marker_converter()
                if name == "marker-fast"
                else docling_converter(formulas=name == "docling-formulas", threads=args.threads)
            )
            initialization_error = None
        except Exception as exc:
            converter = None
            initialization_error = f"{type(exc).__name__}: {exc}"
        initialization_ms = (time.perf_counter() - start) * 1000
        print(f"{name}: initialized in {initialization_ms:.1f} ms; error={initialization_error}", flush=True)
        for record in report["cases"]:
            case = cases[record["name"]]
            leaf = output_dir / f"{case.name}--{name}"
            leaf.mkdir(parents=True, exist_ok=True)
            retained: dict[str, Any] = {}

            convert = conversion_call(
                {"name": name, "converter": converter, "error": initialization_error, "retained": retained}
            )

            options = (
                "mode='fast'; disable_ocr=True (including equations); use_llm=False; extracted image files"
                if name == "marker-fast"
                else f"CPU; do_ocr=False; do_formula_enrichment={name == 'docling-formulas'}; embedded picture images"
            )
            result = run_case(case, Adapter(name, "markdown", options, convert), args.repetitions, leaf)
            result.update({"run_index": len(report["additional_runs"]) - 1, "initialization_ms": initialization_ms})
            if result["status"] == "ok":
                result["raw_output"] = str(Path(leaf.name) / result["raw_output"])
                retain_artifacts(result, retained, leaf)
            record["results"] = [item for item in record["results"] if item["adapter"] != name] + [result]
            print(f"{case.name} / {name}: {result['status']}", flush=True)
            args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    run["Model files"] = model_manifest()
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.output.with_suffix(".md").write_text(format_report(report, output_dir.name), encoding="utf-8")


if __name__ == "__main__":
    main()

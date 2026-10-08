"""Optional hosted vision controls with a separate, conservative spending ledger."""

from __future__ import annotations

import base64
import io
import json
import shlex
import time
import urllib.error
import urllib.request
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pathlib import Path

QWEN_HOSTED = "qwen/qwen3-vl-235b-a22b-instruct"
_API_BUDGET = 1.50
_REQUEST_RESERVE = 0.25
_MAX_PROMPT_BYTES = 200_000
_MAX_IMAGE_SIDE = 1288
_TABLE_THRESHOLD = 0.5


class HostedVision:
    """Retain provider usage and reserve cost before sending a metered request."""

    def __init__(self, root: Path, *, router: bool) -> None:
        """Read only the required credential; never retain it in benchmark artifacts."""
        self.root = root
        self.router = router
        self.model = "typesafe/jev-router" if router else QWEN_HOSTED
        values = {}
        for line in (root / ".env.remote-hosts").read_text().splitlines():
            if "=" not in line or line.lstrip().startswith("#"):
                continue
            key, value = line.split("=", 1)
            parts = shlex.split(value, comments=True)
            if parts:
                values[key.strip().removeprefix("export ")] = parts[0]
        self.key = values["OPENROUTER_API_KEY"]
        self.ledger = root / "bench/results/structure-artifacts/hosted-ledger.json"
        self.responses = self.ledger.parent / "hosted-responses"
        self.responses.mkdir(exist_ok=True)

    def checkpoint(self, value: dict[str, Any]) -> None:
        """Atomically persist charges and reservations before another request."""
        temporary = self.ledger.with_suffix(".json.tmp")
        temporary.write_text(json.dumps(value, indent=2) + "\n")
        temporary.replace(self.ledger)

    def request(self, endpoint: str, body: dict[str, Any]) -> dict[str, Any]:
        """No automatic retries; uncertain charges keep their reserved upper bound."""
        ledger: dict[str, Any] = (
            json.loads(self.ledger.read_text()) if self.ledger.exists() else {"requests": [], "budget_usd": _API_BUDGET}
        )
        charged = sum(row["accounted_usd"] for row in ledger["requests"])
        if charged + _REQUEST_RESERVE > _API_BUDGET:
            msg = "hosted study's $1.50 budget would be exceeded by another request reservation"
            raise ValueError(msg)
        index = len(ledger["requests"])
        entry: dict[str, Any] = {
            "model": body["model"],
            "started_at": time.time(),
            "accounted_usd": _REQUEST_RESERVE,
            "cost_status": "reserved; unknown until provider usage is retained",
        }
        ledger["requests"].append(entry)
        self.checkpoint(ledger)
        request = urllib.request.Request(
            "https://openrouter.ai/api/" + endpoint,
            data=json.dumps(body).encode(),
            headers={
                "Authorization": "Bearer " + self.key,
                "Content-Type": "application/json",
                "X-OpenRouter-Metadata": "enabled",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:  # noqa: S310
                result = json.load(response)
        except urllib.error.HTTPError as error:
            entry["http_status"] = error.code
            self.checkpoint(ledger)
            msg = f"hosted provider rejected request: HTTP {error.code}; no credential/error body retained"
            raise RuntimeError(msg) from None
        (self.responses / f"{index:03d}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
        cost = result.get("usage", {}).get("cost")
        if isinstance(cost, (int, float)) and cost >= 0:
            entry.update(
                {"accounted_usd": cost, "cost_status": "provider-reported USD", "generation_id": result.get("id")}
            )
        entry["completed_at"] = time.time()
        self.checkpoint(ledger)
        result["ledger_index"] = index
        return result

    def generate(self, image: Any, prompt: str, limit: int) -> tuple[str, dict[str, Any]]:  # noqa: ANN401
        """Send the prepared screenshot and exactly the retained experimental prompt."""
        if len(prompt.encode()) > _MAX_PROMPT_BYTES or max(image.size) > _MAX_IMAGE_SIDE:
            msg = "hosted request exceeds the study's input/image budget"
            raise ValueError(msg)
        stream = io.BytesIO()
        image.save(stream, format="PNG")
        data_url = "data:image/png;base64," + base64.b64encode(stream.getvalue()).decode()
        body: dict[str, Any] = {
            "model": self.model,
            "temperature": 0,
            "max_tokens": limit,
            "provider": {"max_price": {"prompt": 1, "completion": 4}},
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": data_url}},
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
        }
        if self.router:
            body["plugins"] = [{"id": "jev-router", "models": ["qwen/*"]}]
        result = self.request("v1/chat/completions", body)
        choice = result["choices"][0]
        usage = result.get("usage", {})
        return choice["message"]["content"], {
            "input_tokens": usage.get("prompt_tokens"),
            "output_tokens": usage.get("completion_tokens"),
            "truncated": choice.get("finish_reason") == "length",
            "generation_id": result.get("id"),
            "provider": result.get("provider"),
            "served_model": result.get("model"),
            "usage": usage,
            "router_metadata": result.get("openrouter_metadata"),
            "ledger_index": result["ledger_index"],
            "cost_scope": "metered API control; separate from local/remote GPU timings",
        }


def gated_geometry(bundle: dict[str, Any], client: HostedVision) -> dict[str, Any]:
    """Use text-only Jev for a typed table decision, then assemble unchanged source IDs."""
    from bench.structure import ARTIFACTS, write_json  # noqa: PLC0415
    from bench.structure_core import geometry_tables, render_tables, validate_patch  # noqa: PLC0415

    words = bundle["words"]
    payload = {"tables": [{"rows": table} for table in geometry_tables(words, wrapped=True)]}
    body = {
        "model": "typesafe/jev-1.13",
        "state": {
            "word_format": ["id", "x0", "y0", "x1", "y1", "text"],
            "source_words": [
                [word["id"], *[round(v, 1) for v in word["logical_bbox"]], word["text"]] for word in words
            ],
            "candidate_tables": payload["tables"],
        },
        "questions": {
            "has_table": {
                "type": "noul",
                "instructions": "The source words contain a table of related records or measurements with shared "
                "columns. Aligned independent prose paragraphs, equations, headings, footnotes and lists "
                "are not tables. "
                "Use source_words and candidate_tables as evidence; the geometric candidates may be false positives.",
            }
        },
    }
    directory = ARTIFACTS / bundle["name"]
    write_json(directory / "jev-text-gated-geometry-wrapped-request.json", body)
    result = client.request("alpha/decisions", body)
    (directory / "jev-text-gated-geometry-wrapped-raw.txt").write_text(json.dumps(result, indent=2))
    probability = result["answers"]["has_table"]["noul"]
    if probability < _TABLE_THRESHOLD:
        payload = {"tables": []}
    matrices, used = validate_patch(payload, words)
    write_json(directory / "jev-text-gated-geometry-wrapped-patch.json", payload)
    return {
        "markdown": render_tables(matrices)
        + "\n\n"
        + " ".join(word["text"] for word in words if word["id"] not in used),
        "tables": matrices,
        "decision": result,
        "decision_threshold": _TABLE_THRESHOLD,
        "decision_scope": "text-only Jev; uncalibrated threshold; cannot recover missing OCR or generate cells",
    }

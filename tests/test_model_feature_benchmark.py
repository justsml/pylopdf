from __future__ import annotations

import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest
from bench.feature_cases import FeatureCase
from bench.features import inspect_output
from bench.model_features import conversion_call, retain_artifacts, validate_inputs


def test_model_study_refuses_changed_input() -> None:
    case = FeatureCase("fixture", b"original PDF", (), "", ())
    report = {"cases": [{"name": case.name, "input_sha256": hashlib.sha256(case.data).hexdigest()}]}
    validate_inputs(report, {case.name: case})
    changed = FeatureCase("fixture", b"different PDF", (), "", ())
    with pytest.raises(RuntimeError, match="Input differs"):
        validate_inputs(report, {changed.name: changed})


def test_model_artifacts_keep_warmup_images_and_structure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    rendered = [SimpleNamespace(text="![image](figure.png)", sequence=index) for index in range(2)]
    image = SimpleNamespace(save=lambda path: path.write_bytes(b"image payload"))
    module = SimpleNamespace(text_from_rendered=lambda value: (value.text, "md", {"figure.png": image}))
    monkeypatch.setattr("bench.model_features.importlib.import_module", lambda _: module)
    retained: dict[str, Any] = {}
    convert = conversion_call(
        {"name": "marker-fast", "converter": lambda _: rendered.pop(0), "error": None, "retained": retained}
    )
    assert convert(b"PDF") == convert(b"PDF")
    assert retained["structured"].sequence == 0
    retained["structured"] = SimpleNamespace(model_dump_json=lambda **_: json.dumps({"page": 1}))
    result: dict[str, Any] = {"adapter": "marker-fast"}
    retain_artifacts(result, retained, tmp_path)
    assert json.loads((tmp_path / "structured.json").read_text()) == {"page": 1}
    assert result["image_assets"][0]["sha256"] == hashlib.sha256(b"image payload").hexdigest()
    assert (tmp_path / "figure.png").read_bytes() == b"image payload"


def test_explicit_internal_link_requires_a_real_anchor() -> None:
    case = FeatureCase("fixture", b"PDF", (), "", ())
    output = '[next](#page-1-0) [missing](#absent)\n\n<span id="page-1-0"></span>Destination'
    pytest.importorskip("markdown_it")
    pytest.importorskip("mdit_py_plugins")
    syntax = inspect_output(output, "markdown", case)["syntax"]
    assert syntax["internal_link_targets"] == {"#page-1-0": True, "#absent": False}

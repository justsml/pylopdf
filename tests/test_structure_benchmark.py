from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from bench import structure
from bench.feature_cases import FeatureCase, page_pdf, text_op
from bench.structure_cases import StructureCase
from bench.structure_core import markdown_tables, render_tables, score_tables, validate_patch


def source_words() -> list[dict[str, Any]]:
    return [{"id": "a", "text": "Heading"}, {"id": "b", "text": "42.00"}]


@pytest.mark.parametrize(
    "payload",
    [
        {"tables": [{"rows": [[["missing"]]]}]},
        {"tables": [{"rows": [[["a"], ["a"]]]}]},
        {"tables": [{"rows": [[["a"]], [["b"], []]]}]},
        {"tables": [{"rows": [[["a"], ["b"]]], "spans": [[0, 0, 1, 2]]}]},
        {"tables": [{"rows": [[["a"]]], "spans": [[0, 0, 2, 1]]}]},
    ],
)
def test_patch_rejects_content_or_geometry_corruption(payload: dict[str, Any]) -> None:
    with pytest.raises(ValueError, match=r"unknown|duplicated|ragged|span"):
        validate_patch(payload, source_words())


def test_merged_patch_expands_anchor_without_reusing_source_ids() -> None:
    matrix, used = validate_patch(
        {"tables": [{"rows": [[["a"], []], [["b"], []]], "spans": [[0, 0, 1, 2]]}]},
        source_words(),
    )
    assert matrix == [[["Heading", "Heading"], ["42.00", ""]]]
    assert used == {"a", "b"}
    pytest.importorskip("markdown_it")
    rendered = render_tables(matrix, spans=[[[0, 0, 1, 2]]])
    assert 'colspan="2"' in rendered
    assert markdown_tables(rendered) == matrix


def test_table_score_detects_swapped_values_and_extra_tables() -> None:
    gold = ((("Name", "Amount"), ("Alpha", "42"), ("Beta", "7")),)
    swapped = [[["Name", "Amount"], ["Alpha", "7"], ["Beta", "42"]]]
    score = score_tables(swapped, gold)
    assert score["correct_cells"] == 4
    assert not score["exact"]
    assert score["relationship_matches"] < score["relationship_expected"]
    assert not score_tables([[list(row) for row in gold[0]], [["extra"]]], gold)["exact"]
    assert not score_tables(swapped, ())["exact"]


def test_parsing_preserves_literals_empty_cells_and_html_spans() -> None:
    pytest.importorskip("markdown_it")
    markdown = "| Left | Center | Right |\n| --- | --- | --- |\n| Alpha | A\\|B | 42 |\n| Beta | C\\\\D | |"
    assert markdown_tables(markdown) == [
        [["Left", "Center", "Right"], ["Alpha", "A|B", "42"], ["Beta", "C\\D", ""]],
    ]
    table = '<table><tr><th colspan="2">Heading</th></tr><tr><td>A &amp; B</td><td>42</td></tr></table>'
    assert markdown_tables(table) == [[["Heading", "Heading"], ["A & B", "42"]]]
    assert markdown_tables(f"```html\n{table}\n```") == []
    assert markdown_tables("| Heading |\n| --- |\n| First<br>second |") == [[["Heading"], ["First second"]]]


def test_bullet_fallback_preserves_empty_value_and_escaping() -> None:
    assert render_tables([[["Name", "Amount"], ["Alpha", "42.00"], ["Beta", ""]]], bullets=True) == (
        "- Name: Alpha; Amount: 42.00\n- Name: Beta; Amount: "
    )


def test_screenshot_is_opaque_and_orientation_follows_display_text(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    image = pytest.importorskip("PIL.Image")
    data = page_pdf("0 1 -1 0 600 200 cm\n" + text_op("Upright display", 40, 200), extra_page="/Rotate 90")
    case = StructureCase(FeatureCase("counter-rotated", data, (), ""))
    monkeypatch.setattr(structure, "ARTIFACTS", tmp_path)
    monkeypatch.setattr(structure, "build_structure_cases", lambda: [case])
    bundle = structure.prepare()[0]
    assert bundle["rotation"] == 90
    assert bundle["orientation"] == 0
    assert bundle["words"]
    screenshot = image.open(tmp_path / "counter-rotated/page.png")
    assert screenshot.getpixel((0, 0)) == (255, 255, 255, 255)

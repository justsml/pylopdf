"""Experimental geometry recovery, source-backed patches, and cell-level scoring."""

from __future__ import annotations

import html
import re
import statistics
from collections import Counter
from html.parser import HTMLParser
from importlib import import_module
from itertools import pairwise
from typing import Any

_MAX_TABLES = 64
_MAX_AXIS = 128
_MIN_COLUMNS = 2
_MIN_SUPPORT_ROWS = 3


def normalized(text: str) -> str:
    """Compare exact characters while ignoring layout whitespace."""
    return " ".join(text.split())


class VisibleText(HTMLParser):
    """Read rendered text without Markdown escape or HTML entity artifacts."""

    def __init__(self) -> None:
        """Initialize retained text fragments."""
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        """Preserve characters inside inline markup."""
        self.parts.append(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:  # noqa: ARG002
        """Separate cells and blocks without splitting emphasis inside words."""
        if tag in {"p", "tr", "td", "th", "li", "br", "h1", "h2", "h3", "h4"}:
            self.parts.append(" ")


def visible_text(markdown: str) -> str:
    """Resolve Markdown escaping and inline markup before literal checks."""
    parser = VisibleText()
    parser.feed(import_module("markdown_it").MarkdownIt("commonmark").enable("table").render(markdown))
    return normalized("".join(parser.parts))


def source_agreement(markdown: str, words: list[dict[str, Any]]) -> dict[str, Any]:
    """Measure token agreement with the text layer, without calling it ground truth."""
    pattern = r"\w+(?:[.,]\d+)*|[^\w\s]"
    source = Counter(re.findall(pattern, " ".join(word["text"] for word in words)))
    observed = Counter(re.findall(pattern, visible_text(markdown)))
    return {
        "source_tokens": sum(source.values()),
        "output_tokens": sum(observed.values()),
        "matched_tokens": sum((source & observed).values()),
        "extra_tokens": sum((observed - source).values()),
        "missing_tokens": sum((source - observed).values()),
        "interpretation": "agreement with extracted source, not OCR or semantic ground truth",
    }


def markdown_tables(text: str) -> list[list[list[str]]]:
    """Parse GFM and HTML tables, retaining empty cells and merged-slot expansion."""
    tokens = import_module("markdown_it").MarkdownIt("commonmark").enable("table").parse(text)
    tables: list[list[list[str]]] = []
    row: list[str] | None = None
    in_cell = False
    for token in tokens:
        if token.type == "table_open":
            tables.append([])
        elif token.type == "tr_open":
            row = []
            tables[-1].append(row)
        elif token.type in {"th_open", "td_open"}:
            in_cell = True
        elif token.type in {"th_close", "td_close"}:
            in_cell = False
        elif in_cell and token.type == "inline" and row is not None:
            value = "".join(
                child.content if child.type in {"text", "code_inline"} else " "
                for child in token.children or []
                if child.type in {"text", "code_inline", "softbreak", "hardbreak"}
                or (child.type == "html_inline" and child.content.lower().startswith("<br"))
            )
            row.append(normalized(value))
    parser = HtmlTables()
    parser.feed("\n".join(token.content for token in tokens if token.type == "html_block"))
    return tables + parser.tables


def markdown_spans(text: str) -> list[list[int]]:
    """Observe merged cells in rendered HTML blocks, excluding fenced code."""
    tokens = import_module("markdown_it").MarkdownIt("commonmark").enable("table").parse(text)
    parser = HtmlTables()
    parser.feed("\n".join(token.content for token in tokens if token.type == "html_block"))
    return list(map(list, parser.spans))


def score_records(tables: list[list[list[str]]], references: dict[str, dict[int, str]]) -> dict[str, Any]:
    """Check independently annotated source records at their logical column positions."""
    details = {}
    correct = 0
    total = 0
    for anchor, cells in references.items():
        candidates = [row for table in tables for row in table if any(normalized(cell) == anchor for cell in row)]
        checks = {}
        for column, value in cells.items():
            checks[str(column)] = any(column < len(row) and normalized(row[column]) == value for row in candidates)
        correct += sum(checks.values())
        total += len(checks)
        details[anchor] = checks
    return {
        "correct": correct,
        "total": total,
        "records": details,
        "interpretation": "visual spot checks, not complete corpus table accuracy",
    }


class HtmlTables(HTMLParser):
    """Expand rowspan/colspan without silently losing covered slots."""

    def __init__(self) -> None:
        """Initialize one flat HTML table parser."""
        super().__init__()
        self.tables: list[list[list[str]]] = []
        self.slots: dict[tuple[int, int], str] | None = None
        self.row = -1
        self.column = 0
        self.cell: tuple[int, int, int] | None = None
        self.parts: list[str] = []
        self.spans: list[tuple[int, int, int, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Record table geometry from HTML attributes."""
        if tag == "table":
            self.slots = {}
            self.row = -1
        elif tag == "tr" and self.slots is not None:
            self.row += 1
            self.column = 0
        elif tag in {"td", "th"} and self.slots is not None:
            while (self.row, self.column) in self.slots:
                self.column += 1
            attributes = dict(attrs)
            rowspan = min(128, max(1, int(attributes.get("rowspan") or 1)))
            colspan = min(128, max(1, int(attributes.get("colspan") or 1)))
            self.cell = (self.column, rowspan, colspan)
            if rowspan > 1 or colspan > 1:
                self.spans.append((self.row, self.column, rowspan, colspan))
            self.parts = []
        elif tag == "br" and self.cell is not None:
            self.parts.append(" ")

    def handle_data(self, data: str) -> None:
        """Retain complete cell text."""
        if self.cell is not None:
            self.parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        """Materialize every covered slot at the cell anchor."""
        if tag in {"td", "th"} and self.cell is not None and self.slots is not None:
            column, rowspan, colspan = self.cell
            for row in range(self.row, self.row + rowspan):
                for col in range(column, column + colspan):
                    self.slots[row, col] = normalized("".join(self.parts))
            self.column += colspan
            self.cell = None
        elif tag == "table" and self.slots is not None:
            if self.slots:
                height = max(row for row, _ in self.slots) + 1
                width = max(col for _, col in self.slots) + 1
                self.tables.append([[self.slots.get((r, c), "") for c in range(width)] for r in range(height)])
            self.slots = None


def geometry_tables(  # noqa: C901, PLR0912
    words: list[dict[str, Any]],
    *,
    wrapped: bool = False,
) -> list[list[list[list[str]]]]:
    """Recover physical rows before column grouping, without reference answers."""
    if not words:
        return []
    height = statistics.median(word["logical_bbox"][3] - word["logical_bbox"][1] for word in words)
    rows: list[list[dict[str, Any]]] = []
    for word in sorted(words, key=lambda w: (w["logical_bbox"][1], w["logical_bbox"][0])):
        if not rows or abs(word["logical_bbox"][1] - rows[-1][0]["logical_bbox"][1]) > height * 0.45:
            rows.append([])
        rows[-1].append(word)
    segments: list[list[list[dict[str, Any]]]] = []
    for row in rows:
        parts: list[list[dict[str, Any]]] = []
        for word in sorted(row, key=lambda w: w["logical_bbox"][0]):
            if not parts or word["logical_bbox"][0] - parts[-1][-1]["logical_bbox"][2] > height * 1.5:
                parts.append([])
            parts[-1].append(word)
        segments.append(parts)
    tables = []
    cursor = 0
    while cursor < len(segments):
        if len(segments[cursor]) < _MIN_COLUMNS:
            cursor += 1
            continue
        start = cursor
        run = [segments[cursor]]
        cursor += 1
        while cursor < len(segments):
            gap = rows[cursor][0]["logical_bbox"][1] - rows[cursor - 1][0]["logical_bbox"][1]
            if gap > height * 5 or (len(segments[cursor]) < _MIN_COLUMNS and not wrapped):
                break
            run.append(segments[cursor])
            cursor += 1
        if sum(len(row) >= _MIN_COLUMNS for row in run) < _MIN_SUPPORT_ROWS:
            continue
        anchors = max(run, key=len)
        cuts = [(left[-1]["logical_bbox"][2] + right[0]["logical_bbox"][0]) / 2 for left, right in pairwise(anchors)]
        matrix: list[list[list[str]]] = []
        for index, segmented_row in enumerate(run):
            cells: list[list[str]] = [[] for _ in anchors]
            for part in segmented_row:
                column = sum(part[0]["logical_bbox"][0] > cut for cut in cuts)
                cells[column].extend(word["id"] for word in part)
            # A short continuation without a record key belongs to the preceding record.
            gap = (
                0
                if index == 0
                else rows[start + index][0]["logical_bbox"][1] - rows[start + index - 1][0]["logical_bbox"][1]
            )
            if wrapped and matrix and not cells[0] and gap < height * 2:
                for column, ids in enumerate(cells):
                    matrix[-1][column].extend(ids)
            else:
                matrix.append(cells)
        tables.append(matrix)
    return tables


def validate_patch(  # noqa: C901, PLR0912
    payload: dict[str, Any],
    words: list[dict[str, Any]],
) -> tuple[list[list[list[str]]], set[str]]:
    """Reject unknown/duplicate IDs and invalid span geometry before any replacement."""
    if not isinstance(payload, dict):
        msg = "patch root must be a JSON object with a tables list"
        raise TypeError(msg)
    source = {word["id"]: word["text"] for word in words}
    consumed: set[str] = set()
    matrices = []
    tables = payload.get("tables")
    if not isinstance(tables, list) or len(tables) > _MAX_TABLES:
        msg = "patch tables must be a bounded list"
        raise ValueError(msg)
    for table in tables:
        rows = table["rows"]
        if not rows or len(rows) > _MAX_AXIS or not rows[0] or len(rows[0]) > _MAX_AXIS:
            msg = "patch table has invalid dimensions"
            raise ValueError(msg)
        width = len(rows[0])
        matrix = []
        for row in rows:
            if len(row) != width:
                msg = "patch table is ragged"
                raise ValueError(msg)
            values = []
            for ids in row:
                if not isinstance(ids, list):
                    msg = "each cell must contain a list of source word IDs"
                    raise TypeError(msg)
                for word_id in ids:
                    if word_id not in source or word_id in consumed:
                        msg = f"unknown or duplicated source ID: {word_id}"
                        raise ValueError(msg)
                    consumed.add(word_id)
                values.append(" ".join(source[word_id] for word_id in ids))
            matrix.append(values)
        covered: set[tuple[int, int]] = set()
        for row, column, rowspan, colspan in table.get("spans", []):
            if (
                min(row, column) < 0
                or min(rowspan, colspan) < 1
                or row + rowspan > len(rows)
                or column + colspan > width
            ):
                msg = "patch span is outside its table"
                raise ValueError(msg)
            value = matrix[row][column]
            for r in range(row, row + rowspan):
                for c in range(column, column + colspan):
                    if (r, c) in covered or ((r, c) != (row, column) and rows[r][c]):
                        msg = "patch spans overlap or cover nonempty cells"
                        raise ValueError(msg)
                    covered.add((r, c))
                    matrix[r][c] = value
        matrices.append(matrix)
    return matrices, consumed


def render_tables(
    matrices: list[list[list[str]]],
    *,
    bullets: bool = False,
    spans: list[list[list[int]]] | None = None,
) -> str:
    """Render identical cells as either HTML tables or labeled records."""
    blocks = []
    for table_index, matrix in enumerate(matrices):
        if bullets:
            blocks.append(
                "\n".join(
                    "- "
                    + "; ".join(
                        f"{header or f'Column {i + 1}'}: {value}"
                        for i, (header, value) in enumerate(zip(matrix[0], row, strict=True))
                    )
                    for row in matrix[1:]
                )
            )
        else:
            anchors = {(r, c): (rs, cs) for r, c, rs, cs in (spans[table_index] if spans else [])}
            covered = {
                (r, c)
                for (row, col), (rs, cs) in anchors.items()
                for r in range(row, row + rs)
                for c in range(col, col + cs)
                if (r, c) != (row, col)
            }
            rows = []
            for r, row in enumerate(matrix):
                cells = []
                for c, value in enumerate(row):
                    if (r, c) in covered:
                        continue
                    rs, cs = anchors.get((r, c), (1, 1))
                    attributes = f' rowspan="{rs}" colspan="{cs}"' if (r, c) in anchors else ""
                    cells.append(f"<td{attributes}>{html.escape(value)}</td>")
                rows.append("<tr>" + "".join(cells) + "</tr>")
            blocks.append("<table>\n" + "\n".join(rows) + "\n</table>")
    return "\n\n".join(blocks)


def score_tables(actual: list[list[list[str]]], expected: tuple[Any, ...] | None) -> dict[str, Any]:  # noqa: C901
    """Score cell positions, exact matrices, and horizontal/vertical relationships."""
    if expected is None:
        return {"gold_available": False, "tables": len(actual)}
    gold = [[[normalized(cell) for cell in row] for row in table] for table in expected]
    observed = [[[normalized(cell) for cell in row] for row in table] for table in actual]
    total = sum(len(row) for table in gold for row in table)
    correct = 0
    for t, table in enumerate(gold):
        for r, row in enumerate(table):
            for c, value in enumerate(row):
                correct += (
                    t < len(observed)
                    and r < len(observed[t])
                    and c < len(observed[t][r])
                    and value == observed[t][r][c]
                )

    def relationships(tables: list[list[list[str]]]) -> Counter[tuple[str, str, str]]:
        edges: Counter[tuple[str, str, str]] = Counter()
        for table in tables:
            for r, row in enumerate(table):
                for c, value in enumerate(row):
                    if c + 1 < len(row):
                        edges["right", value, row[c + 1]] += 1
                    if r + 1 < len(table) and c < len(table[r + 1]):
                        edges["below", value, table[r + 1][c]] += 1
        return edges

    wanted, got = relationships(gold), relationships(observed)
    matched = sum((wanted & got).values())
    return {
        "gold_available": True,
        "tables": len(actual),
        "expected_tables": len(gold),
        "exact": observed == gold,
        "correct_cells": correct,
        "total_cells": total,
        "relationship_matches": matched,
        "relationship_expected": sum(wanted.values()),
        "relationship_observed": sum(got.values()),
    }

"""Controlled PDF fixtures for observing Markdown conversion behavior."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pylopdf

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class FeatureCase:
    """An input, its known content, and checks that require human interpretation."""

    name: str
    data: bytes
    features: tuple[str, ...]
    notes: str
    expected_text: tuple[str, ...] = ()
    expected_order: tuple[str, ...] = ()
    reference_math: str | None = None
    source: str = "Repository-authored synthetic PDF; repository MIT license"
    source_values: dict[str, str] = field(default_factory=dict)


def raw_pdf(objects: list[bytes | str]) -> bytes:
    """Serialize consecutive objects with an exact classic xref table."""
    output = bytearray(b"%PDF-1.7\n")
    offsets = [0]
    for number, body in enumerate(objects, start=1):
        offsets.append(len(output))
        encoded = body.encode("latin-1") if isinstance(body, str) else body
        output.extend(f"{number} 0 obj\n".encode("ascii") + encoded + b"\nendobj\n")
    xref_offset = len(output)
    output.extend(f"xref\n0 {len(offsets)}\n0000000000 65535 f \n".encode("ascii"))
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii"),
    )
    return bytes(output)


def stream_object(content: bytes | str, attributes: str = "") -> bytes:
    """Build one stream with an exact byte length."""
    data = content.encode("latin-1") if isinstance(content, str) else content
    return f"<< /Length {len(data)} {attributes} >>\nstream\n".encode("ascii") + data + b"\nendstream"


def text_op(text: str, x: float, y: float, *, size: float = 12, font: str = "F1") -> str:
    """Place WinAnsi text using PDF-space baseline coordinates."""
    escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return f"BT /{font} {size} Tf {x} {y} Td ({escaped}) Tj ET"


def page_pdf(
    content: str, *, extra_page: str = "", extra_catalog: str = "", extras: tuple[bytes | str, ...] = ()
) -> bytes:
    """Build a one-page PDF with regular, bold, italic, and monospace fonts."""
    return raw_pdf(
        [
            f"<< /Type /Catalog /Pages 2 0 R {extra_catalog} >>",
            "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            (
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R "
                f"/Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R /F4 8 0 R >> >> {extra_page} >>"
            ),
            stream_object(content),
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >>",
            "<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>",
            *extras,
        ]
    )


def _table_case(*, bordered: bool, merged: bool = False) -> FeatureCase:
    """Use visible left/center/right placement, formatting, and empty cells."""
    ops = [text_op("Table heading", 40, 710, size=20)]
    if bordered:
        ops.extend(f"40 {y} m 550 {y} l" for y in (660, 620, 580, 540))
        ops.extend(f"{x} 540 m {x} 660 l" for x in (40, 550))
        ops.append("210 540 m 210 620 l" if merged else "210 540 m 210 660 l")
        ops.append("380 540 m 380 660 l")
        ops.append("S")
    ops.extend(
        [
            text_op("Merged header" if merged else "Left", 50, 635, font="F2"),
            text_op("Right", 510, 635, font="F2"),
            text_op("Alpha", 50, 595, font="F3"),
            text_op("A|B", 275, 595),
            text_op("42", 520, 595),
            text_op("Beta", 50, 555),
            text_op("C\\D", 275, 555),
        ]
    )
    if not merged:
        ops.append(text_op("Center", 275, 635, font="F2"))
    name = "table-merged" if merged else "table-bordered" if bordered else "table-borderless"
    return FeatureCase(
        name,
        page_pdf("\n".join(ops)),
        ("tables", "table alignment", "cell emphasis", "cell escaping", "empty cells", "merged cells"),
        "Three rows/columns; last numeric cell is genuinely empty. Alignment is visual geometry, not PDF semantics. "
        "Bold/italic use non-embedded Standard 14 fonts. The merged case spans the first two header slots.",
        ("Alpha", "Beta", "42", "A|B", "C\\D"),
    )


def _links_case() -> FeatureCase:
    """Expose URI, direct page destination, named destination, and an outline."""
    first = "\n".join(
        text_op(text, 40, y)
        for text, y in [
            ("External documentation", 720),
            ("Jump to second page", 680),
            ("Named section", 640),
        ]
    )
    data = raw_pdf(
        [
            "<< /Type /Catalog /Pages 2 0 R /Names << /Dests 10 0 R >> /Outlines 11 0 R >>",
            "<< /Type /Pages /Kids [3 0 R 4 0 R] /Count 2 >>",
            (
                "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 5 0 R "
                "/Resources << /Font << /F1 7 0 R >> >> /Annots [8 0 R 9 0 R 13 0 R] >>"
            ),
            (
                "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 6 0 R "
                "/Resources << /Font << /F1 7 0 R >> >> >>"
            ),
            stream_object(first),
            stream_object(text_op("Destination section", 40, 720, size=18)),
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            "<< /Type /Annot /Subtype /Link /Rect [40 716 200 734] /A << /S /URI /URI (https://example.org/docs) >> >>",
            "<< /Type /Annot /Subtype /Link /Rect [40 676 200 694] /Dest [4 0 R /XYZ 40 720 null] >>",
            "<< /Names [(section-two) [4 0 R /XYZ 40 720 null]] >>",
            "<< /Type /Outlines /First 12 0 R /Last 12 0 R /Count 1 >>",
            "<< /Title (Outline destination) /Parent 11 0 R /Dest [4 0 R /Fit] >>",
            "<< /Type /Annot /Subtype /Link /Rect [40 636 200 654] /Dest (section-two) >>",
        ]
    )
    return FeatureCase(
        "links-and-outline",
        data,
        ("URI links", "internal links", "named destinations", "bookmarks"),
        "Link targets exist only in annotations, not visible text. A bookmark is not body text. "
        "Preserving an internal link requires both a generated destination and a link that resolves to it.",
        ("External documentation", "Jump to second page", "Named section", "Destination section"),
        source_values={"uri": "https://example.org/docs", "named_destination": "section-two"},
    )


def _image_case(*, with_text: bool) -> FeatureCase:
    """Use a real RGB raster and vector diagram; OCR is not applied."""
    ops = "q 200 0 0 150 40 420 cm /Im1 Do Q\n40 360 200 30 re S\n"
    if with_text:
        ops += text_op("Raster caption", 40, 600) + "\n" + text_op("Vector caption", 40, 320)
    data = raw_pdf(
        [
            "<< /Type /Catalog /Pages 2 0 R >>",
            "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            (
                "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R "
                "/Resources << /Font << /F1 5 0 R >> /XObject << /Im1 6 0 R >> >> >>"
            ),
            stream_object(ops),
            "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            stream_object(
                bytes([255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 255, 0]),
                "/Type /XObject /Subtype /Image /Width 2 /Height 2 /ColorSpace /DeviceRGB /BitsPerComponent 8",
            ),
        ]
    )
    return FeatureCase(
        "images-and-vectors" if with_text else "image-only",
        data,
        ("raster images", "vector graphics", "captions", "image-only pages", "OCR"),
        "One 2x2 RGB image enlarged on the page and one stroked rectangle. No OCR text. "
        "An image reference does not establish source-image preservation or correct caption association.",
        ("Raster caption", "Vector caption") if with_text else (),
    )


def _unicode_case() -> FeatureCase:
    """Pin UTF-16BE CMap surrogates and multi-scalar graphemes without fonts."""
    values = ("BMP \u65e5\u672c\u8a9e café", "NonBMP 𠮷 𝛼 😀", "Emoji 👩🏽‍💻 🇯🇵 ❤️", "Combining e\u0301")
    with pylopdf.Document() as doc:
        page = doc.new_page()
        page.insert_ocr_text_layer([(40, 50 + row * 30, 550, 70 + row * 30, text) for row, text in enumerate(values)])
        doc.set_metadata({"title": "Unicode metadata 𠮷 😀"})
        data = doc.tobytes()
    return FeatureCase(
        "unicode-cmap-and-emoji",
        data,
        ("UTF-16BE ToUnicode", "non-BMP scalars", "emoji", "combining marks"),
        "Invisible text with ToUnicode CMaps: supplementary scalars use UTF-16 surrogate pairs. "
        "Includes a skin-tone/ZWJ emoji, flag regional indicators, variation selector, and decomposed accent. "
        "This tests Unicode decoding; it does not test rendering a color emoji font.",
        values,
        source_values={"unicode": " | ".join(values), "title": "Unicode metadata 𠮷 😀"},
    )


def build_cases() -> list[FeatureCase]:
    """Cover semantic families and independent producers without treating them as exhaustive."""
    structure = "\n".join(
        [
            text_op("Section heading", 40, 740, size=24),
            text_op("Ordinary paragraph with enough body text to establish a body font size.", 40, 700),
            text_op("Bold phrase", 40, 660, font="F2"),
            text_op("Italic phrase", 200, 660, font="F3"),
            text_op("code_value = 42", 40, 620, font="F4"),
            text_op("1. First item", 40, 580),
            text_op("2. Second item", 40, 560),
            text_op("- Nested bullet", 70, 540),
            text_op("Literal *asterisks* [brackets] # hash <tag> \\ backslash", 40, 500),
        ]
    )
    formula = "\n".join(
        [
            text_op("Positioned fraction", 40, 730, size=18),
            text_op("x", 100, 660),
            text_op("2", 107, 668, size=8),
            text_op("+ 1", 120, 660),
            "95 654 m 160 654 l S",
            text_op("y", 120, 632),
            text_op("= z", 175, 650),
            text_op("2", 195, 658, size=8),
        ]
    )
    actual_formula = " /Span << /ActualText <FEFF" + r"\frac{x^2+1}{y}=z^2".encode("utf-16-be").hex() + "> >> BDC\n"
    actual_formula += text_op("visual-formula", 40, 650) + "\nEMC"
    actual_text = " /Span << /ActualText <FEFF" + "accessible replacement".encode("utf-16-be").hex() + "> >> BDC\n"
    actual_text += text_op("painted glyphs", 40, 700) + "\nEMC"
    columns = [text_op("Full width heading", 40, 740, size=20)]
    for row in range(8):
        columns.extend(
            [
                text_op(f"LEFT{row} several words of left column prose", 40, 700 - row * 20, size=10),
                text_op(f"RIGHT{row} several words of right column prose", 320, 700 - row * 20, size=10),
            ]
        )
    cases = [
        FeatureCase(
            "text-structure-and-literals",
            page_pdf(structure),
            ("headings", "bold", "italic", "code", "lists", "nesting", "Markdown escaping"),
            "Standard 14 font variants carry styling names, but no embedded font metadata. "
            "The final line contains literal Markdown punctuation, not source markup.",
            ("Bold phrase", "Italic phrase", "code_value = 42", "Literal *asterisks*"),
        ),
        FeatureCase(
            "positioned-math",
            page_pdf(formula),
            ("fractions", "superscripts", "LaTeX reconstruction"),
            "The fraction bar is a drawing; the PDF has no equation source. Human formula reference is supplied.",
            ("Positioned fraction",),
            reference_math=r"\frac{x^2+1}{y}=z^2",
        ),
        FeatureCase(
            "math-actualtext",
            page_pdf(actual_formula),
            ("ActualText", "math source hint"),
            "ActualText explicitly contains LaTeX, while painted glyphs say visual-formula. "
            "Recovering the hint and producing a math block are separate observations.",
            (r"\frac{x^2+1}{y}=z^2",),
            reference_math=r"\frac{x^2+1}{y}=z^2",
        ),
        FeatureCase(
            "accessible-actualtext",
            page_pdf(actual_text),
            ("ActualText", "accessible text"),
            "ActualText differs intentionally from painted text; check which one survives.",
            ("accessible replacement",),
        ),
        FeatureCase(
            "two-column-order",
            page_pdf("\n".join(columns)),
            ("columns", "reading order"),
            "Content stream alternates columns. Logical reference is all left lines, then all right lines.",
            expected_order=tuple([f"LEFT{row}" for row in range(8)] + [f"RIGHT{row}" for row in range(8)]),
        ),
        _unicode_case(),
        _table_case(bordered=True),
        _table_case(bordered=False),
        _table_case(bordered=True, merged=True),
        _links_case(),
        _image_case(with_text=True),
        _image_case(with_text=False),
    ]
    borderless_ops = [text_op("Aligned labels", 40, 730, size=20)]
    for row, values in enumerate((("Name", "Amount"), ("Alpha", "42"), ("Beta", "7"), ("Gamma", "16"))):
        borderless_ops.extend(text_op(value, 40 + column * 220, 680 - row * 30) for column, value in enumerate(values))
    cases.append(
        FeatureCase(
            "table-borderless-aligned",
            page_pdf("\n".join(borderless_ops)),
            ("borderless tables", "aligned labels"),
            "Four complete rows with fixed left edges and regular leading. Contrast with the ragged, centered case.",
            ("Alpha", "Beta", "Gamma", "42", "7", "16"),
        )
    )
    with pylopdf.open(stream=page_pdf("\n".join(columns))) as doc:
        doc[0].set_rotation(90)
        cases.append(
            FeatureCase(
                "rotated-columns",
                doc.tobytes(),
                ("rotation", "columns", "reading order"),
                "The two-column fixture rotated 90 degrees; logical column order is unchanged.",
                expected_order=tuple([f"LEFT{row}" for row in range(8)] + [f"RIGHT{row}" for row in range(8)]),
            )
        )
    footnotes = "\n".join(
        [
            text_op("Page header", 40, 760, size=10),
            text_op("Body reference", 40, 700),
            text_op("1", 122, 707, size=8),
            text_op("Body paragraph continues here.", 40, 675),
            "40 130 m 180 130 l S",
            text_op("1 Footnote content", 40, 110, size=8),
            text_op("Page footer 1", 40, 40, size=8),
        ]
    )
    cases.append(
        FeatureCase(
            "footnotes-and-page-furniture",
            page_pdf(footnotes),
            ("footnotes", "superscripts", "headers", "footers", "page numbers"),
            "The superscript marker and footnote are positioned text, without a semantic footnote association. "
            "One page tests retention; repeated-header removal requires a separate multipage policy.",
            ("Body reference", "Footnote content", "Page header", "Page footer"),
        )
    )
    logical_rtl = ("שלום עולם", "مرحبا بالعالم", "אב 123 גד")
    visual_rtl = (logical_rtl[0][::-1], logical_rtl[1][::-1], "דג 123 בא")
    with pylopdf.Document() as doc:
        page = doc.new_page()
        page.insert_ocr_text_layer(
            [(40, 60 + row * 40, 400, 80 + row * 40, text) for row, text in enumerate(visual_rtl)]
        )
        cases.append(
            FeatureCase(
                "rtl-visual-glyph-order",
                doc.tobytes(),
                ("RTL", "bidi", "embedded numeric token"),
                "Invisible visual-order Hebrew and Arabic glyph runs; logical reference strings are supplied. "
                "This tests extraction order, not Arabic shaping or paragraph-level bidi layout.",
                logical_rtl,
            )
        )
    tagged = "\n".join(
        [
            "/P << /MCID 0 >> BDC",
            text_op("SECOND logical paragraph", 40, 650),
            "EMC",
            "/P << /MCID 1 >> BDC",
            text_op("FIRST visual paragraph", 40, 700),
            "EMC",
        ]
    )
    cases.append(
        FeatureCase(
            "tagged-reading-order",
            page_pdf(
                tagged,
                extra_page="/StructParents 0",
                extra_catalog="/StructTreeRoot 9 0 R /MarkInfo << /Marked true >>",
                extras=(
                    "<< /Type /StructTreeRoot /K [10 0 R 11 0 R] /ParentTree 12 0 R >>",
                    "<< /Type /StructElem /S /P /P 9 0 R /Pg 3 0 R /K 0 >>",
                    "<< /Type /StructElem /S /P /P 9 0 R /Pg 3 0 R /K 1 >>",
                    "<< /Nums [0 [10 0 R 11 0 R]] >>",
                ),
            ),
            ("tagged PDF", "logical reading order"),
            "Contrived tagged page: structure-tree order SECOND/FIRST differs from visual FIRST/SECOND. "
            "Stream order also matches tag order, so matching the reference does not prove tags were used.",
            expected_order=("SECOND", "FIRST"),
        )
    )
    assets = ROOT / "tests" / "assets" / "real_world"
    for name, pages, features, notes in [
        (
            "usrguide.pdf",
            (22,),
            ("LaTeX producer", "embedded fonts", "displayed math", "superscripts", "code"),
            "Original page 23 contains a displayed fraction and superscripts; source expression requires human review.",
        ),
        (
            "senate-expenditures.pdf",
            (0,),
            ("rotation", "merged headers", "hybrid tables"),
            "Independent rotated report with merged header and missing row rules.",
        ),
        (
            "nics-background-checks-2015-11.pdf",
            (0,),
            ("dense tables", "numeric alignment"),
            "Independent dense 25-column report; exact row/cell correctness requires review.",
        ),
        (
            "pdfium-type3.pdf",
            (0,),
            ("Type 3 fonts", "missing Unicode mapping"),
            "Glyph programs have no ToUnicode; pylopdf has a documented upstream-linked extraction gap.",
        ),
        (
            "f1040.pdf",
            (0,),
            ("form fields", "widgets", "form labels"),
            "IRS form with widget annotations. Field metadata and visible labels are different source objects.",
        ),
    ]:
        with pylopdf.open(assets / name) as doc:
            doc.select(pages)
            data = doc.tobytes()
        cases.append(
            FeatureCase(
                "corpus-" + name.removesuffix(".pdf"),
                data,
                features,
                notes,
                source=f"tests/assets/real_world/{name}; source and license in that directory's README",
            )
        )
    omml_path = ROOT / "bench" / "assets" / "rich" / "omml-equations.pdf"
    if omml_path.exists():
        cases.append(
            FeatureCase(
                "omml-equations",
                omml_path.read_bytes(),
                ("OMML producer", "fractions", "superscripts", "Unicode"),
                "Repository-authored DOCX with native OMML exported through LibreOffice. "
                "The embedded PDF glyph layout is the input, not the original OMML XML.",
                (
                    "Native Office equation",
                    "Bold body",
                    "Italic body",
                    "😀",
                    "👩🏽‍💻",
                    "\u65e5\u672c\u8a9e",
                    "𠮷",
                    "e\u0301",
                ),
                reference_math=r"\frac{x^2+1}{y}=z^2",
                source="bench/assets/rich/README.md; generated source and export provenance",
            )
        )
    return cases

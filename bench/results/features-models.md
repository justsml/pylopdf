# Rich PDF to Markdown feature study

- Run at: 2026-10-08 00:51 UTC
- Source commit: 615465ec20959cd4c4715cbf5ae639e7bad95578
- Environment: Linux-7.2.5-3-omarchy-x86_64-with-glibc2.44 / Python 3.14.7
- Versions: pylopdf 0.13.0, pymupdf 1.28.2, pymupdf4llm 1.28.2, pymupdf-layout 1.28.2, pypdf 6.15.0, pdfplumber 0.11.10, markdown-it-py 4.2.0, mdit-py-plugins 0.6.1, pylopdf-fonts-ar not installed, pylopdf-fonts-he not installed, pylopdf-fonts-hi not installed, pylopdf-fonts-jp not installed, pylopdf-fonts-ko not installed, pylopdf-fonts-th not installed, pylopdf-fonts-zh-cn not installed, pylopdf-fonts-zh-tw not installed
- Repetitions: 3
- OCR: disabled
- Additional model runs: See additional_runs and per-result run_index in JSON
- Observation code commit: f53ca2c4aea21ad214b9de3535b10f84e71d37c0
- Console log: [raw pipeline log](features-models.log)
- Artifact review: Syntax probes reparsed outside timing; original timings, output hashes, and run provenance preserved

Additional run 0: 2026-10-08T01:08:44.010292+00:00; Linux-7.2.5-3-omarchy-x86_64-with-glibc2.44 / Python 3.12.15; 4 CPU threads; 3 measured repetitions.
Versions: docling 2.135.0, marker-pdf 2.0.0, surya-ocr 0.22.1, torch 2.14.1+cpu. OCR: disabled; Docling formula enrichment is separately enabled in docling-formulas. Hosted LLM: disabled.
Source: f4549f4fefa8af3764d18a3748e1b9b0d7e3dcdf; dirty: False. Model file revisions and hashes are retained in JSON.

Additional run 1: 2026-10-08T02:30:01.746021+00:00; Linux-7.2.5-3-omarchy-x86_64-with-glibc2.44 / Python 3.12.15; 4 CPU threads; 3 measured repetitions.
Versions: docling 2.135.0, marker-pdf 2.0.0, surya-ocr 0.22.1, torch 2.14.1+cpu. OCR: disabled; Docling formula enrichment is separately enabled in docling-formulas. Hosted LLM: disabled.
Source: cc742387c9b7f139936d58f0265c2d0b5659527e; dirty: True. Model file revisions and hashes are retained in JSON.

Additional run 2: 2026-10-08T02:34:17.002048+00:00; Linux-7.2.5-3-omarchy-x86_64-with-glibc2.44 / Python 3.12.15; 4 CPU threads; 3 measured repetitions.
Versions: docling 2.135.0, marker-pdf 2.0.0, surya-ocr 0.22.1, torch 2.14.1+cpu. OCR: disabled; Docling formula enrichment is separately enabled in docling-formulas. Hosted LLM: disabled.
Source: a2d493e61d135d1aec7daca15086451d978be953; dirty: True. Model file revisions and hashes are retained in JSON.

Reproduce: `uv sync --group bench-rich && uv run python -m bench.features`.
Optional Docling/Marker runs: see `bench/MODEL_BENCHMARKS.md`; their original run metadata
and model fingerprints are retained separately in the JSON, alongside the earlier measurements.
One warmup plus median fresh-document conversion timings. Imports/model initialization occur
before or during warmup. Page OCR is disabled; the Docling formula mode separately runs recognition.
Source generation, syntax parsing, hashing, artifact serialization, and validation
are outside the timer. Image embedding is enabled for PyMuPDF4LLM, so its output cost differs
from converters that omit images. Timings across these tools are not equivalent-work rankings.

PyMuPDF, pypdf, and pdfplumber provide plain-text baselines here; they are not Markdown converters.
The JSON sidecar retains exact versions/options, source inventories, warnings, and literal probes.
Raw `.out` files contain the full unmodified UTF-8 result, including multilingual fixture data.

Syntax counts establish what markup was emitted, not whether the feature was reconstructed correctly.
Text checks are strict substring probes of parsed text; they are not semantic or visual quality scores.
Internal links need a target that resolves; a fragment-looking URL alone is insufficient.
Math requires checking the reference expression, not counting symbols or math delimiters.
Review table cell positions, merged spans, alignment, and image/caption association in the raw outputs.

## text-structure-and-literals

headings, bold, italic, code, lists, nesting, Markdown escaping

Standard 14 font variants carry styling names, but no embedded font metadata. The final line contains literal Markdown punctuation, not source markup.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/text-structure-and-literals.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 1.385 | 3/4 | 1/0/1/0/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--pylopdf.out) |
| pylopdf-text-tables | markdown | 1.419 | 3/4 | 1/0/1/0/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--pylopdf-text-tables.out) |
| pymupdf | text | 2.045 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/text-structure-and-literals--pymupdf.out) |
| pymupdf-actualtext | text | 1.925 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/text-structure-and-literals--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 14.408 | 3/4 | 1/1/2/1/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 83.114 | 3/4 | 1/1/2/1/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 125.662 | 3/4 | 1/1/2/1/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.213 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/text-structure-and-literals--pypdf.out) |
| pdfplumber | text | 5.908 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/text-structure-and-literals--pdfplumber.out) |
| docling | markdown | 747.402 | 3/4 | 2/0/1/0/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--docling/text-structure-and-literals--docling.out) / [structure](feature-outputs/text-structure-and-literals--docling/structured.json) |
| docling-formulas | markdown | 779.650 | 3/4 | 2/0/1/0/2/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--docling-formulas/text-structure-and-literals--docling-formulas.out) / [structure](feature-outputs/text-structure-and-literals--docling-formulas/structured.json) |
| marker-fast | markdown | 261.656 | 4/4 | 2/1/0/0/3/0/0/0/0/0 | [raw output](feature-outputs/text-structure-and-literals--marker-fast/text-structure-and-literals--marker-fast.out) / [structure](feature-outputs/text-structure-and-literals--marker-fast/structured.json) |

## positioned-math

fractions, superscripts, LaTeX reconstruction

The fraction bar is a drawing; the PDF has no equation source. Human formula reference is supplied.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/positioned-math.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.512 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/positioned-math--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.466 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/positioned-math--pylopdf-text-tables.out) |
| pymupdf | text | 0.967 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/positioned-math--pymupdf.out) |
| pymupdf-actualtext | text | 0.683 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/positioned-math--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 4.428 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/positioned-math--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 81.057 | 1/1 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/positioned-math--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 90.757 | 1/1 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/positioned-math--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.295 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/positioned-math--pypdf.out) |
| pdfplumber | text | 2.633 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/positioned-math--pdfplumber.out) |
| docling | markdown | 813.814 | 1/1 | 1/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/positioned-math--docling/positioned-math--docling.out) / [structure](feature-outputs/positioned-math--docling/structured.json) |
| docling-formulas | markdown | 780.832 | 1/1 | 1/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/positioned-math--docling-formulas/positioned-math--docling-formulas.out) / [structure](feature-outputs/positioned-math--docling-formulas/structured.json) |
| marker-fast | markdown | 241.111 | 1/1 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/positioned-math--marker-fast/positioned-math--marker-fast.out) / [structure](feature-outputs/positioned-math--marker-fast/structured.json) |

## math-actualtext

ActualText, math source hint

ActualText explicitly contains LaTeX, while painted glyphs say visual-formula. Recovering the hint and producing a math block are separate observations.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/math-actualtext.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.495 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.482 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--pylopdf-text-tables.out) |
| pymupdf | text | 0.968 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/math-actualtext--pymupdf.out) |
| pymupdf-actualtext | text | 0.644 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/math-actualtext--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 3.475 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 78.048 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 87.142 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.325 | 0/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/math-actualtext--pypdf.out) |
| pdfplumber | text | 3.027 | 0/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/math-actualtext--pdfplumber.out) |
| docling | markdown | 853.750 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--docling/math-actualtext--docling.out) / [structure](feature-outputs/math-actualtext--docling/structured.json) |
| docling-formulas | markdown | 798.062 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--docling-formulas/math-actualtext--docling-formulas.out) / [structure](feature-outputs/math-actualtext--docling-formulas/structured.json) |
| marker-fast | markdown | 217.663 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/math-actualtext--marker-fast/math-actualtext--marker-fast.out) / [structure](feature-outputs/math-actualtext--marker-fast/structured.json) |

## accessible-actualtext

ActualText, accessible text

ActualText differs intentionally from painted text; check which one survives.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/accessible-actualtext.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.299 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.415 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--pylopdf-text-tables.out) |
| pymupdf | text | 1.298 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/accessible-actualtext--pymupdf.out) |
| pymupdf-actualtext | text | 0.653 | 1/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/accessible-actualtext--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 3.013 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 76.672 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 78.485 | 0/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.269 | 0/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/accessible-actualtext--pypdf.out) |
| pdfplumber | text | 2.903 | 0/1 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/accessible-actualtext--pdfplumber.out) |
| docling | markdown | 733.680 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--docling/accessible-actualtext--docling.out) / [structure](feature-outputs/accessible-actualtext--docling/structured.json) |
| docling-formulas | markdown | 791.381 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--docling-formulas/accessible-actualtext--docling-formulas.out) / [structure](feature-outputs/accessible-actualtext--docling-formulas/structured.json) |
| marker-fast | markdown | 248.444 | 1/1 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/accessible-actualtext--marker-fast/accessible-actualtext--marker-fast.out) / [structure](feature-outputs/accessible-actualtext--marker-fast/structured.json) |

## two-column-order

columns, reading order

Content stream alternates columns. Logical reference is all left lines, then all right lines.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/two-column-order.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 5.924 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/two-column-order--pylopdf.out) |
| pylopdf-text-tables | markdown | 6.425 | 0/0 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/two-column-order--pylopdf-text-tables.out) |
| pymupdf | text | 1.195 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/two-column-order--pymupdf.out) |
| pymupdf-actualtext | text | 1.026 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/two-column-order--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 18.857 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/two-column-order--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 97.609 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/two-column-order--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 118.471 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/two-column-order--pymupdf4llm-html-tables.out) |
| pypdf | text | 2.867 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/two-column-order--pypdf.out) |
| pdfplumber | text | 20.102 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/two-column-order--pdfplumber.out) |
| docling | markdown | 1512.485 | 0/0 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/two-column-order--docling/two-column-order--docling.out) / [structure](feature-outputs/two-column-order--docling/structured.json) |
| docling-formulas | markdown | 1461.563 | 0/0 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/two-column-order--docling-formulas/two-column-order--docling-formulas.out) / [structure](feature-outputs/two-column-order--docling-formulas/structured.json) |
| marker-fast | markdown | 223.257 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/two-column-order--marker-fast/two-column-order--marker-fast.out) / [structure](feature-outputs/two-column-order--marker-fast/structured.json) |

## unicode-cmap-and-emoji

UTF-16BE ToUnicode, non-BMP scalars, emoji, combining marks

Invisible text with ToUnicode CMaps: supplementary scalars use UTF-16 surrogate pairs. Includes a skin-tone/ZWJ emoji, flag regional indicators, variation selector, and decomposed accent. This tests Unicode decoding; it does not test rendering a color emoji font.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/unicode-cmap-and-emoji.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.569 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.545 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--pylopdf-text-tables.out) |
| pymupdf | text | 1.070 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/unicode-cmap-and-emoji--pymupdf.out) |
| pymupdf-actualtext | text | 1.068 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/unicode-cmap-and-emoji--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 4.232 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 88.404 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 85.227 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.501 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/unicode-cmap-and-emoji--pypdf.out) |
| pdfplumber | text | 4.552 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/unicode-cmap-and-emoji--pdfplumber.out) |
| docling | markdown | 749.212 | 3/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--docling/unicode-cmap-and-emoji--docling.out) / [structure](feature-outputs/unicode-cmap-and-emoji--docling/structured.json) |
| docling-formulas | markdown | 769.384 | 3/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--docling-formulas/unicode-cmap-and-emoji--docling-formulas.out) / [structure](feature-outputs/unicode-cmap-and-emoji--docling-formulas/structured.json) |
| marker-fast | markdown | 1131.070 | 0/4 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/unicode-cmap-and-emoji--marker-fast/unicode-cmap-and-emoji--marker-fast.out) / [structure](feature-outputs/unicode-cmap-and-emoji--marker-fast/structured.json) |

## table-bordered

tables, table alignment, cell emphasis, cell escaping, empty cells, merged cells

Three rows/columns; last numeric cell is genuinely empty. Alignment is visual geometry, not PDF semantics. Bold/italic use non-embedded Standard 14 fonts. The merged case spans the first two header slots.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/table-bordered.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.926 | 5/5 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.878 | 5/5 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--pylopdf-text-tables.out) |
| pymupdf | text | 2.624 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-bordered--pymupdf.out) |
| pymupdf-actualtext | text | 2.202 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-bordered--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 8.691 | 3/5 | 1/0/1/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 140.731 | 3/5 | 1/3/1/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 147.085 | 5/5 | 1/0/0/0/0/0/0/0/1/0 | [raw output](feature-outputs/table-bordered--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.401 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-bordered--pypdf.out) |
| pdfplumber | text | 3.437 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-bordered--pdfplumber.out) |
| docling | markdown | 1317.853 | 5/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--docling/table-bordered--docling.out) / [structure](feature-outputs/table-bordered--docling/structured.json) |
| docling-formulas | markdown | 1388.771 | 5/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--docling-formulas/table-bordered--docling-formulas.out) / [structure](feature-outputs/table-bordered--docling-formulas/structured.json) |
| marker-fast | markdown | 1188.723 | 4/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-bordered--marker-fast/table-bordered--marker-fast.out) / [structure](feature-outputs/table-bordered--marker-fast/structured.json) |

## table-borderless

tables, table alignment, cell emphasis, cell escaping, empty cells, merged cells

Three rows/columns; last numeric cell is genuinely empty. Alignment is visual geometry, not PDF semantics. Bold/italic use non-embedded Standard 14 fonts. The merged case spans the first two header slots.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/table-borderless.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.560 | 5/5 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.574 | 5/5 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless--pylopdf-text-tables.out) |
| pymupdf | text | 1.858 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless--pymupdf.out) |
| pymupdf-actualtext | text | 1.568 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 5.323 | 5/5 | 1/3/1/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 136.005 | 3/5 | 1/3/1/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-borderless--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 160.592 | 5/5 | 1/0/0/0/0/0/0/0/1/0 | [raw output](feature-outputs/table-borderless--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.462 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless--pypdf.out) |
| pdfplumber | text | 3.694 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless--pdfplumber.out) |
| docling | markdown | 800.818 | 5/5 | 2/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless--docling/table-borderless--docling.out) / [structure](feature-outputs/table-borderless--docling/structured.json) |
| docling-formulas | markdown | 815.061 | 5/5 | 2/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless--docling-formulas/table-borderless--docling-formulas.out) / [structure](feature-outputs/table-borderless--docling-formulas/structured.json) |
| marker-fast | markdown | 355.298 | 4/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-borderless--marker-fast/table-borderless--marker-fast.out) / [structure](feature-outputs/table-borderless--marker-fast/structured.json) |

## table-merged

tables, table alignment, cell emphasis, cell escaping, empty cells, merged cells

Three rows/columns; last numeric cell is genuinely empty. Alignment is visual geometry, not PDF semantics. Bold/italic use non-embedded Standard 14 fonts. The merged case spans the first two header slots.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/table-merged.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.725 | 5/5 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.956 | 5/5 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--pylopdf-text-tables.out) |
| pymupdf | text | 1.946 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-merged--pymupdf.out) |
| pymupdf-actualtext | text | 1.868 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-merged--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 9.337 | 3/5 | 1/0/1/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 136.256 | 3/5 | 1/2/1/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 159.337 | 5/5 | 1/0/0/0/0/0/0/0/1/0 | [raw output](feature-outputs/table-merged--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.179 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-merged--pypdf.out) |
| pdfplumber | text | 3.563 | 5/5 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-merged--pdfplumber.out) |
| docling | markdown | 1292.085 | 5/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--docling/table-merged--docling.out) / [structure](feature-outputs/table-merged--docling/structured.json) |
| docling-formulas | markdown | 1261.058 | 5/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--docling-formulas/table-merged--docling-formulas.out) / [structure](feature-outputs/table-merged--docling-formulas/structured.json) |
| marker-fast | markdown | 360.043 | 4/5 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-merged--marker-fast/table-merged--marker-fast.out) / [structure](feature-outputs/table-merged--marker-fast/structured.json) |

## links-and-outline

URI links, internal links, named destinations, bookmarks

Link targets exist only in annotations, not visible text. A bookmark is not body text. Preserving an internal link requires both a generated destination and a link that resolves to it.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/links-and-outline.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.801 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/links-and-outline--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.815 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/links-and-outline--pylopdf-text-tables.out) |
| pymupdf | text | 1.043 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/links-and-outline--pymupdf.out) |
| pymupdf-actualtext | text | 1.032 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/links-and-outline--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 6.385 | 4/4 | 1/0/0/0/0/0/0/0/0/1 | [raw output](feature-outputs/links-and-outline--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 158.102 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/links-and-outline--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 181.490 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/links-and-outline--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.494 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/links-and-outline--pypdf.out) |
| pdfplumber | text | 3.123 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/links-and-outline--pdfplumber.out) |
| docling | markdown | 1465.878 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/links-and-outline--docling/links-and-outline--docling.out) / [structure](feature-outputs/links-and-outline--docling/structured.json) |
| docling-formulas | markdown | 1519.015 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/links-and-outline--docling-formulas/links-and-outline--docling-formulas.out) / [structure](feature-outputs/links-and-outline--docling-formulas/structured.json) |
| marker-fast | markdown | 630.314 | 4/4 | 1/0/0/0/0/0/0/0/0/3 | [raw output](feature-outputs/links-and-outline--marker-fast/links-and-outline--marker-fast.out) / [structure](feature-outputs/links-and-outline--marker-fast/structured.json) |

## images-and-vectors

raster images, vector graphics, captions, image-only pages, OCR

One 2x2 RGB image enlarged on the page and one stroked rectangle. No OCR text. An image reference does not establish source-image preservation or correct caption association.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/images-and-vectors.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.683 | 2/2 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/images-and-vectors--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.649 | 2/2 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/images-and-vectors--pylopdf-text-tables.out) |
| pymupdf | text | 0.824 | 2/2 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/images-and-vectors--pymupdf.out) |
| pymupdf-actualtext | text | 0.699 | 2/2 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/images-and-vectors--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 6.692 | 2/2 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/images-and-vectors--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 78.488 | 2/2 | 1/0/0/0/0/0/2/0/0/0 | [raw output](feature-outputs/images-and-vectors--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 81.712 | 2/2 | 1/0/0/0/0/0/2/0/0/0 | [raw output](feature-outputs/images-and-vectors--pymupdf4llm-html-tables.out) |
| pypdf | text | 0.673 | 2/2 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/images-and-vectors--pypdf.out) |
| pdfplumber | text | 2.088 | 2/2 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/images-and-vectors--pdfplumber.out) |
| docling | markdown | 747.712 | 2/2 | 0/0/0/0/0/0/2/0/0/0 | [raw output](feature-outputs/images-and-vectors--docling/images-and-vectors--docling.out) / [structure](feature-outputs/images-and-vectors--docling/structured.json) |
| docling-formulas | markdown | 770.886 | 2/2 | 0/0/0/0/0/0/2/0/0/0 | [raw output](feature-outputs/images-and-vectors--docling-formulas/images-and-vectors--docling-formulas.out) / [structure](feature-outputs/images-and-vectors--docling-formulas/structured.json) |
| marker-fast | markdown | 347.391 | 2/2 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/images-and-vectors--marker-fast/images-and-vectors--marker-fast.out) / [structure](feature-outputs/images-and-vectors--marker-fast/structured.json) |

## image-only

raster images, vector graphics, captions, image-only pages, OCR

One 2x2 RGB image enlarged on the page and one stroked rectangle. No OCR text. An image reference does not establish source-image preservation or correct caption association.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/image-only.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.225 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/image-only--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.219 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/image-only--pylopdf-text-tables.out) |
| pymupdf | text | 0.252 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/image-only--pymupdf.out) |
| pymupdf-actualtext | text | 0.240 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/image-only--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 5.479 | 0/0 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/image-only--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 65.922 | 0/0 | 0/0/0/0/0/0/2/0/0/0 | [raw output](feature-outputs/image-only--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 63.922 | 0/0 | 0/0/0/0/0/0/2/0/0/0 | [raw output](feature-outputs/image-only--pymupdf4llm-html-tables.out) |
| pypdf | text | 0.559 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/image-only--pypdf.out) |
| pdfplumber | text | 1.226 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/image-only--pdfplumber.out) |
| docling | markdown | 1128.213 | 0/0 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/image-only--docling/image-only--docling.out) / [structure](feature-outputs/image-only--docling/structured.json) |
| docling-formulas | markdown | 1171.104 | 0/0 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/image-only--docling-formulas/image-only--docling-formulas.out) / [structure](feature-outputs/image-only--docling-formulas/structured.json) |
| marker-fast | markdown | 339.713 | 0/0 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/image-only--marker-fast/image-only--marker-fast.out) / [structure](feature-outputs/image-only--marker-fast/structured.json) |

## table-borderless-aligned

borderless tables, aligned labels

Four complete rows with fixed left edges and regular leading. Contrast with the ragged, centered case.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/table-borderless-aligned.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.633 | 6/6 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.720 | 6/6 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--pylopdf-text-tables.out) |
| pymupdf | text | 0.899 | 6/6 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless-aligned--pymupdf.out) |
| pymupdf-actualtext | text | 0.891 | 6/6 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless-aligned--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 6.087 | 6/6 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 144.430 | 6/6 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 137.081 | 6/6 | 1/0/0/0/0/0/0/0/1/0 | [raw output](feature-outputs/table-borderless-aligned--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.160 | 6/6 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless-aligned--pypdf.out) |
| pdfplumber | text | 3.586 | 6/6 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/table-borderless-aligned--pdfplumber.out) |
| docling | markdown | 809.125 | 6/6 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--docling/table-borderless-aligned--docling.out) / [structure](feature-outputs/table-borderless-aligned--docling/structured.json) |
| docling-formulas | markdown | 850.860 | 6/6 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--docling-formulas/table-borderless-aligned--docling-formulas.out) / [structure](feature-outputs/table-borderless-aligned--docling-formulas/structured.json) |
| marker-fast | markdown | 343.210 | 6/6 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/table-borderless-aligned--marker-fast/table-borderless-aligned--marker-fast.out) / [structure](feature-outputs/table-borderless-aligned--marker-fast/structured.json) |

## rotated-columns

rotation, columns, reading order

The two-column fixture rotated 90 degrees; logical column order is unchanged.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/rotated-columns.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 4.607 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--pylopdf.out) |
| pylopdf-text-tables | markdown | 4.636 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--pylopdf-text-tables.out) |
| pymupdf | text | 0.903 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rotated-columns--pymupdf.out) |
| pymupdf-actualtext | text | 0.912 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rotated-columns--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 18.027 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 102.591 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 117.857 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--pymupdf4llm-html-tables.out) |
| pypdf | text | 4.572 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rotated-columns--pypdf.out) |
| pdfplumber | text | 17.154 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rotated-columns--pdfplumber.out) |
| docling | markdown | 759.744 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--docling/rotated-columns--docling.out) / [structure](feature-outputs/rotated-columns--docling/structured.json) |
| docling-formulas | markdown | 760.565 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--docling-formulas/rotated-columns--docling-formulas.out) / [structure](feature-outputs/rotated-columns--docling-formulas/structured.json) |
| marker-fast | markdown | 319.310 | 0/0 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rotated-columns--marker-fast/rotated-columns--marker-fast.out) / [structure](feature-outputs/rotated-columns--marker-fast/structured.json) |

## footnotes-and-page-furniture

footnotes, superscripts, headers, footers, page numbers

The superscript marker and footnote are positioned text, without a semantic footnote association. One page tests retention; repeated-header removal requires a separate multipage policy.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/footnotes-and-page-furniture.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.740 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.783 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--pylopdf-text-tables.out) |
| pymupdf | text | 0.754 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/footnotes-and-page-furniture--pymupdf.out) |
| pymupdf-actualtext | text | 0.693 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/footnotes-and-page-furniture--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 5.417 | 4/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 82.075 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 116.045 | 4/4 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--pymupdf4llm-html-tables.out) |
| pypdf | text | 2.683 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/footnotes-and-page-furniture--pypdf.out) |
| pdfplumber | text | 9.985 | 4/4 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/footnotes-and-page-furniture--pdfplumber.out) |
| docling | markdown | 869.848 | 2/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--docling/footnotes-and-page-furniture--docling.out) / [structure](feature-outputs/footnotes-and-page-furniture--docling/structured.json) |
| docling-formulas | markdown | 841.109 | 2/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--docling-formulas/footnotes-and-page-furniture--docling-formulas.out) / [structure](feature-outputs/footnotes-and-page-furniture--docling-formulas/structured.json) |
| marker-fast | markdown | 322.771 | 2/4 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/footnotes-and-page-furniture--marker-fast/footnotes-and-page-furniture--marker-fast.out) / [structure](feature-outputs/footnotes-and-page-furniture--marker-fast/structured.json) |

## rtl-visual-glyph-order

RTL, bidi, embedded numeric token

Invisible visual-order Hebrew and Arabic glyph runs; logical reference strings are supplied. This tests extraction order, not Arabic shaping or paragraph-level bidi layout.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/rtl-visual-glyph-order.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.660 | 3/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.583 | 3/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--pylopdf-text-tables.out) |
| pymupdf | text | 0.880 | 2/3 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rtl-visual-glyph-order--pymupdf.out) |
| pymupdf-actualtext | text | 0.914 | 2/3 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rtl-visual-glyph-order--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 3.779 | 2/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 90.926 | 2/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 83.850 | 2/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--pymupdf4llm-html-tables.out) |
| pypdf | text | 1.977 | 2/3 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rtl-visual-glyph-order--pypdf.out) |
| pdfplumber | text | 5.935 | 0/3 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/rtl-visual-glyph-order--pdfplumber.out) |
| docling | markdown | 767.802 | 3/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--docling/rtl-visual-glyph-order--docling.out) / [structure](feature-outputs/rtl-visual-glyph-order--docling/structured.json) |
| docling-formulas | markdown | 850.495 | 3/3 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--docling-formulas/rtl-visual-glyph-order--docling-formulas.out) / [structure](feature-outputs/rtl-visual-glyph-order--docling-formulas/structured.json) |
| marker-fast | markdown | 345.475 | 0/3 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/rtl-visual-glyph-order--marker-fast/rtl-visual-glyph-order--marker-fast.out) / [structure](feature-outputs/rtl-visual-glyph-order--marker-fast/structured.json) |

## tagged-reading-order

tagged PDF, logical reading order

Contrived tagged page: structure-tree order SECOND/FIRST differs from visual FIRST/SECOND. Stream order also matches tag order, so matching the reference does not prove tags were used.

Source: Repository-authored synthetic PDF; repository MIT license

[Input PDF](feature-outputs/tagged-reading-order.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.858 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.656 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--pylopdf-text-tables.out) |
| pymupdf | text | 1.123 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/tagged-reading-order--pymupdf.out) |
| pymupdf-actualtext | text | 1.135 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/tagged-reading-order--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 6.485 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 93.109 | 0/0 | 2/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 82.806 | 0/0 | 2/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--pymupdf4llm-html-tables.out) |
| pypdf | text | 0.862 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/tagged-reading-order--pypdf.out) |
| pdfplumber | text | 2.700 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/tagged-reading-order--pdfplumber.out) |
| docling | markdown | 951.744 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--docling/tagged-reading-order--docling.out) / [structure](feature-outputs/tagged-reading-order--docling/structured.json) |
| docling-formulas | markdown | 818.051 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--docling-formulas/tagged-reading-order--docling-formulas.out) / [structure](feature-outputs/tagged-reading-order--docling-formulas/structured.json) |
| marker-fast | markdown | 291.392 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/tagged-reading-order--marker-fast/tagged-reading-order--marker-fast.out) / [structure](feature-outputs/tagged-reading-order--marker-fast/structured.json) |

## corpus-usrguide

LaTeX producer, embedded fonts, displayed math, superscripts, code

Original page 23 contains a displayed fraction and superscripts; source expression requires human review.

Source: tests/assets/real_world/usrguide.pdf; source and license in that directory's README

[Input PDF](feature-outputs/corpus-usrguide.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 11.724 | 0/0 | 0/0/1/0/3/0/0/1/0/0 | [raw output](feature-outputs/corpus-usrguide--pylopdf.out) |
| pylopdf-text-tables | markdown | 11.543 | 0/0 | 0/0/1/0/3/0/0/1/0/0 | [raw output](feature-outputs/corpus-usrguide--pylopdf-text-tables.out) |
| pymupdf | text | 6.586 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-usrguide--pymupdf.out) |
| pymupdf-actualtext | text | 7.349 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-usrguide--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 78.934 | 0/0 | 0/0/17/36/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-usrguide--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 153.277 | 0/0 | 0/0/13/35/1/0/0/0/0/0 | [raw output](feature-outputs/corpus-usrguide--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 231.829 | 0/0 | 0/0/13/35/1/0/0/0/0/0 | [raw output](feature-outputs/corpus-usrguide--pymupdf4llm-html-tables.out) |
| pypdf | text | 29.247 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-usrguide--pypdf.out) |
| pdfplumber | text | 96.008 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-usrguide--pdfplumber.out) |
| docling | markdown | 995.513 | 0/0 | 0/0/1/5/1/0/0/0/0/0 | [raw output](feature-outputs/corpus-usrguide--docling/corpus-usrguide--docling.out) / [structure](feature-outputs/corpus-usrguide--docling/structured.json) |
| docling-formulas | markdown | 824.689 | 0/0 | 0/0/1/5/1/0/0/0/0/0 | [raw output](feature-outputs/corpus-usrguide--docling-formulas/corpus-usrguide--docling-formulas.out) / [structure](feature-outputs/corpus-usrguide--docling-formulas/structured.json) |
| marker-fast | markdown | 491.975 | 0/0 | 2/0/0/0/1/0/0/0/0/0 | [raw output](feature-outputs/corpus-usrguide--marker-fast/corpus-usrguide--marker-fast.out) / [structure](feature-outputs/corpus-usrguide--marker-fast/structured.json) |

## corpus-senate-expenditures

rotation, merged headers, hybrid tables

Independent rotated report with merged header and missing row rules.

Source: tests/assets/real_world/senate-expenditures.pdf; source and license in that directory's README

[Input PDF](feature-outputs/corpus-senate-expenditures.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 10.555 | 0/0 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--pylopdf.out) |
| pylopdf-text-tables | markdown | 11.567 | 0/0 | 1/0/0/0/0/2/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--pylopdf-text-tables.out) |
| pymupdf | text | 5.350 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-senate-expenditures--pymupdf.out) |
| pymupdf-actualtext | text | 5.027 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-senate-expenditures--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 899.848 | 0/0 | 0/8/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 378.157 | 0/0 | 0/13/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 946.745 | 0/0 | 0/0/0/0/0/0/0/0/1/0 | [raw output](feature-outputs/corpus-senate-expenditures--pymupdf4llm-html-tables.out) |
| pypdf | text | 87.026 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-senate-expenditures--pypdf.out) |
| pdfplumber | text | 262.146 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-senate-expenditures--pdfplumber.out) |
| docling | markdown | 9919.665 | 0/0 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--docling/corpus-senate-expenditures--docling.out) / [structure](feature-outputs/corpus-senate-expenditures--docling/structured.json) |
| docling-formulas | markdown | 9846.795 | 0/0 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--docling-formulas/corpus-senate-expenditures--docling-formulas.out) / [structure](feature-outputs/corpus-senate-expenditures--docling-formulas/structured.json) |
| marker-fast | markdown | 867.954 | 0/0 | 0/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-senate-expenditures--marker-fast/corpus-senate-expenditures--marker-fast.out) / [structure](feature-outputs/corpus-senate-expenditures--marker-fast/structured.json) |

## corpus-nics-background-checks-2015-11

dense tables, numeric alignment

Independent dense 25-column report; exact row/cell correctness requires review.

Source: tests/assets/real_world/nics-background-checks-2015-11.pdf; source and license in that directory's README

[Input PDF](feature-outputs/corpus-nics-background-checks-2015-11.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 44.912 | 0/0 | 0/2/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pylopdf.out) |
| pylopdf-text-tables | markdown | 50.564 | 0/0 | 0/2/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pylopdf-text-tables.out) |
| pymupdf | text | 6.094 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pymupdf.out) |
| pymupdf-actualtext | text | 5.699 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 2484.910 | 0/0 | 0/27/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 2326.888 | 0/0 | 2/19/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 4911.334 | 0/0 | 2/2/0/0/0/0/0/0/1/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pymupdf4llm-html-tables.out) |
| pypdf | text | 88.213 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pypdf.out) |
| pdfplumber | text | 249.994 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--pdfplumber.out) |
| docling | markdown | 36631.844 | 0/0 | 2/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--docling/corpus-nics-background-checks-2015-11--docling.out) / [structure](feature-outputs/corpus-nics-background-checks-2015-11--docling/structured.json) |
| docling-formulas | markdown | 41483.241 | 0/0 | 2/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--docling-formulas/corpus-nics-background-checks-2015-11--docling-formulas.out) / [structure](feature-outputs/corpus-nics-background-checks-2015-11--docling-formulas/structured.json) |
| marker-fast | markdown | 894.489 | 0/0 | 1/2/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-nics-background-checks-2015-11--marker-fast/corpus-nics-background-checks-2015-11--marker-fast.out) / [structure](feature-outputs/corpus-nics-background-checks-2015-11--marker-fast/structured.json) |

## corpus-pdfium-type3

Type 3 fonts, missing Unicode mapping

Glyph programs have no ToUnicode; pylopdf has a documented upstream-linked extraction gap.

Source: tests/assets/real_world/pdfium-type3.pdf; source and license in that directory's README

[Input PDF](feature-outputs/corpus-pdfium-type3.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 0.253 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--pylopdf.out) |
| pylopdf-text-tables | markdown | 0.229 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--pylopdf-text-tables.out) |
| pymupdf | text | 0.276 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-pdfium-type3--pymupdf.out) |
| pymupdf-actualtext | text | 0.268 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-pdfium-type3--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 2.422 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 74.821 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 77.023 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--pymupdf4llm-html-tables.out) |
| pypdf | text | 0.985 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-pdfium-type3--pypdf.out) |
| pdfplumber | text | 1.335 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-pdfium-type3--pdfplumber.out) |
| docling | markdown | 786.478 | 0/0 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--docling/corpus-pdfium-type3--docling.out) / [structure](feature-outputs/corpus-pdfium-type3--docling/structured.json) |
| docling-formulas | markdown | 771.561 | 0/0 | 0/0/0/0/0/0/1/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--docling-formulas/corpus-pdfium-type3--docling-formulas.out) / [structure](feature-outputs/corpus-pdfium-type3--docling-formulas/structured.json) |
| marker-fast | markdown | 238.670 | 0/0 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/corpus-pdfium-type3--marker-fast/corpus-pdfium-type3--marker-fast.out) / [structure](feature-outputs/corpus-pdfium-type3--marker-fast/structured.json) |

## corpus-f1040

form fields, widgets, form labels

IRS form with widget annotations. Field metadata and visible labels are different source objects.

Source: tests/assets/real_world/f1040.pdf; source and license in that directory's README

[Input PDF](feature-outputs/corpus-f1040.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 19.051 | 0/0 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-f1040--pylopdf.out) |
| pylopdf-text-tables | markdown | 19.625 | 0/0 | 1/0/0/0/0/3/0/0/0/0 | [raw output](feature-outputs/corpus-f1040--pylopdf-text-tables.out) |
| pymupdf | text | 23.140 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-f1040--pymupdf.out) |
| pymupdf-actualtext | text | 27.572 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-f1040--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 1878.959 | 0/0 | 0/1565/0/0/0/3/0/0/0/0 | [raw output](feature-outputs/corpus-f1040--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 1110.355 | 0/0 | 0/103/0/0/0/3/0/0/0/0 | [raw output](feature-outputs/corpus-f1040--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 3269.465 | 0/0 | 0/0/0/0/0/0/0/0/9/0 | [raw output](feature-outputs/corpus-f1040--pymupdf4llm-html-tables.out) |
| pypdf | text | 74.822 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-f1040--pypdf.out) |
| pdfplumber | text | 231.598 | 0/0 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/corpus-f1040--pdfplumber.out) |
| docling | markdown | 1620.392 | 0/0 | 6/0/0/0/34/0/1/0/0/0 | [raw output](feature-outputs/corpus-f1040--docling/corpus-f1040--docling.out) / [structure](feature-outputs/corpus-f1040--docling/structured.json) |
| docling-formulas | markdown | 1939.745 | 0/0 | 6/0/0/0/34/0/1/0/0/0 | [raw output](feature-outputs/corpus-f1040--docling-formulas/corpus-f1040--docling-formulas.out) / [structure](feature-outputs/corpus-f1040--docling-formulas/structured.json) |
| marker-fast | markdown | 689.056 | 0/0 | 1/0/0/0/0/1/0/0/0/0 | [raw output](feature-outputs/corpus-f1040--marker-fast/corpus-f1040--marker-fast.out) / [structure](feature-outputs/corpus-f1040--marker-fast/structured.json) |

## omml-equations

OMML producer, fractions, superscripts, Unicode

Repository-authored DOCX with native OMML exported through LibreOffice. The embedded PDF glyph layout is the input, not the original OMML XML.

Source: bench/assets/rich/README.md; generated source and export provenance

[Input PDF](feature-outputs/omml-equations.pdf)

| Adapter | Kind | Median ms | Text probes | H/B/I/code/list/table/image/math/HTML/link | Result |
|---|---|---:|---:|---|---|
| pylopdf | markdown | 1.761 | 7/8 | 1/1/4/0/0/0/0/0/0/0 | [raw output](feature-outputs/omml-equations--pylopdf.out) |
| pylopdf-text-tables | markdown | 1.767 | 7/8 | 1/1/4/0/0/0/0/0/0/0 | [raw output](feature-outputs/omml-equations--pylopdf-text-tables.out) |
| pymupdf | text | 1.240 | 8/8 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/omml-equations--pymupdf.out) |
| pymupdf-actualtext | text | 1.222 | 8/8 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/omml-equations--pymupdf-actualtext.out) |
| pymupdf4llm-legacy | markdown | 9.067 | 8/8 | 1/2/4/0/0/0/0/0/0/0 | [raw output](feature-outputs/omml-equations--pymupdf4llm-legacy.out) |
| pymupdf4llm-layout | markdown | 85.675 | 7/8 | 1/2/1/0/0/0/1/0/0/0 | [raw output](feature-outputs/omml-equations--pymupdf4llm-layout.out) |
| pymupdf4llm-html-tables | markdown | 89.068 | 7/8 | 1/2/1/0/0/0/1/0/0/0 | [raw output](feature-outputs/omml-equations--pymupdf4llm-html-tables.out) |
| pypdf | text | 8.335 | 7/8 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/omml-equations--pypdf.out) |
| pdfplumber | text | 17.470 | 7/8 | -/-/-/-/-/-/-/-/-/- | [raw output](feature-outputs/omml-equations--pdfplumber.out) |
| docling | markdown | 809.334 | 7/8 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/omml-equations--docling/omml-equations--docling.out) / [structure](feature-outputs/omml-equations--docling/structured.json) |
| docling-formulas | markdown | 758.886 | 7/8 | 1/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/omml-equations--docling-formulas/omml-equations--docling-formulas.out) / [structure](feature-outputs/omml-equations--docling-formulas/structured.json) |
| marker-fast | markdown | 320.447 | 0/8 | 0/0/0/0/0/0/0/0/0/0 | [raw output](feature-outputs/omml-equations--marker-fast/omml-equations--marker-fast.out) / [structure](feature-outputs/omml-equations--marker-fast/structured.json) |

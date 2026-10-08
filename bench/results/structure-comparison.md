# Structured recovery comparison

These are exploratory results on the preserved study inputs, not held-out production accuracy.
Each adapter's denominators describe its attempted cohort. Failed calls remain in the denominators.
Unsupported retained Docling/Marker replays are listed separately and excluded from quality totals.
Positive grids, negative controls, and visual corpus spot checks are separate measurements.
Cell and relationship totals count the reference grid; spot checks do not cover a complete corpus page.
See STRUCTURE_BENCHMARKS.md for timing, source-agreement, training, and provenance limitations.
Truncated counts are lower bounds: older failed calls can lack generation metadata in the report.

## structure-latest

Source report run: 2026-10-08T03:18:26.318705+00:00
Snapshot SHA-256: `617389757e5971a5545d37f311660f269625170f6c9c6c08f29c4178ec8d6cc8`.

| Adapter | Calls | Unsupported | Positive exact | Negative exact | Cells | Relation recall | Precision | Corpus cells | Errors | Truncated |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- | ---: | ---: |
| pylopdf | 28 | 0 | 2/9 | 6/6 | 18/83 | 24/111 | 24/24 | 12/35 | 0 | 0 |
| pylopdf-text | 28 | 0 | 3/9 | 5/6 | 26/83 | 34/111 | 34/56 | 12/35 | 0 | 0 |
| yolo-geometry | 28 | 0 | 3/9 | 6/6 | 34/83 | 43/111 | 43/46 | 6/35 | 0 | 0 |
| yolo-geometry-wrapped | 28 | 0 | 4/9 | 6/6 | 46/83 | 60/111 | 60/63 | 6/35 | 0 | 0 |
| olmocr-image | 28 | 0 | 4/9 | 6/6 | 65/83 | 90/111 | 90/121 | 0/35 | 0 | 1 |
| olmocr-text | 28 | 0 | 3/9 | 6/6 | 61/83 | 93/111 | 93/121 | 0/35 | 3 | 0 |
| olmocr-patch | 28 | 0 | 0/9 | 0/6 | 0/83 | 0/111 | — | 0/35 | 28 | 0 |
| geometry | 28 | 0 | 6/9 | 4/6 | 61/83 | 79/111 | 79/126 | 12/35 | 0 | 0 |
| geometry-bullets | 28 | 0 | 6/9 | 4/6 | 61/83 | 79/111 | 79/126 | 12/35 | 0 | 0 |
| geometry-wrapped | 28 | 0 | 7/9 | 4/6 | 73/83 | 96/111 | 96/143 | 29/35 | 0 | 0 |
| geometry-wrapped-bullets | 28 | 0 | 7/9 | 4/6 | 73/83 | 96/111 | 96/143 | 29/35 | 0 | 0 |
| native-bullets | 28 | 0 | 1/9 | 6/6 | 17/83 | 21/111 | 21/24 | 12/35 | 0 | 0 |
| yolo-normalized-geometry-wrapped | 28 | 0 | 7/9 | 6/6 | 73/83 | 96/111 | 96/99 | 29/35 | 0 | 0 |
| qwen-image | 28 | 0 | 0/9 | 6/6 | 0/83 | 0/111 | — | 0/35 | 0 | 1 |
| qwen-text | 28 | 0 | 0/9 | 6/6 | 0/83 | 0/111 | — | 0/35 | 1 | 3 |
| qwen-patch | 28 | 0 | 0/9 | 0/6 | 0/83 | 0/111 | 0/32 | 0/35 | 25 | 0 |
| native-header-bullets | 28 | 0 | 1/9 | 6/6 | 17/83 | 21/111 | 21/24 | 35/35 | 0 | 0 |
| repair-qwen-image | 28 | 0 | 0/9 | 1/6 | 21/83 | 49/111 | 49/200 | 0/35 | 0 | 0 |
| repair-qwen-text | 28 | 0 | 2/9 | 3/6 | 49/83 | 54/111 | 54/140 | 0/35 | 1 | 0 |
| retained-docling | 28 | 6 | 1/4 | 5/6 | 10/35 | 15/46 | 15/25 | 23/35 | 0 | 0 |
| retained-docling-formulas | 28 | 6 | 1/4 | 5/6 | 10/35 | 15/46 | 15/25 | 23/35 | 0 | 0 |
| retained-marker-fast | 28 | 6 | 1/4 | 6/6 | 29/35 | 28/46 | 28/46 | 12/35 | 0 | 0 |
| ocr-geometry-wrapped | 28 | 0 | 8/9 | 5/6 | 82/83 | 108/111 | 108/133 | 29/35 | 0 | 0 |
| hybrid-html | 28 | 0 | 9/9 | 6/6 | 83/83 | 111/111 | 111/111 | 35/35 | 0 | 0 |
| hybrid-bullets | 28 | 0 | 9/9 | 6/6 | 83/83 | 111/111 | 111/111 | 35/35 | 0 | 0 |
| olmocr-normalized | 3 | 0 | 3/3 | — | 27/27 | 36/36 | 36/36 | — | 0 | 0 |
| olmocr-compact-text | 7 | 0 | 1/4 | 1/1 | 36/39 | 44/53 | 44/53 | 0/35 | 1 | 0 |
| olmocr-4bit-text | 2 | 0 | — | — | — | — | — | 0/35 | 1 | 0 |
| olmocr-yolo-crop | 7 | 0 | 4/4 | 1/1 | 39/39 | 53/53 | 53/53 | 11/35 | 0 | 1 |
| olmocr-geometry-crop | 5 | 0 | 3/4 | 1/1 | 38/39 | 50/53 | 50/53 | — | 0 | 0 |
| olmocr-row-crop | 2 | 0 | — | — | — | — | — | 7/35 | 0 | 1 |
| qwen-compact-text | 7 | 0 | 0/4 | 1/1 | 0/39 | 0/53 | — | 0/35 | 0 | 0 |
| qwen-compact-patch | 5 | 0 | 0/3 | 0/1 | 0/27 | 0/36 | — | 0/23 | 5 | 0 |

## structure-hosted

Source report run: 2026-10-08T04:42:19.263122+00:00
Snapshot SHA-256: `c6ec01020a21efc45fb3e8525300a25ca8245ec44d47386a825fc028973bf3d2`.

| Adapter | Calls | Unsupported | Positive exact | Negative exact | Cells | Relation recall | Precision | Corpus cells | Errors | Truncated |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- | ---: | ---: |
| qwen-hosted-compact-text | 28 | 0 | 0/9 | 6/6 | 0/83 | 0/111 | — | 0/35 | 0 | 0 |
| qwen-jev-hosted-compact-text | 17 | 0 | 8/9 | 4/6 | 74/83 | 99/111 | 99/124 | 0/35 | 2 | 2 |
| qwen-hosted-image | 28 | 0 | 0/9 | 6/6 | 0/83 | 0/111 | — | 0/35 | 0 | 1 |
| qwen-hosted-compact-patch | 28 | 0 | 7/9 | 5/6 | 68/83 | 87/111 | 87/121 | 0/35 | 2 | 0 |
| jev-text-gated-geometry-wrapped | 15 | 0 | 7/9 | 6/6 | 73/83 | 96/111 | 96/99 | — | 0 | 0 |
| qwen-jev-hosted-compact-patch | 17 | 0 | 5/9 | 5/6 | 47/83 | 63/111 | 63/63 | 0/35 | 7 | 0 |
| repair-qwen-hosted-image | 28 | 0 | 6/9 | 6/6 | 63/83 | 105/111 | 105/121 | 23/35 | 0 | 0 |
| repair-qwen-hosted-compact-text | 28 | 0 | 7/9 | 6/6 | 73/83 | 96/111 | 96/116 | 23/35 | 0 | 0 |
| qwen-hosted-compact-row-patch | 2 | 0 | — | — | — | — | — | 0/35 | 2 | 0 |
| qwen-jev-hosted-compact-row-patch | 2 | 0 | — | — | — | — | — | 0/35 | 2 | 0 |

## structure-remote48

Source report run: 2026-10-08T04:51:00.292628+00:00
Snapshot SHA-256: `c2f6bd6c224df7c8e08d323457bf71dfd37224fb195cff17ec2b2dcc94615408`.

| Adapter | Calls | Unsupported | Positive exact | Negative exact | Cells | Relation recall | Precision | Corpus cells | Errors | Truncated |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- | ---: | ---: |
| olmocr-text | 3 | 0 | — | — | — | — | — | 0/35 | 0 | 1 |
| olmocr-compact-text | 3 | 0 | — | — | — | — | — | 0/35 | 0 | 0 |
| qwen-text | 3 | 0 | — | — | — | — | — | 0/35 | 0 | 1 |
| repair-qwen-text | 3 | 0 | — | — | — | — | — | 0/35 | 0 | 0 |

## structure-remote48-long

Source report run: 2026-10-08T04:51:00.292628+00:00
Snapshot SHA-256: `3138c2d400d91afe1c8fb1e42bfbac3359ea5aebf23ff7c42a4a1ff69ec1a6d7`.

| Adapter | Calls | Unsupported | Positive exact | Negative exact | Cells | Relation recall | Precision | Corpus cells | Errors | Truncated |
| --- | ---: | ---: | --- | --- | --- | --- | --- | --- | ---: | ---: |
| olmocr-image | 2 | 0 | — | — | — | — | — | 0/35 | 0 | 1 |


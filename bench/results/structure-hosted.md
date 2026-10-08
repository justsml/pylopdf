# Structured PDF recovery experiments

Run: 2026-10-08T04:42:19.263122+00:00

Page 0 of each preserved input is evaluated. Full inputs, screenshots, positioned words, prompts,
raw responses, validated patches, and errors are retained locally in `structure-artifacts/`.
Reference cells are independent fixture definitions; corpus cells without a reference remain unscored.
Source agreement is not ground truth, especially for missing Unicode, scans, or OCR corrections.
Geometry bullet results score their underlying recovered cells, not reparsed bullet labels.
Timing covers the adapter after preparation, excluding fixture extraction/rendering; prepared baselines
are replayed, so their timing is not a conversion measurement. Process RSS is cumulative high-water RSS.
Model repetitions include the first inference; initialization is reported separately. No throughput claims.
CUDA figures are observed peak allocated bytes for retained generation calls, not reserved VRAM.
The provenance device is the requested backend; native geometry/OCR and replay/repair adapters use CPU.

| Case | Adapter | Exact grid | Cells | Relations recalled | Record cells | Seconds | CUDA GiB | Result |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- |
| table-borderless | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 2.003 | — | ok |
| table-borderless | qwen-jev-hosted-compact-text | True | 9/9 | 12/12 | — | 13.619 | — | ok |
| text-structure-and-literals | qwen-hosted-image | True | — | — | — | 2.152 | — | ok |
| positioned-math | qwen-hosted-image | True | — | — | — | 1.214 | — | ok |
| math-actualtext | qwen-hosted-image | True | — | — | — | 0.872 | — | ok |
| accessible-actualtext | qwen-hosted-image | unscored | — | — | — | 1.112 | — | ok |
| two-column-order | qwen-hosted-image | True | — | — | — | 4.597 | — | ok |
| unicode-cmap-and-emoji | qwen-hosted-image | unscored | — | — | — | 1.469 | — | ok |
| table-bordered | qwen-hosted-image | False | 0/9 | 0/12 | — | 2.453 | — | ok |
| table-borderless | qwen-hosted-image | False | 0/9 | 0/12 | — | 1.812 | — | ok |
| table-merged | qwen-hosted-image | False | 0/9 | 0/12 | — | 3.459 | — | ok |
| links-and-outline | qwen-hosted-image | unscored | — | — | — | 1.046 | — | ok |
| images-and-vectors | qwen-hosted-image | unscored | — | — | — | 3.371 | — | ok |
| image-only | qwen-hosted-image | unscored | — | — | — | 1.394 | — | ok |
| table-borderless-aligned | qwen-hosted-image | False | 0/8 | 0/10 | — | 1.764 | — | ok |
| rotated-columns | qwen-hosted-image | True | — | — | — | 3.554 | — | ok |
| footnotes-and-page-furniture | qwen-hosted-image | True | — | — | — | 1.405 | — | ok |
| rtl-visual-glyph-order | qwen-hosted-image | unscored | — | — | — | 1.110 | — | ok |
| tagged-reading-order | qwen-hosted-image | unscored | — | — | — | 1.078 | — | ok |
| corpus-usrguide | qwen-hosted-image | unscored | — | — | — | 13.765 | — | ok |
| corpus-senate-expenditures | qwen-hosted-image | unscored | — | — | 0/23 | 64.013 | — | ok |
| corpus-nics-background-checks-2015-11 | qwen-hosted-image | unscored | — | — | 0/12 | 67.596 | — | truncated |
| corpus-pdfium-type3 | qwen-hosted-image | unscored | — | — | — | 1.247 | — | ok |
| corpus-f1040 | qwen-hosted-image | unscored | — | — | — | 27.950 | — | ok |
| omml-equations | qwen-hosted-image | unscored | — | — | — | 2.319 | — | ok |
| table-borderless-rotate-90 | qwen-hosted-image | False | 0/9 | 0/12 | — | 3.288 | — | ok |
| table-borderless-rotate-180 | qwen-hosted-image | False | 0/9 | 0/12 | — | 1.867 | — | ok |
| table-borderless-rotate-270 | qwen-hosted-image | False | 0/9 | 0/12 | — | 3.352 | — | ok |
| table-borderless-scanned | qwen-hosted-image | False | 0/9 | 0/12 | — | 1.929 | — | ok |
| table-wrapped-records | qwen-hosted-image | False | 0/12 | 0/17 | — | 1.877 | — | ok |
| text-structure-and-literals | qwen-hosted-compact-text | True | — | — | — | 1.893 | — | ok |
| positioned-math | qwen-hosted-compact-text | True | — | — | — | 1.157 | — | ok |
| math-actualtext | qwen-hosted-compact-text | True | — | — | — | 0.812 | — | ok |
| accessible-actualtext | qwen-hosted-compact-text | unscored | — | — | — | 0.622 | — | ok |
| two-column-order | qwen-hosted-compact-text | True | — | — | — | 3.550 | — | ok |
| unicode-cmap-and-emoji | qwen-hosted-compact-text | unscored | — | — | — | 1.264 | — | ok |
| table-bordered | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 1.442 | — | ok |
| table-merged | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 1.557 | — | ok |
| links-and-outline | qwen-hosted-compact-text | unscored | — | — | — | 0.865 | — | ok |
| images-and-vectors | qwen-hosted-compact-text | unscored | — | — | — | 1.024 | — | ok |
| image-only | qwen-hosted-compact-text | unscored | — | — | — | 1.621 | — | ok |
| table-borderless-aligned | qwen-hosted-compact-text | False | 0/8 | 0/10 | — | 1.467 | — | ok |
| rotated-columns | qwen-hosted-compact-text | True | — | — | — | 3.619 | — | ok |
| footnotes-and-page-furniture | qwen-hosted-compact-text | True | — | — | — | 1.131 | — | ok |
| rtl-visual-glyph-order | qwen-hosted-compact-text | unscored | — | — | — | 1.044 | — | ok |
| tagged-reading-order | qwen-hosted-compact-text | unscored | — | — | — | 0.898 | — | ok |
| corpus-usrguide | qwen-hosted-compact-text | unscored | — | — | — | 11.609 | — | ok |
| corpus-senate-expenditures | qwen-hosted-compact-text | unscored | — | — | 0/23 | 55.245 | — | ok |
| corpus-nics-background-checks-2015-11 | qwen-hosted-compact-text | unscored | — | — | 0/12 | 58.616 | — | ok |
| corpus-pdfium-type3 | qwen-hosted-compact-text | unscored | — | — | — | 0.749 | — | ok |
| corpus-f1040 | qwen-hosted-compact-text | unscored | — | — | — | 26.518 | — | ok |
| omml-equations | qwen-hosted-compact-text | unscored | — | — | — | 1.997 | — | ok |
| table-borderless-rotate-90 | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 1.729 | — | ok |
| table-borderless-rotate-180 | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 1.589 | — | ok |
| table-borderless-rotate-270 | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 3.094 | — | ok |
| table-borderless-scanned | qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 1.363 | — | ok |
| table-wrapped-records | qwen-hosted-compact-text | False | 0/12 | 0/17 | — | 1.847 | — | ok |
| text-structure-and-literals | qwen-hosted-compact-patch | True | — | — | — | 0.843 | — | ok |
| positioned-math | qwen-hosted-compact-patch | True | — | — | — | 0.903 | — | ok |
| math-actualtext | qwen-hosted-compact-patch | True | — | — | — | 0.901 | — | ok |
| accessible-actualtext | qwen-hosted-compact-patch | unscored | — | — | — | 0.806 | — | ok |
| two-column-order | qwen-hosted-compact-patch | False | — | — | — | 14.903 | — | ok |
| unicode-cmap-and-emoji | qwen-hosted-compact-patch | unscored | — | — | — | 1.563 | — | ok |
| table-bordered | qwen-hosted-compact-patch | True | 9/9 | 12/12 | — | 2.215 | — | ok |
| table-borderless | qwen-hosted-compact-patch | True | 9/9 | 12/12 | — | 2.214 | — | ok |
| table-merged | qwen-hosted-compact-patch | True | 9/9 | 12/12 | — | 2.649 | — | ok |
| links-and-outline | qwen-hosted-compact-patch | unscored | — | — | — | 0.855 | — | ok |
| images-and-vectors | qwen-hosted-compact-patch | unscored | — | — | — | 0.885 | — | ok |
| image-only | qwen-hosted-compact-patch | unscored | — | — | — | 0.685 | — | ok |
| table-borderless-aligned | qwen-hosted-compact-patch | True | 8/8 | 10/10 | — | 1.786 | — | ok |
| rotated-columns | qwen-hosted-compact-patch | True | — | — | — | 1.189 | — | ok |
| footnotes-and-page-furniture | qwen-hosted-compact-patch | True | — | — | — | 0.786 | — | ok |
| rtl-visual-glyph-order | qwen-hosted-compact-patch | unscored | — | — | — | 1.427 | — | ok |
| tagged-reading-order | qwen-hosted-compact-patch | unscored | — | — | — | 0.890 | — | ok |
| corpus-usrguide | qwen-hosted-compact-patch | unscored | — | — | — | 2.274 | — | ok |
| corpus-senate-expenditures | qwen-hosted-compact-patch | unscored | — | — | — | 76.435 | — | JSONDecodeError: Expecting value: line 320 column 41 (char 8367) |
| corpus-nics-background-checks-2015-11 | qwen-hosted-compact-patch | unscored | — | — | — | 93.845 | — | JSONDecodeError: Unterminated string starting at: line 497 column 12 (char 10324) |
| corpus-pdfium-type3 | qwen-hosted-compact-patch | unscored | — | — | — | 0.817 | — | ok |
| corpus-f1040 | qwen-hosted-compact-patch | unscored | — | — | — | 9.353 | — | ok |
| omml-equations | qwen-hosted-compact-patch | unscored | — | — | — | 0.890 | — | ok |
| table-borderless-rotate-90 | qwen-hosted-compact-patch | True | 9/9 | 12/12 | — | 2.284 | — | ok |
| table-borderless-rotate-180 | qwen-hosted-compact-patch | True | 9/9 | 12/12 | — | 2.264 | — | ok |
| table-borderless-rotate-270 | qwen-hosted-compact-patch | False | 3/9 | 0/12 | — | 1.795 | — | ok |
| table-borderless-scanned | qwen-hosted-compact-patch | False | 0/9 | 0/12 | — | 0.840 | — | ok |
| table-wrapped-records | qwen-hosted-compact-patch | True | 12/12 | 17/17 | — | 3.718 | — | ok |
| text-structure-and-literals | jev-text-gated-geometry-wrapped | True | — | — | — | 0.222 | — | ok |
| positioned-math | jev-text-gated-geometry-wrapped | True | — | — | — | 0.379 | — | ok |
| math-actualtext | jev-text-gated-geometry-wrapped | True | — | — | — | 0.222 | — | ok |
| two-column-order | jev-text-gated-geometry-wrapped | True | — | — | — | 0.305 | — | ok |
| table-bordered | jev-text-gated-geometry-wrapped | True | 9/9 | 12/12 | — | 0.228 | — | ok |
| table-borderless | jev-text-gated-geometry-wrapped | True | 9/9 | 12/12 | — | 0.249 | — | ok |
| table-merged | jev-text-gated-geometry-wrapped | False | 8/9 | 9/12 | — | 0.234 | — | ok |
| table-borderless-aligned | jev-text-gated-geometry-wrapped | True | 8/8 | 10/10 | — | 0.248 | — | ok |
| rotated-columns | jev-text-gated-geometry-wrapped | True | — | — | — | 0.262 | — | ok |
| footnotes-and-page-furniture | jev-text-gated-geometry-wrapped | True | — | — | — | 0.253 | — | ok |
| table-borderless-rotate-90 | jev-text-gated-geometry-wrapped | True | 9/9 | 12/12 | — | 0.227 | — | ok |
| table-borderless-rotate-180 | jev-text-gated-geometry-wrapped | True | 9/9 | 12/12 | — | 0.257 | — | ok |
| table-borderless-rotate-270 | jev-text-gated-geometry-wrapped | True | 9/9 | 12/12 | — | 0.217 | — | ok |
| table-borderless-scanned | jev-text-gated-geometry-wrapped | False | 0/9 | 0/12 | — | 0.286 | — | ok |
| table-wrapped-records | jev-text-gated-geometry-wrapped | True | 12/12 | 17/17 | — | 0.278 | — | ok |
| text-structure-and-literals | qwen-jev-hosted-compact-text | True | — | — | — | 30.752 | — | ok |
| positioned-math | qwen-jev-hosted-compact-text | True | — | — | — | 5.479 | — | ok |
| math-actualtext | qwen-jev-hosted-compact-text | True | — | — | — | 9.500 | — | ok |
| two-column-order | qwen-jev-hosted-compact-text | False | — | — | — | 4.997 | — | ok |
| table-bordered | qwen-jev-hosted-compact-text | True | 9/9 | 12/12 | — | 12.854 | — | ok |
| table-merged | qwen-jev-hosted-compact-text | True | 9/9 | 12/12 | — | 6.598 | — | ok |
| table-borderless-aligned | qwen-jev-hosted-compact-text | True | 8/8 | 10/10 | — | 3.700 | — | ok |
| rotated-columns | qwen-jev-hosted-compact-text | True | — | — | — | 9.296 | — | ok |
| footnotes-and-page-furniture | qwen-jev-hosted-compact-text | unscored | — | — | — | 14.476 | — | TypeError: data must be str, not NoneType |
| corpus-senate-expenditures | qwen-jev-hosted-compact-text | unscored | — | — | 0/23 | 24.920 | — | truncated |
| corpus-nics-background-checks-2015-11 | qwen-jev-hosted-compact-text | unscored | — | — | 0/12 | 23.128 | — | truncated |
| table-borderless-rotate-90 | qwen-jev-hosted-compact-text | unscored | — | — | — | 17.720 | — | TypeError: data must be str, not NoneType |
| table-borderless-rotate-180 | qwen-jev-hosted-compact-text | True | 9/9 | 12/12 | — | 11.956 | — | ok |
| table-borderless-rotate-270 | qwen-jev-hosted-compact-text | True | 9/9 | 12/12 | — | 8.349 | — | ok |
| table-borderless-scanned | qwen-jev-hosted-compact-text | True | 9/9 | 12/12 | — | 4.877 | — | ok |
| table-wrapped-records | qwen-jev-hosted-compact-text | True | 12/12 | 17/17 | — | 5.817 | — | ok |
| text-structure-and-literals | qwen-jev-hosted-compact-patch | True | — | — | — | 13.136 | — | ok |
| positioned-math | qwen-jev-hosted-compact-patch | True | — | — | — | 3.631 | — | ok |
| math-actualtext | qwen-jev-hosted-compact-patch | True | — | — | — | 6.164 | — | ok |
| two-column-order | qwen-jev-hosted-compact-patch | True | — | — | — | 5.810 | — | ok |
| table-bordered | qwen-jev-hosted-compact-patch | True | 9/9 | 12/12 | — | 4.180 | — | ok |
| table-borderless | qwen-jev-hosted-compact-patch | True | 9/9 | 12/12 | — | 16.788 | — | ok |
| table-merged | qwen-jev-hosted-compact-patch | True | 9/9 | 12/12 | — | 7.612 | — | ok |
| table-borderless-aligned | qwen-jev-hosted-compact-patch | True | 8/8 | 10/10 | — | 2.458 | — | ok |
| rotated-columns | qwen-jev-hosted-compact-patch | unscored | — | — | — | 18.960 | — | TypeError: data must be str, not NoneType |
| footnotes-and-page-furniture | qwen-jev-hosted-compact-patch | True | — | — | — | 2.361 | — | ok |
| corpus-senate-expenditures | qwen-jev-hosted-compact-patch | unscored | — | — | — | 10.277 | — | JSONDecodeError: Unterminated string starting at: line 1 column 1751 (char 1750) |
| corpus-nics-background-checks-2015-11 | qwen-jev-hosted-compact-patch | unscored | — | — | — | 51.921 | — | JSONDecodeError: Unterminated string starting at: line 1 column 255 (char 254) |
| table-borderless-rotate-90 | qwen-jev-hosted-compact-patch | unscored | — | — | — | 20.164 | — | TypeError: data must be str, not NoneType |
| table-borderless-rotate-180 | qwen-jev-hosted-compact-patch | unscored | — | — | — | 14.038 | — | TypeError: data must be str, not NoneType |
| table-borderless-rotate-270 | qwen-jev-hosted-compact-patch | unscored | — | — | — | 24.977 | — | TypeError: data must be str, not NoneType |
| table-borderless-scanned | qwen-jev-hosted-compact-patch | unscored | — | — | — | 11.746 | — | TypeError: data must be str, not NoneType |
| table-wrapped-records | qwen-jev-hosted-compact-patch | True | 12/12 | 17/17 | — | 18.176 | — | ok |
| text-structure-and-literals | repair-qwen-hosted-image | True | — | — | — | 0.026 | — | ok |
| positioned-math | repair-qwen-hosted-image | True | — | — | — | 0.008 | — | ok |
| math-actualtext | repair-qwen-hosted-image | True | — | — | — | 0.011 | — | ok |
| accessible-actualtext | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| two-column-order | repair-qwen-hosted-image | True | — | — | — | 0.009 | — | ok |
| unicode-cmap-and-emoji | repair-qwen-hosted-image | unscored | — | — | — | 0.009 | — | ok |
| table-bordered | repair-qwen-hosted-image | True | 9/9 | 12/12 | — | 0.009 | — | ok |
| table-borderless | repair-qwen-hosted-image | True | 9/9 | 12/12 | — | 0.009 | — | ok |
| table-merged | repair-qwen-hosted-image | True | 9/9 | 12/12 | — | 0.008 | — | ok |
| links-and-outline | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| images-and-vectors | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| image-only | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| table-borderless-aligned | repair-qwen-hosted-image | True | 8/8 | 10/10 | — | 0.008 | — | ok |
| rotated-columns | repair-qwen-hosted-image | True | — | — | — | 0.008 | — | ok |
| footnotes-and-page-furniture | repair-qwen-hosted-image | True | — | — | — | 0.010 | — | ok |
| rtl-visual-glyph-order | repair-qwen-hosted-image | unscored | — | — | — | 0.009 | — | ok |
| tagged-reading-order | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| corpus-usrguide | repair-qwen-hosted-image | unscored | — | — | — | 0.009 | — | ok |
| corpus-senate-expenditures | repair-qwen-hosted-image | unscored | — | — | 23/23 | 0.010 | — | ok |
| corpus-nics-background-checks-2015-11 | repair-qwen-hosted-image | unscored | — | — | 0/12 | 0.008 | — | ok |
| corpus-pdfium-type3 | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| corpus-f1040 | repair-qwen-hosted-image | unscored | — | — | — | 0.011 | — | ok |
| omml-equations | repair-qwen-hosted-image | unscored | — | — | — | 0.008 | — | ok |
| table-borderless-rotate-90 | repair-qwen-hosted-image | False | 0/9 | 12/12 | — | 0.008 | — | ok |
| table-borderless-rotate-180 | repair-qwen-hosted-image | False | 7/9 | 6/12 | — | 0.009 | — | ok |
| table-borderless-rotate-270 | repair-qwen-hosted-image | False | 0/9 | 12/12 | — | 0.009 | — | ok |
| table-borderless-scanned | repair-qwen-hosted-image | True | 9/9 | 12/12 | — | 0.009 | — | ok |
| table-wrapped-records | repair-qwen-hosted-image | True | 12/12 | 17/17 | — | 0.010 | — | ok |
| text-structure-and-literals | repair-qwen-hosted-compact-text | True | — | — | — | 0.027 | — | ok |
| positioned-math | repair-qwen-hosted-compact-text | True | — | — | — | 0.009 | — | ok |
| math-actualtext | repair-qwen-hosted-compact-text | True | — | — | — | 0.012 | — | ok |
| accessible-actualtext | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.009 | — | ok |
| two-column-order | repair-qwen-hosted-compact-text | True | — | — | — | 0.009 | — | ok |
| unicode-cmap-and-emoji | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.009 | — | ok |
| table-bordered | repair-qwen-hosted-compact-text | True | 9/9 | 12/12 | — | 0.012 | — | ok |
| table-borderless | repair-qwen-hosted-compact-text | True | 9/9 | 12/12 | — | 0.009 | — | ok |
| table-merged | repair-qwen-hosted-compact-text | False | 8/9 | 9/12 | — | 0.009 | — | ok |
| links-and-outline | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.009 | — | ok |
| images-and-vectors | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.009 | — | ok |
| image-only | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.010 | — | ok |
| table-borderless-aligned | repair-qwen-hosted-compact-text | True | 8/8 | 10/10 | — | 0.010 | — | ok |
| rotated-columns | repair-qwen-hosted-compact-text | True | — | — | — | 0.010 | — | ok |
| footnotes-and-page-furniture | repair-qwen-hosted-compact-text | True | — | — | — | 0.010 | — | ok |
| rtl-visual-glyph-order | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.009 | — | ok |
| tagged-reading-order | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.010 | — | ok |
| corpus-usrguide | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.010 | — | ok |
| corpus-senate-expenditures | repair-qwen-hosted-compact-text | unscored | — | — | 23/23 | 0.012 | — | ok |
| corpus-nics-background-checks-2015-11 | repair-qwen-hosted-compact-text | unscored | — | — | 0/12 | 0.010 | — | ok |
| corpus-pdfium-type3 | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.009 | — | ok |
| corpus-f1040 | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.010 | — | ok |
| omml-equations | repair-qwen-hosted-compact-text | unscored | — | — | — | 0.010 | — | ok |
| table-borderless-rotate-90 | repair-qwen-hosted-compact-text | True | 9/9 | 12/12 | — | 0.011 | — | ok |
| table-borderless-rotate-180 | repair-qwen-hosted-compact-text | True | 9/9 | 12/12 | — | 0.010 | — | ok |
| table-borderless-rotate-270 | repair-qwen-hosted-compact-text | False | 0/9 | 0/12 | — | 0.010 | — | ok |
| table-borderless-scanned | repair-qwen-hosted-compact-text | True | 9/9 | 12/12 | — | 0.010 | — | ok |
| table-wrapped-records | repair-qwen-hosted-compact-text | True | 12/12 | 17/17 | — | 0.010 | — | ok |
| corpus-senate-expenditures | qwen-hosted-compact-row-patch | unscored | — | — | — | 17.835 | — | ValueError: patch spans overlap or cover nonempty cells |
| corpus-nics-background-checks-2015-11 | qwen-hosted-compact-row-patch | unscored | — | — | — | 21.407 | — | ValueError: patch table is ragged |
| corpus-senate-expenditures | qwen-jev-hosted-compact-row-patch | unscored | — | — | — | 25.291 | — | ValueError: region patch exhausted its output token boundary |
| corpus-nics-background-checks-2015-11 | qwen-jev-hosted-compact-row-patch | unscored | — | — | — | 18.444 | — | ValueError: region patch exhausted its output token boundary |

## Run provenance

```json
{
  "started_at": "2026-10-08T04:42:19.263122+00:00",
  "environment": "Linux-7.2.5-3-omarchy-x86_64-with-glibc2.44",
  "python": "3.14.7",
  "source_commit": "aba57936bc4109bf846d96357012f5cb438a5225",
  "remote_spend_authorized_usd": 15,
  "remote_spend_usd": 1.024262108,
  "observation_code_sha256": "5a1f588ac88fc76515aaa9253d93e1b6a249a4311eedfcd4ffc2979b30d665e3",
  "spend_scope": "Shared whole-study total, including API and rental; do not add totals across reports",
  "remote_cleanup_verified": true,
  "spend_breakdown": {
    "reported_at": "2026-10-08T06:16:29.886431+00:00",
    "rental_provider_reported_usd": 0.684,
    "rental_provider_query_at": 1791440003.470863,
    "api_provider_reported_usd": 0.340262108,
    "api_requests": 138,
    "unsettled_api_requests": 0,
    "combined_provider_reported_usd": 1.024262108,
    "authorized_cap_usd": 15,
    "billing_note": "Provider-reported snapshot after destruction; rental rows are rounded to three decimals",
    "instance_id": 54777034,
    "instance_removed": true,
    "archive_sha256": "31a21270168baa6d283aaea4c40ea2aa2b1ea227d798a9a0657a4f66c047c825"
  }
}
```

| Run | Adapter | Initialization seconds | Repetitions | Device | Model |
| --- | --- | ---: | ---: | --- | --- |
| 0 | qwen-hosted-compact-text | 0.032 | 1 | cuda:0 | qwen/qwen3-vl-235b-a22b-instruct |
| 1 | qwen-jev-hosted-compact-text | 0.001 | 1 | cuda:0 | typesafe/jev-router |
| 2 | qwen-hosted-image | 0.018 | 1 | hosted-API | qwen/qwen3-vl-235b-a22b-instruct |
| 3 | qwen-hosted-compact-text | 0.001 | 1 | hosted-API | qwen/qwen3-vl-235b-a22b-instruct |
| 4 | qwen-hosted-compact-patch | 0.001 | 1 | hosted-API | qwen/qwen3-vl-235b-a22b-instruct |
| 5 | jev-text-gated-geometry-wrapped | 0.017 | 1 | hosted-API | typesafe/jev-1.13 |
| 6 | qwen-jev-hosted-compact-text | 0.016 | 1 | hosted-API | typesafe/jev-router |
| 7 | qwen-jev-hosted-compact-patch | 0.015 | 1 | hosted-API | typesafe/jev-router |
| 8 | repair-qwen-hosted-image | 0.015 | 1 | hosted-API | qwen/qwen3-vl-235b-a22b-instruct |
| 9 | repair-qwen-hosted-compact-text | 0.015 | 1 | hosted-API | qwen/qwen3-vl-235b-a22b-instruct |
| 10 | qwen-hosted-compact-row-patch | 0.017 | 1 | hosted-API | qwen/qwen3-vl-235b-a22b-instruct |
| 11 | qwen-jev-hosted-compact-row-patch | 0.001 | 1 | hosted-API | typesafe/jev-router |

Full dependency versions, per-result run indexes, code hashes, and retained-run provenance are in JSON.

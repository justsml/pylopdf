# Structured PDF recovery experiments

Run: 2026-10-08T03:18:26.318705+00:00

Page 0 of each preserved input is evaluated. Full inputs, screenshots, positioned words, prompts,
raw responses, validated patches, and errors are retained locally in `structure-artifacts/`.
Reference cells are independent fixture definitions; corpus cells without a reference remain unscored.
Source agreement is not ground truth, especially for missing Unicode, scans, or OCR corrections.
Geometry bullet results score their underlying recovered cells, not reparsed bullet labels.
Timing covers the adapter after preparation, excluding fixture extraction/rendering; prepared baselines
are replayed, so their timing is not a conversion measurement. Process RSS is cumulative high-water RSS.
Model repetitions include the first inference; initialization is reported separately. No throughput claims.

| Case | Adapter | Exact grid | Cells | Relations recalled | Record cells | Seconds | Result |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| text-structure-and-literals | pylopdf | True | — | — | — | 0.000 | ok |
| positioned-math | pylopdf | True | — | — | — | 0.000 | ok |
| math-actualtext | pylopdf | True | — | — | — | 0.000 | ok |
| accessible-actualtext | pylopdf | unscored | — | — | — | 0.000 | ok |
| two-column-order | pylopdf | True | — | — | — | 0.000 | ok |
| unicode-cmap-and-emoji | pylopdf | unscored | — | — | — | 0.000 | ok |
| table-bordered | pylopdf | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless | pylopdf | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-merged | pylopdf | True | 9/9 | 12/12 | — | 0.000 | ok |
| links-and-outline | pylopdf | unscored | — | — | — | 0.000 | ok |
| images-and-vectors | pylopdf | unscored | — | — | — | 0.000 | ok |
| image-only | pylopdf | unscored | — | — | — | 0.000 | ok |
| table-borderless-aligned | pylopdf | False | 0/8 | 0/10 | — | 0.001 | ok |
| rotated-columns | pylopdf | True | — | — | — | 0.000 | ok |
| footnotes-and-page-furniture | pylopdf | True | — | — | — | 0.000 | ok |
| rtl-visual-glyph-order | pylopdf | unscored | — | — | — | 0.000 | ok |
| tagged-reading-order | pylopdf | unscored | — | — | — | 0.000 | ok |
| corpus-usrguide | pylopdf | unscored | — | — | — | 0.001 | ok |
| corpus-senate-expenditures | pylopdf | unscored | — | — | 0/23 | 0.001 | ok |
| corpus-nics-background-checks-2015-11 | pylopdf | unscored | — | — | 12/12 | 0.019 | ok |
| corpus-pdfium-type3 | pylopdf | unscored | — | — | — | 0.000 | ok |
| corpus-f1040 | pylopdf | unscored | — | — | — | 0.001 | ok |
| omml-equations | pylopdf | unscored | — | — | — | 0.000 | ok |
| table-borderless-rotate-90 | pylopdf | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-borderless-rotate-180 | pylopdf | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-borderless-rotate-270 | pylopdf | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-borderless-scanned | pylopdf | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-wrapped-records | pylopdf | False | 0/12 | 0/17 | — | 0.000 | ok |
| text-structure-and-literals | pylopdf-text | True | — | — | — | 0.000 | ok |
| positioned-math | pylopdf-text | True | — | — | — | 0.000 | ok |
| math-actualtext | pylopdf-text | True | — | — | — | 0.000 | ok |
| accessible-actualtext | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| two-column-order | pylopdf-text | False | — | — | — | 0.000 | ok |
| unicode-cmap-and-emoji | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| table-bordered | pylopdf-text | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless | pylopdf-text | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-merged | pylopdf-text | True | 9/9 | 12/12 | — | 0.000 | ok |
| links-and-outline | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| images-and-vectors | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| image-only | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| table-borderless-aligned | pylopdf-text | True | 8/8 | 10/10 | — | 0.000 | ok |
| rotated-columns | pylopdf-text | True | — | — | — | 0.000 | ok |
| footnotes-and-page-furniture | pylopdf-text | True | — | — | — | 0.000 | ok |
| rtl-visual-glyph-order | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| tagged-reading-order | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| corpus-usrguide | pylopdf-text | unscored | — | — | — | 0.001 | ok |
| corpus-senate-expenditures | pylopdf-text | unscored | — | — | 0/23 | 0.001 | ok |
| corpus-nics-background-checks-2015-11 | pylopdf-text | unscored | — | — | 12/12 | 0.017 | ok |
| corpus-pdfium-type3 | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| corpus-f1040 | pylopdf-text | unscored | — | — | — | 0.002 | ok |
| omml-equations | pylopdf-text | unscored | — | — | — | 0.000 | ok |
| table-borderless-rotate-90 | pylopdf-text | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-borderless-rotate-180 | pylopdf-text | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-borderless-rotate-270 | pylopdf-text | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-borderless-scanned | pylopdf-text | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-wrapped-records | pylopdf-text | False | 0/12 | 0/17 | — | 0.000 | ok |
| text-structure-and-literals | yolo-geometry | True | — | — | — | 2.317 | ok |
| positioned-math | yolo-geometry | True | — | — | — | 0.041 | ok |
| math-actualtext | yolo-geometry | True | — | — | — | 0.039 | ok |
| accessible-actualtext | yolo-geometry | unscored | — | — | — | 0.038 | ok |
| two-column-order | yolo-geometry | True | — | — | — | 0.042 | ok |
| unicode-cmap-and-emoji | yolo-geometry | unscored | — | — | — | 0.093 | ok |
| table-bordered | yolo-geometry | True | 9/9 | 12/12 | — | 0.041 | ok |
| table-borderless | yolo-geometry | True | 9/9 | 12/12 | — | 0.040 | ok |
| table-merged | yolo-geometry | False | 8/9 | 9/12 | — | 0.040 | ok |
| links-and-outline | yolo-geometry | unscored | — | — | — | 0.040 | ok |
| images-and-vectors | yolo-geometry | unscored | — | — | — | 0.040 | ok |
| image-only | yolo-geometry | unscored | — | — | — | 0.039 | ok |
| table-borderless-aligned | yolo-geometry | True | 8/8 | 10/10 | — | 0.040 | ok |
| rotated-columns | yolo-geometry | True | — | — | — | 0.114 | ok |
| footnotes-and-page-furniture | yolo-geometry | True | — | — | — | 0.041 | ok |
| rtl-visual-glyph-order | yolo-geometry | unscored | — | — | — | 0.035 | ok |
| tagged-reading-order | yolo-geometry | unscored | — | — | — | 0.040 | ok |
| corpus-usrguide | yolo-geometry | unscored | — | — | — | 0.046 | ok |
| corpus-senate-expenditures | yolo-geometry | unscored | — | — | 0/23 | 0.049 | ok |
| corpus-nics-background-checks-2015-11 | yolo-geometry | unscored | — | — | 6/12 | 0.107 | ok |
| corpus-pdfium-type3 | yolo-geometry | unscored | — | — | — | 0.101 | ok |
| corpus-f1040 | yolo-geometry | unscored | — | — | — | 0.056 | ok |
| omml-equations | yolo-geometry | unscored | — | — | — | 0.040 | ok |
| table-borderless-rotate-90 | yolo-geometry | False | 0/9 | 0/12 | — | 0.041 | ok |
| table-borderless-rotate-180 | yolo-geometry | False | 0/9 | 0/12 | — | 0.041 | ok |
| table-borderless-rotate-270 | yolo-geometry | False | 0/9 | 0/12 | — | 0.041 | ok |
| table-borderless-scanned | yolo-geometry | False | 0/9 | 0/12 | — | 0.040 | ok |
| table-wrapped-records | yolo-geometry | False | 0/12 | 0/17 | — | 0.039 | ok |
| text-structure-and-literals | yolo-geometry-wrapped | True | — | — | — | 0.194 | ok |
| positioned-math | yolo-geometry-wrapped | True | — | — | — | 0.040 | ok |
| math-actualtext | yolo-geometry-wrapped | True | — | — | — | 0.040 | ok |
| accessible-actualtext | yolo-geometry-wrapped | unscored | — | — | — | 0.038 | ok |
| two-column-order | yolo-geometry-wrapped | True | — | — | — | 0.042 | ok |
| unicode-cmap-and-emoji | yolo-geometry-wrapped | unscored | — | — | — | 0.035 | ok |
| table-bordered | yolo-geometry-wrapped | True | 9/9 | 12/12 | — | 0.041 | ok |
| table-borderless | yolo-geometry-wrapped | True | 9/9 | 12/12 | — | 0.039 | ok |
| table-merged | yolo-geometry-wrapped | False | 8/9 | 9/12 | — | 0.040 | ok |
| links-and-outline | yolo-geometry-wrapped | unscored | — | — | — | 0.039 | ok |
| images-and-vectors | yolo-geometry-wrapped | unscored | — | — | — | 0.039 | ok |
| image-only | yolo-geometry-wrapped | unscored | — | — | — | 0.038 | ok |
| table-borderless-aligned | yolo-geometry-wrapped | True | 8/8 | 10/10 | — | 0.040 | ok |
| rotated-columns | yolo-geometry-wrapped | True | — | — | — | 0.043 | ok |
| footnotes-and-page-furniture | yolo-geometry-wrapped | True | — | — | — | 0.041 | ok |
| rtl-visual-glyph-order | yolo-geometry-wrapped | unscored | — | — | — | 0.036 | ok |
| tagged-reading-order | yolo-geometry-wrapped | unscored | — | — | — | 0.039 | ok |
| corpus-usrguide | yolo-geometry-wrapped | unscored | — | — | — | 0.045 | ok |
| corpus-senate-expenditures | yolo-geometry-wrapped | unscored | — | — | 0/23 | 0.049 | ok |
| corpus-nics-background-checks-2015-11 | yolo-geometry-wrapped | unscored | — | — | 6/12 | 0.049 | ok |
| corpus-pdfium-type3 | yolo-geometry-wrapped | unscored | — | — | — | 0.037 | ok |
| corpus-f1040 | yolo-geometry-wrapped | unscored | — | — | — | 0.056 | ok |
| omml-equations | yolo-geometry-wrapped | unscored | — | — | — | 0.041 | ok |
| table-borderless-rotate-90 | yolo-geometry-wrapped | False | 0/9 | 0/12 | — | 0.041 | ok |
| table-borderless-rotate-180 | yolo-geometry-wrapped | False | 0/9 | 0/12 | — | 0.040 | ok |
| table-borderless-rotate-270 | yolo-geometry-wrapped | False | 0/9 | 0/12 | — | 0.041 | ok |
| table-borderless-scanned | yolo-geometry-wrapped | False | 0/9 | 0/12 | — | 0.040 | ok |
| table-wrapped-records | yolo-geometry-wrapped | True | 12/12 | 17/17 | — | 0.040 | ok |
| text-structure-and-literals | olmocr-image | True | — | — | — | 4.322 | ok |
| positioned-math | olmocr-image | True | — | — | — | 2.026 | ok |
| math-actualtext | olmocr-image | True | — | — | — | 1.549 | ok |
| accessible-actualtext | olmocr-image | unscored | — | — | — | 1.546 | ok |
| two-column-order | olmocr-image | True | — | — | — | 5.033 | ok |
| unicode-cmap-and-emoji | olmocr-image | unscored | — | — | — | 1.402 | ok |
| table-bordered | olmocr-image | False | 8/9 | 9/12 | — | 4.092 | ok |
| table-borderless | olmocr-image | True | 9/9 | 12/12 | — | 4.343 | ok |
| table-merged | olmocr-image | False | 8/9 | 9/12 | — | 4.729 | ok |
| links-and-outline | olmocr-image | unscored | — | — | — | 1.995 | ok |
| images-and-vectors | olmocr-image | unscored | — | — | — | 2.702 | ok |
| image-only | olmocr-image | unscored | — | — | — | 1.610 | ok |
| table-borderless-aligned | olmocr-image | True | 8/8 | 10/10 | — | 4.567 | ok |
| rotated-columns | olmocr-image | True | — | — | — | 5.661 | ok |
| footnotes-and-page-furniture | olmocr-image | True | — | — | — | 2.333 | ok |
| rtl-visual-glyph-order | olmocr-image | unscored | — | — | — | 1.674 | ok |
| tagged-reading-order | olmocr-image | unscored | — | — | — | 1.993 | ok |
| corpus-usrguide | olmocr-image | unscored | — | — | — | 19.079 | ok |
| corpus-senate-expenditures | olmocr-image | unscored | — | — | 0/23 | 93.437 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-image | unscored | — | — | 0/12 | 119.902 | truncated |
| corpus-pdfium-type3 | olmocr-image | unscored | — | — | — | 1.995 | ok |
| corpus-f1040 | olmocr-image | unscored | — | — | — | 49.383 | ok |
| omml-equations | olmocr-image | unscored | — | — | — | 4.013 | ok |
| table-borderless-rotate-90 | olmocr-image | False | 8/9 | 9/12 | — | 5.052 | ok |
| table-borderless-rotate-180 | olmocr-image | False | 0/9 | 6/12 | — | 5.412 | ok |
| table-borderless-rotate-270 | olmocr-image | False | 3/9 | 6/12 | — | 5.752 | ok |
| table-borderless-scanned | olmocr-image | True | 9/9 | 12/12 | — | 5.085 | ok |
| table-wrapped-records | olmocr-image | True | 12/12 | 17/17 | — | 6.142 | ok |
| text-structure-and-literals | olmocr-text | True | — | — | — | 3.723 | ok |
| positioned-math | olmocr-text | True | — | — | — | 2.484 | ok |
| math-actualtext | olmocr-text | True | — | — | — | 1.816 | ok |
| accessible-actualtext | olmocr-text | unscored | — | — | — | 1.840 | ok |
| two-column-order | olmocr-text | True | — | — | — | 8.389 | ok |
| unicode-cmap-and-emoji | olmocr-text | unscored | — | — | — | 2.859 | ok |
| table-bordered | olmocr-text | False | 8/9 | 9/12 | — | 4.745 | ok |
| table-borderless | olmocr-text | False | 8/9 | 9/12 | — | 4.814 | ok |
| table-merged | olmocr-text | False | 8/9 | 9/12 | — | 4.892 | ok |
| links-and-outline | olmocr-text | unscored | — | — | — | 2.326 | ok |
| images-and-vectors | olmocr-text | unscored | — | — | — | 3.044 | ok |
| image-only | olmocr-text | unscored | — | — | — | 1.926 | ok |
| table-borderless-aligned | olmocr-text | True | 8/8 | 10/10 | — | 4.781 | ok |
| rotated-columns | olmocr-text | True | — | — | — | 9.365 | ok |
| footnotes-and-page-furniture | olmocr-text | True | — | — | — | 2.747 | ok |
| rtl-visual-glyph-order | olmocr-text | unscored | — | — | — | 2.299 | ok |
| tagged-reading-order | olmocr-text | unscored | — | — | — | 2.257 | ok |
| corpus-usrguide | olmocr-text | unscored | — | — | — | 29.877 | ok |
| corpus-senate-expenditures | olmocr-text | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 2.26 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.66 GiB is free. Process |
| corpus-nics-background-checks-2015-11 | olmocr-text | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 4.09 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.25 GiB is free. Process |
| corpus-pdfium-type3 | olmocr-text | unscored | — | — | — | 4.923 | ok |
| corpus-f1040 | olmocr-text | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 3.04 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.26 GiB is free. Process |
| omml-equations | olmocr-text | unscored | — | — | — | 4.819 | ok |
| table-borderless-rotate-90 | olmocr-text | False | 0/9 | 9/12 | — | 5.735 | ok |
| table-borderless-rotate-180 | olmocr-text | False | 0/9 | 9/12 | — | 5.519 | ok |
| table-borderless-rotate-270 | olmocr-text | False | 8/9 | 9/12 | — | 4.932 | ok |
| table-borderless-scanned | olmocr-text | True | 9/9 | 12/12 | — | 4.916 | ok |
| table-wrapped-records | olmocr-text | True | 12/12 | 17/17 | — | 6.426 | ok |
| text-structure-and-literals | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| positioned-math | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| math-actualtext | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| accessible-actualtext | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| two-column-order | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| unicode-cmap-and-emoji | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-bordered | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-borderless | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-merged | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| links-and-outline | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| images-and-vectors | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| image-only | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-borderless-aligned | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| rotated-columns | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| footnotes-and-page-furniture | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| rtl-visual-glyph-order | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| tagged-reading-order | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| corpus-usrguide | olmocr-patch | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 1.18 GiB. GPU 0 has a total capacity of 23.56 GiB of which 490.19 MiB is free. Proce |
| corpus-senate-expenditures | olmocr-patch | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 2.26 GiB. GPU 0 has a total capacity of 23.56 GiB of which 2.16 GiB is free. Process |
| corpus-nics-background-checks-2015-11 | olmocr-patch | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 4.09 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.54 GiB is free. Process |
| corpus-pdfium-type3 | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| corpus-f1040 | olmocr-patch | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 3.04 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.54 GiB is free. Process |
| omml-equations | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-borderless-rotate-90 | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-borderless-rotate-180 | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-borderless-rotate-270 | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| table-borderless-scanned | olmocr-patch | unscored | — | — | — | 0.000 | JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| table-wrapped-records | olmocr-patch | unscored | — | — | — | 0.000 | AttributeError: 'list' object has no attribute 'get' |
| text-structure-and-literals | geometry | True | — | — | — | 0.000 | ok |
| positioned-math | geometry | True | — | — | — | 0.000 | ok |
| math-actualtext | geometry | True | — | — | — | 0.000 | ok |
| accessible-actualtext | geometry | unscored | — | — | — | 0.000 | ok |
| two-column-order | geometry | False | — | — | — | 0.000 | ok |
| unicode-cmap-and-emoji | geometry | unscored | — | — | — | 0.000 | ok |
| table-bordered | geometry | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless | geometry | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-merged | geometry | False | 8/9 | 9/12 | — | 0.000 | ok |
| links-and-outline | geometry | unscored | — | — | — | 0.000 | ok |
| images-and-vectors | geometry | unscored | — | — | — | 0.000 | ok |
| image-only | geometry | unscored | — | — | — | 0.000 | ok |
| table-borderless-aligned | geometry | True | 8/8 | 10/10 | — | 0.000 | ok |
| rotated-columns | geometry | False | — | — | — | 0.000 | ok |
| footnotes-and-page-furniture | geometry | True | — | — | — | 0.000 | ok |
| rtl-visual-glyph-order | geometry | unscored | — | — | — | 0.000 | ok |
| tagged-reading-order | geometry | unscored | — | — | — | 0.000 | ok |
| corpus-usrguide | geometry | unscored | — | — | — | 0.000 | ok |
| corpus-senate-expenditures | geometry | unscored | — | — | 6/23 | 0.001 | ok |
| corpus-nics-background-checks-2015-11 | geometry | unscored | — | — | 6/12 | 0.006 | ok |
| corpus-pdfium-type3 | geometry | unscored | — | — | — | 0.000 | ok |
| corpus-f1040 | geometry | unscored | — | — | — | 0.002 | ok |
| omml-equations | geometry | unscored | — | — | — | 0.000 | ok |
| table-borderless-rotate-90 | geometry | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-180 | geometry | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-270 | geometry | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-scanned | geometry | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-wrapped-records | geometry | False | 0/12 | 0/17 | — | 0.000 | ok |
| text-structure-and-literals | geometry-bullets | True | — | — | — | 0.000 | ok |
| positioned-math | geometry-bullets | True | — | — | — | 0.000 | ok |
| math-actualtext | geometry-bullets | True | — | — | — | 0.000 | ok |
| accessible-actualtext | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| two-column-order | geometry-bullets | False | — | — | — | 0.000 | ok |
| unicode-cmap-and-emoji | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| table-bordered | geometry-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless | geometry-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-merged | geometry-bullets | False | 8/9 | 9/12 | — | 0.000 | ok |
| links-and-outline | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| images-and-vectors | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| image-only | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| table-borderless-aligned | geometry-bullets | True | 8/8 | 10/10 | — | 0.000 | ok |
| rotated-columns | geometry-bullets | False | — | — | — | 0.000 | ok |
| footnotes-and-page-furniture | geometry-bullets | True | — | — | — | 0.000 | ok |
| rtl-visual-glyph-order | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| tagged-reading-order | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| corpus-usrguide | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| corpus-senate-expenditures | geometry-bullets | unscored | — | — | 6/23 | 0.001 | ok |
| corpus-nics-background-checks-2015-11 | geometry-bullets | unscored | — | — | 6/12 | 0.006 | ok |
| corpus-pdfium-type3 | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| corpus-f1040 | geometry-bullets | unscored | — | — | — | 0.002 | ok |
| omml-equations | geometry-bullets | unscored | — | — | — | 0.000 | ok |
| table-borderless-rotate-90 | geometry-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-180 | geometry-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-270 | geometry-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-scanned | geometry-bullets | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-wrapped-records | geometry-bullets | False | 0/12 | 0/17 | — | 0.000 | ok |
| text-structure-and-literals | geometry-wrapped | True | — | — | — | 0.000 | ok |
| positioned-math | geometry-wrapped | True | — | — | — | 0.000 | ok |
| math-actualtext | geometry-wrapped | True | — | — | — | 0.000 | ok |
| accessible-actualtext | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| two-column-order | geometry-wrapped | False | — | — | — | 0.000 | ok |
| unicode-cmap-and-emoji | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| table-bordered | geometry-wrapped | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless | geometry-wrapped | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-merged | geometry-wrapped | False | 8/9 | 9/12 | — | 0.000 | ok |
| links-and-outline | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| images-and-vectors | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| image-only | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| table-borderless-aligned | geometry-wrapped | True | 8/8 | 10/10 | — | 0.000 | ok |
| rotated-columns | geometry-wrapped | False | — | — | — | 0.000 | ok |
| footnotes-and-page-furniture | geometry-wrapped | True | — | — | — | 0.000 | ok |
| rtl-visual-glyph-order | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| tagged-reading-order | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| corpus-usrguide | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| corpus-senate-expenditures | geometry-wrapped | unscored | — | — | 23/23 | 0.001 | ok |
| corpus-nics-background-checks-2015-11 | geometry-wrapped | unscored | — | — | 6/12 | 0.006 | ok |
| corpus-pdfium-type3 | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| corpus-f1040 | geometry-wrapped | unscored | — | — | — | 0.002 | ok |
| omml-equations | geometry-wrapped | unscored | — | — | — | 0.000 | ok |
| table-borderless-rotate-90 | geometry-wrapped | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-180 | geometry-wrapped | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-270 | geometry-wrapped | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-scanned | geometry-wrapped | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-wrapped-records | geometry-wrapped | True | 12/12 | 17/17 | — | 0.000 | ok |
| text-structure-and-literals | geometry-wrapped-bullets | True | — | — | — | 0.000 | ok |
| positioned-math | geometry-wrapped-bullets | True | — | — | — | 0.000 | ok |
| math-actualtext | geometry-wrapped-bullets | True | — | — | — | 0.000 | ok |
| accessible-actualtext | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| two-column-order | geometry-wrapped-bullets | False | — | — | — | 0.001 | ok |
| unicode-cmap-and-emoji | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| table-bordered | geometry-wrapped-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless | geometry-wrapped-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-merged | geometry-wrapped-bullets | False | 8/9 | 9/12 | — | 0.000 | ok |
| links-and-outline | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| images-and-vectors | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| image-only | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| table-borderless-aligned | geometry-wrapped-bullets | True | 8/8 | 10/10 | — | 0.000 | ok |
| rotated-columns | geometry-wrapped-bullets | False | — | — | — | 0.000 | ok |
| footnotes-and-page-furniture | geometry-wrapped-bullets | True | — | — | — | 0.000 | ok |
| rtl-visual-glyph-order | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| tagged-reading-order | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| corpus-usrguide | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| corpus-senate-expenditures | geometry-wrapped-bullets | unscored | — | — | 23/23 | 0.001 | ok |
| corpus-nics-background-checks-2015-11 | geometry-wrapped-bullets | unscored | — | — | 6/12 | 0.006 | ok |
| corpus-pdfium-type3 | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| corpus-f1040 | geometry-wrapped-bullets | unscored | — | — | — | 0.002 | ok |
| omml-equations | geometry-wrapped-bullets | unscored | — | — | — | 0.000 | ok |
| table-borderless-rotate-90 | geometry-wrapped-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-180 | geometry-wrapped-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-rotate-270 | geometry-wrapped-bullets | True | 9/9 | 12/12 | — | 0.000 | ok |
| table-borderless-scanned | geometry-wrapped-bullets | False | 0/9 | 0/12 | — | 0.000 | ok |
| table-wrapped-records | geometry-wrapped-bullets | True | 12/12 | 17/17 | — | 0.000 | ok |
| text-structure-and-literals | native-bullets | True | — | — | — | 0.010 | ok |
| positioned-math | native-bullets | True | — | — | — | 0.009 | ok |
| math-actualtext | native-bullets | True | — | — | — | 0.009 | ok |
| accessible-actualtext | native-bullets | unscored | — | — | — | 0.009 | ok |
| two-column-order | native-bullets | True | — | — | — | 0.011 | ok |
| unicode-cmap-and-emoji | native-bullets | unscored | — | — | — | 0.010 | ok |
| table-bordered | native-bullets | True | 9/9 | 12/12 | — | 0.009 | ok |
| table-borderless | native-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-merged | native-bullets | False | 8/9 | 9/12 | — | 0.010 | ok |
| links-and-outline | native-bullets | unscored | — | — | — | 0.009 | ok |
| images-and-vectors | native-bullets | unscored | — | — | — | 0.009 | ok |
| image-only | native-bullets | unscored | — | — | — | 0.009 | ok |
| table-borderless-aligned | native-bullets | False | 0/8 | 0/10 | — | 0.009 | ok |
| rotated-columns | native-bullets | True | — | — | — | 0.011 | ok |
| footnotes-and-page-furniture | native-bullets | True | — | — | — | 0.009 | ok |
| rtl-visual-glyph-order | native-bullets | unscored | — | — | — | 0.010 | ok |
| tagged-reading-order | native-bullets | unscored | — | — | — | 0.009 | ok |
| corpus-usrguide | native-bullets | unscored | — | — | — | 0.015 | ok |
| corpus-senate-expenditures | native-bullets | unscored | — | — | 0/23 | 0.014 | ok |
| corpus-nics-background-checks-2015-11 | native-bullets | unscored | — | — | 12/12 | 0.037 | ok |
| corpus-pdfium-type3 | native-bullets | unscored | — | — | — | 0.010 | ok |
| corpus-f1040 | native-bullets | unscored | — | — | — | 0.020 | ok |
| omml-equations | native-bullets | unscored | — | — | — | 0.010 | ok |
| table-borderless-rotate-90 | native-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-borderless-rotate-180 | native-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-borderless-rotate-270 | native-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-borderless-scanned | native-bullets | False | 0/9 | 0/12 | — | 0.012 | ok |
| table-wrapped-records | native-bullets | False | 0/12 | 0/17 | — | 0.009 | ok |
| text-structure-and-literals | yolo-normalized-geometry-wrapped | True | — | — | — | 2.125 | ok |
| positioned-math | yolo-normalized-geometry-wrapped | True | — | — | — | 0.041 | ok |
| math-actualtext | yolo-normalized-geometry-wrapped | True | — | — | — | 0.041 | ok |
| accessible-actualtext | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.039 | ok |
| two-column-order | yolo-normalized-geometry-wrapped | True | — | — | — | 0.043 | ok |
| unicode-cmap-and-emoji | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.091 | ok |
| table-bordered | yolo-normalized-geometry-wrapped | True | 9/9 | 12/12 | — | 0.041 | ok |
| table-borderless | yolo-normalized-geometry-wrapped | True | 9/9 | 12/12 | — | 0.041 | ok |
| table-merged | yolo-normalized-geometry-wrapped | False | 8/9 | 9/12 | — | 0.041 | ok |
| links-and-outline | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.042 | ok |
| images-and-vectors | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.040 | ok |
| image-only | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.039 | ok |
| table-borderless-aligned | yolo-normalized-geometry-wrapped | True | 8/8 | 10/10 | — | 0.041 | ok |
| rotated-columns | yolo-normalized-geometry-wrapped | True | — | — | — | 0.044 | ok |
| footnotes-and-page-furniture | yolo-normalized-geometry-wrapped | True | — | — | — | 0.040 | ok |
| rtl-visual-glyph-order | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.035 | ok |
| tagged-reading-order | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.039 | ok |
| corpus-usrguide | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.045 | ok |
| corpus-senate-expenditures | yolo-normalized-geometry-wrapped | unscored | — | — | 23/23 | 0.107 | ok |
| corpus-nics-background-checks-2015-11 | yolo-normalized-geometry-wrapped | unscored | — | — | 6/12 | 0.105 | ok |
| corpus-pdfium-type3 | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.114 | ok |
| corpus-f1040 | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.056 | ok |
| omml-equations | yolo-normalized-geometry-wrapped | unscored | — | — | — | 0.040 | ok |
| table-borderless-rotate-90 | yolo-normalized-geometry-wrapped | True | 9/9 | 12/12 | — | 0.042 | ok |
| table-borderless-rotate-180 | yolo-normalized-geometry-wrapped | True | 9/9 | 12/12 | — | 0.040 | ok |
| table-borderless-rotate-270 | yolo-normalized-geometry-wrapped | True | 9/9 | 12/12 | — | 0.040 | ok |
| table-borderless-scanned | yolo-normalized-geometry-wrapped | False | 0/9 | 0/12 | — | 0.039 | ok |
| table-wrapped-records | yolo-normalized-geometry-wrapped | True | 12/12 | 17/17 | — | 0.040 | ok |
| text-structure-and-literals | qwen-image | True | — | — | — | 3.490 | ok |
| positioned-math | qwen-image | True | — | — | — | 1.401 | ok |
| math-actualtext | qwen-image | True | — | — | — | 1.400 | ok |
| accessible-actualtext | qwen-image | unscored | — | — | — | 1.306 | ok |
| two-column-order | qwen-image | True | — | — | — | 9.615 | ok |
| unicode-cmap-and-emoji | qwen-image | unscored | — | — | — | 18.956 | ok |
| table-bordered | qwen-image | False | 0/9 | 0/12 | — | 2.049 | ok |
| table-borderless | qwen-image | False | 0/9 | 0/12 | — | 3.886 | ok |
| table-merged | qwen-image | False | 0/9 | 0/12 | — | 1.831 | ok |
| links-and-outline | qwen-image | unscored | — | — | — | 1.296 | ok |
| images-and-vectors | qwen-image | unscored | — | — | — | 34.456 | ok |
| image-only | qwen-image | unscored | — | — | — | 1.746 | ok |
| table-borderless-aligned | qwen-image | False | 0/8 | 0/10 | — | 4.104 | ok |
| rotated-columns | qwen-image | True | — | — | — | 9.292 | ok |
| footnotes-and-page-furniture | qwen-image | True | — | — | — | 3.707 | ok |
| rtl-visual-glyph-order | qwen-image | unscored | — | — | — | 16.333 | ok |
| tagged-reading-order | qwen-image | unscored | — | — | — | 1.923 | ok |
| corpus-usrguide | qwen-image | unscored | — | — | — | 13.389 | ok |
| corpus-senate-expenditures | qwen-image | unscored | — | — | 0/23 | 101.120 | ok |
| corpus-nics-background-checks-2015-11 | qwen-image | unscored | — | — | 0/12 | 119.102 | truncated |
| corpus-pdfium-type3 | qwen-image | unscored | — | — | — | 1.330 | ok |
| corpus-f1040 | qwen-image | unscored | — | — | — | 86.313 | ok |
| omml-equations | qwen-image | unscored | — | — | — | 3.992 | ok |
| table-borderless-rotate-90 | qwen-image | False | 0/9 | 0/12 | — | 4.391 | ok |
| table-borderless-rotate-180 | qwen-image | False | 0/9 | 0/12 | — | 3.791 | ok |
| table-borderless-rotate-270 | qwen-image | False | 0/9 | 0/12 | — | 4.081 | ok |
| table-borderless-scanned | qwen-image | False | 0/9 | 0/12 | — | 3.981 | ok |
| table-wrapped-records | qwen-image | False | 0/12 | 0/17 | — | 5.573 | ok |
| text-structure-and-literals | qwen-text | True | — | — | — | 3.149 | ok |
| positioned-math | qwen-text | True | — | — | — | 1.606 | ok |
| math-actualtext | qwen-text | True | — | — | — | 0.897 | ok |
| accessible-actualtext | qwen-text | unscored | — | — | — | 0.927 | ok |
| two-column-order | qwen-text | True | — | — | — | 11.034 | ok |
| unicode-cmap-and-emoji | qwen-text | unscored | — | — | — | 2.351 | ok |
| table-bordered | qwen-text | False | 0/9 | 0/12 | — | 1.922 | ok |
| table-borderless | qwen-text | False | 0/9 | 0/12 | — | 1.922 | ok |
| table-merged | qwen-text | False | 0/9 | 0/12 | — | 1.890 | ok |
| links-and-outline | qwen-text | unscored | — | — | — | 1.442 | ok |
| images-and-vectors | qwen-text | unscored | — | — | — | 2.554 | ok |
| image-only | qwen-text | unscored | — | — | — | 1.409 | ok |
| table-borderless-aligned | qwen-text | False | 0/8 | 0/10 | — | 1.809 | ok |
| rotated-columns | qwen-text | True | — | — | — | 11.139 | ok |
| footnotes-and-page-furniture | qwen-text | True | — | — | — | 1.681 | ok |
| rtl-visual-glyph-order | qwen-text | unscored | — | — | — | 1.207 | ok |
| tagged-reading-order | qwen-text | unscored | — | — | — | 1.027 | ok |
| corpus-usrguide | qwen-text | unscored | — | — | — | 14.689 | ok |
| corpus-senate-expenditures | qwen-text | unscored | — | — | 0/23 | 146.628 | truncated |
| corpus-nics-background-checks-2015-11 | qwen-text | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 2.37 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.45 GiB is free. Process |
| corpus-pdfium-type3 | qwen-text | unscored | — | — | — | 55.771 | ok |
| corpus-f1040 | qwen-text | unscored | — | — | — | 49.757 | ok |
| omml-equations | qwen-text | unscored | — | — | — | 3.009 | ok |
| table-borderless-rotate-90 | qwen-text | False | 0/9 | 0/12 | — | 120.836 | truncated |
| table-borderless-rotate-180 | qwen-text | False | 0/9 | 0/12 | — | 2.284 | ok |
| table-borderless-rotate-270 | qwen-text | False | 0/9 | 0/12 | — | 120.879 | truncated |
| table-borderless-scanned | qwen-text | False | 0/9 | 0/12 | — | 4.069 | ok |
| table-wrapped-records | qwen-text | False | 0/12 | 0/17 | — | 5.307 | ok |
| text-structure-and-literals | qwen-patch | False | — | — | — | 11.073 | ok |
| positioned-math | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| math-actualtext | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| accessible-actualtext | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| two-column-order | qwen-patch | unscored | — | — | — | 0.000 | TypeError: each cell must contain a list of source word IDs |
| unicode-cmap-and-emoji | qwen-patch | unscored | — | — | — | 0.000 | TypeError: each cell must contain a list of source word IDs |
| table-bordered | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-borderless | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-merged | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| links-and-outline | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| images-and-vectors | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| image-only | qwen-patch | unscored | — | — | — | 0.000 | JSONDecodeError: Expecting value: line 5 column 1 (char 182) |
| table-borderless-aligned | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| rotated-columns | qwen-patch | unscored | — | — | — | 0.000 | TypeError: each cell must contain a list of source word IDs |
| footnotes-and-page-furniture | qwen-patch | False | — | — | — | 2.632 | ok |
| rtl-visual-glyph-order | qwen-patch | unscored | — | — | — | 0.000 | TypeError: each cell must contain a list of source word IDs |
| tagged-reading-order | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| corpus-usrguide | qwen-patch | unscored | — | — | — | 0.000 | JSONDecodeError: Unterminated string starting at: line 251 column 10 (char 7811) |
| corpus-senate-expenditures | qwen-patch | unscored | — | — | — | 0.000 | JSONDecodeError: Unterminated string starting at: line 973 column 15 (char 15909) |
| corpus-nics-background-checks-2015-11 | qwen-patch | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 2.38 GiB. GPU 0 has a total capacity of 23.56 GiB of which 1.82 GiB is free. Process |
| corpus-pdfium-type3 | qwen-patch | unscored | — | — | — | 0.000 | TypeError: each cell must contain a list of source word IDs |
| corpus-f1040 | qwen-patch | unscored | — | — | — | 0.000 | JSONDecodeError: Expecting value: line 1 column 1 (char 0) |
| omml-equations | qwen-patch | unscored | — | — | — | 8.790 | ok |
| table-borderless-rotate-90 | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-borderless-rotate-180 | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-borderless-rotate-270 | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-borderless-scanned | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-wrapped-records | qwen-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| text-structure-and-literals | native-header-bullets | True | — | — | — | 0.034 | ok |
| positioned-math | native-header-bullets | True | — | — | — | 0.033 | ok |
| math-actualtext | native-header-bullets | True | — | — | — | 0.031 | ok |
| accessible-actualtext | native-header-bullets | unscored | — | — | — | 0.031 | ok |
| two-column-order | native-header-bullets | True | — | — | — | 0.013 | ok |
| unicode-cmap-and-emoji | native-header-bullets | unscored | — | — | — | 0.010 | ok |
| table-bordered | native-header-bullets | True | 9/9 | 12/12 | — | 0.010 | ok |
| table-borderless | native-header-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-merged | native-header-bullets | False | 8/9 | 9/12 | — | 0.010 | ok |
| links-and-outline | native-header-bullets | unscored | — | — | — | 0.009 | ok |
| images-and-vectors | native-header-bullets | unscored | — | — | — | 0.009 | ok |
| image-only | native-header-bullets | unscored | — | — | — | 0.010 | ok |
| table-borderless-aligned | native-header-bullets | False | 0/8 | 0/10 | — | 0.009 | ok |
| rotated-columns | native-header-bullets | True | — | — | — | 0.011 | ok |
| footnotes-and-page-furniture | native-header-bullets | True | — | — | — | 0.009 | ok |
| rtl-visual-glyph-order | native-header-bullets | unscored | — | — | — | 0.010 | ok |
| tagged-reading-order | native-header-bullets | unscored | — | — | — | 0.010 | ok |
| corpus-usrguide | native-header-bullets | unscored | — | — | — | 0.016 | ok |
| corpus-senate-expenditures | native-header-bullets | unscored | — | — | 23/23 | 0.018 | ok |
| corpus-nics-background-checks-2015-11 | native-header-bullets | unscored | — | — | 12/12 | 0.038 | ok |
| corpus-pdfium-type3 | native-header-bullets | unscored | — | — | — | 0.009 | ok |
| corpus-f1040 | native-header-bullets | unscored | — | — | — | 0.023 | ok |
| omml-equations | native-header-bullets | unscored | — | — | — | 0.011 | ok |
| table-borderless-rotate-90 | native-header-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-borderless-rotate-180 | native-header-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-borderless-rotate-270 | native-header-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-borderless-scanned | native-header-bullets | False | 0/9 | 0/12 | — | 0.009 | ok |
| table-wrapped-records | native-header-bullets | False | 0/12 | 0/17 | — | 0.010 | ok |
| text-structure-and-literals | repair-qwen-image | False | — | — | — | 0.010 | ok |
| positioned-math | repair-qwen-image | True | — | — | — | 0.010 | ok |
| math-actualtext | repair-qwen-image | False | — | — | — | 0.010 | ok |
| accessible-actualtext | repair-qwen-image | unscored | — | — | — | 0.009 | ok |
| two-column-order | repair-qwen-image | False | — | — | — | 0.010 | ok |
| unicode-cmap-and-emoji | repair-qwen-image | unscored | — | — | — | 0.010 | ok |
| table-bordered | repair-qwen-image | False | 2/9 | 4/12 | — | 0.011 | ok |
| table-borderless | repair-qwen-image | False | 5/9 | 7/12 | — | 0.010 | ok |
| table-merged | repair-qwen-image | False | 4/9 | 4/12 | — | 0.010 | ok |
| links-and-outline | repair-qwen-image | unscored | — | — | — | 0.011 | ok |
| images-and-vectors | repair-qwen-image | unscored | — | — | — | 0.014 | ok |
| image-only | repair-qwen-image | unscored | — | — | — | 0.010 | ok |
| table-borderless-aligned | repair-qwen-image | False | 0/8 | 10/10 | — | 0.010 | ok |
| rotated-columns | repair-qwen-image | False | — | — | — | 0.010 | ok |
| footnotes-and-page-furniture | repair-qwen-image | False | — | — | — | 0.010 | ok |
| rtl-visual-glyph-order | repair-qwen-image | unscored | — | — | — | 0.011 | ok |
| tagged-reading-order | repair-qwen-image | unscored | — | — | — | 0.011 | ok |
| corpus-usrguide | repair-qwen-image | unscored | — | — | — | 0.010 | ok |
| corpus-senate-expenditures | repair-qwen-image | unscored | — | — | 0/23 | 0.012 | ok |
| corpus-nics-background-checks-2015-11 | repair-qwen-image | unscored | — | — | 0/12 | 0.011 | ok |
| corpus-pdfium-type3 | repair-qwen-image | unscored | — | — | — | 0.010 | ok |
| corpus-f1040 | repair-qwen-image | unscored | — | — | — | 0.013 | ok |
| omml-equations | repair-qwen-image | unscored | — | — | — | 0.010 | ok |
| table-borderless-rotate-90 | repair-qwen-image | False | 0/9 | 4/12 | — | 0.014 | ok |
| table-borderless-rotate-180 | repair-qwen-image | False | 5/9 | 3/12 | — | 0.011 | ok |
| table-borderless-rotate-270 | repair-qwen-image | False | 0/9 | 0/12 | — | 0.011 | ok |
| table-borderless-scanned | repair-qwen-image | False | 5/9 | 7/12 | — | 0.010 | ok |
| table-wrapped-records | repair-qwen-image | False | 0/12 | 10/17 | — | 0.010 | ok |
| text-structure-and-literals | repair-qwen-text | False | — | — | — | 0.010 | ok |
| positioned-math | repair-qwen-text | True | — | — | — | 0.011 | ok |
| math-actualtext | repair-qwen-text | True | — | — | — | 0.010 | ok |
| accessible-actualtext | repair-qwen-text | unscored | — | — | — | 0.010 | ok |
| two-column-order | repair-qwen-text | False | — | — | — | 0.010 | ok |
| unicode-cmap-and-emoji | repair-qwen-text | unscored | — | — | — | 0.010 | ok |
| table-bordered | repair-qwen-text | False | 7/9 | 6/12 | — | 0.010 | ok |
| table-borderless | repair-qwen-text | False | 7/9 | 6/12 | — | 0.010 | ok |
| table-merged | repair-qwen-text | False | 4/9 | 4/12 | — | 0.010 | ok |
| links-and-outline | repair-qwen-text | unscored | — | — | — | 0.010 | ok |
| images-and-vectors | repair-qwen-text | unscored | — | — | — | 0.011 | ok |
| image-only | repair-qwen-text | unscored | — | — | — | 0.010 | ok |
| table-borderless-aligned | repair-qwen-text | True | 8/8 | 10/10 | — | 0.011 | ok |
| rotated-columns | repair-qwen-text | False | — | — | — | 0.011 | ok |
| footnotes-and-page-furniture | repair-qwen-text | True | — | — | — | 0.011 | ok |
| rtl-visual-glyph-order | repair-qwen-text | unscored | — | — | — | 0.011 | ok |
| tagged-reading-order | repair-qwen-text | unscored | — | — | — | 0.011 | ok |
| corpus-usrguide | repair-qwen-text | unscored | — | — | — | 0.013 | ok |
| corpus-senate-expenditures | repair-qwen-text | unscored | — | — | 0/23 | 0.012 | ok |
| corpus-nics-background-checks-2015-11 | repair-qwen-text | unscored | — | — | — | 0.000 | FileNotFoundError: [Errno 2] No such file or directory: '/home/dan/code/oss/pylopdf/bench/results/structure-artifacts/corpus-nics-background |
| corpus-pdfium-type3 | repair-qwen-text | unscored | — | — | — | 0.011 | ok |
| corpus-f1040 | repair-qwen-text | unscored | — | — | — | 0.010 | ok |
| omml-equations | repair-qwen-text | unscored | — | — | — | 0.011 | ok |
| table-borderless-rotate-90 | repair-qwen-text | False | 0/9 | 0/12 | — | 0.013 | ok |
| table-borderless-rotate-180 | repair-qwen-text | False | 6/9 | 4/12 | — | 0.011 | ok |
| table-borderless-rotate-270 | repair-qwen-text | False | 0/9 | 0/12 | — | 0.012 | ok |
| table-borderless-scanned | repair-qwen-text | False | 5/9 | 7/12 | — | 0.011 | ok |
| table-wrapped-records | repair-qwen-text | True | 12/12 | 17/17 | — | 0.011 | ok |
| text-structure-and-literals | retained-docling | True | — | — | — | 0.747 | ok |
| positioned-math | retained-docling | True | — | — | — | 0.814 | ok |
| math-actualtext | retained-docling | True | — | — | — | 0.854 | ok |
| accessible-actualtext | retained-docling | unscored | — | — | — | 0.734 | ok |
| two-column-order | retained-docling | False | — | — | — | 1.512 | ok |
| unicode-cmap-and-emoji | retained-docling | unscored | — | — | — | 0.749 | ok |
| table-bordered | retained-docling | True | 9/9 | 12/12 | — | 1.318 | ok |
| table-borderless | retained-docling | False | 0/9 | 0/12 | — | 0.801 | ok |
| table-merged | retained-docling | False | 1/9 | 3/12 | — | 1.292 | ok |
| links-and-outline | retained-docling | unscored | — | — | — | 0.000 | ValueError: retained model output requires identical single-page input |
| images-and-vectors | retained-docling | unscored | — | — | — | 0.748 | ok |
| image-only | retained-docling | unscored | — | — | — | 1.128 | ok |
| table-borderless-aligned | retained-docling | False | 0/8 | 0/10 | — | 0.809 | ok |
| rotated-columns | retained-docling | True | — | — | — | 0.760 | ok |
| footnotes-and-page-furniture | retained-docling | True | — | — | — | 0.870 | ok |
| rtl-visual-glyph-order | retained-docling | unscored | — | — | — | 0.768 | ok |
| tagged-reading-order | retained-docling | unscored | — | — | — | 0.952 | ok |
| corpus-usrguide | retained-docling | unscored | — | — | — | 0.996 | ok |
| corpus-senate-expenditures | retained-docling | unscored | — | — | 23/23 | 9.920 | ok |
| corpus-nics-background-checks-2015-11 | retained-docling | unscored | — | — | 0/12 | 36.632 | ok |
| corpus-pdfium-type3 | retained-docling | unscored | — | — | — | 0.786 | ok |
| corpus-f1040 | retained-docling | unscored | — | — | — | 1.620 | ok |
| omml-equations | retained-docling | unscored | — | — | — | 0.809 | ok |
| table-borderless-rotate-90 | retained-docling | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-rotate-180 | retained-docling | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-rotate-270 | retained-docling | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-scanned | retained-docling | unscored | — | — | — | 0.000 | StopIteration:  |
| table-wrapped-records | retained-docling | unscored | — | — | — | 0.000 | StopIteration:  |
| text-structure-and-literals | retained-docling-formulas | True | — | — | — | 0.780 | ok |
| positioned-math | retained-docling-formulas | True | — | — | — | 0.781 | ok |
| math-actualtext | retained-docling-formulas | True | — | — | — | 0.798 | ok |
| accessible-actualtext | retained-docling-formulas | unscored | — | — | — | 0.791 | ok |
| two-column-order | retained-docling-formulas | False | — | — | — | 1.462 | ok |
| unicode-cmap-and-emoji | retained-docling-formulas | unscored | — | — | — | 0.769 | ok |
| table-bordered | retained-docling-formulas | True | 9/9 | 12/12 | — | 1.389 | ok |
| table-borderless | retained-docling-formulas | False | 0/9 | 0/12 | — | 0.815 | ok |
| table-merged | retained-docling-formulas | False | 1/9 | 3/12 | — | 1.261 | ok |
| links-and-outline | retained-docling-formulas | unscored | — | — | — | 0.000 | ValueError: retained model output requires identical single-page input |
| images-and-vectors | retained-docling-formulas | unscored | — | — | — | 0.771 | ok |
| image-only | retained-docling-formulas | unscored | — | — | — | 1.171 | ok |
| table-borderless-aligned | retained-docling-formulas | False | 0/8 | 0/10 | — | 0.851 | ok |
| rotated-columns | retained-docling-formulas | True | — | — | — | 0.761 | ok |
| footnotes-and-page-furniture | retained-docling-formulas | True | — | — | — | 0.841 | ok |
| rtl-visual-glyph-order | retained-docling-formulas | unscored | — | — | — | 0.850 | ok |
| tagged-reading-order | retained-docling-formulas | unscored | — | — | — | 0.818 | ok |
| corpus-usrguide | retained-docling-formulas | unscored | — | — | — | 0.825 | ok |
| corpus-senate-expenditures | retained-docling-formulas | unscored | — | — | 23/23 | 9.847 | ok |
| corpus-nics-background-checks-2015-11 | retained-docling-formulas | unscored | — | — | 0/12 | 41.483 | ok |
| corpus-pdfium-type3 | retained-docling-formulas | unscored | — | — | — | 0.772 | ok |
| corpus-f1040 | retained-docling-formulas | unscored | — | — | — | 1.940 | ok |
| omml-equations | retained-docling-formulas | unscored | — | — | — | 0.759 | ok |
| table-borderless-rotate-90 | retained-docling-formulas | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-rotate-180 | retained-docling-formulas | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-rotate-270 | retained-docling-formulas | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-scanned | retained-docling-formulas | unscored | — | — | — | 0.000 | StopIteration:  |
| table-wrapped-records | retained-docling-formulas | unscored | — | — | — | 0.000 | StopIteration:  |
| text-structure-and-literals | retained-marker-fast | True | — | — | — | 0.262 | ok |
| positioned-math | retained-marker-fast | True | — | — | — | 0.241 | ok |
| math-actualtext | retained-marker-fast | True | — | — | — | 0.218 | ok |
| accessible-actualtext | retained-marker-fast | unscored | — | — | — | 0.248 | ok |
| two-column-order | retained-marker-fast | True | — | — | — | 0.223 | ok |
| unicode-cmap-and-emoji | retained-marker-fast | unscored | — | — | — | 1.131 | ok |
| table-bordered | retained-marker-fast | False | 7/9 | 6/12 | — | 1.189 | ok |
| table-borderless | retained-marker-fast | False | 7/9 | 6/12 | — | 0.355 | ok |
| table-merged | retained-marker-fast | False | 7/9 | 6/12 | — | 0.360 | ok |
| links-and-outline | retained-marker-fast | unscored | — | — | — | 0.000 | ValueError: retained model output requires identical single-page input |
| images-and-vectors | retained-marker-fast | unscored | — | — | — | 0.347 | ok |
| image-only | retained-marker-fast | unscored | — | — | — | 0.340 | ok |
| table-borderless-aligned | retained-marker-fast | True | 8/8 | 10/10 | — | 0.343 | ok |
| rotated-columns | retained-marker-fast | True | — | — | — | 0.319 | ok |
| footnotes-and-page-furniture | retained-marker-fast | True | — | — | — | 0.323 | ok |
| rtl-visual-glyph-order | retained-marker-fast | unscored | — | — | — | 0.345 | ok |
| tagged-reading-order | retained-marker-fast | unscored | — | — | — | 0.291 | ok |
| corpus-usrguide | retained-marker-fast | unscored | — | — | — | 0.492 | ok |
| corpus-senate-expenditures | retained-marker-fast | unscored | — | — | 0/23 | 0.868 | ok |
| corpus-nics-background-checks-2015-11 | retained-marker-fast | unscored | — | — | 12/12 | 0.894 | ok |
| corpus-pdfium-type3 | retained-marker-fast | unscored | — | — | — | 0.239 | ok |
| corpus-f1040 | retained-marker-fast | unscored | — | — | — | 0.689 | ok |
| omml-equations | retained-marker-fast | unscored | — | — | — | 0.320 | ok |
| table-borderless-rotate-90 | retained-marker-fast | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-rotate-180 | retained-marker-fast | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-rotate-270 | retained-marker-fast | unscored | — | — | — | 0.000 | StopIteration:  |
| table-borderless-scanned | retained-marker-fast | unscored | — | — | — | 0.000 | StopIteration:  |
| table-wrapped-records | retained-marker-fast | unscored | — | — | — | 0.000 | StopIteration:  |
| text-structure-and-literals | ocr-geometry-wrapped | True | — | — | — | 0.034 | ok |
| positioned-math | ocr-geometry-wrapped | True | — | — | — | 0.025 | ok |
| math-actualtext | ocr-geometry-wrapped | True | — | — | — | 0.027 | ok |
| accessible-actualtext | ocr-geometry-wrapped | unscored | — | — | — | 0.025 | ok |
| two-column-order | ocr-geometry-wrapped | False | — | — | — | 0.029 | ok |
| unicode-cmap-and-emoji | ocr-geometry-wrapped | unscored | — | — | — | 0.011 | ok |
| table-bordered | ocr-geometry-wrapped | True | 9/9 | 12/12 | — | 0.010 | ok |
| table-borderless | ocr-geometry-wrapped | True | 9/9 | 12/12 | — | 0.010 | ok |
| table-merged | ocr-geometry-wrapped | False | 8/9 | 9/12 | — | 0.009 | ok |
| links-and-outline | ocr-geometry-wrapped | unscored | — | — | — | 0.009 | ok |
| images-and-vectors | ocr-geometry-wrapped | unscored | — | — | — | 0.010 | ok |
| image-only | ocr-geometry-wrapped | unscored | — | — | — | 2.254 | ok |
| table-borderless-aligned | ocr-geometry-wrapped | True | 8/8 | 10/10 | — | 0.009 | ok |
| rotated-columns | ocr-geometry-wrapped | True | — | — | — | 0.012 | ok |
| footnotes-and-page-furniture | ocr-geometry-wrapped | True | — | — | — | 0.010 | ok |
| rtl-visual-glyph-order | ocr-geometry-wrapped | unscored | — | — | — | 0.010 | ok |
| tagged-reading-order | ocr-geometry-wrapped | unscored | — | — | — | 0.009 | ok |
| corpus-usrguide | ocr-geometry-wrapped | unscored | — | — | — | 0.017 | ok |
| corpus-senate-expenditures | ocr-geometry-wrapped | unscored | — | — | 23/23 | 0.018 | ok |
| corpus-nics-background-checks-2015-11 | ocr-geometry-wrapped | unscored | — | — | 6/12 | 0.028 | ok |
| corpus-pdfium-type3 | ocr-geometry-wrapped | unscored | — | — | — | 0.111 | ok |
| corpus-f1040 | ocr-geometry-wrapped | unscored | — | — | — | 0.026 | ok |
| omml-equations | ocr-geometry-wrapped | unscored | — | — | — | 0.010 | ok |
| table-borderless-scanned | ocr-geometry-wrapped | True | 9/9 | 12/12 | — | 2.200 | ok |
| table-wrapped-records | ocr-geometry-wrapped | True | 12/12 | 17/17 | — | 0.011 | ok |
| table-borderless-rotate-90 | ocr-geometry-wrapped | True | 9/9 | 12/12 | — | 0.034 | ok |
| table-borderless-rotate-180 | ocr-geometry-wrapped | True | 9/9 | 12/12 | — | 0.028 | ok |
| table-borderless-rotate-270 | ocr-geometry-wrapped | True | 9/9 | 12/12 | — | 0.026 | ok |
| text-structure-and-literals | hybrid-html | True | — | — | — | 0.043 | ok |
| positioned-math | hybrid-html | True | — | — | — | 0.045 | ok |
| math-actualtext | hybrid-html | True | — | — | — | 0.042 | ok |
| accessible-actualtext | hybrid-html | unscored | — | — | — | 0.043 | ok |
| two-column-order | hybrid-html | True | — | — | — | 0.031 | ok |
| unicode-cmap-and-emoji | hybrid-html | unscored | — | — | — | 0.030 | ok |
| table-bordered | hybrid-html | True | 9/9 | 12/12 | — | 0.029 | ok |
| table-borderless | hybrid-html | True | 9/9 | 12/12 | — | 0.028 | ok |
| table-merged | hybrid-html | True | 9/9 | 12/12 | — | 0.029 | ok |
| links-and-outline | hybrid-html | unscored | — | — | — | 0.033 | ok |
| images-and-vectors | hybrid-html | unscored | — | — | — | 0.029 | ok |
| image-only | hybrid-html | unscored | — | — | — | 2.406 | ok |
| table-borderless-aligned | hybrid-html | True | 8/8 | 10/10 | — | 0.031 | ok |
| rotated-columns | hybrid-html | True | — | — | — | 0.033 | ok |
| footnotes-and-page-furniture | hybrid-html | True | — | — | — | 0.031 | ok |
| rtl-visual-glyph-order | hybrid-html | unscored | — | — | — | 0.041 | ok |
| tagged-reading-order | hybrid-html | unscored | — | — | — | 0.043 | ok |
| corpus-usrguide | hybrid-html | unscored | — | — | — | 0.046 | ok |
| corpus-senate-expenditures | hybrid-html | unscored | — | — | 23/23 | 0.053 | ok |
| corpus-nics-background-checks-2015-11 | hybrid-html | unscored | — | — | 12/12 | 0.115 | ok |
| corpus-pdfium-type3 | hybrid-html | unscored | — | — | — | 0.146 | ok |
| corpus-f1040 | hybrid-html | unscored | — | — | — | 0.072 | ok |
| omml-equations | hybrid-html | unscored | — | — | — | 0.032 | ok |
| table-borderless-rotate-90 | hybrid-html | True | 9/9 | 12/12 | — | 0.031 | ok |
| table-borderless-rotate-180 | hybrid-html | True | 9/9 | 12/12 | — | 0.044 | ok |
| table-borderless-rotate-270 | hybrid-html | True | 9/9 | 12/12 | — | 0.052 | ok |
| table-borderless-scanned | hybrid-html | True | 9/9 | 12/12 | — | 2.560 | ok |
| table-wrapped-records | hybrid-html | True | 12/12 | 17/17 | — | 0.029 | ok |
| text-structure-and-literals | hybrid-bullets | True | — | — | — | 0.030 | ok |
| positioned-math | hybrid-bullets | True | — | — | — | 0.030 | ok |
| math-actualtext | hybrid-bullets | True | — | — | — | 0.029 | ok |
| accessible-actualtext | hybrid-bullets | unscored | — | — | — | 0.031 | ok |
| two-column-order | hybrid-bullets | True | — | — | — | 0.031 | ok |
| unicode-cmap-and-emoji | hybrid-bullets | unscored | — | — | — | 0.030 | ok |
| table-bordered | hybrid-bullets | True | 9/9 | 12/12 | — | 0.030 | ok |
| table-borderless | hybrid-bullets | True | 9/9 | 12/12 | — | 0.029 | ok |
| table-merged | hybrid-bullets | True | 9/9 | 12/12 | — | 0.030 | ok |
| links-and-outline | hybrid-bullets | unscored | — | — | — | 0.030 | ok |
| images-and-vectors | hybrid-bullets | unscored | — | — | — | 0.029 | ok |
| image-only | hybrid-bullets | unscored | — | — | — | 2.465 | ok |
| table-borderless-aligned | hybrid-bullets | True | 8/8 | 10/10 | — | 0.036 | ok |
| rotated-columns | hybrid-bullets | True | — | — | — | 0.032 | ok |
| footnotes-and-page-furniture | hybrid-bullets | True | — | — | — | 0.031 | ok |
| rtl-visual-glyph-order | hybrid-bullets | unscored | — | — | — | 0.031 | ok |
| tagged-reading-order | hybrid-bullets | unscored | — | — | — | 0.029 | ok |
| corpus-usrguide | hybrid-bullets | unscored | — | — | — | 0.035 | ok |
| corpus-senate-expenditures | hybrid-bullets | unscored | — | — | 23/23 | 0.038 | ok |
| corpus-nics-background-checks-2015-11 | hybrid-bullets | unscored | — | — | 12/12 | 0.090 | ok |
| corpus-pdfium-type3 | hybrid-bullets | unscored | — | — | — | 0.138 | ok |
| corpus-f1040 | hybrid-bullets | unscored | — | — | — | 0.043 | ok |
| omml-equations | hybrid-bullets | unscored | — | — | — | 0.034 | ok |
| table-borderless-rotate-90 | hybrid-bullets | True | 9/9 | 12/12 | — | 0.029 | ok |
| table-borderless-rotate-180 | hybrid-bullets | True | 9/9 | 12/12 | — | 0.029 | ok |
| table-borderless-rotate-270 | hybrid-bullets | True | 9/9 | 12/12 | — | 0.030 | ok |
| table-borderless-scanned | hybrid-bullets | True | 9/9 | 12/12 | — | 2.504 | ok |
| table-wrapped-records | hybrid-bullets | True | 12/12 | 17/17 | — | 0.034 | ok |
| table-borderless-rotate-90 | olmocr-normalized | True | 9/9 | 12/12 | — | 4.462 | ok |
| table-borderless-rotate-180 | olmocr-normalized | True | 9/9 | 12/12 | — | 4.221 | ok |
| table-borderless-rotate-270 | olmocr-normalized | True | 9/9 | 12/12 | — | 4.435 | ok |
| two-column-order | olmocr-compact-text | True | — | — | — | 6.605 | ok |
| table-bordered | olmocr-compact-text | False | 8/9 | 9/12 | — | 4.595 | ok |
| table-borderless | olmocr-compact-text | False | 8/9 | 9/12 | — | 4.660 | ok |
| table-merged | olmocr-compact-text | False | 8/9 | 9/12 | — | 4.688 | ok |
| corpus-senate-expenditures | olmocr-compact-text | unscored | — | — | 0/23 | 31.060 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-compact-text | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 1.86 GiB. GPU 0 has a total capacity of 23.56 GiB of which 500.06 MiB is free. Proce |
| table-wrapped-records | olmocr-compact-text | True | 12/12 | 17/17 | — | 7.304 | ok |
| corpus-senate-expenditures | olmocr-4bit-text | unscored | — | — | 0/23 | 44.975 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-4bit-text | unscored | — | — | — | 0.000 | OutOfMemoryError: CUDA out of memory. Tried to allocate 4.09 GiB. GPU 0 has a total capacity of 23.56 GiB of which 2.34 GiB is free. Process |
| two-column-order | olmocr-yolo-crop | True | — | — | — | 5.706 | ok |
| table-bordered | olmocr-yolo-crop | True | 9/9 | 12/12 | — | 3.898 | ok |
| table-borderless | olmocr-yolo-crop | True | 9/9 | 12/12 | — | 3.942 | ok |
| table-merged | olmocr-yolo-crop | True | 9/9 | 12/12 | — | 3.965 | ok |
| corpus-senate-expenditures | olmocr-yolo-crop | unscored | — | — | 11/23 | 106.405 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-yolo-crop | unscored | — | — | 0/12 | 128.006 | truncated |
| table-wrapped-records | olmocr-yolo-crop | True | 12/12 | 17/17 | — | 6.113 | ok |
| two-column-order | olmocr-geometry-crop | True | — | — | — | 5.122 | ok |
| table-bordered | olmocr-geometry-crop | True | 9/9 | 12/12 | — | 4.292 | ok |
| table-borderless | olmocr-geometry-crop | True | 9/9 | 12/12 | — | 4.103 | ok |
| table-merged | olmocr-geometry-crop | False | 8/9 | 9/12 | — | 4.074 | ok |
| table-wrapped-records | olmocr-geometry-crop | True | 12/12 | 17/17 | — | 9.012 | ok |
| corpus-senate-expenditures | olmocr-row-crop | unscored | — | — | 0/23 | 122.965 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-row-crop | unscored | — | — | 7/12 | 1046.099 | truncated |
| two-column-order | qwen-compact-text | True | — | — | — | 6.219 | ok |
| table-bordered | qwen-compact-text | False | 0/9 | 0/12 | — | 1.888 | ok |
| table-borderless | qwen-compact-text | False | 0/9 | 0/12 | — | 1.885 | ok |
| table-merged | qwen-compact-text | False | 0/9 | 0/12 | — | 1.910 | ok |
| corpus-senate-expenditures | qwen-compact-text | unscored | — | — | 0/23 | 94.421 | ok |
| corpus-nics-background-checks-2015-11 | qwen-compact-text | unscored | — | — | 0/12 | 21.152 | ok |
| table-wrapped-records | qwen-compact-text | False | 0/12 | 0/17 | — | 2.382 | ok |
| two-column-order | qwen-compact-patch | unscored | — | — | — | 0.000 | TypeError: each cell must contain a list of source word IDs |
| table-bordered | qwen-compact-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-borderless | qwen-compact-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| table-merged | qwen-compact-patch | unscored | — | — | — | 0.000 | TypeError: patch root must be a JSON object with a tables list |
| corpus-senate-expenditures | qwen-compact-patch | unscored | — | — | — | 0.000 | JSONDecodeError: Expecting property name enclosed in double quotes: line 165 column 17 (char 4684) |

## Run provenance

```json
{
  "started_at": "2026-10-08T03:18:26.318705+00:00",
  "environment": "Linux-7.2.5-3-omarchy-x86_64-with-glibc2.44",
  "python": "3.14.7",
  "source_commit": "fa21fb462d9b10431e705fc2dc727f733b15e48e",
  "remote_spend_authorized_usd": 15,
  "remote_spend_usd": 0,
  "observation_code_sha256": "5a1f588ac88fc76515aaa9253d93e1b6a249a4311eedfcd4ffc2979b30d665e3"
}
```

| Run | Adapter | Initialization seconds | Repetitions | Device | Model |
| --- | --- | ---: | ---: | --- | --- |
| 0 | pylopdf | 0.000 | 3 | cuda:0 | none |
| 1 | pylopdf-text | 0.000 | 3 | cuda:0 | none |
| 2 | geometry | 0.000 | 3 | cuda:0 | none |
| 3 | geometry-bullets | 0.000 | 3 | cuda:0 | none |
| 4 | geometry-wrapped | 0.000 | 3 | cuda:0 | none |
| 5 | geometry-wrapped-bullets | 0.000 | 3 | cuda:0 | none |
| 6 | yolo-geometry | 4.195 | 1 | cuda:0 | /home/dan/.cache/huggingface/hub/models--hantian--yolo-doclaynet/snapshots/49b97586dbd3bdae169e8f5e165710d0facf5f1e/yolo26m-doclaynet.pt |
| 7 | yolo-geometry-wrapped | 0.209 | 1 | cuda:0 | /home/dan/.cache/huggingface/hub/models--hantian--yolo-doclaynet/snapshots/49b97586dbd3bdae169e8f5e165710d0facf5f1e/yolo26m-doclaynet.pt |
| 8 | yolo-geometry | 2.014 | 1 | cuda:0 | /home/dan/.cache/huggingface/hub/models--hantian--yolo-doclaynet/snapshots/49b97586dbd3bdae169e8f5e165710d0facf5f1e/yolo26m-doclaynet.pt |
| 9 | yolo-geometry-wrapped | 0.128 | 1 | cuda:0 | /home/dan/.cache/huggingface/hub/models--hantian--yolo-doclaynet/snapshots/49b97586dbd3bdae169e8f5e165710d0facf5f1e/yolo26m-doclaynet.pt |
| 10 | olmocr-image | 11.510 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 11 | olmocr-text | 12.841 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 12 | olmocr-patch | 8.354 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 13 | geometry | 0.000 | 3 | cuda:0 | none |
| 14 | geometry-bullets | 0.000 | 3 | cuda:0 | none |
| 15 | geometry-wrapped | 0.000 | 3 | cuda:0 | none |
| 16 | geometry-wrapped-bullets | 0.000 | 3 | cuda:0 | none |
| 17 | native-bullets | 0.000 | 3 | cuda:0 | none |
| 18 | native-header-bullets | 0.000 | 3 | cuda:0 | none |
| 19 | yolo-normalized-geometry-wrapped | 2.058 | 1 | cuda:0 | /home/dan/.cache/huggingface/hub/models--hantian--yolo-doclaynet/snapshots/49b97586dbd3bdae169e8f5e165710d0facf5f1e/yolo26m-doclaynet.pt |
| 20 | qwen-image | 12.194 | 1 | cuda:0 | Qwen/Qwen2.5-VL-3B-Instruct |
| 21 | qwen-text | 3.484 | 1 | cuda:0 | Qwen/Qwen2.5-VL-3B-Instruct |
| 22 | qwen-patch | 3.370 | 1 | cuda:0 | Qwen/Qwen2.5-VL-3B-Instruct |
| 23 | native-header-bullets | 0.000 | 3 | cuda:0 | none |
| 24 | repair-qwen-image | 0.000 | 3 | cuda:0 | none |
| 25 | repair-qwen-text | 0.000 | 3 | cuda:0 | none |
| 26 | retained-docling | 0.000 | 1 | cuda:0 | none |
| 27 | retained-docling-formulas | 0.000 | 1 | cuda:0 | none |
| 28 | retained-marker-fast | 0.000 | 1 | cuda:0 | none |
| 29 | ocr-geometry-wrapped | 0.033 | 1 | cuda:0 | none |
| 30 | ocr-geometry-wrapped | 0.017 | 1 | cuda:0 | none |
| 31 | hybrid-html | 0.031 | 3 | cuda:0 | none |
| 32 | hybrid-bullets | 0.009 | 3 | cuda:0 | none |
| 33 | olmocr-normalized | 15.382 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 34 | olmocr-compact-text | 7.341 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 35 | olmocr-4bit-text | 12.052 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 36 | olmocr-yolo-crop | 6.810 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 37 | olmocr-geometry-crop | 8.888 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 38 | olmocr-row-crop | 7.557 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 39 | qwen-compact-text | 5.579 | 1 | cuda:0 | Qwen/Qwen2.5-VL-3B-Instruct |
| 40 | qwen-compact-patch | 5.573 | 1 | cuda:0 | Qwen/Qwen2.5-VL-3B-Instruct |

Full dependency versions, per-result run indexes, code hashes, and retained-run provenance are in JSON.

# Structured PDF recovery experiments

Run: 2026-10-08T04:51:00.292628+00:00

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
| corpus-senate-expenditures | olmocr-text | unscored | — | — | 0/23 | 83.105 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-text | unscored | — | — | 0/12 | 264.915 | truncated |
| corpus-f1040 | olmocr-text | unscored | — | — | — | 32.111 | ok |
| corpus-senate-expenditures | olmocr-compact-text | unscored | — | — | 0/23 | 32.784 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-compact-text | unscored | — | — | 0/12 | 17.271 | ok |
| corpus-f1040 | olmocr-compact-text | unscored | — | — | — | 15.851 | ok |
| corpus-senate-expenditures | qwen-text | unscored | — | — | 0/23 | 244.615 | truncated |
| corpus-nics-background-checks-2015-11 | qwen-text | unscored | — | — | 0/12 | 29.381 | ok |
| corpus-f1040 | qwen-text | unscored | — | — | — | 19.673 | ok |
| corpus-senate-expenditures | repair-qwen-text | unscored | — | — | 0/23 | 0.033 | ok |
| corpus-nics-background-checks-2015-11 | repair-qwen-text | unscored | — | — | 0/12 | 0.001 | ok |
| corpus-f1040 | repair-qwen-text | unscored | — | — | — | 0.001 | ok |

## Run provenance

```json
{
  "started_at": "2026-10-08T04:51:00.292628+00:00",
  "environment": "Linux-5.15.0-141-generic-x86_64-with-glibc2.39",
  "python": "3.12.3",
  "source_commit": "75ea032",
  "remote_spend_authorized_usd": 15,
  "remote_spend_usd": null,
  "remote_instance_id": 54777034,
  "remote_hourly_usd": 0.4333333333333333,
  "native_runtime": "published pylopdf 0.13.0 wheel used only to import runner; all model inputs frozen locally",
  "host_scope": "48 GiB A6000 memory/output-budget controls; separate from 24 GiB baseline"
}
```

| Run | Adapter | Initialization seconds | Repetitions | Device | Model |
| --- | --- | ---: | ---: | --- | --- |
| 0 | olmocr-text | 366.254 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 1 | olmocr-compact-text | 9.448 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |
| 2 | qwen-text | 64.163 | 1 | cuda:0 | Qwen/Qwen2.5-VL-3B-Instruct |
| 3 | repair-qwen-text | 0.000 | 1 | cpu | none |

Full dependency versions, per-result run indexes, code hashes, and retained-run provenance are in JSON.

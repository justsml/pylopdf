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
CUDA figures are observed peak allocated bytes for retained generation calls, not reserved VRAM.
The provenance device is the requested backend; native geometry/OCR and replay/repair adapters use CPU.

| Case | Adapter | Exact grid | Cells | Relations recalled | Record cells | Seconds | CUDA GiB | Result |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- |
| corpus-senate-expenditures | olmocr-image | unscored | — | — | 0/23 | 144.662 | 15.84 | ok |
| corpus-nics-background-checks-2015-11 | olmocr-image | unscored | — | — | 0/12 | 745.276 | 16.47 | truncated |

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
| 0 | olmocr-image | 12.775 | 1 | cuda:0 | allenai/olmOCR-2-7B-1025 |

Full dependency versions, per-result run indexes, code hashes, and retained-run provenance are in JSON.

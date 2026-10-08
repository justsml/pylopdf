# Structured PDF recovery study

This optional study tests table and record relationships, rather than treating
the presence of Markdown table syntax as success. It is separate from the
lightweight timings and CPU model study. It does not change pylopdf's public API
or install models into the library's regular environment.

The preserved inputs include all rich-feature cases plus independent derivatives:
the ragged borderless table at 90/180/270 degrees, a raster-only copy, and wrapped
records. Nine synthetic pages have explicit logical cell grids; six prose/math
pages are negative table controls. Other pages remain unscored for complete grid
accuracy. The Senate and NICS pages have independently visually checked record
cells in `structure_cases.py`: these are spot checks, not complete corpus gold.
Sources and redistribution terms remain in the existing corpus README.

Every adapter receives the same original bytes. Only page 0 is evaluated.
Preparation retains a white-background PNG with longest side 1,288 pixels,
positioned word IDs, source text, page rotation, and dominant display baseline
orientation. Page rotation alone is insufficient for orientation normalization:
the Senate's content is already upright after rendering. Extraction is an input
to the experiment and may itself miss Unicode or accessible text.

## Reproduction

The measured GPU environment uses Python 3.12, PyTorch CUDA 12.8, and a local
RTX 3090 with 24 GiB VRAM. Keep it isolated from the CPU Docling/Marker environment.
Choose a disk-backed path with room for model weights; `/tmp` may be a RAM disk.

```bash
uv venv --python 3.12 ~/.cache/pylopdf-structure-bench
uv pip install --python ~/.cache/pylopdf-structure-bench/bin/python \
  torch==2.11.0 torchvision==0.26.0 \
  --index-url https://download.pytorch.org/whl/cu128
uv pip install --python ~/.cache/pylopdf-structure-bench/bin/python \
  -r bench/structure-requirements.txt
uv pip install --python ~/.cache/pylopdf-structure-bench/bin/python \
  olmocr==0.4.27 --no-deps
uv run python -m bench.structure --prepare \
  --adapter pylopdf --adapter pylopdf-text \
  --adapter geometry --adapter geometry-wrapped \
  --adapter geometry-bullets --adapter geometry-wrapped-bullets \
  --adapter native-bullets --adapter native-header-bullets --repetitions 3
PYTHONPATH=src:. ~/.cache/pylopdf-structure-bench/bin/python -m bench.structure \
  --adapter yolo-geometry --adapter yolo-geometry-wrapped \
  --adapter yolo-normalized-geometry-wrapped
PYTHONPATH=src:. ~/.cache/pylopdf-structure-bench/bin/python -m bench.structure \
  --adapter olmocr-image --adapter olmocr-text --adapter olmocr-patch
PYTHONPATH=src:. ~/.cache/pylopdf-structure-bench/bin/python -m bench.structure \
  --adapter qwen-image --adapter qwen-text --adapter qwen-patch
```

Additional switches expose compact coordinate dumps, NF4 loading, normalized
orientation, and YOLO/geometry crops. Use `--help` for the complete adapter list.
Crop adapters reuse saved YOLO predictions or geometry and report that separately
from inference cost. They preserve extracted text outside the replaced regions;
this is an experimental block replacement, not a complete reading-order policy.
`--case` selects a subset, `--repetitions` repeats complete adapter calls, and
`--force` reruns a result. Completed rows are otherwise resumed by input hash.
Run one writer at a time. `--rescore` checks input/output hashes and updates
observations without regenerating or retiming outputs.

The retained Docling/Marker adapters verify input and output hashes from the
earlier CPU study, require single-page inputs, and carry original timing and
provenance. Replaying their artifacts is not a new performance measurement.
Generate those artifacts using `MODEL_BENCHMARKS.md` before selecting the retained
adapters. They do not support the new derivatives without a new CPU conversion.

## Interventions and evaluation limits

- Geometry regroups physical rows before column assignment and permits trailing
  empty cells. The wrapped variant attaches short continuation lines to a prior
  record. This can incorrectly classify multicolumn prose as a table.
- YOLO26m-DocLayNet gates candidate regions; it does not predict cell structure.
  Detection uses image size 1,024 and confidence cutoff 0.2. Normalization follows
  dominant display text, and candidate coordinates are mapped back to source words.
- Native records preserve vector-grid data and use neutral column labels when
  a very large merged header is unresolved. Header-guided records extend a short
  vector header into the page body and attach description continuations. These
  are experimental heuristics; unrelated prose below a header can be absorbed.
- olmOCR uses its public no-anchoring v4 YAML prompt, BF16, SDPA, greedy decoding,
  and a default 4,096-token output boundary. The text and patch variants are
  experimental prompts, not the recommended upstream conversion pipeline.
  Automatic retries and orientation correction from the upstream toolkit are
  not claimed. NF4 variants are explicitly separate from BF16 results.
- General Qwen2.5-VL-3B variants test image/text and source-ID patch responses.
  Patches reject invented or duplicated IDs, ragged matrices, and invalid spans.
  Source ID validity cannot prove correct semantic cell/header relationships.
- Native OCR runs on white at 150 dpi, uses four threads, and skips existing text.
  Its geometry fallback retains recognition errors rather than silently replacing
  them with the synthetic reference.

Exact grid checks include table count, cell position, punctuation, and empty cells.
Relationship checks compare horizontal/vertical neighbors, with both reference
and observed totals retained. Merged slots expand from explicit spans for cell
checks; HTML span metadata is observed separately. HTML inside a Markdown code
fence is code, not a rendered table. Bullet variants are scored on their recovered
cell matrices; the experiment does not claim that repeated labels are a semantically
verified header hierarchy. Source token agreement is not OCR ground truth.

Preparation/render/extraction costs are outside adapter timings. Prepared pylopdf
baselines are replays and do not provide new conversion timings. GPU initialization
is separate; first inference is included in measured repetitions. Process RSS is
a cumulative high-water value, not a per-case peak. Generation truncation and
allocation failures remain visible. No cross-tool throughput ranking is implied.

## Training pilot

```bash
PYTHONPATH=src:. ~/.cache/pylopdf-structure-bench/bin/python \
  -m bench.structure_train --steps 64
PYTHONPATH=src:. ~/.cache/pylopdf-structure-bench/bin/python -m bench.structure \
  --adapter qwen-4bit-compact-patch --adapter qwen-lora-4bit-compact-patch
```

The fixed pilot uses 36 generated training pages and 12 generated validation
pages, seed 7,100, LoRA rank 8, learning rate 0.0001, and NF4 base weights with BF16
compute. It trains only attention projections and masks image/user tokens from
the loss. The raster's longest side is 640 pixels for this pilot. Validation pages
have separate generated values and layouts, but share template families: this is
a feasibility check, not a template-family holdout or generalization claim.
The original 28 study inputs never enter training. Compare quantized base and
adapted models under the same prompt/quantization before attributing a gain to training.

All PDFs, PNGs, prompts, full responses, traces, model weights, and JSON details
stay outside Git. Commit the protocol, code, tests, and Markdown findings only.
Model licenses remain independent of pylopdf: [YOLO checkpoint](https://huggingface.co/hantian/yolo-doclaynet),
[olmOCR checkpoint](https://huggingface.co/allenai/olmOCR-2-7B-1025), and
[Qwen checkpoint](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct).
The local study does not redistribute any model or trained adapter.
Remote hosting is authorized up to $15 total; local inference consumes no remote
hosting budget. Record every remote charge before enabling a hosted adapter.

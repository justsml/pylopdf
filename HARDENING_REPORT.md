# Pylo PDF hardening review and implementation report

Review baseline: `4b16cddda88b70df2d363a56589a84870f6fc84a` (v0.13.0).
Work branch: `fix/resource-and-validation-hardening`.

## Assessment

The project has substantial functional coverage and unusually detailed resource
admission rules. Its Rust/Python boundary, page-generation contract, immutable
render snapshots, independent-document concurrency, and licensed regression corpus
are useful foundations. The work below addresses confirmed defects and removes
avoidable memory costs without redesigning the public API.

The remaining security boundary matters: parsing and interpretation use complex
native dependencies; per-operation limits do not constitute a process-wide memory
or CPU guarantee. A hostile-PDF service still needs isolated workers with host
memory limits and an external deadline. Successful parsing, rewriting, or raster
rendering does not establish that an output PDF is sanitized or redacted.

## Completed changes

| Priority | Finding | Result and evidence |
| --- | --- | --- |
| High | One-minute CI budgets could terminate native builds and the intended ten-minute fuzz run. | Workload-specific 5–60 minute budgets; fuzz receives 30 minutes. Workflow regressions validate these budgets. |
| High | Temporary PDF/PNG outputs could inherit permissive modes. | Exclusive temporary creation uses `0600`; newly created final files stay private, while existing regular-file permissions are preserved. Tests exercise a permissive umask and permissions during writing. |
| High | PDF saving closed the exclusive descriptor and reopened its pathname. | The public save path streams all normal, object-stream, and encrypted modes through the original open file. Python verifies named-file identity before replacement. Regression tests cover pathname substitution, descriptor wrapping failure, writer failure, and requested-path diagnostics. |
| High | A closed Document could retain its native graph, source bytes, snapshots, and font backing. | `close()` drops its native core and encrypted source bytes. Retained Page views continue to raise `DocumentClosedError`. |
| High | A failed structural edit could add orphan objects and stale an existing Page despite rejecting the operation. | New/copy/import prepare inherited dictionaries, root IDs, and final Kids before commit. Python advances generation only after success. Repeated rejection tests compare serialized bytes and retained page views; malformed source and target imports are covered. |
| Medium | Page count and lookup repeatedly walked the page tree. | One lazily validated ordered page-ID index survives content/metadata changes and invalidates on structural edits or document replacement. Batch validation captures page count once. Mutation and malformed-tree tests cover invalidation. |
| Medium | Structured extraction produced both spans and words for every requested format. | Native layout accepts internal materialization flags; public words/blocks/dict requests build only their required representation. Public signatures remain unchanged. |
| Medium | Extraction-first operations could miss installed locale fallback fonts. | Text, search, and tables initialize the same locale fallback policy as rendering. Tests cover those entry points before a render. |
| Medium | Every Document loaded separate copies of the same bundled CJK font files. | Automatic locale loading shares immutable backing through at most eight weak registry entries. File identity and each caller's size policy are checked. Explicit custom setters remain independent. Budget/freshness tests cover changed size, replacement with preserved timestamps, and immutable existing snapshots. |
| Medium | OCR layer maps and formatted content grew through infallible intermediate collections and strings. | CID maps, sorted CMap entries, and output formatting now grow fallibly before mutation. Unicode tests cross 100-entry CMap blocks and preserve non-BMP surrogate mappings. Dependency allocations remain outside this guarantee. |
| Medium | Iteration could silently observe a structurally changed document. | Iteration captures page count/generation and rejects closure or a generation change before yielding another page. |
| Medium | Fuzz coverage omitted several expensive public read paths, and cancelled runs could be overlooked. | Bounded drawing/image/tree/table/link/Markdown calls broaden the harness. A permission-free observer with no checkout records unsuccessful fuzz completion. Native coverage instrumentation remains outstanding. |
| Medium | CI commands could re-resolve dependencies after installing an environment. | uv sync uses the lock; subsequent uv runs use `--no-sync`; native Cargo/maturin builds use `--locked`. Python font/model package build backends still require separate pinning. |
| Medium | Security and import claims obscured enforcement phases and preservation limits. | English, Japanese, Chinese, and Korean API/security documentation distinguish pre-read, parse, and post-parse policies; explain RSS/deadline responsibilities, signatures, import limitations, and safe output permissions. |

Duplicate low-level imports retain independent page dictionaries and shared
resources. Short Python file writes are handled; temporary Python byte copies are
bounded to 64 KiB. Stable PDF writer bookkeeping is restored after write failure.
Current stable Rust lint compatibility was also repaired without suppressing lints.

## Memory measurement

In separate Linux/CPython 3.14.7 processes retaining 16 empty Documents with one
Japanese sans/serif pair, peak RSS was 189.06 MiB through the explicit uncached
setter and 35.42 MiB through the shared automatic locale setter. Configuration
took 0.0964 s and 0.00554 s respectively in that focused run.

[Reproduction script](bench/font_sharing.py) and
[measurement limitations](bench/results/font-sharing-latest.md) accompany the
change. These compare two paths in the same build, not historical wheels or
rendering throughput. The registry introduces filesystem metadata checks and a
serial first-load lock. Weak sharing helps when documents overlap in lifetime;
different font files or short-lived documents can give different results.

## Remaining work and architectural limitations

| Priority | Remaining issue | Next coherent unit of work |
| --- | --- | --- |
| High for hostile-PDF deployments | Object counts, nesting, and some interpretation policies validate completed dependency work; they cannot bound every allocator or parser instruction before execution. | Deploy process isolation, host RSS limits, and killable deadlines. Parser-integrated limits require upstream cooperation or a separately validated loader. |
| High for fuzz assurance | The Atheris harness exercises workflows, but the current release extension lacks Rust coverage/sanitizer instrumentation. | Build a reproducible native Rust/LLVM/libFuzzer lane, demonstrate coverage reaches parser/interpreter branches, and add crash triage and regression promotion. A smoke run is not evidence of security. |
| Medium | Page import still clones and renumbers the entire source document before pruning. Atomic target commit is fixed; transient source-copy memory remains. | Replace full-source cloning with a reachable-object import planner; separately test cycles, shared resources, duplicate pages, and destinations to excluded pages. |
| Medium | Import does not merge/remap source Catalog features such as the AcroForm registry, outlines/named destinations, page labels, optional-content configuration, or tagged structure. | Define preservation policies and implement one feature at a time with real-world roundtrip fixtures. Current documentation explicitly states the boundary. |
| Medium | Structural edits do not provide comprehensive remapping of existing document-level page labels/destinations/tagged references. | Add a source-to-result page mapping and feature-specific rewrites; decide duplicate-page destination semantics before changing behavior. |
| Medium | Text/table caches are bounded by page count, while compatible defaults permit variable-size interpretations. Font sharing does not make total Document memory bounded. | Introduce an aggregate retained-byte cache budget with explicit eviction accounting; benchmark large text-heavy and table-heavy pages. |
| Medium | hayro-svg returns a complete String before the configured output boundary is checked. | Obtain a bounded streaming converter upstream or use process limits for SVG work. The boundary currently prevents a second oversized Python copy. |
| Medium | Font/model release build backends remain unpinned despite runtime lock enforcement. | Pin backend/tool versions in a reviewed release constraints policy and verify emitted artifacts from an isolated environment. |
| Medium | Much domain logic remains in the large Rust document binding and Python module. | Extract page-tree/import planning, writer policy, and cache policy behind narrow internal interfaces after preserving behavior with the existing Python suite. Avoid a simultaneous broad module rewrite and API expansion. |

Save replacement guarantees atomic visibility, not crash durability: it does not
fsync the file and directory. Destination-directory permissions remain part of
the trust boundary; descriptor retention and identity checks do not promise safe
operation inside a directory controlled by an adversarial account. Private modes
are a POSIX guarantee; Windows access control remains governed by its ACLs.

Extraction also retains documented upstream and geometric limitations, including
Type 3 glyphs with no Unicode mapping, general mixed-direction layout, ruby,
warichu, and ambiguous borderless tables. These require capability-specific
fixtures and upstream work; passing this branch does not remove those limitations.
Same-Document concurrent edits remain outside the supported concurrency contract.

## Validation

- Linux CPython 3.14.7 native suite: **1,129 passed, 11 skipped, 2 expected failures**.
  The known Type 3 warning remains visible; optional capability skips remain.
- Native Cargo check, Rust formatting, and strict Clippy passed, including
  current-stable lint compatibility checks.
- Ruff lint/format, mypy, repository-language checks, and whitespace checks passed.
- All four strict documentation builds passed in EN → JA → zh-CN → KO order.
- Workflow YAML parsing, release-workflow tests, shell syntax, and observer outcome
  checks passed. The observer executes no code from the observed workflow run.
- Expanded Atheris smoke: 40 runs from 23 seeds, with no finding and approximately
  107 MiB reported RSS. This is harness validation, not an exhaustive fuzz campaign.

Windows, macOS, Python 3.10, free-threaded Python, Pyodide, release attestation,
and hosted CI remain review gates rather than locally verified results. No release,
upstream merge, or deployment is included in this work.

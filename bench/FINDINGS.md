# Initial rich-content observations

These findings describe the versions and options in
[the feature report](results/features-latest.md). They are examples from the
bundled inputs, not universal library rankings. The study completed 207
case/configuration measurements; all outputs repeated
exactly over the three measured runs plus warmup.

| Feature | What the retained outputs show | Evidence |
|---|---|---|
| External and internal links | pylopdf's Markdown omits both kinds, although its source inventory resolves all three links. PyMuPDF4LLM legacy preserves the external URI; its layout mode omits it. None of the measured Markdown modes emits the internal destinations. | [Link case](results/features-latest.md#links-and-outline) |
| Images and vector graphics | pylopdf keeps captions and emits no image references. PyMuPDF4LLM emits embedded images; its layout mode also emits the simple vector rectangle as an image. A reference does not prove original-image passthrough or caption association. | [Image case](results/features-latest.md#images-and-vectors) |
| Font styling and literal punctuation | pylopdf retains embedded-font body bold/italic in the Office export, but lacks styling from the unembedded Standard 14 variants. Literal stars and angle brackets become Markdown emphasis/HTML in the punctuation case, so syntax counts can overstate preserved formatting. | [Office output](results/feature-outputs/omml-equations--pylopdf.out), [literal output](results/feature-outputs/text-structure-and-literals--pylopdf.out) |
| Table escaping and spans | pylopdf escapes literal pipes/backslashes and repeats the merged anchor in its pipe table. PyMuPDF4LLM's pipe-table modes lose the strict literal pipe/backslash probes; its HTML mode retains all five text probes but does not emit a `colspan` for this merged header. HTML output alone does not establish correct spans. | [Merged table](results/features-latest.md#table-merged) |
| Borderless tables versus prose | pylopdf's text strategy detects the regular aligned label table, but also converts the two-column prose case into a table and changes the reference reading order. The default bordered strategy preserves the column reference order. This supports keeping text-table detection opt-in. | [Aligned table](results/features-latest.md#table-borderless-aligned), [prose columns](results/features-latest.md#two-column-order) |
| Math structure | The positioned fraction and Office equation do not become the supplied LaTeX reference in any mode. Layout-based PyMuPDF4LLM can emit an equation image. When ActualText already contains LaTeX, PyMuPDF text and PyMuPDF4LLM legacy retain that source hint; pylopdf and the layout modes omit it. Recovering a hint is different from reconstructing an equation. | [Positioned math](results/features-latest.md#positioned-math), [ActualText math](results/features-latest.md#math-actualtext) |
| Unicode and emoji | Every configuration retains all four strict Unicode-CMap probes, including supplementary scalars and emoji sequences. In the Office PDF, pylopdf and pypdf return a composed accent where PyMuPDF returns the source's decomposed sequence. This is a canonical Unicode difference, not proof of missing readable content. | [Unicode case](results/features-latest.md#unicode-cmap-and-emoji), [Office case](results/features-latest.md#omml-equations) |
| RTL and embedded numbers | pylopdf retains all three supplied logical strings, including the bracketed numeric token. The other configurations differ on at least one strict probe. This fixture tests visual glyph ordering with invisible text, not Arabic shaping or arbitrary mixed-direction paragraphs. | [RTL case](results/features-latest.md#rtl-visual-glyph-order) |
| Tagged reading order | Outputs choose different orders on the contrived tagged page. The stream order coincides with the tag order, so matching that reference does not prove that a tool consumed structure tags. A counterfactual untagged or reordered-stream control remains necessary for that attribution. | [Tagged case](results/features-latest.md#tagged-reading-order) |

The Type 3 corpus case separately retains pylopdf's known missing-Unicode
warning and empty extraction result. Color emoji in the Office PDF and invisible
surrogate-pair text are different source representations; results from one
should not be generalized to the other.

The [feature map](FEATURE_MAP.md) lists the review criteria and remaining gaps.
Automatic probes are useful for catching differences, while table geometry,
formula equivalence, internal-link resolution, and image placement still need
source-aware review. The [performance baseline](results/layout-latest.md)
provides before/after timings with exact-output guards for future optimizations.

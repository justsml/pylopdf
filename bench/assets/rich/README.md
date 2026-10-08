# Rich-content fixtures

`omml-equations.docx` is repository-authored synthetic data under the repository
MIT license. It contains a native Office Math Markup Language (OMML) fraction
with superscripts, embedded-font bold/italic text, and Unicode/emoji text.
`bench/generate_omml.py` contains the complete source and writes a deterministic
DOCX archive. It does not use a screenshot for the equation.

The bundled PDF was exported with LibreOffice 26.8.0.3 on Linux using
`pdf:writer_pdf_Export`. Reproduce with:

```bash
uv run python bench/generate_omml.py --export
```

Export uses a temporary isolated LibreOffice profile. Different office versions,
installed fonts, and PDF timestamps can change the exported PDF; benchmark the
bundled PDF for comparable input hashes. The fixture was visually checked to
contain the fraction `(x² + 1) / y = z²`, and its DOCX source retains the native
OMML nodes. Office stores equations in OMML, but that source tree is not retained
as equation markup in this exported PDF. See [Microsoft's math overview](https://learn.microsoft.com/en-us/office/math/).

The PDF embeds subsets of Liberation Serif, Noto Serif CJK SC, Noto Color Emoji,
and OpenSymbol. The color emoji are represented through Type 3 glyph programs,
which deliberately differs from the separate invisible Unicode-CMap fixture.
Font notices and licenses are retained in:

- [Liberation OFL](../../../LICENSES/Liberation-OFL-1.1.txt): Google and Red Hat.
- [Noto CJK OFL](../../../LICENSES/Noto-CJK-OFL-1.1.txt): Adobe and Google.
- [Noto Emoji OFL](../../../LICENSES/Noto-Emoji-OFL-1.1.txt): Google.
- [OpenSymbol MPL 2.0](../../../LICENSES/MPL-2.0.txt): Sun Microsystems and
  subsequent LibreOffice contributors. Its canonical source is
  [OpenSymbol.sfd at the export version](https://github.com/LibreOffice/core/blob/libreoffice-26.8.0.3/extras/source/truetype/symbol/OpenSymbol.sfd).

Other feature-study PDFs are generated from repository-authored content or
selected pages of the existing redistributable corpus. Their sources and
licenses remain documented in [the corpus README](../../../tests/assets/real_world/README.md).
Generated input PDFs and complete converter outputs are review data; multilingual
text in them is intentional fixture content.

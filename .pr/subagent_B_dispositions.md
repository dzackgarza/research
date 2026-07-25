## Lane B Dispositions

- PRRT_kwDOTBB78M6Qt9XF | computations/experiments/sage_lattice_category_spike/objects/categories.py:168 | gemini-code-assist | accepted-remediated | The thread’s requested `ValueError` replacement for missing element in `CountableSets.index` is now present in code (`raise ValueError(...)` instead of `assert False`). | No follow-up required unless additional exception-message wording standardization is desired.

- PRRT_kwDOTBB78M6QuNMZ | writing/Coble Research/knowledge/01_Lattices/Lattice Morphisms and Embeddings.md:26 | cubic-dev-ai | accepted-pending-fix | Line still contains invalid `*` subscripts (`Aut*{Lat}`, `GL*n`, `G*\beta`) in LaTeX. | Replace `*` with `_` and restore proper LaTeX subscripts exactly as suggested.

- PRRT_kwDOTBB78M6QuNMy | writing/Coble Research/knowledge/01_Lattices/E_n root lattices.md:17 | cubic-dev-ai | accepted-pending-fix | `\operatorname{Ann}*{E_8}` remains malformed and should be `\operatorname{Ann}_{E_8}`. | Apply the suggested replacement in both `E_7/E_6` lines.

- PRRT_kwDOTBB78M6QuNM_ | writing/Coble Research/knowledge/01_Lattices/Root lattice.md:14 | cubic-dev-ai | accepted-pending-fix | Definition callout is collapsed and LaTeX now uses `\mathbf{Z}*{\geq 0}` and `\sum*{...}` (invalid subscript syntax).
  | Restore split-callout body and `_` subscripts per the suggestion.

- PRRT_kwDOTBB78M6QuNNI | writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Coble_Surface_Cusps.md:9 | cubic-dev-ai | accepted-pending-fix | Figure caption still has literal asterisks in `G_{(9,9,1)*1}` and `G*{\gens{2} \oplus E_8(2)}`. | Restore underscore-based subscripts (`_1`, `_{...}`) exactly as suggested.

- PRRT_kwDOTBB78M6QuNNO | writing/Coble Research/content_pandoc/sections/Coble_Surfaces/Coble_Surface_Basics.md:70 | cubic-dev-ai | accepted-pending-fix | Footnote [^2] content is still split; second line became a code block and math is no longer in footnote context.
  | Re-indent continuation under `[^2]:` and keep math in footnote body.

- PRRT_kwDOTBB78M6QuNNZ | writing/Coble Research/knowledge/03_Compactifications/Coxeter Groups and Polytopes.md:13 | cubic-dev-ai | accepted-pending-fix | Callout header and body are still merged on one line, so definition text renders as title.
  | Split into proper Obsidian callout form with body on the next `> ...` line.

- PRRT_kwDOTBB78M6QuNNl | writing/Coble Research/knowledge/01_Lattices/Enriques lattice.md:19 | cubic-dev-ai | accepted-pending-fix | `H^2(Z; \mathbf{Z})*f` and `L*{\mathrm{En}}` still use `*`; this is not valid subscript syntax.
  | Replace with `_f` and `_{\mathrm{En}}` as indicated in suggestion.

- PRRT_kwDOTBB78M6QuNNx | writing/Coble Research/knowledge/01_Lattices/Type II Unimodular Lattices.md:13 | cubic-dev-ai | accepted-pending-fix | Callout still merged and LaTeX subscripts remain star-based (`\mathbf{Z}*{\geq 0}`, `\mathrm{II}*{p,q}`). | Split definition callout and restore proper underscore subscripts.

- PRRT_kwDOTBB78M6QuNN9 | writing/Coble Research/knowledge/01_Lattices/Torsion Bilinear and Quadratic Forms.md:13 | cubic-dev-ai | accepted-pending-fix | Definition body is still concatenated to callout title, causing rendering loss.
  | Restore original two-line callout with content on following `>` line.

- PRRT_kwDOTBB78M6QuNOW | writing/Coble Research/knowledge/01_Lattices/Gluing Overlattices.md:13 | cubic-dev-ai | accepted-pending-fix | Proposition title and opening sentence remain merged on same callout line.
  | Keep title text only in header and move sentence to callout body.

- PRRT_kwDOTBB78M6QuNOt | writing/Coble Research/knowledge/01_Lattices/Eichler-Siegel transformations on U+U.md:12 | cubic-dev-ai | accepted-pending-fix | The theorem body is still attached to callout header.
  | Split header/body lines to satisfy Obsidian callout semantics.

- PRRT_kwDOTBB78M6QuNO9 | writing/Coble Research/knowledge/01_Lattices/B_n and C_n root systems.md:13 | cubic-dev-ai | accepted-pending-fix | Example callout is malformed and body starts on header line.
  | Separate title from body; keep examples as bullet list in callout body.

- PRRT_kwDOTBB78M6QuNPI | writing/Coble Research/knowledge/01_Lattices/Nikulin's lattices V_k and U_k.md:14 | cubic-dev-ai | accepted-pending-fix | Definition callout still includes body text on first line and merged prose; renders poorly.
  | Move body to subsequent `> ...` line(s) and keep heading line minimal.

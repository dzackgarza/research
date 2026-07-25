# Lane A Subagent Dispositions

- PRRT_kwDOTBB78M6Qt9WO | computations/scripts/HayStack_Doc_Search.py:287 | gemini-code-assist | accepted-pending-fix | Python 2 exception syntax (`except OSError, ValueError`) is still present and will raise a `SyntaxError` in this Python 3 project.
  | Rewrite to `except (OSError, ValueError):` in the active branch, then re-run static checks.

- PRRT_kwDOTBB78M6QuNMX | writing/Coble Research/knowledge/01_Lattices/Genus of a Lattice.md:14 | cubic-dev-ai | accepted-pending-fix | The line-collapse corruption (`\mathbf{Z}*p`, `L*{2,`) remains; math subscripts in the definition are still broken.
  | Restore underscore subscripts per suggestion so the definition renders as `\mathbf{Z}_p` and `L_{2, ...}`.

- PRRT_kwDOTBB78M6QuNMv | writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Enriques_Surface_Cusps.md:7 | cubic-dev-ai | accepted-pending-fix | The `$\mathop{*}`-style substitutions remain in `G_{(10,10,0)*1}` and `G*{E_{10}(2)}`, so math notation is still incorrect.
  | Replace `*` with `_` in the affected caption subscripts.

- PRRT_kwDOTBB78M6QuNM6 | writing/Coble Research/knowledge/01_Lattices/2-Elementary Lattices.md:36 | cubic-dev-ai | accepted-pending-fix | The file still contains the malformed `*{n*+}` form, so the signature subscript notation is not fixed.
  | Restore `*` to `_` to return `(... )_{n_+}`.

- PRRT_kwDOTBB78M6QuNNF | writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Coble_Surface_Cusps.md:11 | cubic-dev-ai | accepted-pending-fix | Subscripts in `$(7, 7, 1)*0` and `$F*\Co$` remain broken with literal `*`, and output is currently noncompliant.
  | Apply suggested replacements `_(... )_` for both instances in the caption.

- PRRT_kwDOTBB78M6QuNNL | writing/Coble Research/knowledge/01_Lattices/Gram Matrix.md:14 | cubic-dev-ai | accepted-pending-fix | Multiple math fragments still use `*`-subscript form and the line remains merged into the title; rendering is still wrong.
  | Split/restore each expression to `_(...)_` and keep line structure intact.

- PRRT_kwDOTBB78M6QuNNV | writing/Coble Research/knowledge/01_Lattices/Type I Unimodular Lattices.md:13 | cubic-dev-ai | accepted-pending-fix | `\mathrm{id}*{p \times p}` and `\mathrm{id}*{q \times q}` are still present; matrix subscripts are still incorrect.
  | Change both to underscore subscripts as in `\mathrm{id}_{p \times p}` and `\mathrm{id}_{q \times q}`.

- PRRT_kwDOTBB78M6QuNNk | writing/Coble Research/knowledge/02_Moduli/ADE and BC Surfaces.md:14 | cubic-dev-ai | accepted-pending-fix | The callout title/body is still merged on one line, so definition content is being consumed by the title.
  | Split back into `[!definition]` title line and separate content line(s).

- PRRT_kwDOTBB78M6QuNNq | writing/Coble Research/knowledge/02_Moduli/Noether-Lefschetz Locus for Enriques Surfaces.md:12 | cubic-dev-ai | accepted-pending-fix | `\mathrm{NL}*{T*{\mathrm{En}}}` and related subscript corruption remains in the definition header and body.
  | Restore `\mathrm{NL}_{T_{\mathrm{En}}}` and related subscript syntax.

- PRRT_kwDOTBB78M6QuNN6 | writing/Coble Research/knowledge/01_Lattices/A_n root lattice.md:14 | cubic-dev-ai | accepted-pending-fix | The displayed math is still embedded inline in a quote line, so markdown renderers may treat it as inline math.
  | Move the `$$ ... $$` equation to its own blockquoted lines.

- PRRT_kwDOTBB78M6QuNOP | justfile:110 | cubic-dev-ai | accepted-pending-fix | `test-ci` no longer depends on `test` and now drops repository and spike-level gate behavior in this branch.
  | Restore `test` prerequisite and preserve the full CI command invocation.

- PRRT_kwDOTBB78M6QuNOo | writing/Coble Research/content_pandoc/sections/Lattices_and_Moduli/Coble_Moduli_Basics.md:20 | cubic-dev-ai | accepted-pending-fix | The fenced div opening is still split as `:::` + `:{.remark}`, leaving unmatched/blocking pandoc structure.
  | Change back to single-line opening `:::: {.remark}`.

- PRRT_kwDOTBB78M6QuNO5 | writing/Coble Research/knowledge/01_Lattices/Geometric Identification of the Dual Lattice.md:12 | cubic-dev-ai | accepted-pending-fix | The theorem header still merges with first sentence, so callout content is not clearly separated.
  | Restore `[!theorem] Geometric Identification of the Dual Lattice` line and move body text below.

- PRRT_kwDOTBB78M6QuNPF | writing/Coble Research/knowledge/02_Moduli/The K3 Double Cover construction.md:11 | cubic-dev-ai | accepted-pending-fix | `[!remark]` title remains concatenated with content, so renderer treats both as title text.
  | Restore a separate title line and one or more `> ...` content lines.

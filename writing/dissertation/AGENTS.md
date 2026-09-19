# Dissertation

Markdown source of *Compact Moduli of Numerically Polarized Degree Two Enriques
Surfaces* (D. Zack Garza, University of Georgia, 2025), and its build.

- `main.md` — front-matter metadata (title page, committee, abstract, index words)
  and the ordered `include` list of section files.
- `sections/` — one directory per part, one per chapter, numbered files per
  section. `#` is a part, `##` a chapter, `###` a section. Theorem-like
  environments are fenced divs (`:::{.theorem title="..."}`); cross-references
  use typed Pandoc-crossref IDs and `@...` references; citations use Pandoc citation syntax (`@key` or `[@key]`) with Better BibTeX keys. The full
  conventions are `~/.pandoc/AUTHORING_STYLE.md`.
- `figures` — symlink to `~/.pandoc/figures`, the single owner of every figure and
  its editable source.
- `submitted-2025-08-12.pdf` — the dissertation as submitted to the UGA Graduate
  School, 227 pages, built from the LaTeX that this Markdown superseded. It is a
  record, not a build target; `just compile` does not produce it and will not
  match it page for page.

## Build

```bash
just compile          # dissertation-<date>.pdf via ~/.pandoc (pandoc -> latexmk)
just preview FILE     # live preview of one section
just format-md        # normalize markdown
```

Everything the build needs lives in `~/.pandoc`: the page template
`templates/uga-dissertation.tex`, the macro package `styles/dzg-dissertation.sty`
(shared tiers plus `styles/macros/dissertation-overrides.tex`), TikZ sources under
`figures/tikz/dissertation/`, and the bibliography `bib/references.bib`, which is
the live Zotero export. A citation key that does not resolve there is fixed in
Zotero, never in a local bib file.

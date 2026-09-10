# Coble project — agent instructions

## What this directory is

One vault for the Coble surfaces work. Every page is one topic. The mathematics that is
written up sits beside the computations and the open questions that produced it. There
is no separate "paper" tree and no separate "notes" tree.

The vault is the Coble part of the Quarto site rooted at `writing/`. Pages are listed as
chapters in `writing/.book/_quarto.yml`; a new page is not published until it is added there.

```
<topic>/            One directory per topic, kebab-case, one page per file
index.md            The part landing page
summary.md          Project status: what is proven, what is blocked
papers/             Extracted third-party sources, one directory per citation key
reference/          Source PDFs and the last built version of the paper
scripts/            The computational toolchain
tables/             Generated lattice and diagram tables
heegner-report/     A standalone research report and its own bibliography
coble_supplement.bib  Project-local entries not yet in the global bibliography
```

## Building

The site builds from the repository root, not from here.

```bash
just docs-preview                # serve the site locally with live reload
just docs-lint coble/<page>.md   # render one page, in seconds
just docs-check                  # render, then fail on any citation, cross-ref, or link defect
```

There is no PDF build for this work. The last dated PDF build is kept in `reference/`.

## Citations

Zotero is the source of truth for references. The global bibliography is exported to
`~/.pandoc/bib/references.bib` and copied to `writing/.book/references.bib` by the build.

To cite a work, use its Better BibTeX key: `@AE23`. If the work is not in Zotero, add it
there first, by DOI or arXiv identifier, through the live local API. See the `zotero`
skill.

`coble_supplement.bib` holds only entries that have no global counterpart yet. Adding an
entry there is a stopgap; the work still belongs in Zotero.

Never write a citation as an inline URL to arXiv, a DOI, or nLab. The docs gate rejects
it.

## Writing conventions

Numbered environments go through the `custom-numbered-blocks` filter:

```markdown
::: {.Theorem #thm:coble-cusps}
### Cusps of the Coble moduli space

...
:::
```

Reference it as `\ref{thm:coble-cusps}`, or `\longref{thm:coble-cusps}` for
"Theorem 2.9". Labels use colon separators. Do not start a label with a Quarto-reserved
prefix (`def-`, `thm-`, `lem-`, `cor-`, `prp-`, `cnj-`, `exm-`, `exr-`, `fig-`, `tbl-`,
`eq-`, `sec-`, `lst-`); Quarto hijacks those for its own crossrefs and the render fails.

## What a cross-reference can reach

`\ref` and `\longref` are the only two commands that resolve here. The resolver is
`writing/.book/_extensions/ute/custom-numbered-blocks/cnb-3-crossref.lua`, and it
matches those two literal strings and nothing else.

**A `\cref` or `\Cref` renders as nothing.** It never matches, and pandoc then drops the
unmatched macro rather than printing it, so the reference does not appear as visible
broken text — it disappears, and the sentence around it is left dangling: "the 3-step
chain $W_0 \subset W_1 \subset W_2 \subset W_3$ of ." That is how 390 of them
accumulated unnoticed. `docs-check` now scans the sources for them, because there is
nothing in the rendered HTML to find.

**`\longref` reaches numbered blocks only.** The resolver keeps a registry of the blocks
it has processed, so a target that is not one of them resolves to nothing however it is
written:

- sections, `\longref{sec:lattice-theory}` — write the section's name in prose instead;
- figures and tables, `\longref{fig:coble-cusps}` — an anchor like `{#fig:x width=70%}`
  or a `\label{tbl:x}` is not a numbered block;
- more than one target, `\longref{a,b}` — the resolver matches a single id.

## The two parts cannot reference each other

The Coble part uses the numbered-block filter above. The category-theory part uses
Quarto's own crossrefs, `::: {#def-x}` referenced as `@def-x`. Neither resolver sees the
other's registry, and there is no cross-part reference anywhere in the book.

So "state it once and cite it from the other part" is not available, and proposing it
produces references that resolve to nothing. When a notion is needed on both sides:

1. One defining occurrence **per part**, never two within a part.
2. A notion appears in a part only if that part's own results use it. Do not import a
   notion because the other part has it.
3. Where both parts state it, the statements must agree — same convention, same formula,
   each independently correct.

The canonical form of a Coxeter system is stated in both parts for this reason, and the
two agree character for character. That is permitted; a second occurrence inside one
part is not.

## What is not part of this book

`writing/.book` links in `category-theory`, `coble`, `data` and `index.md`. Everything
else under `writing/` — the dissertation, the research statement, the talks, the exams —
builds through `~/.pandoc`, whose template loads **cleveref**. There `\cref` is the
correct command and `\longref` does not exist. Never sweep a reference fix across
`writing/` as a whole; the boundary is what `writing/.book` links in, not a path list.

Do not number headings by hand. Sections auto-number and are referenced by `@sec-`.

The declared block classes are listed at the bottom of `writing/.book/_quarto.yml`. Add a class
there before using it.

## Extracted papers

`papers/<KEY>/` holds a source archive for a third-party paper: its LaTeX, its figures,
and where available a readable extraction. These are read-only reference material.

The extraction pipeline resolves `\cite{}` to `?` and `\ref{}` to `[0]`. Read an
extraction for its mathematics, never for its citations or its internal numbering; go to
the PDF for those.

Do not commit LaTeX build intermediates alongside an extraction.

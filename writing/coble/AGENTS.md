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
papers/             Extracted third-party sources, one directory per citation key
reference/          Source PDFs and the last built version of the paper
scripts/            The computational toolchain
tables/             Generated lattice and diagram tables
heegner-report/     A standalone research report and its own bibliography
coble_supplement.bib  Project-local entries not yet in the global bibliography
```

A page that is not listed in `writing/.book/_quarto.yml` does not render at all. Check
that in **both directions** after adding pages: every entry in the chapter list has a
file, *and* every prose file is either listed or deliberately unlisted. The first check
alone passes while a page you just wrote is invisible, which is how eleven chapters of
absorbed mathematics came to be committed and unpublished.

## Where a new chapter goes

`writing/.book/_quarto.yml` is not a manifest of files that exist. It is the book's
**reading order**, and it is the only place that order is written down. A chapter's
position makes two claims about its mathematics:

- everything it uses is defined above it, and
- the part it sits in names the subject it is about.

So a page is placed by **reading it**: what it defines, what it uses, and which of the
two the rest of the part does. Appending to the end of a part, or inserting next to a
file with a similar name, decides neither question. Filename order is unrelated to
dependency order — sorting three Coble-lattice chapters by filename once produced the
exact reverse of the order their own references require, and put all three inside the
general lattice run whose results they depend on.

Three checks, each cheap, each catching a different defect:

- **Dependency.** For each `\ref`/`\longref` in the new page, find the page that
  defines the target. Every one should be earlier. A handful of forward references is
  normal in a book; a page whose targets are mostly later is in the wrong place.
- **Subject.** Say what the part is about in one clause, then check the new page is
  about that. General machinery and this project's own results are different subjects
  and belong in different parts, however closely related — that split is what keeps
  either readable.
- **Size.** A part of a dozen chapters has stopped being a group. Split it at the seam
  the mathematics already has.

A page's own frontmatter often settles the grouping: `unit:` distinguishes a reusable
`method` from the `computation` it produced and from a `research-program`, and
`status: conjectural` marks what is not proved. The Computations run and the open-problems
run are grouped on exactly those fields.

Title a chapter with its subject, never with its format. "Lattice Summary" told a reader
nothing and hid a chapter about Baily--Borel embeddings inside the lattice-theory run.
One level-1 heading per page: later `# ` headings are sections, so write them as `##`.

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

**`\longref` reaches any numbered block in the book**, in any chapter, in either
direction. That holds because every chapter is symlinked flat into `writing/.book`,
which gives the resolver one registry instead of one per topic directory, and because
the gate renders twice, which is what lets a reference reach a block declared later.
Both are load-bearing: `writing/.book/TRAPS.md` records what breaks without them.

A target that is not a numbered block still resolves to nothing however it is written:

- sections, `\longref{sec:lattice-theory}` — link to the section instead, the way the
  category-theory part does: `[Lattice Theory](lattice-theory.md#sec:lattice-theory)`;
- tables, `\label{tbl:x}` — a table carries no number here; link to the page that
  holds it;
- more than one target, `\longref{a,b}` — the resolver matches a single id.

**Figures use Quarto's own numbering, not this filter.** Anchor a figure `{#fig-x}`,
with a hyphen, and reference it `@fig-x`. Quarto then numbers it within its chapter
(Figure 65.1) and resolves the reference across the book. The reserved-prefix warning
above is about numbered blocks: for a figure the prefix is what makes it work. The
image itself lives in the shared pandoc-config repo and is staged into the book by
`scripts/docs_figures.py`; citing a figure that is not there fails the build rather
than rendering a broken image.

## The two parts cannot reference each other

The Coble part uses the numbered-block filter above. The category-theory part uses
Quarto's own crossrefs, `::: {#def-x}` referenced as `@def-x`. Neither resolver sees the
other's registry, and there is no cross-part reference anywhere in the book, so a
reference written from one part to a label in the other resolves to nothing.

A notion both parts need is therefore stated in both, and the two statements must agree.
The canonical form of a Coxeter system is stated twice for this reason.

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

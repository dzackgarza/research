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

- **Dependency.** For each `@thm:key` reference in the new page, find the page that
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

Cite the Stacks Project by tag, `[@stacks-02LS]`. The `stacks-tags` filter rewrites the
key to the single global Stacks entry and appends a hyperlinked `[Tag 02LS]`; verify the
tag against the tag page before using it, since a wrong tag still renders.

## Writing conventions

Numbered environments use the same syntax as the pandoc papers, which the amsenv filter
(`~/.pandoc/filters/convert_amsthm_envs.lua`) turns into amsthm environments and
cleveref references for LaTeX:

```markdown
::: {.theorem #thm:coble-cusps title="Cusps of the Coble moduli space"}

...
:::
```

The class is the full lowercase environment name (`.definition`, `.proposition`,
`.theorem`). The id is a family prefix, a colon, and a key. Reference the block as
`@thm:coble-cusps` for "Theorem 2.9", or `[-@thm:coble-cusps]` for the bare "2.9".
A bracketed cluster keeps its text: `[see @thm:a, (ii); @lem:b]`.

The family prefixes are `ass clm conj cons conv cor def ex exr lem not obs prob prop
qst rmk thm warn`. The registry is `THEOREM_FAMILY_METADATA` in the zettlr-pandoc
fork; the amsenv filter and `writing/.book/_extensions/local/amsthm-refs` mirror it.
The colon keeps these ids apart from Quarto's reserved hyphen prefixes (`def-`,
`thm-`, `fig-`, `sec-`, ...), which Quarto takes for its own crossrefs.

## What a cross-reference can reach

The `amsthm-refs` filter rewrites every theorem-family citation into the `\ref` and
`\longref` commands that `custom-numbered-blocks` resolves
(`writing/.book/_extensions/ute/custom-numbered-blocks/cnb-3-crossref.lua`). A cluster
that holds any other key, such as a bibliography key, goes to citeproc unchanged.

**A reference to an id that no block declares renders as nothing.** cnb drops it, and
the sentence around it is left dangling: "the meanings fixed in ." Raw LaTeX such as
`\cref{x}` disappears the same way. `docs-check` scans the sources for both, because
there is nothing in the rendered HTML to find.

**A reference reaches any numbered block in the book**, in any chapter and in either
part, in either direction. That holds because every chapter is symlinked flat into
`writing/.book`, which gives the resolver one registry instead of one per topic
directory, and because the gate renders twice, which is what lets a reference reach a
block declared later. Both are load-bearing: `writing/.book/TRAPS.md` records what
breaks without them. Ids must therefore be unique across the whole book.

A target that is not a numbered block does not resolve through this filter:

- sections — anchor the heading `{#sec-x}` and reference it `@sec-x`, or link to it;
- tables — a table carries no number here; link to the page that holds it.

**Figures use Quarto's own numbering, not this filter.** Anchor a figure `{#fig-x}`,
with a hyphen, and reference it `@fig-x`. Quarto then numbers it within its chapter
(Figure 65.1) and resolves the reference across the book. The image itself lives in
the shared pandoc-config repo and is staged into the book by
`scripts/docs_figures.py`; citing a figure that is not there fails the build rather
than rendering a broken image.

## What is not part of this book

`writing/.book` links in `category-theory`, `coble`, `data` and `index.md`. Everything
else under `writing/` — the dissertation, the research statement, the talks, the exams —
builds through `~/.pandoc`. The theorem syntax is the same there, so a block moves
between the book and a paper unchanged. The book's own mechanics (the flat chapter
links, the two renders, the declared block classes) stop at what `writing/.book` links
in, not at a path list.

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

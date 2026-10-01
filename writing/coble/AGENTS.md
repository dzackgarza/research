# Coble project — agent instructions

## What this directory is

One vault for the Coble surfaces work. Every page is one topic. The mathematics that is
written up sits beside the computations and the open questions that produced it. There
is no separate "paper" tree and no separate "notes" tree.

The vault is the Coble part of the Quarto site rooted at `writing/`. Pages are listed as
chapters in `writing/.book/_quarto.yml`; a new page is not published until it is added there.

```text
<topic>/            One directory per topic, kebab-case, one page per file
index.md            The part landing page
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

Placement of chapters, block syntax, references, and citations follow the
[writing house conventions](../../CONTRIBUTING.md#writing-house-conventions).

## Extracted papers

`papers/<KEY>/` holds a source archive for a third-party paper: its LaTeX, its figures,
and where available a readable extraction. These are read-only reference material.

The extraction pipeline resolves `\cite{}` to `?` and `\ref{}` to `[0]`. Read an
extraction for its mathematics, never for its citations or its internal numbering; go to
the PDF for those.

Do not commit LaTeX build intermediates alongside an extraction.

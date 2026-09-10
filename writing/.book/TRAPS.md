# Quarto traps in this layout

This directory is the Quarto project root; the parts of the book reach it as
symlinks from `writing/`. Quarto's symlink support is partial and its failures are
silent, so each constraint below is a verified measurement, not a guess. Upstream:
[quarto-cli#4167](https://github.com/quarto-dev/quarto-cli/issues/4167),
[#5807](https://github.com/quarto-dev/quarto-cli/issues/5807),
[#9069](https://github.com/quarto-dev/quarto-cli/issues/9069).

The one fact underneath all of them: **Quarto resolves a project-relative path
against this directory, but pandoc runs with its working directory at the real
location of the input.** For every symlinked part those differ by exactly one
level, at every input depth.

## A filter given as a path is not found

`filters: [stacks-tags.lua]` fails with `cannot open ../stacks-tags.lua`. Package
the filter as an extension under `_extensions/local/` and name it. Extension
filters are resolved by name and are immune.

## Anything pandoc opens itself must live in `.assets/`

The bibliographies and the header includes are opened by pandoc, so their relative
path lands one level above this directory — that is, in `writing/`. They are kept
in `writing/.assets/`, reached from here through a symlink, so both tools find
them. Assets Quarto resolves and copies (the stylesheet) need none of this.

## A directory in `resources:` copies nothing, and says nothing

Quarto's resource collection walks the project directory and does not enter a
symlink, with or without a glob. `resources: [data]` and `resources: [data/**]`
both produce an empty result and no warning. Single named files still work and
stay in `_quarto.yml`; the resource trees are copied by `.assets/copy-resources.sh`
as a post-render step.

## Only `book.chapters` renders; `render:` entries are ignored

Behind a symlink, Quarto renders exactly the files `book.chapters` names. A page
listed in `project: render:` is skipped with no page and no error, and a glob
there matches nothing. There is therefore **no way to have a page that renders and
is searchable but stays out of the sidebar** for anything under a symlinked part.

Measured in an isolated two-page project: with `render:` naming `index.md`,
`gen/alpha.md` and `gen/beta.md`, and only `index.md` in `chapters:`, the render
reported success and produced `index.html` alone.

This is why the generated inventory lives at `.book/inventory/`, a real directory
inside this project root, where globs, render lists and discovery all behave
normally. Generated pages go there; authored prose never does.

## Two Quarto processes on one project corrupt each other

Quarto renders each input to a sibling `.html` beside the source, then moves it
into `_site`. Two processes — a `quarto preview` left running and a `quarto
render` from the gate — write and move the same intermediate paths, and one
steals the other's file. The symptom is a rename failure naming a file that
"does not exist", on a different chapter each run.

A writer outside Quarto does the same thing: an agent editing prose in a
directory during a render can remove an intermediate before Quarto reaches it.
Do not run a full render while another process is writing under `writing/`.

`docs_check.py` stops if a preview is listening, because the failure is otherwise
read as a defect in the book.

## A part replaced by a copy renders green

If a symlink here is replaced by a real copy — which a rename-into-place writer
will do — the book renders perfectly from the copy while the copy and the prose
drift apart. `docs_check.py` checks every linked part before rendering, for that
reason.

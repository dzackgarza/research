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

## A book renders exactly `book.chapters`, and nothing else

`project: type: book` publishes the files `book.chapters` names. Nothing else
reaches the site: not a file discovered in the project directory, not one named
explicitly in `project: render:`, not one matched by a glob there. The skip is
silent — the render reports success and the page simply does not exist.

**This has nothing to do with symlinks.** Measured twice in isolated projects, once
with the extra pages behind a symlink and once with them in a real directory inside
the project root: in both, `render:` named four files, `chapters:` named two, and
exactly the two chapters were produced.

So there is **no way to have a page that renders and is searchable but stays out of
the sidebar** in a book project. A page is a chapter or it is not published. The
alternatives are to list it, or to generate standalone HTML the way
`category-theory/lean/category-graph.html` does and link to it from a chapter.

(A `website` project does render discovered files. A book does not.)

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

## `ruamel.yaml` does not round-trip `_quarto.yml`

Loading and dumping this file with the obvious comment-preserving YAML library
reattaches comment blocks across item boundaries, truncates the item they were
attached to, and reindents every list in the file. Edit `_quarto.yml` by line and
parse it afterwards to check the structure, rather than round-tripping it.

Reported by a parallel session that hit it while merging chapter entries; the
damage was caught before it was committed.

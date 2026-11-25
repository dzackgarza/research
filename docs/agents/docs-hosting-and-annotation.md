# Docs hosting and annotation

## Docs hosting surfaces

The docs book ships as a Quarto site (`writing/.book/_quarto.yml`, `project.type: book`) in three surfaces.

`writing/` holds only authored prose. Every piece of Quarto machinery — the config, the
extensions, the Lua filters, the CSS, the bibliographies, the render cache and the build
output — lives in `writing/.book/`, which is the project root. Each part of the book is
symlinked into that directory (`index.md`, `category-theory`, `coble`, `data`), so book
membership is what `ls writing/.book` shows, and the writing that is not site content
(the dissertation, talks, exams, research statement) is excluded simply by not being
linked in. Edit the real file under `writing/`; the symlink is only how Quarto reaches it.

- **Local site** — http://lattice-research.localhost/, served by nginx from
  `/var/www/static-sites/lattice-research`, which is a symlink straight at
  `writing/.book/_site`. `just docs-deploy` rebuilds it: the gate runs first, so a book
  with a broken citation or a dangling reference never reaches the served copy. Local site updates use an explicit docs-deploy; the push gate does not render
  or deploy. GitHub Pages has a separate push-triggered docs workflow. The dashboard picks
  the site up on its own — it lists every directory under `/var/www/static-sites` that
  has an `index.html`, and takes the card's name from that page's `<title>`.

- **Local preview** — `just docs-preview` serves `writing/.book` at http://localhost:7654/
  with live reload, for the annotation loop below and for tight edit-and-look work. Run
  it when you want it and stop it when you are done: it is not a service, and `docs-check`
  refuses to start while it is running, because the two renders write the same
  intermediate paths and corrupt each other.

- **Published site** — GitHub Pages at https://dzackgarza.github.io/research/ (`build_type: workflow`, branch `main`), deployed by `.github/workflows/docs.yml`. The site-url is recorded in `_quarto.yml` (`book.site-url`). The lattice database is published separately, at https://dzackgarza.github.io/lattice-database/, from its own repository.

- **GitHub wiki** — the repo's native GitHub wiki is **disabled** (no `wiki/` ref exists; `hasWiki: true` in API but no commits).
  Do not conflate "the wiki" (historical name for the docs book, migrated via PR #272 "wiki-book-migration") with the GitHub wiki feature.
  The book under `writing/` is the wiki's successor.

A push of `main` that changes `writing/` triggers `docs.yml` and redeploys Pages; local edits do not appear on the published site until pushed.

The two gates read different bibliographies. `just docs-check` copies `~/.pandoc/bib/references.bib`, the working copy of the `pandoc-config` clone; `docs.yml` clones that repository's `main`. While the working copy holds an uncommitted bib edit, the local gate and the CI gate disagree on which citation keys are undefined.

## Annotation feedback loop

The user delivers docs feedback by annotating the rendered pages in the browser; the `annotate` CLI turns those annotations into a committed batch the agent acts on.
The CLI is not installed on `PATH` (`/bin/annotate` is an unrelated tool) — it is the `uvx`-installable console script from the Hypothesis fork at `~/gitclones/hypothesis-fork-project/hypothesis-review`, always invoked from `~/research` as:

```bash
uvx --from ~/gitclones/hypothesis-fork-project/hypothesis-review annotate <subcommand>
```

`<subcommand>` is `wait` / `pull` / `slice` / `record` / `resolve` / `status` / `doctor`; the steps below name it bare for readability.
One cycle:

1. **Serve** — `just docs-preview` runs in the background on `:7654`.

2. **Open a session** — from `~/research`, `annotate doctor` first confirms readiness (inside a git repo, `h` API + Postgres reachable), then `annotate wait` records the open timestamp locally and blocks, serving the loopback session-close endpoint on `127.0.0.1:8902`, waiting for the browser.
   A *session* is a time window.
   Run it as a background job so the agent can keep working while the window is open.
   **Spawn `annotate wait` with `notifyOnExit: true`** (or the equivalent exit-notification flag on your PTY/spawn tool) so that when the user hits **Send to agent** and `wait` exits, the agent receives the completion signal automatically instead of having to poll.
   Do not poll with `pty_read` + sleep loops to detect completion; wait for the exit notification.

3. **Annotate** — over the `:7654` pages, the user highlights spans and writes comments via the Hypothesis client, then hits **Send to agent**. That closes the window and unblocks `wait`.

4. **Record + deliver** — `wait` collects every annotation created during the window, appends them to `feedback/ledger.jsonl`, commits (`feedback: record N annotation(s) …`), *then* drains them from `h`, and prints the batch JSON. **Record-before-drain is the safety property**: feedback cannot reach the agent unrecorded, and a failed write leaves the notes in the sidebar rather than deleting the only copy.
   (`pull` does the same for an already-open session; `slice`+`record` capture ad-hoc notes made outside a session.)

5. **Act (agent)** — read the batch / ledger.
   **Discuss before editing.** An annotation identifies a concern; it is not an implementation instruction.
   Before changing any artifact, discuss the intended update with the user and obtain explicit approval.
   For mathematical feedback, establish the correct theory and the source that states it before proposing prose.
   Do not make a reflexive local correction from the quoted span or from memory: confirm that the proposed change fits the document's global mathematical story.

   Each entry's `uri` (`localhost:7654/category-theory/Roadmap.html`) plus the normalized `TextQuoteSelector.exact` pin the exact source span → map to `writing/category-theory/Roadmap.md` and apply the edit.
   Hot-reload re-renders each touched page live: the tight edit → one reload → look cycle.

6. **Resolve** — `annotate resolve` tags the batch acted via the Hypothesis API, dropping it from the open set (`annotate status` shows open vs. acted).
   Commit the doc edits alongside the already-committed ledger so git history anchors each note to the state it landed against.

7. **Reopen** — `annotate wait` again for the next window (with `notifyOnExit: true`). Back to step 2.

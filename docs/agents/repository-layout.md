# Repository layout

Top-level directories (this is a navigational map; each tree owns its own README/AGENTS.md):

- **`computations/`** — the working computational corpus.
  Its `experiments/` subtree holds the **spikes** (see the lineage note below and [adding a spike](adding-a-spike.md)). Other subdirs are task-specific: `vendor/` (third-party code — see below), `coxiter/` (CoxIter tool integration), `enriques-moduli/` + `enriques-paper-artifacts/` (Enriques-surface moduli work), `notebooks/` (**the user's plane — see below**), `scripts/` (one-off and exploratory scripts — **the only `scripts/` dir; it is QC-exempt**, and is where exploratory code is relocated to de-scope it from the strict gates; holds `components/`, the reusable computation pieces such as the `coxeter-vinberg/` prototypes, relocated here in `746595e`, and the exploratory `lattice-orbits/` isotropic-orbit scripts), `reports/` (generated output).

- **`src/`** — the installable package (`dzack_research`). The session preamble is `src/dzack_research/preamble/`; `from dzack_research.preamble.all import *` is the session import. The mathematical library lives in [sage-extensions](https://github.com/dzackgarza/sage-extensions) (`sage_extensions`), a git dependency on its `main` head. Non-mathematical repository tooling that analyzes or generates source artifacts lives under `src/dzack_research/utilities/` and is not part of the preamble session surface. **Migration criterion:** code lives in a spike until it has matured past spike status and is usable for real research — demonstrated by *shipped, tested, high-level notebooks* that do actual work with it.
  Only then does it migrate here, and the move is the semantic statement that it is meant to be shared and reused.
  Do not promote code into `src/` because it looks finished; promote it when a notebook proves a researcher can use it.

- **`computations/`** is the JupyterLab `root_dir`, so the live research control surface opens at the computational workspace rather than at `$HOME` or only the notebook subtree.
- **`computations/notebooks/`** — **the user's notebook audit and control plane, not agent work.** It is not subject to QC, to layout conventions, to naming or taxonomy rules, or to agent tidying: no agent proposes reorganizing it, splitting it, imposing folder schemes on it, or holding its contents to the standards that govern `src/` and the spikes.
  Agents write here only when explicitly asked.
  What agents *may* do is make things reachable from it — see the symlinks below.

  Reachability is by symlink, verified working through the live server (list, open, save, delete all round-trip to the real path, no restart needed):

  - `archive/` → `archives/notebooks/` — the retired notebooks, still live reference material

  Symlinking is preferred over moving: the originals stay in the tree that owns them (archive stays QC-exempt), while the control plane can see everything.

  **Implicit typesetting:** a bare `X` at the end of a cell renders as LaTeX when Sage can genuinely typeset `X`, so `show()` is not needed for ordinary inspection.
  Explicit `show()` still works and is still worth writing where the intent is presentation rather than inspection.

  The source of that behaviour is **`sage-init.sage` at the repo root** — tracked here, because it is part of how this repo's notebooks are meant to read. It loads `dzack_research.preamble.all`.
  It becomes active only by being linked to Sage's startup file. `just sage-init-install` links `${DOT_SAGE:-~/.sage}/init.sage` to `sage-init.sage`, and `just sage-init-check` proves in a real kernel that Sage objects typeset and plain text does not:

  ```
  just sage-init-install
  just sage-init-check
  ```

  `sage-init-install` is idempotent and refuses to replace anything it did not create, including a symlink pointing elsewhere — a pre-existing `init.sage` is never clobbered.
  Sage reads that one file for the terminal REPL *and* every Jupyter kernel, so installing it once covers both with nothing to remember per notebook.

  It is deliberately *not* `%display latex`, which also typesets strings, numpy arrays and opaque objects into unreadable character-by-character fallbacks; the file's own header comment records the measurements behind that choice.
  Being a tracked `.sage` file it is in Sage QC scope: it passes `_sage-syntax` (the commit tier) and draws no vulture findings.

- **`computations/vendor/`** — **third-party code you did not write.** Clone or drop external scripts here and they are importable from every Sage process (CLI, `sage -python`, every Jupyter kernel) with no restart and no registration; see its README. Contents are gitignored, and `vendor` is already a globally QC-excluded directory name, so external code never enters the gates.
  Nothing authored here ever graduates — write your own code in a spike.

**How code becomes importable in a Sage notebook.** One rule per kind, no bespoke path plumbing:

| Kind | Home | Made importable by |
| --- | --- | --- |
| External, published | — | `sage -pip install <pkg>` (or `sage -pip install "<name> @ git+<url>"` when it has no PyPI wheel, as `ore_algebra` does) |
| External, unpackaged | `computations/vendor/` | drop it there; `sage-init.sage` puts it on `sys.path` for interactive sessions |
| Ours, spike | `computations/experiments/<name>_spike/` | `sage -pip install --no-deps -e <spike-dir>` (already done for both spikes; edits are live) |
| Ours, graduated | `src/dzack_research/` | `sage -pip install --no-deps -e .` (already done; edits are live) |

Editable installs point at the working tree, so a rebuilt or reinstalled Sage is the only thing that breaks them — re-run the two `-e` installs and check the vendor path with `sage -c 'import _vendor_selfcheck'`.

- **`tests/`** — the expectation suite (`tests/constructions/`, `tests/user_simulations/`, `tests/conftest.py`) and the tests of the research tooling. The implementation tests, the test lint, the suite budget and the coverage recipes live in sage-extensions.
  The archived preamble's tests travelled with it to `archives/preamble/tests/`.
  Spike tests live in each spike's own `tests/` tree.
  The original lattice-research source is retained by the research repository’s archival tags and [provenance records](../../archives/provenance/lattice-research/README.md). Its former submodule is retired.

- **The lattice database** — the catalogue of lattices, one record per lattice, and its site, live in their own repository, `dzackgarza/lattice-database`. It imports this preamble from research's `src/`, so a preamble change can break its build; its nightly `verify` workflow checks it against `research` `main`. Its `AGENTS.md` owns the rule that it stores every computation about its lattices.

- **`writing/`** — authored prose: the Coble paper draft and research notes, oral exams, research statement, talks.
  The user's durable authored artifacts — preserve native LaTeX/tikz source.

- **`notes/`** — research notes (`computations/`, `papers/`, `topics/`). The terminology-drift dictionary is **not** here; it is vault-owned at `.agents/references/terminology-dictionary.md` (see the banned-language index in `AGENTS.md`).

- **`references/`** — external inputs: `pdfs/`, `generated-indexes/`, `local-system-dependencies/`.

- **`archives/`** — retired material (`provenance/`, `preamble/`, `notebooks/`).

## Source index (ctags)

`just tags` writes a Universal Ctags index of `src/` to `tags` at the repo
root. Use it to find where a class, method, or function is defined, instead of
searching the tree by name. Every entry carries a `class:` scope field, which
tells apart the many same-named methods the category tree holds — 403 tags for
`__init__`, 243 for `super_categories`.

The file is gitignored. It goes stale as soon as a definition in `src/`
changes, so run `just tags` yourself before you trust it. The run takes about
0.1 seconds.

## category_specs and the absorbed spikes (prior attempts at the same substrate)

The goal — a mathematically-semantic, Sage-compatible substrate for exact lattice/surface computation — had three earlier attempts, all finished as separate surfaces:

- **`archives/provenance/lattice-research/source-main/category_specs/`** — the frozen first attempt; the historical source references, retained mathematical results and live acceptance requirements are linked in its [provenance README](../../archives/provenance/lattice-research/README.md). Parity-audit issues citing `category_specs/…` paths refer to that source.

- **The spikes** (`sage_lattice_category_spike`, `sage_lattice_feature_spike`) — the second attempt — were absorbed into the preamble and deleted on 2026-08-19 (PLAN-spike-absorption-workstreams; the migration commits' bodies record each notion's origin and synthesis). Git history is their archive; do not expect their directories to exist.

- **The archived preamble** — the third attempt — was archived on 2026-08-30 at `archives/preamble/`.
- **The live preamble** is `src/dzack_research/preamble/`. `from dzack_research.preamble.all import *` is the session import. Its mathematics is [sage-extensions](https://github.com/dzackgarza/sage-extensions) (`sage_extensions`).

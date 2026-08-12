# Research

Workspace for mathematical notes, computation experiments, and live research project references.

## Sage research package

The installable `dzack_research` package is the preamble.
After checkout or after `.envrc` changes, run:

```bash
direnv allow
```

The exploratory spikes are archived reference material under `computations/archives/` — small sprints the preamble cannibalizes; they stay importable in a session for reference and are imported by nothing:

```sage
import sage_lattice_feature_spike as feature   # reference only

L.<v> = feature.base.Lattice([[2]], label="<2>")
v * v   # 2
```

`just test` runs the repository hygiene sweep and then delegates to the base-spike test gate.

## Repository Layout

- `computations/`: scratchpad code, notebooks, named computation threads, generated artifacts, and reusable components.

- `computations/scripts/components/`: code factored out of computations for reuse inside this repo.

- `computations/vendor/`: third-party code, cloned or dropped in; importable from every Sage process.
  See `AGENTS.md` for how each kind of code becomes importable.

- `notes/`: human mathematical notes, paper notes, findings, extraction plans, and computation notes.

- `projects/`: live research projects tracked as submodules once they deserve their own history.

- `references/`: PDFs, generated indexes, upstream references, and local dependency notes.

## Live Projects

- `projects/lattice-research`: submodule for the live Coble/lattice research project.

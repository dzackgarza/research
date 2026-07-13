# Research

Workspace for mathematical notes, computation experiments, and live research project references.

## Sage research package

The installable `dzack_research` package exposes the maintained lattice spikes as `lattice` and `feature`. After checkout or after `.envrc` changes, run:

```bash
direnv allow
```

Use the Sage-parity spike for lattice work:

```sage
from dzack_research import lattice

L.<v> = lattice.Lattice([[2]], label="<2>")
v * v   # 2  (quadratic form via *)
```

See `.agents/references/spike-style-guide.md` for the full style guide governing spike code, notebooks, and documentation.

Use the feature spike as the fork point for literature-gated work beyond Sage parity.
It imports the parity spike as `base`.

```sage
from dzack_research import feature

L.<v> = feature.base.Lattice([[2]], label="<2>")
v * v   # 2
```

Run the spike test gates from the repository root:

```bash
just -f computations/experiments/sage_lattice_category_spike/justfile test
just -f computations/experiments/sage_lattice_feature_spike/justfile test
```

`just test` runs the repository hygiene sweep and then delegates to the base-spike test gate.

## Repository Layout

- `computations/`: scratchpad code, notebooks, named computation threads, generated artifacts, and reusable components.
- `computations/components/`: code factored out of computations for reuse inside this repo.
- `notes/`: human mathematical notes, paper notes, findings, extraction plans, and computation notes.
- `projects/`: live research projects tracked as submodules once they deserve their own history.
- `references/`: PDFs, generated indexes, upstream references, and local dependency notes.

## Live Projects

- `projects/lattice-research`: submodule for the live Coble/lattice research project.

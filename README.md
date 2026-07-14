# Research

Workspace for mathematical notes, computation experiments, and live research project references.

## Lattice Spikes

The maintained Sage lattice-category experiments live under `computations/experiments`. The repo-local `.envrc` puts that experiment root on `PYTHONPATH`, so Sage scripts and notebooks opened from this repo can import the spikes directly.
After checkout or after `.envrc` changes, run:

```bash
direnv allow
```

Use the base spike for Sage-parity lattice work:

```sage
from sage_lattice_category_spike import *

L.<v> = Lattice([[2]], label="<2>")
v * v   # 2  (quadratic form via *)
```

See `.agents/references/spike-style-guide.md` for the full style guide governing spike code, notebooks, and documentation.

Use the feature spike only as the fork point for work beyond Sage parity.
It imports the base spike as `base`; no ungated feature engines are assumed to exist there.

```sage
from sage_lattice_feature_spike import *

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

- `computations/`: scratchpad code, notebooks, named computation threads, generated artifacts, and exploratory scripts.
- `computations/scripts/`: user-authored exploratory code (including former `components/`, `lattice-orbits/`, and `enriques-moduli/`); excluded from generic QC.
- `notes/`: human mathematical notes, paper notes, findings, extraction plans, and computation notes.
- `projects/`: live research projects tracked as submodules once they deserve their own history.
- `references/`: PDFs, generated indexes, upstream references, and local dependency notes.

## Live Projects

- `projects/lattice-research`: submodule for the live Coble/lattice research project.

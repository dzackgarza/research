# Research

Canonical workspace for research notes, computational scratch work, and live project
references.

This repository is the umbrella for active mathematical research work. The layout
follows the research pipeline, not a taxonomy of mathematical objects.

Raw scratch work can start messy. When a calculation becomes recognizable, give it a
named computation thread. When code from a thread becomes generally useful inside this
repo, promote it into a component. When a component becomes a project with its own
history, split it into `projects/` as a submodule.

## Layout

- `computations/`: scratchpad code, notebooks, named computation threads, generated artifacts, and reusable components.
- `computations/components/`: code factored out of computations for reuse inside this repo.
- `notes/`: human mathematical notes, paper notes, findings, extraction plans, and computation notes.
- `projects/`: live research projects tracked as submodules once they deserve their own history.
- `references/`: PDFs, generated indexes, upstream references, and local dependency notes.
- `archives/provenance/`: non-agent source-context files retained to explain where imported material came from.
- `.agents/`: agent-facing instructions, implementation references, operator guidance, and agent provenance.

## Live Projects

- `projects/lattice-research`: submodule for the live Coble/lattice research project.

## Lattice Spikes

The Sage lattice spikes live under `computations/experiments` and import as top-level
Python packages when Sage runs from that directory.

Use the base spike for Sage-parity lattice work:

```bash
cd computations/experiments
sage -python - <<'PY'
from sage.all import ZZ
import sage_lattice_category_spike.lattice_categories as lc

L = lc.Lattices(ZZ).from_gram_matrix([[2]], label="<2>")
v = L.gen(0)
print(v.b(v))
PY
```

Expected output:

```text
2
```

Use the feature spike only as the fork point for work beyond Sage parity. It imports
the base spike as `base`; no ungated feature engines are assumed to exist there.

```bash
cd computations/experiments
sage -python - <<'PY'
from sage.all import ZZ
import sage_lattice_feature_spike as feature

L = feature.base.Lattices(ZZ).from_gram_matrix([[2]], label="<2>")
print(L.gen(0).q())
PY
```

Expected output:

```text
2
```

Run the spike test gates from the repository root:

```bash
just -f computations/experiments/sage_lattice_category_spike/justfile test
just -f computations/experiments/sage_lattice_feature_spike/justfile test
```

`just test` runs the repository hygiene sweep and then delegates to the base-spike
test gate.

## Import Policy

Imported scratchpad material is preserved before cleanup. Do not rewrite mathematical
algorithms as part of organization-only work. Do not create empty directories as a plan
for future classification. Let actual files and actual workflows justify directories.

Use named computation threads for work that cuts across curves, surfaces, lattices,
periods, and implementation details. Mathematical research rarely belongs to one clean
object class.

Promote stable code into cleaner components with separate verification commits.

Do not commit machine-local dependency symlinks, transient index lock files,
`node_modules`, `__pycache__`, or credential-bearing notebooks.

Human mathematical material and agent/operator material have different homes. Paper
summaries, research findings, and mathematical discussions belong under `notes/`.
Instructions for running tools, navigating Sage internals, or avoiding agent workflow
mistakes belong under `.agents/`.

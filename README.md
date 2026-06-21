# Research

Canonical workspace for research notes, computational scratch work, and live project
references.

This repository is the umbrella. Live projects with their own development history stay
as submodules under `projects/`; reusable or archival computational material lives under
`computations/`; prose and mathematical notes live under `notes/`.

## Layout

- `computations/`: Sage, Singular, Python, notebook, diagram, and generated computational artifacts.
- `notes/`: mathematical notes, extraction plans, comparisons, and legacy research prose.
- `projects/`: live research projects tracked as submodules.
- `references/`: PDFs, generated indexes, upstream references, and local dependency notes.
- `archives/provenance/`: source-context files retained to explain where imported material came from.

## Live Projects

- `projects/lattice-research`: submodule for the live Coble/lattice research project.

## Import Policy

Imported scratchpad material is preserved before cleanup. Do not rewrite mathematical
algorithms as part of organization-only work. Promote stable code into cleaner component
packages with separate verification commits.

Do not commit machine-local dependency symlinks, transient index lock files,
`node_modules`, `__pycache__`, or credential-bearing notebooks.


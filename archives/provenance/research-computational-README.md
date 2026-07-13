# Research Computational

Scratchpad repository for computational research artifacts that are worth preserving: small reusable components, exploratory notebooks, extraction notes, generated indexes, and computational references.

This repository is not the live Coble research project.
Keep that project as its own repository, eventually referenced here as `projects/coble-research` when the remote and local Git boundary exist.

## Layout

- `components/`: reusable code or code close enough to reuse after cleanup.
- `experiments/`: runnable exploratory code organized by mathematical topic.
- `notebooks/`: notebook artifacts, including broken or format-mismatched notebooks.
- `notes/`: prose research notes, extraction plans, comparisons, and mathematical notes.
- `references/`: generated indexes, local dependency notes, and upstream-reference state.
- `projects/`: external live project references, preferably submodules rather than vendored copies.

## Import Policy

Preserve original computational content first.
Do not rewrite mathematical algorithms during organization.
If code later becomes a maintained package or production component, promote it with tests and a separate cleanup commit.

Generated indexes may be kept under `references/generated-indexes/` when they encode useful retrieval state, but they should not be confused with source code.

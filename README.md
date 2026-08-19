# Research

Workspace for mathematical notes, computation experiments, and live research project references.

## Sage research package

The installable `dzack_research` package is the preamble.
It is a **Sage** package, not a plain Python package: its modules are `.sage` sources that the [sageparse](https://github.com/dzackgarza/tree-sitter-sage) preparser compiles to Python on import.
`tree-sitter-sage` is therefore a hard runtime dependency, and the package must be imported inside a Sage environment (`SAGE_BIN`; `src/sitecustomize.py` installs the import hook into every process).
After checkout or after `.envrc` changes, run:

```bash
direnv allow
```

The exploratory spikes that preceded the preamble were fully absorbed into it and deleted (2026-08-19); git history is their record. The active code surface is the preamble, `src/dzack_research/preamble/`.

`just test` runs the repository hygiene sweep and the experiment test gates.

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

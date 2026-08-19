# Research Computational — subtree READMEs and repository rulings

The per-directory READMEs of the `research-computational` clone, kept verbatim beside
`research-computational-README.md`. They record the clone's own organizational rulings —
what each tree held, what was deliberately not imported, and the promotion criterion from
experiments to components. The bodies below are transcribed unchanged from the clone.

## `notes/README.md`

```markdown
# Notes

Research prose separated from runnable code.

- `extraction-specs/`: plans for extracting reusable tools from existing systems.
- `comparisons/`: comparisons between computational approaches or libraries.
- `topology/`: topology notes that are not yet tied to a runnable component.
```

## `notebooks/README.md`

```markdown
# Notebooks

Notebook artifacts grouped by topic and condition.

- `curves/`: curve and ideal scratchpads.
- `lattices/`: lattice-related notebook state.
- `periods/`: period-computation notebooks or notebook exports.
- `empty-or-broken/`: notebooks kept for provenance but not currently useful as runnable artifacts.

`periods/fermat-periods-nbviewer.html` was named `.ipynb` in the source directory but is
an HTML notebook-viewer export, not JSON notebook data.
```

That HTML export is in-tree at
`references/external-notebooks/fermat-quartic-periods-lefschetz-family.html`; it is the
`lefschetz_family` package's own worked example for the Fermat quartic surface, so it is
kept as an external reference and not absorbed.

## `experiments/README.md`

```markdown
# Experiments

Runnable exploratory code that is not yet reusable enough for `components/`.

Group experiments by mathematical topic. Promote stable code to `components/` only
after preserving the original algorithm and adding verification appropriate to the
mathematical claim.
```

## `references/README.md`

```markdown
# References

Reference state that supports the scratchpad but is not itself a reusable component.

- `generated-indexes/`: persisted local retrieval/index outputs.
- `local-system-dependencies/`: notes about machine-local dependency links that should
  not be committed as portable source.
```

## `references/local-system-dependencies/README.md`

```markdown
# Local System Dependencies

The source directory `~/research-code` contained `mylibs/libflint.so.22`, a symlink to
`/usr/lib/libflint.so.21`.

That symlink was not imported because it points at machine-local system state. Recreate
the dependency through the system package manager or a project environment instead of
tracking the symlink in Git.
```

The same ruling is in-tree at `references/local-system-dependencies/README.md`.

## `projects/README.md`

```markdown
# Projects

Live projects belong here as references, preferably Git submodules.

`coble-research` should be added here after the live project has a real Git boundary and
remote. Do not vendor the current `~/gitclones/research` tree into this repository.
```

## Declared submodules

`.gitmodules` declared two submodules, neither of which was ever checked out into the
clone's working tree:

- `polyhedral_common` — `https://github.com/dzackgarza/polyhedral_common`
- `sage-dzg-fork` — `git@github.com:dzackgarza/sage-fork-dzg.git`

## Structural checks the clone enforced

The clone's `justfile` ran four checks over the imported material, all of which the
in-tree copies still satisfy:

- the four JSON notebooks parse and carry a `cells` key;
- the Fermat periods artifact starts with `<!DOCTYPE html>`, i.e. it is the HTML export
  and not notebook JSON;
- no `*.lock` file from a generated retrieval index is tracked;
- the machine-local FLINT symlink `mylibs/libflint.so.22` was not imported.

# Sage Lattice Category Spike

The base parity spike for replacing Sage's scattered lattice surfaces with one owned category-shaped package.

This directory is the maintained base spike.
It stays focused on Sage parity, normalization, and literature-backed behavior that already has a known reference surface.
New mathematics with no Sage analogue belongs in the separate `sage_lattice_feature_spike` fork, behind the gap-ledger gate.

## Types: the lexicon is the single type surface

Every type noun in a signature comes from `lexicon/` (`from ..lexicon import Lattice, Matrix, Ring, ...`); Sage's untyped modules get real types from the sibling `typings/sage/` stub tree, which the project QC picks up automatically.
**Read `lexicon/INVENTORY.md` before touching any type**: it owns the catalogue, the representation policy (category-first; `Any` is never a representation), and the naming rules (mathematical nouns only — no Carrier/Host/Kernel mangles, no hand protocols at use sites, `Sage*` prefix only where Sage's object differs from ours).
Gate every type change with `just lexicon-check`. Known Sage typing traps are in the agent-memory vault (`projects/.../traps/sage-type-surface-traps-for-the-lexicon-stub-tree`).

## Boundaries

- `lattice_categories.py` is the public facade used by tests and downstream spikes.
- `lexicon/` + `typings/` are the centralized type surface (see above).
- `algebra/` is pure language shape: typed carriers, value modules, and scalar helpers.
- `objects/` owns Sage category classes, lattice parents, elements, and constructors.
- `forms/` owns discriminant groups/forms and genus data.
- `morphisms/` owns Hom/End/O(L) objects and group actions.
- `tests/` is organized by proof obligation: owned behavior, literature fixtures, Sage reference contracts, and slow CI-only fixtures.

Keep new code in the narrowest owning package.
Do not add cross-package helpers until two real call sites force a shared abstraction.

## Verification

Run this spike through `just -f computations/experiments/sage_lattice_category_spike/justfile test`. The repository root `just test` delegates to the same recipe after the umbrella hygiene sweep.

# Lattice Redesign Rules

## Primary Artifacts

- The complete execution plan is `theory/lattice_interface_redesign_plan.md`.
- The primary durable correction artifact is `theory/lattice_redesign_corrections_spec.md`.
- The exact backup to read alongside the correction artifact is `.agents/theory/spec-backups/lattices_written_spec_backup.py`.
- The canonical written semantic source remains `src/lattices/lattices.py`.

Future redesign work must read the correction artifact and the backup before changing the public lattice and module hierarchy.

## Replacement Policy

- Do not preserve stale public layers with compatibility shims, facade modules, or parallel split implementations during the redesign.
- Replace the public layer directly in `src/lattices/lattices.py`.
- Move direct consumers to the new surface instead of routing through `coble_geometry_foundation`, `src/lattices/core.py`, or `src/lattices/groups.py`.
- Keep exact backups of user-written spec and review text under `.agents/theory/spec-backups/` before rewriting.

## Dependency Order

Treat `tests/sage_spec/misc.sage` as an upstream contract, not a downstream cleanup item. The required order is:

1. Foundational ring, module, and field semantics.
2. Category-correct general bilinear modules over PID or Dedekind-style bases.
3. Lattice, rational, dual, and discriminant specializations.
4. Orthogonal, root, Weyl, Coxeter, Eichler, and group surfaces.
5. General indefinite isometry backend completion.

Preserve and migrate the current FGP, pydantic, and Sage-wrapper machinery where it is sound. Do not restart from scratch.

## Sage Integration Contract

- Before running lattice tests, verify `src/lattices/lattices.py` exports the public nouns expected by `src/lattices/__init__.py` and the spec tests.
- Use Sage `Parent` plus category, real `Element` or `ElementWrapper` element types, `_Hom_` for custom homset construction, and `_element_constructor_` for parent-side conversion.
- Do not override parent `__call__` to fake this contract.

## Verification Targets

- `python -c "import src.lattices"` should succeed.
- New spec tests should target `src.lattices.lattices` directly.
- The redesign plan should stay grouped by semantic boundaries from the written spec: hierarchy, promotion, dual and discriminant semantics, morphisms, subobjects, and groups or backends.
- Public lattice code should not rely on raw Sage-object admission or Sage-private discriminant internals on its external contract.

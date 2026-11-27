# Lattices Triage

The lattice subtree is admitted as a top-level category subtree. It has `AGENTS.md`,
`__init__.py`, `homsets.py`, Sage inventory and mapping docs, construction
subcategories, and smoke files. Generic formed-module classes now live in `forms/`;
the old generic files under `lattices/subcategories/` are compatibility imports.

## Current Smoke Frontier

`lattices/chain_smoketest.sage` and `lattices/smoketest.sage` cover Cat registration,
the ambient module chain, Hom/End/Aut construction, Subobjects construction,
`DualObjects()` construction vocabulary with the `DualLattices()` compatibility alias,
and the `Even()` predicate surface. Constructor admission remains outside the current
smoke surface: `lattices/AGENTS.md` requires concrete constructors to enter through
`Lattices(R).Constructors()` after Sage constructor inventory mapping.

## Orthogonal-Group Frontier

`LatticeOrthogonalGroup` is the lattice-category specialization of the general
formed-module aut surface: `Lattices(R).AutCategory().Of(L)`. This is the right owner
for integral lattice isometries; matrix-group realization, determinant-one subgroups,
finite-generation data, and finite-presentation data are later refinements.

The discriminant-form specialization is mathematically the same aut surface applied to
the finite torsion module with its discriminant form. A precise exported
`DiscriminantGroupAut` type package is still blocked because
`lattices/subcategories/constructions/discriminant_groups.py` does not yet define Hom,
End, and Aut standard names, and that file is outside this task's write scope.

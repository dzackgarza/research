# Lattices Subtree

This subtree specifies module lattices: finite-rank modules equipped with bilinear
forms and their lattice-theoretic refinements.  It is unrelated to order-theoretic
lattices in `posets/`.

Rules:

- Keep generic form evaluation in `modules/`; lattice files only refine the
  lattice-theoretic vocabulary.
- Preserve mathematical nouns in public names: `Lattice`, `LatticeMorphism`,
  `LatticeHomCategory`, `DiscriminantGroup`, `Overlattice`, and `DualLattice`.
- Every subcategory file must expose explicit `ParentMethods`, `ElementMethods`,
  and `MorphismMethods` classes, even when the current body is only `...`.
- Hom, end, and aut refinements live in `homsets.py` and use `HomCategory`,
  `EndCategory`, and `AutCategory` vocabulary, not homset/endset/autset names.
- Construction categories live under `subcategories/constructions/`.
- Concrete constructors are admitted only through `Lattices(R).Constructors()`
  after the Sage constructor inventory has been mapped.

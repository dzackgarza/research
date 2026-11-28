# Dependencies

## Prerequisite Tasks

- T-0001 (canonical lattice constructors)
- T-0002 (invariant and predicate primitives for 2-elementary lattices)
- T-1001 (standard lattice fixtures: U, A1, E8, Lambda_K3)
- T-1002 (literature-backed invariant ledger for Coble lattices: S_Co, T_Co invariants)
- T-1003 (finite quadratic-form fixtures: discriminant forms)
- T-2001 (gate: lattice constructors)
- T-2002 (gate: discriminant-form invariants)
- T-2009 (gate: reduction ledger)

## Local Sources

- GOAL.md (lines 15-18, 26 for invariants)
- REFERENCES.md (Nikulin 1979, Sterk 1991)
- theory/mathematical_background.md
- theory/literature_claim_map.md
- T-1001 fixture data (standard lattice Gram matrices)
- T-1002 fixture data (S_Co, T_Co expected invariants)
- T-1003 fixture data (finite quadratic form representatives)

## Required Tools / Backends

- T-0001.1: Lattice constructor for S_Co with signature (1,10), determinant 1
- T-0001.2: Lattice constructor for T_Co with signature (2,9), determinant 1
- T-0002.1: (r,a,δ) invariant computation
- T-0002.2: Discriminant form computation
- T-0002.3: Genus cardinality verification
- T-0003.1: Orthogonal complement computation

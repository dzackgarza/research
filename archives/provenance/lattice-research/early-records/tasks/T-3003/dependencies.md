# Dependencies

## Prerequisite Tasks

- T-0003 (composable embedding primitives)
- T-1002 (literature-backed invariant ledger for Coble lattices)
- T-1004 (primitive-embedding fixtures)
- T-2003 (gate: embedding primitives)
- T-2009 (gate: reduction ledger)

## Local Sources

- GOAL.md (lines 19, 22, 27 for Λ_K3 embedding requirement)
- REFERENCES.md (Nikulin 1979, lattice embedding theory)
- theory/oscar_lattices.md
- theory/mathematical_background.md
- T-1002 fixture data (T_Co invariants)
- T-1004 fixture data (embedding test cases)
- T-3002 verification (T_Co Gram matrix)

## Required Tools / Backends

- T-0003.1: create_embedding(T_Co, Λ_K3) - primitive embedding constructor
- T-0003.2: compose_embeddings - compose multiple embeddings
- T-0003.3: extract_image - extract sublattice image
- T-0003.4: orthogonal_complement - compute complement in ambient lattice
- T-0003.5: is_primitive(embedding) - verify primitivity
- T-0002.3: is_isometric(lattice1, lattice2) - verify complement isometry to S_Co

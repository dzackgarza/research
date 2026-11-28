# Dependencies

## Prerequisite Tasks

- T-0003 (composable embedding primitives)
- T-0008 (involution and polarization primitives)
- T-1001 (standard lattice fixtures: Λ_K3)
- T-1002 (literature-backed invariant ledger for Coble lattices)
- T-1004 (primitive-embedding fixtures)
- T-2003 (gate: embedding primitives)
- T-2008 (gate: involution primitives)
- T-2009 (gate: reduction ledger)
- T-3002 (lattice invariant verification for S_Co, T_Co)
- T-3003 (primitive embedding T_Co → Λ_K3)

## Local Sources

- GOAL.md (lines 79, 82, 85 for involution construction)
- REFERENCES.md (Nikulin 1979, lattice involution theory)
- theory/oscar_lattices.md
- theory/mathematical_background.md
- T-1001 fixture data (Λ_K3 standard basis)
- T-1002 fixture data (S_Co, T_Co invariants)
- T-3002 verification (S_Co, T_Co invariants)
- T-3003 verification (T_Co → Λ_K3 embedding)

## Required Tools / Backends

- T-0008.1: sign_involution(Λ_K3) - construct involution with specified eigenspaces
- T-0008.2: extract_invariant_sublattice - compute +1 eigenspace
- T-0008.3: extract_coinvariant_sublattice - compute -1 eigenspace
- T-0008.4: verify_discriminant_action - verify action on discriminant group
- T-0008.5: transport_distinguished_vector - transport h_Co to h_En
- T-0002.1: (r,a,δ) invariant computation for eigenspace verification
- T-0002.3: is_isometric for eigenspace-to-lattice comparison
- T-0003.4: orthogonal_complement for eigenspace extraction

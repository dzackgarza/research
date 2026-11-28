# Reduction Ledger: T-3003

This file documents how each exact computation in T-3003 strengthens a GOAL.md claim.

## GOAL.md Linkage

- **GOAL.md Item**: Task 1.3: "Derive the explicit primitive embedding matrices for T_Co
  ↦ T_En ↦ T_dP ↦ Λ_K3."
- **GOAL.md Section**: 1. Foundation: Coble Curves and Picard Lattices

## Necessity Statement

Exact computation is required because:
- The embedding matrix must have exact integer entries to preserve the integral lattice
  structure.
- Primitivity verification requires checking that the cokernel is torsion-free - a
  property that either holds or does not.
- Gram matrix preservation M^T * G_Λ_K3 * M = G_T_Co is an exact equality of integer
  matrices.
- The complement lattice isometry T_Co^⊥ ≅ S_Co must be verified exactly, not
  approximately.

## Computed Values

1. **Embedding matrix M**: 11×22 integer matrix representing the primitive embedding
   T_Co → Λ_K3.
2. **Primitivity certificate**: Verification that cokernel Λ_K3/T_Co is torsion-free.
3. **Gram matrix verification**: Proof that M^T * G_Λ_K3 * M = G_T_Co.
4. **Complement lattice**: Explicit description of T_Co^⊥ as a sublattice of Λ_K3.
5. **Complement isometry**: Verification that T_Co^⊥ ≅ S_Co (signature (1,10),
   discriminant 1).
6. **Coordinate basis**: Explicit coordinates for T_Co vectors in the Λ_K3 standard
   basis.

## Strengthening Claim

The primitive embedding of T_Co into Λ_K3 is a critical structural result that enables:
- Verification that T_Co and S_Co are orthogonal complements in Λ_K3 (confirming
  T-3002).
- Construction of the involution on Λ_K3 with eigensublattices T_Co and S_Co (T-3011).
- Establishment of the lattice-theoretic foundation for the Coble moduli space.

Without explicit embedding matrices and primitivity verification, the orthogonal
decomposition Λ_K3 = T_Co ⊕ S_Co remains a theoretical statement without computational
confirmation.

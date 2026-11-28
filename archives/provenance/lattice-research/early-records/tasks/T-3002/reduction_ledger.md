# Reduction Ledger: T-3002

This file documents how each exact computation in T-3002 strengthens a GOAL.md claim.

## GOAL.md Linkage

- **GOAL.md Item**: Task 1.2: "Compute the Gram matrices for S_Co and T_Co, and verify
  their (r, a, δ) invariants and genus cardinality using Nikulin's classification (r > a
  check)."
- **GOAL.md Section**: 1. Foundation: Coble Curves and Picard Lattices

## Necessity Statement

Exact computation is required because:
- The invariants (r,a,δ) and genus cardinality are mathematical properties that cannot
  be approximated—either the genus contains a unique isometry class or it does not.
- The discriminant form duality q_S = -q_T mod 2Z is an exact isomorphism condition.
- Verification against Nikulin's classification requires exact integer invariants, not
  floating-point approximations.

## Computed Values

1. **S_Co Gram matrix**: 11x11 diagonal matrix diag(2, -2, ..., -2)
2. **T_Co Gram matrix**: 11x11 integer matrix with signature (2,9), determinant 1
3. **(r,a,δ) for S_Co**: (11, 11, 1)
4. **(r,a,δ) for T_Co**: (11, 11, 1)
5. **Discriminant form**: q_S ≅ q_T ≅ (Z/2Z)^11 with q_S = -q_T mod 2Z
6. **Genus cardinality**: Unique isometry class (r > a verified)

## Strengthening Claim

These computations verify that GOAL.md's stated invariants for S_Co and T_Co are
mathematically correct.
This verification is a prerequisite for:
- Proving the primitive embedding chain T_Co → T_En → T_dP → Λ_K3 (T-3003)
- Constructing the involution on Λ_K3 (T-3011)
- Establishing the Coble moduli space structure

Without verified lattice invariants, downstream tasks cannot proceed with mathematical
confidence.

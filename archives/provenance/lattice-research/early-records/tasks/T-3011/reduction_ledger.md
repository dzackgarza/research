# Reduction Ledger: T-3011

This file documents how each exact computation in T-3011 strengthens a GOAL.md claim.

## GOAL.md Linkage

- **GOAL.md Item**: Task 5.1: "Construct the 22×22 matrix θ and compute the signature
  and invariants of its fixed sublattice to confirm isometry (2-elementary check)."
- **GOAL.md Section**: 5. Explicit Involution Matrix and Sublattice Invariants

## Necessity Statement

Exact computation is required because:
- The involution matrix θ must have exact integer entries to be an isometry of Λ_K3.
- Eigenspace isometry verification requires exact (r,a,δ) computation, not numerical
  approximation.
- The discriminant group action is a finite quadratic form property that must be
  verified exactly.
- Distinguished vector transport must preserve exact lattice coordinates.

## Computed Values

1. **Involution matrix θ**: 22×22 integer matrix with θ^2 = I and θ^T * G_Λ_K3 * θ =
   G_Λ_K3.
2. **+1 eigenspace Λ_K3^θ**: Sublattice with signature (2,9), (r,a,δ) = (11,11,1),
   isometric to T_Co.
3. **-1 eigenspace Λ_K3^-θ**: Sublattice with signature (1,10), (r,a,δ) = (11,11,1),
   isometric to S_Co.
4. **Discriminant action**: Verification that θ acts as sign change on the 22-element
   discriminant group.
5. **Distinguished vector transport**: Certificate that h_Co maps to h_En under the
   involution.

## Strengthening Claim

The involution θ is the "horizontal folding" that identifies the Coble and Enriques
sectors of the moduli space.
This construction is essential for:
- Identifying the coinvariant sublattice as S_Co (the Coble polarization).
- Identifying the invariant sublattice as T_Co (the transcendental lattice).
- Establishing the relationship between Coble and Enriques polarizations (h_Co ↔ h_En).
- Providing the foundation for monodromy invariant computation (Task 6.1).

Without an explicit θ matrix and eigenspace verification, the structural relationship
between Λ_K3, S_Co, and T_Co remains theoretical.

# Implementation Plan

## Mathematical Claim

Construct an explicit involution θ on Λ_K3 such that:
- θ is an order-2 isometry
- Λ_K3^θ (fixed sublattice, +1 eigenspace) ≅ T_Co
- Λ_K3^-θ (-1 eigenspace) ≅ S_Co

## Subtasks

1. **Load Λ_K3 lattice**: Use T-0001 constructor from T-1001 fixture (standard K3
   lattice U^3 ⊕ E_8^2).

2. **Construct involution**: Use T-0008.1 sign_involution to create θ with specified
   eigenspace signatures.

3. **Verify isometry**: Verify θ^T * G_Λ_K3 * θ = G_Λ_K3.

4. **Extract +1 eigenspace**: Use T-0008.2 to compute Λ_K3^θ (kernel of θ - I).

5. **Extract -1 eigenspace**: Use T-0008.3 to compute Λ_K3^-θ (kernel of θ + I).

6. **Verify +1 eigenspace isometry**: Use T-0002.1 to compute (r,a,δ) and T-0002.3
   is_isometric to verify Λ_K3^θ ≅ T_Co.

7. **Verify -1 eigenspace isometry**: Use T-0002.1 to compute (r,a,δ) and T-0002.3
   is_isometric to verify Λ_K3^-θ ≅ S_Co.

8. **Verify discriminant action**: Use T-0008.4 to verify action on A_Λ_K3.

9. **Transport distinguished vector**: Use T-0008.5 to verify h_Co maps to h_En.

## Exit Criteria

All 9 subtasks must pass with verification reports.
If any check fails, task fails.

## Validation

- Each subtask produces a verification report (pass/fail with evidence).
- Final report aggregates all subtask results.
- Reduction ledger must be created documenting each computation's GOAL.md rationale.

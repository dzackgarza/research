# Implementation Plan

## Mathematical Claim

Verify the exact invariants of S_Co and T_Co match GOAL.md specifications:
- S_Co: signature (1,10), determinant 1, (r,a,δ) = (11,11,1)
- T_Co: signature (2,9), determinant 1, (r,a,δ) = (11,11,1)
- Discriminant form: q_S ≅ q_T ≅ (Z/2Z)^11 with q_S = -q_T mod 2Z

## Subtasks

1. **Construct S_Co lattice**: Use T-0001 constructors to build S_Co with signature
   (1,10), verify Gram matrix diag(2, -2^10).

2. **Construct T_Co lattice**: Use T-0001 constructors to build T_Co with signature
   (2,9), verify properties from T-1002 fixtures.

3. **Compute (r,a,δ) for S_Co**: Apply T-0002 invariant computation, verify result
   (11,11,1).

4. **Compute (r,a,δ) for T_Co**: Apply T-0002 invariant computation, verify result
   (11,11,1).

5. **Verify discriminant form duality**: Use T-0002 discriminant form primitives to
   verify q_S ≅ q_T ≅ (Z/2Z)^11.

6. **Verify genus cardinality**: Use T-0002 genus verification to confirm unique
   isometry class (r > a).

7. **Verify complement embedding**: Use T-0003 primitives to verify S_Co = T_Co^⊥ in
   Λ_K3.

## Exit Criteria

All 7 subtasks must pass with verification reports.
If any check fails, task fails.

## Validation

- Each subtask produces a verification report (pass/fail with evidence).
- Final report aggregates all subtask results.
- Reduction ledger must be created documenting each computation's GOAL.md rationale.

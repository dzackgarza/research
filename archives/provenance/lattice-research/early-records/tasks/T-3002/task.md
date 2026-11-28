# Task T-3002: Verify Lattice Invariants Of S_Co And T_Co

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - Line 15: "Coble Lattice: S_Co ≅ ⟨2⟩ ⊕ ⟨-2⟩^10 ≅ (11, 11, 1)_1. Signature (1, 10)."
  - Line 16: "Gram Matrix: Q_S_Co = diag(2, -2, ..., -2)."
  - Line 17: "Transcendental Lattice: T_Co = S_Co^⊥_Λ_K3 ≅ (11, 11, 1)_2. Signature (2,
    9)."
  - Line 18: "Invariants: Both satisfy q_S ≅ q_T ≅ (Z/2Z)^11 with q_S = -q_T (mod 2Z)."
  - Line 26: "Task 1.2: Compute the Gram matrices for S_Co and T_Co, and verify their
    (r, a, δ) invariants and genus cardinality using Nikulin's classification (r > a
    check)."
- GOAL linkage: GOAL.md Task 1.2

## Objective

Verify the exact invariants of S_Co and T_Co, their discriminant-form duality, and the
genus or cardinality uniqueness claims stated in GOAL.md.

## Parent Sufficiency Map

Discharges the lattice-invariant burden of G1.2; broader moduli claims remain external
literature.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0001, T-0002, T-1001, T-1002, T-1003, T-2001, T-2002, T-2009
- Local sources:
- GOAL.md
- REFERENCES.md
- theory/mathematical_background.md
- theory/literature_claim_map.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are
  binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- May apply existing tools, but may not invent missing algorithms.
- Must not broaden the mathematical claim beyond the parent sufficiency map.
- Must be ready to downgrade to REPLAN_REQUIRED or conjectural status if prerequisites
  fail.

## Acceptance Criteria (TASK_SPECIFICATION)

For T-3002 to PASS, the following must be verified:

1. **S_Co Gram Matrix**: Compute and verify Gram matrix for S_Co is diagonal(2, -2, ...,
   -2) with 1 positive and 10 negative eigenvalues (signature (1,10)).

2. **T_Co Gram Matrix**: Compute and verify Gram matrix for T_Co has signature (2,9) and
   determinant 1.

3. **(r,a,δ) Invariants**: Compute (r,a,δ) for both S_Co and T_Co using Nikulin's
   classification; verify both are (11,11,1).

4. **Discriminant Form Duality**: Verify q_S ≅ q_T ≅ (Z/2Z)^11 as finite quadratic
   forms, with q_S = -q_T mod 2Z.

5. **Genus Cardinality**: Verify the genus of S_Co and T_Co contains a unique isometry
   class (r > a condition per Nikulin).

6. **Complement Embedding**: Verify S_Co embeds as the orthogonal complement of T_Co in
   Λ_K3.

## Non-Goals

- T-3002 does NOT compute the full genus decomposition beyond cardinality uniqueness.
- T-3002 does NOT verify moduli space dimension (this is GOAL.md literature).
- T-3002 does NOT construct explicit equations for Coble surfaces (T-3001 handles this).
- T-3002 does NOT verify isotropic orbit counts (T-3005 handles this).
- T-3002 does NOT verify the primitive embedding chain T_Co → T_En → T_dP → Λ_K3 (T-3003
  handles this).

## Failure Conditions

- If any T-2 gate (T-2001, T-2002, T-2009) fails, T-3002 cannot proceed to IMPLEMENT.
- If computed Gram matrices differ from expected by more than machine precision, FAIL.
- If (r,a,δ) invariants do not compute to (11,11,1) for both lattices, FAIL.
- If discriminant form isomorphism check fails, FAIL.
- If genus cardinality check shows more than one isometry class, FAIL.

## Required Conventions

- Lattice bases must follow the canonical ordering from T-0001 constructors.
- (r,a,δ) computation must use Nikulin's definition (r = rank, a = length of
  discriminant form, δ ∈ {0,1}).
- Gram matrices must be returned as integer matrices with exact arithmetic.
- Discriminant form equality must be checked using the quadratic form classification
  from T-0002.

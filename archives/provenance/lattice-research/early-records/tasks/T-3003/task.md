# Task T-3003: Direct Primitive Embedding T_Co Into Lambda_K3

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - Line 19: "Ambient Lattices: T_En ≅ (12, 10, 0)_2, T_dP ≅ (20, 2, 0)_2, and Λ_K3 ≅
    (22, 0, 0)_1."
  - Line 22: "primitivity of the lattice embeddings lack rigorous derivation in terms of
    coordinate bases."
  - Line 27: "Task 1.3: Derive the explicit primitive embedding matrices for T_Co ↦ T_En
    ↦ T_dP ↦ Λ_K3."
- GOAL linkage: GOAL.md Task 1.3 (direct embedding portion)

## Objective

Construct an explicit primitive embedding T_Co -> Lambda_K3 with matrix data, complement
certificate, and exact provenance.

## Parent Sufficiency Map

Discharges only the direct Lambda_K3 portion of G1.3; the intermediate factorization
remains separate.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0003, T-1002, T-1004, T-2003, T-2009
- Local sources:
- GOAL.md
- REFERENCES.md
- theory/oscar_lattices.md
- theory/mathematical_background.md

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

For T-3003 to PASS, the following must be verified:

1. **T_Co → Λ_K3 embedding matrix**: Compute explicit 11×22 integer matrix representing
   the primitive embedding of T_Co into Λ_K3.

2. **Embedding primitivity**: Verify the embedding is primitive (cokernel T_Co^⊥/T_Co is
   torsion-free).

3. **Gram matrix preservation**: Verify the embedding preserves the bilinear form: M^T *
   G_Λ_K3 * M = G_T_Co.

4. **Complement lattice**: Compute T_Co^⊥ in Λ_K3 and verify it is isometric to S_Co.

5. **Orthogonal decomposition**: Verify Λ_K3 = T_Co ⊕ S_Co (direct sum as sublattice).

6. **Explicit coordinate basis**: Provide explicit coordinates for T_Co vectors in the
   Λ_K3 basis.

## Non-Goals

- T-3003 does NOT compute the intermediate embeddings T_Co → T_En or T_En → T_dP (these
  are separate tasks in goal_expansion.md).
- T-3003 does NOT verify the T_En or T_dP embeddings separately.
- T-3003 does NOT compute the full automorphism group of Λ_K3.
- T-3003 does NOT verify lattice invariants of S_Co or T_Co (T-3002 handles this).
- T-3003 does NOT construct the involution on Λ_K3 (T-3011 handles this).

## Failure Conditions

- If T-2003 (embedding primitives gate) fails, T-3003 cannot proceed to IMPLEMENT.
- If the embedding matrix entries are not integers, FAIL.
- If the embedding is not primitive (cokernel has torsion), FAIL.
- If Gram matrix preservation fails, FAIL.
- If complement lattice is not isometric to S_Co, FAIL.

## Required Conventions

- Embedding matrix must be expressed in the canonical Λ_K3 basis from T-1001.
- T_Co lattice must use the basis from T-3002 verification.
- Primitivity check must use the definition from T-0003 (cokernel torsion-free).

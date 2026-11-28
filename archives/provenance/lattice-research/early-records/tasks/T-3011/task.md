# Task T-3011: Construct Involution Theta On Lambda_K3

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - Line 79: "The horizontal folding θ must act on Λ_K3 such that its invariant and
    coinvariant sublattices are correctly identified: Λ_K3^θ ≅ T_Co and Λ_K3^-θ ≅ S_Co."
  - Line 82: "The explicit matrix for θ on the standard basis of U^3 ⊕ E8^2 is missing.
    One must verify the isometry classes of the ±1 eigenspaces via (r, a, δ)
    comparison."
  - Line 85: "Task 5.1: Construct the 22×22 matrix θ and compute the signature and
    invariants of its fixed sublattice to confirm isometry (2-elementary check)."
- GOAL linkage: GOAL.md Task 5.1

## Objective

Construct an explicit involution theta on Lambda_K3 and verify that its +1 and -1
eigensublattices match T_Co and S_Co with the required primitivity data.

## Parent Sufficiency Map

Discharges G5.1 if the lattice and embedding certificates all pass.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0003, T-0008, T-1001, T-1002, T-1004, T-2003, T-2008, T-2009
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

For T-3011 to PASS, the following must be verified:

1. **Involution matrix**: Construct 22×22 matrix θ representing an involution (order 2)
   on Λ_K3.

2. **Isometry verification**: Verify θ is an isometry: θ^T * G_Λ_K3 * θ = G_Λ_K3.

3. **+1 eigenspace**: Compute the +1 eigenspace Λ_K3^θ and verify it is isometric to
   T_Co (signature (2,9), (r,a,δ) = (11,11,1)).

4. **-1 eigenspace**: Compute the -1 eigenspace Λ_K3^-θ and verify it is isometric to
   S_Co (signature (1,10), (r,a,δ) = (11,11,1)).

5. **Discriminant action**: Verify the action of θ on the discriminant group A_Λ_K3
   matches the expected involution (sign change on the 22-torsion).

6. **Distinguished vector transport**: Verify the distinguished polarization vector h_Co
   in T_Co maps under transport to the Enriques polarization h_En in T_En.

## Non-Goals

- T-3011 does NOT construct the full automorphism group of Λ_K3 (just the single
  involution θ).
- T-3011 does NOT verify the intermediate embeddings T_Co → T_En or T_En → T_dP.
- T-3011 does NOT compute monodromy invariants (this is Task 6.1 in goal_expansion.md).
- T-3011 does NOT verify lattice invariants of S_Co or T_Co (T-3002 handles this).
- T-3011 does NOT construct the explicit sextic (T-3001 handles this).

## Failure Conditions

- If T-2008 (involution primitives gate) fails, T-3011 cannot proceed to IMPLEMENT.
- If θ is not order 2 (θ^2 ≠ I), FAIL.
- If θ is not an isometry, FAIL.
- If Λ_K3^θ is not isometric to T_Co, FAIL.
- If Λ_K3^-θ is not isometric to S_Co, FAIL.
- If the discriminant group action is incorrect, FAIL.

## Required Conventions

- θ must be expressed in the standard Λ_K3 basis (U^3 ⊕ E_8^2) from T-1001.
- Eigenspaces must be computed as the kernels of (θ - I) and (θ + I).
- Invariant comparison must use (r,a,δ) from T-0002 primitives.

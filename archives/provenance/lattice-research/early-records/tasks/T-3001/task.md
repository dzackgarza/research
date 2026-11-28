# Task T-3001: Explicit 10-Nodal Sextic And K3 Cover

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - Line 8: "A Coble surface S is obtained via the blowup π: S → P^2 at the 10 A_1 nodes
    of an irreducible rational plane sextic C = {F(x,y,z) = 0}."
  - Line 9: "The polynomial F is a homogeneous sextic of the form: F(x,y,z) = Σ a_ijk
    x^i y^j z^k satisfying the nodal conditions F(p_m) = ∂F/∂x(p_m) = ∂F/∂y(p_m) =
    ∂F/∂z(p_m) = 0 for 10 special point positions p_1, ..., p_10 ∈ P^2."
  - Line 10: "The moduli space of such sextics is 9-dimensional."
  - Line 12: "The K3 cover X → S is the double cover of P^2 branched along C, with
    equation w^2 = F(x,y,z) in the weighted projective space P(1,1,1,3)."
  - Line 25: "Task 1.1: Derive an explicit equation F(x,y,z)=0 for a rational sextic
    with 10 nodes and the corresponding K3 surface w^2 = F(x,y,z)."
- GOAL linkage: GOAL.md Task 1.1

## Objective

Fix a literature-backed special 10-point configuration and derive one exact rational
sextic F(x,y,z)=0 with ten nodes together with the K3-cover equation w^2 = F.

## Parent Sufficiency Map

Discharges the explicit-example burden of G1.1 only; it does not prove uniqueness or
classify all such sextics.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0007, T-1007, T-2006
- Local sources:
- GOAL.md
- REFERENCES.md
- theory/literature_claim_map.md
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

For T-3001 to PASS, the following must be verified:

1. **Point Configuration**: Fix a specific 10-point configuration from literature
   (Steiner sextic or Halphen pencil derived).

2. **Sextic Equation**: Derive explicit homogeneous polynomial F(x,y,z) of degree 6 that
   vanishes to order 2 at all 10 points (nodes/A_1 singularities).

3. **Nodal Verification**: Verify that the sextic has exactly 10 nodes (A_1
   singularities) and no other singularities.

4. **K3 Cover Equation**: Derive the double cover equation w^2 = F(x,y,z) in P(1,1,1,3).

5. **K3 Singularity Profile**: Verify the K3 surface has exactly 10 A_1 singularities
   above the nodal points of the sextic.

6. **Rationality Check**: Verify the base surface is rational (or confirm birationality
   to P^2).

## Non-Goals

- T-3001 does NOT prove uniqueness of the sextic (all such sextics).
- T-3001 does NOT classify all possible 10-nodal sextics.
- T-3001 does NOT compute the full moduli space (this is GOAL.md literature).
- T-3001 does NOT verify lattice invariants of S_Co or T_Co (T-3002 handles this).
- T-3001 does NOT construct primitive embeddings (T-3003 handles this).

## Failure Conditions

- If T-2006 (sextic primitives gate) fails, T-3001 cannot proceed to IMPLEMENT.
- If the derived sextic has fewer than 10 nodes, FAIL.
- If the derived sextic has singularities other than A_1 nodes, FAIL.
- If the K3 cover has singularities not of type A_1 above nodes, FAIL.
- If the nodal positions do not match the fixed point configuration, FAIL.

## Required Conventions

- Point coordinates must be from the canonical fixture in T-1007.
- Sextic coefficients must be exact rational numbers.
- Singularities must be classified using the terminology from T-0007 primitives.
- K3 cover must be expressed in weighted projective space P(1,1,1,3).

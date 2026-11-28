# Task T-2002: Gate Discriminant-Form And Invariant Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source:
  [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL.md origin (exact lines):
  - GOAL.md line 34: "For 2-elementary lattices with $r > a$, the genus contains a
    **unique isometry class**, and $O(T) \to O(q_T)$ is surjective (Nikulin 1.5.2)."
  - GOAL.md line 37: "One must formally verify the **lifting of isotropic orbits** from
    $A_T$ to $T_{\mathrm{Co}}$ using Sterk's lifting theorems."
  - GOAL.md Task 2.1: "Enumerate isotropic vectors in $A_{T_{\mathrm{Co}}}$ and compute
    their orbits under $O(q_T)$."
  - GOAL.md Task 2.2: "Lift these orbits to $T_{\mathrm{Co}}$ and verify that exactly
    one $O^*(T)$-orbit exists for divisibility 2."
- GOAL linkage: Gate for T-3002 (corrected from stale T-3005/T-3006 references)

## Objective

Gate the discriminant-form and invariant primitives by replaying them on T-1002 and
T-1003, then matching Brown invariants, divisibilities, and isotropic counts exactly.
This gate verifies:

1. **Discriminant form computation**: The discriminant form $q_L: A_L \to
   \mathbb{Q}/2\mathbb{Z}$ computed by T-0002 must match the fixture data from T-1003
2. **Brown invariant verification**: The Brown invariant $\beta(L)$ computed by T-0002
   must match the expected value from T-1002 fixtures
3. **Isotropic count verification**: The number of isotropic vectors in the discriminant
   group must match the fixture value from T-1003
4. **Divisibility mapping**: The divisibility map $v/d + T$ for primitive isotropic
   vectors must produce the expected set of discriminant group elements

## Parent Sufficiency Map

Blocks downstream discriminant-group and lifting results until the finite quadratic data
is exact.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0002, T-1002, T-1003
- Local sources:
- tasks/goal_expansion.md
- STATE_MACHINE.md
- PROOF_AUDITING.md

## Acceptance Criteria

1. **Discriminant form equality**: The quadratic form $q_L$ computed by T-0002 must
   equal the fixture's $q_L$ on all elements of $A_L$
2. **Brown invariant match**: Computed $\beta(L)$ must match expected value from T-1002
   fixtures (for S_Co: $\beta = 0 \pmod 8$; for T_Co: $\beta = 0 \pmod 8$)
3. **Isotropic count match**: Number of isotropic elements (those with $q(x) = 0$) must
   equal $2^{r-a}$ for 2-elementary lattices per Nikulin
4. **Divisibility orbit count**: Number of distinct $v/d + T$ images must match expected
   count from T-1003 fixture
5. **2-elementary invariants**: The $(r,a,\delta)$ computed by T-0002 must match fixture
   values exactly
6. **Genus uniqueness verification**: For $r > a$, must verify genus contains exactly
   one isometry class (per Nikulin 1.5.2)

## Non-Goals

1. **No new discriminant form computation**: This is a gate, uses T-0002 as black box
2. **No proof of Nikulin's theorem**: Assumes theory is correct; gate only verifies
   consistency with fixtures
3. **No O(T) group computation**: Gate verifies invariants, not full automorphism groups
4. **No lifting algorithm**: Uses pre-computed lifting data from T-1003; algorithm is
   T-0002
5. **No genus decomposition beyond uniqueness**: Only checks uniqueness, not full
   decomposition

## Allowed Dependencies

- **Prerequisite tasks**: T-0002 (discriminant form primitives), T-1002 (Coble lattice
  invariants), T-1003 (finite quadratic fixtures)
- **Local sources** (must cite):
  - tasks/goal_expansion.md — task ordering
  - STATE_MACHINE.md — tier semantics
  - PROOF_AUDITING.md — audit criteria

## Required Conventions

1. **Gate naming**: Use pattern `gate_discriminant_form_<fixture>`
2. **Assertion function**: Create reusable
   `assert_discriminant_form_equals(q_computed, q_fixture)`
3. **Brown invariant convention**: Use the convention $\beta(L) \in
   \mathbb{Z}/8\mathbb{Z}$ per Conway-Sloane
4. **Isotropic definition**: $x \in A_L$ isotropic iff $q(x) = 0$ in
   $\mathbb{Q}/2\mathbb{Z}$
5. **Failure format**: Report as `gate_fail: discriminant_form - <mismatch-details>`

## Failure Conditions

1. **Discriminant form mismatch**: If any $q(x)$ value differs, gate fails with
   `fail_discriminant_form`
2. **Brown invariant mismatch**: If $\beta(L)$ differs, gate fails with
   `fail_brown_invariant`
3. **Isotropic count mismatch**: If count differs from $2^{r-a}$, gate fails with
   `fail_isotropic_count`
4. **Orbit count mismatch**: If divisibility orbits differ, gate fails with
   `fail_divisibility_orbits`
5. **(r,a,δ) mismatch**: If invariants differ from fixture, gate fails with
   `fail_invariants`

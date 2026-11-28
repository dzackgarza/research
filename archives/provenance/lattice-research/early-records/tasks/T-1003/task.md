# Task T-1003: Finite Quadratic-Form Fixtures

## Status

Selected in Wave A. TASK_SPECIFICATION complete as of 2026-04-02. Ready for PRE_AUDIT.

## Tier

Tier 1.

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
- GOAL linkage: Fixture support for T-0002 and T-2002

## Objective

Assemble finite quadratic-form fixtures for 2-elementary forms, including known
isotropic counts and small-orbit examples that exercise the discriminant-group
machinery. The fixture package must include:

1. **A_T discriminant group fixtures**: $A_{T_{\mathrm{Co}}} \cong
   (\mathbb{Z}/2\mathbb{Z})^{11}$ with the standard quadratic form $q_T: A_T \to
   \mathbb{Q}/2\mathbb{Z}$
2. **Isotropic vector data**: All 2^11 = 2048 isotropic vectors in $A_T$ with their
   orbit representatives under $O(q_T)$
3. **Small 2-elementary forms**: Representative finite quadratic forms with varying $(r,
   a, \delta)$ invariants for testing:
   - $(1, 1, 0)$, $(1, 1, 1)$, $(2, 0, 0)$, $(2, 2, 0)$, $(2, 2, 1)$, $(3, 1, 0)$, $(3,
     3, 0)$, $(3, 3, 1)$, $(4, 0, 0)$, $(4, 4, 0)$
4. **Orbit representatives**: For each form, canonical orbit representatives under
   $O(q)$
5. **Lifting examples**: Explicit lifts of discriminant-group elements to primitive
   isotropic vectors in $T_{\mathrm{Co}}$ for divisibility $d \in \{1, 2\}$

## Parent Sufficiency Map

Provides exact expected values for discriminant-form and isotropic-count gates; does not
verify them by itself.

## Deliverable Type

fixture data

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- theory/mathematical_background.md
- theory/gap_orbits.md
- REFERENCES.md

## Acceptance Criteria

1. **A_T fixture verification**: The fixture for $A_{T_{\mathrm{Co}}} \cong
   (\mathbb{Z}/2\mathbb{Z})^{11}$ must have exactly 2048 elements with the correct
   quadratic form values $q_T(x) \in \{0, 1\} \subset \mathbb{Q}/2\mathbb{Z}$
2. **Isotropic count verification**: Number of isotropic vectors in $A_T$ (elements $x$
   with $q_T(x) = 0$) must equal $2^{11 - a}$ where $a$ is the $a$-invariant of
   $T_{\mathrm{Co}}$ (from T-1002: $a=11$), the 527 nonzero isotropic vectors (the zero
   vector doesn't count as an orbit representative) form exactly 1 orbit under $O(q_T)$
   per Nikulin 1.5.2
3. **Small form invariants**: Each of the 10 listed small 2-elementary forms must have
   correctly computed $(r, a, \delta)$ invariants matching Nikulin's classification
4. **Orbit structure**: The orbit decomposition of $O(q)$ on the isotropic set must
   produce the expected number of orbits (1 for $T_{\mathrm{Co}}$ case per Nikulin
   1.5.2)
5. **Lifting verification**: For each discriminant-group representative, there exists a
   primitive isotropic lift to $T_{\mathrm{Co}}$ with the correct divisibility
6. **GAP compatibility**: All fixture data must be importable into GAP and produce the
   documented orbit structures
7. **Serialization roundtrip**: Fixtures serialized to JSON and re-loaded must produce
   identical data structures

## Non-Goals

1. **No verification of lattice properties**: This task only provides fixtures;
   verification of discriminant-form correctness happens in T-0002 and T-2002
2. **No implementation of orbit-finding algorithms**: The fixture data is pre-computed;
   algorithmic verification happens in T-0002
3. **No genus decomposition beyond fixtures**: Only provides data for testing; formal
   genus verification is T-3002
4. **No computation of full O(T) groups**: Only provides data for O(q_T) orbits; O(T)
   computation is T-0002
5. **No proof of surjectivity**: The fixture supports testing but formal proof is
   mathematical work (T-3002)

## Allowed Dependencies

- **Prerequisite tasks**: none (this is T-1 foundation)
- **Local sources** (must cite specific sections):
  - theory/mathematical_background.md — sections on discriminant groups and 2-elementary
    lattices
  - theory/gap_orbits.md — GAP orbit computation patterns
  - REFERENCES.md — Nikulin (1979), Sterk (1991) for orbit lifting theorems

## Required Conventions

1. **Basis ordering**: The standard basis for $(\mathbb{Z}/2\mathbb{Z})^{11}$ is $e_1,
   \dots, e_{11}$ where $e_i$ has 1 in position $i$ and 0 elsewhere
2. **Quadratic form convention**: $q(x_1, \dots, x_{11}) = \sum_i x_i^2
   \pmod{2\mathbb{Z}}$ (the standard even form on 2-elementary groups)
3. **Isotropic definition**: $x \in A$ is isotropic if $q(x) = 0$ in
   $\mathbb{Q}/2\mathbb{Z}$
4. **Orbit representative selection**: Use lexicographically smallest element in each
   orbit as canonical representative
5. **GAP export format**: Fixtures must be exportable to GAP-readable format (json or
   plain text with gap syntax)
6. **Fixture naming**: All fixtures use the pattern `qf_<r>_<a>_<delta>` where each is
   the integer value

## Failure Conditions

1. **Incorrect isotropic count**: If the fixture reports a number other than $2^{11-a}$
   isotropic vectors, the fixture is rejected
2. **Non-integral form values**: If any quadratic form value $q(x)$ is not in $\{0, 1\}
   \subset \mathbb{Q}/2\mathbb{Z}$, the fixture is rejected
3. **Orbit count mismatch**: If the number of $O(q)$-orbits on isotropic vectors does
   not match the theoretical prediction, the fixture is rejected
4. **Missing lifting data**: If any discriminant-group element lacks a documented
   primitive lift, the fixture is rejected
5. **GAP import failure**: If the fixture cannot be loaded into GAP, the fixture is
   rejected

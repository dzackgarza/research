---
id: TASK-LAT-PHASE5-ORTHOGONAL-SUBGROUPS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement orthogonal subgroups through ConditionSet composition
status: complete
priority: high
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
  is approved.
successCriteria:
- Read the cited source section before implementation.
- Keep changes inside the named target boundary unless a new card or decision expands
  scope.
- Preserve the mathematical semantics from the source plan and category-spec style
  rules.
- Record validation commands and results before handoff.
- Do not mark this card done without human approval.
complexity: 55
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER
---
# Implement orthogonal subgroups through ConditionSet composition

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.2: Orthogonal Subgroups
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.2),
`category-abc-spec.md`, `forms/docs/MAPPING.md`,
`category_specs/lattices/docs/MAPPING.md`, and `lattice-interface-style-guide.md`.

- Subgroups are predicate-defined refinements of `LatticeOrthogonalGroup` through `LatticeOrthogonalSubgroup`.
- Constructor contracts:
  - `centralizer(g)` adds predicate `f g = g f`.
  - `stabilizer(v)`:
    - if `v in L`, fixes vector (`f(v)=v`);
    - if `v` is a submodule or flagged subobject, preserves its image setwise through
      the subobject inclusion morphism and chosen generators, rather than comparing raw
      ambient coordinates.
  - `stabilizer_of_isotropic_line(v)` applies line-level predicate (`f(v) ∈ {v,-v}`).
  - `kernel_of_discriminant_action()` adds the condition that the induced action on
    `A_L` is identity.
  - `special_orthogonal_subgroup()` is the determinant-one subgroup after the chosen
    matrix realization of `O(L)` is fixed.
- Subgroup operations are via `ConditionSet` intersection/union; no bespoke composition operators.
- Membership semantics remains inherited from ambient orthogonal group and predicate set.

Backend routing:
- Subgroup predicates are in-memory and deterministic.
- For finite subgroup computations (order, Schreier search, stabilizer lifts), prefer
  GAP once a finite matrix-group realization exists.
- For indefinite subgroup membership inherited from `O(L)`, reuse the Indefinite.jl
  ambient group realization rather than introducing subgroup-specific local search.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/groups/orthogonal.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

## Current Phase Gate

- 2026-05-06: Blocked by the current category-spec and semantic-vocabulary phase. This
  is implementation-phase Sage/lattice work and must not be executed merely to make
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

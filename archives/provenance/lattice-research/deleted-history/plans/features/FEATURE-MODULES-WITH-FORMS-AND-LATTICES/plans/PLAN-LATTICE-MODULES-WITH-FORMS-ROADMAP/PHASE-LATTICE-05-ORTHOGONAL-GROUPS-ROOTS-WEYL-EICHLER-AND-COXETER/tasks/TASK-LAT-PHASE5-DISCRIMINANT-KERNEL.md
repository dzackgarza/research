---
id: TASK-LAT-PHASE5-DISCRIMINANT-KERNEL
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement kernel of discriminant action
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
# Implement kernel of discriminant action

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.9: Kernel of Discriminant Action
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.9),
`category_specs/lattices/docs/MAPPING.md`,
`category_specs/forms/docs/MAPPING.md`,
`category-abc-spec.md`, and `lattice-interface-style-guide.md`.

- The discriminant action is the induced group morphism `O(L) -> O(A_L)` coming from
  the quotient `A_L = L^*/L`.
- For `f in O(L)`, the induced action on a class `g in A_L` is computed by choosing
  `g.lift() in L^*`, applying the dual extension of `f`, then projecting back with
  `discriminant_class()`. The action must be independent of the chosen lift because the
  quotient kills the image of `L`.
- `kernel_of_discriminant_action()` returns the subgroup of `O(L)` (or of a subgroup
  `G <= O(L)`) acting trivially on every generator/class of `A_L`.
- This subgroup lives on the orthogonal-group layer, not on the lattice as an ad hoc
  helper. Membership is a predicate on orthogonal-group elements, composed through the
  same `ConditionSet` architecture as stabilizers and centralizers.

Backend routing:
- The induced action on the finite discriminant object is local once `A_L`, `lift()`,
  and `discriminant_class()` are implemented.
- Finite-group computations on `O(A_L)` or subgroup images may route to GAP/Sage small
  group machinery, but this card does not introduce a separate discriminant-action
  algorithm.

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

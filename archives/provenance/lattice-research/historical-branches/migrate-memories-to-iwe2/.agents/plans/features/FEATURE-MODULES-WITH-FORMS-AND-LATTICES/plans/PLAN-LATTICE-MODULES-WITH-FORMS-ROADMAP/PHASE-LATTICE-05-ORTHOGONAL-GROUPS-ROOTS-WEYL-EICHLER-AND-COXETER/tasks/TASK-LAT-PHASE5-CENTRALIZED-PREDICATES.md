---
id: TASK-LAT-PHASE5-CENTRALIZED-PREDICATES
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement centralized predicates for orthogonal subgroup surfaces
status: complete
priority: critical
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
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER
---
# Implement centralized predicates for orthogonal subgroup surfaces

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.0: Centralized Predicates
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.0),
`category-abc-spec.md`, `forms/docs/MAPPING.md`,
`category_specs/lattices/docs/MAPPING.md`, and
`lattice-interface-style-guide.md`.

- Centralized predicates live in `src/lattices/predicates.py` and are the only shared containment policy.
- Required predicate objects:
  - `IsometryPredicate(gram)` evaluates `M^T * G * M == G` to define `f ∈ O(L)`.
  - `CentralizerPredicate(g)` evaluates `f * g == g * f`.
  - `StabilizerPredicate(v)` evaluates `f(v) == v`.
  - `LinePredicate(v)` evaluates `f(v) in {v,-v}`.
  - `DiscriminantKernelPredicate(L)` evaluates `f` acting trivially on `A_L` through
    the quotient map `L^* -> A_L`, using `lift()` on discriminant generators and
    `discriminant_class()` on their images.
- These predicates are morphism predicates. The underlying universe is the relevant
  matrix/hom realization (`GL_n(R)` or `End(L)`), but the public contract remains
  subgroup membership in a morphism-valued parent.
- Subgroup composition is done strictly by `ConditionSet` set operators (`&`, `|`) on predicate sets.
- Any site that needs containment checks calls predicate objects through `LatticeOrthogonalSubgroup`/group membership, never `assert`ing raw matrix equations.
- `f in O(L)` remains true iff `f` is a morphism `L → L` and passes `is_isometry`.

Backend routing:
- Predicate checks themselves are local and deterministic.
- Finite subgroup enumeration or stabilizer search routes to GAP once the subgroup is
  realized as a finite action.
- Indefinite automorphism membership still routes through the ambient Indefinite.jl
  isometry/automorphism adapters; this file owns the predicate layer, not the search
  algorithms.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/predicates.py`.

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
  current Sage objects pass category-obligation examples before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

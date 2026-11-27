---
id: TASK-LAT-PHASE2-PYDANTIC-VALIDATION
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
dependsOn: []
title: Implement constructor validation models for Phase 2 carriers
status: complete
priority: high
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.
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
- PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS
---
# Implement constructor validation models for Phase 2 carriers

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.8: Pydantic Validation
- Parent plan: `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- `validation/presentations.py` defines all Phase 2 constructor-level proof obligations for form objects and
  carriers; validation is data-structural, not behavioral.
- Required model contracts:
  - `FormCodomainModel`: validate `base_ring` (PID-compatible) and `codomain` as a coherent Sage parent.
  - `BilinearModulePresentationModel`: validate form domain/rank, square matrix shape, and branch-consistent
    entries.
  - `FreeModulePresentationModel`: validate free-rank realization and coefficient ring membership.
  - `TorsionModulePresentationModel`: validate invariant tuples and torsion codomain in quotient-valued branches.
- Required mechanics:
  - Use `model_validator(mode="after")` for derived checks (e.g., symmetry when `symmetric=True`,
    nondegeneracy assumptions, rank and ring branch coherence).
  - Keep error messages actionable and branch-specific (`integral`, `rational`, `torsion_*`).
  - Export only model-level constructors used by `core` carriers in this phase.
- Acceptance checks:
  - Invalid shape/ring/branch input fails before object construction.
  - Valid models permit the corresponding `from_*` constructors in `core/abstract.py`/`core/free.py`/`core/torsion.py`.
  - Validation does not mutate semantic state; it only rejects malformed presentations.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/validation/presentations.py`.

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

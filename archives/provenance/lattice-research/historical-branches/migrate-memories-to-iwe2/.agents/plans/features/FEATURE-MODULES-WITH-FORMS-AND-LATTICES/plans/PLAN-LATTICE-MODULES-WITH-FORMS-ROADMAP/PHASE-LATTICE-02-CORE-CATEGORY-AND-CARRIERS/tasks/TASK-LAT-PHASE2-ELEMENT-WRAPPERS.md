---
id: TASK-LAT-PHASE2-ELEMENT-WRAPPERS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
dependsOn: []
title: Implement thin element wrappers backed by category mixins
status: complete
priority: critical
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
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS
---
# Implement thin element wrappers backed by category mixins

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.5: Thin Element Wrappers Backed by Category Mixins
- Parent plan: `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Element wrappers in `core/elements.py` are thin `ElementWrapper` adapters over backend elements. They do
  not define category semantics independently; semantics are owned in `ModulesWithForms(...)`
  `ElementMethods`.\n-  - Carrier classes: `BilinearModuleElement`, `FreeBilinearModuleElement`, `TorsionBilinearModuleElement`,\n+  - Carrier classes: `BilinearModuleElement`, `FreeBilinearModuleElement`, `TorsionBilinearModuleElement`,\n    `QuadraticModuleElement`, `FreeQuadraticModuleElement`, `TorsionQuadraticModuleElement`.
- Required element API this phase:
  - parent access and conversion: `parent()`, `__hash__`, `__eq__`, `to_vector()`, `to_coordinates()`.
  - arithmetic in symbolic space: `__add__`, `__sub__`, `__neg__`, scalar action via `__rmul__`/`__mul__`.
  - bilinear/quadratic evaluation: `__mul__`/`_mul_(other)` dispatch to parent form when available,
    with `q()`/`norm()` delegating to form evaluation.
  - geometric predicates: `is_isotropic()` and `is_primitive()` via category-owned predicates.
- Ownership boundaries:
  - `span()` and inclusion maps belong to category/parent methods; wrappers only expose delegates.
  - `additive_order()` appears on torsion elements only and delegates to parent torsion data.
- Acceptance checks:
  - Symbolic behavior holds (`L.<e,f>; [1,0] not in L`; `e * f` and `e.is_isotropic()` derive from form).
  - `v + w`, `-v`, scalar actions remain closed in same parent type.
  - `hash(v)` and equality are stable under presentation-preserving operations.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/elements.py`.

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

---
id: TASK-LAT-PHASE2-THIN-CARRIERS-PROMOTION
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
dependsOn: []
title: Implement thin concrete carriers and category promotion
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
# Implement thin concrete carriers and category promotion

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.4: Thin Concrete Parent Carriers and Promotion
- Parent plan: `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Thin carrier classes in `core/abstract.py` are state-holding parents only. They must delegate core
  algebraic behavior to `ModulesWithForms` category mixins (`ParentMethods`, `ElementMethods`,
  `MorphismMethods`), including validation ownership, inclusion maps, span behavior, and hom
  construction.
- Constructor contracts:
  - `ModuleWithForm.from_gram(R, gram_matrix, codomain=...)` for free presentations.
  - `ModuleWithForm.from_module_and_form_data(module, gram_matrix, codomain=...)` for mixed carriers.
  - `ModuleWithForm.from_cokernel(morphism)` remains a Phase 3 concrete implementation point.
  - `from_quotient(...)` is a local shim only when quotient parent is provided by a tested backend.
- Promotion contract:
  - Carrier promotion is determined by predicates (`Bilinear`/`Quadratic`, `Free`/`Torsion`,
    `Integral`/`Rational`, `NonDegenerate`) and returns the richest compatible meet.
- Required method-level operators:
  - `__add__`: direct sum / orthogonal block sum in the same carrier family.
  - `__pow__`: `n`-fold direct sum (`L^n`).
  - `__mul__` and `__rmul__`: scalar submodule operation using module multiplication on coordinates.
  - `__contains__`: parent membership only; coordinates are not coerced by default.
  - `_element_constructor_` to construct/wrap elements via owned element class.
- Acceptance checks:
  - `L + L` remains a `ModuleWithForm` in the expected meet.
  - `L ^ 3` is well-typed and preserves form degree and presentation intent.
  - `a in L` is a true parent-membership query.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/abstract.py`.

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

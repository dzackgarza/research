---
id: TASK-LAT-PHASE2-FREE-TORSION-CARRIERS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
dependsOn: []
title: Implement concrete free and torsion carriers
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
# Implement concrete free and torsion carriers

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.6: Concrete Free and Torsion Carriers
- Parent plan: `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Concrete carriers in `core/free.py` and `core/torsion.py` implement presented objects:
  - `FreeBilinearModule`: free finite-rank objects with form matrix data (`M ≅ R^n`).
  - `TorsionBilinearModule`: torsion quotients/invariants with codomain in `K/R` or `K/(2R)` branches.\n-  - `Rational`/`integral` classification is property-based via `FormCodomain`.
- Required methods in this phase:
  - `span(gens)` returns the subobject with inherited form on generated vectors.
  - `perp(submodule)`/`orthogonal_complement(submodule)` for symmetric forms.
  - `is_nondegenerate()`, `is_degenerate()`.
  - form invariants in free branch: `determinant()`, `discriminant()`, `signature_pair()`, `rank()`.
  - torsion predicates and invariants: `is_torsion()`, `additive_order()`, `value_module()`.
- Method ownership:
  - Structural submodule/quotient behavior comes from category subobject/quotient surfaces where available.
  - Torsion/discriminant-specific behavior stays in torsion carrier classes and forms-owned methods.\n-  - No legacy `is_injective`/`is_surjective`/`is_identity` ad hoc checks are introduced here.\n+- Acceptance checks:
  - `FreeBilinearModule(...).span([e])` returns free module of expected rank and inherited form matrix.
  - `perp()` returns complement object in same family when symmetry permits.
  - `TorsionBilinearModule.from_invariants_and_gram(...)` validates invariants and keeps form codomain in `QQ/ZZ`/`QQ/2ZZ` when `R=ZZ`.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/free.py; src/lattices/core/torsion.py`.

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

---
id: TASK-LAT-PHASE2-FORM-CODOMAIN
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
dependsOn: []
title: Implement FormCodomain and quotient-valued codomain predicates
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
# Implement FormCodomain and quotient-valued codomain predicates

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.2: FormCodomain
- Parent plan: `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Canonical codomain object: `FormCodomain` is a typed descriptor carrying
  `(base_ring: R, codomain: S)` where `S` is a genuine `R`-module parent accepting all
  form values.
- Required value targets:
  - `FormCodomain.integral(R) -> S = R` (`Bilinear`/`Quadratic` integral branch),
  - `FormCodomain.rational(R) -> S = Frac(R)`,
  - `FormCodomain.torsion_bilinear(R) -> S = Frac(R) / R`,
  - `FormCodomain.torsion_quadratic(R) -> S = Frac(R) / (2R)`.
- `R = ZZ` specializations are `QQ`, `QQ/ZZ`, and `QQ/2ZZ` in the working codomain stack.
- Method-level contract in `core/codomains.py`:
  - `integral`, `rational`, `torsion_bilinear`, `torsion_quadratic` constructors.
  - `coerce(value)`/call-style coercion into `S` for form evaluation.
  - `is_torsion_valued` predicate and `contains(value)` checks against the codomain parent.
- Ownership:
  - `Form` objects own no matrix/ambient conventions; codomain determines branch predicates.
  - No separate “fake codomain descriptor” is permitted beyond a validated parent holder.
- Acceptance checks:
  - `FormCodomain.integral(ZZ).codomain() is ZZ`.
  - `FormCodomain.rational(ZZ).codomain() is QQ`.
  - `FormCodomain.torsion_bilinear(ZZ).codomain() == QQ / ZZ`.
  - `FormCodomain.torsion_quadratic(ZZ).codomain() == QQ / (2*ZZ)`.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/codomains.py`.

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

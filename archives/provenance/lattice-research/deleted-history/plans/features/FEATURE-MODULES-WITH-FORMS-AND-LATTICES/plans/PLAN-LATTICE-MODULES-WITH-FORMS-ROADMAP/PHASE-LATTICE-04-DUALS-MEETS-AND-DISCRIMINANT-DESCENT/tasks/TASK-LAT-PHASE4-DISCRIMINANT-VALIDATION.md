---
id: TASK-LAT-PHASE4-DISCRIMINANT-VALIDATION
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
dependsOn: []
title: Implement discriminant descent validation models
status: complete
priority: high
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is
  approved.
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
- PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT
---
# Implement discriminant descent validation models

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is approved.

## Source Provenance

- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- Source section: DiscriminantGroupFromCokernelModel and related validation
- Parent plan: `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-4-discriminant-descent.md` (Step 4.6), `category-abc-spec.md`, `category_specs/lattices/docs/MAPPING.md`, and `theory/spec_backups/lattices_written_spec_backup.py`.

- `LatticeFromGramModel` and `DiscriminantGroupFromCokernelModel` are validation contracts for public parse/creation paths:
  - `from_gram` requires symmetric integral Gram matrix and nondegeneracy (`det != 0`).
  - discriminant validation requires `module.cardinality() == abs(det(G_L))` for cokernel input from dual inclusion.
  - quotient form values must be reduced into `QQ/ZZ` and `QQ/2ZZ` representatives in the discriminant categories.
  - dual/discriminant parse paths must distinguish algebraic-dual metadata from
    rational-dual presentation data, so `lift()` and `discriminant_class()` typecheck
    against actual dual/discriminant parents rather than raw coordinate containers.
- These are data contracts only (Pydantic/Basemodel validation shape); they encode invariants that the public methods must satisfy before object creation.
- Model-level predicates must remain close to source:
  - `discriminant_group` is an actual object with inherited operations (`additive_order`, `is_isomorphic_to`, etc.), not just metadata.
  - `A_L` presentation equality and isometry/isomorphism are category-level methods on the discriminant object.

Backend routing:
- Validation is local and schema-level.
- Expensive checks (`is_isometric_to`, local genus checks, automorphism queries) should not be reimplemented in this layer.

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
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

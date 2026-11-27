---
id: TASK-LAT-PHASE4-RATIONAL-LATTICE-MEET
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
dependsOn: []
title: Implement RationalLattice meet and scalar multiple semantics
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
# Implement RationalLattice meet and scalar multiple semantics

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is approved.

## Source Provenance

- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- Source section: Step 4.1: Rational Lattice Meet
- Parent plan: `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `category-abc-spec.md`, `lattice-interface-style-guide.md`, `forms/docs/MAPPING.md`, `theory/foundations/bilinear-forms-duals-morphisms.md`, and `pln-lattice-phase-4-discriminant-descent.md` (Step 4.1).

- `RationalLattice` is the meet
  `ModulesWithForms(R).Bilinear().Free().NonDegenerate().Rational()`.
  For `R = ZZ`, this is a `QQ`-valued free symmetric nondegenerate bilinear module.
- In this category the parent must expose:
  - `form()`, `b(v,w)`, `gram_matrix()`;
  - `rank()`, `gens()`, `span(...)`, `perp(...)`;
  - `is_nondegenerate()` etc from the category axioms.
- `from_free_module_and_gram(...)` must construct the free module and its `QQ`-valued Gram matrix in coordinates; `b(v,w)` is the coordinate evaluation in that generating set.
- Scalar multiplication and twist are distinct:
  - `n * L` is the submodule `{ n*v : v in L }` with generators `{ n*e_i }` and Gram matrix `n^2 G_L`.
  - `L.twist(n)` scales the form only: Gram matrix `n*G_L`.
  - The constructor contract is explicit in the plan (`not (2*U).is_isometric_to(U.twist(2))`).
- `L = (1/n) * L` is represented as a free rational module with Gram `(1/n^2) G_L` and the same abstract basis semantics as other scalar multiples.
- `divisibility(v)` remains the categorical form definition from `category-abc`:
  `divisibility(v) = < b(v, w) : w in M > <= S`, where `S` is the form codomain.
  For scalar-valued integral forms `S = R`, this is an ideal of `R`; for rational
  codomain `S = K`, it is a submodule of `K`, not a coordinate gcd.
- `__mul__` and `__add__` are module operations, not ambient-vector shortcuts.

Backend routing:
- No new local linear-algebra engine is introduced here; this card only defines the in-memory rational-lattice meet contract.
- For invariants needing external engines later in the phase, use the Phase 4/5 backend protocol (Indefinite/CARAT split) rather than matrix-level hand proofs.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/rational.py`.

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

---
id: TASK-LAT-PHASE4-DISCRIMINANT-OBJECTS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
dependsOn: []
title: Implement discriminant quotient objects and form data
status: complete
priority: critical
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
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT
---
# Implement discriminant quotient objects and form data

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is approved.

## Source Provenance

- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- Source section: Step 4.3: Discriminant Objects
- Parent plan: `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `category-abc-spec.md`, `forms/docs/MAPPING.md`, `theory/foundations/bilinear-forms-duals-morphisms.md`, `theory/spec_backups/lattices_written_spec_backup.py`, and `pln-lattice-phase-4-discriminant-descent.md` (Step 4.3).

- Discriminant object:
  - The discriminant group is `A_L := coker(iota_L)` for `iota_L : L -> L^*`.
  - Construction is generic cokernel machinery on `ModulesWithForms`: this is a torsion formed module with descended form in `K/R` and optional quadratic refinement in `K/2R`.
- Quotient-valued form semantics:
  - For bilinear object `(coker iota_L, \bar b)`, define
    `\bar b([x], [y]) = b(x,y) mod R` in `K/R`.
  - For associated quadratic structure, codomain is `K/2R` when available.
  - In `R = ZZ`, this is the integral workflow `QQ/ZZ` and `QQ/2ZZ`.
- `discriminant_class` semantics:
  - For `x in L^*`, `discriminant_class(x)` is class of `x` in `A_L`.
  - For `v in L` (ordinary lattice element), class is zero by factorization through inclusion `L -> L^*`.
- Category placement:
  - quotient-valued discriminant forms belong to torsion formed categories:
    `ModulesWithForms(R).Quadratic().Torsion().NonDegenerate()` with the correct
    quotient-valued codomain.
  - discriminant group API should not collapse to raw invariant packages; `A_L` is an actual category object from the cokernel.
- Divisibility remains a form-codomain submodule: for element `[x]` in `A_L`,
  `divisibility([x]) = <bar_b([x], [y]) : [y] in A_L>` in the torsion value module,
  not an integer divisor extracted from a lift.

Model/validation contract:
- `DiscriminantGroupFromCokernelModel` validates:
  - `module.cardinality() == abs(det(gram_matrix(L)))`;
  - derived bilinear values are well-defined in `QQ/ZZ` (and quadratic values in `QQ/2ZZ` where present).
  - the quotient map `L^* -> A_L` sends the image of `L` to zero, and `lift()` lands
    back in the chosen dual-lattice presentation.
- Equality on discriminant groups is equality of presented torsion objects; isometry is a predicate with induced morphism witness.

Backend routing:
- Cokernel descent uses existing module `cokernel()` semantics from `ModulesWithForms` and should not introduce standalone quotient arithmetic.
- Any downstream finite classification checks (isomorphism/order checks) may use GAP/CARAT/Sage bridges as dictated by rank/definiteness in later backend rules.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/discriminant.py`.

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

---
id: TASK-LAT-PHASE4-DUAL-LATTICE-OBJECTS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
dependsOn: []
title: Implement dual lattice objects as functionals
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
# Implement dual lattice objects as functionals

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` is approved.

## Source Provenance

- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- Source section: Step 4.2: Dual Lattice Objects
- Parent plan: `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `theory/foundations/bilinear-forms-duals-morphisms.md`, `category-abc-spec.md`, `forms/docs/MAPPING.md`, and `theory/spec_backups/lattices_written_spec_backup.py` (DualLattice, dual-lattice section).

- Algebraic dual and sharp/rational dual split:
  - Algebraic dual is `Hom_R(L, R)` in the abstract category of formed modules.
  - Rational dual (the home used by this code) is `L_K = L ⊗_R K` equipped with the form extended to `K`, and the sublattice
    `L^# = { x in L_K : β_K(x, L) ⊆ R }` (`K = Frac(R)`).
  - For nondegenerate free modules, basis choices identify `L^#` with `L^*`; the
    Gram matrix represents the adjoint map `L -> L^*`, while the inverse Gram matrix
    represents the inclusion `L^# -> L_K` after the dual basis is chosen through
    `lambda^{-1}(e_i^*)`.
- `DualLattice` is a rational-lattice object living in `RationalLattice`:
  - elements are functionals `L -> R` or `L -> K` as explicit members of the dual module, not raw ambient vectors.
  - `source_lattice() -> L` is mandatory metadata; this is not an equality with an ambient copy.
  - `DualLattice.from_lattice(L)` must use `L`’s Gram matrix as the linear map `ι_L: L → L^*` by convention in chosen coordinates.
- `inclusion_morphism()` contract:
  - returns `iota_L` in `L.Hom(dual)` and `to_matrix()` equals Gram matrix of `L` in canonical generators after the `category-abc` representation.
  - evaluation semantics: for basis vectors `e_j`, `iota_L(e_j) = Σ_i β(e_j,e_i) e_i^*`.
- `DualLatticeElement` and `LatticeElement` both expose:
  - `discriminant_class()` on dual side: map to `A_L = coker(iota_L)`.
  - `L` elements map to zero class via the inclusion path.
- `divisibility` and `is_primitive` remain form-derived (not coordinate gcd by default):
  `divisibility(v) = <b(v, w) : w in L>` in the form codomain, and ordinary lattice
  elements are primitive by the presented-module inclusion data, not by ambient-vector
  shortcuts.

Backend and routing:
- `inclusion_morphism` and dual module construction stay in `ModulesWithForms`/`DualObjects`; no custom local algebra engines are introduced in this card.
- Any finite/infinite isometry or automorphism claim using `DualLattice` is deferred to later Phase-4/5 backend decisions (currently no new math kernels in this card).

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
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

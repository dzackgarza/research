---
id: TASK-LAT-PHASE5-ORTHOGONAL-GROUP
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement LatticeOrthogonalGroup as morphism-valued parent
status: complete
priority: high
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
complexity: 55
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER
---
# Implement LatticeOrthogonalGroup as morphism-valued parent

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.1: LatticeOrthogonalGroup
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.1), `category-abc-spec.md`, `category_specs/lattices/docs/MAPPING.md`, and `forms/docs/MAPPING.md`.

- `orthogonal_group` is `Aut(M,b)` on the formed module category object `(M,b)`.
- `LatticeOrthogonalGroup` is therefore a subgroup of automorphisms of `L` in the form-preserving hom category:
  - elements are lattice morphisms, not matrices.
  - `O(L)` membership filters on object type (`L → L`) plus form preservation predicate from predicates module.
- `from_matrix` and `__call__` are constructor/dispatch layers:
  - both return morphisms in `O(L)` after validation.
  - matrix entry is always interpreted as a representation in the canonical generators, then validated by `is_isometry`.
- `identity`, `gens`, `order`, `__iter__` stay on `LatticeOrthogonalGroup`.
- Required semantics checks:
  - `L.orthogonal_group().lattice() == L`;
  - a raw matrix is not a group element until wrapped by `O(L).from_matrix(...)` or
    `O(L)(...)`;
  - every element of `O(L)` is a morphism in `L.End()` that preserves the form.

Exact backend routing:
- Positive-definite finite matrix-group auxiliaries may use CARAT and GAP through
  backend adapters.
- Indefinite isometry testing routes to polyhedral_common
  (`src/external/dutsik_polyhedral/polyhedral_common`) via
  `INDEF_FORM_TestEquivalence`. The Python wrapper bridge exists at
  `src.bak/backends/external/py_polyhedral/` and exports
  `indefinite_form_test_equivalence`, `indefinite_form_automorphism_group`,
  `indefinite_form_get_orbit_representative`, `indefinite_form_stabilizer_vector`,
  `lorentzian_reflective_edgewalk`, and related functions.
- The `LatticeIsometryBackend` at `src.bak/backends/isometry_backend.py` uses this
  bridge and is the reference for how to route indefinite isometry queries through
  the orthongal-group surface.
- The `DawesOrbitBackend` at `src.bak/backends/dawes_orbit_backend.py` (1034 lines)
  uses the same bridge for orbit and stabilizer computations with indefinite forms.
- See `projects/github.com__dzackgarza__lattice-research/references/polyhedral-common-indefinite-methods`
  for the full API table of the polyhedral_common bridge.
- The Julia-based Indefinite.jl bridge is a secondary option when polyhedral_common
  binaries are unavailable.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/groups/orthogonal.py`.

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

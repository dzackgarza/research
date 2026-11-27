---
id: TASK-LAT-PHASE5-ISOTROPIC-ORBITS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement isotropic orbit enumeration
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
# Implement isotropic orbit enumeration

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.3: Isotropic Orbits
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.3),
`theory/references/index.md` (Dawes), `theory/backends/software-capability-map.md`,
and `theory/backends/indefinite-jl.md`.

- Orbits:
  - `isotropic_line_orbits()` enumerates primitive isotropic lines modulo sign.
  - `isotropic_plane_orbits()` enumerates primitive isotropic 2-planes modulo group action.
  - `isotropic_flag_orbits(dim)` enumerates isotropic flags of the requested length/dimension.
  - `isotropic_lines_are_equivalent(v,w)` is an orbit-membership predicate.
- Sign convention is inherited from lattice primitives: lines are projective (`<v>`), so line predicates are projective and should not confuse with vector-orbit predicates.
- For `O(L)` vs `SO(L)` semantics: `O(L)` may identify more line orbits due to determinant sign flexibility; `SO(L)` may split those orbits.
- Orbit outputs are representatives in the semantic lattice/group categories: a line
  orbit returns primitive isotropic line representatives, a plane orbit returns
  primitive isotropic sublattices or their chosen generator data, and a flag orbit
  returns nested isotropic subobject data.

Backend routing (exact):
- Indefinite forms: use Indefinite.jl APIs:
  - `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`, `INDEF_FORM_GetOrbit_IsotropicKflag`.
- Vector/isometry equivalence questions arising while comparing orbit representatives
  route to `INDEF_FORM_TestEquivalence`.
- Finite groups/actions: use GAP orbit/stabilizer tools.
- This card does not introduce new local isotropic-flag enumeration engines.

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
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

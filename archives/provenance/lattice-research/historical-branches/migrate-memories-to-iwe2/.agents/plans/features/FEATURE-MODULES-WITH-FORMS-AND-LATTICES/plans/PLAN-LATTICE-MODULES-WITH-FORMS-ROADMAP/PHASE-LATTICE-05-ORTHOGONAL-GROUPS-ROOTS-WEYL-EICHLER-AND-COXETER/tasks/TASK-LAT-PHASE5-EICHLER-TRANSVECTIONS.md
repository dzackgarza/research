---
id: TASK-LAT-PHASE5-EICHLER-TRANSVECTIONS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement Eichler transvections
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
# Implement Eichler transvections

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.7: Eichler Transvections
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Mining Deliverable

Source anchors checked: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.7),
`category-abc-spec.md`, `lattice-interface-style-guide.md`,
`category_specs/lattices/docs/MAPPING.md`, `theory/foundations/bilinear-forms-duals-morphisms.md`,
`theory/backends/software-capability-map.md`, `theory/backends/vinberg-algorithm.md`,
and `theory/references/index.md`.

- The migrated phase prose records the candidate Eichler transvection formula
  `t_{e,r}(w) = w - (r,w)e + (e,w)r - (r,r)/2 * (e,w)e`, with hypotheses `e`
  isotropic and `r in e^perp`, but the required local theory/reference sources above do
  not yet provide a canonical cited authority for that formula or for the claimed
  identities (`t_{e,r}^{-1} = t_{e,-r}`, product-of-reflections decomposition,
  multiplicativity in the second argument).
- Therefore the concrete deliverable of this leaf is source mining inside the existing
  repo reference spine: identify and cite the primary local authority from
  `theory/references/index.md` or acquired literature, then pin
  - the exact formula,
  - the precise hypotheses on `e`, `r`, and the ambient lattice,
  - the return object as an element of `O(L)`,
  - every algebraic identity that will become an acceptance criterion.
- Until that source is pinned, do not implement a public `eichler_transvection` or
  `EichlerGroup` API from the migrated prose alone.

Backend routing:
- Once the formula is source-grounded, construction of a specific transvection is a
  local morphism-building task in `O(L)`.
- This card does not justify a new external backend and does not license a bespoke
  replacement formula.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/groups/eichler.py`.

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

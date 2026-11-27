---
id: TASK-LAT-PHASE5-INVOLUTION-EIGENLATTICES
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
dependsOn: []
title: Implement involution eigenlattices
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
# Implement involution eigenlattices

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.4: Involution Eigenlattices
- Parent plan: `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.4), `category-abc-spec.md`, and `theory/spec_backups/lattices_written_spec_backup.py`.

- `L.invariant_sublattice(g)` contract:
  - Defined for involution `g ∈ O(L)` as `ker(g - id)` and expressed via kernel on hom-space.
  - Hypothesis: `g^2 = id`; precondition for interpretation as invariant part.
- `L.coinvariant_sublattice(g)` contract:
  - Defined as `ker(g + id)` (−1-eigenspace lattice in free module terms).
  - Expectation: in hyperbolic rank-2 examples `coinvariant = invariant.perp()` when form is nondegenerate.
- Return objects are lattices with inherited forms (subobject kernels with restricted form).
- These are lattice-level methods on `Lattice` with subobject semantics, not matrix operators.
- Compatibility checks must use morphism arithmetic only (`g + id`, `g - id`) and kernel construction from morphism category.

Vocabulary requirement:
- The involution g is an element of the lattice Aut category, represented as a
  morphism `L.Aut()(g)`, not as a raw matrix. The `g` is constructed as a lattice
  isometry; a matrix representation is extracted only for verification against
  backend computations.
- `invariant_sublattice(g)` is `g.kernel_minus_one()` expressed in the lattice's
  subobject vocabulary (`L.Subobjects()`), not a matrix nullspace computation.
- `coinvariant_sublattice(g)` is `g.kernel_plus_one()` by the same token.
- The resulting sublattice objects carry inclusion morphisms into L, not bare
  generator matrices.

Backend routing:
- Kernel/inclusion computations are category-algebraic local operations on hom-objects.
- Any downstream group-order computations from these sublattices are delegated according to backend map (finite exact / indefinite split).

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

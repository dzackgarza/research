---
id: FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
plans: []
title: Sage-backed categorical implementation layer
status: unstarted
priority: critical
description: Implement or wrap Sage and external mathematical objects so the repo owns objects satisfying approved category specs directly, with categorical interfaces, coercions, validation, and backend bridge boundaries rather than permanent refinement notes.
---
# Feature: Sage-backed categorical implementation layer

## Summary

Build the owned categorical implementation layer required by `GOAL.md` after the category-spec and Sage-refinement work has settled. This feature is not the spec program itself: it owns the production implementation and wrapper surfaces that make approved category specs executable mathematical objects.

## Source Provenance

- `GOAL.md`, stage "owned categorical implementation layer".
- `.agents/current-goal-phase.md`, which gates implementation work behind the active semantic-vocabulary phase.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES.md`.
- `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`.
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`.

## Scope

- Implement or wrap Sage classes so objects satisfy approved category specs directly.
- Preserve mature backend ownership: Sage, GAP, Singular, Macaulay2, Oscar/Julia, PARI/GP, CARAT, and related systems provide mathematical kernels where they already exist.
- Keep local code focused on categorical interfaces, coercions, validation, exact bridge boundaries, and typed object/morphism surfaces.
- Turn spec-discovered backend gaps into explicit follow-up specs, plans, or backend-research cards rather than ad hoc local algorithms.

## Non-Goals

- Do not replace approved specs with implementation convenience.
- Do not implement mathematical kernels locally when a mature exact backend can supply them.
- Do not treat raw matrices, untyped morphisms, or helper scripts as public mathematical objects.

## Acceptance Criteria

- [ ] Approved category specs have corresponding owned implementation or wrapper surfaces.
- [ ] Object, morphism, Hom, End, Aut, constructor, coercion, and validation behavior is expressed through typed categorical interfaces.
- [ ] Backend bridge boundaries state the exact external system, input/output contracts, witness checks, and unsupported cases.
- [ ] Implementation tests use real mathematical data and verify recovered or produced objects, not mocks.
- [ ] Any unsupported spec requirement is filed as a backend-gap, spec, or implementation card with source provenance.

## Dependencies And Boundaries

This feature starts only after the category, ModulesWithForms/lattice, and geometry-facing spec surfaces are in the DAG as completed prerequisites. It does not authorize downstream Coble computations by itself; later features still need universal categorical algorithms and Coble-specific geometric lattice foundation work.

## Work Log

- Created as a GOAL.md coverage card so the tracker distinguishes completed specification work from the later owned implementation layer.

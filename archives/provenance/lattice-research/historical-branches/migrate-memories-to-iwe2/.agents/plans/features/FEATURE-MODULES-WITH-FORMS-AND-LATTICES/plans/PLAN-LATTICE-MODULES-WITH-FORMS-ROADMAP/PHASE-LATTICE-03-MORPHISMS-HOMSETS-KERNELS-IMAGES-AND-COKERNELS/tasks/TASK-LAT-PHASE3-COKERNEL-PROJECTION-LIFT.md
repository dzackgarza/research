---
id: TASK-LAT-PHASE3-COKERNEL-PROJECTION-LIFT
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
dependsOn: []
title: Implement cokernel projection and lift contract
status: complete
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
  is approved.
successCriteria:
- Every cokernel object returned by Phase 3 exposes a canonical projection morphism
  from the original codomain, and that projection is surjective with kernel equal
  to the image of the original morphism.
- '`lift()` exists only as quotient-representative selection for cokernel elements
  and composes with `projection()` to recover the original quotient class.'
- Quotient invariants, generators, and cardinality remain properties of the cokernel
  object itself rather than ad hoc helpers on the original morphism wrapper.
- The projection/lift API works for both ordinary quotient modules and the discriminant-style
  quotient path needed later for `L^#/L`.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS
---
# Implement cokernel projection and lift contract

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.5: Cokernel Contract
- Parent plan: `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Source anchors:
  - `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/plans/PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP/PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS/PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS.md` (Step 3.5)
  - `category_specs/modules/docs/MAPPING.md`
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  - `theory/foundations/bilinear-forms-duals-morphisms.md`
- Projection semantics:
  - if `C = f.cokernel()`, then `C.projection()` is the canonical quotient morphism `pi : codomain(f) -> C`;
  - `pi` is a morphism in the relevant formed-module homspace, `pi.is_surjective()` is true, and `ker(pi) = im(f)` as categorical objects.
- Lift semantics:
  - each cokernel element `x_bar in C` may expose `x_bar.lift()` returning some chosen representative `x in codomain(f)` such that `pi(x) = x_bar`;
  - this is representative data for the quotient projection, not a new section or splitting morphism;
  - the implementation may delegate representative choice to the underlying FGP quotient lift, then wrap the representative back into the codomain object.
- Quotient-object surface:
  - invariants, cardinality, generators, and other quotient data belong on the cokernel object `C`, not on the original morphism;
  - `projection()` lives on the quotient object because it is structure of the quotient, while `lift()` lives on quotient elements because it chooses representatives of quotient classes.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/morphisms/bilinear.py`.

## Acceptance Criteria

- [ ] Every cokernel object returned by Phase 3 exposes a canonical projection morphism from the original codomain, and that projection is surjective with kernel equal to the image of the original morphism.
- [ ] `lift()` exists only as quotient-representative selection for cokernel elements and composes with `projection()` to recover the original quotient class.
- [ ] Quotient invariants, generators, and cardinality remain properties of the cokernel object itself rather than ad hoc helpers on the original morphism wrapper.
- [ ] The projection/lift API works for both ordinary quotient modules and the discriminant-style quotient path needed later for `L^#/L`.

## Dependencies And Boundaries

Execute within `src/lattices/morphisms/bilinear.py`, keeping quotient structure on the cokernel object and representative choice on cokernel elements. Do not reinterpret `lift()` as a canonical inverse to the projection.

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

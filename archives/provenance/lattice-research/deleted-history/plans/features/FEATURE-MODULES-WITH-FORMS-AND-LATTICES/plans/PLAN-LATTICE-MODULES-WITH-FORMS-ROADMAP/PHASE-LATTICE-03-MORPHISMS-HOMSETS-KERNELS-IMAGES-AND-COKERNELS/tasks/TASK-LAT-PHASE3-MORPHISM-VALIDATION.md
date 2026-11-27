---
id: TASK-LAT-PHASE3-MORPHISM-VALIDATION
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
dependsOn: []
title: Implement validation for morphism construction and containment
status: complete
priority: high
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
  is approved.
successCriteria:
- Validation models reject shape-mismatched matrices, incomplete generator-image data,
  and codomain-incompatible images before homspace construction is attempted.
- Validation models encode the sourced matrix convention and ordered-generator convention
  once, so `from_dict`, `from_images`, and `from_matrix` are checked against the same
  data contract.
- Validation success produces constructor-ready data for morphism wrappers; containment
  in `M.Hom(N)` still performs the form-preservation check.
- No validation surface treats raw matrices or raw dictionaries as public morphism
  elements.
complexity: 55
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS
---
# Implement validation for morphism construction and containment

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.8: Morphism Validation
- Parent plan: `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Source anchors:
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  - `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
  - `category_specs/homsets/docs/MAPPING.md`
  - `category_specs/modules/docs/MAPPING.md`
  - `category_specs/forms/docs/MAPPING.md`
- Validation owner: `src/lattices/validation/presentations.py` validates constructor data for public morphism-building routes; it does not redefine morphism semantics outside the hom-category.
- Constructor-data contracts:
  - mapping/dict input must cover the chosen domain generators and land in the codomain object;
  - image tuples must have the correct length and ordered-generator meaning;
  - matrix input must match the domain/codomain presentation sizes and the sourced column convention `column_j = f(e_j)`.
- Containment contracts:
  - validation distinguishes raw constructor data from already-built morphism wrappers;
  - a validated morphism candidate still becomes an element of `M.Hom(N)` only when linearity/domain/codomain compatibility and form preservation hold.
- Boundary:
  - validation may certify that data can build a morphism wrapper;
  - it does not treat matrices, dicts, or image tuples as morphism elements in their own right.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/validation/presentations.py`.

## Acceptance Criteria

- [ ] Validation models reject shape-mismatched matrices, incomplete generator-image data, and codomain-incompatible images before homspace construction is attempted.
- [ ] Validation models encode the sourced matrix convention and ordered-generator convention once, so `from_dict`, `from_images`, and `from_matrix` are checked against the same data contract.
- [ ] Validation success produces constructor-ready data for morphism wrappers; containment in `M.Hom(N)` still performs the form-preservation check.
- [ ] No validation surface treats raw matrices or raw dictionaries as public morphism elements.

## Dependencies And Boundaries

Execute within `src/lattices/validation/presentations.py`, keeping validation focused on constructor data and presentation shape. Public morphism membership remains owned by the homspace.

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

---
id: TASK-LAT-PHASE3-END-AUT-QUOTIENT-NOTATION
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
dependsOn: []
title: Implement End Aut and quotient notation through homset machinery
status: complete
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
  is approved.
successCriteria:
- '`M.End()` is implemented as the same parent as `M.Hom(M)` and carries the documented
  endomorphism identity and composition structure.'
- '`M.Aut()` is implemented as the invertible part of `M.End()`, with `inverse()`
  and `is_isomorphism()` coming from the aut/end hierarchy rather than ad hoc matrix
  predicates.'
- For formed modules and lattices, orthogonal-group semantics are expressed through
  `Aut(M, b)` membership, so form preservation remains the containment law for aut
  elements.
- '`M / N` routes through the inclusion morphism and returns the cokernel object in
  the formed-module hierarchy.'
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS
---
# Implement End Aut and quotient notation through homset machinery

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Steps 3.6 and 3.7: End Aut and quotient notation
- Parent plan: `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Source anchors:
  - `category_specs/homsets/docs/MAPPING.md`
  - `category_specs/modules/docs/MAPPING.md`
  - `category_specs/forms/docs/MAPPING.md`
  - `category_specs/lattices/docs/MAPPING.md`
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- Hom/End/Aut semantics:
  - for any formed object `M`, `M.End()` is the end object `End(M) = Hom(M, M)` in the same hom-category hierarchy as `M.Hom(M)`;
  - `M.Aut()` is the invertible part of `End(M)`, i.e. the units in the endomorphism monoid, not a separately guessed matrix group;
  - in the forms-owned categories, `Aut(M, b)` is the orthogonal group: automorphisms of `M` that preserve the attached form.
- Public-construction boundary:
  - `End` and `Aut` are category-recognized parents with domain/codomain semantics inherited from the generic hom object;
  - Sage `ConditionSet` may appear as an internal bridge in generic aut construction, but the public surface is the project-owned aut parent/object.
- Quotient notation:
  - `M / N` means the cokernel of the canonical inclusion `N -> M` when `N` is a genuine subobject of `M`;
  - the result is the categorical quotient object in `ModulesWithForms(R)` with induced quotient data, not shorthand for ambient-coordinate elimination.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/categories/modules_with_forms.py`.

## Acceptance Criteria

- [ ] `M.End()` is implemented as the same parent as `M.Hom(M)` and carries the documented endomorphism identity and composition structure.
- [ ] `M.Aut()` is implemented as the invertible part of `M.End()`, with `inverse()` and `is_isomorphism()` coming from the aut/end hierarchy rather than ad hoc matrix predicates.
- [ ] For formed modules and lattices, orthogonal-group semantics are expressed through `Aut(M, b)` membership, so form preservation remains the containment law for aut elements.
- [ ] `M / N` routes through the inclusion morphism and returns the cokernel object in the formed-module hierarchy.

## Dependencies And Boundaries

Execute within `src/lattices/categories/modules_with_forms.py`, preserving the generic hom/end/aut construction from the category-spec mapping. Do not expose quotient notation as raw presentation syntax detached from an inclusion morphism.

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

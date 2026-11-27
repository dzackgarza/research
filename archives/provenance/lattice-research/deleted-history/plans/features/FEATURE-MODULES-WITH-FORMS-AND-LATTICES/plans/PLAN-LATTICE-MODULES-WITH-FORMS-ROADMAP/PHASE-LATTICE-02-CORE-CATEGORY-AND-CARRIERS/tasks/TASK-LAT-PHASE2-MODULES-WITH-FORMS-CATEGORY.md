---
id: TASK-LAT-PHASE2-MODULES-WITH-FORMS-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
dependsOn: []
title: Implement ModulesWithForms category and subcategory methods
status: complete
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.
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
- PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS
---
# Implement ModulesWithForms category and subcategory methods

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.1: ModulesWithForms(R) Category
- Parent plan: `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Object definition: `ModulesWithForms(R)` is a category of pairs `(M, f)` where `M` is a
  finitely presented `R`-module (owned by the module stack) and `f` is form data on a
  graded/quotiented tensor construction of `M` valued in an actual `R`-module parent `S`
  (`FormCodomain`). Source-owned canonical definition is in
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Branches:
  - `Bilinear()` — degree-2 form with `sigma = id_R`, source `M \otimes_R M` or an
    explicitly descended symmetric quotient such as `Sym^2(M)`.
  - `Quadratic()` — degree-1 form with the same `Module + form` pipeline and lattice-side
    convention `sigma(r) = r^2`.
- Morphism contract:
  - Over equal base rings: `f: M1 -> M2` is an `R`-linear map satisfying
    `form2(f(v), f(w)) = form1(v,w)` for all generators/elements.
  - Over base change `g: R1 -> R2`, morphisms are triples `(g, \~f, \~h)` on base-changed
    modules and codomains in `theory/foundations/bilinear-forms-duals-morphisms.md`.
- Presentation semantics: two objects with different generating data (`gens`/basis) are
  distinct even if isometric; method-level equality uses presentation identity, while isometry
  is through hom-set containment.
- Elements and ownership:
  - Object-level element semantics come from `ModulesWithForms(...).ElementMethods`.
  - Thin wrappers in `src/lattices/core/elements.py` are `ElementWrapper` adapters only.
  - `ModulesWithForms(...).Hom(other)` and `Homsets.ParentMethods` are the public constructor
    for morphism objects.
- Methods this card owns:
  - category mixins: `ParentMethods.form`, `ParentMethods.Gens`, `ParentMethods.free_part`,
    `ParentMethods.torsion_part`, `ParentMethods.Hom`, `ElementMethods.to_vector`,
    `MorphismMethods.{__call__,kernel,image,domain,codomain}` and `SubcategoryMethods` for
    `Bilinear/Quadratic/Free/Torsion/NonDegenerate/Integral/Rational/CartesianProducts/
    TensorProducts/DualObjects`.
- Acceptance checks in scope:
  - `L in ModulesWithForms(ZZ).Bilinear()` for phase-2 bilinear constructions.
  - `Hom(L1, L2)` exists and returns category-owned hom-space object.
  - `L1.Hom(L2).element_class` and `L1.Hom(L2).morphism_class` resolve to thin wrapper
    carriers.
  - `isinstance(m, Morphism) and m.domain() is L1 and m.codomain() is L2` for all promoted
    hom-space constructors covered in this phase.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/categories/modules_with_forms.py`.

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

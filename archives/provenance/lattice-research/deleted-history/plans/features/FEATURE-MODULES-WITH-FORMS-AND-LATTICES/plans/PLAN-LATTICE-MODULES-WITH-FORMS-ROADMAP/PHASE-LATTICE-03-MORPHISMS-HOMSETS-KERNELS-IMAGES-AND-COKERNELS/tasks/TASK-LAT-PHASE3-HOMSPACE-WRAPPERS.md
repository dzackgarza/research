---
id: TASK-LAT-PHASE3-HOMSPACE-WRAPPERS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
dependsOn: []
title: Implement concrete Hom-space wrappers
status: complete
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
  is approved.
successCriteria:
- '`M.Hom(N)` is admitted as `ModulesWithForms(R).Bilinear().HomCategory().Of(M, N)`
  and retains the `R`-module parent structure documented for module homsets.'
- Dicts, ordered image tuples, and matrices are accepted only as constructor data;
  equivalent inputs produce the same `BilinearModuleMorphism`, while the raw constructor
  data itself is not an element of `M.Hom(N)`.
- '`__contains__` accepts exactly wrapper morphisms with matching domain/codomain
  whose underlying map is linear and form-preserving in the sense `b_N(f(v), f(w))
  = b_M(v, w)` on domain generators.'
- '`identity()` exists only on end objects, `zero()` exists on every hom object, and
  both return morphisms parented by the same homspace.'
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS
---
# Implement concrete Hom-space wrappers

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.1: Concrete Hom-Space Wrappers
- Parent plan: `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Source anchors:
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  - `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
  - `category_specs/homsets/docs/MAPPING.md`
  - `category_specs/forms/docs/MAPPING.md`
- Homspace semantics: for objects `M, N` in `ModulesWithForms(R).Bilinear()` (or refinements), `M.Hom(N)` is the categorical parent `Hom(M, N)`.
  - Its elements are wrapper morphisms only (not raw matrices or bare maps).
  - The parent carries domain and codomain and uses ambient `Hom` structure from `ModulesWithForms`.
- Constructor-data semantics:
  - `element_from_dict({g_i: x_i})` consumes an explicit map from `M.gens()` to `N` and returns a morphism in `M.Hom(N)`.
  - `element_from_images((x_1, ..., x_n))` consumes ordered domain-generator images and returns a morphism in the same homspace.
  - `element_from_matrix(A)` consumes a matrix whose column `j` is `f(e_j)` and returns `f` in `M.Hom(N)`.
- Containment semantics (`__contains__`):
  - valid only if `f` is a `BilinearModuleMorphism` parented by this homspace and whose underlying FGP map is in the parent fgp-homset;
  - and form preservation holds: `N.b(f(e_i), f(e_j)) == M.b(e_i, e_j)` for all domain generators.
- Dispatch semantics:
  - `__call__` is a thin wrapper: pass through existing homspace elements, lift FGP morphisms from the cached fgp-homset, otherwise treat matrix-like constructor data through `element_from_matrix`.
- Algebraic identity:
  - `zero()` and `identity()` construct morphisms in this homspace using category-level construction, preserving source/codomain and form-aware membership constraints.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/morphisms/homspaces.py`.

## Acceptance Criteria

- [ ] `M.Hom(N)` is admitted as `ModulesWithForms(R).Bilinear().HomCategory().Of(M, N)` and retains the `R`-module parent structure documented for module homsets.
- [ ] Dicts, ordered image tuples, and matrices are accepted only as constructor data; equivalent inputs produce the same `BilinearModuleMorphism`, while the raw constructor data itself is not an element of `M.Hom(N)`.
- [ ] `__contains__` accepts exactly wrapper morphisms with matching domain/codomain whose underlying map is linear and form-preserving in the sense `b_N(f(v), f(w)) = b_M(v, w)` on domain generators.
- [ ] `identity()` exists only on end objects, `zero()` exists on every hom object, and both return morphisms parented by the same homspace.

## Dependencies And Boundaries

Execute within `src/lattices/morphisms/homspaces.py` against the Phase 3 plan and existing `ModulesWithForms(R)` hom-category contracts. Preserve the distinction between constructor data and morphism elements; do not move form-preservation checks out of homspace containment.

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

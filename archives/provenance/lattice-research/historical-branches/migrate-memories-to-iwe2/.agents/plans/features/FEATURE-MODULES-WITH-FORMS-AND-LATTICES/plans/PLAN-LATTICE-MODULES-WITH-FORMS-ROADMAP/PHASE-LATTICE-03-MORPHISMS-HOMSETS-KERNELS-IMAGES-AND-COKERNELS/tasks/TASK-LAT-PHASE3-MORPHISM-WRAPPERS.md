---
id: TASK-LAT-PHASE3-MORPHISM-WRAPPERS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
dependsOn: []
title: Implement concrete bilinear module morphism wrappers
status: complete
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
  is approved.
successCriteria:
- '`BilinearModuleMorphism` remains a `Morphism` wrapper over an underlying linear
  map; matrices stay representational output via `to_matrix()`, not first-class morphism
  elements.'
- '`to_matrix()`, `images()`, and any dict/image reconstruction agree on the ordered-generator
  convention used by the homspace constructors.'
- Composition, additive operations, scalar action, direct sum, and `inverse()` all
  preserve domain/codomain orientation and return morphisms in the correct hom or
  end parent.
- '`is_isometry()` is equivalent to membership in the relevant form-preserving hom/end/aut
  object, while `is_isomorphism()` and `is_primitive()` stay module-level predicates
  defined through bijectivity and torsionfreeness of the cokernel.'
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS
---
# Implement concrete bilinear module morphism wrappers

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.2: Concrete Morphism Wrappers
- Parent plan: `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Source anchors:
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  - `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
  - `category_specs/homsets/docs/MAPPING.md`
  - `category_specs/forms/docs/MAPPING.md`
- Morphism carrier: `BilinearModuleMorphism` is a Sage `Morphism` object whose parent is a concrete homspace from `.Hom(N)`.
- Data model: store underlying Sage/FGP morphism (`_fgp_morphism`) and expose domain/codomain via homspace parent.
- Evaluation contract (`_call_`): map `x in domain` to `codomain`.
- Constructor/representation contracts:
  - `to_matrix()` returns the matrix of generator images in codomain generators, matching the constructor layout used by homspace methods.
  - `images()` / `im_gens` return the tuple of domain-generator images.
- Algebraic contracts:
  - `__add__`, `__neg__`, `__sub__`, and direct sum are inherited `Hom`-module/sum operations and stay inside this homspace.
  - `__mul__` implements composition with strict domain/codomain compatibility (`(self ∘ other)` style).
  - `direct_sum` returns block-diagonal direct-sum morphism on `M1+M2 -> N1+N2`.
  - `inverse()` is defined only for bijective maps (`is_bijective`); `is_isometry` delegates to form-aware containment (`self in self.parent()`).
- Predicate contracts:
  - `is_injective()` tests `kernel().ngens() == 0`.
  - `is_surjective()` tests `cokernel().ngens() == 0`.
  - `is_isomorphism()` means bijective underlying linear map (for module-level semantics).
  - `is_primitive()` means `self.cokernel().is_torsionfree()` for lattice morphisms.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/morphisms/bilinear.py`.

## Acceptance Criteria

- [ ] `BilinearModuleMorphism` remains a `Morphism` wrapper over an underlying linear map; matrices stay representational output via `to_matrix()`, not first-class morphism elements.
- [ ] `to_matrix()`, `images()`, and any dict/image reconstruction agree on the ordered-generator convention used by the homspace constructors.
- [ ] Composition, additive operations, scalar action, direct sum, and `inverse()` all preserve domain/codomain orientation and return morphisms in the correct hom or end parent.
- [ ] `is_isometry()` is equivalent to membership in the relevant form-preserving hom/end/aut object, while `is_isomorphism()` and `is_primitive()` stay module-level predicates defined through bijectivity and torsionfreeness of the cokernel.

## Dependencies And Boundaries

Execute within `src/lattices/morphisms/bilinear.py` using the existing homspace parent as the sole owner of domain/codomain and form-preservation semantics. Do not reintroduce matrix-first or ambient-space semantics on the public morphism surface.

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

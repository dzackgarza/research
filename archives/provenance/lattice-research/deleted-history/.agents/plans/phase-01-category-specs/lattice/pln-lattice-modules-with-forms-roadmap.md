---
trackerStatus:
  type: plan
title: Lattice and ModulesWithForms roadmap
status: approved
planId: PLN-LAT-000
planType: implementation-roadmap
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-CAT-100
tags:
- category-specs
- plan
- lattices
- modules
- forms
- theme-modules-tensors
- theme-category-core
---

# Lattice and ModulesWithForms roadmap

## Objective

Organize the lattice redesign around the actual dependency chain: Sage/module prerequisites, category core, morphisms and cokernels, lattice/dual/discriminant descent, then orthogonal and Coxeter structures.

## Source corpus

- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `theory/foundations/bilinear-forms-duals-morphisms.md`
- `theory/spec_backups/lattices_written_spec_backup.py`
- `plans/PHASE_0_SAGE_PATCHES.md`
- Deleted superseded crosswalk: `plans/PHASE_1_BILINEAR_MODULES.md`
- `plans/PHASE_2_CORE_OBJECTS.md`
- `plans/PHASE_3_MORPHISMS.md`
- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`

The skill-local files and `theory/` files are the current durable source layer. The
old phase-plan files remain migration provenance and implementation inventory, not
standalone authority for definitions.

## Mathematical Grounding Rules

Every lattice/module/form child card must ground public vocabulary before execution:

- modules with forms are pairs `(M, f)` over an explicit base ring with an explicit
  form source and codomain;
- a bilinear form is stated first as a morphism/pairing, with matrices appearing only
  after a presentation or generator choice is fixed;
- changing generators or basis data changes the presented object, even when the result
  is isometric;
- duals, discriminant groups, isometries, cokernels, primitive predicates,
  divisibility, and orthogonal-group operations must cite exact definitions and
  hypotheses before code or spec surfaces are moved;
- old code in `theory/spec_backups/` is source material to mine, not an API to copy.

Cards that cannot state source, definition, hypotheses, codomain/return object, and
choice-independence or equivalence obligations are blocked only for that leaf; the
correct continuation is a source-mining, decision, or split prerequisite.

## Admitted Definitions

The roadmap admits these definitions from the current source layer:

- `ModulesWithForms(R)` is the category of finitely generated or finitely presented
  `R`-modules equipped with form data, with `R` currently scoped to commutative PIDs
  through `ModuleBaseRings`. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- The generic object is `(M, f)`, where `M` is an `R`-module and `f` is semilinear
  tensor-degree data with an actual `R`-module codomain `S`; scalar-valued forms
  `S = R` are a special case, not the general definition. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Bilinear, quadratic, free, torsion, nondegenerate, integral, rational, tensor,
  Cartesian, dual, and Homset strata are subcategory axioms or construction
  categories, not separate foundations. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Presented object identity is generator-sensitive: a free bilinear module is
  presented by module, form, and selected generators. Changing generators changes the
  presented object; isometry is a morphism-level relation with a witness. Sources:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md` and
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- Form-preserving morphisms and isometries are categorical morphisms: a bilinear
  morphism `f: M1 -> M2` satisfies `b1(v,w) = b2(f(v), f(w))`; an isometry is an
  isomorphism with that property. Source:
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.
- Dual and discriminant constructions are morphism/cokernel constructions. `ad_b:
  L -> L^*` sends `v` to `b(v,-)`, and `A_L` is recovered as the cokernel quotient
  `L^*/L` with quotient-valued form data when hypotheses hold. Sources:
  `theory/foundations/bilinear-forms-duals-morphisms.md` and
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`.

## Phase tree

- `PLN-LAT-010`: Phase 0 Sage patch prerequisites.
- `PLN-LAT-020`: Phase 2 ModulesWithForms core category and carriers.
- `PLN-LAT-030`: Phase 3 morphisms, homsets, kernels, images, and cokernels.
- `PLN-LAT-040`: Phase 4 lattice meets, duals, and discriminant descent.
- `PLN-LAT-050`: Phase 5 orthogonal groups, roots, Weyl, Eichler, and Coxeter.

## Structural rule

Phase 1 is gone as an active unit. It was a crosswalk from the old monolithic plan into Phases 2-5. The active graph is Phase 0 -> Phase 2 -> Phase 3 -> Phase 4 -> Phase 5.

## Acceptance Criteria

- [ ] Phase 0 prerequisites are complete before Phase 2 implementation starts.
- [ ] Category vocabulary and method ownership from `PLN-CAT-100` are settled before dependent implementation.
- [ ] Phase 3 cokernels exist before Phase 4 discriminant descent.
- [ ] Phase 4 lattice/discriminant objects exist before Phase 5 group theory.
- [ ] Every executable item links to exactly one phase or foundation plan.

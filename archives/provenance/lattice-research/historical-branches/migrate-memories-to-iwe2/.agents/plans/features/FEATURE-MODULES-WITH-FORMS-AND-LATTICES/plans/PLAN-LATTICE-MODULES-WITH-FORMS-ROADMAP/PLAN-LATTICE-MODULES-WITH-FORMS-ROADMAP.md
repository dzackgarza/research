---
id: PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
trackerStatus:
  type: plan
parents:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
dependsOn: []
title: Lattice and ModulesWithForms roadmap
status: complete
priority: critical
owner: Zack
description: 'Organize the lattice redesign around the actual dependency chain: Sage/module
  prerequisites, category core, morphisms and cokernels, lattice/dual/discriminant
  descent, then orthogonal and Coxeter structures.'
successCriteria:
- Phase 0 prerequisites are complete before Phase 2 implementation starts.
- Category vocabulary and method ownership from `PLAN-CATEGORY-FOUNDATION-KERNEL`
  are settled before dependent implementation.
- Phase 3 cokernels exist before Phase 4 discriminant descent.
- Phase 4 lattice/discriminant objects exist before Phase 5 group theory.
- Every executable item links to exactly one phase or foundation plan.
phases:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
- '[[PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS]]'
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
- '[[PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER]]'
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
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

## Existing backend bridge: polyhedral_common

A working Python wrapper for the polyhedral_common C++ library already exists in
`src.bak/`. This is the intended route for all indefinite lattice computations
(automorphism groups, isometry testing, orbit representatives, stabilizers,
Vinberg edgewalk). Key files:

- **Python wrapper module**: `src.bak/backends/external/py_polyhedral/` — exports
  `indefinite_form_test_equivalence`, `indefinite_form_automorphism_group`,
  `indefinite_form_get_orbit_representative`, `indefinite_form_stabilizer_vector`,
  `lorentzian_reflective_edgewalk`, and related functions.
- **Isometry backend**: `src.bak/backends/isometry_backend.py` — `LatticeIsometryBackend`
  with rank/signature/determinant screening → Nikulin 2-elementary branch → general
  indefinite polyhedral_common dispatch.
- **Orbit backend**: `src.bak/backends/dawes_orbit_backend.py` (1034 lines) — orbit
  and stabilizer computation for indefinite forms using the same bridge.
- **Memory docs**: `the Polyhedral Common Reference memory in the iwe2 vault`
  with API tables and indefinite method reference.

These backends are quarantine code (moved to `src.bak/` during the spec-first phase)
and will be reactivated when the category spec vocabulary is in place. Their interfaces
may need wrapping to use the spec's lattice objects rather than raw Sage matrices.

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

- `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`: Phase 0 Sage patch prerequisites.
- `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS`: Phase 2 ModulesWithForms core category and carriers.
- `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`: Phase 3 morphisms, homsets, kernels, images, and cokernels.
- `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT`: Phase 4 lattice meets, duals, and discriminant descent.
- `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER`: Phase 5 orthogonal groups, roots, Weyl, Eichler, and Coxeter.

## Structural rule

Phase 1 is gone as an active unit. It was a crosswalk from the old monolithic plan into Phases 2-5. The active graph is Phase 0 -> Phase 2 -> Phase 3 -> Phase 4 -> Phase 5.

## Acceptance Criteria

- [ ] Phase 0 prerequisites are complete before Phase 2 implementation starts.
- [ ] Category vocabulary and method ownership from `PLAN-CATEGORY-FOUNDATION-KERNEL` are settled before dependent implementation.
- [ ] Phase 3 cokernels exist before Phase 4 discriminant descent.
- [ ] Phase 4 lattice/discriminant objects exist before Phase 5 group theory.
- [ ] Every executable item links to exactly one phase or foundation plan.

## Work Log

- 2026-05-06: Corrected roadmap status to `blocked`: Phase 0 execution was premature
  during the spec/vocabulary phase. The roadmap remains approved as future implementation
  structure, but implementation leaves are not current executable work.

## Current Phase Gate

- 2026-05-06: Blocked by the repo's current category-spec and semantic-vocabulary
  phase. This roadmap is implementation-phase work: it exists as an approved future
  implementation plan, but it must not be executed to make Sage pass category-obligation tests while
  the ideal mathematical specs and ownership vocabulary are still being settled.
- Category-obligation examples exhibit whether representative objects satisfy declared category obligations; they do not justify weakening specs or adding
  Sage patches during spec work. Continue approved spec, source-mining, audit, and
  decision leaves outside this implementation path until the phase-transition criteria
  in `GOAL.md` and `.agents/current-goal-phase.md` are met.

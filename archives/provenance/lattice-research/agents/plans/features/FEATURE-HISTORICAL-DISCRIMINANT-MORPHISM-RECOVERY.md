---
id: FEATURE-HISTORICAL-DISCRIMINANT-MORPHISM-RECOVERY
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
plans: []
title: Historical discriminant and morphism recovery
status: complete
priority: high
description: Recover discriminant-group, quotient-valued form, Hom, End, Aut, kernel, image, cokernel, and discriminant-descent behavior from historical src.bak under the current ModulesWithForms contract.
---
# Historical discriminant and morphism recovery

## Summary

Recover the discriminant and morphism capabilities visible in
`src.bak/lattices/core/discriminant.py` and `src.bak/lattices/morphisms/` as
category-correct formed-module operations. This feature exists because the old code
contains useful target behavior but used narrow wrappers and shortcut promotion logic
that must be replaced by the current categorical cokernel and Hom semantics.

## Source Provenance

- `src.bak/lattices/core/discriminant.py`
- `src.bak/lattices/morphisms/discriminant.py`
- `src.bak/lattices/morphisms/lattice.py`
- `src.bak/lattices/morphisms/homspaces.py`
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- IWE `bilinear-form-category-semantics`

## Recovery Boundary

The historical code points to required behavior: discriminant groups/forms, generators,
iteration over finite torsion objects, `q` and `b` evaluation, elementary-abelian
predicates, submodules, quotients, orthogonal submodules, Hom construction, and
morphism kernel/image/cokernel operations.

The recovered surface must make `A_L = L^#/L` a categorical cokernel of the metric
inclusion `L -> L^#` with descended quotient-valued form data. It must not rely on a
special-case quotient of a Sage object as the public definition, and it must not
identify the metric dual `L^#` with the Hom dual `Hom_R(L,R)` unless an explicit
form-induced transport map supplies that identification under stated hypotheses.

## Non-Preservation Boundaries

- Do not preserve `DiscriminantForm = DiscriminantGroup` as a semantic collapse unless
  a spec explicitly records the alias and its limits.
- Do not make discriminant-group backends the public owner of Hom/End/Aut semantics.
- Do not promote arbitrary cokernels to discriminant groups by pattern matching a
  special `DualLattice` class without stating the morphism and coefficient data.
- Do not bury form-preservation in ad hoc matrix checks outside Hom containment.

## Child Specs

- `[[SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE]]`
- `[[SPEC-HISTORICAL-DISCRIMINANT-DESCENT-MORPHISM-SURFACE]]`

## Acceptance Criteria

- [ ] Discriminant objects are recovered as quotient-valued formed-module objects.
- [ ] Hom/End/Aut, kernel, image, and cokernel behavior is owned by the category and
  morphism layers.
- [ ] Old wrapper shortcuts are converted into explicit contracts or rejected.

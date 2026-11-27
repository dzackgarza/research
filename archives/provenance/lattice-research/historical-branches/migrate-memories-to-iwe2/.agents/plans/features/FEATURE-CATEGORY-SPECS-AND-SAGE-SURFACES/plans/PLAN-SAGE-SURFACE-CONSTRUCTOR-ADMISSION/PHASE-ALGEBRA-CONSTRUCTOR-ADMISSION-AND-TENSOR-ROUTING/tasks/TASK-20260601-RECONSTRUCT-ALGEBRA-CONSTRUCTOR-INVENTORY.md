---
id: TASK-20260601-RECONSTRUCT-ALGEBRA-CONSTRUCTOR-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Reconstruct algebra constructor inventory from Sage source before code repair
status: unstarted
priority: high
description: Rebuild the Algebras constructor-name inventory from Sage docs/source
  and repair the owner split before treating QC failures as code edits.
activityType: source-mining
uncertaintyState: ordinary-open
workstreamRole: implementation
claimStatus: source-backed
successCriteria:
- Sage algebra constructor docs/source are cited for each admitted constructor shape.
- SPEC-MAPPING-ALGEBRAS records constructorNameInventories for every exposed algebra
  constructor collector.
- Magmatic, associative, and unital algebra constructor ownership is reconciled before
  implementation changes.
- check-constructor-name-inventory no longer reports algebra constructor collector
  failures.
complexity: 55
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Reconstruct algebra constructor inventory from Sage source before code repair

## Summary

The constructor-name validator reports public methods on
`category_specs.algebras.Algebras._Constructors` with no machine-readable mapping
inventory.
This is not a naming-cleanup task.
The first repair is to rebuild the constructor admission source: Sage docs/source,
mapping rows, owner category, accepted input shapes, and only then code/category-obligation example changes.

## Source Provenance

- `category_specs/algebras/docs/SAGE_INVENTORY.md`
- `category_specs/algebras/docs/MAPPING.md`
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-ALGEBRAS.md`
- `category_specs/algebras/__init__.py`
- Sage sources named by the mapping: `sage/categories/algebra_functor.py`,
  `sage/categories/sets_cat.py`, `sage/algebras/free_algebra.py`,
  `sage/categories/magmatic_algebras.py`,
  `sage/categories/associative_algebras.py`, and
  `sage/algebras/finite_dimensional_algebras/finite_dimensional_algebra.py`.

## Context

The existing mapping already states source-backed routes for:

- `FreeAlgebra(R, n, names)` / `algebras.Free(R, n, names)`;
- `S.algebra(R, category=...)` through magma, semigroup, monoid, group, additive
  semigroup, additive monoid, and additive group source categories;
- finite-dimensional algebra construction through multiplication tensors.

The mapping also says some routes land in `MagmaticAlgebras(R)` or
`AssociativeAlgebras(R)`, while the current code exposes all public methods on
`Algebras(R)._Constructors`.
Resolve that owner split at the mapping/source level before changing code.

## Acceptance Criteria

- [ ] List every admitted Sage algebra constructor shape and the exact Sage source
      branch that accepts it.
- [ ] Decide the smallest owner category for each constructor collector:
      `MagmaticAlgebras(R)`, `AssociativeAlgebras(R)`, or `Algebras(R)`.
- [ ] Add or correct `constructorNameInventories` in `SPEC-MAPPING-ALGEBRAS` for
      every exposed collector.
- [ ] Move/rename implementation methods only after the mapping owner is explicit.
- [ ] Run `just --justfile category_specs/justfile check-constructor-name-inventory`
      and record any remaining non-algebra failures separately.

## Dependencies And Boundaries

- Do not classify these failures as stale QC or inherited noise.
- Do not preserve rejected constructor ideas as mapping rows.
- Do not broaden the task into tensor-component constructor repair except where the
  algebra mapping delegates a finite-dimensional algebra input to a tensor constructor.

## Work Log

- Created from constructor-name inventory QC output after the anti-polishing constructor
  source gate was added.

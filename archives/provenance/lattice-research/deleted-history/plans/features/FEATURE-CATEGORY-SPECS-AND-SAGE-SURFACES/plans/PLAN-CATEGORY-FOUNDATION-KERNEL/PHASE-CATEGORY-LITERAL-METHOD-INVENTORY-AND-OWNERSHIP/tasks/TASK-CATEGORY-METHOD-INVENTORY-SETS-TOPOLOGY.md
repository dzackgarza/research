---
id: TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Write set topology and metric method ownership rows
status: complete
priority: critical
owner: Zack
description: Mine set, finite-set, enumerated-set, subobject, image-set, topological,
  and metric inventories into literal method-owner rows.
successCriteria:
- The target method-inventory spec contains set, finite, countable/enumerated, subobject,
  image-object, topological, and metric method tables.
- '`len(X)` / `__len__` is recorded as finite-set or finite-enumeration protocol ownership,
  not a root `Sets()` method.'
- Every set operation row states whether the owner is root `Sets()`, countable or
  enumerated sets, finite sets, subobjects, image subobjects, topological spaces,
  or metric spaces.
- Sage wrapper and RealSet methods are either admitted with owner and codomain, mapped
  to named constructor or subobject routes, or rejected as interop/display/private
  behavior.
complexity: 70
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Write set topology and metric method ownership rows

## Summary

Write the literal method-owner rows for sets and topology. This task should produce
actual tables in `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` or split
trackable spec cards when the table becomes too large.

## Source Provenance

- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`
- `category_specs/topological_spaces/docs/MAPPING.md`
- Existing partition follow-up spec:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`

## Context

The seed rows include:

- root set surface: `__contains__`, `an_element`, `some_elements`, `cardinality`,
  `is_empty`, `is_finite`, `subsets`, `subsets_lattice`, `union`, set comparison,
  `_sympy_`;
- countable/enumerated surface: `__iter__`, `rank`, `unrank`, `__getitem__`,
  iterator ranges, `first`, `next`, `random_element`;
- finite surface: `len(X)`, `__len__`, `list(X)`, `tuple(X)`, finite conversion
  protocols and caches;
- subobject surface: `intersection`, `difference`, `symmetric_difference`,
  `complement`, subset comparisons requiring a common ambient;
- image/subquotient surface: `ambient`, `lift`, `retract`;
- set-to-algebra routes: `free_module(R)` and `free_algebra(R)` with module or algebra
  constructor owners, not generic Sage `S.algebra(R)` ownership;
- RealSet and topology surface: `closure`, `interior`, `boundary_points`, `contains`,
  interval/ray/real-line constructor methods, connectedness and compactness refinements;
- metric surface: `metric_function`, `metric`, `dist`, element distance delegation,
  product metric, complete metric refinement.

## Complexity And Ownership

- Owner/role: category-spec sets/topology spec writer.
- Complexity: `70` (high).
- Rationale: this touches root set semantics, Python protocols, finite/countable
  distinctions, subobject operations, RealSet topology, and metric refinements.
- Split/promote note: if the set and topology tables exceed one readable spec section,
  split into separate set and topology spec cards while keeping this task as the
  coordinating leaf.

## Acceptance Criteria

- [x] The target method-inventory spec contains set, finite, countable/enumerated, subobject, image-object, topological, and metric method tables.
- [x] `len(X)` / `__len__` is recorded as finite-set or finite-enumeration protocol ownership, not a root `Sets()` method.
- [x] Every set operation row states whether the owner is root `Sets()`, countable or enumerated sets, finite sets, subobjects, image subobjects, topological spaces, or metric spaces.
- [x] Sage wrapper and RealSet methods are either admitted with owner and codomain, mapped to named constructor or subobject routes, or rejected as interop/display/private behavior.

## Dependencies And Boundaries

- Do not expose Sage `Set(X)` as a generic public constructor.
- Do not collapse real intervals, open subsets, finite point sets, and general
  topological spaces into one constructor owner.
- Do not admit Python export methods such as `set()` or `frozenset()` as mathematical
  set methods unless a new source-grounded decision says otherwise.
- When Sage places a method on a concrete wrapper, map it to the minimal mathematical
  category or reject it as wrapper state.

## Work Log

- 2026-05-05: Created as the sets/topology leaf for the literal method ownership inventory phase.
- 2026-05-06: Wrote the set/topology/metric method rows into
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`, including finite `len(X)`
  ownership and rejected Sage wrapper/export surfaces. Moved this task to
  needs-review.
- 2026-05-07: Added missing `RealSet.contains(x)` /
  `InternalRealInterval.contains(x)` and `InternalRealInterval.boundary_points()` rows
  to the literal inventory after Gate 2 review found those required seed/source
  surfaces were neither admitted nor rejected/deferred.

## Review Log

### Review 2026-05-07 (Tesla)

**Gates passed:** Gate 1 for existing rows
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** revision-required, then reworked within this card's scope; independent
re-review still required

#### Gate 2 Finding: Missing Real-Subset Literal Surfaces

- The task seed and target spec seed require `boundary_points` and `contains`.
- The sets and topological inventories list `RealSet.contains` and
  `InternalRealInterval.boundary_points` / `contains`.
- The final method rows covered root membership, RealSet Boolean operations,
  `n_components` / `get_interval`, and ambient-relative topology, but did not admit,
  reject, or defer the literal `contains` and `boundary_points` surfaces.

#### Rework

- Added `RealSet.contains(x)` / `InternalRealInterval.contains(x)` as a
  compatibility spelling for root set membership, with `bool` codomain.
- Added `InternalRealInterval.boundary_points()` as a real-line finite-interval
  representation surface, not a general topological boundary object.

### Re-review 2026-05-07 (Avicenna)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- Confirmed the prior Gate 2 gap is resolved: the target inventory now covers
  `RealSet.contains(x)` / `InternalRealInterval.contains(x)` and
  `InternalRealInterval.boundary_points()` with owner, codomain, status, and
  source.
- Confirmed the rows are grounded by `SPEC-MAPPING-SETS.md` and the topological
  Sage inventory.
- Spot-checked that finite `len(X)` is not root `Sets()`, set/subobject/image/
  RealSet rows are present, topology/metric rows are present, and rejected or
  interoperability set surfaces remain represented.

#### Residual Risk

- Review was against local `HEAD` after the row repair and was not a human
  acceptance step.

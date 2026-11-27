---
id: TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Write ring algebra and module method ownership rows
status: complete
priority: critical
owner: Zack
description: Mine ring, algebra, and module inventories into literal method-owner
  rows, preserving base-ring, basis, finite-rank, PID, quotient, and constructor boundaries.
successCriteria:
- The target method-inventory spec contains ring, algebra, module, basis-bearing,
  ordered-generating-set, subobject, quotient, tensor, dual, and hom-constructor method
  tables.
- Basis-dependent methods are not placed on arbitrary modules, and generator methods
  distinguish `WithGenerators`, ordered generators, and bases.
- Algebra constructor and ideal rows split Sage option bags and side strings into
  named mathematical routes.
- Module methods such as rank, dimension, coordinates, support, span, quotient, intersection,
  saturation, tensor, dual, and hom are assigned to minimal owners with hypotheses.
complexity: 78
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Write ring algebra and module method ownership rows

## Summary

Write the literal method-owner rows for rings, algebras, and modules. This task must
produce concrete rows, not another "map methods later" card.

## Source Provenance

- `category_specs/rings/docs/SAGE_INVENTORY.md`
- `category_specs/rings/docs/MAPPING.md`
- `category_specs/algebras/docs/SAGE_INVENTORY.md`
- `category_specs/algebras/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- `category_specs/modules/docs/MAPPING.md`
- Parent plan admitted definition for `WithGenerators` and `FinitelyPresented`.

## Context

The seed rows include:

- rings: `zero`, `one`, characteristic and exactness surfaces where source-backed,
  unit predicates, ideals, quotients, localizations, completions, precision changes,
  p-adic and q-adic routes, polynomial/power-series/matrix-ring constructor surfaces;
- square matrix parents: constructor ownership in `Rings().Constructors()`, algebra
  and module refinements on the returned object, and element constructors such as
  zero matrix, scalar matrix, entries, rows, or existing matrix;
- algebras: `characteristic`, `has_standard_involution`, `algebra_generators`,
  `one`, multiplication, product tensor ownership, subalgebra, left/right/two-sided
  ideals, radical, center, semisimple quotient, idempotent and Peirce surfaces;
- modules: `rank`, `dimension`, `basis`, `gens`, `gen`, `ngens`, coordinate vectors,
  support/coefficient access, ordered-basis methods, `span`, `submodule`,
  `submodule_with_basis`, `intersection`, `saturation`, `quotient_module`,
  `cover`, `relations`, `lift`, `retract`;
- module construction owners: `Subobjects`, `Quotients`, `Subquotients`,
  `CartesianProducts`, `TensorProducts`, `DualObjects`, and `HomCategory`;
- finite-presentation and PID rows: invariant factors, torsion/free parts,
  annihilator, Smith-form data, element order, cyclic submodule primitive predicate;
- rejected or interop-only rows: display, raw representation hooks, random elements
  without a stated distribution, broad coercion plumbing, generic option bags.

## Complexity And Ownership

- Owner/role: category-spec algebra/module spec writer.
- Complexity: `78` (high).
- Rationale: this covers several public category surfaces and known dangerous
  conflations around basis, generators, and free-module element predicates.
- Split/promote note: keep one leaf if it writes one coherent algebra/module table; split
  only if ring, algebra, and module rows need separate spec cards for readability.

## Acceptance Criteria

- [x] The target method-inventory spec contains ring, algebra, module, basis-bearing, ordered-generating-set, subobject, quotient, tensor, dual, and hom-constructor method tables.
- [x] Basis-dependent methods are not placed on arbitrary modules, and generator methods distinguish `WithGenerators`, ordered generators, and bases.
- [x] Algebra constructor and ideal rows split Sage option bags and side strings into named mathematical routes.
- [x] Module methods such as rank, dimension, coordinates, support, span, quotient, intersection, saturation, tensor, dual, and hom are assigned to minimal owners with hypotheses.

## Dependencies And Boundaries

- Do not use Sage wrapper inheritance as owner evidence.
- Do not admit free-module element divisibility from coordinate gcds or chosen
  generators. The sourced formed-element divisibility row belongs to the forms/lattice
  task.
- Do not place `basis()` on modules that only have a generating set.
- Do not make constructor option bags part of public mathematical APIs.

## Work Log

- 2026-05-05: Created as the algebra/module leaf for the literal method ownership inventory phase.
- 2026-05-06: Added ring, algebra, and module method rows to
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`, covering constructor splits,
  matrix-parent ownership, ideals, quotient surfaces, basis and ordered-basis methods,
  Hom/tensor/dual routes, PID finite-presentation rows, graded/Ore/representation
  methods, and rejected interop surfaces. Moved this task to needs-agent-review.
- 2026-05-07: Reworked the algebra row for `has_standard_involution()` after Gate 1
  review found it was unsafe to admit on all `Algebras(R)`. The literal inventory now
  splits `characteristic()` as inherited-only from `has_standard_involution()` as
  decision-needed, and `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]` tracks the
  unresolved quaternion/involutive-algebra owner.

## Review Log

### Review 2026-05-07 (Rawls)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope; independent
re-review still required

#### Gate 1 Finding: `has_standard_involution()` Owner Was Ungrounded

- `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` admitted
  `has_standard_involution()` as an `Algebras(R).ParentMethods` row.
- `SPEC-MAPPING-ALGEBRAS.md` records this predicate as unresolved and warns that the
  checked Sage implementation evidence is quaternion-specific and basis-dependent.
- The row therefore treated a Sage compatibility predicate as generally grounded on
  all `Algebras(R)`, which is not mathematically safe.

#### Rework

- Split the combined `characteristic()` / `has_standard_involution()` row in
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`.
- Kept `characteristic()` as inherited-only from ring/base-ring behavior, not a new
  algebra owner.
- Changed `has_standard_involution()` to `decision-needed` and linked
  `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]`.
- Created `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]` to decide whether the
  owner is a quaternion-algebra refinement, an algebra-with-involution refinement, or
  no public project method yet.

### Re-review 2026-05-07 (Hypatia)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope; independent
re-review still required

#### Gate 1 Finding: Live Algebra Surface Still Admitted The Method

- The inventory and decision card correctly stopped admitting
  `has_standard_involution()` on general `Algebras(R)`.
- `category_specs/algebras/__init__.py` still declared
  `has_standard_involution()` as an abstract method on the general algebra parent
  surface, contradicting the reworked inventory and decision.

#### Rework

- Removed the general `Algebras(R).ParentMethods.has_standard_involution()` abstract
  method from `category_specs/algebras/__init__.py`.
- Left Sage inventory and mapping references intact as source evidence for the
  unresolved decision, not as public project admission.

### Re-review 2026-05-07 (McClintock)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- Confirmed `has_standard_involution()` is not admitted on general `Algebras(R)` in
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`; the row is
  `decision-needed`.
- Confirmed `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]` keeps the method out of
  general `Algebras(R)` until the owner is settled.
- Confirmed the live Python surface no longer declares the method in
  `_AlgebraParentMethods`.
- Exact search `rg -n "has_standard_involution" category_specs src tests -g '*.py'
  -S` found no live Python definition or use under `category_specs`, `src`, or
  `tests`.

#### Residual Risk

- Sage inventory still records the upstream Sage method as source evidence, which is
  intentional and not project admission.
- `[[DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER]]` remains unstarted and must be
  resolved before any public project admission of the method.

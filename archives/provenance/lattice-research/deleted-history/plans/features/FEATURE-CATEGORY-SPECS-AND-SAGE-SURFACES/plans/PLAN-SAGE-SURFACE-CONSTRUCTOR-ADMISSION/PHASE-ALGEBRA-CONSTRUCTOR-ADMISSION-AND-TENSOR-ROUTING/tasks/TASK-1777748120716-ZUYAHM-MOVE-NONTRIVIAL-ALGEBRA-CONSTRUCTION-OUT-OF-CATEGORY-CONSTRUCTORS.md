---
id: TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Move nontrivial algebra construction out of category constructors
status: needs-review
priority: high
description: Move nontrivial algebra construction out of category constructors
successCriteria:
- The card names the canonical source rows that define the algebra-constructor boundary.
- Public algebra category constructors are limited to admitted lightweight routing and
  refinement surfaces, not raw heavy constructors such as Zmod, CyclotomicField,
  NumberField, or generic Sage option bags.
- Free algebra routes are source-category-selected named methods; Sage's generic
  category= disambiguation is not exposed as project API.
- Finite-dimensional algebra construction from tables, matrices, or module-element
  data is routed through TensorAlgebraComponents before
  Algebras(R).Constructors().from_multiplication_tensor.
- Relevant algebra smoke evidence is recorded without weakening mapping decisions or
  smoke obligations.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Move nontrivial algebra construction out of category constructors
Source: pasted backlog 2026-05-02.

Task: move nontrivial algebra construction (Zmod, Cyclotomic, NumberField, etc.) out of category constructors, restrict to lightweight wrapper logic.

## Source Provenance

- Canonical algebra mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-ALGEBRAS.md`.
- Constructor source-category rows in `SPEC-MAPPING-ALGEBRAS` define the admitted public
  routes: `S.free_algebra(R)` for the selected source category routes to named
  constructors such as `free_algebra_from_set`, `free_algebra_from_monoid`,
  `free_algebra_from_group`, and their additive/magma/semigroup variants.
- The same mapping rejects Sage's generic `category=` disambiguation as public project
  API. The source category, not a runtime option bag, chooses the constructor.
- The multiplication tensor section in `SPEC-MAPPING-ALGEBRAS` defines the canonical
  finite-rank algebra constructor:
  `Algebras(R).Constructors().from_multiplication_tensor(multiplication=mu)`, with
  tables, matrices, module-element matrices, and right-multiplication data routed
  first through `TensorAlgebraComponents(R).Constructors()`.
- Implementation surface:
  `category_specs/algebras/__init__.py`, especially the constructor methods on
  `Algebras(R).Constructors()`.

## Grounded Boundary

The executable obligation is not to delete all Sage-backed construction. It is to keep
`Algebras(R).Constructors()` as a category-spec routing/refinement namespace whose
public inputs are mathematically named source objects or canonical tensor objects. Heavy
raw algebra constructors such as `Zmod`, `CyclotomicField`, `NumberField`, generic Sage
option bags, and table/matrix-shaped finite-dimensional algebra calls do not become
public algebra category constructors here. When they are mathematically relevant, they
belong to their own ring/field/source-object owners or to tensor-component interop
before algebra construction.

Admitted algebra constructor routes are therefore:

- true free associative algebra on a finite set of generators, with a recorded
  generator presentation;
- source-category-selected algebra routes from magmas, semigroups, monoids, groups,
  additive semigroups, additive monoids, and additive groups;
- the canonical finite-rank multiplication-tensor route after
  `TensorAlgebraComponents` has converted coordinate/table/matrix data into a tensor
  `mu` with `tensor_type() == (1, 2)`.

## Complexity Justification
- Owner: C77
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Move nontrivial algebra construction out of category constructors
- Why this specific score:
  - This task is high-coupling by design: lifting substantial algebra-construction behavior out of category constructors affects constructor semantics, import layering, and initialization pathways across multiple algebra families (Zmod, Cyclotomic, NumberField).
- Item-specific evidence:
  - The text explicitly calls out nontrivial constructions (`Zmod`, `Cyclotomic`, `NumberField`) and a hard behavior boundary (`lightweight wrapper logic`), which increases migration and compatibility risk.
  - Complexity is validated by expected downstream behavior shifts rather than small typed annotation edits.

## Work Log

- 2026-05-06 implementation review: the current algebra constructor surface does
  not directly construct `Zmod`, cyclotomic fields, number fields, or comparable
  nontrivial algebra parents inside category constructors. It keeps category
  constructors to named routing/refinement logic over Sage-backed objects:
  `FreeAlgebra`, source-category `S.algebra(R, category=...)`, and
  `FiniteDimensionalAlgebra` reached only after tensor-component construction.
  This matches the boundary in `SPEC-MAPPING-ALGEBRAS` that nontrivial raw
  constructor shapes are not public algebra category constructors.
- 2026-05-06 validation: `just --justfile category_specs/justfile smoke-file
  algebras/smoketest.sage` passes. Status moved to `needs-review`; this does
  not mark the card accepted or complete.
- 2026-05-06 Gate 1 rework: after independent review found that the card remained
  backlog-shaped, added source provenance, the grounded algebra-constructor boundary,
  and non-tautological success criteria naming the exact spec rows and owner split.

## Negative Finding

- Searched: `rg -n "Zmod|Cyclotomic|NumberField" category_specs/algebras`;
  `category_specs/algebras/__init__.py`; `SPEC-MAPPING-ALGEBRAS`.
- Found: no direct algebra-constructor implementation route for `Zmod`,
  cyclotomic fields, or number fields in `category_specs/algebras`; the code and
  spec route constructor work through named lightweight Sage-backed routes and
  refinement.
- Conclusion: inference based on the checked algebra subtree and canonical
  mapping spec: the current algebra constructor surface satisfies this card's
  boundary by keeping these heavy constructors out of category constructors.
- Confidence: High.
- Gaps: other subtrees may still mention these constructors for their own module,
  ring, or field surfaces; that is outside this algebra-constructor card.

## Review Log

### Review 2026-05-06 (Beauvoir)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Definition Grounding

- The card body was still grounded only as `Source: pasted backlog 2026-05-02`.
- The success criterion was tautological and did not name the controlling spec rows,
  exact admitted constructor surfaces, or replacement owners for moved behavior.
- The implementation evidence looked directionally consistent with the task intent,
  but Gate 1 failed before later gates mattered.

#### Rework

- Added source provenance for `SPEC-MAPPING-ALGEBRAS`, the source-category constructor
  table, the rejection of Sage `category=` as public API, and the multiplication-tensor
  constructor boundary.
- Replaced the tautological success criterion with concrete acceptance conditions about
  lightweight routing, heavy-constructor exclusion, source-category-selected free
  algebra routes, tensor-component handoff, and non-weakening validation.
- Recorded the grounded executable boundary so future review can check the actual
  implementation against named mathematical owners rather than backlog wording.

### Status correction 2026-05-09

Human feedback clarified that constructor cards must distinguish mathematical owner,
human-facing named-constructor convention, and code-maintenance owner. `Zmod`,
cyclotomic fields, and number fields are conventionally ring/field constructor names,
while aggregate surfaces such as `Cat().Constructors()` may expose the total user
entry point. This card's algebra-subtree finding is agent-reviewable; any broader
named-constructor convention question should be a separate decision, not a reason to
hold this card in `needs-human-input`.

---
trackerStatus:
  type: plan
title: Static category refinement and constructor interception order
status: approved
planId: PLN-CAT-110
planType: spec-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
tags:
- category-specs
- plan
- category-refinement
- constructors
- theme-category-core
- theme-constructor-routing
parentPlan: PLN-CAT-100
---

# Static category refinement and constructor interception order

## Objective

Turn `CATEGORY_REFINEMENT_PHASES.md` into the governing order for category-spec admission: static hierarchy first, concrete interceptors second, top-level constructor redefinitions last.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Admitted Definitions

This plan admits the following ordering rules as source-backed constraints:

- Static hierarchy comes before constructor interception. The mathematical category and
  its method owner must be written explicitly before runtime examples are used to add
  behavior. Source: migrated `CATEGORY_REFINEMENT_PHASES.md` body below.
- Runtime inspection and smoke output are evidence about Sage behavior only. They do
  not define a project category, axiom, constructor, or predicate unless the mapping doc
  records the mathematical owner and hypotheses.
- Constructor interception is local: a concrete method may call the inherited Sage
  method of the same name, then refine the returned parent into the target category.
  Constructor code must not contain hierarchy policy.
- Top-level constructors are last-stage entry points into already specified
  categories; they call Sage once, then refine through the target category.

## Source corpus

- `plans/CATEGORY_REFINEMENT_PHASES.md`
- `plans/category_creation_notes.md`
- `plans/axioms_with_generators_finitely_presented.md`

## Phases

- Static hierarchy and method surface: enumerate mathematical categories and method owners explicitly.
- Concrete category interceptors: refine returned parents only from the correct owner method.
- Top-level constructor redefinitions: call Sage constructors once, then refine through the target category.

## Leaf ownership

This plan records the ordering rule. Domain-specific constructor and signature
cards live under the Sage sprint leaf plans or `SPR-VARIADIC-AUDIT-01KQN9`.

## Acceptance Criteria

- [ ] Runtime discovery is used only as source research, never as the operative spec.
- [ ] Constructor routing never contains hierarchy policy.
- [ ] Every admitted constructor has a mathematical owner and a Sage-source provenance note.


## Migrated Source Bodies

### Former `plans/CATEGORY_REFINEMENT_PHASES.md`

# Category Refinement Phases

## Goal

Build the Sage category refinement surface as a static mathematical spec before
installing behavior.  The category hierarchy is the source of truth.  Runtime
inspection may be used once to learn Sage's existing method names on examples,
but the resulting method lists are recorded explicitly in the spec.

## Constraints

- `Rings` is only a staging namespace so the spec does not clobber
  Sage's `Rings` category during development.
- Subcategories are mathematical categories, not software categories.
- Predicates are mathematical names such as `is_field`, `is_number_field`,
  `is_complete_ring`, and `is_pid`.
- No runtime method discovery, generic routing tables, or exception-driven type
  checks belong in the spec.
- Constructor interception is deferred until the category hierarchy and method
  surfaces are explicit.

## Phase 1: Static Hierarchy And Method Surface

Define the full ring and module subcategory hierarchy first.  For each
subcategory, statically enumerate the relevant existing Sage method names on
`ParentMethods`, `ElementMethods`, or `MorphismMethods`.

Runtime examples may be inspected only as source material.  Once selected, each
method is written into the appropriate subcategory by name.  Methods remain
abstract unless the category itself owns a trivial predicate.

Acceptance:
- `category_specs/rings.py` imports.
- `category_specs/sage_modules.py` imports.
- The category spec files themselves are the reviewed artifact.
- There are no runtime method-list discovery checks or generic routing helpers.

## Phase 2: Concrete Category Interceptors

Replace selected abstract methods with concrete methods only when the
subcategory can reuse an existing same-named Sage implementation through the
MRO.

The implementation pattern is:

```python
result = super().method_name(*args, **kwds)
result._refine_category_(target_category)
return result
```

Methods that do not return rings, ideals, or module parents may remain abstract
as documentation.

Acceptance:
- Concrete methods appear only on the mathematically correct subcategory.
- Each concrete method calls the inherited implementation by the same name.
- Result refinement is local to the method that produced the result.

## Phase 3: Top-Level Constructor Redefinitions

Redefine top-level constructors only after Phase 1 and Phase 2 are stable.
Each redefinition has the same shape:

```python
obj = SageConstructor(*args, **kwds)
obj = TargetCategory(...)(obj)
return obj
```

Constructor redefinitions do not contain hierarchy policy.  The category call
performs refinement into the correct mathematical subcategory.

Acceptance:
- `FreeModule(R, n)` refines through `Modules(R)`.
- Ring constructors refine through `Rings`.
- Constructor code contains no generic routing beyond calling the target
  category.

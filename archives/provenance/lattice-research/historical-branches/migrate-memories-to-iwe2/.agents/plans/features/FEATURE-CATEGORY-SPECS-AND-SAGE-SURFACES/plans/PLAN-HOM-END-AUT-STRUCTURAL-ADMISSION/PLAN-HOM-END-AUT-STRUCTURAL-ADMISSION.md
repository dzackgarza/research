---
id: PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
title: Hom End Aut category objects
status: in-progress
priority: critical
owner: Zack
description: Define Hom_C(X,Y), End_C(X), dual objects, and Aut_C(X) as category
  objects with source-backed Sage realizations and representation machinery kept
  subordinate to those definitions.
successCriteria:
- '`Hom_C(X,Y)`, `End_C(X)`, and `Aut_C(X) = End_C(X)^\times` are stated as category
  objects under explicit hypotheses.'
- Hom objects have domain, codomain, construction, containment, and composition
  semantics; End and Aut inherit their obligations from category membership.
- Public APIs return project Hom, End, Aut, or subobject objects; Sage `ConditionSet`
  remains implementation evidence only.
phases:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Hom End Aut category objects

## Objective

State the mathematical objects
`Hom_C(X,Y)`, `End_C(X) = Hom_C(X,X)`, and
`Aut_C(X) = End_C(X)^\times` first, then record how Sage and project categories
realize them. Dual objects are Hom objects when the mathematical definition is
`M^* = Hom_R(M,R)`.

This plan was reopened on 2026-05-10 after a runtime ownership audit during QC
triage showed that `category_specs.homsets.homsets.HomCategory.parent_class` does
not currently inherit Sage's concrete `sage.categories.homset.Homset` parent methods. The
generic Hom/End/Aut mapping spec records those upstream owners as source inventory.
`TASK-ALIGN-GENERIC-HOMSET-PARENT-OWNERSHIP-WITH-SAGE-RUNTIME` now carries the
project-owned semantic-owner split and is human-gated after fresh-context review.
Remaining runtime MRO proof waits on the Sage import gap; do not treat full-suite mypy
output as evidence for or against these mathematical definitions while the plugin work
is active.


## Grounded Implementation Contract

Source anchors for this plan:

- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/cat/docs/MAPPING.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/lattices/docs/MAPPING.md`

The mathematical target for this plan is:

- `C.HomCategory().Of(A, B)` is `Hom_C(A, B)` with `domain`, `codomain`, construction,
  containment, and composition owned by the hom-category hierarchy.
- `C.EndCategory().Of(A)` is `End_C(A) = Hom_C(A, A)`; it is the endomorphism monoid
  carried by the same hom-object semantics, with extra algebra structure only where the
  module mapping establishes it.
- `C.AutCategory().Of(A)` is `Aut_C(A) = End_C(A)^\times`; it is a group object whose
  elements are invertible endomorphisms in the ambient category.
- `AutCategory.from_end_category` may use Sage `ConditionSet` internally, but the
  public return object is the project Aut or subobject object.
- For formed modules and lattices, `Aut(M, b)` is the orthogonal group because
  form-preserving automorphisms are exactly the invertible endomorphisms in the forms
  category.

Matrix, function, and predicate calculations remain implementation evidence only after
the categorical Hom/End/Aut parent and element meanings above are fixed.

## Reusable Definitions

Hom/End/Aut child cards may use these definitions without re-deriving them:

- `C.HomCategory().Of(A, B)` is the hom object `Hom_C(A, B)` for objects `A, B` of
  `C`; it owns `domain`, `codomain`, identity/zero where valid, and morphism
  construction/containment for the category. Source:
  `category_specs/homsets/docs/MAPPING.md`.
- `C.EndCategory().Of(A)` is `End_C(A) = Hom_C(A, A)`. Domain and codomain are already
  the generic hom-object methods, so subtree aliases such as `base_set()` or
  `base_space()` are migration conveniences, not new definitions. Source:
  `category_specs/homsets/docs/MAPPING.md`.
- `C.AutCategory().Of(A)` is the invertible part of `End_C(A)`. The generic aut
  construction is a project extension over Sage's audited generic homset behavior;
  child work must not duplicate aut construction with raw `ConditionSet` objects.
  Source: `category_specs/homsets/docs/MAPPING.md`.
- For modules, `Hom_R(M,N)` carries `R`-module structure, and `End_R(M)` carries
  algebra structure where the module mapping doc establishes it. For formed modules,
  orthogonal groups are `Aut(M,b)` in the category of modules with forms. Sources:
  `category_specs/modules/docs/MAPPING.md`, `category_specs/forms/docs/MAPPING.md`,
  `category_specs/lattices/docs/MAPPING.md`.

## Structural target

- Hom objects carry module structure where mathematically valid.
- End objects are endomorphism monoids and can specialize to algebra objects.
- Aut objects are groups of invertible endomorphisms in the ambient category.
- Dual objects are connected to Hom objects when `M* = Hom_R(M, R)` is the mathematical meaning.
- Public category operations do not expose raw `ConditionSet` as the final API.

## Owned existing cards

- `spec_01KQN9J3WJE9W76X72DAT10H4Y`: dual-object Hom routing and method ownership.
- `spec_01KQN9J3WQDJ0Z27BXTY67HA72`: DiscriminantGroup Hom/End/Aut standard names.
- `task_1777748120385_rrvdig`: remove raw ConditionSet from public Aut-category objects.

## Acceptance Criteria

- [ ] `Hom_C(X,Y)`, `End_C(X)`, and `Aut_C(X) = End_C(X)^\times` are stated as category objects under explicit hypotheses.
- [ ] Hom objects have domain, codomain, construction, containment, and composition semantics; End and Aut inherit their obligations from category membership.
- [ ] Public APIs return project Hom, End, Aut, or subobject objects; Sage `ConditionSet` remains implementation evidence only.

## Current Mathematical Claim Shape

For a category `C` and objects `X,Y in C`, `Hom_C(X,Y)` is the object or set of
`C`-morphisms from `X` to `Y`. Its elements have domain `X` and codomain `Y`, and
composition is the operation

```text
Hom_C(Y,Z) x Hom_C(X,Y) -> Hom_C(X,Z).
```

`End_C(X) = Hom_C(X,X)` is the endomorphism monoid under composition. If the category
or object supplies additional additive, `R`-linear, finite-generation, presentation, or
matrix-representation structure, those are extra category/refinement claims requiring
the corresponding hypotheses and witnesses.

`Aut_C(X) = End_C(X)^\times` is the group of invertible endomorphisms in `C`. It has
group operations because it is an automorphism group. It does not have generators,
presentations, orbit enumeration, or stabilizer generators unless the same object is
also placed in a stronger category such as finite groups, finitely generated groups,
finitely presented groups, matrix groups with certified generators, or explicitly
generated subgroups.

For formed modules and lattices, `Aut(M,b)` is the subgroup of module automorphisms
that preserve the form `b`; this is the orthogonal group of the formed object. A
candidate element is certified by checking that it is an automorphism in the underlying
module category and preserves the stated bilinear or quadratic form.

## Retired Historical Machinery

The former migrated source bodies about `Homsets`, `Endset`, `Autset`, Sage axiom
registration, representation methods, `ConditionSet` plumbing, and review-log closure
are retired from this active plan. They remain in git history as provenance, not as
instructions and not as source evidence for completing this plan.

A future task may reintroduce a quoted Sage method, category class, or implementation
mechanism only after it first states the mathematical assertion above in the form:

```text
For objects X,Y in category C satisfying hypotheses H,
operation m is defined, has codomain or return object Z,
and requires witness data W.
```

Only after that assertion is visible may the task identify the Sage method or project
wrapper that realizes it.

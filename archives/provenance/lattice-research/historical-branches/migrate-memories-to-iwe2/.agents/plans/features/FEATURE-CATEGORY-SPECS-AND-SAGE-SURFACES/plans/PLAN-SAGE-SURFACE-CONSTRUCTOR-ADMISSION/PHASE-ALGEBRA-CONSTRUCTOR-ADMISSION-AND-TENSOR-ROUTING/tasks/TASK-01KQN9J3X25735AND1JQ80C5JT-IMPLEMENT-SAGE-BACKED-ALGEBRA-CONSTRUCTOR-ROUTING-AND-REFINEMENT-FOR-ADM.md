---
id: TASK-01KQN9J3X25735AND1JQ80C5JT-IMPLEMENT-SAGE-BACKED-ALGEBRA-CONSTRUCTOR-ROUTING-AND-REFINEMENT-FOR-ADM
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Implement Sage-backed algebra constructor routing and refinement for admitted
  constructors
status: complete
priority: high
description: The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ),
  a module hom-category/forms blocker for DualObjects, and constructor admission gaps.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  category-obligation examples or mapping decisions to make failures disappear.
- Relevant category-obligation output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just category-obligation-file algebras/category_obligations.sage after algebra category initialization
  or constructor changes.
- Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module
  over Modules(R).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Implement Sage-backed algebra constructor routing and refinement for admitted constructors
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- `category_specs/algebras/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Implement Sage-backed algebra constructor routing and refinement for admitted constructors from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken category-obligation examples or mapping decisions to make failures disappear.
- [ ] Relevant category-obligation output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just category-obligation-file algebras/category_obligations.sage after algebra category initialization or constructor changes.
- [ ] Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module over Modules(R).

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 implementation review: current `category_specs/algebras/__init__.py`
  implements the admitted Sage-backed constructor routes recorded in
  `SPEC-MAPPING-ALGEBRAS`: true free algebras from finite sets use Sage
  `FreeAlgebra`; magma, semigroup, monoid, group, additive-semigroup,
  additive-monoid, and additive-group routes call Sage `S.algebra(R,
  category=...)` only behind named project constructors; multiplication-table
  construction is centralized through `from_multiplication_tensor(mu)`. The
  implementation explicitly rejects the plain-set `S.algebra(R)` route as an
  algebra constructor and leaves that surface to module construction.
- 2026-05-06 validation: `just --justfile category_specs/justfile category-obligation-file
  algebras/category_obligations.sage` passes after the algebra constructor and tensor
  component refinement work in the linked phase. Status moved to
  `needs-agent-review`; this does not mark the card accepted or complete.

## Review Log

### Review 2026-05-06 (Archimedes)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Definition Grounding

- `free_algebra_from_set(S)` is specified as the free associative unital algebra on a
  generator set `S`, and Sage inventory grounds `FreeAlgebra(R, n, names)` as a free
  algebra on named symbols.
- The implementation used only `S.cardinality()` and Sage names `"x"`, which lost the
  actual generator set and recorded no bijection from elements of `S` to Sage
  generators. Cardinality alone is not enough data for the public constructor
  `free_algebra_from_set(S)`.

#### Rework

- The Sage-backed constructor now takes `tuple(S)` as the finite generator
  presentation, constructs Sage names `x0, x1, ...`, and records the presentation
  witness `tuple(S) -> algebra.gens()` on the returned object.
- `SPEC-MAPPING-ALGEBRAS` now records this as presentation data, not a claim that
  cardinality alone canonically determines the free algebra on `S`.
- `algebras/category_obligations.sage` now checks the recorded generator presentation in addition
  to category membership.

### Re-review 2026-05-06 (Parfit)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before completion

#### Evidence

- Gate 1 prior failure is fixed: `category_specs/algebras/__init__.py` now
  materializes `tuple(generators)`, creates Sage names from that tuple, and records
  `_category_specs_generator_presentation =
  tuple(zip(generator_tuple, algebra.gens(), strict=True))`.
- `SPEC-MAPPING-ALGEBRAS` records the chosen enumeration as presentation data, not a
  claim that cardinality alone canonically determines the free algebra on `S`.
- Plain-set `S.algebra(R)` remains routed to module construction, while
  `Sets.free_algebra` routes through the named project constructor.
- `category_specs/algebras/category_obligations.sage` asserts the generator presentation witness
  and includes that check in the algebra category-obligation example statement.
- Validation observed by the reviewer: `just --justfile category_specs/justfile
  category-obligation-file algebras/category_obligations.sage` passed; targeted diffs and
  `git diff a074be9^ a074be9 --check` were clean.

#### Residual Risks

- The acceptance checkboxes remain unchecked because this is agent review evidence,
  not human acceptance.
- The reviewer searched decided decision cards for algebra/free-constructor
  contradictions and found no evidence of a conflict, but did not exhaustively read
  every decision body line-by-line.

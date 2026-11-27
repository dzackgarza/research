---
id: TASK-1777748120385-RRVDIG-REMOVE-RAW-CONDITIONSET-FROM-PUBLIC-AUT-CATEGORY-SURFACE
trackerStatus:
  type: task
parents:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
dependsOn: []
title: Remove raw ConditionSet from public Aut-category surface
status: complete
priority: critical
description: Remove raw ConditionSet from public Aut-category surface
successCriteria:
- Raw `SageConditionSet` no longer appears as a public aut-object method.
- '`from_end_category` constructors route through a private helper.'
- Public aut-object methods retain the documented `Aut_C(A)` surface.
- The homsets mapping records the private/public boundary.
- Human review accepts the implementation and closes the card.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION
- PHASE-HOM-END-AUT-WORK-QUEUE
---
# Remove raw ConditionSet from public Aut-category surface
Source: pasted backlog 2026-05-02.

Files: category_specs/homsets/autsets.py

Issue: UniversalAutObjectMethods.condition_set() and the from_end_category constructors expose SageConditionSet directly on the public category-spec surface.

Task: replace public condition_set vocabulary with a project-owned subobject/aut-object surface, keep SageConditionSet behind a private helper or implementation bridge, ensure AutCategory().from_end_category(E) returns a project aut/subobject object, and add missing @final markers on the affected concrete aut-object methods.

## Grounded Implementation Contract

- Source anchors:
  - `category_specs/homsets/docs/MAPPING.md`
  - `category_specs/cat/docs/MAPPING.md`
  - `category_specs/modules/docs/MAPPING.md`
  - `category_specs/forms/docs/MAPPING.md`
  - `category_specs/lattices/docs/MAPPING.md`
- Public aut semantics:
  - `C.AutCategory().Of(A)` is the invertible part of `C.EndCategory().Of(A)` and therefore a project-owned aut object with `domain`, `codomain`, identity, inverse, and order semantics.
  - `AutCategory.from_end_category(E)` is the generic construction of that invertible part from the end object `E = End_C(A)`.
- ConditionSet boundary:
  - the homset mapping admits Sage `ConditionSet` only as an implementation bridge for the generic aut construction;
  - the final public return from `from_end_category` and related aut-object helpers must be the project-owned aut/subobject surface, not a bare `SageConditionSet`.
- Forms/lattices consequence:
  - for formed modules, the same aut surface specializes to orthogonal-group semantics `Aut(M, b)`;
  - therefore ConditionSet leakage is not merely cosmetic: it breaks the documented owner chain from generic aut objects to form-preserving automorphism groups.
- Concrete file target:
  - `category_specs/homsets/autsets.py` owns the generic aut construction and any private bridge helpers needed to keep Sage interop internal.

## Complexity Justification
- Owner: C76
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Remove raw ConditionSet from public Aut-category surface
- Why this specific score:
  - This is a migration-level API boundary change in `autsets.py`, touching public category semantics, object construction paths, and return types. Moving `SageConditionSet` off the public surface while preserving behavior through internal bridges creates both compatibility and correctness risk across dependent category-callers.
  - The task also adds invariants (`@final` on concrete aut-object methods), which increases refactor blast radius beyond a local symbol rename.
- Item-specific evidence:
  - The file names exact touch points (`condition_set`, `from_end_category`, `aut/subobject` surface) and a single authoritative target file, `category_specs/homsets/autsets.py`.
  - Complexity is driven by explicit public/private contract reshaping rather than a single implementation edit.

## Implementation Result

- Removed `UniversalAutObjectMethods.condition_set()` from the public aut-object
  surface.
- Centralized raw `SageConditionSet` construction in the private
  `_aut_object_from_end_category(...)` bridge.
- Kept public aut objects on the project surface through `AutCategory.from_end_category`,
  `AutCategoryConstruction.from_end_category`, and `AutCategoryOf.from_end_category`.
- Marked the concrete aut-object methods `end_category`, `domain`, `codomain`, and
  `identity` as final; `domain`, `codomain`, and `identity` explicitly override the
  generic hom/end object contracts.
- Updated `category_specs/homsets/docs/MAPPING.md` to state that raw `ConditionSet` is
  private implementation backing and that public aut objects expose `end_category()`
  rather than `condition_set()`.
- Reworked the constructor path after review: raw `SageConditionSet` construction now
  lives in a distinct private bridge, while `_aut_object_from_end_category(...)`
  refines that backing object into the project aut category before returning it.
- Added homsets category assertions for `from_end_category` returning an Aut object and
  for the public Aut object exposing `end_category` rather than `condition_set`.
- `just --justfile category_specs/justfile category-obligation-file homsets/category_obligations.sage` passed
  with exit code 0.

## Acceptance Criteria

- [x] Raw `SageConditionSet` no longer appears as a public aut-object method.
- [x] `from_end_category` constructors route through a private helper.
- [x] Public aut-object methods retain the documented `Aut_C(A)` surface.
- [x] The homsets mapping records the private/public boundary.
- [ ] Human review accepts the implementation and closes the card.

## Review Log

### Review 2026-05-06 (Noether)

**Gates passed:** Gate 1 Definition Grounding
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 2 Finding: Acceptance Criteria

- The card and parent plan require final public returns to be project-owned
  aut/subobject surfaces, with Sage `ConditionSet` only as localized interop backing.
- `_aut_object_from_end_category(...)` still returned `SageConditionSet(...)`
  directly, and public constructors returned that helper result.
- The reviewer identified the set-subobject construction path as the model: construct
  a condition-backed object internally, then refine the returned public object into
  the project-owned subobject category surface.

#### Rework

- Split raw Sage construction into `_condition_aut_object_from_end_category(...)`.
- Kept `_aut_object_from_end_category(...)` as the public helper used by
  `from_end_category(...)`, but now it refines the condition-backed object into the
  requested project aut category before returning it.
- Added targeted homsets category-obligation example coverage for the public Aut object surface.
- `just --justfile category_specs/justfile category-obligation-file homsets/category_obligations.sage` passed
  with exit code 0.

### Re-review 2026-05-06 (Fermat)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- The prior Gate 2 public-surface leak is fixed: raw `SageConditionSet(...)` now lives
  only in `_condition_aut_object_from_end_category(...)`, and the public
  `_aut_object_from_end_category(...)` refines that backing object with
  `refine_category(..., [aut_category])`.
- `SPEC-MAPPING-HOMSETS.md` grounds the boundary: raw `ConditionSet` is implementation
  detail, while public aut objects expose `end_category()`, `domain()`, `codomain()`,
  and `identity()`, not `condition_set()`.
- `just --justfile category_specs/justfile category-obligation-file homsets/category_obligations.sage` exited 0.

#### Residual Risks

- The underlying implementation object is still Sage `ConditionSet` by design; raw
  Python type introspection will still reveal the backing class.
- Full category-spec category-obligation example still fails in unrelated posets and rings category-obligation example files, so
  this review supports only the Hom/End/Aut card and not a global phase transition.

---
title: Object Method Resolution Goal State
status: active-correction
tags: [goal-state, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Goal State

## Preserved Object

This note preserves the corrected category-spec model for object-method resolution:
`ParentMethods` abstract methods are mathematical object-method obligations, refinement
declares category view, and category-obligation examples expose gaps between current
implementations and the spec.

## Current Mode

`ACTIVE-CORRECTION`: the previous ABC-boundary state treated refinement as an
enforcement or validation boundary. That model is invalid for this repo.

Do not use the prior generated-body/assert patch, refinement-rejection tests, or
"strict enforcement" language as design evidence. They record a failed local objective
frame, not the semantics of `category_specs`.

## Corrected Repo Model

The governing facts are:

- `category_specs` is specification work inside Sage's category/object universe.
- Project specs state mathematical obligations Sage did not know.
- Refined Sage objects are expected to be partial relative to those specs.
- `refine_category(X, C)` declares that `X` is to be regarded as an object of `C`.
- Refinement imposes the category contract conceptually; it does not validate
  satisfaction.
- Refinement must not interrogate the object for method satisfaction.
- Refinement must not reject because project abstract methods remain.
- Category-obligation examples instantiate or exercise category objects to expose
  implementation gaps.
- Missing methods after refinement are expected gap evidence, not refinement failures.
- ABCMeta may be used only to represent project abstract methods faithfully in Python's
  class system and MRO.
- Concrete Sage/project methods satisfy obligations only by ordinary lookup.
- Missing obligations remain abstract/visible for category-obligation examples and later
  implementation work.

## Invalidated Prior State

The following prior state claims are invalid for future work:

- "invalid refined Sage objects cannot enter project categories";
- "`refine_category` rejects unresolved obligations before mutating the parent";
- "strict enforcement exposes root ring-surface obligations";
- "failed refinement is atomic" as an acceptance criterion for abstract method gaps;
- checking `__abstractmethods__` as a refinement blocker;
- generated missing-obligation bodies as an enforcement substitute;
- accepting or rejecting ABC strategies based on raw Sage refinement rather than the
  project-owned category/refinement/constructor pathway.

Tests, commits, and reports built around those claims are historical evidence of the
misframed attempt. They are not acceptance criteria for the corrected spec model.

## Valid Direction

The viable local strategy remains structural:

- project-owned category base wrappers may construct project `parent_class` objects
  through dynamic metaclasses that minimally compose Sage's dynamic metaclasses with
  `ABCMeta`;
- all non-ABC dynamic behavior should defer to Sage's existing mechanisms;
- project abstract methods should participate in normal Python abstractmethod/MRO
  behavior;
- no project code should manually compute satisfaction, subtract abstract names,
  special-case method names, or generate call-time failure bodies;
- `refine_category` should stay a declaration mechanism, not become a validator.

## Next Pickup

Repair source and tests against the corrected model:

- remove or replace refinement-time abstract-method rejection logic;
- replace adversarial tests that assert rejection before `refine_category` returns with
  tests that prove refinement declares the category contract and category-obligation
  examples expose missing implementations;
- preserve tests proving generated bodies, `assert False`, cache priming, source-shape
  checks, and name special-casing are invalid substitutes for abstract spec structure;
- keep root `Rings().Constructors().ZZ()`/`QQ()` obligations visible as implementation
  gaps unless separate source work actually supplies them.

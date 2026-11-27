---
id: TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES
trackerStatus:
  type: task
parents:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
dependsOn:
- '[[TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES]]'
title: Ground set-wrapper private-slot shape probes
status: complete
priority: high
description: Source-audit the remaining private-slot and optional-attribute probes
  in set-wrapper one-object categories, then either document them as Sage wrapper
  boundaries or replace them with source-backed type, category, or accessor dispatch.
successCriteria:
- Sage docs/source for integer ranges, callable-backed enumerated sets, and recursively
  enumerated sets are read before editing implementation code.
- Each remaining probe in `integer_range.py`, `enumerated_from_iterator.py`, and `recursively_enumerated.py`
  is classified as documented Sage wrapper storage or invalid object-shape dispatch.
- Invalid probes are replaced with source-backed Sage/project type checks, category
  predicates, or named wrapper/accessor boundaries.
- Public mathematical specs, category-obligation examples, and abstract obligations are not weakened to
  make the implementation pass.
complexity: 55
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-OBLIGATION-EXAMPLES
- PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT
---
# Ground set-wrapper private-slot shape probes

## Summary

Source-audit the remaining private-slot and optional-attribute probes in set-wrapper
one-object categories, then either document them as Sage wrapper boundaries or replace
them with source-backed type, category, or accessor dispatch.

## Source Provenance

- Parent audit:
  `TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES`.
- Style policy: `.agents/skills/category-spec-style/references/style.md`, especially
  the no-duck-typing rule and the preference for real type/category dispatch.
- Affected implementation surfaces:
  `category_specs/sets/subcategories/integer_range.py`,
  `category_specs/sets/subcategories/enumerated_from_iterator.py`, and
  `category_specs/sets/subcategories/recursively_enumerated.py`.
- Required Sage source/doc surfaces: Sage integer ranges, callable-backed enumerated
  sets, and recursively enumerated forest/set implementations.

## Context

The first duck-type audit pass found that these set-wrapper files inspect private Sage
storage such as `_middle_point`, `_end`, `_cache`, `_args`, `_kwds`, `_max_depth`,
`_roots`, and `_seeds`, or probe for `successors`. These may be legitimate wrapper
boundaries if Sage defines those storage variants as part of the concrete class family,
but that must be grounded in source before the project treats them as acceptable.

This card is intentionally separate from the initial static audit. The remediation may
need Sage source reading and may reveal that the right replacement is a named project
wrapper accessor rather than an immediate local rewrite.

## Complexity And Ownership

- Owner role: set-wrapper audit/implementation worker.
- Complexity: 55, moderate band.
- Rationale: the scope is confined to three related set-wrapper surfaces, but the correct
  fix depends on Sage source details and should not be guessed from private attribute
  names.

## Acceptance Criteria

- [x] Sage docs/source for integer ranges, callable-backed enumerated sets, and
  recursively enumerated sets are read before editing implementation code.
- [x] Each remaining probe in `integer_range.py`, `enumerated_from_iterator.py`, and
  `recursively_enumerated.py` is classified as documented Sage wrapper storage or invalid
  object-shape dispatch.
- [x] Invalid probes are replaced with source-backed Sage/project type checks, category
  predicates, or named wrapper/accessor boundaries.
- [x] Public mathematical specs, category-obligation examples, and abstract obligations are not weakened to
  make the implementation pass.

## Source Audit Result

- `integer_range.py`: Sage source defines `IntegerRangeFinite`,
  `IntegerRangeInfinite`, `IntegerRangeFromMiddle`, and `IntegerRangeEmpty` as concrete
  class variants. The project wrapper now dispatches by those Sage types and delegates
  containment to the Sage owner instead of probing `_middle_point` or `_end`.
- `enumerated_from_iterator.py`: Sage source defines `_func`, optional `_args` and
  `_kwds`, and optional `_cache` as storage for `EnumeratedSetFromIterator`; Sage
  already owns `__iter__` and `clear_cache`. The project wrapper now delegates to the
  Sage class methods instead of repeating private-slot logic.
- `recursively_enumerated.py`: Sage source defines generic recursive sets with
  `seeds()`, a documented `successors` attribute, and `_max_depth`; forest recursive
  sets have a `roots()` method. The project wrapper now uses Sage generic/forest type
  boundaries and public Sage methods where available, leaving the bounded-depth
  evidence as a source-backed generic-wrapper boundary.

## Dependencies And Boundaries

- Do not change unrelated set constructors, category assertions, or mathematical method
  ownership.
- Do not replace Sage internals merely because they use private storage; first determine
  whether this project is at a documented wrapper boundary.
- If Sage source shows multiple concrete object families with different semantics, split
  those families into separate owner cards rather than normalizing them through one
  broad helper.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete/done

#### Evidence

**Gate 1 — Definition Grounding:**
- Source provenance cites the parent audit task and affects 3 implementation surfaces: `integer_range.py`, `enumerated_from_iterator.py`, `recursively_enumerated.py`.
- Each probe classified in the source-audit result section traces to Sage source analysis:
  - `IntegerRangeFinite`/`Infinite`/`FromMiddle`/`Empty` classes documented in Sage source.
  - `EnumeratedSetFromIterator._func/_args/_kwds/_cache` documented Sage storage.
  - `recursively_enumerated_set.pyx` seeds/successors/max_depth documented as generic/forest type boundaries.
- Style policy cited from `.agents/skills/category-spec-style/references/style.md`.

**Gate 2 — Acceptance Criteria:**
- [x] Sage docs/source for integer ranges, callable-backed enumerated sets, and recursively enumerated sets are read before editing → Source Audit Result documents Sage class/type findings for all three surfaces.
- [x] Each remaining probe classified as documented Sage wrapper storage or invalid dispatch → integer_range.py: Sage type dispatch instead of `_middle_point`/`_end` probes; enumerated_from_iterator.py: delegation to Sage class methods; recursively_enumerated.py: Sage generic/forest type boundaries with bounded-depth wrapper boundary.
- [x] Invalid probes replaced with source-backed type checks, category predicates, or named wrapper/accessor boundaries → all three files updated with explicit Sage type dispatch or delegation.
- [x] Public mathematical specs, category-obligation examples, and abstract obligations are not weakened → no spec or category-obligation example changes were made; only implementation details in wrapper files.

**Gate 3 — Spec-Weakening:**
- No staged or unstaged diffs on spec files or category-obligation example files. Changes are limited to the 3 implementation files.
- No abstract methods, constructor obligations, or category assertions deleted.

**Gate 4 — Gradient:**
- No decision cards are contradicted. The duck-type-to-category-dispatch direction follows the established category-spec-style policy.
- No previously passing category-obligation examples regressed.

**Gate 5 — Mathematical Correctness:**
- The task is implementation-hygiene, not mathematical claim verification. Replacing private-slot probes with Sage type dispatch is mechanically correct for the documented Sage class structures.
- No mathematical claims are altered.

**Gate 6 — Style and Compliance:**
- No raw ConditionSet, variadic option bags, or AI-slop patterns.
- Style policy rule against duck-typed private-attribute dispatch is followed.
- `just plan-validate` passes.

#### Residual Risks
- The bounded-depth evidence in `recursively_enumerated.py` is left as a source-backed generic-wrapper boundary; future Sage version changes to recursive-set internals may require updates.

---

## Work Log

- 2026-05-06: Created from the duck-type object-shape audit after local fixes handled
  `Sets().__contains__` and `Cat().Subobjects().__contains__`, while set-wrapper
  private-slot cases remained source-dependent.
- 2026-05-06: Read installed Sage source for `sage.sets.integer_range`,
  `sage.sets.set_from_iterator`, and `sage.sets.recursively_enumerated_set.pyx`. Replaced
  local optional attribute probes with Sage type/delegate boundaries and recorded the
  classification above. No public specs, category-obligation examples, or abstract obligations were weakened.

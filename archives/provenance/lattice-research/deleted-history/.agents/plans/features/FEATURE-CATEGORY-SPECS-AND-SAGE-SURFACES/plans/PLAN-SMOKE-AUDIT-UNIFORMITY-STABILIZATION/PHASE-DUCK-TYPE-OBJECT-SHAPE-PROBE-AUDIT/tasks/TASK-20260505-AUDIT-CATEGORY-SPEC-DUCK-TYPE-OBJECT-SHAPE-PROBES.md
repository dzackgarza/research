---
id: TASK-20260505-AUDIT-CATEGORY-SPEC-DUCK-TYPE-OBJECT-SHAPE-PROBES
trackerStatus:
  type: task
parents:
- '[[PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT]]'
dependsOn: []
title: Audit category-spec duck-type object-shape probes
status: complete
priority: critical
description: Audit category-spec implementation code for `getattr`, `hasattr`, optional
  attribute fallbacks, and private-slot probes that infer object shape instead of
  matching real Sage/project types, documented wrappers, or category membership.
successCriteria:
- Scan `category_specs/` implementation files for `getattr`, `hasattr`, optional attribute
  fallback, and private-slot probe patterns.
- For each finding, record whether the branch is Sage interop, a documented wrapper
  boundary, real category/type dispatch, or invalid duck-type probing.
- Replace invalid probes with real Sage/project type checks, category membership/subcategory
  checks, or named wrapper/accessor boundaries when the fix is local and source-backed.
- Split any nonlocal or mathematically ambiguous remediation into owner-scoped follow-up
  cards instead of guessing inside the audit.
- Do not weaken smokes or add broad exception-catching to hide the audit finding.
complexity: 60
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
- PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT
---
# Audit category-spec duck-type object-shape probes

## Summary

Audit category-spec implementation code for `getattr`, `hasattr`, optional attribute
fallbacks, and private-slot probes that infer object shape instead of matching real
Sage/project types, documented wrappers, or category membership.

## Source Provenance

- Owning sprint: `PHASE-DUCK-TYPE-OBJECT-SHAPE-PROBE-AUDIT`.
- Parent audit plan: `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`.
- Repo style policy: `.agents/skills/category-spec-style/references/style.md`.
- Proof-audit warning:
  `.agents/skills/research-proof-auditing/references/proof-auditing.md`.
- Lattice interface audit guidance:
  `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`.
- Triggering observation: 2026-05-05 smoke implementation exposed `getattr`/`hasattr`
  patterns in category-spec set wrappers; the user directed that this be left to a
  real audit phase rather than fixed opportunistically inside the active smoke card.

## Context

Duck-type object-shape probes are dangerous in category-spec code because they make
mathematical dispatch depend on storage accidents. The audit should distinguish
between legitimate Sage interop machinery and project code that should instead use
source-backed type checks, explicit wrapper classes, named accessors, or category
membership/subcategory predicates.

## Complexity And Ownership

- Owner role: category-spec audit worker, with parent-agent review.
- Complexity: 60, moderate band.
- Rationale: the first pass is a bounded static audit across category-spec implementation
  surfaces plus classification. Remediation may touch several files, but independent
  owner surfaces should be split rather than handled as one broad rewrite.

## Acceptance Criteria

- [x] Scan `category_specs/` implementation files for `getattr`, `hasattr`, optional
  attribute fallback, and private-slot probe patterns.
- [x] For each finding, record whether the branch is Sage interop, a documented wrapper
  boundary, real category/type dispatch, or invalid duck-type probing.
- [x] Replace invalid probes with real Sage/project type checks, category
  membership/subcategory checks, or named wrapper/accessor boundaries when the fix is
  local and source-backed.
- [x] Split any nonlocal or mathematically ambiguous remediation into owner-scoped
  follow-up cards instead of guessing inside the audit.
- [x] Do not weaken smokes or add broad exception-catching to hide the audit finding.

## Static Audit Result

- `category_specs/cat/base_category_types.py`: constructor forwarding, provider
  assembly, predicate validation, and Sage axiom descriptor interop. Classified as
  documented Sage/project wrapper boundary or real category dispatch. Source grounding:
  `CategoryWithAxiom`, `CategoryWithAxiom_singleton`, and
  `CategoryWithAxiom_over_base_ring` define `ambient_category()` as `base_category()`
  and `defining_predicates()` through `_declared_defining_predicates()` plus
  `_validate_defining_predicates()`, which checks that every predicate is exposed on
  the ambient category's parent class and on the local `ParentMethods`.
- `category_specs/cat/subcategories/constructions/subobjects.py`:
  `Subcategories.__contains__` is grounded as a wrapper-boundary check, not a duck-type
  shape probe. It first requires membership in project `Cat()`, whose
  `category_specs/cat/__init__.py` boundary accepts Sage category objects by checking
  `candidate.category().is_subcategory(Cat())` and accepts Sage join-category objects
  through the documented join wrapper. It then matches the three project axiom-wrapper
  bases that expose the required `ambient_category()` and `defining_predicates()`
  contract. The Sage source basis is
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category_with_axiom.py`:
  `CategoryWithAxiom` is the Sage base for categories obtained by adding an axiom to a
  base category, its `__init__` stores `_base_category`, and Sage's axiom test expects
  the singleton and base-ring variants when the base category has those shapes.
- `category_specs/sets/__init__.py`: root `Sets().__contains__` used optional
  `category` lookup. Replaced with the real Sage `Parent` type boundary plus Sage
  category membership. Source grounding:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/structure/parent.pyx`
  defines `Parent.category()` to return the initialized Sage category, defaulting to
  `Sets()` when missing, and `_test_category()` asserts that a parent category is a
  subcategory of Sage `Sets()`. Sage
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category.py`
  defines `Category.is_subcategory(c)` as the natural-forgetful-functor relation,
  implemented by the category supercategory set/hook. The project `Sets` docstring
  states that objects are Sage parents lying in `SageSets()`.
- `category_specs/sets/__init__.py`: root `_SetObjectMethods._element_constructor_`
  uses `hasattr(self, "element_class")`. Classified as Sage element-constructor
  interop, not mathematical object-shape dispatch. Source grounding:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/sets_cat.py`
  defines Sage `Sets.ParentMethods._element_constructor_` by the same
  `element_class` branch and routes it to
  `_element_constructor_from_element_class`, which constructs
  `self.element_class(self, *args, **keywords)`. Sage
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/structure/parent.pyx`
  defines `Parent.element_class` as the dynamic parent/category element class built
  from the parent's `Element` class and the category's abstract element class. The
  project branch is therefore a local restatement of Sage's element-constructor
  boundary for set parents, not an attempt to infer whether an arbitrary mathematical
  object has some optional storage shape.
- `category_specs/sets/subcategories/image.py`: local `ImageSubobject` wrapper probes
  Sage backing storage. Classified as documented Sage-wrapper storage only because
  Sage
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/image_set.py`
  defines `ImageSubobject` as the image of a map on a domain subset, stores
  `self._domain_subset = domain_subset` in `__init__`, and uses `_domain_subset` inside
  `_element_constructor_()` to validate inverse-image membership. The project wrapper
  still delegates general membership to `_element_constructor_()`; the `_domain_subset`
  read is restricted to the finite-domain enumeration shortcut and should not become a
  general pattern for unrelated wrappers.
- `category_specs/sets/subcategories/integer_range.py`,
  `category_specs/sets/subcategories/enumerated_from_iterator.py`, and
  `category_specs/sets/subcategories/recursively_enumerated.py`: private-slot and
  optional-attribute probes require Sage source grounding before rewrite. Routed to
  `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES`.
- `category_specs/utils.py`: class/module and abstract-method inspection. Classified
  as project validation boundary, not mathematical object-shape dispatch.

## Dependencies And Boundaries

- This card belongs to the audit phase and should not block ordinary approved smoke
  implementation cards unless a duck-type probe is the direct cause of the active
  failure being fixed.
- Do not replace Sage internals or documented Sage dispatch mechanics merely because
  they contain `getattr`/`hasattr`; classify those separately.
- Do not use this card to perform unrelated typing cleanup, formatter normalization, or
  API redesign.

## Validation Requirements

- Run a targeted static search showing remaining `getattr`/`hasattr` patterns and their
  classifications.
- Run the narrowest relevant category-spec smoke or static checks for files changed by
  local remediations.
- If validation is skipped because this card only routes findings, record that clearly
  in the work log.

## Review Findings

- 2026-05-06 parent-agent review failed Gate 1, definition grounding. The audit recorded
  classifications by file, but not by each probe or branch with source-grounded
  evidence.
- The `CategoryWithAxiom` wrapper-boundary claim must cite the exact project/Sage
  source definitions and hypotheses for `ambient_category`, `defining_predicates`, and
  the completeness of the wrapper class boundary.
- The `Sets().__contains__` replacement must cite the Sage/project source defining the
  `Parent` plus Sage-category-membership object boundary.
- The `ImageSubobject` private-storage probe must record the source-grounded storage
  and interop contract before it can be accepted as a documented wrapper boundary.
- Recommended status is `revision-required`, not `blocked`: the failed review is
  fixable inside this leaf and does not exhaust the DAG frontier.
- 2026-05-06 follow-up resolved the grounding gap by recording source anchors for each
  disputed branch. The card is back in `needs-agent-review`; it is not accepted or complete.
- 2026-05-06 independent re-review failed Gate 1 again because
  `_SetObjectMethods._element_constructor_` still had an unclassified
  `hasattr(self, "element_class")` probe. This is fixable in-card, so the outcome is
  `revision-required`, not `blocked`.
- 2026-05-06 follow-up resolved the second Gate 1 finding by recording Sage
  `Sets.ParentMethods._element_constructor_` and `Parent.element_class` as the source
  boundary for that branch. The card is back in `needs-agent-review`; it is not accepted or
  complete.
- 2026-05-06 independent re-review passed Gates 1-6. The reviewer confirmed that all
  known `getattr`/`hasattr`/private-slot probes are now classified or routed, including
  `_SetObjectMethods._element_constructor_`; nonlocal set-wrapper cases are routed to
  `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES`; no spec/smoke
  weakening or negative backsliding was found. Residual risk: full `just test` still
  lacks a clean signal because repo-wide mypy currently fails on broad existing
  Sage/stub/type errors.

## Review Log

### Re-review 2026-05-06 (independent audit)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before completion

#### Evidence

- The static audit classifies each known `getattr`/`hasattr`/private-slot probe as
  Sage interop, documented wrapper boundary, real category/type dispatch, or routed
  follow-up work.
- Remaining `category_specs/` implementation matches for `getattr(` and `hasattr(`
  are the Cat wrapper machinery, Sage `element_class` constructor interop, project
  utility validation, OS process interop, and the source-grounded `ImageSubobject`
  finite-domain shortcut.
- Nonlocal set-wrapper private-slot remediation is split to
  `[[TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES]]` rather than guessed
  inside this audit card.
- No smoke assertions, abstract obligations, or public mathematical specs were
  weakened by the audit follow-ups.

#### Residual Risks

- Full `just test` does not yet provide a clean signal because repo-wide mypy still
  fails on broad existing Sage/stub/type errors.
- The acceptance checkboxes remain checked from the implementation pass, but this
  review entry is not human acceptance or card closure.

## Work Log

- 2026-05-05: Created from user correction and routing decision. This card exists so
  duck-type object-shape probing is audited deliberately during `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`, not
  opportunistically inside unrelated smoke implementation work.
- 2026-05-06: Ran static searches for `getattr`, `hasattr`, optional fallbacks, private
  slots, and `try`/attribute fallback patterns under `category_specs/`. Fixed the two
  local invalid implementation probes in `Cat().Subobjects().__contains__` and
  `Sets().__contains__`. Left source-dependent set-wrapper private-slot cases to
  `TASK-20260506-GROUND-SET-WRAPPER-PRIVATE-SLOT-SHAPE-PROBES` instead of guessing.
  No smoke assertions or spec obligations were weakened.
- 2026-05-06: Parent review moved this card to `revision-required` because the recorded
  classifications are not yet source-grounded at probe/branch granularity.
- 2026-05-06: Added probe/branch-level source grounding for the Cat axiom-wrapper
  boundary, the Sage `Parent`/`Sets()` membership boundary, and Sage
  `ImageSubobject` backing storage. Moved the card back to `needs-agent-review` for human
  review. Spec-weakening review: this follow-up changed only this tracker card; it did
  not delete abstract methods, narrow smokes, remove constructor obligations, or move
  any spec surface.
- 2026-05-06: Added source-grounded classification for
  `_SetObjectMethods._element_constructor_` and its Sage `element_class` interop
  branch after independent review caught the omission. This follow-up changed only this
  tracker card; it did not delete abstract methods, narrow smokes, remove constructor
  obligations, or move any spec surface.
- 2026-05-06: Recorded the independent re-review pass. The card remains
  `needs-agent-review` pending human acceptance; it is not marked complete.

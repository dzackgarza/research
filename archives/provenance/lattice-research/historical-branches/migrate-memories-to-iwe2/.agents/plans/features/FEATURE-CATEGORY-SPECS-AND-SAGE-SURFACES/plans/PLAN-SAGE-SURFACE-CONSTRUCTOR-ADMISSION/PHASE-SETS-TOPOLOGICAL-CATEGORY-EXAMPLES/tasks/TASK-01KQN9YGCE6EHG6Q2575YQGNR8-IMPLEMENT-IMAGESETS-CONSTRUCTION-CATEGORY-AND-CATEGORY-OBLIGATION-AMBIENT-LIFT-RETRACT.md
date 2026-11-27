---
id: TASK-01KQN9YGCE6EHG6Q2575YQGNR8-IMPLEMENT-IMAGESETS-CONSTRUCTION-CATEGORY-AND-CATEGORY-OBLIGATION-AMBIENT-LIFT-RETRACT
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES]]'
dependsOn: []
title: Implement ImageSets construction category and category-obligation example ambient lift retract and
  image-subobject membership
status: complete
priority: high
description: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  category-obligation examples or mapping decisions to make failures disappear.
- Relevant category-obligation output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES
---
# Implement ImageSets construction category and category-obligation example ambient lift retract and image-subobject membership
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Implement ImageSets construction category and category-obligation example ambient lift retract and image-subobject membership from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Review Log

### Review - 2026-05-07 (gap found and repaired; see below)

#### Gate 2 Finding (from prior review)

The initial category-obligation example lacked ambient/lift/retract coverage. Fixed by adding a focused category-obligation example witness. This finding is resolved.

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence

**Gate 1 — Definition Grounding:**
- Source provenance cites `category_specs/sets/docs/MAPPING.md` as the canonical source for image-subobject, ambient/lift/retract, and constructor routing surfaces.
- Implementation commit `983a058` routes through typed `Sets().Constructors().ImageSubobject(f, domain_subset)` with refinement through ImageSets, subobjects, and subquotients.

**Gate 2 — Acceptance Criteria:**
- [x] Implementation changes only scoped surface and does not weaken category-obligation examples → verified: no category-obligation example changes beyond the ambient/lift/retract additions; the prior Gate 2 gap (missing category-obligation example for ambient/lift/retract) was repaired.
- [x] Relevant category-obligation output updated → category-obligation example passes exit 0 with ambient/lift/retract assertions.
- [x] Project category vocabulary used → ImageSubobject, ImageSets, subobjects/subquotients are project category surfaces, not Sage fallback names.
- [x] Exact mapping row cited → `ImageSubobject(f, domain_subset)` routes through the MAPPING.md image-subobject surface.
- [x] No generic Sage Set(X) exposed as public constructor → verified: the constructor is the typed project route.

**Gate 3 — Spec-Weakening:**
- `git diff --cached` and `git diff` show no changes to set spec files, category-obligation example files, or mapping docs.
- The prior Gate 2 finding was repaired by adding category-obligation example coverage, not by removing obligations.

**Gate 4 — Gradient:**
- No decision cards contradicted.
- Sets category-obligation example passes with same exit 0 as baseline.
- The Sage `Set(X)` exclusion follows the established spec-surface hygiene rule.

**Gate 5 — Mathematical Correctness:**
- Image subobject semantics are correct: `ImageSubobject(f, domain_subset)` constructs the image of `f` restricted to a subset of its domain, with `ambient()` returning the codomain set and `lift()`/`retract()` providing the subobject morphism pair.
- Implementation is source-grounded in the sets MAPPING.md image-subobject rows.

**Gate 6 — Style and Compliance:**
- No raw ConditionSet, variadic option bags, or AI-slop patterns.
- `git diff --check` passed per commit evidence.
- `just plan-validate` passes.

#### Residual Risks
- None identified in the reviewed scope.



## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken category-obligation examples or mapping decisions to make failures disappear.
- [x] Relevant category-obligation output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Commit `983a058` completed the category-obligation example-facing ImageSubobject implementation
  against the `category_specs/sets/docs/MAPPING.md` image-subobject rows: the constructor
  remains the typed `Sets().Constructors().ImageSubobject(f, domain_subset)` route,
  the result refines through `ImageSets`, subobjects, and subquotients, and finite image
  subobjects now recover membership and cardinality in the Sets category-obligation example without exposing
  generic Sage `Set(X)` as a public constructor.
- 2026-05-05: Validation evidence from `983a058`: `just --justfile
  category_specs/justfile category-obligation-file sets/category_obligations.sage` passed; `just --justfile
  category_specs/justfile check-abstract-redefinitions` passed; `git diff --check`
  passed. This card is moved to `in-review`; human acceptance is still required for
  closure.

## Review Log

### Review - 2026-05-07

Outcome: review gap found and repaired; card remains `needs-agent-review` for a fresh review
and human acceptance.

- Gate 2 initially lacked direct category-obligation example evidence for the ambient/lift/retract part of
  the card title. The existing category-obligation example covered finite-image membership and cardinality
  for a Python callable whose Sage codomain is `None`.
- Added a focused category-obligation example witness using a set morphism
  `IntegerRange(3) -> IntegerRange(5)` so `ImageSubobject.ambient()` is a real
  codomain rather than Sage's callable fallback.
- Added category assertions for `ambient()`, `lift()`, and `retract()` on that codomain
  witness while preserving the existing membership/cardinality assertions.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance

**Gates failed:** none

**Outcome:** complete. All six gates pass.

- Gate 1: SPEC-MAPPING-SETS.md lines 304-325 document ImageSubobject admission. Implementation follows spec exactly.
- Gate 2: All 5 ACs satisfied. Project vocabulary used (ImageSubobject, ImageSets).
- Gate 3: Zero changes to spec files. No abstract methods removed. Prior gap repaired by adding assertions.
- Gate 4: Set(X) exclusion preserved. Category-obligation example passes.
- Gate 5: ImageSubobject = {f(x) | x in domain_subset} correct. Fixed Sage __eq__ identity bug.
- Gate 6: @override/@final used. Type annotations.

Verification: just category-obligation-file sets/category_obligations.sage passes.

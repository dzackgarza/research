---
id: TASK-AUDIT-SETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-SETS]]'
title: Audit Sets hom mapping for mirrored Sage homset surfaces
status: complete
priority: high
description: Audit `category_specs/sets/homsets.py` and the Sets mapping/spec surface so
  retained Sage homset/container methods such as identity, zero-like constructors,
  and image-list construction paths are explicitly mirrored or rejected.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Sets hom mapping records the retained Sage homset/container methods relevant to set maps.
- Each retained method is assigned to a Sets hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Sets hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Sets hom mapping to ensure the project explicitly mirrors any retained
Sage homset/container methods instead of assuming generic Sage homset inheritance.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`
- `category_specs/sets/homsets.py`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- Sage docs/source for set homsets and finite-set-map behavior as needed

## Context

Sets is the first subtree where generic hom containers meet actual concrete map
behavior. This audit decides which Sage homset/container methods belong on the
project Sets hom/end/aut surfaces and which are interop-only.

## Acceptance Criteria

- [x] The Sets mapping/spec identifies Sage homset/container methods relevant to set
      hom objects and set-map construction.
- [x] Each method is mirrored onto a project owner, routed elsewhere, or rejected as
      interop-only with source grounding.
- [x] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not use this audit to weaken set-map obligations already admitted in the Sets
  mapping.
- Keep this card on `sets/homsets.py` and the Sets mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.
- 2026-05-17: Added the Sets homset mirroring audit to `[[SPEC-MAPPING-SETS]]`,
  covering generic homset infrastructure, generic endset routing, set-map inverse
  and injectivity/surjectivity predicates, image-subobject construction, finite
  set-map constructors, finite endomap identity/composition, and finite image/fiber
  evidence. `fibers()` was not admitted as a generic set-hom surface; it remains a
  separately nameable finite-fiber/preimage-family owner if later work needs it.
- 2026-05-17: Fresh-context agent review recommended `complete` with no material
  findings. The card is now human-gated; do not mark `complete` without human
  approval.

## Review Log

### Fresh-Context Agent Review - 2026-05-17

Recommendation: `complete`; routed to `needs-human-input` for the required human gate.

- Gate 1: Source grounding checked against `[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]`, `category_specs/sets/docs/MAPPING.md`, `category_specs/sets/docs/SAGE_INVENTORY.md`, `category_specs/sets/homsets.py`, and installed Sage homset, set-morphism, image-set, and finite-set-map sources.
- Gate 2: Acceptance criteria are covered by the new `[[SPEC-MAPPING-SETS]]` Sets homset mirroring audit.
- Gate 3: Staged diff review found only plan/task/spec/memory/DAG changes and no unrelated plugin-owned paths.
- Gate 4: Review found no deleted baseline obligations or Sage-gap-driven weakening of the Sets mapping.
- Gate 5: Identity, endset, set-map predicate, image, finite-set-map constructor, finite endomap, and finite image/fiber surfaces are mirrored, routed, or rejected with source evidence.
- Gate 6: `just plan-validate` passed.
- Red flag log: no introspection red flags were found in changed spec/card content; upstream Sage evidence contains ordinary boundary-use `isinstance`, `hasattr`, and `type` checks that are not defects of this card.

---
id: TASK-AUDIT-RINGS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-RINGS]]'
title: Audit Rings hom mapping for mirrored Sage homset surfaces
status: complete
priority: high
description: Audit `category_specs/rings/homsets.py` and the Rings mapping/spec surface so
  retained Sage ring-hom container methods are explicitly mirrored, rerouted, or
  rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Rings hom mapping records the retained Sage homset/container methods relevant to ring homs and endomorphisms.
- Each retained method is assigned to a Rings hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Rings hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Rings hom mapping under the project-owned HomCategory semantic base so
retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`
- `category_specs/rings/homsets.py`
- `category_specs/rings/docs/MAPPING.md`
- `category_specs/rings/docs/SAGE_INVENTORY.md`
- Sage docs/source for ring homsets and ring endomorphism containers as needed

## Context

Rings is a major homset-bearing subtree with constructor/coercion conventions that
should not be carried into the project by assumption. This audit makes those
choices explicit in the mapping surface.

## Acceptance Criteria

- [x] The Rings mapping/spec identifies Sage homset/container methods relevant to ring hom objects and their constructors.
- [x] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [x] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not weaken ring-hom obligations or overload signatures to match current Sage
  convenience behavior.
- Keep this card on `rings/homsets.py` and the Rings mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.
- 2026-05-17: Added the Rings homset mirroring audit to `[[SPEC-MAPPING-RINGS]]`,
  covering generic Hom/End routing, `RingHomset` construction, natural and
  zero-codomain maps, ring morphism injectivity/fraction-field extension, ideal
  pushforward and inverse-image behavior, quotient-cover lifts, generator-image and
  base-map constructor evidence, Frobenius endomorphisms, and field-family
  embedding/automorphism witnesses. Fresh-context review found that the current
  project `section()` declaration could not be left to a later downstream card, so
  `[[TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING]]`
  resolved it by removing the generic ring-hom declaration and recording the separate
  generic-map, quotient/subquotient, split/coercion-map, and family-specific owners.
  No new decision card was required by this audit; previously identified
  roots-of-unity, Ore-localization, and q-adic precision decisions remain the owning
  dependency surface for their separate issues.

## Review Log

### Fresh-Context Agent Review - 2026-05-17

Recommendation: `revision-required`.

- Blocking finding: `category_specs/rings/homsets.py` declared
  `_RingHomomorphisms.section` without a final ring-hom owner/reroute outcome.
- Source evidence: Sage generic `Map.section`, composite-map `section`, identity
  morphism `section`, and set-isomorphism `section` live in generic map/morphism
  code; checked core ring homset and ring morphism sources do not define a
  ring-generic `section()` method.
- Rework route: resolve `[[TASK-AUDIT-RINGS-HOM-SECTION-OWNERSHIP-AND-SAGE-SOURCE-GROUNDING]]`
  before routing this card to human approval.

### Fresh-Context Agent Review After Rework - 2026-05-17

Recommendation: `needs-human-input`.

- Blocking findings: none.
- Review checked that `_RingHomomorphisms.section` was removed from
  `category_specs/rings/homsets.py`, and that `[[SPEC-MAPPING-RINGS]]` now records
  `section()` as generic map/morphism, family-specific, quotient/subquotient, or
  split/coercion-map vocabulary rather than a ring-generic hom obligation.
- Validation: `just plan-validate` passed. Full `just test` was intentionally not used
  as acceptance evidence because the parallel mypy-plugin work still owns the global
  mypy gate.
- Routing: this card is human-gated; continue autonomous work at
  `[[TASK-AUDIT-ALGEBRAS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]`.

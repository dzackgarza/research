---
id: TASK-AUDIT-CAT-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-CAT]]'
title: Audit Cat hom mapping for mirrored Sage homset surfaces
status: complete
priority: high
description: Audit `category_specs/cat/homsets.py` and the Cat mapping/spec surface so
  any retained Sage homset/container methods are explicitly mirrored, routed, or
  rejected rather than assumed inherited.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Cat hom mapping records every retained Sage homset/container method relevant to category-object homs.
- Each retained method is assigned to a Cat hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 36
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Cat hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Cat hom mapping after the decision that project `HomCategory` is the
semantic base and Sage homset/container behavior is mirrored explicitly rather
than inherited semantically.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md`
- `category_specs/cat/homsets.py`
- `category_specs/cat/docs/MAPPING.md`
- `category_specs/cat/docs/SAGE_INVENTORY.md`
- Sage docs/source for category-object `Homsets()` / `Endsets()` routing as needed

## Context

Cat owns category-object Hom/End/Aut navigation, but the reopened homset decision
means any Sage container methods that remain on this surface must now be mirrored
explicitly in the mapping rather than treated as inherited generic Homset owners.

## Acceptance Criteria

- [x] The Cat mapping/spec identifies the Sage homset/container methods relevant to
      category-object hom surfaces.
- [x] Each method is mirrored onto a project owner, routed elsewhere, or rejected as
      interop-only with source grounding.
- [x] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not weaken Cat-owned Hom/End/Aut obligations because Sage category-object
  behavior is inconvenient.
- Keep this card on Cat hom mapping only; do not survey unrelated Cat constructor or
  category-obligation examples.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.
- 2026-05-17: Added the Cat homset mirroring audit to `[[SPEC-MAPPING-CAT]]`.
  The audit routes Sage `Homsets()` and `Endsets()` selectors through project
  `HomCategory()` and `EndCategory()`, keeps direct `A.Hom(B)` as the Cat-owned
  functor hom parent, routes generic container methods such as `domain`,
  `codomain`, `identity`, `one`, `natural_map`, and `reversed` to the shared
  Hom/End layer or interop-only status, mirrors Sage `Functor` and
  `ConstructionFunctor` methods onto Cat element owners, and reconciles the
  missing generic Sage `Autset` class by keeping `AutCategory()` project-owned.
- 2026-05-17: Fresh-context review found no blockers or required edits. The card
  is ready for human approval rather than autonomous rework.

## Review Log

### Fresh-Context Agent Review - 2026-05-17

Recommendation: route to human approval.

- Blocking findings: none.
- Review checked that the stale `HomsetsCategory.Autset` row was replaced by a
  project-owned `AutCategory()` route, that generic Sage Homset container
  methods are explicitly routed to shared Hom/End or interop-only owners, and
  that the bounded negative finding does not make an unsupported global absence
  claim.
- Routing: this card is human-gated; continue autonomous work at
  `[[TASK-AUDIT-LATTICES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]`.

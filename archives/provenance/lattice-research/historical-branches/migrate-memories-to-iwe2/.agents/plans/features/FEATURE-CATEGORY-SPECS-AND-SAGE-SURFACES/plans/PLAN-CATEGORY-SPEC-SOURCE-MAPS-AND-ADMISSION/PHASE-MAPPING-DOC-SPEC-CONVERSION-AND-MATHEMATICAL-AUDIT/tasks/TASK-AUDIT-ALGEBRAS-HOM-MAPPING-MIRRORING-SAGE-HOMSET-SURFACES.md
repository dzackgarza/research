---
id: TASK-AUDIT-ALGEBRAS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-ALGEBRAS]]'
title: Audit Algebras hom mapping for mirrored Sage homset surfaces
status: complete
priority: high
description: Audit `category_specs/algebras/homsets.py` and the Algebras mapping/spec
  surface so retained Sage algebra-hom container methods are explicitly mirrored,
  rerouted, or rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Algebras hom mapping records the retained Sage homset/container methods relevant to algebra homs and endomorphisms.
- Each retained method is assigned to an Algebras hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Algebras hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Algebras hom mapping under the project-owned HomCategory semantic base so
retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-ALGEBRAS.md`
- `category_specs/algebras/homsets.py`
- `category_specs/algebras/docs/MAPPING.md`
- `category_specs/algebras/docs/SAGE_INVENTORY.md`
- Sage docs/source for algebra homsets and algebra endomorphism containers as needed

## Context

Algebra hom containers sit close to ring and module behavior but have their own
constructor and method surfaces. This audit makes those retained Sage surfaces
explicit in the project mapping.

## Acceptance Criteria

- [x] The Algebras mapping/spec identifies Sage homset/container methods relevant to algebra hom objects and their constructors.
- [x] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [x] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not weaken algebra-hom obligations or overload signatures to match current Sage
  convenience behavior.
- Keep this card on `algebras/homsets.py` and the Algebras mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.
- 2026-05-17: Added the Algebras homset mirroring audit to
  `[[SPEC-MAPPING-ALGEBRAS]]`, covering generic Hom/End routing, absence of a base
  Sage algebra homset class, finite-dimensional algebra homset construction and
  validation, graded commutative algebra homsets, functorial constructor interop, and
  the `has_standard_involution()` non-homset rejection. Corrected
  `category_specs/algebras/homsets.py` so algebra hom kernels return
  `AlgebraIdeal` rather than `Algebra`.
- 2026-05-17: Review required revision for unresolved inherited mapping-spec gaps;
  reconciled `semisimple_quotient()`, `Supercommutative()`, the separate Sage
  `radical()` callable, and the Cellular decision reference in
  `[[SPEC-MAPPING-ALGEBRAS]]`.
- 2026-05-17: Fresh-context review verified the revised `semisimple_quotient()`,
  `Supercommutative()`, Cellular handoff, and `kernel() -> AlgebraIdeal` rows
  against Sage sources and project decisions; no remaining blocker found.

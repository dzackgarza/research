---
id: TASK-AUDIT-LATTICES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-LATTICES]]'
title: Audit Lattices hom mapping for mirrored Sage homset surfaces
status: complete
priority: high
description: Audit `category_specs/lattices/homsets.py` and the Lattices mapping/spec
  surface so retained Sage homset/container methods are explicitly mirrored,
  rerouted, or rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Lattices hom mapping records the retained Sage homset/container methods relevant to lattice morphisms and automorphism objects.
- Each retained method is assigned to a Lattices hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 40
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Lattices hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Lattices hom mapping under the project-owned HomCategory semantic base
so retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`
- `category_specs/lattices/homsets.py`
- `category_specs/lattices/docs/MAPPING.md`
- `category_specs/lattices/docs/SAGE_INVENTORY.md`
- Sage docs/source for lattice/module hom containers and isometry surfaces as needed

## Context

Lattices builds on module/form hom ownership, but it still has its own homset file
and mapping obligations. This audit makes retained Sage container methods explicit
in the lattice mapping surface.

## Acceptance Criteria

- [x] The Lattices mapping/spec identifies Sage homset/container methods relevant to lattice hom objects and their constructors.
- [x] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [x] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not use lattice backend convenience as a substitute for explicit hom-method ownership.
- Keep this card on `lattices/homsets.py` and the Lattices mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.
- 2026-05-17: Added the Lattices homset mirroring audit to
  `[[SPEC-MAPPING-LATTICES]]`. The audit routes generic Homset container methods to
  the shared Hom/End base, free/FGP construction mechanics to module Hom owners,
  formed-module isometry semantics to the forms Hom/Aut layers, and lattice-specific
  subgroup/discriminant bridge surfaces to `Lattices(R).AutCategory()`. Existing
  downstream lattice cards cover formed cokernel and discriminant-kernel implementation
  gaps; this card is ready for fresh-context review.
- 2026-05-17: Fresh-context review found no blockers. It checked that generic
  Homset containers are routed to generic Hom/End ownership, FGP/free-module Hom
  mechanics route to module/form owners, discriminant bridge names route to downstream
  tracked cards rather than nonexistent Sage methods, and no `MorphismMethods`, local
  casts, or Sage ambient-lattice public API were introduced. Routed to
  `needs-human-input` for human approval.

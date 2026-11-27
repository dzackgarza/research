---
id: PHASE-STATIC-CATEGORY-REFINEMENT-WORK-QUEUE
trackerStatus:
  type: phase
parents:
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
dependsOn: []
title: Static category refinement work queue
status: unstarted
description: 'This phase groups current cards that were previously attached directly to `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER`
  or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work
  remains in child task cards, while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- Any mathematical spec changes cite their source grounding before implementation proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
---
# Static category refinement work queue

## Summary

This phase groups current cards that were previously attached directly to `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

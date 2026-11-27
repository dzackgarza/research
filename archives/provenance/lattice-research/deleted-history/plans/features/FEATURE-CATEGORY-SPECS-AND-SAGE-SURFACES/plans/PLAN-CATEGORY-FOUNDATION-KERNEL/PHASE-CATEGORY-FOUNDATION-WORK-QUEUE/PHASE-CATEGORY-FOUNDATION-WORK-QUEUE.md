---
id: PHASE-CATEGORY-FOUNDATION-WORK-QUEUE
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
dependsOn: []
title: Category foundation work queue
status: unstarted
description: 'This phase groups current cards that were previously attached directly to `PLAN-CATEGORY-FOUNDATION-KERNEL`
  or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work
  remains in child task cards, while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- Any mathematical spec changes cite their source grounding before implementation proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
---
# Category foundation work queue

## Summary

This phase groups current cards that were previously attached directly to `PLAN-CATEGORY-FOUNDATION-KERNEL` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

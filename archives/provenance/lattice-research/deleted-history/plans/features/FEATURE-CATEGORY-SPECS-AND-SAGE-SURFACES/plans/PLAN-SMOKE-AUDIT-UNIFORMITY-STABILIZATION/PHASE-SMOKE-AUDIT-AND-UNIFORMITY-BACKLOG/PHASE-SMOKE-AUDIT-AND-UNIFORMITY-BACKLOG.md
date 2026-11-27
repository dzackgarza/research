---
id: PHASE-SMOKE-AUDIT-AND-UNIFORMITY-BACKLOG
trackerStatus:
  type: phase
parents:
- '[[PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION]]'
dependsOn: []
title: Smoke audit and uniformity backlog
status: unstarted
description: 'This phase groups current cards that were previously attached directly to `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`
  or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work
  remains in child task cards, while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- Any mathematical spec changes cite their source grounding before implementation proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION
---
# Smoke audit and uniformity backlog

## Summary

This phase groups current cards that were previously attached directly to `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

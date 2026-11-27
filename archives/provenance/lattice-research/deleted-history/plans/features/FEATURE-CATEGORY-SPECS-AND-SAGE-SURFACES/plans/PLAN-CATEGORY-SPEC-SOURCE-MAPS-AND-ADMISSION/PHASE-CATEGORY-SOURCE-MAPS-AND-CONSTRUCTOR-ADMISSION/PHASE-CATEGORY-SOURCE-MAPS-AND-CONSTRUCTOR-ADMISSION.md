---
id: PHASE-CATEGORY-SOURCE-MAPS-AND-CONSTRUCTOR-ADMISSION
trackerStatus:
  type: phase
parents:
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
dependsOn: []
title: Category source maps and constructor admission
status: unstarted
description: 'This phase groups current cards that were previously attached directly to `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`
  or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work
  remains in child task cards, while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- Any mathematical spec changes cite their source grounding before implementation proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
---
# Category source maps and constructor admission

## Summary

This phase groups current cards that were previously attached directly to `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete, blocked with concrete blockers, or split into successor cards.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

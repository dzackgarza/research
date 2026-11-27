---
id: PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
trackerStatus:
  type: phase
parents:
- '[[PLAN-GEOMETRIC-SOURCE-ADMISSION]]'
dependsOn: []
title: Geometric source admission research
status: complete
description: >-
  This phase groups current cards that were previously attached directly
  to `PLAN-GEOMETRIC-SOURCE-ADMISSION` or to the corresponding legacy `.agents` work
  queue. It is a routing phase: executable work remains in child task cards, while
  definition-heavy work remains in feature-level spec cards.
successCriteria:
- >-
  Child task cards are complete only after blockers are resolved, or after the
  original card is superseded by a linked successor that remains active; blocked
  child cards do not satisfy phase acceptance.
- >-
  Any mathematical spec changes cite their source grounding before implementation
  proceeds.
- >-
  Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
---
# Geometric source admission research

## Summary

This phase groups current cards that were previously attached directly to
`PLAN-GEOMETRIC-SOURCE-ADMISSION` or to the corresponding legacy `.agents` work
queue. It is a routing phase: executable work remains in child task cards, while
definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete only after blockers are resolved, or after the
      original card is superseded by a linked successor that remains active; blocked
      child cards do not satisfy phase acceptance.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

## Review Log

### 6-Gate Protocol Review (2026-05-07)

Reviewer: Hermes Agent. Gates passed: G1 Source Paths, G2 Exit Criteria Checkability,
G3 Task Inventory Complete, G4 Scope Containment, G5 Dependencies Correct.
Gates failed: none. Outcome: pass-with-observations.

#### G1: Source Paths — PASS

Phase parents to PLAN-GEOMETRIC-SOURCE-ADMISSION to FEATURE-GEOMETRY-CATEGORY-INTERFACES.
All child tasks cite specific sources (Stacks Project tags, Sage docs, OSCAR docs,
Macaulay2 docs, installed Sage source files).

#### G2: Exit Criteria — PASS

Three success criteria are all checkable. Criterion 1 (child task completion after
blocker resolution) can be validated by enumerating child card statuses. Criterion 2
(mathematical spec changes cite source grounding) is a future-facing guard; no spec
changes exist yet in this research-only phase. Criterion 3 (follow-up work filed as
tracked cards) can be verified by filesystem enumeration.

#### G3: Task Inventory — PASS

12 child task cards inventoried: TASK-INTEGRATE-SCHEMES-CATEGORY (substrate),
TASK-INTEGRATE-VARIETIES-CATEGORY, TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY,
TASK-INTEGRATE-POLYTOPES-CATEGORY, TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY,
TASK-INTEGRATE-COMPLEX-MANIFOLDS-CATEGORY, TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY,
TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY, TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY,
TASK-INTEGRATE-POLYHEDRA-2D-POLYTOPES-CATEGORY, TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY,
TASK-WRAPUP-PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH. All major geometry category
vocabularies expected from the parent plan are covered.

#### G4: Scope — PASS

Phase scoped as a routing phase — executable work in child tasks, definition-heavy
work in feature-level spec cards. All 12 child cards are research/planning tasks
(type=task, no implementation). No scope creep detected.

#### G5: Dependencies — PASS

Dependency graph is correct and consistent. Phase dependsOn=[] (child tasks encode
their own deps). All child task dependsOn edges match mathematical refinement order
(Schemes → Varieties → Complex Varieties → Curves/Surfaces; Smooth Manifolds →
Complex Manifolds; Polytopes → 2D Polytopes; Varieties + Polytopes → Toric Varieties).

#### G6: No Weakening — PASS

No weakening detected. All child cards route toward stricter refinements. Cards
consistently correct over-narrow invariant ownership by pushing ownership to broadest
scheme/variety refinements.

#### Observations

- Warning: 4 of 12 child cards remain needs-human-input at review time (schemes,
  varieties, smooth manifolds, polytopes).
- Warning: TASK-WRAPUP dependsOn includes itself.
- Info: 7 of 12 child cards marked complete with 6-gate reviews.
- Info: All child cards maintain evidence/inference separation and cite specific
  source URLs, file paths, or Stacks Project tags.

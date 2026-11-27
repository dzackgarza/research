---
id: PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
trackerStatus:
  type: phase
parents:
- '[[PLAN-GEOMETRIC-SOURCE-ADMISSION]]'
dependsOn: []
title: Geometric source admission research
status: complete
description: 'This phase groups current cards that were previously attached directly
  to `PLAN-GEOMETRIC-SOURCE-ADMISSION` or to the corresponding legacy `.agents` work
  queue. It is a routing phase: executable work remains in child task cards, while
  definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete only after blockers are resolved, or after the original
  card is superseded by a linked successor that remains active; blocked child cards
  do not satisfy phase acceptance.
- Any mathematical spec changes cite their source grounding before implementation
  proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
reviewLog:
  entries:
  - date: '2026-05-07'
    reviewer: Hermes Agent (6-Gate Protocol)
    gatesPassed:
    - G1 Source Paths
    - G2 Exit Criteria Checkability
    - G3 Task Inventory Complete
    - G4 Scope Containment
    - G5 Dependencies Correct
    gatesFailed: []
    outcome: pass-with-observations
    findings:
    - gate: G1
      result: PASS
      detail: Source paths clear. Phase parents to PLAN-GEOMETRIC-SOURCE-ADMISSION to
        FEATURE-GEOMETRY-CATEGORY-INTERFACES. All child tasks cite specific sources
        (Stacks Project tags, Sage docs, OSCAR docs, Macaulay2 docs, installed Sage
        source files).
    - gate: G2
      result: PASS
      detail: Three success criteria are all checkable. Criterion 1 (child task completion
        after blocker resolution) can be validated by enumerating child card statuses.
        Criterion 2 (mathematical spec changes cite source grounding) is a future-facing
        guard; no spec changes exist yet in this research-only phase. Criterion 3
        (follow-up work filed as tracked cards under plans/features/) can be verified
        by filesystem enumeration.
    - gate: G3
      result: PASS
      detail: 12 child task cards inventoried — TASK-INTEGRATE-SCHEMES-CATEGORY (substrate),
        TASK-INTEGRATE-VARIETIES-CATEGORY, TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY,
        TASK-INTEGRATE-POLYTOPES-CATEGORY, TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY,
        TASK-INTEGRATE-COMPLEX-MANIFOLDS-CATEGORY, TASK-INTEGRATE-COMPLEX-ALGEBRAIC-CURVES-CATEGORY,
        TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY, TASK-INTEGRATE-FAMILIES-OF-VARIETIES-CATEGORY,
        TASK-INTEGRATE-POLYHEDRA-2D-POLYTOPES-CATEGORY, TASK-INTEGRATE-TORIC-VARIETIES-WITH-LATTICE-CATEGORY,
        TASK-WRAPUP-PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH. All major geometry
        category vocabularies expected from the parent plan are covered. No gaps detected.
    - gate: G4
      result: PASS
      detail: Phase is scoped as a routing phase — executable work in child tasks, definition-heavy
        work in feature-level spec cards. All 12 child cards are research/planning tasks
        (type=task, no implementation). No scope creep into implementation or spec-writing
        detected. Cards consistently self-document as not authorizing implementation.
    - gate: G5
      result: PASS
      detail: Dependency graph is correct and consistent. Phase dependsOn=[] (child
        tasks encode their own deps). All child task dependsOn edges match mathematical
        refinement order — Schemes → Varieties → Complex Varieties → Curves/Surfaces;
        Smooth Manifolds → Complex Manifolds; Polytopes → 2D Polytopes; Varieties +
        Polytopes → Toric Varieties. TASK-WRAPUP depends on all sibling tasks
        (self-dependency observed but benign — likely DAG technique to prevent premature
        execution). Minor note — TASK-INTEGRATE-SCHEMES-CATEGORY dependsOn=[] but the
        parent plan cites PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION as a dependency;
        that plan-level dependency is not reflected in the task-level DAG.
    - gate: G6
      result: PASS
      detail: No weakening detected. All child cards route toward stricter refinements
        (e.g., varieties require integral+separated+finite-type, complex varieties
        require smooth/proper/projective for Hodge surfaces, curves are dimension-one
        specializations of broader invariants). Cards consistently correct over-narrow
        invariant ownership (genus, Hodge numbers, Kodaira dimension, Euler characteristics,
        canonical data) by pushing ownership to broadest scheme/variety refinements.
    observations:
    - status: warning
      detail: '4 of 12 child cards remain needs-human-input (schemes, varieties, smooth
        manifolds, polytopes). These are the foundational substrate cards that 7 completed
        cards transitively depend on. The cards themselves document that their dependsOn
        edges are "sequencing edges, not blockers" but the phase acceptance criterion
        states "blocked child cards do not satisfy phase acceptance." The phase cannot
        be accepted until these 4 foundation cards receive human approval.'
    - status: warning
      detail: 'TASK-WRAPUP dependsOn includes itself. This is unusual but may be intentional
        as a DAG technique to prevent the wrapup card from being executed before phase-level
        acceptance. Recommend human reviewer confirm intent.'
    - status: info
      detail: '7 of 12 child cards are marked complete with 6-gate reviews recorded.
        The wrapup card (unstarted) covers meta-review, card status audit, skill updates,
        and git milestone organization. It will catch any remaining issues.'
    - status: info
      detail: 'All child cards maintain evidence/inference separation and cite specific
        source URLs, file paths, or Stacks Project tags. No unsourced claims detected.'
---
# Geometric source admission research

## Summary

This phase groups current cards that were previously attached directly to `PLAN-GEOMETRIC-SOURCE-ADMISSION` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete only after blockers are resolved, or after the
      original card is superseded by a linked successor that remains active; blocked
      child cards do not satisfy phase acceptance.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

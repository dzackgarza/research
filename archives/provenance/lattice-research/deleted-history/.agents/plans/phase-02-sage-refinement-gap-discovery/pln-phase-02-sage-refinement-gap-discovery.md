---
trackerStatus:
  type: plan
title: Phase 02 Sage refinement and gap discovery
status: blocked
planId: PLN-PHASE-02
planType: phase-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-RESEARCH-000
tags:
  - plan
  - phase-control
  - sage
  - gap-research
---

# Phase 02 Sage refinement and gap discovery

## Objective

Refine existing Sage constructions into the specified category layer and identify the
precise gaps that require wrappers, bridges, source research, or owned implementation.


## Definition Grounding Gate

Phase 02 may refine Sage objects only after the corresponding Phase 01 spec has recorded
the mathematical owner, definition, hypotheses, and return/codomain. Sage behavior is
evidence about implementation and compatibility; it is not definition authority when it
conflicts with the project category model.

For each Sage constructor or method under refinement, the child card must cite the
accepted spec surface, relevant `category_specs/*/docs/MAPPING.md` and
`SAGE_INVENTORY.md` rows, Sage written docs/source, and any source-mining or decision
card that resolved ambiguity. Missing or conflicting evidence becomes a gap-discovery
card, not an ad hoc local wrapper.

## Entry criteria

- [ ] `PLN-PHASE-01` has approved specs for the relevant category surfaces.
- [ ] Source maps identify the Sage constructors and methods being refined.

## Exit criteria

- [ ] Each Sage gap is classified as supported, bridge-needed, spec mismatch, or true implementation gap.
- [ ] Blockers are represented as tracked research, decision, or implementation cards.

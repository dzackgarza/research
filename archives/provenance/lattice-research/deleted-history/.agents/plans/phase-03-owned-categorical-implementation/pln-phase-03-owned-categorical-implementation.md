---
trackerStatus:
  type: plan
title: Phase 03 owned categorical implementation layer
status: blocked
planId: PLN-PHASE-03
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
  - implementation
  - sage
---

# Phase 03 owned categorical implementation layer

## Objective

Implement or wrap Sage classes so project objects satisfy the specs directly, while
leveraging mature open-source mathematical software for exact kernels.


## Definition Grounding Gate

Phase 03 implementation work may start only from accepted specs and Phase 02 gap records.
Each implementation card must name the public mathematical noun being implemented, the
source-grounded definition, hypotheses, return/codomain, and backend or Sage object used
as the exact computation carrier.

Use `category_specs/*/docs/MAPPING.md`, `category_specs/*/docs/SAGE_INVENTORY.md`,
`theory/backends/software-capability-map.md`, and `research-software-wiring` before
writing local algorithms. If no backend or owned category surface can express the noun,
file a backend-gap or base-vocabulary prerequisite before implementation.

## Entry criteria

- [ ] Phase 01 specs are approved for the target surfaces.
- [ ] Phase 02 has classified the relevant Sage and backend gaps.

## Exit criteria

- [ ] Core category objects expose the specified semantic interfaces.
- [ ] Implementation cards route mathematical kernels through preferred open-source backends or approved true-gap code.
- [ ] QC gates the committed implementation surface before phase transition.

---
trackerStatus:
  type: plan
title: Phase 06 geometry and Coble interfaces
status: blocked
planId: PLN-PHASE-06
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
  - geometry
  - coble
  - lean
  - formalization
---

# Phase 06 geometry and Coble interfaces

## Objective

Expose semantic interfaces for schemes, varieties, complex varieties, curves, surfaces,
families, divisors, Picard groups, blowups, covers, and Coble-specific relative
constructions.


## Mathematical Grounding Gate

Geometry interface work must start from sourced scheme/variety/surface/family
vocabulary, not raw polynomial or matrix calculations. Each child card must name the
geometric object, morphism, divisor/Picard construction, hypotheses, return object, and
software backend or literature source that justifies the operation.

Use `theory/references/index.md`, `theory/moduli/`, geometry source-admission cards,
Sage/Singular/Macaulay2/Oscar documentation, and accepted category specs before adding
interfaces. Coble-specific claims remain blocked until the geometry and lattice objects
can express the claim semantically.

## Lean and Aristotle thread

Extend the formalization vocabulary only where the geometry interfaces have stabilized.
Targets should be small statements that support later paper arguments: Picard/divisor
vocabulary, pullback and pushforward identities, cover and ramification hypotheses, and
source-backed lemmas that are cleanly expressible without encoding implementation
details.

Aristotle may run asynchronously on these bounded formalization tasks. Do not use it to
skip source acquisition, mathematical review, or the requirement that the repo's
semantic objects state the result clearly.

## Entry criteria

- [ ] Lattice and universal category surfaces are stable enough to express Picard and cover constructions.
- [ ] Backend routing is documented for commutative algebra and algebraic geometry systems.

## Exit criteria

- [ ] Coble constructions can be expressed through Picard, divisor, blowup, cover, pullback, pushforward, and ramification vocabulary.
- [ ] Known primary-source examples are recovered semantically.
- [ ] Geometry-facing formalization cards exist for small reusable lemmas that later Coble proofs will need.
- [ ] QC gates the committed implementation surface before phase transition.

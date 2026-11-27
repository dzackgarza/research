---
id: TASK-RESEARCH-PICARD-FUCHS-MONODROMY-JNF-FAMILIES
trackerStatus:
  type: task
parents:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
dependsOn: []
title: Research Picard-Fuchs and monodromy JNF computations for families
status: complete
priority: low
description: Research how to compute Jordan normal forms of monodromy operators for
  families of curves and surfaces, including Picard-Fuchs operator routes.
successCriteria:
- Read the referenced Noether-Lefschetz/Singular material enough to understand the
  Picard-Fuchs route.
- Identify required backend tools and what each certifies.
- State the exact mathematical inputs/outputs for curve-family and surface-family
  cases.
- Create follow-up cards for backend decisions, category specs, and implementation
  tasks if warranted.
complexity: 35
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
- PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
---
# Research Picard-Fuchs and monodromy JNF computations for families

## Summary

Research how to compute Jordan normal forms of monodromy operators for families of curves and surfaces, including Picard-Fuchs operator routes.

## Source Provenance

Migrated from `specs/TODO.md`: "Computations of the JNF of a monodromy operator of a family of curves f(x,y,t) and a family of surfaces f(x,y,z,t)" and note about Picard-Fuchs operators and Singular `foliation.lib` in `https://github.com/movasati/NoetherLefschetz/tree/master`.

## Context

This card should clarify the mathematical/computational route before any implementation: Sage, Singular, ore_algebra, or another exact backend. It likely feeds future families-of-varieties category work.

## Acceptance Criteria

- Read the referenced Noether-Lefschetz/Singular material enough to understand the Picard-Fuchs route.
- Identify required backend tools and what each certifies.
- State the exact mathematical inputs/outputs for curve-family and surface-family cases.
- Create follow-up cards for backend decisions, category specs, and implementation tasks if warranted.

## Dependencies And Boundaries

Do not implement monodromy or Picard-Fuchs computation in this card. Do not claim exactness or correctness without proof-audit-ready evidence.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Researched the Noether-Lefschetz `foliation.lib` source,
  Singular Gauss-Manin manual, local quarantined foliation backend notes, Sage
  Riemann-surface mapping, and `ore_algebra` mapping. Recorded the backend
  boundary in
  `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/specs/SPEC-PICARD-FUCHS-MONODROMY-BACKEND-MAPPING.md`.

## Research Result

This card is ready for review. No monodromy implementation is admitted from this
pass.

For curve families, there are two distinct routes that should not be conflated:
Sage `RiemannSurface` can provide a numerical analytic route for a sequence of
plane-curve fibers after a curve/family spec chooses a plane model and certified
comparison data, while Picard-Fuchs/Gauss-Manin methods compute differential
equations for periods of selected differential forms. The output basis and
certification burden differ.

For surface or higher-dimensional hypersurface families, the relevant route is
the Gauss-Manin/Picard-Fuchs route: start with a one-parameter family, choose the
cohomology class or differential form whose periods are being studied, compute a
Gauss-Manin system or scalar Picard-Fuchs operator, then compute operator
monodromy/Jordan data. This computes monodromy of the selected period local
system only after the geometric-to-operator identification is proved or sourced.

`foliation.lib` is source evidence for Gauss-Manin and Picard-Fuchs derivation in
the Brieskorn-module/tame-hypersurface setting. `ore_algebra` is source evidence
for downstream monodromy of a known differential operator, but its local import
currently fails and it does not itself derive Picard-Fuchs operators from
geometry. Macaulay2 was checked only at the general system/documentation level in
this card; no installed local `M2` command or source-backed `PeriodIntegrals`
route was found in the checked surface.

## Review Log

### Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance.
**Gates failed:** None.
**Outcome:** no concrete revision findings; human approval remains required before
marking the card complete.

Findings: none. The review found that the produced backend mapping spec separates
geometric Picard-Fuchs derivation from operator-level monodromy, records local
environment gaps, refuses implementation admission, and satisfies this research
card's acceptance criteria.

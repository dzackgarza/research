---
id: TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE
trackerStatus:
  type: task
parents:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
dependsOn: []
title: Research Sage Riemann surface interface integration
status: complete
priority: low
description: Research how Sage Riemann surface functionality should map into the category-spec
  vocabulary and whether it warrants wrapper, constructor, or method cards.
successCriteria:
- Read the Sage Riemann surface documentation and relevant source.
- List candidate constructors, methods, and mathematical nouns relevant to category
  specs.
- Identify required decisions about ownership, naming, and allowed wrapper boundaries.
- Create follow-up cards for any implementation or decision work that is concrete
  enough to execute.
complexity: 35
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
- PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
---
# Research Sage Riemann surface interface integration

## Summary

Research how Sage Riemann surface functionality should map into the category-spec vocabulary and whether it warrants wrapper, constructor, or method cards.

## Source Provenance

Migrated from `specs/TODO.md`: "Wrap and interface with https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html".

## Context

This should survey the Sage Riemann surface API, identify the finite set of relevant constructors and methods, and map them to existing or missing category-spec concepts.

## Acceptance Criteria

- Read the Sage Riemann surface documentation and relevant source.
- List candidate constructors, methods, and mathematical nouns relevant to category specs.
- Identify required decisions about ownership, naming, and allowed wrapper boundaries.
- Create follow-up cards for any implementation or decision work that is concrete enough to execute.

## Dependencies And Boundaries

Do not design a variadic or convenience wrapper. Do not implement code. Do not treat Sage method names as project vocabulary without mapping them through category-spec style rules.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Started source-admission research. Scope is Sage
  `RiemannSurface` documentation and installed Sage source; no wrapper or public
  API implementation is authorized by this card.
- 2026-05-06: Completed the bounded source-admission pass. Read official Sage
  Riemann-surface documentation and installed Sage source at
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`,
  plus curve entry points in `affine_curve.py` and `projective_curve.py`.
  Created `[[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]` to record constructor
  and method mapping, public owner candidates, numerical limitations, and the
  decision not to admit wrapper implementation yet. Status moved to
  `needs-agent-review`; this does not mark the card accepted or complete.
- 2026-05-06: Independent Gate 2 review found that the concrete geometry
  ownership follow-up remained inline in the mapping spec. Added
  `[[SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP]]` and linked the mapping spec's
  follow-up consequence to that tracked spec card.

## Research Findings

- Constructor evidence: Sage exposes direct `RiemannSurface(f, prec=53,
  certification=True, differentials=None, integration_method='rigorous')` and curve
  methods `AffineCurve.riemann_surface(**kwargs)` /
  `ProjectivePlaneCurve.riemann_surface(**kwargs)`.
- Mathematical object: a compact analytic Riemann surface determined by a bivariate
  plane-curve equation over a subfield of the complex numbers, interpreted as a cover
  of the coordinate plane in the first variable.
- Candidate public project owner: a future complex curve / analytic Riemann-surface
  refinement attached to a curve, not a raw Sage `RiemannSurface` wrapper.
- Candidate backend methods: local branch monodromy permutations, homology basis,
  holomorphic differential basis, period/Riemann matrix, period-lattice reduction,
  Abel-Jacobi map, numerical Jacobian homomorphism/endomorphism bases, and symplectic
  isomorphism/automorphism searches.
- Boundary: `monodromy_group()` is branch-cover monodromy for the chosen projection,
  not the fundamental group of a curve complement and not family monodromy on
  cohomology.
- Follow-up: no implementation card is warranted yet. The concrete follow-up is the
  tracked mapping spec above and
  `[[SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP]]`; implementation should wait
  for curve, divisor, Jacobian, homology, and period-lattice ownership specs.

## Review Log

### Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding.
**Gates failed:** Gate 2 Acceptance Criteria.
**Outcome:** revision-required, reworked in the work log above, returned to
`needs-agent-review` for another independent pass.

Finding:

- The card required follow-up cards for concrete implementation or decision work,
  but the produced mapping spec left the curve/Jacobian/period-lattice ownership
  spec as inline prose rather than linking a tracked successor.

### Re-Review 2026-05-06 (Independent Explorer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and
Compliance.
**Gates failed:** None.
**Outcome:** no concrete revision findings; human approval remains required before
marking the card complete.

Findings: none. The review found the prior Gate 2 defect resolved by
`[[SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP]]`, which now tracks the geometry
ownership spec that had been left as inline follow-up prose.

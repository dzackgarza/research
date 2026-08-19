---
id: FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
plans: []
title: Historical geometry and Coble vocabulary recovery
status: complete
priority: medium
description: Recover geometry, Coble surface, K3 cover, divisor, Picard, family, and monodromy vocabulary visible in historical src.bak as future specs after geometry and lattice categories can express the constructions.
---
# Historical geometry and Coble vocabulary recovery

## Summary

Recover the useful geometry-facing nouns and backend tie-ins visible in
`src.bak/varieties/varieties.py` and `src.bak/backends/foliation_backend.py`. This is
not downstream Coble computation. It is a specification bucket for the future interface
that will let Coble constructions be expressed as real geometry, maps, divisors,
Picard groups, covers, and lattices.

## Source Provenance

- `src.bak/varieties/varieties.py`
- `src.bak/coble_geometry_varieties.py`
- `src.bak/backends/foliation_backend.py`
- `.agents/memories/theory-backend-routing.md`
- `.agents/memories/theory/backends/software-capability-map.md`
- `.agents/memories/theory/backends/abstract-to-external-mapping.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-SCHEMES-CATEGORY.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-VARIETIES-CATEGORY.md`
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/plans/PLAN-GEOMETRIC-SOURCE-ADMISSION/PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH/tasks/TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY.md`
- `GOAL.md`, stages for geometry interfaces and confined Coble research.

## Recovery Boundary

The old code records vocabulary to recover: varieties, morphisms, curves, surfaces,
divisors, Picard groups, blowups, Coble surfaces, branched covers, K3 surfaces,
Enriques surfaces, families, specialization, Picard-Fuchs operators, and monodromy
data. These become specs for future category and backend admission work.

## Non-Preservation Boundaries

- Do not compute Coble lattices by naming expected lattice presentations before
  constructing the Coble surface, blowup, Picard group, cover, pullback, and K3
  cohomology lattice context.
- Do not treat abstract method stubs as implementation evidence.
- Do not couple geometry nouns to one backend before source admission records the
  correct owner.
- Do not put heavyweight monodromy state into memories or planning metadata.

## Child Specs

- `[[SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE]]`
- `[[SPEC-HISTORICAL-COBLE-K3-COVER-PIPELINE]]`
- `[[SPEC-HISTORICAL-FAMILY-MONODROMY-BACKEND-SURFACE]]`

## Acceptance Criteria

- [ ] Geometry nouns are recovered as category-interface requirements, not code stubs.
- [ ] Coble/K3 construction obligations are expressed as maps and objects.
- [ ] Monodromy and Picard-Fuchs backend work is routed through exact backend research.

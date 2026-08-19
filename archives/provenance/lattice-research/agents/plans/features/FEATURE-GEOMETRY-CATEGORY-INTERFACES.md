---
id: FEATURE-GEOMETRY-CATEGORY-INTERFACES
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
plans:
- '[[PLAN-GEOMETRIC-SOURCE-ADMISSION]]'
- '[[PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS]]'
title: Geometry category interfaces
status: complete
priority: high
description: Collect geometry-facing category interface research for schemes, varieties,
  manifolds, curves, surfaces, families, toric interfaces, curve complements, monodromy,
  and backend admission before phase-06 implementation is attempted.
---
# Feature: Geometry category interfaces

## Summary

Collect geometry-facing category interface research for schemes, varieties, manifolds, curves, surfaces, families, toric interfaces, curve complements, monodromy, and backend admission before phase-06 implementation is attempted.

## Acceptance Criteria

- [ ] Geometry source-admission work records exact source and backend evidence.
- [ ] Curve-complement and monodromy backend work stays research-scoped until category ownership is explicit.
- [ ] No downstream Coble computation is treated as phase-local geometry category work.

## Dependencies And Boundaries

This feature is downstream of the root category-spec and Sage-surface vocabulary. It records geometry-facing category surfaces and backend admission requirements, but does not authorize Coble construction, moduli comparison, or stable-model research before the implementation and lattice gates are complete.

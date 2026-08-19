---
title: Sage Category Source Maps
status: active
date: 2026-05-29
---
# Sage Category Source Maps

This skill owns Sage source maps migrated from the retired `.agents/plans/` directory.

## Load references by task

- `mem:skills/sage-category-source-maps/ring-integration`: load for Sage ring
  construction entry points, pushout/coercion, completions, localizations, quotient
  rings, p-adics, polynomial/series rings, and matrix rings.
- `mem:skills/sage-category-source-maps/set-spec`: load for Sage set category hierarchy,
  concrete set implementations, RealSet, ImageSubobject, enumerated sets, and
  topology/metric/complete surfaces.

## Hard rules

- Verify Sage source/docs before admitting constructors.
- Separate Sage entry point, mathematical owner, and project-facing API.
- Source maps are research inputs; executable work belongs in Nimbalyst cards.

## Referenced documents

[SageMath Ring Construction Entry Points](sage-category-source-maps/ring-integration)

[SageMath Set Implementations: Comprehensive Reference](sage-category-source-maps/set-spec)

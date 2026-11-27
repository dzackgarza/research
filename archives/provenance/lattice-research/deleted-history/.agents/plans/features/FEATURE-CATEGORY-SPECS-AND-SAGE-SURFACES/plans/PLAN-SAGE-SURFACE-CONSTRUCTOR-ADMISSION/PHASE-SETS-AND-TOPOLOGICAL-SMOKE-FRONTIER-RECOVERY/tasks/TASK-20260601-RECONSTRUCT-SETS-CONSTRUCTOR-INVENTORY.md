---
id: TASK-20260601-RECONSTRUCT-SETS-CONSTRUCTOR-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Reconstruct sets constructor inventory from Sage source
status: unstarted
priority: high
description: Mine Sage set, real-set, finite-map, product, family, and set-partition
  constructors before repairing Sets collector names.
activityType: source-mining
uncertaintyState: ordinary-open
workstreamRole: implementation
claimStatus: source-backed
successCriteria:
- Sage source/docs are cited for every admitted Sets constructor shape.
- SPEC-MAPPING-SETS records constructorNameInventories for every exposed Sets constructor
  collector.
- Generic Set wrapper ambiguity is eliminated without preserving rejected constructor
  rows.
- check-constructor-name-inventory no longer reports Sets constructor collector failures.
complexity: 70
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---
# Reconstruct sets constructor inventory from Sage source

## Summary

The constructor-name validator reports many public methods on
`category_specs.sets.Sets._Constructors`, spanning finite enumerated sets, real sets,
integer ranges, primes, image subobjects, finite maps, families, Cartesian products,
and set partitions.
Do not turn this into a name whitelist.
Reconstruct the Sage constructor inventory, then align the collector surface.

## Source Provenance

- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/__init__.py`
- Sage installed source and docs for set constructors, real sets, finite set maps,
  image sets, Cartesian products, families, integer ranges, primes, and set partitions.

## Context

The generic Sage `Set(X)` wrapper is not itself a project constructor source.
Do not keep a rejected row for it.
Each admitted case must be source-grounded as a finite, named, category-owned route.
Set-partition and real-set static constructors are especially likely to require
overload enumeration under original Sage constructor names rather than invented
`From...` routes.

## Acceptance Criteria

- [ ] Enumerate every admitted Sage set constructor family and finite input shape.
- [ ] Decide which names are exact Sage constructor names and which are legitimate
      project-owned construction names.
- [ ] Add or correct `constructorNameInventories` in `SPEC-MAPPING-SETS`.
- [ ] Remove or rename invented collector methods only after the mapping establishes
      the source-grounded surface.
- [ ] Re-run constructor-name QC and record remaining non-sets failures separately.

## Dependencies And Boundaries

- Do not broaden into topological-space smoke failures unless a failing route is a
  Sets constructor inventory violation.
- Do not preserve rejected generic-wrapper ideas as evidence artifacts.

## Work Log

- Created from constructor-name inventory QC output after the anti-polishing constructor
  source gate was added.

---
id: TASK-20260601-RECONSTRUCT-POSET-CONSTRUCTOR-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
dependsOn: []
title: Reconstruct poset constructor inventory from Sage source
status: unstarted
priority: high
description: Replace poset From-style constructor drift with source-grounded Sage
  constructor inventory before code repair.
activityType: source-mining
uncertaintyState: ordinary-open
workstreamRole: implementation
claimStatus: source-backed
successCriteria:
- Sage poset, meet-semilattice, join-semilattice, and lattice constructor source branches
  are enumerated.
- SPEC-MAPPING-POSETS records constructorNameInventories for all admitted poset collectors.
- Invented From-style public names are either mapped as project-owned constructions
  with proof or replaced by original Sage constructor names.
- check-constructor-name-inventory no longer reports poset constructor collector failures.
complexity: 60
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS
---
# Reconstruct poset constructor inventory from Sage source

## Summary

The constructor-name validator reports many public methods on
`category_specs.posets.Posets._Constructors`, including `from_digraph`,
`from_relations`, `meet_semilattice_from_*`, `join_semilattice_from_*`, and
`lattice_from_*`.
These names must not be polished in place.
Mine Sage's actual poset and lattice constructor surfaces first, then decide whether
each project name is an admitted named-only overload, a project-owned construction, or
an invented name to remove.

## Source Provenance

- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-POSETS.md`
- `category_specs/posets/docs/SAGE_INVENTORY.md`
- `category_specs/posets/docs/MAPPING.md`
- `category_specs/posets/__init__.py`
- Sage poset, lattice-poset, meet-semilattice, and join-semilattice constructor docs
  and installed source.

## Context

The phase name still contains old "deferred" wording; this task must not preserve that
state model.
Constructor mapping admits source-grounded routes only.
If a Sage constructor is variadic, enumerate finite valid input shapes and expose them
as named-only overloads under the recovered constructor family.

## Acceptance Criteria

- [ ] List each Sage constructor route with exact accepted input shapes.
- [ ] Record the smallest mathematical owner for posets, meet-semilattices,
      join-semilattices, and lattices.
- [ ] Add or correct `constructorNameInventories` in `SPEC-MAPPING-POSETS`.
- [ ] Remove or replace invented names after the mapping establishes the correct
      constructor surface.
- [ ] Re-run constructor-name QC and record non-poset failures separately.

## Dependencies And Boundaries

- Do not fix failed category assertions by changing raw Sage imports or raw constructor calls.
- Do not retain "deferred" or "gap" constructor artifacts as evidence.

## Work Log

- Created from constructor-name inventory QC output after the anti-polishing constructor
  source gate was added.

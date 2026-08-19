---
id: FEATURE-UNIVERSAL-CATEGORICAL-ALGORITHMS
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-CATEGORICAL-IMPLEMENTATION-LAYER]]'
plans: []
title: Universal categorical algorithms
status: unstarted
priority: critical
description: Implement inheritable categorical algorithms at the highest valid level, especially explicit countability and deterministic enumeration for sets, products, free modules, and later lattice searches.
---
# Feature: Universal categorical algorithms

## Summary

Implement general algorithms at the highest valid categorical level before downstream lattice and Coble searches rely on them. The immediate exemplar from `GOAL.md` is deterministic enumeration: explicitly countable rings, finite products, free modules over countable rings, and lattices over `ZZ` should inherit principled enumeration instead of reimplementing search loops locally.

## Source Provenance

- `GOAL.md`, stage "universal categorical algorithms".
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`.
- `plans/features/FEATURE-MODULES-WITH-FORMS-AND-LATTICES/FEATURE-MODULES-WITH-FORMS-AND-LATTICES.md`.

## Scope

- Define explicit countability and deterministic enumeration surfaces where the mathematical hypotheses justify them.
- Lift enumeration through finite products and free-module constructions through approved category APIs.
- Expose bounded or filtered enumeration in lattice categories only through inherited set/module semantics and source-backed lattice predicates.
- Route backend-specific algorithms through typed bridge contracts when a mature system owns the kernel.

## Non-Goals

- Do not add lattice-local loops that bypass set/module/category enumeration semantics.
- Do not claim exhaustive enumeration for infinite objects without a precise ordering, bound, or proof of coverage.
- Do not conflate finite carrier enumeration with infinite lattice-vector enumeration.

## Acceptance Criteria

- [ ] Countability predicates and enumeration methods are specified and implemented at the correct category owners.
- [ ] Product and free-module enumeration inherits from component carriers with deterministic order.
- [ ] Lattice vector enumeration is expressed through inherited carrier algorithms plus lattice predicates and bounds.
- [ ] Vinberg, orbit, and exhaustive-search consumers can depend on categorical enumeration contracts rather than bespoke loops.
- [ ] Tests verify enumeration order and coverage on real finite and countable mathematical fixtures.

## Dependencies And Boundaries

This feature depends on the owned categorical implementation layer, which itself depends on the approved spec surfaces. It supports later lattice-theoretic implementation and Coble experimental research, but it does not itself own discriminant forms, primitive embeddings, Coble geometry, or moduli claims.

## Work Log

- Created as a GOAL.md coverage card so universal algorithms are tracked separately from lattice-specific implementation work.

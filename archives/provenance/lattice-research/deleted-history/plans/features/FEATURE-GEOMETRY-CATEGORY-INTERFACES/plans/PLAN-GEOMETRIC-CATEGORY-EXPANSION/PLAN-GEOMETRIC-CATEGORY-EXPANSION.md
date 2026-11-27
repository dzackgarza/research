---
id: PLAN-GEOMETRIC-CATEGORY-EXPANSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn: []
title: Geometric category expansion research program
status: approved-and-unstarted
priority: high
owner: Zack
description: Group the high-priority geometric category research cards so schemes,
  varieties, manifolds, polytopes, toric varieties, and related categories enter the
  system through source-backed vocabulary and dependency-aware planning.
successCriteria:
- Each geometric category has source-backed Sage and mathematical vocabulary before
  implementation.
- Dependencies are recorded before implementation cards are created.
- Toric varieties explicitly route through the lattice category integration decision.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Geometric category expansion research program

## Objective

Group the high-priority geometric category research cards so schemes, varieties, manifolds, polytopes, toric varieties, and related categories enter the system through source-backed vocabulary and dependency-aware planning.


## Mathematical Grounding Requirements

This geometry plan is source-admission work, not a license for ad hoc algebraic-geometry
interfaces. Each child card must cite the relevant literature, Sage/Singular/Macaulay2/
Oscar documentation, or local theory note before admitting a category, constructor,
backend, invariant, or morphism.

The grounding record must state the geometric object, morphism or construction,
hypotheses, return object, and backend evidence. If the software only exposes raw
polynomials, matrices, or option bags, the child card must translate them into project
category vocabulary or split a source/backend decision first.

## Subplans

- `PLAN-GEOMETRIC-SOURCE-ADMISSION`: geometric category source admission research.
- `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS`: curve complement and monodromy backend research.

Leaf task ownership is encoded by `parents` containment under the child plan phases.

## Dependency intuition

Definitions and vocabulary come first: schemes and varieties precede specialized complex algebraic categories; lattice integration must precede toric-variety constructor decisions; manifolds and complex manifolds should not be forced through algebraic-variety vocabulary unless the source research justifies it.

## Acceptance Criteria

- [ ] Each geometric category has source-backed Sage and mathematical vocabulary before implementation.
- [ ] Dependencies are recorded before implementation cards are created.
- [ ] Toric varieties explicitly route through the lattice category integration decision.

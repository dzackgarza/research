---
id: PLAN-SPEC-CORE-VERTICAL-SLICE
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PLAN-CATEGORY-SPEC-PROGRAM]]'
title: Spec core vertical slice
status: complete
priority: critical
owner: Zack
description: Establish the narrow typed spec-core, construction-witness, and report
  slice needed to prove finite/countable cartesian-product obligations on free finite-rank
  modules before broad category expansion resumes.
successCriteria:
- A typed declarative spec core records obligations, providers, construction witnesses,
  and reports as data rather than only as Sage method-container structure.
- The slice proves the finite case by reporting that `GF(5)^3` inherits a finite cartesian-power
  carrier with cardinality `125`, without module-local cardinality reimplementation.
- The slice proves the countable case by reporting that `ZZ^2` inherits a countable
  cartesian-power carrier with infinite cardinality and a deterministic enumeration
  obligation routed to product/countable-set providers.
- '`Cat().Constructors()`, `Rings().Constructors()`, and `Modules(R).Constructors()`
  remain constructor-discovery surfaces; the spec-core layer reports how a constructor
  satisfies inherited obligations rather than replacing constructor routing.'
- No non-slice category expansion, category-obligation example broadening, or mypy cleanup is accepted as
  progress for this plan unless it directly changes one of the slice reports.
phases:
- '[[PHASE-SPEC-CORE-VERTICAL-SLICE]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Spec core vertical slice

## Objective

Build the smallest executable spec-core route that answers the feedback in
`/home/dzack/vault/projects/research/Spec Enforcement in Sage.md`: an object should
declare a mathematical category, the inherited obligation closure should be inspectable,
missing obligations should be explicit, and construction witnesses should satisfy
set-level obligations by composition instead of downstream reimplementation.

This plan intentionally narrows the active frontier. Existing broad category-spec
plans remain source material and prior work, but the next success metric is this
vertical slice.

## Source Provenance

- `/home/dzack/vault/projects/research/Spec Enforcement in Sage.md`
- `GOAL.md`, especially the category-spec and universal categorical algorithm stages.
- `.agents/current-goal-phase.md`
- `[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]`
- `[[PLAN-CATEGORY-SPEC-PROGRAM]]`
- `[[PLAN-CATEGORY-FOUNDATION-KERNEL]]`
- `[[SPEC-MAPPING-CAT]]`
- `[[SPEC-MAPPING-SETS]]`
- `[[SPEC-MAPPING-MODULES]]`
- `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`

## Slice Boundary

Admitted examples:

- `GF(5)^3`: finite base ring and finite rank module, with underlying finite
  cartesian power and cardinality `5^3 = 125`.
- `ZZ^2`: countable infinite base ring and finite rank module, with underlying
  countable cartesian power, infinite cardinality, and deterministic enumeration
  obligation.

Required public report shape:

- declared category and constructor route;
- inherited obligations from set, product, and module categories;
- explicit provider or construction witness satisfying each obligation;
- computed finite/countable cardinality result where available;
- missing obligations, if any, with the exact owner category and prerequisite.

Non-goals:

- Do not expand unrelated subtree surfaces to make the plan look busier.
- Do not chase full-suite mypy/QC failures as slice evidence.
- Do not implement lattice-local or module-local enumeration loops when a set/product
  provider should own the obligation.
- Do not replace Sage category wrapping wholesale before this slice proves the needed
  source-of-truth split.

## Acceptance Criteria

- [x] `GF(5)^3` has a spec report showing finite cartesian-power provenance and
  cardinality `125`.
- [x] `ZZ^2` has a spec report showing countable cartesian-power provenance, infinite
  cardinality, and a deterministic enumeration obligation owned by product/countable
  set providers.
- [x] The module implementation does not satisfy those set-level obligations by
  duplicating cardinality or enumeration logic inside the free-module surface.
- [x] A dummy or deliberately incomplete object claiming the slice category produces a
  precise missing-obligations report rather than a silent pass or unrelated category-obligation example
  failure.
- [x] Constructor-discovery surfaces still expose available constructors with
  provenance, and the slice report can name the constructor route used.
- [x] Focused validation covers only the slice reports and directly owned category-obligation examples/tests.

## Dependencies And Boundaries

This plan is approved by the interactive pivot directive. It does not require broad
source-map completion, Hom/End/Aut human-gate closure, or global QC before execution.
If the slice discovers a missing mathematical owner or source-grounding gap, split a
new source-mining or decision card and continue any other ready slice task.

## Work Log

- Created as the pivot plan after review feedback identified broad category expansion
  and mypy/QC routing as poor success metrics without a decisive vertical slice.
- Activated for the spec-core registry/report kernel implementation leaf.
- Completed after the typed report kernel, free finite-rank witness reports, and
  focused validation leaf all reached `complete`.

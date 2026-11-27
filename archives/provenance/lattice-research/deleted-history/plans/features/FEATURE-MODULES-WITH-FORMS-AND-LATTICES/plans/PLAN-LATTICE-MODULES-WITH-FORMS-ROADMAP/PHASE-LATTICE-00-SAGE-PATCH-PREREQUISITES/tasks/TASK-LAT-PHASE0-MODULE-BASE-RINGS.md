---
id: TASK-LAT-PHASE0-MODULE-BASE-RINGS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn: []
title: Implement ModuleBaseRings category refinement and installation
status: complete
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.
successCriteria:
- Read the cited source section before implementation.
- Keep changes inside the named target boundary unless a new card or decision expands
  scope.
- Preserve the mathematical semantics from the source plan and category-spec style
  rules.
- Record validation commands and results before handoff.
- Do not mark this card done without human approval.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES
---
# Implement ModuleBaseRings category refinement and installation

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: ring_base_category.py -- ModuleBaseRings category and installation
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/modules/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`
- `theory/foundations/bilinear-forms-duals-morphisms.md` (for dual-notation and morphism discipline)
- `category_specs/rings.py` (contracted category surface)

### Public owner and target category
- Owner: `ModuleBaseRings` in `src/sage_patches/ring_base_category.py`.
- Integration boundary: ring parents are installed with
  `ring._refine_category_(ModuleBaseRings())` and dispatch through
  `ModuleBaseRings.ParentMethods`; no new ring classes.
- Downstream owners are `Modules(R)` and `Modules(R).WithForms()` for form-bearing
  modules built from those bases.

### Definitions and hypotheses
- `R` is a base ring in the enriched PID scope:
  `ZZ`, `Zp(p)`, `QQ`, `RR`, `CC`, `QQbar`, and `GF(p^n)`.
- `Modules(R)` methods are available on all parents reached by these overrides.
- `r * R` / `R * r` means principal ideal object with submodule semantics
  (`{r*x : x in R}`), not multiplication output.
- Integer-ring quotient syntax is not owned by this category-refinement card. Sage's
  concrete dispatch bypasses refined category `quotient` and `__truediv__` methods for
  that surface, so it is owned by `TASK-LAT-PHASE0-INTEGER-QUOTIENT-COMPATIBILITY`.
- Returned localizations/completions/fraction fields in scope stay in `ModuleBaseRings`
  so module expressions continue to route through redesigned semantics.

### Return objects / codomains
- `R / (n*R)` / `R / (n)` ⇒ module parent intended to satisfy `parent in Modules(R)`.
- `R^n` via `__pow__` ⇒ enriched free module parent in `Modules(R)`.
- `R.complete(...)`, `R.localize(...)`, `R.fraction_field()` outputs remain
  PID-family module-aware ring parents (when in scope).
- `ideal(...)` and `R * I` / `I * R` outputs remain ideal-submodule parents with
  module category membership.

### Concrete implementation work
- Implement `ModuleBaseRings = Rings().PrincipalIdealDomains().Commutative().Subcategory`
  and required `ParentMethods`.
- In `ParentMethods`, override:
  - `__pow__` to produce enriched `R^n`,
  - `ideal`, `__mul__`, `__rmul__` for ideal-submodule construction where Sage dispatch
    reaches the refined category,
  - `completion` / `localization` / `fraction_field` to refine returned parents.
- Make `_refine_category_` application idempotent in `install()`.
- Keep module-membership checks consistent with `Modules(R)` by refining ring
  quotient and ideal outputs after native construction.
- Wire install order via `_install.py` after module import path initialization.

### Acceptance checks
- `[ ]` `ZZ in Modules(ZZ)` after install, with `ZZ^n` and ideal construction routed
  through the refined category where Sage dispatch supports it.
- `[ ]` `QQ in Modules(QQ)` after install; fraction quotient codomain refinement remains
  owned by `TASK-LAT-PHASE0-FRACTION-QUOTIENT-CODOMAINS`.
- `[ ]` `2 * ZZ`, `ZZ * 2`, and `ZZ.ideal(2)` land in module-compatible categories.
- `[ ]` `Zp(5)` and `GF(5)` produced by install still satisfy `Modules` membership
  expectations.
- `[ ]` `ZZ.complete(5)` and `ZZ.localize(5)` return refined ring parents that are
  accepted by the same `Modules` membership checks.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/ring_base_category.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

## Decision Resolution

- 2026-05-06: `[[DECISION-LAT-PHASE0-QUOTIENT-SYNTAX-DISPATCH]]` chose a split path.
  `ModuleBaseRings` owns category-refinable methods only; integer quotient syntax is
  handled by `[[TASK-LAT-PHASE0-INTEGER-QUOTIENT-COMPATIBILITY]]`.
- Evidence retained from preflight: Sage category refinement can add ordinary methods
  and intercept `__pow__` and `ideal`, but `ZZ / 2` and `ZZ.quotient(2*ZZ)` bypass
  refined category methods.
- This card is unblocked for its reduced category-refinement contract. It must not
  reintroduce quotient syntax as a `ModuleBaseRings.ParentMethods` obligation.

## Current Phase Gate

- 2026-05-06: Blocked by the current category-spec and semantic-vocabulary phase. This
  is implementation-phase Sage/lattice work and must not be executed merely to make
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

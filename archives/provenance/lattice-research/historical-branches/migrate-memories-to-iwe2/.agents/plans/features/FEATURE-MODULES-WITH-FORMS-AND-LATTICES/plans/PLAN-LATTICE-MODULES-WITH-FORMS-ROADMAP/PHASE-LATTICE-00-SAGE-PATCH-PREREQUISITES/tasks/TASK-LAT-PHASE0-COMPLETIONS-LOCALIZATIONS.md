---
id: TASK-LAT-PHASE0-COMPLETIONS-LOCALIZATIONS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn:
- '[[TASK-LAT-PHASE0-MODULE-BASE-RINGS]]'
title: Implement completion and localization refinement aliases
status: complete
priority: high
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
complexity: 55
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES
---
# Implement completion and localization refinement aliases

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: completions.py -- ZZ.complete(p), ZZ.localize(p)
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `category_specs/modules/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`
- `theory/foundations/bilinear-forms-duals-morphisms.md`

### Public owner and target category
- Owner: `completions.py` in `src/sage_patches/`.
- Public category boundary remains `ModuleBaseRings` via ring refinement from
  `ring_base_category.py`.
- Returned objects flow into `Modules` and `Lattices` workflows through existing base-change logic.

### Definitions and hypotheses
- `complete` and `localize` are alias-style accessors for `completion` and `localization`
  in target ring parents.
- `ZZ.complete(p)` must refine output to `Zp(p)`-style parent with `ModuleBaseRings` category.
- `ZZ.localize(5)` must produce `Localization(ZZ, [5])` and preserve membership in
  module-aware ring scope when in PID family.
- Any refined completion/localization parent remains compatible with `base_change` and
  `fraction_field()`.

### Return objects / codomains
- `complete(p)` return type: ring parent (typically `Zp(p)`) with same base-ring
  module semantics as `ZZ`.
- `localize(p)` return type: localization ring object in the same enriched scope with
  fraction map from `ZZ`.
- `fraction_field()` remains native return (`QQ` from `ZZ`; `Qp(p)` from `Zp(p)`), but
  must preserve refined category where applicable.

### Concrete implementation work
- Add stable alias methods:
  - `complete = completion`
  - `localize = localization`
  in `ModuleBaseRings.ParentMethods` and ensure each calls `super()` then category-refines
  returned object.
- Ensure `completions.install()` is invoked from `_install.py` after `ring_base_category.install()`.
- Gate all operations by ring-scope checks so non-target ring objects keep native behavior.
- Add targeted assertions in misc test flow for `complete`/`localize` object identity and
  membership.

### Acceptance checks
- `[ ]` `ZZ.complete(5) == Zp(5)` and membership assertions for refined ring behavior.
- `[ ]` `ZZ.localize(5) == Localization(ZZ, [5])` and `1/5 in ZZ.localize(5)`.
- `[ ]` `1/3 not in ZZ.localize(5)` (or equivalent non-member check).
- `[ ]` `ZZ.fraction_field() == QQ` and `Zp(5).fraction_field() == Qp(5)` still true.
- `[ ]` `(ZZ^3).base_change(ZZ.complete(5))` and `(ZZ^3).base_change(ZZ.localize(5))`
  preserve enriched module behavior.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/completions.py`.

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

## Blocker

- 2026-05-06: Path-local dependency blocker recorded from the Phase 0 dependency order.
  This card depends on `TASK-LAT-PHASE0-MODULE-BASE-RINGS`: its contract refines completion, localization, and fraction-field outputs through the ModuleBaseRings ring-side category path, which is currently blocked on `[[DECISION-LAT-PHASE0-QUOTIENT-SYNTAX-DISPATCH]]`.
- This is not a global blocker for the active goal; continue another approved active leaf
  outside this dependency chain while the prerequisite decision or prerequisite cards
  remain unresolved.

## Current Phase Gate

- 2026-05-06: Blocked by the current category-spec and semantic-vocabulary phase. This
  is implementation-phase Sage/lattice work and must not be executed merely to make
  current Sage objects pass category-obligation examples before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

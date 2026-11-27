---
id: TASK-LAT-PHASE0-IDEAL-QUOTIENT-MODULES
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn:
- '[[TASK-LAT-PHASE0-MODULE-BASE-RINGS]]'
title: Implement ideal-submodule and quotient-module refinement
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
# Implement ideal-submodule and quotient-module refinement

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: ideal_submodule and quotient handling
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/AGENTS.md`

### Public owner and target category
- Owner: `IdealSubmodule` refinement path in `src/sage_patches/ideal_submodule.py`.
- Parent owner: ring-side category is `ModuleBaseRings`, so ideals are treated as
  submodule objects of the ring module and retain module semantics.

### Definitions and hypotheses
- For any target ring `R` in phase-0 scope, a principal ideal `I = (a)` is modeled
  as a submodule of the free module `R` with canonical inclusion map `I ↪ R`.
- `r * R` and `R * r` are aliases for `R.ideal(r)` / `R.ideal(ZZ)` style ideal-submodule
  construction, with `r` allowed from `R` or iterable generators.
- `R / I` is interpreted as quotient by a submodule of a module; equality and
  coercion on ideal codomain must be via quotient-parent category methods.

### Return objects / codomains
- `R.ideal(...)`, `r * R`, and `R * r` return a module parent in
  `Modules(R)` (at least in the enriched `R` contexts).
- `I._as_module()` / internal coercion points produce subobjects that support:
  - base-ring change,
  - submodule inclusion maps,
  - quotient construction in `src/sage_patches/module_operations.py` and `hom_enrichment.py`.

### Concrete implementation work
- Install an ideal submodule category via `_refine_category_` on ideal outputs
  from `ModuleBaseRings` ring operations.
- Ensure `Ring.ideal`, `__mul__`, and `__rmul__` produce the refined ideal-submodule
  type and preserve subobject invariants (domain/range, inclusion map).
- Patch membership hooks so `I in Modules(R)` and `I in Modules(I.base_ring())`
  both hold for ring-ideal module objects.
- Maintain compatibility with existing Sage internals by preserving native quotient and
  coercion behavior while adding category/membership metadata only.

### Acceptance checks
- `[ ]` `I = 2 * ZZ`, `J = ZZ * 2`, and `K = ZZ.ideal(2)` represent the same ideal
  object and satisfy `I == J == K`.
- `[ ]` `I in Modules(ZZ)` and `I in Modules(I)` both true.
- `[ ]` `I <= ZZ` and `I.inclusion().codomain() == ZZ`.
- `[ ]` `(ZZ / I).base_ring() == ZZ` and `(ZZ / I).is_finite()` as expected in FGP checks.
- `[ ]` `isinstance((ZZ / I), Modules(ZZ).category())` style membership checks in
  `tests/sage_spec/misc.sage` remain stable.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/ideal_submodule.py`.

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
  This card depends on `TASK-LAT-PHASE0-MODULE-BASE-RINGS`: its contract treats ideals as submodule objects produced from the ModuleBaseRings ring-side refinement path, which is currently blocked on `[[DECISION-LAT-PHASE0-QUOTIENT-SYNTAX-DISPATCH]]`.
- This is not a global blocker for the active goal; continue another approved active leaf
  outside this dependency chain while the prerequisite decision or prerequisite cards
  remain unresolved.

## Current Phase Gate

- 2026-05-06: Blocked by the current category-spec and semantic-vocabulary phase. This
  is implementation-phase Sage/lattice work and must not be executed merely to make
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

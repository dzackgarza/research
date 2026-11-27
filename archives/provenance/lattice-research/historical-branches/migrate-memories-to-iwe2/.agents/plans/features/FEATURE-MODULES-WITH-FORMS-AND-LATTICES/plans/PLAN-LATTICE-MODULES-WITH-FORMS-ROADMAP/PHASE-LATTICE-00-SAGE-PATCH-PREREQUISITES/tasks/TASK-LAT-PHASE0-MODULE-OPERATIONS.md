---
id: TASK-LAT-PHASE0-MODULE-OPERATIONS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn:
- '[[TASK-LAT-PHASE0-MODULE-ENRICHMENT]]'
title: Implement free torsion and generator operations for enriched modules
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
# Implement free torsion and generator operations for enriched modules

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: module_operations.py -- free_part, torsion_part, generator assignment
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/modules/docs/MAPPING.md`
- `theory/foundations/bilinear-forms-duals-morphisms.md`

### Public owner and target category
- Owner: `src/sage_patches/module_operations.py`.
- Target category: `Modules(R).FinitelyPresented()` and `Modules(R).Free()`
  operations that refine into the redesigned module model.

### Definitions and hypotheses
- Smith normal form invariants control free/torsion decomposition.
- `free_part()` is the maximal free summand of an FGP module.
- `torsion_part()` is the finite-torsion quotient (zero if no torsion factors).
- Generator assignment (`M.<x,y> = ...`) uses `._first_ngens(n)` for ordered ambient generators;
  fallback verification only if native path does not supply this on refined objects.

### Return objects / codomains
- `free_part()` returns an `Modules(R).Free()` parent in the same base ring.
- `torsion_part()` returns a finitely presented torsion parent (e.g. product of cyclic
  quotients or direct-sum torsion summand).
- Generator tuple methods must return `M.gen(i)`-style elements in `M`.
- `invariants()` outputs remain valid and consistent with decomposition.

### Concrete implementation work
- Implement `FGP_Module_class.free_part()`:
  - compute Smith normal form invariants,
  - identify zero-invariant positions as free generators,
  - construct explicit free submodule parent.
- Implement `FGP_Module_class.torsion_part()` from complement invariants with explicit
  canonical presentation.
- Validate and optionally harden `_first_ngens` to preserve the generator-binding flow
  used by Sage preparser (`M.<x,y> = ZZ^n`).
- Keep decomposition methods idempotent under repeated calls and stable under
  parent equivalence in refined categories.

### Acceptance checks
- `[ ]` `M1 = ZZ^2 + ZZ/5` satisfies:
  - `M1.free_part() == ZZ^2`,
  - `M1.torsion_part() == ZZ/5`.
- `[ ]` `M2 = ZZ^3 + ZZ/7` satisfies:
  - `M2.free_part().rank() == 3`,
  - `M2.torsion_part() == ZZ/7`.
- `[ ]` Direct-sum decomposition returns parents in expected `is_free`/`is_torsion` states.
- `[ ]` `M.<x,y,z> = ZZ^3` creates ordered generators and each generator index maps
  to basis embeddings in `M`.
- `[ ]` Smith/invariants of `ZZ/5 + ZZ/3` remain unchanged by recomposition through
  `free_part`/`torsion_part`.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/module_operations.py`.

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
  This card depends on `TASK-LAT-PHASE0-MODULE-ENRICHMENT` because free/torsion decomposition and generator operations must attach to enriched module parents, not raw Sage module parents.
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

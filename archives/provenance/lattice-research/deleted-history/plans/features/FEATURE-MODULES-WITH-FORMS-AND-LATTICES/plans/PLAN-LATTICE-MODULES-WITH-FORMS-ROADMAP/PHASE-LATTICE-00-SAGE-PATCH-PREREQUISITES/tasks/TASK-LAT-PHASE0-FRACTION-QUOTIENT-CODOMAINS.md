---
id: TASK-LAT-PHASE0-FRACTION-QUOTIENT-CODOMAINS
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn: []
title: Research and implement QQ modulo ZZ quotient codomains
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
# Research and implement QQ modulo ZZ quotient codomains

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: fraction_quotients.py -- QQ/ZZ, QQ/nZZ quotient modules
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/forms/docs/MAPPING.md`
- `category_specs/modules/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`

### Public owner and target category
- Owner: `fraction_quotients` patch layer in `src/sage_patches/fraction_quotients.py`.
- Target codomain owners:
  - module form codomain family (`QQ/ZZ`, `QQ/nZZ`) as `Modules(ZZ)` objects,
  - discriminant-bilinear form codomains in `forms` workflows.

### Definitions and hypotheses
- For divisible-group-like codomain, `QmodnZ(1)` is `QQ / ZZ` and `QmodnZ(n)` is
  `QQ / (n*ZZ)`; equality is quotient-class equality.
- Parent must report `base_ring() == ZZ` so it is semantically a `ZZ`-module.
- Objects are additive modules in `Modules(ZZ)` with natural quotient map `x ↦ x mod ZZ`
  and canonical class lift behavior.

### Return objects / codomains
- `QQ / ZZ` returns a `QmodnZ(1)` object in `Modules(ZZ)`.
- `QQ / (n*ZZ)` returns `QmodnZ(n)` in `Modules(ZZ)` for integer/numeric `n`.
- `QQ / (k)` where `k` is an ideal in `ZZ` should normalize through ideal path and
  return the same quotient-class codomain.
- `element` lift/equality must preserve canonical-class representatives (`1/2 == 3/2` in `QmodnZ(1)`).

### Concrete implementation work
- Patch `QQ.__truediv__` (and `RationalField.__truediv__`) to dispatch through:
  - denominator `ZZ` → `QmodnZ(1)`,
  - denominator `n*ZZ` or ideal in `ZZ` → corresponding `QmodnZ(n)`.
- Register `QmodnZ` outputs as module parents:
  - refine category / membership to `Modules(ZZ)`,
  - define `base_ring()` to `ZZ`,
  - preserve coercions from `QQ`.
- Add targeted regression helpers in `install()` to ensure codomain availability before
  form workflows call `FormCodomain.torsion_*` helpers.

### Acceptance checks
- `[ ]` `R = QQ / ZZ` satisfies `R in Modules(ZZ)` and `R(1/2) == R(3/2)`.
- `[ ]` `R = QQ / (2*ZZ)` satisfies `R in Modules(ZZ)` and elements have expected
  torsion order by coercion checks.
- `[ ]` `R(3/2).lift()` returns a `QQ` representative in the expected class.
- `[ ]` `isinstance(QQ / ZZ, ModuleBaseRings category owner)` (or equivalent refined
  module parent check) holds in smoke assertions.
- `[ ]` Discriminant codomain constructor assertions in Phase-1 form tests can instantiate
  `QQ/ZZ` and `QQ/2ZZ` and evaluate `beta(v,w)` there.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/fraction_quotients.py`.

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

## Premature Implementation Cleanup

- 2026-05-06: A premature implementation-phase adapter was created at
  `src/sage_patches/fraction_quotients.py` during spec-phase work. It has been removed
  from `main` by a forward cleanup commit because Sage patches are not current
  executable work.
- The already-done implementation work is intentionally preserved for the later
  implementation phase on remote branch
  `origin/implementation/sage-fraction-quotient-codomains`, rooted at commit
  `cc993dfc34cedfdc4d07387ee78ec86b9bee4d9f` (`feat: refine fraction quotient
  codomains`). Future reintegration should review that branch rather than rewriting
  the adapter from scratch.
- The removed adapter had been a narrow post-processing patch over Sage's existing
  `QQ / ZZ` and `QQ / (n*ZZ)` route through
  `sage.groups.additive_abelian.qmodnz.QmodnZ`; it kept quotient-class arithmetic
  native and only refined returned `QmodnZ` parents into `Modules(ZZ)`.
- The adapter patches `RationalField.__truediv__` only to post-process native
  `QmodnZ` outputs. It does not reimplement quotient arithmetic, canonical lifts,
  equality, or coercions.
- The Phase 0 `ModuleBaseRings` quotient-syntax path remains separately blocked by
  `[[DECISION-LAT-PHASE0-QUOTIENT-SYNTAX-DISPATCH]]`; this card can still reach its
  codomain surface because Sage's rational-field quotient route already exists.

## Superseded Validation

- Superseded premature implementation validation: `sage -python -m py_compile src/sage_patches/fraction_quotients.py` passed before the file was removed.
- `sage -python` witness passed after `install()` and repeated `install()`:
  - `QQ / ZZ in Modules(ZZ)`,
  - `(QQ / ZZ)(1/2) == (QQ / ZZ)(3/2)`,
  - `(QQ / ZZ)(3/2).lift() == QQ(1)/2`,
  - `QQ / (2*ZZ) in Modules(ZZ)`,
  - `(QQ / (2*ZZ))(1/2) == (QQ / (2*ZZ))(5/2)`,
  - `(QQ / (2*ZZ))(5/2).lift() == QQ(1)/2`.
- Full Phase 0 smoke was not run because upstream Phase 0 module-base, ideal, module,
  and hom enrichment cards remain unresolved.

## Current Phase Gate

- 2026-05-06: Blocked by the current category-spec and semantic-vocabulary phase. This
  is implementation-phase Sage/lattice work and must not be executed merely to make
  current Sage objects pass smokes before the ideal specs, method ownership, and
  vocabulary are settled.
- This is a path-local phase gate, not a global blocker for the active goal. Continue
  approved spec, source-mining, audit, and decision leaves outside this implementation
  path.

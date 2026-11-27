---
id: TASK-01KQN9YGCJ26WJ2044DVNVNE87-IMPLEMENT-Q-ADIC-LATTICE-PRECISION-CAP-CONSTRUCTORS-AS-EXPLICIT-BLOCKED
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Implement q-adic lattice precision-cap constructors as explicit blocked Sage-gap surfaces
  rather than broken pass-throughs
status: complete
priority: high
description: Rings mapping records constructor namespace decisions, split p-adic and q-adic
  precision routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
  lattice-precision gaps.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken smokes
  or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with exact
  failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only
  categories.
- For q-adic precision items, preserve the five-field negative finding format when updating
  evidence.
- For topological ring work, check both ring and topological-space category membership.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Implement q-adic lattice precision-cap constructors as explicit blocked Sage-gap surfaces rather than broken pass-throughs
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Implement q-adic lattice precision-cap constructors as explicit blocked Sage-gap surfaces rather than broken pass-throughs from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [x] For topological ring work, check both ring and topological-space category membership.

## Implementation Review

Existing scoped implementation:

- `category_specs/rings/__init__.py` already defines
  `Rings().Constructors().ZqWithPrecisionCaps(...)` and
  `Rings().Constructors().QqWithPrecisionCaps(...)` as admitted public constructor
  names.
- Both constructors require a lattice precision type and then raise an explicit
  assertion explaining that installed Sage has no unramified `Zq`/`Qq` extension
  constructor for split relative/absolute lattice precision caps.
- The implementation uses project vocabulary: `ZqWithPrecisionCaps`,
  `QqWithPrecisionCaps`, `relative_cap`, `absolute_cap`, `lattice relative/absolute
  precision caps`, and `unramified extension`, rather than a Sage fallback helper name.

Smoke/frontier state:

- `category_specs/rings/smoketest.sage` already preserves the exact frontier labels:
  `Constructors().ZqWithPrecisionCaps(25, 4, 8, names='a') is a deferred
  Sage-extension frontier` and the analogous `QqWithPrecisionCaps` label.
- The smoke statements intentionally still expose the frontier if run; this card does
  not narrow the smoke to hide the remaining upstream Sage gap.
- `just --justfile category_specs/justfile smoke-file rings/smoketest.sage` exists and
  currently fails broadly on the ring smoke frontier. The output includes the exact
  `ZqWithPrecisionCaps` and `QqWithPrecisionCaps` deferred Sage-extension labels and
  assertion messages; this is gap evidence, not a reason to weaken the spec.

Source and mapping evidence:

- The five-field q-adic negative finding now lives in `[[SPEC-MAPPING-RINGS]]`.
- Upstream research is recorded in
  `[[TASK-01KQN9YGCQA3E2Y2RAMA2EHZPR-RESEARCH-UPSTREAM-SAGE-SUPPORT-OR-ISSUES-FOR-Q-ADIC-UNRAMIFIED-EXTENSION]]`.
- This is not topological-ring implementation work. No ring/topological-space
  membership changed; the topological inheritance mapping remains in
  `[[SPEC-MAPPING-RINGS]]`.

Spec-weakening review:

- No code, spec, or smoke file was changed in this pass.
- The admitted q-adic split precision names were preserved.
- The remaining Sage gap remains explicit in both implementation assertions and smoke
  frontier labels.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06: Reviewed existing q-adic split-cap constructors and confirmed the
  implementation already records explicit Sage-gap assertions rather than broken
  pass-throughs. Advanced the stale task to review without weakening the smoke
  frontier.

## Review Log

### Review - 2026-05-07

Outcome: scoped review passes; card remains `needs-agent-review` for human acceptance.

- Verified `category_specs/rings/__init__.py` preserves admitted public constructor
  names `ZqWithPrecisionCaps(...)` and `QqWithPrecisionCaps(...)` under
  `Rings().Constructors()`.
- Focused runtime probes for both constructors raise the intended `AssertionError`
  messages: installed Sage has no unramified `Zq`/`Qq` extension constructor for split
  lattice relative/absolute precision caps, so the admitted names stay deferred until
  Sage exposes a lattice-precision extension route.
- Verified `SPEC-MAPPING-RINGS.md` contains the five-field negative finding for this
  q-adic lattice-precision gap and that the companion spec card preserves the admitted
  names as deferred frontiers rather than deleting or renaming them.
- Ran `just --justfile category_specs/justfile smoke-file rings/smoketest.sage`; it
  fails on the current ring smoke frontier, including the exact q-adic deferred-frontier
  labels and assertion messages. Broader ring smoke failures such as
  `hilbert_polynomial`, `completion`, `_change_print_mode`, and `algebraic_closure`
  remain separate frontier evidence, not blockers for this scoped q-adic leaf.
- This card does not change topological-ring behavior. The topological membership
  criterion is inherited parent context and is not the operative acceptance surface for
  this q-adic deferred-constructor review.

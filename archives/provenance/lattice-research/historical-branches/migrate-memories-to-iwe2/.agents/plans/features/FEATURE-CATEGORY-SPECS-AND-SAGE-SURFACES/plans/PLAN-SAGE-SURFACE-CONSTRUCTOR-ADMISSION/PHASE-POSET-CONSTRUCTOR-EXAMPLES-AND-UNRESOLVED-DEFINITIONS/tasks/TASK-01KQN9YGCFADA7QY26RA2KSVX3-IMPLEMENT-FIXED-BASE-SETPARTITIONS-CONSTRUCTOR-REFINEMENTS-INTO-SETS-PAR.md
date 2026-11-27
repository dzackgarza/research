---
id: TASK-01KQN9YGCFADA7QY26RA2KSVX3-IMPLEMENT-FIXED-BASE-SETPARTITIONS-CONSTRUCTOR-REFINEMENTS-INTO-SETS-PAR
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
dependsOn: []
title: Implement fixed-base SetPartitions constructor refinements into Sets().Partitioned()
  and keep AllSetPartitions countable-only
status: complete
priority: high
description: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  category-obligation examples or mapping decisions to make failures disappear.
- Relevant category-obligation output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS
---
# Implement fixed-base SetPartitions constructor refinements into Sets().Partitioned() and keep AllSetPartitions countable-only
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Implement fixed-base SetPartitions constructor refinements into Sets().Partitioned() and keep AllSetPartitions countable-only from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken category-obligation examples or mapping decisions to make failures disappear.
- [x] Relevant category-obligation output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Implementation Result

- Registered the set-partition axioms `Partitioned` and `FiniteTotallyOrderedBase` in
  `category_specs/axioms.py`.
- Made `Sets().Partitioned().FiniteTotallyOrderedBase()` reachable as the scoped
  subcategory method from `PartitionedSetsCategory`.
- Centralized fixed-base `SetPartitions` refinement categories in
  `Sets.Constructors._set_partitions_categories(...)`.
- Kept `Sets().Constructors().AllSetPartitions()` refined only through `Sets()` and
  `Sets().Countable()`.
- Refined the Sage integer fixed-base routes `SetPartitions(3)`,
  `SetPartitionsWithBlockCount(3, 2)`, and
  `SetPartitionsWithBlockSizes(3, [2, 1])` into
  `Sets().Partitioned().FiniteTotallyOrderedBase()` because Sage's integer route has
  the standard finite ordered base `{1, ..., n}`. Iterable routes remain only
  `Sets().Partitioned()` and do not use raw Python ordering as category evidence.

## Validation Notes

- `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passed with
  the pre-existing Sage inherited `Sets.Topological` warning.
- `just --justfile category_specs/justfile check-abstract-redefinitions` passed.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Implemented the fixed-base partition refinement route, added category-obligation example
  assertions proving `AllSetPartitions()` is not fixed-base `Partitioned`, and proved
  integer fixed-base partition constructors refine through
  `Sets().Partitioned().FiniteTotallyOrderedBase()`.

## Review Log

### Review - 2026-05-07

Outcome: scoped review passes; card remains `needs-agent-review` for human acceptance.

- Verified `SPEC-MAPPING-SETS.md` rows for `SetPartitions(s)`,
  `SetPartitions(s, k)`, `SetPartitions(s, part)`, and `SetPartitions()`:
  fixed-base parents route through `Sets().Partitioned()`, integer fixed-base routes
  also route through `Sets().Partitioned().FiniteTotallyOrderedBase()`, and
  all-finite-partitions route only through `Sets().Countable()`.
- Verified `category_specs/sets/__init__.py` centralizes fixed-base partition
  constructor categories in `Sets.Constructors._set_partitions_categories(...)` and
  distinguishes integer cardinality bases from iterable or set-object bases.
- Verified `category_specs/sets/subcategories/partitioned.py` records
  `FiniteTotallyOrderedBase` as an axiom on `Sets().Partitioned()`, with
  supercategories `Sets().Partitioned()` and `Sets().Countable().Finite()`.
- `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passed
  with the pre-existing inherited `Sets.Topological` warning.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Completeness, Gate 2 Correctness, Gate 3 Consistency, Gate 4 Coverage, Gate 5 Non-regression, Gate 6 Artifact Quality

**Gates failed:** none

**Outcome:** complete. All six gates pass.

- Gate 1: Partitioned/FiniteTotallyOrderedBase in axioms.py. Constructor dispatch centralized in `_set_partitions_base`. AllSetPartitions only through Sets() + Countable().
- Gate 2: Mathematical reasoning sound for all dispatch cases (SageInteger→FiniteTotallyOrderedBase, CategoryObject→Partitioned, Iterable→Partitioned).
- Gate 3: Project conventions followed (LazyImport, @final, CategoryWithAxiom_singleton).
- Gate 4: All SPEC-MAPPING-SETS.md rows for SetPartitions implemented and verified.
- Gate 5: `just check-abstract-redefinitions` passes. `just category-obligation-file sets/category_obligations.sage` passes.
- Gate 6: Docstrings present. Source provenance cited. Clean commit history.

Verification: `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passes.

---
id: TASK-01KQN9YGCG1916T40B7XTZX9MH-IMPLEMENT-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FI
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS]]'
dependsOn: []
title: Implement partition refinements coarsenings and strict coarsenings as finite-set
  constructor outputs
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
# Implement partition refinements coarsenings and strict coarsenings as finite-set constructor outputs
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- Canonical mapping rows:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md:282-286`
  for `SetPartitions(s)` and `SetPartition(blocks, check=True)`, and
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md:360-382`
  for partition-element operations, `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()`.
- Grounded spec card:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC8WM34SAME35N4VGX5-SPECIFY-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FINI.md`.
- Source inventory: `category_specs/sets/docs/SAGE_INVENTORY.md`.
- Original migrated line: `Implement partition refinements coarsenings and strict coarsenings as finite-set constructor outputs from category_specs/sets/docs/MAPPING.md`

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

## Path-Local Blocker

Resolved by `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md`.

Preflight evidence:

- Sage source defines concrete `SetPartition.refinements()`,
  `SetPartition.coarsenings()`, and `SetPartition.strict_coarsenings()` in
  `sage/combinat/set_partition.py`.
- After refining the fixed-base parent through project constructors,
  `C.SetPartitions(3)([[1,3],[2]]).refinements()` still returns a Python `list`.
- Therefore adding ordinary category `ElementMethods` with the same method names would
  not change runtime behavior; Sage's element-class methods shadow the category method
  provider.

Decision outcome:

- Keep Sage's concrete `refinements()`, `coarsenings()`, and
  `strict_coarsenings()` as list-returning compatibility methods.
- Add project finite-set methods `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()`.
- Forbid hidden monkeypatching of Sage `SetPartition`.

## Implementation Result

- Updated `category_specs/sets/docs/MAPPING.md` to distinguish Sage compatibility
  method names from project finite-set method names.
- Updated `category_specs/sets/subcategories/partitioned.py`:
  `refinement_set()` and `coarsening_set()` live on
  `Sets().Partitioned().ElementMethods`, and
  `ordered_coarsening_closure()` lives on
  `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`.
- Each project method routes the corresponding Sage list through
  `Sets().Constructors().from_iterable(...)`, producing a project finite set object
  without changing Sage element construction or parent behavior.
- Added set category-obligation examples proving the three project methods return finite countable set
  objects and include the source partition.

## Validation Notes

- `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passed with
  the known Sage inherited `Sets.Topological` axiom warning.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Preflighted the implementation route and found a Sage concrete-method
  shadowing issue. Created
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md` and blocked
  this leaf until the project chooses wrapper, renamed project methods, monkeypatch, or
  spec-revision strategy.
- 2026-05-05: Implemented the decision route using separate project finite-set method
  names and moved this card to in-review.

## Review Log

### Review 2026-05-06 (Epicurus)

**Gates passed:** None
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Stale Mapping Anchors

- The task cited `category_specs/sets/docs/MAPPING.md` as provenance even though that
  file is now only a redirect to the tracked canonical mapping spec.
- The linked specification cited stale `category_specs/sets/docs/MAPPING.md` line
  anchors rather than the current canonical rows in `SPEC-MAPPING-SETS.md`.

#### Rework

- Updated this task's Source Provenance to cite the canonical tracked
  `SPEC-MAPPING-SETS.md` rows for fixed-base partition constructors and partition
  element methods.
- Updated the grounded spec card to cite current `SPEC-MAPPING-SETS.md` anchors for
  owner, hypotheses, codomain, and compatibility-name split.

### Re-review 2026-05-06 (Aristotle)

**Gates passed:** Gates 1-6
**Gates failed:** None
**Outcome:** needs-agent-review evidence ready for human approval; card not marked complete

#### Evidence

- Canonical grounding is now in this task's Source Provenance and the linked spec's
  Grounded Spec Contract, backed by current `SPEC-MAPPING-SETS.md` rows for fixed-base
  partition constructors and partition element methods.
- Owner, hypotheses, codomain, and migration consequence are recorded in the linked
  spec, with `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()` kept as project finite-set methods separate from
  Sage's list-returning compatibility names.
- Implementation and category-obligation example evidence match the admitted surface in
  `category_specs/sets/subcategories/partitioned.py` and
  `category_specs/sets/category_obligations.sage`.
- Validation: `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage`
  passed with only the known inherited `Sets.Topological` Sage warning.

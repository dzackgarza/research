---
id: DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide how partition element methods override Sage list-returning methods
status: decided
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide how partition element methods override Sage list-returning methods

## Summary

The partition refinement implementation card requires `refinements()`,
`coarsenings()`, and `strict_coarsenings()` to return project finite set objects.
Installed Sage already defines those concrete methods on the `SetPartition` element
class and returns Python lists. Ordinary category `ElementMethods` refinement cannot
override concrete methods already present on the Sage element class.

## Source Provenance

- Blocking card:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-POSET-CONSTRUCTOR-EXAMPLES-AND-UNRESOLVED-DEFINITIONS/tasks/TASK-01KQN9YGCG1916T40B7XTZX9MH-IMPLEMENT-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FI.md`
- Spec leaf:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC8WM34SAME35N4VGX5-SPECIFY-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FINI.md`
- Mapping anchors:
  - `category_specs/sets/docs/MAPPING.md`, rows for `refinements()`,
    `coarsenings()`, and `strict_coarsenings()`
  - `category_specs/sets/subcategories/partitioned.py`
- Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/combinat/set_partition.py`

## Context

`Sets().Partitioned().ElementMethods` records the project surface, but Sage's concrete
`SetPartition` element class already owns the same method names. A direct probe after
refining the fixed-base parent still shows:

```text
type(C.SetPartitions(3)([[1,3],[2]]).refinements()) == list
```

That means a normal category-method patch would document the desired surface but not
change runtime behavior.

## Decision Grounding Required

Before moving this decision to `decided`, choose the implementation route and record
the effect on public partition-element vocabulary:

- whether to introduce a true project `SetPartition` element wrapper/subclass and have
  fixed-base parents construct wrapped elements;
- whether to keep Sage names list-returning for interop and add project finite-set
  names such as `refinement_set()` / `coarsening_set()`;
- whether a localized monkeypatch of Sage `SetPartition` is acceptable in this spec
  layer; or
- whether the mapping/spec should be revised because the runtime surface cannot safely
  claim the Sage method names with different codomains.

## Decision

Use separate project finite-set method names and keep Sage's concrete names as Sage
compatibility methods:

- `refinements()` stays the Sage list-returning concrete method.
- `coarsenings()` stays the Sage list-returning concrete method.
- `strict_coarsenings()` stays the Sage list-returning concrete method whose ordered
  reflexive closure semantics are preserved as Sage compatibility behavior.
- Project finite-set surfaces are `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()`.

This route preserves Sage element class behavior, avoids hidden monkeypatching, and
keeps the project codomain claim true at runtime. The project methods route Sage's
concrete list outputs through `Sets().Constructors().from_iterable(...)`, so the public
project surface returns finite set objects of partition elements.

Rejected routes:

- True `SetPartition` element wrapper/subclass: viable later, but too heavy for this
  leaf because it would require changing fixed-base parent element construction while
  preserving Sage membership, coercion, and parent behavior.
- Local monkeypatching of Sage `SetPartition`: rejected because it would silently alter
  upstream concrete methods and create an audit hazard.
- Keeping the project spec on the Sage names with different codomains: rejected because
  ordinary category `ElementMethods` do not override concrete methods on the installed
  Sage element class.

Consequences:

- `category_specs/sets/docs/MAPPING.md` must map the Sage names to compatibility
  behavior and the project finite-set names to the category surface.
- `category_specs/sets/subcategories/partitioned.py` must expose
  `refinement_set()`, `coarsening_set()`, and `ordered_coarsening_closure()` instead of
  abstract methods named `refinements()`, `coarsenings()`, and `strict_coarsenings()`.
- The blocked implementation card can resume by implementing the separate project
  method names; it must not claim that Sage's concrete names return project finite set
  objects.

## Acceptance Criteria

- [x] The chosen route states whether public method names stay
  `refinements()`, `coarsenings()`, and `strict_coarsenings()` or move to separate
  project names.
- [x] The decision records how element construction through
  `Sets().Constructors().SetPartitions(...)` preserves Sage membership and parent
  behavior.
- [x] The decision forbids hidden monkeypatching unless the rationale and audit
  surface are explicitly accepted.
- [x] The implementation card can either resume with a concrete write path or be
  revised/superseded without weakening the partition mapping silently.

## Dependencies And Boundaries

- Do not expose a generic Sage `Set(X)` constructor.
- Do not make `strict_coarsenings()` mean ordinary proper coarsening; Sage's method is
  reflexive and order-dependent.
- Do not treat this as a blocker for unrelated approved phase-01 leaves.

## Work Log

- 2026-05-05: Created after implementation preflight showed Sage concrete
  `SetPartition` methods shadow category `ElementMethods` and still return Python
  lists after parent refinement.
- 2026-05-05: Decided to keep Sage names as list-returning compatibility methods and
  add separate project finite-set names: `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()`.

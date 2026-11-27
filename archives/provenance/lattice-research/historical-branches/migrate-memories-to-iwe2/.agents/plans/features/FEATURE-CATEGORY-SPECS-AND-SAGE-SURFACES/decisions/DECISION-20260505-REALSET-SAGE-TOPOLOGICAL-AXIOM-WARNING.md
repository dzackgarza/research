---
id: DECISION-20260505-REALSET-SAGE-TOPOLOGICAL-AXIOM-WARNING
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide how to handle Sage RealSet inherited Sets.Topological axiom warning
status: decided
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide how to handle Sage RealSet inherited Sets.Topological axiom warning

## Summary

`just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` now passes, but
the RealSet rows still emit Sage's warning:
`Expecting Sets.Topological to be a subclass of CategoryWithAxiom ... got
sage.categories.topological_spaces.TopologicalSpaces`.

The functional failed category assertions is clear. The remaining decision is how the project
should treat the original Sage `RealSet` category provenance when refining RealSet
objects into the local topological hierarchy.

## Source Provenance

- Blocking card:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES/tasks/TASK-01KQN9J3X04R2PWJADC8B4EF9A-FIX-SETS-ROOT-CONTAINMENT-REFINED-CONSTRUCTOR-RICHCMP-PRIMES-ITERATION-R.md`
- Implementation commit: `983a058`
- Tracker synchronization commit: `f606652`
- Mapping anchors:
  - `category_specs/sets/docs/MAPPING.md`
  - `category_specs/topological_spaces/docs/MAPPING.md`
  - `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`

## Context

The warning is not a failed category assertion. It is emitted by Sage category machinery
while RealSet objects carry their original Sage `TopologicalSpaces()` category join.
Local attempts to remove direct Sage topological supercategory references and override
project topological construction-category joins reduced warning exposure in
`topological_spaces/category_obligations.sage`, but the Sets category-obligation example still reaches the warning
through the original Sage `RealSet` category provenance.

## Decision Grounding Required

This decision cannot be settled by hiding the warning or by weakening the category-obligation example. Before
moving to `decided`, record:

- exact Sage source path and call stack for the warning;
- whether project refinement may replace or strip an object's original Sage category
  provenance without losing necessary Sage parent methods;
- whether local construction-category joins should special-case Sage's non-axiom
  `TopologicalSpaces()` category;
- whether the warning should instead be accepted and documented as inherited Sage
  behavior until owned RealSet carriers exist.

Negative findings must use the five-field search format.

## Options

- Replace or strip the original Sage `RealSet` category during refinement.
- Patch local construction-category joins to avoid applying the `Topological` axiom to
  Sage `Sets()` supercategories reached through original RealSet provenance.
- Accept and document the warning as inherited Sage behavior while keeping functional
  category-obligation example passing until the owned categorical implementation phase.

## Acceptance Criteria

- [x] The decision lists the chosen option, rationale, and affected implementation or
  documentation cards.
- [x] The decision states whether the root Sets category-obligation card can move from `blocked` to
  `in-review` with the warning documented, or whether a concrete implementation card
  must clear the warning.
- [x] Any implementation consequence preserves the admitted RealSet constructor surface
  and does not reintroduce catch-all `Constructors().RealSet`.
- [x] Any accepted warning is documented in the owning card or mapping docs rather than
  buried in chat.

## Dependencies And Boundaries

- Do not use this decision to add a pure `TopologicalSpaces().Constructors()` namespace.
- Do not weaken or remove RealSet category-obligation example rows.
- Do not treat this as a blocker for unrelated approved phase-01 spec, research,
  implementation, or audit leaves.

## Work Log

- 2026-05-05: Created after commit `983a058` cleared functional Sets failed category assertions but
  left Sage's inherited `Sets.Topological` warning on the RealSet path.
- 2026-05-05: Reproduced and traced the warning; decided to accept and document it as
  inherited Sage category-provenance behavior during the current spec phase.

## Sources Reviewed

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES/tasks/TASK-01KQN9J3X04R2PWJADC8B4EF9A-FIX-SETS-ROOT-CONTAINMENT-REFINED-CONSTRUCTOR-RICHCMP-PRIMES-ITERATION-R.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/topological_spaces/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`
- `category_specs/sets/category_obligations.sage`
- `category_specs/sets/__init__.py`
- `category_specs/sets/subcategories/real_set.py`
- `category_specs/topological_spaces/__init__.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/real_set.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/topological_spaces.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/sets_cat.py`
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category.py`

## Reproduction And Stack

`just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passes and
emits the warning from Sage category machinery:

```text
/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category.py:2074:
UserWarning: Expecting Sets.Topological to be a subclass of CategoryWithAxiom ...
got <class 'sage.categories.topological_spaces.TopologicalSpaces'>; ignoring
```

Promoting the warning to an exception with a minimal RealSet constructor call gives
this stack:

- `category_specs/sets/__init__.py:593`,
  `Constructors.RealSetFromIntervals(...)`;
- `category_specs/sets/__init__.py:579`, `_refine_real_subset(...)`;
- `category_specs/utils.py:107`, `refine_category(...)`;
- Sage `Parent._refine_category_`;
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category.py:2525`,
  `Category.join(...)`;
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category.py:2079-2081`,
  `_with_axiom_as_tuple(...)` recursing through supercategories;
- `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/category.py:2074`,
  the warning branch.

Sage `RealSet.__init__` assigns original category provenance in
`sage/sets/real_set.py:1299-1316`: a `RealSet` starts in Sage
`TopologicalSpaces()`, then may refine through Sage `Connected`, `Subobjects`,
`Finite`, `Infinite`, or `Compact` according to interval data.

The local constructor then refines that existing Sage parent with project categories
from `category_specs/sets/__init__.py:544-579`, including `Sets().Topological()`,
`_RealSets()`, and topological subobject refinements. Sage's installed
`Sets.Topological` attribute is `sage.categories.topological_spaces.TopologicalSpaces`,
a regressive construction-category class, not a `CategoryWithAxiom` subclass. When the
join combines the original Sage topological provenance with the local project
`Topological` axiom, Sage tries to reapply the `Topological` axiom through Sage
`Sets` and warns that its own `Sets.Topological` is not axiom-shaped.

## Decision

Accept and document the warning as inherited Sage category-provenance behavior for the
current spec phase. The root Sets category-obligation card may move from `blocked` to `in-review`
with this warning recorded.

Do not strip or replace the original Sage `RealSet` category provenance in this pass.
Do not add a local special-case around Sage's construction-category join machinery in
this pass. Do not reintroduce the rejected catch-all `Sets().Constructors().RealSet`
route, and do not weaken or remove the RealSet category-obligation example rows.

## Rationale

The warning is not an assertion failure and not evidence that the admitted RealSet
constructor surface is semantically wrong. It is emitted while Sage computes a category
join during refinement, and Sage explicitly ignores the non-axiom `Sets.Topological`
path after warning.

Replacing or stripping the original Sage category would hide useful provenance from
`sage.sets.real_set.RealSet`: Sage's constructor records connected, compact, finite,
infinite, subobject, and topological category facts at object construction. Removing
that category in a spec-phase category-obligation example fix would be a larger carrier-design decision, not
a local warning cleanup.

Special-casing the join path locally would also be the wrong layer for this phase. The
underlying mismatch is between Sage's construction-category model for
`TopologicalSpaces()` and the project axiom-category wrapper. A local suppression would
risk hiding real category-join problems elsewhere while only improving a passing category-obligation example
log.

Owned RealSet carriers in the later implementation phase can avoid this mixed
provenance problem by constructing local objects directly in the project category
hierarchy. Until then, keeping the warning visible and documented is safer than
mutating Sage provenance or adding a suppression path.

## Consequences

- The blocking Sets category-obligation card can move to `in-review`; the functional failed category assertions
  is cleared, and the residual warning is documented here and on that card.
- The admitted RealSet constructor surface remains the named set-constructor family:
  `RealSetFromIntervals`, `RealSetInterval`, interval/ray/point constructors, and
  `RealLine`.
- The rejected catch-all `Sets().Constructors().RealSet(...)` route remains rejected.
- Future implementation work may revisit this only as owned RealSet-carrier work or a
  carefully scoped category-bridge design card, not as incidental category-obligation example cleanup.

## Affected Tracker Items

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES/tasks/TASK-01KQN9J3X04R2PWJADC8B4EF9A-FIX-SETS-ROOT-CONTAINMENT-REFINED-CONSTRUCTOR-RICHCMP-PRIMES-ITERATION-R.md`

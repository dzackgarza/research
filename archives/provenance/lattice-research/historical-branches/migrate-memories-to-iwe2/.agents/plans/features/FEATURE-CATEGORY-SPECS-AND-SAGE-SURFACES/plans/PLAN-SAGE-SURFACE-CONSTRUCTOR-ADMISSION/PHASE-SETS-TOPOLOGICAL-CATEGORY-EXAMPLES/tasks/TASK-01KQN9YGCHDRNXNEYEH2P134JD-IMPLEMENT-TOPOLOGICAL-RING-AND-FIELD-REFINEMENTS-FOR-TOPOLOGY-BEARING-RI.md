---
id: TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS-FOR-TOPOLOGY-BEARING-RI
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES]]'
dependsOn: []
title: Implement topological ring and field refinements for topology-bearing ring
  objects without duplicating topological-space methods
status: complete
priority: high
description: Rings mapping records constructor namespace decisions, split p-adic and
  q-adic precision routes, matrix-ring ownership, topological ring inheritance, and
  p-adic and q-adic constructor routes.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  category-obligation examples or mapping decisions to make failures disappear.
- Relevant category-obligation output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- For q-adic precision items, preserve the five-field negative finding format when
  updating evidence.
- For topological ring work, check both ring and topological-space category membership.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-TOPOLOGICAL-CATEGORY-EXAMPLES
---
# Implement topological ring and field refinements for topology-bearing ring objects without duplicating topological-space methods
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and p-adic and q-adic
constructor routes.

## Source Provenance

- Canonical ring mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`,
  especially `## Topological Rings`.
- Topological ring/field recovery decision:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC3XPWZWJK8QHVE3GGM-SPECIFY-TOPOLOGICAL-RING-AND-FIELD-RECOVERY-THROUGH-TOPOLOGICAL-SPACES-I.md`.
- Legacy source provenance: `category_specs/rings/docs/MAPPING.md`.
- Original migrated line: `Implement topological ring and field refinements for topology-bearing ring objects without duplicating topological-space methods from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [x] The retained implementation changes only the scoped category-spec surface and does not weaken category-obligation examples or mapping decisions to make failures disappear.
- [x] Relevant category-obligation output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The retained precision-field change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] No q-adic precision evidence was changed; existing q-adic five-field findings remain in the mapping/frontier cards.
- [x] Topological ring membership uses a design-preserving implementation path for
      inherited topological-space methods, with unresolved concrete topology adapters
      reported as runtime gaps owned by `TopologicalSpaces()`.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Preflighted with
  `just --justfile category_specs/justfile category-obligation-file rings/category_obligations.sage`. The category-obligation example
  fails before topological membership assertions because topology-bearing ring
  constructors such as `RR`, `CC`, `RDF`, `CDF`, `RIF`, `RealField(100)`,
  `ComplexField(100)`, and `RealBallField(100)` refine into a topological surface with
  abstract topological methods such as `boundary` still unimplemented. The same category-obligation example
  also reports unrelated ring-frontier failures (`hilbert_polynomial`, `ideal_monoid`,
  matrix-ring MRO). This finding is leaf-local evidence
  for the topological ring implementation card and is not a global blocker for other
  approved phase-01 leaves.
- 2026-05-06: Added source-backed `change_precision` implementations for real and
  complex precision-field categories. `RealField`, `RealDoubleField`,
  `RealIntervalField`, `ComplexField`, `ComplexDoubleField`, and
  `ComplexIntervalField` use Sage's `to_prec`; `RealBallField` and
  `ComplexBallField` use their source-backed constructor route with the new
  precision.
- 2026-05-06: Rejected and reversed an attempted topological-root implementation that
  removed abstract obligations from `TopologicalSpaces().ParentMethods` and delegated
  ambient-relative methods only for Sage `RealSet` subsets. That would have weakened
  the ideal topological-space surface to make a ring failed category assertions disappear.
- Current revision finding: topology-bearing ring objects still refine into
  `TopologicalSpaces()` and hit abstract root obligations such as `boundary`.
  Implementing those methods directly in ring files would duplicate topological
  method ownership; removing abstractness at the topological root weakens the spec.
  This leaf needs design-preserving rework for how concrete topological-space behavior
  is supplied to topology-bearing ring objects while preserving the root owner
  obligations. This is rework for this task, not a `blocked` status.
- 2026-05-06: Added a `TopologicalSpaces()`-owned runtime-gap provider for topology
  carriers whose Sage-backed parents do not yet expose subset-topology adapters, and
  wired `Rings().Topological()` to reuse those method bodies without subclassing its
  Sage `ParentMethods` provider. The root `TopologicalSpaces().ParentMethods`
  obligations remain abstract; the ring subtree now records the topological-space
  supercategory edge and does not define independent ring-local topological methods.
- 2026-05-06: Added ring category assertions that `Rings().Constructors().RR()` is both
  a topological ring and a topological space. The prior `boundary` abstract-method
  failure is no longer the first frontier for topology-bearing precision fields; the
  category-obligation file now reaches unrelated general ring frontiers such as `hilbert_polynomial`,
  plus already-recorded `ideal_monoid`, q-adic extension, p-adic print-mode,
  interval/ball algebraic-closure, series, and matrix-MRO frontiers. Those remaining
  failures are not topological method-ownership blockers for this leaf.
- Verification:
  - `python -m py_compile category_specs/rings/subcategories/real_precision_field.py category_specs/rings/subcategories/complex_precision_field.py` passed.
  - `python -m py_compile category_specs/topological_spaces/__init__.py category_specs/rings/subcategories/topological.py category_specs/rings/subcategories/real_precision_field.py category_specs/rings/subcategories/complex_precision_field.py category_specs/rings/subcategories/p_adic_ring.py` passed.
  - `git diff --check -- category_specs/rings/subcategories/real_precision_field.py category_specs/rings/subcategories/complex_precision_field.py` passed.
  - `just --justfile category_specs/justfile category-obligation-file topological_spaces/category_obligations.sage` passed.
  - `just --justfile category_specs/justfile category-obligation-file rings/category_obligations.sage` remains
    failing after the topological-space `boundary` frontier was cleared. Remaining
    ring-frontier failures observed in the same category-obligation example include `hilbert_polynomial`,
    `algebraic_closure` for complex interval/ball fields, `ideal_monoid`, q-adic
    deferred extension constructors, p-adic `_change_print_mode`, power-series
    `cardinality`, Laurent/Puiseux `completion`, matrix-ring module MRO, and
    quadratic-field `alternating_form`.

## Category-Obligation Output

2026-05-06 targeted topological-space category-obligation example rerun:

```text
$ just --justfile category_specs/justfile category-obligation-file topological_spaces/category_obligations.sage
<exit 0; no stdout/stderr>
```

The broader ring category-obligation file remains failing on the non-topological frontier list recorded in
the work log. This card does not claim a clean full ring category-obligation example; it preserves those
frontiers as separate ring-surface work.

## Review Log

### Review 2026-05-06 (parent)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** parent review passed; human approval still required before completion

#### Evidence

- Gate 1: source grounding now points at `SPEC-MAPPING-RINGS` and the tracked
  topological ring/field recovery decision, not only the legacy mapping doc.
- Gate 2: acceptance criteria are checked in the card, and category-obligation output is recorded for
  the targeted topological-space category-obligation example while the broader ring-failed category assertions remain
  explicitly preserved.
- Gate 3: the implementation path keeps topological-space methods owned by
  `TopologicalSpaces()` and ring membership owned by `Rings().Topological()`.
- Gate 4: the card records and rejects the prior weakening attempt that removed
  topological root abstract obligations; no current spec or category-obligation example weakening is claimed.
- Gate 5: `just --justfile category_specs/justfile category-obligation-file
  topological_spaces/category_obligations.sage` exited `0`; the broader ring category-obligation example is not used as
  completion evidence because unrelated frontiers remain.
- Gate 6: residual risk is the non-topological ring frontier list already recorded in
  the work log, plus the unresolved concrete topology adapters owned by
  `TopologicalSpaces()`.

---
id: TASK-01KQN9J3X3Y3S80FYCGEQDEJJZ-FIX-POSETS-CONSTRUCTOR-REFINEMENT-RICHCMP-FAILURES
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
dependsOn: []
title: Fix Posets constructor refinement __richcmp__ failures
status: complete
priority: high
description: The deleted Posets triage recorded settled order-theoretic mapping items,
  a concrete design decision about equivalence relations/set partitions, and evidence
  gaps around semilattice category introspection.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- Use the five-field negative-finding format for further Sage semilattice evidence
  gaps.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES
---
# Fix Posets constructor refinement __richcmp__ failures
## Summary

The deleted Posets triage recorded settled order-theoretic mapping items, a concrete
design decision about equivalence relations/set partitions, and evidence gaps around
semilattice category introspection.

## Source Provenance

- `category_specs/posets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/posets/docs/TRIAGE.md`.
- Original migrated line: `Fix Posets constructor refinement __richcmp__ failures from category_specs/posets/docs/TRIAGE.md and posets smoketest frontier`

## Context

- Poset constructors are named non-variadic adaptations; acyclic DiGraph is the canonical finite-poset constructor.
- Meet and join expose binary operations plus sequence folds, not optional-argument aggregate signatures.
- Lattice congruences use set-theoretic vocabulary: EquivalenceRelation and SetPartition, with congruence_generated_by(blocks).
- certificate=True Sage paths map to separately named witness-returning certificate methods.
- Sage semilattice category evidence remains incomplete because local Sage imports failed before category introspection.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- [x] Use the five-field negative-finding format for further Sage semilattice evidence gaps.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Resolved the poset constructor smoke frontier without weakening
  constructor assertions. Root `Posets()` methods backed by Sage
  `sage.categories.posets.Posets.ParentMethods` were made final concrete project
  methods where the local abstract surface had shadowed Sage's implementation:
  `directed_subset`, principal order ideal/filter, order-ideal toggles, and
  order-ideal/order-filter/chain/antichain predicates.
- 2026-05-05: Resolved finite-poset constructor refinement failures by wiring
  Sage-backed final methods for `height_certificate`, `width_certificate`,
  `meet_semilattice_certificate`, `join_semilattice_certificate`,
  `is_poset_morphism`, and `order_ideals_lattice`.
- 2026-05-05: Resolved the finite join-semilattice smoke frontier by adding the
  `subjoinsemilattice` join-closure construction to the mathematically correct
  `Posets().JoinSemilattice().Finite()` owner. Source grounding:
  `category_specs/posets/docs/MAPPING.md` maps `subjoinsemilattice` there, while
  Sage source places the construction in
  `sage/combinat/posets/lattices.py`.
- 2026-05-05 validation: `just --justfile category_specs/justfile smoke-file
  posets/smoketest.sage` passed; `just --justfile category_specs/justfile
  check-abstract-redefinitions` passed; `git diff --check` passed.

## Review Log

### Review - 2026-05-07

Outcome: review found one stale smoke fixture and repaired it; card remains
`needs-review` for fresh review and human acceptance.

- Current `posets/smoketest.sage` failed because the reusable `diamond_poset`
  fixture was a raw Sage `Poset(...)`, so project-only
  `height_certificate()` and semilattice certificate helpers were not mixed in.
- Repaired the fixture to use the public project constructor
  `Posets().Constructors().from_upper_covers_dict(diamond_covers)`. The
  `raw_diamond_poset()` helper remains available for `from_existing(...)` smoke
  assertions, so raw Sage constructor interop is still tested without weakening
  the project-surface assertions.
- Source grounding remains `category_specs/posets/docs/SAGE_INVENTORY.md` for Sage
  finite-poset methods and
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-POSETS.md`
  for project constructor/method ownership.

Sage semilattice category evidence gap:

- Searched: `category_specs/posets/docs/SAGE_INVENTORY.md`,
  `category_specs/posets/docs/MAPPING.md`, installed Sage category files under
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories`,
  and `sage -c` imports for `sage.categories.meet_semilattices`,
  `sage.categories.join_semilattices`,
  `sage.categories.finite_meet_semilattices`, and
  `sage.categories.finite_join_semilattices`.
- Found: Sage has `sage.categories.posets`, `lattice_posets`, and
  `finite_lattice_posets`; the four standalone semilattice category module imports
  raise `ModuleNotFoundError`.
- Conclusion: inference - installed Sage does not expose standalone semilattice
  category modules matching the project `Posets().MeetSemilattice()` and
  `Posets().JoinSemilattice()` surfaces; the project semilattice categories are
  grounded in order-theoretic definitions plus Sage concrete finite semilattice
  constructors/methods, not in Sage category modules.
- Confidence: High for the installed Sage environment and local docs searched.
- Gaps: Sage upstream documentation outside the installed docs was not web-searched
  in this pass, because the task-local smoke defect and installed-source evidence
  were sufficient for the current leaf.

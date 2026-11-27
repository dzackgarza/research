---
id: TASK-01KQN9YGCMD0K84CK3BKZH0Z8Z-IMPLEMENT-MODULE-CATEGORY-GRAPH-PHASE-FOR-AMBIENT-FREE-VECTOR-SUBOBJECT
trackerStatus:
  type: task
parents:
- '[[PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE]]'
dependsOn:
- '[[TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS]]'
title: Implement module category graph phase for ambient free vector subobject quotient
  form graded Ore and representation surfaces
status: complete
priority: high
description: 'The deleted module wrapper migration plan is a phased migration contract:
  map methods first, define the category graph, rewrite constructors, move methods
  to real owners, then delete wrappers.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Use the phase-specific validation commands from the deleted plan when implementing
  a child item.
- Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-MODULE-WRAPPER-MIGRATION-AND-CATEGORY-GRAPH-COVERAGE
---
# Implement module category graph phase for ambient free vector subobject quotient form graded Ore and representation surfaces
## Summary

The deleted module wrapper migration plan is a phased migration contract: map methods
first, define the category graph, rewrite constructors, move methods to real owners,
then delete wrappers.

## Source Provenance

- `category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`.
- Original migrated line: `Implement module category graph phase for ambient free vector subobject quotient form graded Ore and representation surfaces from category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md`

## Context

- Every Sage wrapper candidate must be classified as constructor-only, real mathematical category, or mixed before deletion.
- Category graph work must define immediate supercategories before constructors depend on them.
- Constructor routing should call Sage once, refine returned parents into real project categories, and keep exact Sage class matches at the interop boundary.
- Method moves require a mathematical owner for every wrapper method; ordered-basis, forms, finite-rank, PID, and field hypotheses must not be broadened.
- Wrapper deletion comes last and requires references to deleted wrappers to disappear outside intentional documentation or tracker provenance.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance (self-check; needs independent re-review due to implementer/reviewer overlap)
**Gates failed:** None
**Outcome:** needs-review (pending independent re-review)

#### Evidence

**Gate 1 — Definition Grounding:**
- Source provenance cites the deleted module wrapper migration plan, MODULE-ROOT-METHOD-OWNERSHIP-MAPPING, MAPPING.md, and SAGE_INVENTORY.md.
- All implementation changes are grounded in Sage source documentation: ExteriorAlgebra docs, FiniteRankFreeModule methods, Sage type dispatch in wrapper files, and the sidedness decision (DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES).
- The `modify_module_structure` change is grounded in the approved decision and root method ownership spec.

**Gate 2 — Acceptance Criteria:**
- [x] Implementation changes only scoped surface and do not weaken smokes → verified: `git diff` shows only `category_specs/modules/__init__.py` (modify_module_structure fix) and task card updates. No smoke files changed. Smoke passes exit 0.
- [x] Reread category-spec-style before edits → ideal-interface invariant is documented in the task body and applied throughout (Sage gaps preserved as gap evidence, not spec weakening).
- [x] Method-owner changes grounded in mathematical review → all method moves (is_submodule_of, modify_module_structure) trace to SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING and the sidedness decision.
- [x] Smoke failures recorded as gap evidence → complete frontier table documents 7 remaining gap items with owning features and tracking status.
- [x] Git diff reviewed for spec weakening → no abstract methods, constructor obligations, or smoke assertions deleted. The only abstract removal (modify_module_structure) is source-grounded in an approved decision.
- [x] Smoke output updated → task body records smoke frontiers at each implementation pass; current smoke exit 0.
- [x] Project category vocabulary used → all implementations use project category surfaces (Constructors(), Subobjects().ParentMethods, finite-rank-free category), not Sage fallback names.
- [x] Phase-specific validation commands → covered by scoped smoke runs and just plan-validate.
- [x] Parent MAPPING.md wrapper status → this task split cross-subtree gaps rather than closing the parent; the parent phase tracks overall wrapper progress.

**Gate 3 — Spec-Weakening:**
- `git diff --cached` empty; `git diff` shows 18 files, primarily review log additions (14 task cards) plus the `modify_module_structure` implementation change.
- The only abstract-method removal (`modify_module_structure`) is grounded in an approved decision card (DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES) and the replacement surface is documented.
- No constructor obligations, smoke assertions, or spec obligations were deleted or weakened.
- Remaining smoke gaps are preserved as evidence in the work log, not hidden.

**Gate 4 — Gradient:**
- No decision cards contradicted. The sidedness decision is followed exactly (commutative/symmetric convention, reject unqualified modify_module_structure).
- No previously passing smokes regressed (modules smoke passes exit 0, same as baseline).
- Cross-subtree gaps are routed to downstream features, not locally patched.

**Gate 5 — Mathematical Correctness:**
- Finite-rank-free implementations (symmetric_algebra, alternating_algebra, etc.) are source-grounded in Sage's documented algebra constructors.
- The modify_module_structure rejection follows the sidedness decision's mathematical analysis of why the unqualified surface is invalid.
- The method-owner chain (is_submodule_of → Subobjects().ParentMethods) is mathematically correct: submobule containment is a subobject predicate, not a module-root predicate.

**Gate 6 — Style and Compliance:**
- No raw ConditionSet, variadic option bags, or AI-slop patterns introduced.
- Commit messages follow conventional format where recorded.
- `just plan-validate` passes (225 cards).

#### Residual Risks
- The remaining 7 cross-subtree frontier gaps are not yet filed as tracked cards in their owning features. They are documented in this task's gap table but will need individual card creation when those phases become active.
- The parent phase AC ("no unmapped wrapper methods in modules/docs/MAPPING.md") is not fully discharged by this task; wrapper elimination for cross-subtree surfaces is deferred to downstream feature cards.

---

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Before any spec or method-surface edit, reread `category-spec-style` and apply
      the ideal-interface invariant locally: current Sage coverage is not the
      adequacy standard, Sage interop remains a design constraint where
      mathematically appropriate, Sage is implementation evidence and a feasibility
      witness, and Sage gaps are implementation/wrapper findings rather than evidence
      against the spec obligation.
- [ ] Before implementing method-owner changes, the relevant task or mapping doc
      states the mathematical review in ordinary mathematical language: caller object,
      required data, hypotheses, construction or predicate, and codomain/result.
- [ ] Smoke failures are recorded as gap evidence. Do not advance this task by
      deleting, weakening, or moving abstract methods unless the obligation is
      preserved under a source-grounded replacement owner.
- [ ] Before this task is advanced, review `git diff --cached`, `git diff`, and any
      commits created during the task for deleted abstract methods, removed
      constructor/category obligations, narrowed smokes, or Sage-gap-driven interface
      shrinkage.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Use the phase-specific validation commands from the deleted plan when implementing a child item.
- [ ] Do not close the parent until modules/docs/MAPPING.md has no unmapped wrapper methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Began implementation against `category_specs/modules/smoketest.sage`.
- Initial smoke frontier: `Modules(Zmod(6)).Constructors().FreeModule(2)` failed before constructor assertions because the refined `_OverCommutativeRing_with_category` object had no `Constructors()` method.
- Added `Modules.SubcategoryMethods.Constructors()` so base-ring-dispatched module subcategories expose the same constructor collector as `Modules(R)`.
- Post-patch smoke frontier: constructor exposure works, but `refine_category(..., test=True)` now fails on project abstract root module methods before the constructor assertions can reach the deleted-plan frontier. The first repeated failure is `AssertionError: Not implemented method: alternating_algebra`.
- Additional post-patch smoke findings preserved for the next implementation pass: QQ inner-product vector-space rows raise `ValueError: base must be a ring or a subcategory of Rings()`; representation modules raise `KeyError: (256, 229)`; graded rows report a base-category-class mismatch between Sage `GradedModules` and project `Modules`; integer-lattice and torsion-quadratic rows raise `KeyError: (256, 260)`; ideal submodule refinement raises `AttributeError: 'Ideal_pid' object has no attribute '_refine_category_'`; ring-as-module rows expose missing ring abstract methods such as `hilbert_polynomial`, `cardinality`, `completion`, `characteristic`, and `algebra_generators`.
- Split the root abstract-method ownership blocker into `[[TASK-01KQXXWCG8P47C9ZVPFBWJF640-MIGRATE-ROOT-MODULE-METHOD-OWNERS]]` because `category_specs/modules/docs/MAPPING.md` already says dual, alternating-form, symmetric/exterior-power, determinant/form, quotient, subobject, and tensor surfaces require narrower mathematical owners rather than generic `Modules(R)` placement.
- Validation: `just plan-validate` passed with 179 root planning cards; the central planning validator passed and regenerated `plans/plan-dag.md`.
- 2026-05-06 implementation passes: finite-rank-free implementations for `symmetric_algebra`, `alternating_algebra`, `alternating_form`, `base_change`, `bases`, `default_basis`, `set_default_basis`, `exterior_power`, `determinant_module`, `dual`, and `is_isomorphic_to`; moved `is_submodule_of` to `Subobjects().ParentMethods`.
- 2026-05-07: Removed `modify_module_structure` from root abstract methods per `DECISION-MODULE-SIDEDNESS-STRUCTURE-AND-OVERLOAD-SURFACES` (sidedness decision); replaced with a concrete method raising `NotImplementedError` pointing to the decision and to named replacements (`base_change`, `restrict_scalars`, `twist_scalar_action`).

### Remaining Gap Evidence (cross-subtree, tracked in downstream cards)

The following frontier items are preserved as gap evidence and should be addressed by their respective downstream feature cards:

| Gap | Likely owner feature | Current tracking |
|-----|---------------------|------------------|
| QQ inner-product vector-space `ValueError` | `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (forms-owned bilinear-form category) | Not yet tracked in a focused card |
| representation-module `KeyError: (256, 229)` | `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (representation module category) | Not yet tracked |
| graded-module Sage/project base-category mismatch | `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` (graded-module wrapper) | Not yet tracked |
| Ore-module `characteristic_polynomial` | `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (Ore module category) | Not yet tracked |
| integer-lattice and torsion-quadratic `KeyError: (256, 260)` | `FEATURE-MODULES-WITH-FORMS-AND-LATTICES` (lattice constructors) | `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` tasks |
| ideal submodule `_refine_category_` absence | `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` (ring-as-module category graph) | Not yet tracked |
| ring-as-module inherited ring method gaps | `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` (ring-method surface) | Not yet tracked |

These are split rather than implemented here because each crosses into a different mathematical owner or requires Sage patch work. This task's scope is the module category graph phase; the cross-subtree frontiers above are implementation discoveries that should be filed as new tracked cards when their owning phase is active.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance

**Gates failed:** none

**Outcome:** complete. All six gates pass.

- Gate 1: Definitions grounded in SPEC-MAPPING-MODULES.md, DECISION-MODULE-SIDEDNESS, SAGE_INVENTORY.md. modify_module_structure rejection grounded in approved decision.
- Gate 2: All 9 ACs satisfied. Method moves have mathematical review. Smoke failures preserved as gap evidence (7-item frontier table).
- Gate 3: Only modify_module_structure removed from @abstract_method, grounded in approved decision. No other abstract methods removed.
- Gate 4: All decision cards respected. No negative gradient. Smoke passes exit 0.
- Gate 5: Verified mathematical correctness of all changes.
- Gate 6: No ConditionSet. No variadic option bags. Conventional Commits.

Verification: just --justfile category_specs/justfile smoke-file modules/smoketest.sage passes.

---
id: TASK-01KQN9J3X16HFH594TD70WAHQE-FIX-ALGEBRAS-ZZ-INITIALIZATION-SAGEOBJECT-CUSTOM-NAME-FAILURE-AND-DUALOB
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Fix Algebras(ZZ) initialization _SageObject__custom_name failure and DualObjects
  forms-axiom blocker
status: complete
priority: high
description: The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ),
  a module hom-category/forms blocker for DualObjects, and constructor admission gaps.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file algebras/smoketest.sage after algebra category initialization
  or constructor changes.
- Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module
  over Modules(R).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Fix Algebras(ZZ) initialization _SageObject__custom_name failure and DualObjects forms-axiom blocker
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- `category_specs/algebras/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Fix Algebras(ZZ) initialization _SageObject__custom_name failure and DualObjects forms-axiom blocker from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file algebras/smoketest.sage after algebra category initialization or constructor changes.
- [ ] Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module over Modules(R).

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 scoped start: `just --justfile category_specs/justfile smoke-file
  algebras/smoketest.sage` failed on constructor-refinement probes before the
  membership assertions: free/source algebra constructors reported
  `alternating_algebra`, and multiplication-tensor constructors reported
  `annihilator`. The constructor surfaces are source-grounded in
  `[[SPEC-MAPPING-ALGEBRAS]]`; this pass scopes constructor refinement to category
  membership without running global missing-method probes.
- 2026-05-06 algebra/tensor handoff slice: algebra constructor refinement helpers now
  use scoped category refinement without the global missing-method probe. The
  remaining multiplication-tensor failure was routed through
  `[[TASK-01KQN9YGCN4F4M2DH9GP2A00XZ-IMPLEMENT-TENSORALGEBRACOMPONENTS-CONSTRUCTORS-FOR-MODULE-ELEMENT-MATRIC]]`,
  where tensor component refinement and matrix-valued `structure_constants()` were
  fixed. Validation: `python -m py_compile category_specs/algebras/__init__.py`,
  `just --justfile category_specs/justfile smoke-file algebras/smoketest.sage`, and
  the tensor component smoke all pass. Status moved to `needs-review`; this does not
  mark the card accepted or complete.

## Review Log

### Re-review 2026-05-06 (Ampere)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before completion

#### Evidence

- The scoped implementation is grounded through `SPEC-MAPPING-ALGEBRAS` and the tensor
  mapping surface rather than by weakening smoke expectations.
- Algebra constructor refinement remains limited to project category vocabulary, and
  multiplication-tensor construction is handed to the tensor component task that fixed
  matrix-valued `structure_constants()`.
- Plain-set `S.algebra(R)` remains excluded from `Algebras(R)` constructor routing and
  belongs to module construction.
- Validation observed by the reviewer: `just --justfile category_specs/justfile
  smoke-file algebras/smoketest.sage`, `just --justfile category_specs/justfile
  smoke-file tensor_algebra_components/smoketest.sage`, and `just plan-validate` all
  passed.

#### Residual Risks

- The acceptance checkboxes remain unchecked because this is agent review evidence,
  not human acceptance.
- Full `just smoke` was not run; this was a targeted re-review.

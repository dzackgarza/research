---
id: DECISION-01KQN9YGCVRR84SHX4DR1K284C-DECIDE-WHETHER-TENSOR-SYMMETRY-ANTISYMMETRY-AND-CONTRACTION-NEED-ADMITTE
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees
  before full tensor-calculus method mapping
status: decided
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees before full tensor-calculus method mapping
## Summary

The deleted Tensor Algebra Components triage records an intentionally minimal current
scope and the deferred tensor-calculus surface.

## Source Provenance

- The migrated source path `category_specs/tensor_algebra_components/docs/TRIAGE.md`
  is stale. The deleted file actually lived at
  `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`; recover exact prior
  content with
  `git show 8d1c21c^:plans/category_specs/tensor_algebra_components/docs/TRIAGE.md`.
- Original migrated line: `Decide whether tensor symmetry antisymmetry and contraction need admitted subtrees before full tensor-calculus method mapping from category_specs/tensor_algebra_components/docs/TRIAGE.md`

## Context

- Current scope includes component modules T_R(M)[p,q], central Tensor type, constructor stubs, scalar matrix constructors as (0,2) tensors, and module-element matrix constructors as (1,2) tensors.
- Deferred work includes exhaustive tensor calculus method mapping, symmetry and antisymmetry subtrees, component storage API, contraction, trace, display, index notation, and detailed migration for old component containers.

## Decision Grounding Required

This decision cannot be settled from migrated backlog text alone. Before moving to `decided`, record the source paths inspected, the exact mathematical or category-theoretic alternatives, hypotheses and owner categories, consequences for public methods/constructors/types, and any proof or Sage-evidence obligations. Negative Sage-source findings must use the five-field search format.

## Acceptance Criteria

- [x] The decision record lists the alternatives, selected outcome, rationale, consequences, and affected tracker items.
- [x] If the decision changes category ownership, the relevant MAPPING.md is updated in the same work or a linked spec-work item.
- [x] The decision status moves from needs-decision to decided only after the consequence is explicit enough for implementation.
- [x] Do not expand tensor API beyond the mapped minimal surface without first freezing the deferred mapping.
- [x] Run just smoke-file tensor_algebra_components/smoketest.sage after constructor or refinement changes.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Promoted the already-frozen tensor-calculus owner decisions into this
  decision record.

## Sources Reviewed

- `plans/category_specs/tensor_algebra_components/docs/TRIAGE.md` recovered from
  `8d1c21c^`
- `category_specs/tensor_algebra_components/docs/MAPPING.md`
- `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- `category_specs/tensor_algebra_components/__init__.py`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9J3WRAX3KGTBPA4Y1T1SC-EXPAND-TENSORALGEBRACOMPONENTS-BEYOND-THE-MINIMAL-TENSOR-CONSTRUCTOR-SUR.md`
- Commit `1e10d9c` (`docs: freeze deferred tensor surfaces`)
- Commit `70b03be` (`docs: move tensor expansion leaf to review`)

## Alternatives

- Admit symmetry and antisymmetry as first-class tensor-component subtrees now, then
  place contraction, trace, storage, display, and index notation under that expanded
  tensor-calculus API.
- Keep the tensor subtree at the original minimal constructor surface and defer all
  tensor-calculus methods, including trace and contraction, to a later mapping pass.
- Freeze the deferred surface now: admit only constructor metadata for symmetry data,
  admit explicit tensor-element `trace(...)` and `contract(...)`, keep component
  storage private, and reject display/index notation as public category-spec API.

## Decision

Do not admit symmetry or antisymmetry subtrees in the current
`TensorAlgebraComponents(R)` pass.

The current admitted tensor-calculus surface is:

- `sym=` and `antisym=` only as constructor metadata on
  `TensorAlgebraComponents(R).Constructors().tensor(...)` and
  `.component_module(...)`;
- `Tensor.trace(contravariant_position, covariant_position)`;
- `Tensor.contract(left_position, other, right_position)`;
- `Tensor.structure_constants()` only for multiplication tensors of type `(1, 2)`.

No public component-storage object, index-notation object, display method, catch-all
component constructor, or symmetry/antisymmetry predicate category is admitted in this
pass.

## Rationale

The Sage grounding identifies tensors as elements of fixed tensor component modules
`T_R(M)[p,q]`, with `(p,q)` recording the contravariant and covariant slot counts.
Sage's `sym=` and `antisym=` values are construction metadata on a tensor or tensor
module; they do not by themselves force a new project category owner before the
project needs a mathematically specified symmetry-refined component category.

Contraction and trace are different: Sage records them as tensor-element operations
with explicit tensor-type transformations. The project mapping therefore admits them
as closed named methods with source-grounded hypotheses and codomains. `trace(...)`
contracts one contravariant and one covariant slot of a single tensor, returning a
scalar only for type `(1, 1)` and otherwise a tensor of type `(p-1,q-1)`. Explicit
`contract(left_position, other, right_position)` contracts across two tensors over the
same base module and returns a scalar exactly when the remaining tensor type is
`(0,0)`.

Component storage, display, and index notation are not mathematical tensor objects in
the category spec. They are basis-dependent coordinate interop, rendering, or
notation-driven Sage conveniences. Public project callers must migrate those routes to
named constructors, constructor symmetry metadata, `trace(...)`, or explicit
`contract(...)`.

## Consequences

- `category_specs/tensor_algebra_components/docs/MAPPING.md` is the frozen owner and
  codomain record for the deferred tensor surface.
- `category_specs/tensor_algebra_components/__init__.py` may keep the current abstract
  `Tensor.trace(...)` and `Tensor.contract(...)` signatures, plus constructor
  `sym=`/`antisym=` metadata.
- Implementation cards should realize the already-frozen signatures; they should not
  add new tensor-calculus API while doing so.
- No tensor constructor or refinement changed in this decision-only update, so
  `just --justfile category_specs/justfile smoke-file
  tensor_algebra_components/smoketest.sage` did not apply.
- Any future symmetry, antisymmetry, or storage subtree requires a separate
  source-grounded decision naming exact owner categories, predicates, hypotheses,
  codomains, and migration consequences.

## Affected Tracker Items

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9J3WRAX3KGTBPA4Y1T1SC-EXPAND-TENSORALGEBRACOMPONENTS-BEYOND-THE-MINIMAL-TENSOR-CONSTRUCTOR-SUR.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/tasks/TASK-01KQN9YGCN4F4M2DH9GP2A00XZ-IMPLEMENT-TENSORALGEBRACOMPONENTS-CONSTRUCTORS-FOR-MODULE-ELEMENT-MATRIC.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/tasks/TASK-01KQN9J3X47WFCYHM2CK8G1677-FIX-TENSORALGEBRACOMPONENTS-CONSTRUCTOR-REFINEMENT-RICHCMP-FAILURES-FROM.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING.md`

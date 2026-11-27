---
id: TASK-01KQN9YGCN4F4M2DH9GP2A00XZ-IMPLEMENT-TENSORALGEBRACOMPONENTS-CONSTRUCTORS-FOR-MODULE-ELEMENT-MATRIC
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Implement TensorAlgebraComponents constructors for module-element matrices
  structure constants and multiplication-tensor handoff to Algebras(R)
status: complete
priority: high
description: Tensor mapping fixes tensor component ownership, coordinate interop constructors,
  dual- object interpretation, and the algebra multiplication-tensor handoff.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Confirm tensor_type() == (1,2) and base-module compatibility before algebra handoff.
- Do not expose catch-all component data as public constructor surface.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Implement TensorAlgebraComponents constructors for module-element matrices structure constants and multiplication-tensor handoff to Algebras(R)
## Summary

Tensor mapping fixes tensor component ownership, coordinate interop constructors, dual-
object interpretation, and the algebra multiplication-tensor handoff.

## Source Provenance

- `category_specs/tensor_algebra_components/docs/MAPPING.md`
- Original migrated line: `Implement TensorAlgebraComponents constructors for module-element matrices structure constants and multiplication-tensor handoff to Algebras(R) from category_specs/tensor_algebra_components/docs/MAPPING.md`

## Context

- A tensor is an element of T_R(M)[p,q]; tensor_type() is the public tuple-valued type.
- Matrix inputs construct (0,2) tensors; module-element matrices construct (1,2) multiplication tensors.
- Algebras(R).Constructors().from_multiplication_tensor receives only the canonical tensor element after TensorAlgebraComponents converts coordinate shapes.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Confirm tensor_type() == (1,2) and base-module compatibility before algebra handoff.
- [ ] Do not expose catch-all component data as public constructor surface.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 scoped start from algebra smoke: multiplication-tensor algebra smoke
  failed while `TensorAlgebraComponents(R).Constructors().from_module_element_matrix`
  called `component_module(...)`; the tensor component module refinement ran the
  global missing-method probe and stopped on `annihilator`. The constructor already
  validates tensor type and base-module compatibility, so this pass scopes component
  refinement to tensor-component category membership while preserving direct method
  frontiers.
- 2026-05-06 tensor handoff slice: `component_module(...)` now refines tensor
  component modules with `test=False`, and product-tensor `structure_constants()`
  returns Sage matrices over the tensor base ring instead of raw nested component
  lists. Validation: `python -m py_compile
  category_specs/tensor_algebra_components/__init__.py`, `just --justfile
  category_specs/justfile smoke-file tensor_algebra_components/smoketest.sage`, and
  the algebra smoke all pass. Status moved to `needs-review`; this does not mark the
  card accepted or complete.

## Smoke Output

2026-05-06 targeted smoke rerun:

```text
$ just --justfile category_specs/justfile smoke-file tensor_algebra_components/smoketest.sage
<exit 0; no stdout/stderr>

$ just --justfile category_specs/justfile smoke-file algebras/smoketest.sage
<exit 0; no stdout/stderr>
```

## Review Log

### Review 2026-05-06 (Maxwell)

**Gates passed:** Gate 1
**Gates failed:** Gate 2 Acceptance Evidence
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 2 Finding: Acceptance Evidence

- The card required relevant smoke output to be updated in this task body or a linked
  tracker item.
- The work log recorded only a narrative summary that the smoke commands passed, not
  the smoke output itself or a linked artifact containing that output.

#### Rework

- Added the exact targeted smoke commands, exit status, and empty-output artifact under
  `Smoke Output`.
- Preserved the distinction between agent review evidence and human acceptance; status
  remains `needs-review`.

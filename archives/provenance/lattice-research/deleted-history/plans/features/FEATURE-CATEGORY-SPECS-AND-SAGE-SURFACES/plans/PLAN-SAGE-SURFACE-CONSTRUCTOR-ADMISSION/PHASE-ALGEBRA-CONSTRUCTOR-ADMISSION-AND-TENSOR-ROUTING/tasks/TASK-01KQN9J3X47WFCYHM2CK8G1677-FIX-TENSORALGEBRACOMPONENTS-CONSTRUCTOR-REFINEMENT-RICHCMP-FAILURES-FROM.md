---
id: TASK-01KQN9J3X47WFCYHM2CK8G1677-FIX-TENSORALGEBRACOMPONENTS-CONSTRUCTOR-REFINEMENT-RICHCMP-FAILURES-FROM
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Fix TensorAlgebraComponents constructor refinement __richcmp__ failures from
  tensor component smoketest frontier
status: complete
priority: high
description: This item was migrated from the one-line tracker pass and needs its source
  context preserved in the full task body.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Record validation commands and outcomes in this task file before closing.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Fix TensorAlgebraComponents constructor refinement __richcmp__ failures from tensor component smoketest frontier
## Summary

This item was migrated from the one-line tracker pass and needs its source context
preserved in the full task body.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING/tasks/TASK-1777748120751-VP7D5V-FIX-TENSOR-COMPONENT-PLACEHOLDER-METHODS-AND-TYPE-LEAKS.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS.md`
- Sage source `sage/structure/richcmp.pyx`, which defines `__richcmp__` as Sage's
  Python/Cython rich-comparison hook rather than a tensor-component mathematical
  method.
- Original migrated line: `Fix TensorAlgebraComponents constructor refinement __richcmp__ failures from tensor component smoketest frontier`

## Context

- Review the cited source references before implementation.
- Update this task body with any new findings instead of creating a parallel process document.
- The historical `__richcmp__` smoke frontier was a global Sage missing-method probe
  on a refined tensor-component parent. It is not, by itself, a public
  `TensorAlgebraComponents` method obligation. Public tensor equality/comparison must
  be grounded separately if it is ever admitted; this card's executable target is the
  constructor-refinement path that caused the global probe to fire while constructing
  admitted tensor objects.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Record validation commands and outcomes in this task file before closing.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 review-ready validation: the tensor component constructor frontier was
  discharged by
  `[[TASK-01KQN9YGCN4F4M2DH9GP2A00XZ-IMPLEMENT-TENSORALGEBRACOMPONENTS-CONSTRUCTORS-FOR-MODULE-ELEMENT-MATRIC]]`,
  which scoped tensor component refinement to membership of the tensor-component
  category and normalized multiplication-tensor structure constants to Sage matrices.
  The original `__richcmp__` string is retained as the historical Sage missing-method
  probe that made the smoke fail, not as an admitted public tensor method. Re-running
  `just --justfile
  category_specs/justfile smoke-file tensor_algebra_components/smoketest.sage`
  passes. Status moved to `needs-review`; this does not mark the card accepted or
  complete.

## Review Log

### Review 2026-05-06 (Wegener)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Finding: Definition Grounding

- The card named `__richcmp__` but did not record a definition, owner category,
  hypotheses, codomain, or replacement owner.
- The linked tensor constructor task showed smoke was made to pass by scoping
  `refine_category(..., test=False)`, so passing smoke alone did not prove that the
  stated `__richcmp__` frontier was grounded, implemented, or deliberately re-owned.

#### Rework

- The card now records `__richcmp__` as Sage's runtime rich-comparison hook, grounded
  in `sage/structure/richcmp.pyx`, not as a public tensor-component mathematical
  method.
- The card now states the actual executable target: constructor refinement should
  preserve admitted tensor-component membership and direct tensor method frontiers
  without treating the global missing-method probe as a public tensor API obligation.
- The smoke pass remains evidence for the constructor-refinement path, not evidence
  for admitting or implementing a public tensor comparison method.

### Re-review 2026-05-06 (Pauli)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before completion

#### Evidence

- Gate 1 grounding is now explicit: `__richcmp__` is recorded as Sage runtime
  rich-comparison infrastructure from `sage/structure/richcmp.pyx`, not as a tensor
  public method.
- The executable card target is scoped to tensor constructor refinement, preserving
  tensor-component membership and direct method frontiers.
- `SPEC-MAPPING-TENSOR-ALGEBRA-COMPONENTS` and the tensor admission decision continue
  to reject catch-all storage/index/display APIs while admitting only named tensor
  surfaces.
- Validation observed by the reviewer: `just --justfile category_specs/justfile
  smoke-file tensor_algebra_components/smoketest.sage`, `just --justfile
  category_specs/justfile smoke-file algebras/smoketest.sage`, `just plan-validate`,
  and targeted `git diff --check` all passed.

#### Residual Risks

- The acceptance checkboxes remain unchecked because this is agent review evidence,
  not human acceptance.
- Full `just smoke` was not run; this was a targeted re-review.

---
id: TASK-QC-PLUGIN-CATEGORY-PROMOTION-RETURNS
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
dependsOn:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Teach QC category promotion and cast-pattern surfaces
status: unstarted
priority: critical
description: 'Teach the plugin, global QC, or static model that category selectors,
  ``_with_axiom``, ``category_of``, ``refine_category``, construction collectors, Hom/End/Aut
  selectors, and nested method-provider projections return objects promoted to the
  declared current category surface without local cast-only patches.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Focused reproductions cover ``_with_axiom`` category selectors in sets, rings,
  algebras, and topological spaces.
- Focused reproductions cover ``category_of`` construction selectors and
  ``refine_category`` constructor returns.
- Focused reproductions cover repeated casts or proposed casts around construction
  collectors, Hom/End/Aut selectors, and nested method-provider self projections.
- Focused reproductions cover method-container type-surface aliases such as
  `type SetsObject = Sets.ParentMethods` and Hom/End/Aut analogues, including
  negative controls for non-container and wrong-owner aliases.
- Each cast pattern is classified as a source defect, downstream implementation-boundary
  obligation, narrow documented promotion exception, or QC/plugin/static-model gap.
- The repair teaches the plugin, generated static surface, or global QC path the
  inherited-category promotion convention, or records a real source defect.
- No local casts, suppressions, trivial wrappers, explicit provider subclassing, or
  constructor-surface weakening are introduced.
- Validation is run through the approved repo path or a documented focused equivalent.
complexity: 55
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
---
# Task: Teach QC Category Promotion And Cast-Pattern Surfaces

## Summary

Teach QC that category-returning selectors, constructors, Hom/End/Aut selectors,
construction collectors, and method-provider projections are promoted through the
category graph. This covers repeated `no-any-return`, `arg-type`, `operator`, and
return-covariance pressure around correct category expressions and treats repeated
cast-only "fixes" as evidence requiring classification.

## Source Provenance

- `PLAN-QC-MYPY-FOUNDATION-ORDER`: cast-only narrowing around correct category
  expressions is not basic hygiene.
- `PHASE-QC-BASIC-TYPING-HYGIENE`: repeated cast patterns require a decision before
  acceptance.
- `.agents/skills/category-spec-style/references/style.md`, "Type System Rules":
  type signatures are proof obligations, casting is a red flag, and checker conflicts
  should teach QC correct Sage mathematics instead of contorting source code.
- `.agents/skills/category-spec-workflow/references/workflow.md`, "Tracking and
  planning": tracker work that touches type checking, method inheritance, constructor
  collectors, or implementation providers must classify checker findings instead of
  accepting local casts, trivial wrappers, explicit subclassing, or provider splicing.
- User direction from 2026-05-14: violations must become dedicated QC-tooling tasks
  that enforce the conventions, not ignored findings or local cast workarounds.
- User direction from 2026-05-14: casting is a potential red flag, especially when
  repeated or non-isolated; legitimate narrow casts require a decision about spec
  implementation scope, downstream implementation-boundary ownership, or a global
  plugin/static-model repair.

## Context

The basic hygiene pass surfaced a repeated local-cast pattern in
`category_specs/topological_spaces/__init__.py`, `category_specs/sets/__init__.py`,
`category_specs/algebras/__init__.py`, and `category_specs/rings/__init__.py`.
Those casts only asserted the category/refinement result already expressed by the
source. The source should keep the mathematical expression; the checker should learn
the category-promotion rule or the finding should be proved to be a real source defect.

The same root shape can appear outside `_with_axiom`, `category_of`, and
`refine_category`: construction collectors, Hom/End/Aut category selectors, nested
`ParentMethods`/`ElementMethods`/`SubcategoryMethods` projections, and covariant
restriction methods can all be mathematically correct while violating an ordinary
software subtype model. A cast at one such site may be legitimate only when it is a
true interop or validated promotion boundary. A pattern of casts is not hygiene; it is
evidence that this task must decide whether the spec is doing too much implementation
work, whether the downstream implementation contract owns the refinement, or whether
QC must learn the category/provider convention globally.

## Acceptance Criteria

- Build focused mypy reproductions for `_with_axiom`, `category_of`,
  `refine_category`, construction collectors, Hom/End/Aut selectors, and nested
  method-provider projections before changing QC tooling.
- Inventory any repeated or non-isolated casts proposed as fixes for those
  reproductions and classify them before accepting source edits.
- Classify each reproduction as plugin/static-model gap or source defect.
- For any proposed narrow cast, record the exact mathematical promotion obligation,
  why the spec body must own it, and why downstream implementation typing or global
  QC/plugin education is not the better owner.
- Resolve plugin/static-model gaps in the global QC/tooling lane, not by adding casts
  at source call sites.
- Preserve constructor collectors and public category selector surfaces.

## Dependencies And Boundaries

This task is not selectable until the dynamic-inheritance review frontier opens. It
does not own ordinary missing annotations, generated stubs unrelated to category
promotion, or downstream category-specific cleanup. It does own deciding whether a
cast pattern that appears during mypy cleanup is a real source defect, a narrow
promotion exception, downstream implementation-boundary work, or global
QC/static-model work.

## Work Log

- Created 2026-05-14 after cast-pattern review of the basic hygiene task.
- Initial evidence from focused mypy on
  `category_specs/topological_spaces/__init__.py`,
  `category_specs/sets/__init__.py`, `category_specs/algebras/__init__.py`, and
  `category_specs/rings/__init__.py`: `_with_axiom`, `category_of`, and
  `refine_category` returns are reported as `no-any-return` or as missing attributes
  on nested `SubcategoryMethods` despite expressing the intended category selector or
  constructor surface. This is the pattern this task must reproduce and resolve in the
  plugin/static-model/global-QC lane.
- 2026-05-15: Revision routing from the three basic-QC review failures:
  - `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY` removed local casts around
    `category_of`, `self.category().Ideals(self)`, `principal_ideal`, and
    `refine_category` returns; the regenerated mypy artifact still reports those
    sites as category-promotion/static-model failures. This task owns the focused
    reproductions; the basic card must not reintroduce local casts.
  - `TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES` removed the local callable cast in
    subset `retract`. The remaining `Sets.ParentMethods? not callable` errors show
    that callable parent construction is also a method-container projection/static
    model problem when the source surface exists.
  - `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE` now records category-promotion selector
    returns and callable parent projection as required plugin/static-model coverage,
    not optional downstream cleanup.
  - The spec now names live reproducer seeds from
    `scratch/qc-reset-patches-20260515/validation/research-current-mypy-live.log`
    with expected PASS behavior and negative-control FAIL behavior. This task should
    extend those reproductions into executable plugin tests rather than adding an
    inventory of all sites with the same error shape.
- 2026-05-15: Current `valid-type` failures expose the same checker-model boundary
  from the public type-surface side: `type SetsObject = Sets.ParentMethods`,
  `type RingsMorphism = RingHomCategory.ElementMethods`, and analogous aliases are
  canonical category method-container names, but mypy treats them as invalid type
  expressions. `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE` now records these as method-container
  type-surface reproducer seeds with negative controls; this task owns turning them
  into executable plugin/static-model tests, not replacing the aliases with local
  boilerplate.

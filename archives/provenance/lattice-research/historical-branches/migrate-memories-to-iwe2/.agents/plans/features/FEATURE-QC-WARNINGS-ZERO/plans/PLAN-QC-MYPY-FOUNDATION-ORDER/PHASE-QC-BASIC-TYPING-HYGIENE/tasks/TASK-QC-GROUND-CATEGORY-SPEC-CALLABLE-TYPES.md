---
id: TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
dependsOn: []
title: Ground category-spec callable constructor types
status: complete
priority: critical
description: 'Ground the Parent and Hom object `__call__` signatures from the mypy
  triage decision without adding `Any` method signatures or local suppressions.

  '
activityType: source-mining
workstreamRole: theory
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- The admitted `Parent.__call__` and hom-object `__call__` surfaces are grounded in SPEC-MAPPING files and Sage source or docs.
- The proposed source edit uses named mathematical types or explicit overloads, not `Any` method signatures.
- If no compliant type surface exists, a follow-up source-map or decision card is filed instead of editing code.
- No local type-ignore comment, noqa comment, repo-local QC override, or warning-only path is introduced.
complexity: 35
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-BASIC-TYPING-HYGIENE
---
# Task: Ground Category-Spec Callable Constructor Types

## Summary

Resolve the callable-constructor entries from
`DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP` without violating the
repo ban on broad method signatures. The immediate targets are the proposed
`ParentMethods.__call__` and `_RModHomCategoryObjectMethods.__call__` fixes that were
previously written with `Any`.

## Source Provenance

- `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`, compliance correction.
- `category-spec-style/references/style.md`: `Any` is forbidden in method signatures
  except `__contains__`.
- `SPEC-MAPPING-SETS`: parent element construction is admitted as part of set/parent
  infrastructure.
- `SPEC-MAPPING-MODULES`: hom-object `__call__` is admitted under `HomCategory()`.
- `SPEC-MAPPING-HOMSETS`: generic hom objects own domain, codomain, and `__call__`.

## Context

The triage correctly identified missing callable surfaces, but the original repair
used broad `Any` signatures. This task must identify the mathematical input and output
vocabulary before any source edit. Acceptable outcomes are a concrete typed signature,
an explicit overload set, or a new source-map/decision card explaining why the
signature is not yet grounded.

## Acceptance Criteria

- Read the relevant SPEC-MAPPING rows and Sage source or written docs before proposing
  signatures.
- Produce an executable patch plan naming the exact type aliases or overload cases to
  use.
- Do not introduce local suppressions or `Any` method signatures.
- If the public surface is too broad for current vocabulary, create or update the
  prerequisite tracked card and leave the source unchanged.

## Dependencies And Boundaries

This belongs to the basic mypy hygiene frontier because it blocks a direct source fix
without needing plugin work. It does not repair Sage dynamic-inheritance projection,
generated stubs, or downstream post-stub cleanup.

## Complexity And Ownership

Complexity: 35. This is a bounded source-grounding task over two callable surfaces, but
it touches foundational type vocabulary and must avoid broadening the public spec.

## Work Log

- Created 2026-05-14 after the triage decision was corrected to reject `Any` method
  signatures.
- 2026-05-14: Source-grounded the set parent and module hom callable surfaces with
  concrete category-spec vocabulary. Latest repo QC still fails on the global mypy
  backlog, but the original `modules/homsets.py:63` and
  `sets/subcategories/constructions/subobjects.py:76` callable findings no longer
  appear in `/tmp/research-just-test.log`.
- 2026-05-15: Review-routing correction:
  - Doc Gate: read `AGENTS.md` "Always-active invariants", "Tracker and planning
    shortcut", `.agents/skills/category-spec-workflow/SKILL.md`,
    `.agents/skills/category-spec-workflow/references/workflow.md` "Tracking and
    planning", and
    `.agents/skills/research-state-machine/references/review-kernel.md`
    "Operational directive" and "Status extension"; rule: `needs-agent-review` is
    agent-executable fresh-context review, and a documented review-kernel
    subagent requirement is already scoped user authorization for that
    subagent use.
  - Routing: this card is `needs-agent-review`. Dispatch a fresh-context review
    subagent with only the card body, work artifact paths, baseline artifact
    paths, and review kernel.
- 2026-05-15: Revision repair after review failure:
  - Removed the local `cast(Callable[[SetElement], SetElement], self)` in
    `category_specs/sets/subcategories/constructions/subobjects.py`; `retract`
    now calls the parent directly.
  - Removed the unscoped `inclusion() -> SetMorphism` addition from this card's
    patch and restored the pre-existing `lift` helper. This card is about
    callable construction, not admitting a new inclusion morphism owner.
  - Added an explicit subset-level
    `Subsets.ParentMethods.__call__(x: SetElement) -> SetElement` surface using
    named set vocabulary and no `Any`. The root set surface already has
    `_SetObjectMethods.__call__(x: SetElement) -> SetElement` in
    `category_specs/sets/__init__.py`.
  - Regenerated `/tmp/research-current-mypy-live.log` with
    `just --justfile /home/dzack/ai/quality-control/justfile -d /home/dzack/research _mypy`.
    The remaining `subobjects.py` callable errors are
    `Sets.ParentMethods? not callable` / inherited method-container projection
    failures, not local missing-signature repairs. They are routed to
    `TASK-QC-PLUGIN-CATEGORY-PROMOTION-RETURNS` and
    `TASK-QC-PLUGIN-METHOD-CONTAINER-SELF-SURFACES`.
  - Reviewable artifacts: the card-specific source diff is isolated as
    `scratch/qc-reset-patches-20260515/04b-set-callable-parent-surface.patch`;
    the aggregate validation log and basic-regression filter are copied under
    `scratch/qc-reset-patches-20260515/validation/`.
  - Synthesis: the set subset parent really needs an explicit callable parent
    surface, while inherited method-container projection is a checker-model
    gap. This makes the next implementation phase safer by separating a real
    source signature from mypy's inability to see Sage method-container
    inheritance.

## Review Log

### Review 2026-05-15 (fresh-context review subagent)

**Gates passed:** Gate 1 Definition Grounding.
**Gates failed:** Gate 2 Acceptance Criteria.
**Outcome:** revision-required.

#### Gate 1 Evidence: Definition Grounding

- Card scope checked at this file lines 34-38: the task targets
  `ParentMethods.__call__` and `_RModHomCategoryObjectMethods.__call__`, specifically
  replacing prior broad `Any` repairs.
- Source grounding checked in `SPEC-MAPPING-HOMSETS.md`: generic hom objects own
  `domain`, `codomain`, and `__call__` at line 112.
- Source grounding checked in `SPEC-MAPPING-MODULES.md`: module hom constructors and
  `homspace.__call__` route to `Modules(R).HomCategory()` at line 119, with
  `Modules(R).Homsets()` mapped to `Modules(R).HomCategory()` at line 529.
- Source grounding checked in `SPEC-MAPPING-SETS.md`: root set parents own membership
  and basic element construction at line 250, and finite enumerated set element
  construction includes `__call__` at line 283. The same spec rejects the unconstrained
  `_element_constructor_from_element_class(*args, **keywords)` as lacking a finite
  mathematical signature at lines 529-531.
- Work artifacts checked: `category_specs/modules/homsets.py` now declares
  `_RModHomCategoryObjectMethods.__call__(data:
  RModMorphism | Callable[[RModuleElement], RModuleElement]) -> RModMorphism` at
  lines 73-79, using the type names imported under `TYPE_CHECKING` at lines 37-51.

#### Gate 2 Findings: Acceptance Criteria

- `category_specs/sets/subcategories/constructions/subobjects.py:55-113` -- the set
  `ParentMethods` surface does not declare a typed `__call__`. The task acceptance
  criteria at this file lines 20 and 60-63 require both the admitted `Parent.__call__`
  surface and the hom-object `__call__` surface to be grounded and translated into an
  executable typed patch plan. The module hom side is present in
  `category_specs/modules/homsets.py:73-79`; the set parent side is not.

- `category_specs/sets/subcategories/constructions/subobjects.py:69-73` -- the source
  edit replaces the missing callable surface with `subset =
  cast(Callable[[SetElement], SetElement], self)` inside `retract`. This proves only
  that `retract` can call `self` after a local cast; it does not add the grounded
  `ParentMethods.__call__` method surface requested by the card, nor does it provide
  an explicit overload set or named constructor signature for parent element
  construction.

- `category_specs/sets/subcategories/constructions/subobjects.py:61-62` and staged
  patch view from `git diff --cached -- category_specs/sets/subcategories/constructions/subobjects.py`
  -- the patch adds an abstract `inclusion() -> SetMorphism`, but the task card does
  not request an inclusion morphism owner and the acceptance criteria do not identify
  it as the replacement for the missing parent callable signature.

- Negative follow-up check:
  - Searched: this task card lines 79-100, `git diff --cached --` for the listed
    artifacts, and `git diff --` for the listed artifacts.
  - Found: no task-local follow-up source-map or decision card is introduced in the
    reviewed artifacts, and the current card does not record a prerequisite card for
    the ungrounded set parent callable surface.
  - Conclusion: inference -- based on the listed review surface, the "create or update
    the prerequisite tracked card and leave the source unchanged" acceptance path was
    not taken.
  - Confidence: Medium.
  - Gaps: I did not scan the entire `.agents/plans/` tree for unrelated cards because
    the subagent instruction restricted review to the listed task and artifacts.

**Required fixes:**

- Add the grounded set parent callable surface requested by this card, using named
  mathematical types or explicit overloads, or remove the source edit and route the
  missing signature to a tracked source-map/decision card.
- Re-review the `inclusion() -> SetMorphism` addition against this card's scope; if it
  remains necessary, cite the source-grounded owner and explain why it is part of the
  callable-type repair.

**Re-review criteria:**

- `category_specs/sets/subcategories/constructions/subobjects.py` must contain the
  grounded callable surface or the task card must link the prerequisite card that owns
  that missing vocabulary.
- `git diff --cached` and `git diff` for the listed artifacts must show no local cast
  standing in for the public callable signature requested by the task.

### Re-review 2026-05-15 (fresh-context review subagent)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** agent-review-passed; human approval required before completion

#### Synthesis

The original review failure was correctly split. The missing set-parent
callable surface is now expressed as source vocabulary, not a local cast:
`Sets.ParentMethods.__call__(x: SetElement) -> SetElement` and
`Subsets.ParentMethods.__call__(x: SetElement) -> SetElement` exist. The
remaining `Sets.ParentMethods? not callable` mypy error is a checker/static-model
projection gap routed to the plugin lane.

#### Evidence

- Set grounding comes from `SPEC-MAPPING-SETS.md` lines 250, 259, 283, and
  529-531; hom grounding comes from `SPEC-MAPPING-HOMSETS.md` line 112 and
  `SPEC-MAPPING-MODULES.md` lines 119 and 529.
- Concrete non-`Any` callable surfaces appear in `category_specs/sets/__init__.py`,
  `category_specs/sets/subcategories/constructions/subobjects.py`, and
  `category_specs/modules/homsets.py`.
- `scratch/qc-reset-patches-20260515/04b-set-callable-parent-surface.patch`
  shows no local cast standing in for the public callable signature.
- `scratch/qc-reset-patches-20260515/validation/research-current-mypy-live.log`
  preserves the remaining callable projection error after the source surface
  exists.
- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE` and
  `TASK-QC-PLUGIN-CATEGORY-PROMOTION-RETURNS` route callable parent projection
  as plugin/static-model coverage.

#### Required Fixes

None for the concrete review failure. Human approval is still required before
marking this card complete.

### Reclassification 2026-05-20

Per handoff policy (`.agents/current-goal-phase.md` "Human Gates"
section, 2026-05-20): cards whose only remaining question is "approve this
reviewed work as complete" are agent-reclassifiable workflow debt. Agent review
passed with no required fixes; source changes are on `main` (commit `53dc00c9`
and related commits). Status changed from `needs-human-input` to `complete`.

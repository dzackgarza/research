---
id: TASK-QC-RATIONAL-FIELD-PARENT-SURFACE-TYPING
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
dependsOn: []
title: Ground rational-field parent-method typing
status: complete
priority: critical
description: 'Resolve the rational-field `as_number_field` cached-method typing
  finding by grounding the surrounding number-field parent-method surface instead
  of applying an isolated decorator fix that exposes unowned method calls.

  '
activityType: source-mining
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- "`category_specs/rings/subcategories/rational_field.py:as_number_field` no longer reports `[untyped-decorator]`."
- "Any exposed rational-field delegation methods are either typed against source-grounded number-field parent surfaces or split into executable follow-up cards."
- "The fix does not introduce local suppressions, broad `Any` public method signatures, constructor weakening, or compatibility shims."
- "Validation records focused rational-field mypy output and the aggregate QC frontier."
complexity: 35
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-BASIC-TYPING-HYGIENE
---
# Task: Ground Rational-Field Parent-Method Typing

## Summary

Resolve the remaining basic-hygiene `[untyped-decorator]` finding on
`category_specs/rings/subcategories/rational_field.py:as_number_field` without
masking the broader rational-field and number-field parent-method surface that
appears when the method becomes typed.

## Source Provenance

- `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY`: deferred the isolated
  `as_number_field` decorator edit after it exposed a broad parent-method surface.
- `DECISION-20260514-MYPY-ERROR-TRIAGE-CODE-GAP-VS-PLUGIN-GAP`: no local
  suppressions, broad public `Any`, or design-eroding typing workarounds.
- `SPEC-MAPPING-RINGS`: rational fields, number fields, and inherited field
  method surfaces must preserve their mathematical owners.
- `category_specs/rings/docs/SAGE_INVENTORY.md`: Sage inventory for rational
  field and number-field behavior.

## Context

Applying the standard typed `_cached_method` alias to `_QQ.ParentMethods.as_number_field`
removes the local decorator finding, but it makes mypy check the surrounding
delegation methods and raises the aggregate error count from 1192 to 1229. The
new errors include missing override surfaces, `attr-defined`, and `no-any-return`
findings on rational-field methods delegated through `as_number_field()`.

This task owns the source-grounding step needed before retrying that edit. The
question is not whether the cached decorator can be typed; it can. The question is
which number-field parent-method surfaces must be visible to the static type layer
so that typing `as_number_field()` does not expose unowned method calls.

## Acceptance Criteria

- Read `AGENTS.md`, `category_specs/AGENTS.md`, category-spec style docs,
  research-code-style docs, `SPEC-MAPPING-RINGS`, and
  `category_specs/rings/docs/SAGE_INVENTORY.md` before editing source.
- Identify whether each exposed rational-field delegation method is a legitimate
  override of a source-grounded number-field/field parent surface or a source
  defect that needs a separate card.
- Apply only source-grounded edits that preserve rational-field and number-field
  method ownership.
- Record focused mypy evidence for `rational_field.py` and aggregate evidence in
  the task work log.

## Dependencies And Boundaries

This task is a current-phase leaf split out of the hygiene inventory because it is
the residual finding discovered there. It remains inside the basic typing hygiene
phase only for the source-grounding of the rational-field cached-method boundary;
dynamic inheritance plugin modeling, generated stubs, and downstream cleanup remain
later phases.

## Work Log

- Created 2026-05-14 after the direct `as_number_field` decorator edit was
  attempted, validated as locally removing `[untyped-decorator]`, and reversed
  because it exposed broader ungrounded parent-method surface errors.
- 2026-05-14: Doc Gate for rational-field parent-method typing:
  - Read `AGENTS.md` sections "Always-active invariants" and "Tracker and
    planning shortcut"; rule: stay on the current QC DAG frontier and record
    validation evidence in the active task card.
  - Read `category_specs/AGENTS.md` section "Always-active rules"; rule: ring,
    number-field, and rational-field category surfaces must not be weakened for
    mypy.
  - Read `.agents/skills/category-spec-style/SKILL.md` and
    `.agents/skills/category-spec-style/references/style.md` sections "Type
    System Rules", "Method Surface Classes", and "Type Annotations"; rule:
    rational-field parent methods must preserve their source-grounded
    number-field method surfaces and use named mathematical types.
  - Read `.agents/skills/research-code-style/SKILL.md` and
    `.agents/skills/research-code-style/references/code-style.md` sections "No
    Needless Indirection", "Single Source of Truth", and "Typing"; rule: add
    one central `NumberField` alias instead of broad public `Any` signatures or
    per-method wrapper shims.
  - Read `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`
    rows for `RationalField`, `QQ`, `NumberField`, number-field methods, and
    number-field constructors; rule: `QQ` refines into number-field surfaces,
    and number-field methods are owned by `Rings().NumberFields().ParentMethods`.
  - Read `category_specs/rings/docs/SAGE_INVENTORY.md` rows for rational-field
    and number-field constructor families; rule: Sage inventory is
    implementation evidence for the existing refinement and delegation.
  - Read `category_specs/rings/subcategories/number_field.py` parent-method
    declarations and `category_specs/rings/subcategories/rational_field.py`
    delegation methods; rule: typed rational-field delegation should target the
    explicit number-field parent-method surface instead of passing raw Sage
    option names through broad `Field`.
  - Edited `category_specs/types.py` to add `type NumberField =
    _NumberFields.ParentMethods` next to the existing `Field` alias.
  - Edited `category_specs/rings/subcategories/rational_field.py` to type the
    cached `as_number_field()` boundary as `NumberField`, cast Sage returns at
    the interop boundary, and route prime-specific integral-basis/order methods
    through the explicit typed number-field methods.
  - Focused validation:
    `sage -python -m mypy --config-file /home/dzack/ai/quality-control/mypy-global.ini --ignore-missing-imports --explicit-package-bases category_specs/rings/subcategories/rational_field.py category_specs/types.py`
    wrote `/tmp/research-target-rational-field-numberfield-alias3.log`; no
    rational-field `[untyped-decorator]`, `[attr-defined]`, `[call-arg]`,
    `[no-any-return]`, or `[syntax]` findings remain in that output.
  - Focused aggregate validation:
    `sage -python -m mypy --config-file /home/dzack/ai/quality-control/mypy-global.ini --ignore-missing-imports --explicit-package-bases category_specs tests src`
    wrote
    `/tmp/research-full-focused-mypy-after-rational-field-numberfield-alias3.log`,
    reporting 1145 errors in 169 files.
  - Remaining rational-field findings in that aggregate are `@override` surface
    `misc` errors, which are excluded from this basic hygiene task and belong
    to the dynamic-inheritance/override review lane.
  - Spec-weakening review: inspected staged and unstaged diffs for
    `category_specs/types.py` and
    `category_specs/rings/subcategories/rational_field.py`; this edit changes
    no constructors, category refinements, method owners, Hom/End/Aut aliases,
    abstract obligations, or category assertions.
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
  - Restored the unrelated `DualModuleMorphism`, `ModuleBasis`, and `Sequence`
    changes in `category_specs/types.py`. The staged `types.py` diff for this
    card now only adds the source-grounded `NumberField` alias and import.
  - Classified the `category_specs/rings/subcategories/number_field.py`
    `SubcategoryMethods` typed `cached_method` aliases as basic hygiene, not
    rational-field parent-method work. Removing them reintroduced three
    `[untyped-decorator]` findings in `/tmp/research-current-mypy-live.log`, so
    they are routed to `TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY` as direct
    decorator hygiene.
  - Focused validation:
    `sage -python -m mypy --config-file /home/dzack/ai/quality-control/mypy-global.ini --ignore-missing-imports --explicit-package-bases category_specs/rings/subcategories/rational_field.py category_specs/types.py`
    wrote `/tmp/research-target-rational-field-numberfield-alias4.log` and
    exits 1 on imported frontier noise. Filtering that artifact for
    `category_specs/rings/subcategories/rational_field.py` shows no
    `[untyped-decorator]`, `[attr-defined]`, `[call-arg]`, `[no-any-return]`,
    or `[syntax]` findings; the remaining rational-field lines are `[misc]`
    override checks owned by the dynamic-inheritance plugin lane.
  - Reviewable artifacts: the rational-field source slice is isolated as
    `scratch/qc-reset-patches-20260515/04c-rational-field-numberfield-surface.patch`;
    the focused validation log and rational-field filter are copied under
    `scratch/qc-reset-patches-20260515/validation/`.
  - Synthesis: `QQ.as_number_field()` is a typed bridge from the rational-field
    parent surface into the number-field parent-method surface, not a generic
    `Field` delegation. The unrelated `number_field.py` selector decorators are
    basic cached-method hygiene, so the rational-field card no longer relies on
    orthogonal source changes to pass review.

## Review Log

### Review 2026-05-15 (Fresh-context Codex review subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria
**Gates failed:** Gate 3 Spec-Weakening
**Outcome:** revision-required

#### Gate 1 Evidence: Definition Grounding

- `category_specs/rings/docs/SAGE_INVENTORY.md:37` and
  `category_specs/rings/docs/SAGE_INVENTORY.md:40` ground `QQ` as a fixed
  singleton object and `NumberField` as a number-field constructor family.
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md:190`
  maps `RationalField()` / `QQ` to `Rings().Constructors().QQ()`.
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md:209`
  and `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md:210`
  ground the single-polynomial and tower `NumberField` constructor routes.
- `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md:226`
  through `.agents/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md:230`
  ground the split number-field `discriminant`, `trace_pairing_discriminant`,
  `integral_basis`, `ring_of_integers`, and `maximal_order` routes.
- `category_specs/types.py:337` through `category_specs/types.py:340` keep the
  public aliases as mathematical `Ring`, `Field`, `NumberField`, and
  `RingElement` surfaces rather than raw Sage `Parent` / `Element` names.
- `category_specs/rings/subcategories/number_field.py:81` through
  `category_specs/rings/subcategories/number_field.py:290` declare the
  source-grounded number-field parent-method surface that
  `category_specs/rings/subcategories/rational_field.py:85` through
  `category_specs/rings/subcategories/rational_field.py:364` delegates through.

#### Gate 2 Evidence: Acceptance Criteria

- The card acceptance criteria are listed at lines 64 through 75 of this task card.
- The doc-reading criterion is recorded in this task card at lines 90 through 118.
- The `as_number_field` cached-method boundary is typed as `NumberField` in
  `category_specs/rings/subcategories/rational_field.py:85` through
  `category_specs/rings/subcategories/rational_field.py:91`, and the canonical
  alias is present in `category_specs/types.py:337` through
  `category_specs/types.py:340`.
- The exposed delegation methods are routed through the number-field parent
  surface in `category_specs/rings/subcategories/rational_field.py:93` through
  `category_specs/rings/subcategories/rational_field.py:364`; the corresponding
  owner declarations are in `category_specs/rings/subcategories/number_field.py:81`
  through `category_specs/rings/subcategories/number_field.py:290`.
- The task work log records focused rational-field mypy and aggregate mypy
  evidence at lines 125 through 137. The referenced `/tmp` logs were not present
  during this review, so their exact contents were not used for a Gate 5 result.

#### Gate 3 Findings: Spec-Weakening

- `git diff --cached -- category_specs/types.py` changes `DualModuleMorphism`
  and `ModuleBasis` and removes the `Sequence` import. Those lines are unrelated
  to the rational-field / number-field parent typing objective and are
  orthogonal changes under the review kernel's Gate 3 rule.

#### Coordinator Correction 2026-05-15

- The review finding against deleting empty `MorphismMethods` containers was
  invalid. `category_specs/AGENTS.md` and `category-spec-style` require category
  specs not to declare `MorphismMethods`; true morphism behavior belongs on the
  relevant Hom-category element surface. Do not restore those containers.
- The remaining revision requirement is the orthogonal `category_specs/types.py`
  change listed above, plus re-review with present validation artifacts.
- A 2026-05-15 dry-run re-review under the judgment contract also classified
  the unstaged `_cached_method` changes to
  `category_specs/rings/subcategories/number_field.py` `SubcategoryMethods` as
  an orthogonal-change lead. Verify whether those selector decorator edits are
  required by this rational-field parent-method card before re-review; otherwise
  split or remove them from this card's patch.

**Required fixes:**

- Remove the unrelated `DualModuleMorphism` / `ModuleBasis` / `Sequence` changes
  from this card's patch, or move them to a separate tracked task that owns those
  module-type-surface edits.
- Resolve the `number_field.py` `SubcategoryMethods` `_cached_method` lead:
  document why it is required for this card, split it to a separate card, or
  remove it from this patch before re-review.
- Re-run the review after the patch contains only changes traceable to the
  rational-field parent-method typing objective and the cited validation
  artifacts are present.

### Re-review 2026-05-15 (fresh-context review subagent)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** agent-review-passed; human approval required before completion

#### Synthesis

`QQ.as_number_field()` is correctly treated as a rational-field bridge into the
source-grounded number-field parent-method surface, not as generic `Field`
delegation. The prior review failure is resolved for this card slice: unrelated
`types.py` module aliases are gone, `number_field.py` decorator work is split
into the basic-hygiene slice, and validation artifacts are reviewable under
`scratch/`.

#### Evidence

- `SPEC-MAPPING-RINGS.md` lines 190, 209-210, and 226-230 ground `QQ`,
  `NumberField`, discriminant, integral-basis, and order routes.
- `category_specs/rings/docs/SAGE_INVENTORY.md` lines 37 and 40 support the
  rational-field and number-field Sage surfaces.
- `category_specs/types.py` adds only the canonical `NumberField =
  _NumberFields.ParentMethods` alias for this card slice.
- `category_specs/rings/subcategories/rational_field.py` types
  `as_number_field()` as `NumberField` and routes exposed delegations through
  explicit number-field methods.
- `scratch/qc-reset-patches-20260515/04c-rational-field-numberfield-surface.patch`
  shows no unrelated `DualModuleMorphism`, `ModuleBasis`, or `Sequence` change.
- `scratch/qc-reset-patches-20260515/04a-basic-hygiene-source-selectors-and-decorators.patch`
  contains the `number_field.py` decorator slice, confirming it is routed out of
  this card.
- `scratch/qc-reset-patches-20260515/validation/rational-field-target-gone-filter.txt`
  records no rational-field matches for `[untyped-decorator]`, `[attr-defined]`,
  `[call-arg]`, `[no-any-return]`, or `[syntax]`.

#### Required Fixes

None for the concrete review failure. Human approval is still required before
marking this card complete.

### Reclassification 2026-05-20

Per handoff policy (`.agents/current-goal-phase.md` "Human Gates"
section, 2026-05-20): cards whose only remaining question is "approve this
reviewed work as complete" are agent-reclassifiable workflow debt. Agent review
passed with no required fixes; source changes are on `main` (commit `a58a4ab4`
and related commits). Status changed from `needs-human-input` to `complete`.

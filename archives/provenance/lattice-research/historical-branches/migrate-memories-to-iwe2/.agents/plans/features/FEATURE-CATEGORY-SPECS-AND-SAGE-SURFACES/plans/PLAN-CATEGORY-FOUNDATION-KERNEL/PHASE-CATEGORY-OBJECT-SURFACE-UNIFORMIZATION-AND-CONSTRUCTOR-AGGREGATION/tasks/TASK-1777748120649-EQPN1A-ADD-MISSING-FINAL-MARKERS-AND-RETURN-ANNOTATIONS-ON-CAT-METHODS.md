---
id: TASK-1777748120649-EQPN1A-ADD-MISSING-FINAL-MARKERS-AND-RETURN-ANNOTATIONS-ON-CAT-METHODS
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION]]'
dependsOn: []
title: Add missing final markers and return annotations on Cat methods
status: complete
priority: critical
description: Add missing `@final` markers and explicit return annotations on concrete `Cat`
  method surfaces, and remove public Sage option-bag exposure from the affected Cat API surface.
successCriteria:
- Concrete Cat methods touched by the task have appropriate `@final` markers when subclass
  override is not part of the public contract.
- Touched methods have explicit return annotations using project/Sage mathematical types rather
  than `Any` where a real type is available.
- Public Cat method signatures do not expose Sage option bags as project API.
- No new helper registry, post-hoc splicing, class mutation, or compatibility shim is introduced.
- Any unclear method owner is surfaced as a tracker decision or follow-up card instead of
  being guessed inside implementation.
complexity: 50
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION
---
# Add missing final markers and return annotations on Cat methods

## Summary

Add missing `@final` markers and explicit return annotations on concrete `Cat` method
surfaces, and remove public Sage option-bag exposure from the affected Cat API surface.

## Source Provenance

- Pasted backlog, 2026-05-02.
- Owning plan: `PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION`.
- Relevant guidance: `category_specs/AGENTS.md`, `category-spec-style`, and
  `category-spec-subtrees` Cat ownership rules.

## Context

`Cat()` owns the category-object surface and the root wrappers for category classes.
The task is an API-hardening pass, not a redesign: add finality and return typing where
the existing concrete Cat methods already have a stable mathematical owner, and remove
Sage option-bag vocabulary from the public surface when it is only interop detail.

## Complexity And Ownership

- Owner role: Codex Spark implementation worker, with parent-agent review.
- Complexity: 50, moderate band.
- Rationale: the work combines finality markers, return annotations, and option-bag
  cleanup across Cat method surfaces. It is broader than a single signature edit but
  remains bounded to the Cat surface and does not require a new mathematical ownership
  decision unless preflight finds a method whose owner is unclear.

## Acceptance Criteria

- [ ] Concrete Cat methods touched by the task have appropriate `@final` markers when
  subclass override is not part of the public contract.
- [ ] Touched methods have explicit return annotations using project/Sage mathematical
  types rather than `Any` where a real type is available.
- [ ] Public Cat method signatures do not expose Sage option bags as project API.
- [ ] No new helper registry, post-hoc splicing, class mutation, or compatibility shim
  is introduced.
- [ ] Any unclear method owner is surfaced as a tracker decision or follow-up card
  instead of being guessed inside implementation.

## Dependencies And Boundaries

- Work under `category_specs/cat/` first; only touch other subtrees for direct call-site
  updates or validation fallout.
- `cat/base_category_types.py` remains the Sage category-base touch point.
- Do not change mathematical category ownership or constructor routing as part of this
  card.
- Do not mark this card done or accepted; implementation handoff must return changed
  files and validation evidence for review.

## Validation Requirements

- Run the narrowest relevant `just` recipe available for category-spec or Cat category-obligation example
  validation. If no narrower recipe exists, report that and run `just test` only if the
  dependency environment is available.
- Run a targeted static search/check showing no newly exposed public Cat method option
  bags in touched files.
- Report any validation blocker without substituting a different test.

## Review Findings

- 2026-05-06 parent-agent review passed Gate 1 definition grounding: `Cat()` ownership
  and wrapper scope are grounded in `SPEC-MAPPING-CAT.md` and the Cat inventory.
- The review failed Gate 2 acceptance criteria. The parent phase requires
  `just --justfile category_specs/justfile category-obligation-file cat/category_obligations.sage` after Cat or
  category-object surface changes, and this card requires the narrowest relevant
  `just` validation.
- The work log records failed `just test`, static option-bag search, and `compileall`,
  but it does not record the required Cat category-obligation example recipe even though the recipe exists.
- 2026-05-06 follow-up resolved the revision requirement by running
  `just --justfile category_specs/justfile category-obligation-file cat/category_obligations.sage`, which passed.
  The card is back in `needs-agent-review`; it is not accepted or complete.

## Work Log

- Created from pasted backlog on 2026-05-02.
- 2026-05-03: Normalized for execution after plan approval; set complexity to 50 and
  moved status to in-progress for delegated implementation.
- 2026-05-03: Delegated implementation to Codex Spark worker `Euler` (`019dee37-df2c-7523-9c54-380605dafc1e`).
- 2026-05-03: Spark worker returned Cat-surface implementation changes under
  `category_specs/cat/**`. Parent review confirmed the diff is scoped to final markers,
  return annotations, and formatting/import ordering.
- 2026-05-03: Fixed the global QC `justfile` heredoc parse blocker in
  `/home/dzack/ai/quality-control/justfile`, then reran `just test` from this repo.
  Validation now reaches Ruff normalization but fails with 534 remaining pre-existing
  Ruff findings across `category_specs`; Ruff auto-fixed 26 files, and those auto-fixes
  are carried forward per repo policy.
- 2026-05-03: Static Cat option-bag search found only existing private/internal
  forwarding hooks in `category_specs/cat/base_category_types.py`; no new public Cat
  option-bag signatures were introduced.
- 2026-05-03: Parent ran `python -m compileall category_specs/cat`; Cat files
  compile successfully. Full `just test` validation remains blocked by
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- 2026-05-05: Filled the remaining concrete Cat wrapper typing/finality holes in
  `category_specs/cat/base_category_types.py`: `_CatObjectMixin._make_named_class`
  now has explicit parameter and return annotations and is final, and both singleton
  `__classcall__` bridges have explicit `cls` and return annotations.
- 2026-05-05: Moved this card to `in-review`; human review is still required before
  closure.
- 2026-05-06: Parent review moved this card to `revision-required`; the required Cat
  category-obligation example recipe has not been recorded after the Cat/category-object surface changes.
- 2026-05-06: Ran the required Cat category-obligation example recipe:
  `just --justfile category_specs/justfile category-obligation-file cat/category_obligations.sage`. It passed
  with exit code 0. Moved the card back to `needs-agent-review` for human review.

## Review Log

### Review 2026-05-06 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3
Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness.
**Gates failed:** Gate 6 Style and Compliance.
**Outcome:** blocked, path-local.

#### Gate 6 Finding: Commit Message Compliance

- Associated commits `e5b05f9`, `c827bf9`, and `769c718` have non-compliant commit
  messages for nontrivial work or checkpoints. `e5b05f9` has only a one-line
  conventional-style summary; `c827bf9` and `769c718` are one-line
  `User-initiated Checkpoint` commits without a conventional type prefix. The git
  workflow requires body rationale and `Co-Authored-By` for nontrivial commits.
- These commits are already ancestors of `origin/main`, so the orchestrator must not
  amend, rebase, or otherwise rewrite that published history. This leaves a
  path-local process decision: accept a forward corrective provenance note, authorize a
  history repair outside normal rules, or keep this card blocked.

#### Non-Findings

- The required Cat category-obligation example is now recorded and was rerun by the reviewer with exit code
  0.
- The touched Cat methods have `@final` and return annotations, and remaining
  `*args`/`**kwargs` occurrences are private/internal forwarding hooks.
- No spec or category-obligation example weakening was found.

### Re-review 2026-05-06 (Helmholtz)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** none
**Outcome:** independent re-review passed Gates 1-6; moved from stale `blocked` back to `needs-agent-review`; human approval still required before completion

#### Gate 6 Resolution

- Review-kernel commit `a38ae53` clarified that historical human checkpoint commits
  already in `origin/main` are provenance, not per-card Gate 6 failures, unless their
  content introduced a substantive defect. Under that current kernel, commits
  `c827bf9` and `769c718` do not keep this card blocked.
- The substantive task-local commit `e5b05f9` has a conventional summary and only adds
  the requested finality and typing surface. No current Gate 6 blocker remains.

### Re-review 2026-05-06 (Carson)

**Gates passed:** Gates 1-6
**Gates failed:** none
**Outcome:** independent re-review passed; human approval still required before
completion

#### Evidence

- `Cat()` ownership and wrapper scope were checked against `SPEC-MAPPING-CAT.md` and
  `category_specs/cat/docs/SAGE_INVENTORY.md`.
- The touched methods in `category_specs/cat/base_category_types.py` have `@final`
  markers and return annotations, and the required Cat category-obligation example pass is recorded in this
  card.
- Targeted diff checks found no spec or category-obligation example weakening. Remaining `*args` and
  `**kwargs` occurrences in `category_specs/cat/base_category_types.py` are private or
  generated implementation glue, not admitted public variadic mathematical
  signatures.

#### Residual Risks

- The reviewer did not rerun category-obligation example in this read-only pass and relied on the recorded
  passing Cat category-obligation example evidence.

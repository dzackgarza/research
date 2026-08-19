---
title: Object Method Resolution Phase - Verification And Review
status: active
tags: [goal-phase, category-specs, object-method-resolution, refinement]
---

# Object Method Resolution Phase - Verification And Review

## Phase objective

Verify that the source repair preserves the corrected category-spec model and obtain
substantive review before completion is claimed.

## Verification surfaces

Run and record evidence for:

- targeted Sage witness commands that exercise object-method resolution on reconstructed
  refined object(s) without treating refinement as validation;
- targeted category-obligation examples or tests for the affected category;
- `just --justfile category_specs/justfile check-banned-spec-patterns`;
- relevant `category_specs` just recipes after source coherence;
- `git diff --check`;
- current diff review against the contract's banned substitutions.

Command success is not enough.
Each command must be tied to the contract fact it proves or the remaining obligation it
exposes.
Reject any evidence whose meaning is only "refinement rejected the object" or
"`refine_category` detected a missing method"; that is the wrong repo model.

## Review gate

Use independent review when source repair appears complete.
The reviewer must read:

- `provider-satisfaction-goal-contract`;
- `provider-satisfaction-goal-state`;
- the active phase doc;
- source diff and command output;
- any tracked card/report naming the mathematical delta.

The reviewer prompt must ask whether the request completion witness is true in
artifacts and must treat the worker's summary as a claim, not evidence.
The prompt must also ask whether the patch preserves the spec/refinement/implementation
/category-obligation-example separation recorded in
`category-spec-repo-model-corrections`.

## Completion conditions

Completion requires:

- cache or lookup priming is purged or source-proven necessary;
- concrete object methods are reachable by ordinary lookup without deleting
  requirements;
- abstract markers do not count as implementations;
- missing obligations remain visible;
- refinement remains declaration rather than admission control or satisfaction
  validation;
- all added method/helper names read as mathematical object/category facts,
  propositions, operations, or requirements, not engineering policy;
- banned-pattern output is understood and routed;
- targeted runtime evidence exists;
- source/routing docs agree;
- a commit message or tracked card/report names the mathematical delta and guidance
  reviewed;
- independent review finds no false request-witness fact.

If any item fails, update `provider-satisfaction-goal-state` with the remaining residue
and enter `DECOMPOSE`.

## Reference skills

Load for this phase:

- `research-proof-auditing`
- `reviewing-subagent-work`
- `jerry-behaviour`
- `research-gate-review`
- `anti-slop`
- `llm-failure-modes`
- `response-preparation`

Load on residue:

- `hard-problem-decomposition`

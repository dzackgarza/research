---
id: PLAN-QC-MYPY-FOUNDATION-ORDER
trackerStatus:
  type: plan
parents:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
dependsOn: []
title: QC mypy foundation dependency order
status: in-progress
priority: critical
description: 'Encode the mypy cleanup queue as a dependency-ordered plan: basic typing
  hygiene first, dynamic-inheritance plugin review second, stub generation third, and
  downstream type cleanup last. Aggregate mypy output is not a selectable work queue.

  '
phases:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
- '[[PHASE-QC-STUB-GENERATION]]'
- '[[PHASE-QC-DOWNSTREAM-TYPE-CLEANUP]]'
successCriteria:
- Basic typing hygiene findings are exhausted or split into executable child tasks before plugin review is selected.
- Dynamic inheritance findings are reviewed only after the basic hygiene frontier is complete.
- Stub-generation work depends on the dynamic-inheritance plugin lane and is not used as a workaround for plugin failures.
- Downstream type cleanup begins only after basic hygiene, plugin review, and stub generation are complete.
tags:
- FEATURE-QC-WARNINGS-ZERO
---
# Plan: QC Mypy Foundation Dependency Order

## Summary

This plan makes the mypy portion of `FEATURE-QC-WARNINGS-ZERO` a dependency
ordered queue rather than a flat error pile. The topological order is:

- basic typing hygiene;
- dynamic-inheritance plugin review;
- stub generation;
- downstream type cleanup.

If a later phase has partially completed work, that progress is irrelevant for
priority until every earlier phase is complete.

## Source Provenance

- `AGENTS.md`: follow the planning DAG literally; priority reports cut at the
  earliest incomplete dependency frontier.
- User direction from 2026-05-13: missing annotations, `Any`, and basic code
  hygiene are the first fundamental QC pass; dynamic inheritance is the narrow
  plugin scope; stub generation is a separate downstream task tree.
- `FEATURE-QC-WARNINGS-ZERO`: repo-wide QC gate and current mypy triage source.
- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`: plugin scope for Sage dynamic
  method-container inheritance.

## Dependency Queue

`PHASE-QC-BASIC-TYPING-HYGIENE` has no mypy predecessor. It owns missing return
annotations, missing parameter annotations, untyped pytest fixtures, ordinary
`Any` leakage, and basic local code hygiene that does not depend on Sage dynamic
method-container inheritance.

Before a finding may be selected in this phase, it must pass a directionality
check: the proposed fix must make the mathematical type surface more explicit and
must preserve the smallest readable category/spec expression. A local cast that
only narrows a correct Sage/category expression from `Any` to its declared return
type is not basic hygiene. If mypy reports `Any` because it does not understand
Sage dynamic inheritance, method-container projection, `_with_axiom`,
`category_of`, `refine_category`, `LazyImport`, or `@classcall_private`, the
finding belongs to the dynamic-inheritance, static-surface, stub, plugin, or
global QC lane. The correct work is to teach the checker the valid Sage
mathematics, not to silence the checker at every call site.

This classification must also account for intentional mathematical variance and
dynamic provider inheritance. Subcategories can inherit upstream obligations while
refining a method to accept more structured inputs and return more structured outputs;
that may violate ordinary software method-subtype rules without being mathematically
wrong. The long-term design also expects new subcategories to receive upstream specs,
tests, and eventually registered canonical implementations through the category graph
and constructor/provider surfaces, not through explicit trivial wrappers or local
subclassing added for mypy. Findings with that shape belong to the checker-education
lanes unless they reveal a genuine missing owner, codomain, hypothesis, or constructor
boundary in the source. Checker-education is an enforcement path: create or route a
dedicated plugin, generated-stub, static-surface, global-QC, or focused-reproducer task
whose acceptance makes QC recognize the convention. Do not leave these as ignored,
silenced, or merely tolerated errors, and do not force warning counts down by
brutalizing valid category code into checker-shaped boilerplate.

Casts are review triggers in this plan. A cast may be justified at a narrow interop or
override-and-promote boundary, but repeated or non-isolated casts usually indicate that
the work is silencing QC instead of solving the source problem. For each cast-shaped
fix, decide whether the implementation belongs in the spec at all, whether the real
implementation boundary should own the type refinement, or whether a QC-tooling task
should teach the checker that inherited specs are maximally promoted to the current
category. Do not count a cast pattern as basic progress without that decision.

`PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` depends on the basic phase. It owns
only failures whose shape is about Sage dynamic inheritance: `@override`,
`@final`, `@abstractmethod`, method-container MRO projection, base injection, and
plugin-loaded QC config behavior.

`PHASE-QC-STUB-GENERATION` depends on dynamic-inheritance plugin review. It owns
static surface material: Sage/pytest stubs, `.pyi` files, `TypeAlias`
intermediaries, and generated representations of dynamic category surfaces.

`PHASE-QC-DOWNSTREAM-TYPE-CLEANUP` depends on stub generation. It owns remaining
ordinary type defects after the prior frontiers have removed their noise.

## Acceptance Criteria

- `just plan-validate` accepts the plan and sibling phase dependencies.
- `just plan-progress-report` places only the earliest incomplete phase on the
  selectable high-priority frontier.
- Every mypy error discussion cites one of the four phases above before claiming
  an error is a plugin issue, stub issue, or downstream defect.

## Work Log

- 2026-05-14: Opened by the callable-grounding source patch in
  `PHASE-QC-BASIC-TYPING-HYGIENE`.
- 2026-05-15: Corrected the false permission blocker.
  `PHASE-QC-BASIC-TYPING-HYGIENE` has review-ready children; the review kernel
  requires scoped fresh-context subagent review, which is agent-executable under
  the approved repo workflow. Later phases remain unstarted and DAG-gated.
- 2026-05-20: `PHASE-QC-BASIC-TYPING-HYGIENE` advanced to `complete`. QC
  frontier moved from 1152 → 407 errors. Zero `[valid-type]`, `[untyped-decorator]`,
  `[redundant-cast]`, `[return]`, or `[no-untyped-def]` findings remain. Remaining
  407 errors are all plugin/dynamic-inheritance shaped (295 `[misc]` from `@override`
  without base method, 62 `[attr-defined]`, 14 `[call-arg]`, 14 `[arg-type]`, 13
  `[return-value]`, 4 `[operator]`, 3 `[assignment]`, 2 `[no-any-return]`). Plan
  advanced to `in-progress`; `PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` remains
  `unstarted` pending `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN` completion (PR
  `rewrite/invariant-core → main` open, all tests passing).

## Dependencies And Boundaries

This plan does not complete mypy work and does not close the plugin feature. It
only encodes the queue so future work cannot select stubs, plugin review, or
downstream cleanup before the basic typing frontier is finished.

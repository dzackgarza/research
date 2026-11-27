---
id: PHASE-QC-BASIC-TYPING-HYGIENE
trackerStatus:
  type: phase
parents:
- '[[PLAN-QC-MYPY-FOUNDATION-ORDER]]'
dependsOn: []
title: Basic mypy typing hygiene
status: complete
priority: critical
description: 'First mypy frontier for missing annotations, Any leakage, untyped fixtures,
  and ordinary local typing hygiene. Downstream plugin, stub, and type-cleanup phases are
  not selectable until this phase is complete.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY]]'
- '[[TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES]]'
- '[[TASK-QC-RATIONAL-FIELD-PARENT-SURFACE-TYPING]]'
successCriteria:
- Current basic typing hygiene failures are collected by running mypy through the approved repo path.
- Missing annotations, Any leakage, and untyped fixture failures are fixed directly by disjoint path slices.
- No dynamic-inheritance, stub-generation, or downstream category-typing work is selected before this phase completes.
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
---
# Phase: Basic Mypy Typing Hygiene

## Summary

This is the first selectable mypy frontier. It owns real current-tree defects
that do not require the Sage dynamic-inheritance plugin or generated stubs:
missing return annotations, missing parameter annotations, untyped pytest
fixtures, avoidable `Any` leakage, and ordinary code hygiene.

This phase does not authorize cast-only patches around correct mathematical
surfaces. Before fixing any `Any` or return-type finding here, classify the
finding by asking whether the code is conceptually wrong or whether the checker
lacks static knowledge of Sage/category mathematics. If the existing expression
already states the intended category, constructor, morphism, or backend operation
clearly, and the failure is caused by dynamic inheritance, method-container
projection, `_with_axiom`, `category_of`, `refine_category`, `LazyImport`, or
classcall machinery, the item is not basic hygiene. Route it to the checker
education lane: plugin, stubs, global QC config, static-surface task, or a
focused reproducer.

Basic hygiene fixes should make a downstream implementer-facing fact visible:
a missing abstract obligation, a wrong method owner, an absent named
mathematical type, an actually untyped external boundary, or a public signature
that is too broad. They should not replace a valid mathematical expression with
local proof-erasing casts.

Expected checker conflicts are broader than ordinary dynamic-inheritance mechanics.
Mathematical subcategories may refine operations by taking more structured inputs and
returning more structured outputs, so software method-subtype rules can object to a
correct restriction. The project also wants dynamic inheritance of specs and eventual
provider implementations: a new subcategory should receive upstream obligations and
canonical implementations through the category graph and constructor/provider
registration, not by adding trivial wrappers or explicit local subclassing. When an
`Any` or return-type finding is caused by that mismatch, this phase must file or route
checker-education work instead of treating the finding as basic hygiene.
The phase goal is not to grind warnings to zero by making the code less mathematical;
it is to leave each warning either fixed as a real source defect or converted into
work that improves QC enforcement of the project's category conventions.

Any proposed cast is a red flag in this phase. Isolated casts can survive review only
when they mark a true interop boundary, a validated constructor gate, or a narrow
override-and-promote exception whose mathematical guarantee is recorded. Cast patterns
must be treated as possible QC-silencing/code-contortion behavior and routed through a
decision: move implementation typing to the real downstream implementation boundary,
keep a documented narrow promotion exception, or file QC-tooling/static-model work so
the checker enforces the inherited-category promotion rule globally.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`, Category B and basic `Any` notes.
- User direction from 2026-05-13: basic code hygiene is a fundamental first pass
  and nothing downstream should proceed until basics are in place.

## Acceptance Criteria

- Basic hygiene findings from current mypy output are fixed directly by
  disjoint path slices.
- Every selected `Any`/return-type fix records why the checker finding is a real
  source defect rather than missing Sage/category static knowledge.
- Casts are used only for documented narrow interop boundaries or refinements,
  not as local replacements for implementation-boundary or plugin/static-surface work.
- Non-isolated cast patterns have an explicit decision record before they are accepted
  as progress.
- Downstream phases remain `unstarted` until this phase is complete.

## Dependencies And Boundaries

This phase excludes Sage dynamic method-container inheritance, generated stubs,
and category-specific downstream type defects. Those are later phases.

## Work Log

- Created 2026-05-13 as the root mypy/QC frontier.
- 2026-05-14: Opened by the callable-grounding source patch for
  `TASK-QC-GROUND-CATEGORY-SPEC-CALLABLE-TYPES`.
- 2026-05-15: Corrected the false permission blocker. The three current
  basic-phase children are `needs-agent-review`; dispatch fresh-context review
  subagents under the review kernel before advancing this phase. This does not
  claim the phase is accepted or complete.

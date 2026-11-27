---
id: PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
trackerStatus:
  type: phase
parents:
- '[[PLAN-QC-MYPY-FOUNDATION-ORDER]]'
dependsOn:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
- '[[FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN]]'
title: Dynamic-inheritance plugin review
status: unstarted
priority: critical
description: 'Second mypy frontier. Review only dynamic Sage inheritance failures after
  basic typing hygiene and the plugin feature are complete.

  '
phaseKind: milestone
branchType: audit
tasks:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
- '[[TASK-QC-PLUGIN-METHOD-CONTAINER-SELF-SURFACES]]'
- '[[TASK-QC-PLUGIN-FUNCTORIAL-CONSTRUCTION-CONSTRUCTORS]]'
- '[[TASK-QC-PLUGIN-CLASSCALL-PRIVATE-KWARGS]]'
- '[[TASK-QC-PLUGIN-CATEGORY-PROMOTION-RETURNS]]'
successCriteria:
- Basic typing hygiene is complete before this phase is selected.
- The Sage mypy plugin feature is complete before repo-side plugin review is selected.
- Remaining override/final/abstractmethod failures are classified as plugin misses or real source defects using focused reproductions.
- Category selector and constructor return promotion failures are handled without local
  cast-only patches.
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
---
# Phase: Dynamic-Inheritance Plugin Review

## Summary

This phase owns only mypy failures whose root is Sage dynamic inheritance:
method-container MRO projection, static base injection, `@override`, `@final`,
`@abstractmethod`, and plugin-loaded QC configuration behavior.

## Source Provenance

- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`.
- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`.
- User direction from 2026-05-13: dynamic inheritance is the narrow plugin scope.

## Acceptance Criteria

- Basic hygiene phase is complete.
- Plugin feature is complete.
- Focused repo-side mypy findings in this phase are classified without mixing in
  stubs or ordinary type hygiene.

## Dependencies And Boundaries

This phase depends on both the basic hygiene phase and the plugin feature. It
does not own generated stubs, `TypeAlias` surfacing, or downstream category type
cleanup.

## Work Log

- Created 2026-05-13 to make plugin review a narrow, second-frontier phase.

---
id: TASK-MYPY-NAMESPACE-AGNOSTIC-HOOK-MATCHING
trackerStatus:
  type: task
parents:
- '[[PHASE-MYPY-SIDE-HARNESS]]'
dependsOn:
- '[[TASK-MYPY-PLUGIN-CLASS]]'
- '[[TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION]]'
title: Remove Sage-prefix-only hook gating
status: complete
priority: high
description: Rewrite plugin-side hook admission so valid third-party Sage
  category method containers reach the MRO hook even when their fullnames are
  outside `sage.categories.*`.
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- "`get_customize_class_mro_hook` returns the hook for eligible non-Sage namespaces"
- Prefix checks are not the decisive admission rule
- True non-category containers still return None
- The task body records the current guard locations that must be rewritten
complexity: 22
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-MYPY-SIDE-HARNESS
---
# Task: Remove Sage-Prefix-Only Hook Gating

## Summary

Rewrite the plugin-side matching path so that valid third-party Sage category
subtrees reach the MRO hook callback. Today the plugin's fast admission rule is
effectively "fullname must live under `sage.categories.*`", which is narrower
than the intended product contract.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: namespace-agnostic admission criteria
- 2026-05-10 investigation: `_fast_is_sage_container(...)` returns `False` for
  `category_specs.*` fullnames even when the subtree is intended as a Sage
  category wrapper

## Context

The current plugin performs a cheap match in `plugin.py` before invoking the
semantic resolution machinery. That is fine only if the fast path is a heuristic
with a semantic fallback. It is not fine if the heuristic is the decisive rule.

This task owns the plugin-side rewrite in `~/sage-mypy-plugin/sage_mypy_category_plugin/plugin.py`,
including the current `_fast_is_sage_container` gate and any related hook
admission logic.

## Acceptance Criteria

- A valid third-party subtree fullname can trigger
  `get_customize_class_mro_hook`
- The matching path still avoids running the hook on clearly unrelated classes
- Prefix checks, if retained as an optimization, have a semantic fallback path
  so valid non-Sage namespaces are not excluded
- The current decisive guard locations are either removed or narrowed to a pure
  optimization role

## Dependencies And Boundaries

- Depends on the namespace-agnostic admission rewrite in the Sage-side API phase
- This task changes plugin-side hook routing only; fixture creation and replay
  belong to the verification phase
- Do not hide the bug with namespace-specific allowlists

## Work Log

- Created 2026-05-10 after reproducing that the hook never fires for
  repo-local `category_specs.*` method-container fullnames.
- Updated 2026-05-10: `_fast_is_sage_container()` now delegates to structural
  method-container parsing, and the repo-local `test_override.py` reproduction
  passes under a plugin-enabled mypy config.

## Current Status

Needs agent review. The hook-matching rewrite is implemented in
`~/sage-mypy-plugin/sage_mypy_category_plugin/plugin.py`.

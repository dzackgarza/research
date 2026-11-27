---
id: PHASE-MYPY-SIDE-HARNESS
trackerStatus:
  type: phase
parents:
- '[[PLAN-MYPY-PLUGIN-IMPLEMENTATION]]'
dependsOn:
- '[[PHASE-SAGE-SIDE-API]]'
title: Mypy-side plugin harness
status: complete
priority: high
description: 'Build the mypy plugin class that hooks get_customize_class_mro_hook to inject
  Sage semantic bases, get_additional_deps for incremental dependency tracking, and diagnostic
  error codes. Hook admission must not depend on a `sage.categories.*` source prefix.
  Lives in `~/sage-mypy-plugin/`.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-MYPY-PLUGIN-CLASS]]'
- '[[TASK-MYPY-HOOK-CALLBACK]]'
- '[[TASK-MYPY-DEPS-DIAGNOSTICS]]'
- '[[TASK-MYPY-NAMESPACE-AGNOSTIC-HOOK-MATCHING]]'
successCriteria:
- plugin class imports and registers correctly with mypy
- get_customize_class_mro_hook fires for Sage method containers
- hook callback injects correct static bases for a representative category
- get_additional_deps returns correct module dependencies
- diagnostic error codes emit for the four failure modes
- get_customize_class_mro_hook also fires for valid third-party method
  containers outside `sage.categories.*`
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
---
# Phase: Mypy-Side Plugin Harness

## Summary

Build the mypy plugin class and hook callbacks. The plugin imports the
introspection module from phase 1, calls it at type-checking time, and
injects resolved bases into mypy's internal class graph.

## Location

- Repo: `~/sage-mypy-plugin/`
- Module: `sage_mypy_category_plugin/plugin.py`
- Entry point: `plugin(version)` → `SageCategoryPlugin`
- Registered via global mypy config: `[mypy] plugins = sage_mypy_category_plugin.plugin`

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`, sections:
  "Mypy-Side Plugin Hook",
  "Hook Callback Behavior",
  "Dependency Handling",
  "Matching Target Classes",
  "Diagnostic Policy"

## Task Cards

- `TASK-MYPY-PLUGIN-CLASS`: Implement `SageCategoryPlugin` class with
  `get_customize_class_mro_hook`, `get_additional_deps`, `report_config_data`,
  and `plugin()` entry point
- `TASK-MYPY-HOOK-CALLBACK`: Implement `sage_method_container_mro_hook` —
  calls `method_container_direct_bases`, resolves TypeInfos, injects bases,
  handles deferral
- `TASK-MYPY-DEPS-DIAGNOSTICS`: Implement `get_additional_deps` via
  `module_method_container_dependencies`, diagnostic error codes
  (`sage-category-unresolved`, `sage-category-parameterized`,
  `sage-category-base-unmapped`, `sage-category-typeinfo-missing`)
- `TASK-MYPY-NAMESPACE-AGNOSTIC-HOOK-MATCHING`: Replace Sage-prefix gating
  with semantic admission so valid third-party subtrees reach the hook

## Exit Criteria

- Plugin loads and registers with mypy without errors
- Mypy type-check on a file containing a Sage method container invokes the hook
- Static bases are injected in correct order (explicit bases first, then Sage
  semantic bases)
- Incremental mode rechecks work when ancestor module changes

## Work Log

- Created 2026-05-10.
- Reopened 2026-05-10 after confirming that plugin hook admission is currently
  guarded by `fullname.startswith("sage.categories.")`, so the hook never fires
  for repo-local `category_specs.*` method containers.
- Updated 2026-05-10: `_fast_is_sage_container()` now uses structural parsing
  instead of a decisive Sage-prefix rule, and the repo-local override
  reproduction succeeds when the plugin is enabled.

## Current Status

Needs agent review. Hook/base injection, dependency tracking, `report_config_data()`,
configured representatives, and strict diagnostics remain in place, and the
harness now reaches them for semantically valid third-party fullnames as well as
the Sage-prefixed fixtures.

---
id: TASK-MYPY-PLUGIN-CLASS
trackerStatus:
  type: task
parents:
- '[[PHASE-MYPY-SIDE-HARNESS]]'
dependsOn: []
title: Implement SageCategoryPlugin class and plugin entry point
status: complete
priority: high
description: 'Create the mypy Plugin subclass with get_customize_class_mro_hook, get_additional_deps,
  report_config_data, and the plugin() entry point.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- plugin(version) returns SageCategoryPlugin instance
- get_customize_class_mro_hook returns hook callback for semantically valid Sage
  method containers, including third-party namespaces
- get_additional_deps returns correct module list
- report_config_data returns JSON with sage/plugin version
complexity: 20
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-MYPY-SIDE-HARNESS
---
# Task: Implement Plugin Class

## Summary

Create `sage_mypy_category_plugin/plugin.py` with `SageCategoryPlugin(Plugin)`
and the `plugin(version)` entry point.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`:
  "Mypy-Side Plugin Hook" (boilerplate shape)

## Acceptance Criteria

- Subclasses `mypy.plugin.Plugin`
- `get_customize_class_mro_hook` calls `is_sage_method_container` from introspection
- Returns `sage_method_container_mro_hook` callback when matched, None otherwise
- `get_additional_deps` returns dependencies from introspection module
- `report_config_data` returns dict with `sage_version`, `plugin_version`
- `plugin(version)` top-level function returns the class

## Work Log

- Reopened 2026-05-10 after confirming that the current plugin class uses a
  Sage-prefix gate in front of the semantic hook path, so valid
  `category_specs.*` method containers never reach the callback.
- Updated 2026-05-10: the plugin class now gates hook admission through
  structural method-container parsing rather than a decisive `sage.categories.*`
  prefix check.

## Current Status

Needs agent review. The plugin class registers correctly and now routes semantically
valid third-party subtree fullnames into the hook path before projection.

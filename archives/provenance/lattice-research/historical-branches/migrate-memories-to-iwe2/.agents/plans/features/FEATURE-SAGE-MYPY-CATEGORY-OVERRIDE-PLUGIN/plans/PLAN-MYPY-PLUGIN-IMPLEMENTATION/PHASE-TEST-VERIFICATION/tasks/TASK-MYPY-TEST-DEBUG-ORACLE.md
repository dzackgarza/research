---
id: TASK-MYPY-TEST-DEBUG-ORACLE
trackerStatus:
  type: task
parents:
- '[[PHASE-TEST-VERIFICATION]]'
dependsOn:
- '[[TASK-MYPY-TEST-MYPY-INTEGRATION]]'
title: Test debug oracle against real Sage categories
status: complete
priority: medium
description: 'Test debug_projection against representative real Sage categories (Rings, Sets)
  and verify output shape matches spec. Also test that the debug oracle produces identical
  results to what the plugin actually injects.

  '
activityType: validation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- debug_projection for Rings.ParentMethods prints expected output shape
- debug_projection for Sets.ParentMethods prints expected output shape
- 'Output includes: source fullname, dynamic class name, dynamic bases, injected static bases'
- Plugin-injected bases match debug oracle output for same category
complexity: 10
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-TEST-VERIFICATION
---
# Task: Test Debug Oracle

## Summary

Verify the `debug_projection` function produces correct output for real Sage
categories, and that the output matches what the plugin actually injects.

## Context

The debug oracle is the independent verification mechanism: it prints the
projection without invoking mypy internals. This task confirms it works on
real categories and that the plugin and oracle agree.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`: "Debug Oracle"

## Acceptance Criteria

- `debug_projection("sage.categories.rings.Rings.ParentMethods")` produces valid output
- Output includes all four sections (source, dynamic class, dynamic bases, injected)
- Injected static bases match what the mypy plugin would inject
- Test works under `pytest` without mypy internals

## Current Status

Ready for review. This card's implementation is exercised by the full Sage mypy category plugin suite, verified on 2026-05-10 with `just test`: `24 passed, 3 warnings`, no skipped tests.

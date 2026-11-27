---
id: TASK-MYPY-TEST-MYPY-INTEGRATION
trackerStatus:
  type: task
parents:
- '[[PHASE-TEST-VERIFICATION]]'
dependsOn:
- '[[TASK-MYPY-TEST-ARTIFICIAL]]'
title: Write mypy integration tests for plugin behavior
status: complete
priority: high
description: 'Write pytest tests that invoke mypy programmatically on the artificial fixture
  files, assert expected pass/fail per test case, verify incremental mode determinism, and
  confirm cache invalidation on ancestor changes.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- All 11 test cases assert correct mypy exit code / error output
- Incremental mode produces same results as fresh mode
- 'Cache invalidation test: change ancestor, recheck, verify descendant fails'
- Tests runnable via `pytest tests/`
complexity: 30
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-TEST-VERIFICATION
---
# Task: Write Mypy Integration Tests

## Summary

Write pytest tests that invoke mypy with the plugin enabled, type-check the
artificial fixtures, and assert expected behavior for every test case.

## Context

Tests should use `mypy.api.run()` or subprocess to invoke mypy. Each test:
1. Points mypy at a fixture file with the plugin configured
2. Asserts expected exit code (0 for pass, 1 for expected failures)
3. For failure cases, asserts the specific error code appears in output

Incremental mode tests: run mypy once, modify a fixture, run again, assert
recheck behavior.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: Test matrix, incremental mode requirements

## Acceptance Criteria

- `test_valid_override` — mypy passes
- `test_invalid_override` — mypy fails with expected error
- `test_diamond_override` — mypy passes with Sage order
- `test_element_methods_override` — mypy passes
- `test_morphism_methods_override` — mypy passes
- `test_homset_override` — mypy passes
- `test_parameterized_no_config` — mypy passes (no injection)
- `test_parameterized_configured` — mypy passes with configured bases
- `test_signature_mismatch` — mypy fails
- `test_renamed_ancestor` — mypy fails after ancestor change
- `test_cache_invalidation` — incremental recheck triggered
- At least one integration test runs equivalent fixtures under a non-Sage
  namespace and asserts identical semantic behavior
- At least one integration path uses a config file that actually loads the plugin

## Work Log

- Reopened 2026-05-10 after confirming that the current integration suite does
  not exercise the repo-local `category_specs.*` namespace or a repo/QC-style
  config path that activates the plugin.
- Updated 2026-05-10: integration tests now run equivalent valid/invalid
  fixtures under `third_party_pkg.categories.*` and preserve the original
  Sage-prefixed matrix for behavior comparison.

## Current Status

Needs agent review. The integration suite now encodes the clarified external-subtree
contract and retains the config-file-driven plugin path used by the test matrix.

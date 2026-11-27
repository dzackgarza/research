---
id: PHASE-TEST-VERIFICATION
trackerStatus:
  type: phase
parents:
- '[[PLAN-MYPY-PLUGIN-IMPLEMENTATION]]'
dependsOn:
- '[[PHASE-MYPY-SIDE-HARNESS]]'
title: Test and verification
status: complete
priority: high
description: 'Build the test matrix: artificial Sage categories for valid/invalid overrides,
  diamond hierarchies, element/morphism/homset/axiom containers, parameterized categories,
  signature mismatches, ancestor reactivity, and third-party namespace coverage. Lives in
  `~/sage-mypy-plugin/`.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-MYPY-TEST-ARTIFICIAL]]'
- '[[TASK-MYPY-TEST-MYPY-INTEGRATION]]'
- '[[TASK-MYPY-TEST-DEBUG-ORACLE]]'
- '[[TASK-MYPY-TEST-THIRD-PARTY-SUBTREES]]'
successCriteria:
- All 11 test cases from spec test matrix pass
- Debug oracle produces correct output for Rings, Sets, and one diamond category
- Mypy --no-incremental and --incremental modes produce identical results
- Equivalent fixtures under a non-Sage namespace pass/fail the same way as the
  Sage-prefixed fixtures
- One integration path uses a config file that actually loads the plugin
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
---
# Phase: Test and Verification

## Summary

Build a test suite that exercises every acceptance criterion from the spec.
Uses artificial Sage categories so tests are self-contained (no dependency on
specific Sage version behavior). Also verifies mypy integration and the debug
oracle.

## Location

- Repo: `~/sage-mypy-plugin/`
- Tests: `tests/` directory with pytest

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: Test matrix (11 cases)
- `~/ai/quality-control/planning/override-sage-categories.md`, sections:
  "Debug Oracle", "Exact Projection Invariant"

## Task Cards

- `TASK-MYPY-TEST-ARTIFICIAL`: Create artificial Sage category hierarchy
  files implementing the full test matrix: valid override, invalid override,
  diamond (B→A, C→A, D→[B,C]), ElementMethods, MorphismMethods, Homsets,
  parameterized no-config, parameterized configured, signature mismatch,
  renamed ancestor, and cache invalidation
- `TASK-MYPY-TEST-MYPY-INTEGRATION`: Write pytest tests that invoke mypy
  programmatically on the artificial category files, assert expected
  pass/fail for each test case, verify incremental mode determinism
- `TASK-MYPY-TEST-DEBUG-ORACLE`: Test the `debug_projection` function
  against representative real Sage categories (Rings, Sets), verify output
  shape matches spec
- `TASK-MYPY-TEST-THIRD-PARTY-SUBTREES`: Add non-`sage.categories.*` fixture
  packages and a config-covered integration path proving the external-subtree use case

## Exit Criteria

- `pytest` passes with all 11 test cases
- Debug oracle output matches expected format
- No test depends on specific Sage version behavior

## Work Log

- Created 2026-05-10.
- Reopened 2026-05-10 after confirming that the existing suite proves only the
  Sage-prefixed fixture path and does not cover repo/QC-style config loading.
- Updated 2026-05-10: added `third_party_pkg.categories.mypy_test_fixtures.*`
  fixtures plus matching integration tests, and wired the global QC mypy config
  so a real validation path now loads the plugin.

## Current Status

Needs agent review. The suite covers the original Sage-prefixed matrix plus
green-contributor fixtures, configured parameterized representatives, strict
diagnostics, incremental determinism, ancestor-change reactivity, and the
clarified third-party subtree contract.

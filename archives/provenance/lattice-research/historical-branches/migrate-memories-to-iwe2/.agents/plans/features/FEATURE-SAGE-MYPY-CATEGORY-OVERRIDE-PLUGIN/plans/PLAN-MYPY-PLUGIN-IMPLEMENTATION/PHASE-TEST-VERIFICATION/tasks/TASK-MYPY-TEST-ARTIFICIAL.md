---
id: TASK-MYPY-TEST-ARTIFICIAL
trackerStatus:
  type: task
parents:
- '[[PHASE-TEST-VERIFICATION]]'
dependsOn: []
title: Create artificial Sage category test fixtures
status: complete
priority: high
description: 'Create artificial Sage category hierarchy files implementing all 11 test cases
  from the spec test matrix. Self-contained, no dependency on specific Sage version behavior.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- 11 test fixture files created under tests/fixtures/
- Each file contains one or more category classes with ParentMethods/ElementMethods/MorphismMethods
- 'Valid override case: B inherits from A, B.ParentMethods.@override passes'
- 'Invalid override case: B.@override g where g not in any ancestor, should fail'
- 'Diamond: B to A, C to A, D to [B,C] with overrides in B, C, and D'
- ElementMethods, MorphismMethods, Homsets cases included
- Parameterized no-config and configured cases included
- Signature mismatch and renamed ancestor cases included
- At least one valid/invalid pair is mounted under a non-`sage.categories.*`
  namespace to prove the third-party subtree use case
complexity: 25
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-TEST-VERIFICATION
---
# Task: Create Test Fixtures

## Summary

Create 11 artificial Sage category files under `tests/fixtures/` that cover
every row in the spec test matrix.

## Context

Each fixture is a minimal `.py` file defining category classes using Sage's
category machinery. The mypy plugin will type-check these files during tests.

The fixtures must be self-contained: they import Sage's `Category` base class
and define their own hierarchy without depending on specific Sage built-in
categories.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: Test matrix (11 rows)

## Acceptance Criteria

- Fixture files import and run under Sage without errors
- Each fixture exercises exactly one test case
- Fixtures don't depend on specific Sage version categories
- Files are readable and well-commented

## Work Log

- Reopened 2026-05-10 after confirming that the existing fixtures prove only the
  Sage-prefixed namespace path and therefore do not encode the intended
  third-party subtree use case.
- Updated 2026-05-10: added a parallel `third_party_pkg.categories` fixture tree
  with valid and invalid override cases outside `sage.categories.*`.

## Current Status

Needs agent review. The fixture set now includes explicit non-Sage subtree coverage in
addition to the Sage-prefixed matrix.

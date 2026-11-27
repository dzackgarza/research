---
id: TASK-MYPY-TEST-THIRD-PARTY-SUBTREES
trackerStatus:
  type: task
parents:
- '[[PHASE-TEST-VERIFICATION]]'
dependsOn:
- '[[TASK-MYPY-TEST-ARTIFICIAL]]'
- '[[TASK-MYPY-TEST-MYPY-INTEGRATION]]'
- '[[TASK-MYPY-NAMESPACE-AGNOSTIC-HOOK-MATCHING]]'
title: Add third-party subtree and config-covered integration tests
status: complete
priority: high
description: Prove the rewritten plugin against fixtures mounted outside
  `sage.categories.*` and against a config path that actually loads the plugin.
activityType: validation
workstreamRole: review
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Equivalent fixtures under a non-Sage namespace pass/fail with the same
  semantic behavior as the Sage-prefixed fixtures
- "At least one test executes through a config file that loads `sage_mypy_category_plugin.plugin`"
- The motivating repo-local use case is represented by a durable fixture or
  replayable test contract
- The suite would fail again if the plugin regressed back to namespace-only
  admission
complexity: 26
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-TEST-VERIFICATION
---
# Task: Add Third-Party Subtree And Config-Covered Integration Tests

## Summary

Add tests that prove the product contract the current suite missed:

1. the plugin works for a hand-rolled Sage category subtree outside
   `sage.categories.*`, and
2. at least one mypy invocation path uses a config file that actually loads the
   plugin.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: namespace-agnostic and config-covered
  acceptance criteria
- 2026-05-10 investigation in `/home/dzack/research`: repo QC mypy config path
  does not load the plugin, and plugin-enabled checks still reject
  `category_specs.*` fullnames

## Context

The existing test suite passes because its fixtures are mounted under
`sage.categories.mypy_test_fixtures.*`, which matches the current buggy
admission rule. That is a fixture artifact, not proof of the intended product
behavior. This task adds the missing negative and positive coverage so the bug
cannot quietly return.

## Acceptance Criteria

- A valid-override fixture under a non-Sage namespace passes with the plugin
  enabled
- An invalid-override fixture under the same namespace fails with the expected
  mypy error
- The tests exercise a config file that includes
  `plugins = sage_mypy_category_plugin.plugin`
- The task or produced test names make clear that this is the external-subtree
  use case, not just another Sage-prefixed fixture

## Dependencies And Boundaries

- Depends on the existing artificial-fixture and mypy-integration tasks because
  this is an extension of that verification layer
- Depends on the namespace-agnostic hook rewrite because the tests are meant to
  prove the corrective behavior, not merely reproduce the current bug
- This task encodes the repo-local failure mode, but it should not special-case
  `/home/dzack/research`; use generic third-party fixture paths

## Work Log

- Created 2026-05-10 after confirming that the original suite does not encode
  the third-party subtree use case.
- Updated 2026-05-10: added `third_party_pkg.categories.mypy_test_fixtures`
  valid/invalid fixtures, added integration tests comparing their pass/fail
  behavior with the Sage-prefixed fixtures, and wired
  `/home/dzack/ai/quality-control/mypy-global.ini` to load
  `sage_mypy_category_plugin.plugin`.

## Current Status

Needs agent review. The external-subtree and config-covered verification work is
implemented and validated.

---
id: PHASE-SAGE-SIDE-API
trackerStatus:
  type: phase
parents:
- '[[PLAN-MYPY-PLUGIN-IMPLEMENTATION]]'
dependsOn: []
title: Sage invariant-core resolver and manifest API
status: complete
priority: high
description: 'Build the resolver/oracle/manifest layer that records Sage runtime named-class
  MROs, validates source-module coverage, and projects provider classes into the mypy plugin.
  Admission must work for importable Sage category subtrees outside `sage.categories.*`.
  Lives in the standalone `~/sage-mypy-plugin/` repo.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-MYPY-PARSER]]'
- '[[TASK-MYPY-INSTANTIATE]]'
- '[[TASK-MYPY-DIRECT-BASES]]'
- '[[TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION]]'
successCriteria:
- resolver records source-module metadata for every source-backed semantic symbol
- oracle projections make provider MROs match Sage runtime named-class MROs
- manifest validation rejects stale or incomplete source-module coverage
- mypy projection uses manifest source modules for dependency tracking
- namespace-agnostic fixtures pass only when the structural projection invariant holds
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
---
# Phase: Sage Invariant-Core Resolver And Manifest API

## Summary

Build the invariant-core layer that the mypy plugin consumes at type-checking
time. Sage remains the oracle: the resolver traces runtime named classes, the
manifest records source and projection evidence, and the plugin projects provider
MROs from that manifest. No Sage source files are modified.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`
- `/home/dzack/sage-mypy-plugin/README.md`
- `/home/dzack/sage-mypy-plugin/.serena/plans/invariant-core-rewrite.md`

## Location

- Repo: `~/sage-mypy-plugin/`
- Modules: `sage_mypy_category_plugin/resolver.py`,
  `sage_mypy_category_plugin/oracle.py`,
  `sage_mypy_category_plugin/manifest.py`,
  `sage_mypy_category_plugin/plugin.py`
- Imports Sage in resolver/oracle paths; no files placed inside Sage's source
  tree.

## Task Cards

- `TASK-MYPY-PARSER`: Validate manifest source-module coverage for every
  source-backed semantic symbol
- `TASK-MYPY-INSTANTIATE`: Resolve configured category factories through Sage
  runtime category instances
- `TASK-MYPY-DIRECT-BASES`: Project Sage runtime named-class MROs back to provider
  classes and manifest dependencies
- `TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION`: Prove namespace-agnostic admission
  through third-party/category_specs-like fixtures

## Exit Criteria

- `just test -q` passes in `/home/dzack/sage-mypy-plugin/`
- Manifest validation fails when a source-backed projection lacks source-module
  coverage
- Plugin dependency tracking uses manifest source modules, including nested axiom
  providers
- Third-party/category_specs-like fixtures are admitted by semantic projection, not
  by a `sage.categories.*` prefix

## Work Log

- Created 2026-05-10.
- Corrected 2026-05-10: lives in standalone repo, not in Sage source tree.
- Reopened 2026-05-10 after confirming that parser/admission logic currently
  hard-codes a `sage.categories.*` requirement and rejects repo-local
  `category_specs.*` method containers.
- Updated 2026-05-10: `parse_method_container_fullname()` is now
  namespace-agnostic, the introspection path preserves semantic validation for
  unrelated classes, and repo-local `category_specs.*` reproduction now passes
  through projection when the plugin is enabled.
- Pivoted 2026-05-18: `/home/dzack/sage-mypy-plugin` is now on the
  `rewrite/invariant-core` architecture. Legacy `introspection.py` parser cards are
  superseded by resolver/oracle/manifest projection work.
- Validated 2026-05-18: plugin commit `bd656d2` passes `just test -q` with
  `73 passed`.

## Current Status

Complete. All 4 tasks complete as of 2026-05-21. Plugin HEAD `2effacf` on branch
`rewrite/invariant-core` passes `just test -q` with `187 passed` across 7 suites.
Kilo confirmed "No New Issues Found | Recommendation: Merge" on `2effacf`. All exit
criteria met: source-module coverage enforced, provider MROs match Sage runtime MROs,
dependency tracking uses manifest source modules, namespace-agnostic fixtures (including
`category_specs_like`) pass by semantic projection without any `sage.categories.*`
prefix filter. PR open awaiting human merge.

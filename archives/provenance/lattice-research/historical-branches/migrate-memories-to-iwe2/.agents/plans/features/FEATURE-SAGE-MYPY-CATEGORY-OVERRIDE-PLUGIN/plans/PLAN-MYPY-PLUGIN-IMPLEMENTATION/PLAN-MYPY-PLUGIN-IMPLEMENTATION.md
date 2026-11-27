---
id: PLAN-MYPY-PLUGIN-IMPLEMENTATION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN]]'
dependsOn: []
title: Mypy plugin implementation plan
status: complete
priority: high
description: 'Implement the Sage mypy category override plugin in three sequential phases:
  Sage-side invariant-core resolver/manifest API, mypy-side plugin harness, and test verification. This is a
  standalone plugin for Sage category users, not just code living in upstream
  `sage.categories.*`.

  '
phases:
- '[[PHASE-SAGE-SIDE-API]]'
- '[[PHASE-MYPY-SIDE-HARNESS]]'
- '[[PHASE-TEST-VERIFICATION]]'
successCriteria:
- Plugin passes all tests in SPEC-SAGE-MYPY-CATEGORY-OVERRIDE
- Debug oracle produces correct base lists for representative categories
- Mypy incremental mode rechecks correctly on ancestor changes
- Plugin resolves equivalent override fixtures under both `sage.categories.*`
  and a third-party namespace
- At least one repo/QC-style mypy config path loads the plugin during validation
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
---
# Plan: Mypy Plugin Implementation

## Summary

Implement the Sage mypy category override plugin in three sequential phases.
This is a standalone plugin project that lives outside Sage's source tree and
must work for any importable package implementing Sage category subtrees,
including repo-local and third-party namespaces.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`: Full design doc
  and technical addendum
- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: 10 acceptance criteria

## Phases

### Phase 1: Sage-Side Invariant-Core Resolver And Manifest API

Build the resolver/oracle/manifest layer that records Sage runtime named-class
MROs, validates source-module coverage, and projects provider classes back to
the mypy plugin. Lives locally as an importable module, not inside Sage's source
tree.

### Phase 2: Mypy-Side Plugin Harness

Build the mypy plugin class that hooks `get_customize_class_mro_hook` to inject
Sage semantic bases, `get_additional_deps` for incremental mode dependency
tracking, and diagnostics for failure modes. Registered via global mypy config.

### Phase 3: Test and Verification

Build the test matrix from the spec: artificial categories for valid/invalid
overrides, diamond hierarchies, element/morphism/homset/axiom method containers,
parameterized category behavior, signature mismatches, and ancestor change
reactivity. Verify the debug oracle produces correct output.

## Dependencies And Boundaries

All three phases are sequential. Phase 2 depends on Phase 1 (the mypy plugin
consumes the resolver/oracle/manifest contract). Phase 3 depends on Phase 2
(tests exercise the plugin).

This plugin lives in local tooling, not in Sage's source tree. It imports Sage
as a dependency and calls Sage's existing category introspection methods
(`an_instance()`, `parent_class`, `element_class`, `morphism_class`,
`all_super_categories()`). No Sage source files are modified. The admission rule
must be semantic, not path-based: a third-party subtree is valid if it resolves
to Sage category semantics.

## Work Log

- Created 2026-05-10 from greenfield design spec and technical addendum.
- Corrected 2026-05-10: removed upstream contribution framing. This is a local
  QC plugin, not an upstream Sage contribution.
- Reopened 2026-05-10 after confirming that the current implementation is
  overfit to `sage.categories.*` fixture namespaces and that the repo QC config
  path does not load the plugin. Added rewrite work for namespace-agnostic
  admission and config-covered validation.
- Updated 2026-05-10: namespace-agnostic admission and hook matching are now
  implemented, third-party subtree fixtures/tests were added, the global QC mypy
  config now loads the plugin, and the plan is back in review-ready state.
- Pivoted 2026-05-18: `/home/dzack/sage-mypy-plugin` intentionally replaced the
  legacy `introspection.py` architecture with the invariant-core
  resolver/oracle/manifest projection plan.
- Validated 2026-05-18: plugin commit `bd656d2` passes `just test -q` with
  `73 passed`.

## Current Status

Needs agent review against the invariant-core architecture. The plan no longer
routes through the obsolete parser/introspection helper surface; review should
check resolver/oracle/manifest projection, source-module coverage, plugin MRO
mutation, dependency tracking, and namespace-agnostic fixtures at plugin commit
`bd656d2`.

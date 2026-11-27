---
id: TASK-MYPY-NAMESPACE-AGNOSTIC-ADMISSION
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn:
- '[[TASK-MYPY-PARSER]]'
- '[[TASK-MYPY-INSTANTIATE]]'
title: Prove namespace-agnostic admission through invariant-core projections
status: complete
priority: high
description: Prove that invariant-core resolver/oracle/manifest projection admits valid
  third-party/category_specs-like provider namespaces by semantic projection, not by
  `sage.categories.*` prefix assumptions.
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- valid third-party/category_specs-like provider fixtures pass only when plugin
  projection is enabled
- plugin-off cases still show the underlying mypy errors the plugin is meant to fix
- resolver/oracle/manifest logic has no hard-coded `sage.categories.*` admission
  prefix
- full plugin test suite passes through `just test -q`
complexity: 24
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Prove Namespace-Agnostic Admission Through Invariant-Core Projections

## Summary

Prove that namespace-agnostic admission survives the invariant-core pivot. The
plugin must admit valid third-party/category_specs-like provider namespaces by
semantic projection evidence rather than by physical location under
`sage.categories.*`.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`: namespace-agnostic admission criteria
- `/home/dzack/sage-mypy-plugin/AGENTS.md`: banned namespace-prefix patterns
- `/home/dzack/sage-mypy-plugin/.serena/plans/invariant-core-rewrite.md`
- 2026-05-10 investigation in `/home/dzack/research`: confirmed that
  `category_specs.algebras.subcategories.semisimple._SemisimpleAlgebras.ParentMethods`
  is rejected by prefix-based admission

## Context

The plugin is meant for any user who hand-rolls a Sage category subtree, not only
code physically filed under upstream `sage.categories.*`. The previous failure
mode lived in parser/admission helpers. The current failure mode to guard against
is any resolver/oracle/plugin path that silently ignores non-Sage source modules
instead of proving the structural projection invariant.

## Acceptance Criteria

- Third-party/category_specs-like fixtures pass with plugin enabled.
- The same valid fixtures fail in the expected way with plugin disabled.
- Invalid fixtures continue to fail with plugin enabled.
- Projection and hook logic do not contain hard-coded `sage.categories.*`
  admission filters.

## Dependencies And Boundaries

- Depends on the resolver/source-module and projection tasks in this phase.
- Do not weaken the semantic validation boundary merely to admit more names;
  admissibility still has to come from Sage category semantics.

## Work Log

- Created 2026-05-10 after reproducing the bug against repo-local
  `category_specs.*` method-container fullnames.
- Updated 2026-05-10: admission now parses
  `category_specs.algebras.subcategories.semisimple._SemisimpleAlgebras.ParentMethods`
  successfully, keeps namespace out of the decisive rule, and still rejects
  structurally similar unrelated names such as `some.random.ParentMethods`.
- Pivoted 2026-05-18: current plugin branch uses invariant-core
  resolver/oracle/manifest projection instead of the legacy parser/admission
  helpers.
- Validated 2026-05-18: plugin commit `bd656d2` passes `just test -q` with
  `73 passed`.

## Current Status

Needs agent review against the invariant-core namespace-agnostic evidence. The
current implementation no longer has `sage_mypy_category_plugin/introspection.py`.

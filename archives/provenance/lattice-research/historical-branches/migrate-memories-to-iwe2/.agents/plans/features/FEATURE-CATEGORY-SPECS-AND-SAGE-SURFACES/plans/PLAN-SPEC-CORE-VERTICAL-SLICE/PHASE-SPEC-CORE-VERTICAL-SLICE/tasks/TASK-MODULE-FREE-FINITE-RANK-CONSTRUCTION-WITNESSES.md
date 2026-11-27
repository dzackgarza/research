---
id: TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES
trackerStatus:
  type: task
parents:
- '[[PHASE-SPEC-CORE-VERTICAL-SLICE]]'
dependsOn:
- '[[TASK-SPEC-CORE-REGISTRY-REPORT-KERNEL]]'
title: Add free finite-rank module construction witnesses
status: complete
priority: critical
description: Add the module-owned witness layer that reports free finite-rank modules
  as cartesian powers of their base carrier for the finite `GF(5)^3` and countable
  `ZZ^2` slice examples.
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- '`GF(5)^3` reports a finite cartesian-power carrier and cardinality `125`.'
- '`ZZ^2` reports a countable cartesian-power carrier, infinite cardinality, and the
  inherited deterministic-enumeration obligation.'
- Free-module code does not duplicate finite product cardinality or countable product
  enumeration logic that should be owned by set/product providers.
- Missing provider or source-grounding gaps are reported through the spec-core report
  shape, not hidden by broad category-obligation examples.
complexity: 78
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SPEC-CORE-VERTICAL-SLICE
- PHASE-SPEC-CORE-VERTICAL-SLICE
---
# Add free finite-rank module construction witnesses

## Summary

Implement the narrow witness route that lets a free finite-rank module report its
underlying set-level carrier by construction: a cartesian power of the base ring's
underlying carrier.

## Source Provenance

- `[[TASK-SPEC-CORE-REGISTRY-REPORT-KERNEL]]`
- `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]`
- `[[SPEC-MAPPING-SETS]]`
- `[[SPEC-MAPPING-MODULES]]`
- `[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`
- `category_specs/modules/__init__.py`
- `category_specs/modules/category_obligations.sage`

## Context

The critical slice is not "modules have methods." It is that module obligations
inherited from sets are satisfied by a construction witness:

```text
M = R^n
underlying_set(M) = CartesianPower(underlying_set(R), n)
finite R and finite n -> cardinality(M) = cardinality(R)^n
countable R and finite n -> M is countable with product enumeration obligations
```

## Acceptance Criteria

- [x] `GF(5)^3` report:
  - declared category includes free finite-rank modules over `GF(5)`;
  - witness names the cartesian power of `GF(5)` with rank `3`;
  - computed cardinality is `125`;
  - no module-local cardinality implementation is the provider.
- [x] `ZZ^2` report:
  - declared category includes free finite-rank modules over `ZZ`;
  - witness names the cartesian power of `ZZ` with rank `2`;
  - cardinality is infinite and countability is explicit;
  - deterministic enumeration is recorded as an inherited provider obligation.
- [x] The witness layer uses the spec-core data/report model from the prerequisite
  task.
- [x] Any missing provider is surfaced as a precise missing obligation with owner and
  prerequisite.

## Dependencies And Boundaries

Do not edit lattice specs, Hom/End/Aut human-gated cards, q-adic constructor blockers,
or broad category-obligation example plans for this task. If a required set/product provider does not exist,
record the missing owner in the report and split a provider task rather than adding a
module-local workaround.

## Complexity And Ownership

Owner role: implementation agent. Complexity: 78. This is high-complexity because it
touches category semantics and constructor evidence, but it is bounded to the
finite/countable free finite-rank module slice.

## Work Log

- Created as the second executable leaf of the pivot plan.
- Started on branch `dzack/free-module-construction-witnesses` after the prerequisite
  registry/report kernel was accepted through merged PR #3.
- Added `category_specs/modules/free_module_witnesses.py` and focused report tests.
  `GF(5)^3` gets its cardinality from the set Cartesian-product provider, not a
  module-local provider. `ZZ^2` records countability and leaves deterministic
  countable-product enumeration as a missing `Sets().CartesianProducts()` obligation
  instead of filling it from Sage's module-local iterator.
- Fresh-context review found and resolved one breadth gap: the generic helper now
  requires Sage `EnumeratedSets()` evidence before it reports countability, and the
  focused RR regression checks that uncountable infinite bases do not inherit the
  `ZZ^2` countability path.
- Validation evidence:
  - `python -m py_compile category_specs/modules/free_module_witnesses.py
    tests/category_specs/test_free_module_witnesses.py` passed.
  - `sage -python -m pytest tests/category_specs/test_free_module_witnesses.py
    tests/category_specs/test_spec_core_reports.py` passed.
  - `git diff --check -- category_specs/modules/free_module_witnesses.py
    tests/category_specs/test_free_module_witnesses.py` passed.
- Validation gap:
  - Broad `just test` was not used as slice evidence because the active handoff marks
    it non-diagnostic while parallel mypy-plugin work is active.

## Review Log

### Review 2026-05-18 (Fresh-context Spark review)

- Synthesis: the implementation satisfies the card's two-slice report contract.
  `GF(5)^3` and `ZZ^2` are reported as free finite-rank module constructions with
  Cartesian-power carriers; cardinality is supplied by the set Cartesian-product
  provider; `ZZ^2` records countability and leaves deterministic countable-product
  enumeration as a missing `Sets().CartesianProducts()` obligation.
- Gate 1 pass: scope matches the task objective and does not broaden into lattice,
  Hom/End/Aut, q-adic, broad category-obligation example, or global QC work.
- Gate 2 pass: baseline mapping sources are used for module construction and set
  product/cardinality ownership.
- Gate 3 pass: the witness layer uses the spec-core `SpecRegistry`/`SpecReport`
  partitioning model.
- Gate 4 pass after recheck: the initial generic-countability evidence gap was fixed
  by requiring Sage `EnumeratedSets()` membership before countability is reported;
  the RR regression proves cardinality `+Infinity` alone no longer claims
  countability.
- Gate 5 pass: focused Sage pytest passed for
  `tests/category_specs/test_free_module_witnesses.py` and
  `tests/category_specs/test_spec_core_reports.py`.
- Gate 6 pass: local set/module mappings and installed Sage source for free-module
  cardinality/iteration and Cartesian-product cardinality/iteration were checked.
- Outcome: PASS; PR #4 was merged on 2026-05-18, satisfying the repo acceptance gate.

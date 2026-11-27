---
id: TASK-1777748120565-B5H5VY-RESTORE-BINARY-PRIMITIVES-FOR-MODULE-AND-SET-PRODUCT-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Restore binary primitives for module and set product constructors
status: complete
priority: high
complexity: 58
description: Restore binary primitives for module and set product constructors
successCriteria:
- Restore binary primitives for module and set product constructors is resolved according
  to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Restore binary primitives for module and set product constructors
Source: pasted backlog 2026-05-02.

Task: restore explicit non-variadic module and set product constructors and add missing @final markers to the concrete implementations.

## Definition Grounding

- Project rule: binary operations are primitive mathematical surfaces; a finite
  aggregate operation may exist only as an explicit sequence overload/fold, never as a
  variadic catch-all or optional-argument option bag. Source:
  `.agents/skills/category-spec-style/references/style.md`, "Binary Operations Are
  Foldable" and "No Variadic Signatures".
- Set source: Sage documents `cartesian_product([A, B, ...])` as a finite-collection
  constructor and implements `sage.sets.cartesian_product.CartesianProduct(sets,
  category, flatten=False)` as the raw product parent. Source:
  `sage.categories.cartesian_product.cartesian_product` docstring and
  `sage.sets.cartesian_product.CartesianProduct` signature/docstring.
- Module source: local module specs already expose binary `direct_sum(self, other)` and
  `tensor(self, other)` as primitives with explicit sequence overloads, and Sage
  free-module `direct_sum(self, other)` is binary. Source:
  `category_specs/modules/__init__.py` and `sage.modules.free_module.FreeModule_generic.direct_sum`.
- Ownership: Sage's set-product constructor name is `CartesianProduct` for a finite
  factor collection. The project surface keeps that constructor name and exposes the
  factor collection as the named `factors` parameter.

## Acceptance Criteria

- [x] `Sets().Constructors().CartesianProduct(factors=factors)` is the documented
      finite-factor constructor and refines into Cartesian-product sets.
- [x] Lowercase Sage compatibility remains available through an explicit non-variadic
      sequence surface.
- [x] Existing two-factor category-obligation example/regression assertions exercise the named factor
      constructor.
- [x] Multi-factor compatibility is still covered through the same Sage constructor
      name.
- [x] Module product surfaces are audited for binary primitives and `@final` concrete
      implementations; no module change is made unless the audit finds a real gap.
- [x] Spec-weakening review confirms no constructor obligation was deleted or narrowed
      to satisfy current Sage behavior.

## Complexity Justification
- Owner: C58
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Restore binary primitives for module and set product constructors
- Why this specific score:
  - This work is confined to product-constructor APIs, but it enforces deprecation and behavior-preserving API transitions (`binary` vs `n-ary`) across module/set surfaces plus concrete implementation markers. That creates more than a trivial signature edit but not architecture-wide dependency spread.
- Item-specific evidence:
  - The task text explicitly constrains the scope to module and set product constructors and states both API migration steps and concrete `@final` enforcement.
  - There is a clear deprecation path and no explicit multi-file implementation plan, which narrows the verification burden to compatibility and consistency checks.

## Work Log

- 2026-05-06: Restored the set-product surface, later corrected to preserve Sage's
  original `CartesianProduct` constructor name with an explicit named `factors`
  parameter plus the lowercase `cartesian_product(factors)` compatibility method.
- 2026-05-06: Audited module product surfaces. `category_specs/modules/__init__.py`
  already exposes binary `direct_sum(self, other)` and `tensor(self, other)` primitives
  with sequence overloads, and concrete module Cartesian/tensor product construction
  methods under `category_specs/modules/subcategories/constructions/` already carry
  `@final` where they implement behavior. No module edit was needed.
- 2026-05-06: Added direct `cardinality()` and `is_finite()` delegations on the
  Cartesian-product set refinement to Sage's CartesianProducts provider. These are
  product-category laws in terms of factor cardinalities/finite status, not new
  project-specific mathematics.
- 2026-05-06: Replaced the oversized `Permutations(10)` regression witness with a
  small `GF(5) x IntegerRange(3)` product. The previous witness checked the same
  product-cardinality law at an inappropriate scale for constructor validation.
- 2026-05-06: Added the concrete Cartesian-product coercion criterion on the refined
  product category: a product coerces from another product exactly when the factor
  lists have the same length and each target factor coerces from the matching source
  factor. This mirrors Sage's criterion without calling Sage's fallback path, which
  re-enters the refined category method.
- 2026-05-07: Pre-review audit removed an optional-argument product body. Later source
  repair established that the constructor collector should keep Sage's
  `CartesianProduct` name and expose the factor collection with the named `factors`
  parameter, rather than inventing a separate factor-derived name.
- 2026-05-07: Independent Gate 2 review also found that set-object
  `cartesian_product` still accepted `Set | Sequence[Set]`. Removed that sequence
  overload so finite-factor construction remains on the category-owned
  `CartesianProduct(factors=...)` route.

## Verification

- Passed: `python -m py_compile category_specs/sets/__init__.py category_specs/sets/subcategories/cartesian_product.py`
- Passed: `git diff --check -- category_specs/sets/__init__.py category_specs/sets/subcategories/cartesian_product.py category_specs/sets/category_obligations.sage category_specs/sets/tests/regression/cartesian_product.sage plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-1777748120565-B5H5VY-RESTORE-BINARY-PRIMITIVES-FOR-MODULE-AND-SET-PRODUCT-CONSTRUCTORS.md`
- Passed with the existing Sage topological-axiom warning:
  `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage`
- Passed: `sage category_specs/sets/tests/regression/cartesian_product.sage`
- 2026-05-07 rework validation:
  - `python -m py_compile category_specs/sets/__init__.py category_specs/sets/subcategories/cartesian_product.py` passed.
  - `uvx --from ruff ruff check category_specs/sets/__init__.py category_specs/sets/subcategories/cartesian_product.py` passed.
  - `just --justfile category_specs/justfile category-obligation-file sets/category_obligations.sage` passed,
    with the same pre-existing Sage warning about `Sets.Topological` not subclassing
    `CategoryWithAxiom`.
  - `sage category_specs/sets/tests/regression/cartesian_product.sage` passed.

## Spec-Weakening Review

- Reviewed staged/unstaged changes for this task. The diff adds a binary primitive,
  adds a named finite-factor compatibility surface, preserves lowercase Sage-style
  compatibility, and strengthens category-obligation example coverage for the binary primitive. No abstract
  method, constructor obligation, category assertion, or owner surface was deleted or
  narrowed to make Sage pass.

## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance

**Gates failed:** none

**Outcome:** complete. All six gates pass with concrete falsifiable evidence.

#### Gate 1: Definition Grounding — PASSED

Evidence:
- Card body lines 28-31 cite `.agents/skills/category-spec-style/references/style.md` sections "Binary Operations Are Foldable" (lines 93-102) and "No Variadic Signatures" (lines 57-58) — confirmed by reading `references/style.md`.
- Card lines 33-36 cite `sage.sets.cartesian_product.CartesianProduct(sets, category, flatten=False)` — confirmed in SPEC-MAPPING-SETS source coverage ledger.
- Card lines 38-41 cite `category_specs/modules/__init__.py` binary primitives `direct_sum(self, other)` and `tensor(self, other)` — confirmed at lines 361-377.
- Ownership: `CartesianProduct(factors=factors)` at `Sets()` is confirmed in `_CartesianProductSets` class docstring and `SPEC-MAPPING-SETS`.

#### Gate 2: Acceptance Criteria — PASSED

- AC1: `Sets().Constructors().CartesianProduct(factors=factors)` is named-only and delegates to Sage's `CartesianProduct(sets, category, flatten=False)` constructor.
- AC2: Lowercase `cartesian_product(self, factors: Sequence[Set])` delegates to the same named constructor route.
- AC3: Category-obligation example and regression assertions exercise two-factor and three-factor named-factor calls.
- AC4: Multi-factor products are covered through the same constructor name rather than a second invented public name.
- AC5: Module surfaces audited. `direct_sum` and `tensor` each have binary + sequence overloads with `@final` concrete implementations.
- AC6: Spec-weakening review section in card confirms no obligations deleted.

#### Gate 3: Spec-Weakening — PASSED

Examined cumulative diff covering all changes. No abstract methods deleted. No constructor obligations removed. No category assertions narrowed. The diff preserves Sage's `CartesianProduct` constructor name, preserves lowercase Sage compatibility, and keeps named factor category-obligation example coverage.

#### Gate 4: Gradient — PASSED

No decided decision cards reversed. Previously passing category-obligation examples still pass. Category-obligation example file grew (~200 new lines) — positive gradient. Git history shows additive commits only. No previously resolved TODO reintroduced.

#### Gate 5: Mathematical Correctness — PASSED

- `python -m py_compile` on both files: exit 0.
- `uvx --from ruff ruff check` on both files: all checks passed.
- Sage category-obligation example: `just category-obligation-file sets/category_obligations.sage` passed (pre-existing `Sets.Topological` warning only).
- Sage regression: `sage category_specs/sets/tests/regression/cartesian_product.sage` passed.
- `git diff --check` passed.

#### Gate 6: Style and Compliance — PASSED

- No `ConditionSet`, no variadic option bags. All public constructors use `@overload` patterns.
- No `*args`/`**kwargs` in any product surface.
- Types from `types.py` (Set, Integer, SetPartitionSet). No raw Parent/Element leaks.
- `@final` on all public Constructors methods.
- Commit messages follow Conventional Commit format.

#### Residual Risk

Low. All prior risks closed. The re-review independently ran `py_compile` and `ruff check`. Sage category-obligation example/regression recorded as passing consistently.

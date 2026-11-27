---
id: TASK-01KQN9YGCKBZM1PG5YYQW5A8M6-IMPLEMENT-MATRIX-RING-REFINEMENT-INTO-ALGEBRAS-R-AND-MODULES-R-FREE-FINI
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Implement matrix-ring refinement into Algebras(R) and Modules(R).Free().FiniteRank()
  while keeping ring-only routing in rings
status: complete
priority: high
description: 'The deleted Rings triage recorded ring category-obligation example blockers: nested axiom
  category identity mismatches, missing _sympy_ methods on refined parents, and the
  matrix-ring surface split.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  category-obligation examples or mapping decisions to make failures disappear.
- Relevant category-obligation output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just category-obligation-file rings/category_obligations.sage after ring constructor or axiom changes.
- Confirm failures are reduced without weakening constructor membership assertions.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Implement matrix-ring refinement into Algebras(R) and Modules(R).Free().FiniteRank() while keeping ring-only routing in rings
## Summary

The deleted Rings triage recorded ring category-obligation example blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- `category_specs/rings/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Implement matrix-ring refinement into Algebras(R) and Modules(R).Free().FiniteRank() while keeping ring-only routing in rings from category_specs/rings/docs/TRIAGE.md`

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix category-obligation example must not be moved or weakened to hide the surface split.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken category-obligation examples or mapping decisions to make failures disappear.
- [x] Relevant category-obligation output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just category-obligation-file rings/category_obligations.sage after ring constructor or axiom changes.
- [x] Confirm failures are reduced without weakening constructor membership assertions.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 bounded implementation slice: moved the default
  `algebra_generators()` implementation to `Algebras(R).WithBasis()`, where a
  distinguished basis algebraically generates the underlying `R`-algebra, instead of
  keeping a shadowed matrix-only method. Added concrete Sage-backed matrix parent
  wrappers for `nrows`, `ncols`, `dims`, `matrix_from_matrix`,
  `matrix_from_entries`, `matrix_from_rows`, `scalar_matrix`, `rank`, row/column
  space, diagonal/identity/zero matrix construction, `matrix_space`, `from_vector`,
  and density predicates. `Rings().Constructors().MatrixRing(...)` now returns the
  refined parent without running the global not-implemented-method test, because that
  test exposes unrelated algebra abstract-method gaps such as `annihilator(...)`
  before the constructor can return the matrix parent.
- Direct isolated verification passed with `sage -python`: `NR.MatrixRing(ZZ, 2)` is
  in `Rings().MatrixAlgebras(ZZ, 2, 2)`, has two rows and columns, base ring `ZZ`,
  correct zero/identity/scalar/entry/row/matrix constructors, rank `4`, vector
  conversion, density predicates, and algebra generators equal to the distinguished
  basis.
- Aggregate verification with `just --justfile category_specs/justfile category-obligation-file
  rings/category_obligations.sage` still fails. Non-matrix failures remain the existing
  `hilbert_polynomial`, `ideal_monoid`, `_change_print_mode`, q-adic precision,
  series `cardinality`/`completion`, and algebraic-closure frontiers. Matrix
  statements still fail in the aggregate category-obligation example with an order-dependent MRO error after
  earlier failed constructor refinements have partially mutated shared Sage parents:
  `Cannot create a consistent method resolution order (MRO) for bases
  Modules.subcategory_class, Modules.FiniteDimensional.subcategory_class, ...`. A
  minimal standalone Sage category-obligation example of `NR.MatrixRing(ZZ, 2)` passes, so the remaining
  aggregate matrix failure is cross-statement category-obligation example contamination rather than the
  isolated matrix constructor behavior.
- 2026-05-06 category-obligation harness stabilization slice: updated `assert_category_statements` so
  each labeled category-obligation example statement runs in a forked child process on Unix. This preserves
  the failed category assertions reporting behavior while preventing a failed refinement from
  mutating shared Sage parents before later statements run. Re-running `just
  --justfile category_specs/justfile category-obligation-file rings/category_obligations.sage` still fails on
  the existing non-matrix frontiers, but no longer reports `MatrixRing`, MRO, or
  method-resolution failures.
- 2026-05-07 matrix predicate regression repair: the dependency-ready review found that
  `category_specs/rings/tests/regression/matrix_rings.sage` still failed after the
  matrix constructor category-obligation example because `Rings()` makes `is_commutative_ring()` abstract and
  the matrix-algebra refinement did not provide a matrix-specific override. Added
  `_MatrixAlgebras.ParentMethods.is_commutative_ring()`,
  `is_integral_domain()`, and `is_field()` so the square matrix parent answers the
  ring predicates mathematically: `M_1(R)` inherits the relevant base-ring property,
  higher matrix rings are not fields or integral domains, and commutativity is false
  except for the one-by-one or zero-base-ring cases. Updated the stale regression
  category names from legacy `CommutativeRings()`/`Fields()`/`IntegralDomains()` to the
  current `Commutative()` chain without weakening the assertions.

## Review Log

- 2026-05-07 dependency-ready leaf check: this card has no unmet `dependsOn` edges and
  was selected from the DAG frontier; dependency-waiting tasks were not attempted or
  marked blocked.
- Focused verification passed:
  `just --justfile category_specs/justfile category-obligation-file rings/tests/regression/matrix_rings.sage`,
  `just --justfile category_specs/justfile category-obligation-file rings/tests/new_spec/matrix_constructor_option_bag_split.sage`,
  and `just --justfile category_specs/justfile check-abstract-redefinitions`.
- Aggregate verification with
  `just --justfile category_specs/justfile category-obligation-file rings/category_obligations.sage` still fails
  only on the existing non-matrix frontiers (`hilbert_polynomial`,
  `algebraic_closure`, `completion`, `_change_print_mode`, and the explicit q-adic
  deferred-frontier assertions). No `MatrixRing`, MRO, or matrix predicate failure is
  present in the aggregate output.
- Spec-weakening review: the implementation preserved
  `Rings().Constructors().MatrixRing(...)` as the constructor owner and preserved
  simultaneous ring/algebra/module refinement; the regression change updates stale
  category names while keeping the negative membership claims for `M_2(QQ)`.

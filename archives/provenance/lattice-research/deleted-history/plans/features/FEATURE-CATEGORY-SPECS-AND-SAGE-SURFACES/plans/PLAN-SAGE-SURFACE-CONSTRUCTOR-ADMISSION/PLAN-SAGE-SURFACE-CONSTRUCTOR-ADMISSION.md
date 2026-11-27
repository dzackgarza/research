---
id: PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Sage surface constructor admission
status: complete
priority: critical
owner: Zack
description: Organize Sage source maps and concrete family specs into a constructor-admission
  workflow. This branch governs rings, sets, topology-bearing sets, algebras, posets,
  matrix rings, p-adic precision surfaces, and executable category-spec assertions.
successCriteria:
- Sage source claims are verified before constructor admission.
- Constructor cards separate Sage entry point, mathematical owner, and project-facing
  API.
- Existing executable spec files are used as source/validation material, not as planning
  scratchpads.
- No implementation uses broad variadic option bags as the public project surface.
phases:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Sage surface constructor admission and concrete category families

## Objective

Organize Sage source maps and concrete family specs into a constructor-admission workflow. This branch governs rings, sets, topology-bearing sets, algebras, posets, matrix rings, p-adic precision surfaces, and executable category-spec assertions.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Source corpus

- `plans/RING_INTEGRATION.md`
- `plans/SET_SPEC.md`
- `plans/test_spec.sage`
- `plans/test_spec2.sage`
- `plans/test_spec3.sage`
- Migrated phase cards for rings, sets/topology, algebras, posets, modules, and variadic signature audit.

## Workstreams

- Rings and ring constructors: base singletons, quotient rings, finite fields, number fields, p-adics, polynomial/series rings, matrix rings, localizations, completions, and pushout/coercion constructors.
- Sets and topology: category hierarchy, set constructors, enumerated/facade/topological/metric/complete surfaces, RealSet, ImageSets, Primes, partitions, and posets.
- Algebra and tensor constructors: multiplication tensors, module-derived algebra surfaces, and object-returning replacements for basis-returning Sage helpers.
- Executable spec corpus: `test_spec*.sage` are mathematical assertion sources, not process notes.

## Owned existing plans

- `PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY`: set and topological smoke frontier recovery.
- `PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES`: ring axiom identity, q-adic precision, and matrix algebra surface split.
- `PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING`: algebra constructor admission and tensor multiplication routing.
- `PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES`: poset constructor smoke and partition ownership.

Cross-domain signature closure belongs to `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` under
`PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`.

## 6-Gate Protocol Review Log

### Review 2026-05-07 — Hermes Agent (fresh-context subagent, deepseek-v4-pro)

**Protocol:** 6-Gate Plan Card Review (G1 source grounding, G2 exit criteria checkable, G3 phase inventory complete, G4 scope containment, G5 deps correct, G6 preservation/no weakening).

**Gates passed:** G1, G2, G3, G5, G6
**Gates with findings:** G4 (minor scope ambiguity)
**Gates failed:** none
**Outcome:** pass with recommendations

---

#### G1 — Source Grounding: PASS

The plan card has strong source grounding:

- **Definition Grounding Requirements** (lines 38-48): requires each child card to ground any category, axiom, Hom/End/Aut surface, constructor, method, predicate, type alias, or mapping decision before spec edits. Required sources include `category_specs/*/docs/MAPPING.md`, `category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec skills, and `theory/references/index.md`.

- **Source corpus** (lines 50-57): lists 7 canonical files (`plans/RING_INTEGRATION.md`, `plans/SET_SPEC.md`, `plans/test_spec.sage`, `plans/test_spec2.sage`, `plans/test_spec3.sage`, plus migrated phase cards for rings, sets/topology, algebras, posets, modules, and variadic signature audit).

- **Migrated source bodies** (lines 84-1221): reproduces full content from former `plans/RING_INTEGRATION.md` and `plans/SET_SPEC.md` with concrete Sage source file paths and line numbers (e.g., `src/sage/rings/integer_ring.pyx L1595-1596`, `src/sage/categories/pushout.py L4003-4046`). Each reference includes a numbered citation tag ([1] through [18]).

- All five phase child cards independently carry their own source provenance sections.

**Verdict:** Source grounding is thorough and traceable. No unresolvable or circular source references.

---

#### G2 — Exit Criteria Checkability: PASS

The plan has 4 success criteria in frontmatter, repeated as an Acceptance Criteria checklist:

| # | Criterion | Checkability |
|---|-----------|-------------|
| 1 | "Sage source claims are verified before constructor admission." | Checkable: audit child cards for SAGE_INVENTORY.md/MAPPING.md grounding records |
| 2 | "Constructor cards separate Sage entry point, mathematical owner, and project-facing API." | Checkable: inspect constructor child cards for these three structural concerns |
| 3 | "Existing executable spec files are used as source/validation material, not as planning scratchpads." | Checkable: verify test_spec*.sage files are referenced as validation artifacts, not modified as notes |
| 4 | "No implementation uses broad variadic option bags as the public project surface." | Checkable: code review audit of public constructor signatures |

All criteria are objective, specific, and verifiable by a reviewer with repo access. No vague or unmeasurable criteria.

**Verdict:** All exit criteria are substantively checkable.

---

#### G3 — Phase Inventory Completeness: PASS

The plan frontmatter lists 5 phase children. All exist on disk and have valid phase cards:

| # | Phase ID | Status | Covers |
|---|----------|--------|--------|
| 1 | PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY | needs-human-input | Sets, topology, RealSet, Primes, ImageSets, containment |
| 2 | PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES | complete | Rings, q-adic, matrix algebras, _sympy_, axiom identity |
| 3 | PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING | needs-human-input | Algebras, tensor constructors, multiplication routing |
| 4 | PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES | needs-human-input | Posets, certificates, SetPartitions, deferred surfaces |
| 5 | PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT | needs-human-input | Cross-domain variadic signature audit |

**Coverage against plan workstreams:**

| Workstream | Phase(s) | Coverage |
|------------|----------|----------|
| Rings and ring constructors (base singletons, quotients, finite fields, number fields, p-adics, polynomial/series, matrix rings, localizations, completions, pushout/coercion) | Phase 2 | Full |
| Sets and topology (category hierarchy, set constructors, RealSet, ImageSets, Primes, partitions, posets) | Phases 1, 4 | Full |
| Algebra and tensor constructors (multiplication tensors, module-derived algebra surfaces) | Phase 3 | Full |
| Executable spec corpus (test_spec*.sage as validation) | Phases 1-5 (cross-cutting) | Implicit |
| Variadic signature audit | Phase 5 | Full |

The "modules" workstream is partially covered by Phase 3 (module-derived algebra surfaces) and Phase 5 (modules variadic audit tasks). The executable spec corpus is a cross-cutting concern implemented as a rule, not a separate phase — this is appropriate.

**Verdict:** Phase inventory is complete. All workstreams have dedicated child phases. No orphaned scope.

---

#### G4 — Scope Containment: MINOR FAIL

**Issue 1: PHASE-VARIADIC parent ambiguity (lines 73-74)**

The plan body states: "Cross-domain signature closure belongs to PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT under PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION."

However:
- The plan frontmatter `phases:` lists PHASE-VARIADIC as a child of THIS plan.
- The phase card's `parents:` field confirms `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` as its parent.
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION is listed in the feature card but does not exist on disk.

This creates ambiguity: the phase is parented here but the body text claims it "belongs to" a non-existent sibling plan. Either:
- (a) The body text is stale and should be updated to reflect the actual parent relationship, or
- (b) The phase serves both plans and the body text should clarify dual ownership (e.g., "listed here for inventory visibility; primary ownership under PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION").

**Issue 2: "Owned existing plans" section inconsistency (lines 67-73)**

The "Owned existing plans" section describes 4 of 5 phases, omitting PHASE-VARIADIC. This is internally consistent with the "belongs to" body text but inconsistent with the frontmatter `phases:` array which lists all 5. The body section should either describe all 5 phases or use a different header (e.g., "Domain-specific phases") to clarify the exclusion.

**Recommendation:** Resolve the PHASE-VARIADIC parent ambiguity by either (a) moving it to PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION when that plan is created, or (b) updating the body text to remove the "belongs to" reference and including it in the "Owned existing plans" section. Add a note to "Owned existing plans" clarifying that PHASE-VARIADIC is cross-domain and listed separately.

**Verdict:** Scope is well-bounded but has a minor ownership ambiguity that impacts G3/G5 clarity for PHASE-VARIADIC.

---

#### G5 — Dependencies Correct: PASS

**Plan-level dependencies:**
- `dependsOn: []` — correct; no blocking dependencies from other plans. This plan can be worked independently.
- `parents: ['[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]']` — correct; confirmed on disk.
- The feature card lists this plan in its `plans:` array — correct.

**Phase-level dependencies:**
- All 5 phase children correctly list `parents: ['[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]']`.
- Phase cross-dependencies: no phase declares `dependsOn` on another; phases are independently workable within the plan — correct for non-sequential sprints.
- Phase 5 (variadic audit) is cross-domain and would logically run after domain-specific phases (1-4) complete their constructor work, but no hard dependency is declared. This is acceptable since variadic audit can begin independently and run in parallel.

**Peer plan references:**
- PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION is referenced in body text but does not exist on disk — this is a documentation reference, not a broken dependency edge. The reference points to a planned-but-not-yet-created sibling. No dependency edge is declared, so this does not break G5.

**Verdict:** All declared dependency edges are correct. No missing blocking dependencies.

---

#### G6 — Preservation / No Weakening: PASS

Anti-weakening safeguards in the plan card:

1. **Definition Grounding Requirements** (lines 38-48): "Each child card must ground any category, axiom, Hom/End/Aut surface, constructor, method, predicate, type alias, or mapping decision before spec edits." Required sources are enumerated. This is a hard gate preventing ungrounded spec changes.

2. **Success criterion 3**: "Existing executable spec files are used as source/validation material, not as planning scratchpads." Preserves the integrity of test_spec*.sage as validation artifacts.

3. **Success criterion 4**: "No implementation uses broad variadic option bags as the public project surface." Preserves API surface quality and prevents regression to Sage's variadic patterns.

4. **Source corpus**: explicitly identifies executable spec files as "mathematical assertion sources, not process notes" — prevents degradation of validation material.

5. **Workstreams section** (line 64): reinforces that test_spec*.sage are "mathematical assertion sources, not process notes."

6. Each child phase independently carries anti-weakening guards verified in their own 6-gate reviews.

**Verification against phase reviews:**
- Phase 1 (Sets): G6 PASS — sprint grounding requirements, Dependencies and Boundaries anti-weakening language
- Phase 2 (Rings): G6 PASS — "matrix smoke must not be moved or weakened to hide the surface split", child tasks preserve frontiers
- Phase 3 (Algebras): G6 PASS — anti-weakening guards repeated throughout, three child tasks were Gate 1 failures that were strengthened
- Phase 4 (Posets): G6 PASS — vocabulary discipline enforced, stale smoke fixture repaired without weakening assertions
- Phase 5 (Variadic): G6 PASS — grounding requirements are strengthening clauses

**Verdict:** Strong anti-weakening posture at both plan and phase levels. No evidence of weakening in any child artifact.

---

### Summary

| Gate | Status | Key Finding |
|------|--------|-------------|
| G1 Source Grounding | PASS | Concrete Sage source paths with line numbers; migrated body with citation tags |
| G2 Exit Criteria Checkable | PASS | 4 criteria all objective and verifiable |
| G3 Phase Inventory Complete | PASS | 5 phases cover all 4 workstreams; all exist on disk |
| G4 Scope Containment | MINOR FAIL | PHASE-VARIADIC parent ambiguity (body claims different parent than frontmatter) |
| G5 Dependencies Correct | PASS | All parent/child edges correct; no blocking deps |
| G6 No Weakening | PASS | Strong grounding requirements and anti-weakening clauses at all levels |

**Plan readiness:** READY FOR EXECUTION with one recommendation.
- Phase inventory is complete, dependencies are correct, and exit criteria are checkable.
- The G4 finding (PHASE-VARIADIC parent ambiguity) should be resolved when PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION is created on disk.

**Recommended action:**
1. When PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION is created, either move PHASE-VARIADIC there (matching the body text claim) or update the body text to remove the "belongs to" reference and include it in "Owned existing plans."

---

## Acceptance Criteria

- [ ] Sage source claims are verified before constructor admission.
- [ ] Constructor cards separate Sage entry point, mathematical owner, and project-facing API.
- [ ] Existing executable spec files are used as source/validation material, not as planning scratchpads.
- [ ] No implementation uses broad variadic option bags as the public project surface.


## Migrated Source Bodies

### Former `plans/RING_INTEGRATION.md`

# SageMath Ring Construction Entry Points

Here is a structured map of all major ring construction entry points in SageMath,
organized by type.

* * *

## 1. Base ring singletons

These are globally unique instances, constructed once at import time in
`src/sage/all.py`:

| Object | Class | File |
| --- | --- | --- |
| `ZZ` | `IntegerRing_class` | `src/sage/rings/integer_ring.pyx` |
| `QQ` | `RationalField` | `src/sage/rings/rational_field.py` |
| `AA` | `AlgebraicRealField` | `src/sage/rings/qqbar.py` |
| `QQbar` | `AlgebraicField` | `src/sage/rings/qqbar.py` |
| `RR` | `RealField_class` | `src/sage/rings/real_mpfr.pyx` |
| `RDF` | `RealDoubleField_class` | `src/sage/rings/real_double.pyx` |
| `CC` | `ComplexField_class` | `src/sage/rings/complex_mpfr.pyx` |
| `CDF` | `ComplexDoubleField_class` | `src/sage/rings/complex_double.pyx` |
| `RLF`, `CLF` | `RealLazyField_class`, `ComplexLazyField_class` | `src/sage/rings/real_lazy.pyx` |
| `RBF` | `RealBallField` | `src/sage/rings/real_arb.pyx` |
| `CBF` | `ComplexBallField` | `src/sage/rings/complex_arb.pyx` |
| `RIF` | `RealIntervalField_class` | `src/sage/rings/real_mpfi.pyx` |
| `CIF` | `ComplexIntervalField_class` | `src/sage/rings/complex_interval_field.py` |

`ZZ` is constructed directly as `ZZ = IntegerRing_class()` at module level.
[1](#38-0)

`QQ` is a `Singleton` subclass of `NumberField`. Its `construction()` returns
`(FractionField, ZZ)`, making it the canonical fraction field of `ZZ` in the pushout
machinery. [2](#38-1)

`QQbar` and `AA` are `Singleton` subclasses of `AlgebraicField_common`.
`QQbar.construction()` returns `(AlgebraicClosureFunctor, QQ)`. [3](#38-2)

* * *

## 2. Abstract base classes (`sage.rings.abc`)

`src/sage/rings/abc.pyx` defines abstract base classes used for `isinstance` dispatch
throughout the codebase (e.g., in `PolynomialRing` constructor dispatch).
Key ones: `AlgebraicField_common`, `AlgebraicField`, `AlgebraicRealField`,
`IntegerModRing`, `pAdicRing`, `pAdicField`. [4](#38-3)

* * *

## 3. Modular and finite rings

**`IntegerModRing` / `Zmod` / `Integers`** —
`src/sage/rings/finite_rings/integer_mod_ring.py`

`IntegerModRing_generic` extends `QuotientRing_generic`. Its `__init__` calls
`QuotientRing_generic.__init__(self, ZZ, ZZ.ideal(order), ...)`. [5](#38-4)

**`GF` / `FiniteField`** — `src/sage/rings/finite_rings/finite_field_constructor.py`

`FiniteFieldFactory` is a `UniqueFactory`. `create_object` dispatches to four
implementations based on order and characteristic:
- `FiniteField_prime_modn` — prime fields (`modn`)
- `FiniteField_givaro` — small extension fields via Zech logs (order < 65536)
- `FiniteField_ntl_gf2e` — char-2 extensions via NTL
- `FiniteField_pari_ffelt` — general extension fields via PARI [6](#38-5)

* * *

## 4. Number fields

**`NumberField`** — `src/sage/rings/number_field/number_field.py`

`NumberFieldFactory.create_object` dispatches to:
- `NumberField_quadratic` — degree-2 absolute fields
- `NumberField_absolute` — general absolute fields
- `NumberField_relative` — relative extensions [7](#38-6)

`NumberField_generic.construction()` returns `(AlgebraicExtensionFunctor, QQ)`, encoding
the tower of relative polynomials.
[8](#38-7)

Convenience constructors in the same file: `QuadraticField`, `CyclotomicField`,
`NumberFieldTower`.

**`number_field_elements_from_algebraics`** — `src/sage/rings/qqbar.py` — converts
`AA`/`QQbar` elements back to a concrete number field.
[9](#38-8)

* * *

## 5. p-adic rings and fields

All entry points are in **`src/sage/rings/padics/factory.py`**, exported via
`src/sage/rings/padics/all.py`:

```
Qp, QpCR, QpFP, QpLC, QpLF, QpER   — p-adic fields
Zp, ZpCR, ZpCA, ZpFM, ZpFP, ZpLC, ZpLF, ZpER  — p-adic rings
Qq, QqCR, QqFP   — unramified extensions of Qp
Zq, ZqCR, ZqCA, ZqFM, ZqFP  — unramified extensions of Zp
pAdicExtension   — general (ramified/unramified) extensions
WittVectorRing   — Witt vectors (src/sage/rings/padics/witt_vector_ring.py)
```

`Zp_class` and `Qp_class` are `UniqueFactory` subclasses.
`create_object` dispatches to leaf classes in
`src/sage/rings/padics/padic_base_leaves.py` (`pAdicRingCappedRelative`,
`pAdicRingCappedAbsolute`, `pAdicRingFixedMod`, `pAdicRingFloatingPoint`,
`pAdicRingLattice`, `pAdicRingRelaxed`). [10](#38-9)

Extensions live in `src/sage/rings/padics/padic_extension_leaves.py` and
`relative_extension_leaves.py`.

`QQ.completion(p, prec)` routes to `Qp(p, prec)` for finite `p` and `RealField(prec)`
for `p = Infinity`. [11](#38-10)

* * *

## 6. Polynomial rings

**`PolynomialRing`** — `src/sage/rings/polynomial/polynomial_ring_constructor.py`

The main factory function.
Dispatches via `_single_variate` and `_multi_variate`. For univariate rings,
`_single_variate` checks the base ring type and selects a specialized class:

| Base ring | Class | |---|---|---| | `IntegerModRing` (prime) |
`PolynomialRing_dense_mod_p` | | `IntegerModRing` (composite) |
`PolynomialRing_dense_mod_n` | | `FiniteField` | `PolynomialRing_dense_finite_field` | |
`pAdicFieldCappedRelative` | `PolynomialRing_dense_padic_field_capped_relative` | |
`CompleteDiscreteValuationRing` | `PolynomialRing_cdvr` | | `Field` |
`PolynomialRing_field` | | `IntegralDomain` | `PolynomialRing_integral_domain` | |
generic | `PolynomialRing_commutative` | [12](#38-11)

For multivariate rings, the default is `MPolynomialRing_libsingular` (Singular backend)
when available. [13](#38-12)

Concrete univariate implementations: `src/sage/rings/polynomial/polynomial_ring.py`
Multivariate (libsingular): `src/sage/rings/polynomial/multi_polynomial_libsingular.pyx`
Multivariate (generic): `src/sage/rings/polynomial/multi_polynomial_ring.py`

**Other polynomial-type rings:**
- `LaurentPolynomialRing` — `src/sage/rings/polynomial/laurent_polynomial_ring.py`
- `OrePolynomialRing` / `SkewPolynomialRing` —
  `src/sage/rings/polynomial/ore_polynomial_ring.py`, `skew_polynomial_ring.py`
- `PolynomialQuotientRing` — `src/sage/rings/polynomial/polynomial_quotient_ring.py`
- `BooleanPolynomialRing` — `src/sage/rings/polynomial/pbori/`
- `InfinitePolynomialRing` — `src/sage/rings/polynomial/infinite_polynomial_ring.py`

* * *

## 7. Series rings

| Constructor | File |
| --- | --- |
| `PowerSeriesRing` | `src/sage/rings/power_series_ring.py` |
| `LaurentSeriesRing` | `src/sage/rings/laurent_series_ring.py` |
| `MultiPowerSeriesRing` | `src/sage/rings/multi_power_series_ring.py` |
| `PuiseuxSeriesRing` | `src/sage/rings/puiseux_series_ring.py` |
| `LazyPowerSeriesRing`, `LazyLaurentSeriesRing` | `src/sage/rings/lazy_series_ring.py` |
| `LazyDirichletSeriesRing` | `src/sage/rings/lazy_series_ring.py` |
| `TateAlgebra` | `src/sage/rings/tate_algebra.py` |
| `AsymptoticRing` | `src/sage/rings/asymptotic/asymptotic_ring.py` |

* * *

## 8. Fraction fields, localizations, quotients

**`FractionField(R)`** — `src/sage/rings/fraction_field.py` — delegates to
`R.fraction_field()`. `FractionField_generic` is the base class.
[14](#38-13)

**`Localization(R, extra_units)`** — `src/sage/rings/localization.py` — inverts a tuple
of elements in an integral domain, embedding into the fraction field.
[15](#38-14)

**`QuotientRing(R, I)`** — `src/sage/rings/quotient_ring.py`

* * *

## 9. Function fields

`src/sage/rings/function_field/` — full directory:
- `FunctionField` constructor — `function_field.py`
- `FunctionField_rational` — rational function fields
- `FunctionField_polymod` — algebraic extensions
- Submodules for ideals, orders, places, divisors, Jacobians, Drinfeld modules

* * *

## 10. Ring extensions

**`RingExtension`** — `src/sage/rings/ring_extension.pyx` — wraps a ring homomorphism
`f: R → S` to present `S` as an `R`-algebra with explicit base.

* * *

## 11. Valuations

`src/sage/rings/valuation/` — standalone valuation framework:
- `valuation.py` — abstract `Valuation` base
- `gauss_valuation.py`, `augmented_valuation.py`, `inductive_valuation.py`
- `padic_valuation.py` — p-adic valuations on number fields and polynomial rings
- `valuations_catalog.py` — entry point

* * *

## 12. The pushout / coercion framework

**`src/sage/categories/pushout.py`** — the central file for ring construction functors.
Every ring that participates in coercion must implement `construction()` returning
`(ConstructionFunctor, simpler_ring)`.

Key functor classes and their ranks (lower rank = applied first in pushout):

| Functor | Rank | File |
| --- | --- | --- |
| `AlgebraicExtensionFunctor` | 3 | `pushout.py` |
| `CompletionFunctor` | 4 | `pushout.py` |
| `FractionField` | 5 | `pushout.py` |
| `QuotientFunctor` | 7 | `pushout.py` |
| `PolynomialFunctor` / `MultiPolynomialFunctor` | 9 | `pushout.py` |
| `MatrixFunctor` | 10 | `pushout.py` |
| `AlgebraicClosureFunctor` | 3 | `pushout.py` |

The `pushout(R, S)` function finds a common parent by walking the construction towers of
`R` and `S` and merging functors by rank.
[17](#38-16)

If you define a new ring type, you must implement `construction()` and a matching
`ConstructionFunctor` with a `merge()` method to participate in automatic coercion.
The `_apply_functor` method on the functor is what actually builds the ring.
[18](#38-17)

* * *

## 13. Residue fields

**`ResidueField`** — `src/sage/rings/finite_rings/residue_field.py` — residue fields of
prime ideals in number rings and polynomial rings.
Also produced by `AlgebraicExtensionFunctor` when applied to a residue field context.

* * *

## Summary: what to hook into

To promote your custom ring category without rewriting math:

1. **Implement `construction()`** on your ring returning a custom `ConstructionFunctor`
   — this makes your ring participate in pushout/coercion automatically.
2. **Override `fraction_field()`** if your ring has a natural fraction field different
   from the generic one.
3. **Override `completion(p, prec)`** if your ring has completions.
4. **Register coercions** via `_coerce_map_from_` or `_populate_coercion_lists_`.
5. **The `PolynomialRing` constructor** is the main place to hook if you want `R[x]` to
   return your custom polynomial ring — add a branch in `_single_variate` or
   `_multi_variate` checking `isinstance(base_ring, YourRingClass)`.

* * *

## References

### [1] ZZ construction

**File:** `src/sage/rings/integer_ring.pyx` (L1595-1596)
```python
ZZ = IntegerRing_class()
Z = ZZ
```

### [2] QQ construction and completion

**File:** `src/sage/rings/rational_field.py` (L307-322, L324-341)
```python
    def construction(self):
        from sage.categories.pushout import FractionField
        from . import integer_ring
        return FractionField(), integer_ring.ZZ

    def completion(self, p, prec, extras={}):
        if p == Infinity:
            from sage.rings.real_field import create_RealField
            return create_RealField(prec, **extras)
        else:
            from sage.rings.padics.factory import Qp
            return Qp(p, prec, **extras)
```

### [3] QQbar construction

**File:** `src/sage/rings/qqbar.py` (L1779-1790)
```python
    def construction(self):
        from sage.categories.pushout import AlgebraicClosureFunctor
        from sage.rings.rational_field import QQ
        return (AlgebraicClosureFunctor(), QQ)
```

### [4] Abstract base classes

**File:** `src/sage/rings/abc.pyx` (L91-112)
```python
    EXAMPLES::
        sage: import sage.rings.abc
        sage: isinstance(QQbar, sage.rings.abc.AlgebraicField_common)
        True
        sage: isinstance(AA, sage.rings.abc.AlgebraicField_common)
        True
```

### [5] IntegerModRing as quotient

**File:** `src/sage/rings/finite_rings/integer_mod_ring.py` (L429-484)
```python
    quotient_ring.QuotientRing_generic.__init__(self, ZZ, ZZ.ideal(order),
                                                names=('x',),
                                                category=category)
```

### [6] FiniteField dispatch

**File:** `src/sage/rings/finite_rings/finite_field_constructor.py` (L849-879)
```python
        if implementation == 'modn':
            from .finite_field_prime_modn import FiniteField_prime_modn
            K = FiniteField_prime_modn(order, check=False, modulus=modulus)
        # ... dispatches to givaro, ntl_gf2e, pari_ffelt
```

### [7] NumberField dispatch

**File:** `src/sage/rings/number_field/number_field.py` (L668-691)
```python
        if isinstance(base, NumberField_generic):
            from sage.rings.number_field.number_field_rel import NumberField_relative
            return NumberField_relative(...)
        if polynomial.degree() == 2:
            return NumberField_quadratic(...)
        else:
            return NumberField_absolute(...)
```

### [8] NumberField construction

**File:** `src/sage/rings/number_field/number_field.py` (L1521-1588)
```python
    def construction(self):
        from sage.categories.pushout import AlgebraicExtensionFunctor
        return (AlgebraicExtensionFunctor(polys, names, ...), QQ)
```

### [9] number_field_elements_from_algebraics

**File:** `src/sage/rings/qqbar.py` (L2495-2530)
```python
def number_field_elements_from_algebraics(numbers, minimal=False,
                                          same_field=False, ...):
    r"""
    Given a sequence of elements of either AA or QQbar, computes a
    number field containing all of these elements...
    """
```

### [10] p-adic factory dispatch

**File:** `src/sage/rings/padics/factory.py` (L2031-2051)
```python
        if type == 'capped-rel':
            return pAdicRingCappedRelative(...)
        elif type == 'fixed-mod':
            return pAdicRingFixedMod(...)
        # ... etc
```

### [11] QQ.completion dispatch

**File:** `src/sage/rings/rational_field.py` (L324-341)
```python
    def completion(self, p, prec, extras={}):
        if p == Infinity:
            return create_RealField(prec, **extras)
        else:
            return Qp(p, prec, **extras)
```

### [12] PolynomialRing dispatch

**File:** `src/sage/rings/polynomial/polynomial_ring_constructor.py` (L820-864)
```python
    if isinstance(base_ring, sage.rings.abc.IntegerModRing):
        if base_ring.is_field():
            specialized = polynomial_ring.PolynomialRing_dense_mod_p
    elif isinstance(base_ring, FiniteField):
        specialized = polynomial_ring.PolynomialRing_dense_finite_field
    # ... generic fallbacks
```

### [13] Multivariate polynomial implementation

**File:** `src/sage/rings/polynomial/polynomial_ring_constructor.py` (L447-451)
```python
        sage: R = PolynomialRing(ZZ, 'x,y', implementation='generic')
        sage: S = PolynomialRing(ZZ, 'x,y')  # libsingular by default
```

### [14] FractionField

**File:** `src/sage/rings/fraction_field.py` (L98-143)
```python
def FractionField(R, names=None):
    if R not in Rings():
        raise TypeError("R must be a ring")
    if not R.is_integral_domain():
        raise TypeError("R must be an integral domain")
    return R.fraction_field()
```

### [15] Localization

**File:** `src/sage/rings/localization.py` (L564-715)
```python
class Localization(Parent, UniqueRepresentation):
    r"""
    The localization generalizes the construction of the field of fractions...
    """
    def __init__(self, base_ring, extra_units, ...):
        # ... implementation
```

### [16] Functor ranks

**File:** `src/sage/categories/pushout.py` (L44-127)
```python
class ConstructionFunctor(Functor):
    """
    Base class for construction functors with merge() and rank attributes.
    """
    rank = None  # lower rank = applied first
```

### [17] pushout algorithm

**File:** `src/sage/categories/pushout.py` (L4003-4046)
```python
def pushout(R, S):
    r"""
    Given a pair of objects R and S, try to construct a
    reasonable object Y and return maps such that
    canonically R <- Y -> S.
    """
```

### [18] _apply_functor pattern

**File:** `src/doc/en/thematic_tutorials/coercion_and_categories.rst` (L1305-1320)
```python
    sage: class MyFracFunctor(ConstructionFunctor):
    ....:     rank = 5
    ....:     def _apply_functor(self, R):
    ....:         return MyFrac(R,*self.args,**self.kwds)
    ....:     def merge(self, other):
    ....:         if isinstance(other, (type(self), FractionField)):
    ....:             return self
```

### Former `plans/SET_SPEC.md`

# SageMath Set Implementations: Comprehensive Reference

## 1. Category Hierarchy

The category framework distinguishes three layers:

1. **Actual hierarchy** — the containment graph
2. **SubcategoryMethods** — restriction methods on any category
3. **Shortcut methods** — named conveniences on `Sets()` (not axioms, not hierarchy)

* * *

### 1a. Actual Hierarchy (Containment Graph)

The real category containment:

```
Sets
├── FiniteSets
├── InfiniteSets
├── CountableSets
│   ├── FiniteEnumeratedSets
│   ├── InfiniteEnumeratedSets
│   └── RecursivelyEnumeratedSets
├── FacadeSets
├── PartiallyOrderedSets
│   └── TotallyOrderedSets
├── TopologicalSets
│   └── MetricSets
│       └── CompleteMetricSets
├── ObjectsOver(X)
│   └── SubsetsOf(X)
├── ObjectsUnder(X)
│   └── QuotientsOf(X)
├── FamiliesIndexedBy(I)
└── CartesianProductsOf(F)
```

Key cross-containments to encode:

```
FiniteSets ≤ CountableSets
FiniteEnumeratedSets ≤ FiniteSets
FiniteEnumeratedSets ≤ CountableSets
InfiniteEnumeratedSets ≤ InfiniteSets
InfiniteEnumeratedSets ≤ CountableSets
RecursivelyEnumeratedSets ≤ CountableSets

TotallyOrderedSets ≤ PartiallyOrderedSets

MetricSets ≤ TopologicalSets        ← every metric set is a topological set
CompleteMetricSets ≤ MetricSets

SubsetsOf(X) ≤ ObjectsOver(X)
QuotientsOf(X) ≤ ObjectsUnder(X)
```

**Rule:** `MetricSets` must have `TopologicalSets` as a supercategory in the actual
hierarchy, even though `Sets().Metric()` is a valid restriction method.

* * *

### 1b. `SubcategoryMethods` (Restriction Methods)

These are methods you can call on any subcategory.
They restrict the category independently of where the resulting category sits in the
actual hierarchy.

**On `Sets.SubcategoryMethods`:**

| Method | Returns |
| --- | --- |
| `Finite()` | Finite subcategory |
| `Infinite()` | Infinite subcategory |
| `Countable()` | Countable subcategory |
| `Facade()` | Facade subcategory |
| `PartiallyOrdered()` | Partially ordered subcategory |
| `TotallyOrdered()` | Totally ordered subcategory |
| `Topological()` | Topological subcategory |
| `Metric()` | Metric subcategory |
| `ObjectsOver(X)` | Objects over X subcategory |
| `ObjectsUnder(X)` | Objects under X subcategory |
| `IndexedBy(I)` | Indexed subcategory |
| `CartesianProducts()` | Cartesian products subcategory |
| `Algebras(base_ring)` | Algebra functor category |

**On lower categories:**

| Category | Method | Returns |
| --- | --- | --- |
| `CountableSets` | `RecursivelyEnumerated()` | Recursively enumerated subcategory |
| `ObjectsOver(X)` | `Subsets()` | Subsets subcategory |
| `ObjectsUnder(X)` | `Quotients()` | Quotients subcategory |
| `MetricSets` | `Complete()` | Complete metric subcategory |

* * *

### 1c. Shortcut Methods (Named Conveniences)

These are named aliases on `Sets()` returning canonical categories.
They are **not** the hierarchy and **not** axioms — just chained restrictions.

| Shortcut | Equivalent |
| --- | --- |
| `Sets().FiniteSets()` | `Sets().Finite()` |
| `Sets().InfiniteSets()` | `Sets().Infinite()` |
| `Sets().CountableSets()` | `Sets().Countable()` |
| `Sets().FiniteEnumeratedSets()` | `Sets().Countable().Finite()` |
| `Sets().InfiniteEnumeratedSets()` | `Sets().Countable().Infinite()` |
| `Sets().RecursivelyEnumeratedSets()` | `Sets().Countable().RecursivelyEnumerated()` |
| `Sets().PartiallyOrderedSets()` | `Sets().PartiallyOrdered()` |
| `Sets().TotallyOrderedSets()` | `Sets().TotallyOrdered()` |
| `Sets().TopologicalSets()` | `Sets().Topological()` |
| `Sets().MetricSets()` | `Sets().Metric()` |
| `Sets().CompleteMetricSets()` | `Sets().Metric().Complete()` |
| `Sets().SubsetsOf(X)` | `Sets().ObjectsOver(X).Subsets()` |
| `Sets().QuotientsOf(X)` | `Sets().ObjectsUnder(X).Quotients()` |
| `Sets().FamiliesIndexedBy(I)` | `Sets().IndexedBy(I)` |
| `Sets().CartesianProductsOf(F)` | `Sets().CartesianProducts()` |

* * *

## 2. Category Definitions and Methods

### `Sets` — `src/sage/categories/sets_cat.py`

The base category for all parents.
Its `SubcategoryMethods` (available on any subcategory) are:

| Method | Returns |
| --- | --- |
| `CartesianProducts()` | Category of Cartesian products of sets |
| `Subquotients()` | Category of subquotients |
| `Quotients()` | Category of quotients |
| `Subobjects()` | Category of subobjects |
| `IsomorphicObjects()` | Category of isomorphic objects |
| `Topological()` | Topological subcategory |
| `Metric()` | Metric subcategory |
| `Algebras(base_ring)` | Algebra functor category |
| `Finite()` | Finite subcategory |
| `Infinite()` | Infinite subcategory |
| `Enumerated()` | Enumerated subcategory |
| `Facade()` | Facade subcategory |

`Sets.ParentMethods` (inherited by all parents in `Sets()`):

| Method | Description |
| --- | --- |
| `__contains__(x)` | Abstract: test membership |
| `an_element()` | Return a typical element (cached) |
| `some_elements()` | Return a list of elements for testing |
| `is_parent_of(element)` | Check if `self` is the parent (no coercion) |
| `_element_constructor_` | Lazy attribute for element construction |
| `_element_constructor_from_element_class(...)` | Default element constructor |
| `_test_an_element(**options)` | Test `an_element()` |
| `_test_elements(**options)` | Run test suite on `an_element()` |
| `_test_elements_eq_reflexive(**options)` | Test `==` is reflexive |
| `_test_elements_eq_symmetric(**options)` | Test `==` is symmetric |
| `_test_elements_eq_transitive(**options)` | Test `==` is transitive |
| `_test_elements_neq(**options)` | Test `==` and `!=` are consistent |
| `_test_some_elements(**options)` | Test `some_elements()` |

* * *

### `FiniteSets` — `src/sage/categories/finite_sets.py`

Axiom: `Finite`. Super category: `Sets()`.

`SubcategoryMethods`:
- `Infinite()` — raises `TypeError` (incompatible axiom)

`ParentMethods`:
- `is_finite()` — always returns `True`

`Subquotients` — adds `FiniteSets()` as extra super category (subquotient of a finite
set is finite).

`Algebras` — adds `ModulesWithBasis(base_ring).FiniteDimensional()` as extra super
category.

* * *

### `EnumeratedSets` — `src/sage/categories/enumerated_sets.py`

Axiom: `Enumerated`. Super category: `Sets()`.

`ParentMethods`:

| Method | Description |
| --- | --- |
| `__iter__()` | Iterator; dispatches to `_iterator_from_next`, `_iterator_from_unrank`, or `_iterator_from_list` |
| `is_empty()` | Return whether the set is empty |
| `iterator_range(start, stop, step)` | Iterate over a range of elements by rank |
| `unrank_range(start, stop, step)` | Return a list of elements by rank range |
| `__getitem__(i)` | Shorthand for `unrank(i)` or `unrank_range(slice)` |
| `__len__()` | Return `int(cardinality())` |
| `tuple()` | Return a cached tuple of elements |
| `list()` | Return a fresh list of elements |
| `cardinality()` | Return number of elements (Integer or infinity) |
| `unrank(n)` | Return the n-th element |
| `rank(e)` | Return the position of element `e` |
| `first()` | Return the first element |
| `next(e)` | Return the element following `e` |
| `random_element()` | Return a random element |
| `_test_enumerated_set_contains(**options)` | Test `__contains__` |
| `_test_enumerated_set_iter_cardinality(**options)` | Test consistency of `__iter__` and `cardinality` |

* * *

### `FiniteEnumeratedSets` — `src/sage/categories/finite_enumerated_sets.py`

Super categories: `EnumeratedSets()`, `FiniteSets()`.

`ParentMethods` (additional to `EnumeratedSets`):

| Method | Description |
| --- | --- |
| `__len__()` | `int(cardinality())` |
| `_cardinality_from_iterator()` | Brute-force cardinality by iteration |
| `_cardinality_from_list()` | Cardinality from cached list |
| `_list_from_iterator()` | Build and cache list from iterator |
| `_first_from_iterator()` | First element from iterator |
| `_next_from_iterator(obj)` | Next element from iterator |
| `_unrank_from_iterator(r)` | Unrank by iterating |
| `_rank_from_iterator(x)` | Rank by iterating |
| `_test_enumerated_set_iter_cardinality(**options)` | Consistency test |

* * *

### `InfiniteEnumeratedSets` — `src/sage/categories/infinite_enumerated_sets.py`

Super categories: `EnumeratedSets()`, `Sets().Infinite()`.

`ParentMethods`:

| Method | Description |
| --- | --- |
| `random_element()` | Raises `NotImplementedError("infinite set")` |
| `tuple()` | Raises `NotImplementedError("cannot list an infinite set")` |
| `list()` | Raises `NotImplementedError("cannot list an infinite set")` |
| `_test_enumerated_set_iter_cardinality(**options)` | Checks `cardinality() == infinity` and `list()` raises |

* * *

### `FacadeSets` — `src/sage/categories/facade_sets.py`

Axiom: `Facade`. A facade set represents its elements as elements of another parent.

`ParentMethods`:
- `_element_constructor_(element)` — coerces element from any facade parent

* * *

## 3. Concrete Set Implementations in `sage.sets`

All public exports are listed in `src/sage/sets/all.py`:

* * *

### `Set` (factory function) — `src/sage/sets/set.py`

The `Set(X)` factory returns one of several concrete classes depending on `X`:
- `Set_object_enumerated` if `X` is finite (frozenset-backed)
- `Set_object` otherwise

**Mix-in base classes:**

| Class | Purpose |
| --- | --- |
| `Set_base` | Provides `union`, `intersection`, `difference`, `symmetric_difference` |
| `Set_boolean_operators` | Provides `__or__`, `__and__`, `__xor__` |
| `Set_add_sub_operators` | Provides `__add__` (union), `__sub__` (difference) |

#### `Set_object` — general wrapper

Category: `Sets()` (or `Sets().Finite()`, `Sets().Infinite()`, `Sets().Enumerated()`
inferred from wrapped object).

| Method | Description |
| --- | --- |
| `__hash__()` | Hash of wrapped object |
| `_latex_()` | LaTeX representation |
| `_repr_()` | String representation |
| `__iter__()` | Iterate over wrapped object |
| `_an_element_()` | Return an element |
| `__contains__(x)` | Membership test |
| `__richcmp__(right, op)` | Comparison |
| `cardinality()` | Return cardinality |
| `is_empty()` | Return whether empty |
| `is_finite()` | Return whether finite |
| `object()` | Return the underlying wrapped object |
| `subsets(size=None)` | Return `Subsets` object |
| `subsets_lattice()` | Return lattice of subsets (finite only) |
| `_sympy_()` | Return SymPy set equivalent |

#### `Set_object_enumerated` — finite enumerated set wrapper

Extends `Set_object`. Category: `FiniteEnumeratedSets()`.

| Method | Description |
| --- | --- |
| `random_element()` | Random element |
| `is_finite()` | Always `True` |
| `cardinality()` | Count elements |
| `__len__()` | Length |
| `__iter__()` | Iterate over `frozenset` |
| `_latex_()` | LaTeX `\left\{...\right\}` |
| `_repr_()` | String `{...}` |
| `list()` | List of elements |
| `set()` | Python `set` |
| `frozenset()` | Python `frozenset` |
| `__hash__()` | Hash of frozenset |
| `__richcmp__(other, op)` | Set equality/comparison |

#### Binary set operation classes

All extend `Set_object` and are created lazily by `Set_base` methods:

| Class | Operation |
| --- | --- |
| `Set_object_union` | `A ∪ B` |
| `Set_object_intersection` | `A ∩ B` |
| `Set_object_difference` | `A \ B` |
| `Set_object_symmetric_difference` | `A △ B` |

* * *

### `FiniteEnumeratedSet` — `src/sage/sets/finite_enumerated_set.py`

Category: `FiniteEnumeratedSets().Facade()`. Backed by a tuple stored in memory.
Unique representation.

Key methods: `list()`, `cardinality()`, `random_element()`, `first()`, `__iter__()`,
`__contains__()`, `rank()`, `unrank()`.

* * *

### `IntegerRange` — `src/sage/sets/integer_range.py`

Factory returning one of three subclasses:

| Class | When used |
| --- | --- |
| `IntegerRangeFinite` | Both `begin` and `end` are finite |
| `IntegerRangeInfinite` | One bound is infinite, no `middle_point` |
| `IntegerRangeFromMiddle` | `middle_point` is given |

Category: `FiniteEnumeratedSets()` or `InfiniteEnumeratedSets()` depending on bounds.

Key methods: `rank(x)`, `unrank(n)`, `first()`, `next(x)`, `cardinality()`,
`__iter__()`, `__contains__()`, `__len__()`.

* * *

### `NonNegativeIntegers` — `src/sage/sets/non_negative_integers.py`

Category: `InfiniteEnumeratedSets().Facade()`. Elements are plain `Integer` objects with
parent `ZZ`.

Key methods: `__iter__()`, `first()`, `next(x)`, `cardinality()`, `__contains__()`,
`an_element()`.

* * *

### `PositiveIntegers` — `src/sage/sets/positive_integers.py`

Subclass of `IntegerRangeInfinite`. Category: `InfiniteEnumeratedSets().Facade()`.

Additional methods: `_repr_()`, `an_element()` (returns 42), `_sympy_()` (returns SymPy
`Naturals`).

* * *

### `Primes` — `src/sage/sets/primes.py`

Category: `InfiniteEnumeratedSets().Facade()` (or `FiniteEnumeratedSets().Facade()` for
finite subsets via congruence conditions).

Supports congruence conditions via `modulus` and `classes` arguments.

Key methods: `__contains__(x)`, `__iter__()`, `cardinality()`, `first()`, `next(x)`,
`an_element()`, `unrank(n)`.

* * *

### `RealSet` — `src/sage/sets/real_set.py`

A subset of the real line represented as a finite union of intervals.
Inherits `Set_base`, `Set_boolean_operators`, `Set_add_sub_operators`. Category:
`TopologicalSpaces()`.

**Construction class methods:**

| Method | Example |
| --- | --- |
| `RealSet.open(a, b)` | `(a, b)` |
| `RealSet.closed(a, b)` | `[a, b]` |
| `RealSet.open_closed(a, b)` | `(a, b]` |
| `RealSet.closed_open(a, b)` | `[a, b)` |
| `RealSet.point(a)` | `{a}` |
| `RealSet.unbounded_below_open(b)` | `(-oo, b)` |
| `RealSet.unbounded_below_closed(b)` | `(-oo, b]` |
| `RealSet.unbounded_above_open(a)` | `(a, +oo)` |
| `RealSet.unbounded_above_closed(a)` | `[a, +oo)` |
| `RealSet.interval(a, b, lower_closed, upper_closed)` | General interval |

**Instance methods:** `union`, `intersection`, `difference`, `symmetric_difference`,
`complement()`, `is_empty()`, `is_finite()`, `is_connected()`, `inf()`, `sup()`,
`measure()`, `closure()`, `interior()`, `boundary()`, `contains(x)`, `__iter__()` (over
`InternalRealInterval` components), `_sympy_()`.

**`InternalRealInterval`** (internal component class):

| Method | Description |
| --- | --- |
| `lower()` / `upper()` | Endpoint values |
| `lower_closed()` / `upper_closed()` | Closedness at endpoints |
| `lower_open()` / `upper_open()` | Openness at endpoints |
| `is_empty()` | Whether interval is empty |
| `is_point()` | Whether interval is a single point |

* * *

### `RecursivelyEnumeratedSet` — `src/sage/sets/recursively_enumerated_set.pyx`

A set defined by seeds and a successor function.
Supports four structure types:

| Structure | Class |
| --- | --- |
| None (general) | `RecursivelyEnumeratedSet_generic` |
| `'symmetric'` | `RecursivelyEnumeratedSet_symmetric` |
| `'graded'` | `RecursivelyEnumeratedSet_graded` |
| `'forest'` | `RecursivelyEnumeratedSet_forest` |

Key methods:

| Method | Description |
| --- | --- |
| `__iter__()` | Default iteration (BFS or DFS depending on structure) |
| `breadth_first_search_iterator()` | BFS iterator |
| `depth_first_search_iterator()` | DFS iterator |
| `graded_component(depth)` | Elements at a given depth (graded/symmetric) |
| `graded_component_iterator()` | Iterator over graded components |
| `elements_of_depth_iterator(depth)` | Elements at given depth |
| `cardinality()` | Cardinality (may be infinite) |

* * *

### `DisjointUnionEnumeratedSets` — `src/sage/sets/disjoint_union_enumerated_sets.py`

Category: `FiniteEnumeratedSets()` or `InfiniteEnumeratedSets()` depending on the
family.

Options: `keepkey=True` (returns `(key, element)` pairs), `facade=False` (wraps
elements).

Key methods: `__iter__()`, `cardinality()`, `an_element()`, `first()`, `__contains__()`.

* * *

### `CartesianProduct` — `src/sage/sets/cartesian_product.py`

Raw data structure for Cartesian products.
Use `cartesian_product(...)` at the user level.

Key methods: `cartesian_factors()`, `cardinality()`, `random_element()`, `an_element()`,
`__iter__()`, `__contains__()`, `_cartesian_product_of_elements(...)`.

* * *

### `ConditionSet` — `src/sage/sets/condition_set.py`

Set of elements of a universe satisfying given predicates.
Inherits `Set_base`, `Set_boolean_operators`, `Set_add_sub_operators`.

```python
Evens = ConditionSet(ZZ, is_even)
SmallOdds = ConditionSet(ZZ, is_odd, abs(y) <= 11, vars=[y])
```

Key methods: `__contains__(x)` (applies all predicates), `universe()`, `predicates()`,
`_sympy_()`.

* * *

### `ImageSubobject` — `src/sage/sets/image_set.py`

The image `{f(x) | x ∈ X}` of a set under a map.

Options: `is_injective` (`None`, `False`, `True`, `'check'`), `inverse`.

Key methods: `__iter__()`, `__contains__(x)`, `cardinality()`, `an_element()`.

* * *

### `TotallyOrderedFiniteSet` — `src/sage/sets/totally_ordered_finite_set.py`

A finite set with a user-specified total order.
Category: `FiniteEnumeratedSets()` and `Posets()`.

Elements are `TotallyOrderedFiniteSetElement` objects (when `facade=False`) supporting
`<`, `<=`, `>`, `>=`.

Key methods: `__iter__()`, `cardinality()`, `rank(x)`, `unrank(n)`, `__contains__()`.

* * *

### `FiniteSetMaps` — `src/sage/sets/finite_set_maps.py`

The set of all maps between two finite sets.
Category: `FiniteMonoids()` (for endo-maps) or `FiniteEnumeratedSets()`.

Key methods: `cardinality()`, `__iter__()`, `an_element()`, `identity()` (for
endo-maps), `__mul__` (composition).

* * *

### `DisjointSet` — `src/sage/sets/disjoint_set.pyx`

A union-find (disjoint-set) data structure.
**Not** a `Parent`; it is a mutable partition tracker.

Two variants: `DisjointSet_of_integers` (for `0..n-1`) and `DisjointSet_of_hashables`.

Key methods:

| Method | Description |
| --- | --- |
| `find(x)` | Return the canonical representative of `x`'s block |
| `union(x, y)` | Merge the blocks of `x` and `y` |
| `number_of_subsets()` | Number of disjoint blocks |
| `root_to_elements_dict()` | Dict mapping roots to their blocks |
| `element_to_root_dict()` | Dict mapping elements to their roots |
| `to_digraph()` | Return the union-find tree as a digraph |
| `set_partition()` | Return as a `SetPartition` |

* * *

### `Family` — `src/sage/sets/family.pyx`

Factory for indexed families `(f_i)_{i ∈ I}`. Returns one of several internal classes:

| Class | When used |
| --- | --- |
| `TrivialFamily` | Input is a list/tuple (identity function) |
| `FiniteFamily` | Finite dict-based family |
| `LazyFamily` | Infinite or lazy function-based family |
| `EnumeratedFamily` | Wraps an enumerated set |

Key methods: `keys()`, `values()`, `__getitem__(i)`, `__iter__()`, `cardinality()`,
`list()`, `map(f)`, `zip(other)`.

* * *

### `EnumeratedSetFromIterator` — `src/sage/sets/set_from_iterator.py`

Builds an enumerated set from a callable that returns an iterator.
Supports optional caching.

Also provides decorators `@set_from_function` and `@set_from_method`.

Key methods: `__iter__()`, `cardinality()`, `an_element()`, `unrank(n)`.

* * *

## 4. Summary Table

| Class | File | Category | Finite? |
| --- | --- | --- | --- |
| `Set_object` | `sets/set.py` | `Sets()` (inferred) | depends |
| `Set_object_enumerated` | `sets/set.py` | `FiniteEnumeratedSets()` | yes |
| `Set_object_union/intersection/difference/symmetric_difference` | `sets/set.py` | `Sets()` | depends |
| `FiniteEnumeratedSet` | `sets/finite_enumerated_set.py` | `FiniteEnumeratedSets().Facade()` | yes |
| `IntegerRange` | `sets/integer_range.py` | `FiniteEnumeratedSets()` or `InfiniteEnumeratedSets()` | depends |
| `NonNegativeIntegers` | `sets/non_negative_integers.py` | `InfiniteEnumeratedSets().Facade()` | no |
| `PositiveIntegers` | `sets/positive_integers.py` | `InfiniteEnumeratedSets().Facade()` | no |
| `Primes` | `sets/primes.py` | `InfiniteEnumeratedSets().Facade()` | no (or yes with congruence) |
| `RealSet` | `sets/real_set.py` | `TopologicalSpaces()` | no |
| `RecursivelyEnumeratedSet` | `sets/recursively_enumerated_set.pyx` | `EnumeratedSets()` | depends |
| `DisjointUnionEnumeratedSets` | `sets/disjoint_union_enumerated_sets.py` | `FiniteEnumeratedSets()` or `InfiniteEnumeratedSets()` | depends |
| `CartesianProduct` | `sets/cartesian_product.py` | inferred from factors | depends |
| `ConditionSet` | `sets/condition_set.py` | inferred from universe | depends |
| `ImageSubobject` | `sets/image_set.py` | inferred from domain | depends |
| `TotallyOrderedFiniteSet` | `sets/totally_ordered_finite_set.py` | `FiniteEnumeratedSets()` + `Posets()` | yes |
| `FiniteSetMaps` | `sets/finite_set_maps.py` | `FiniteMonoids()` or `FiniteEnumeratedSets()` | yes |
| `DisjointSet` | `sets/disjoint_set.pyx` | (not a Parent; union-find structure) | — |
| `Family` | `sets/family.pyx` | `FiniteEnumeratedSets()` or `InfiniteEnumeratedSets()` | depends |
| `EnumeratedSetFromIterator` | `sets/set_from_iterator.py` | `EnumeratedSets()` | depends |

* * *

### Citations

**File:** src/sage/categories/sets_cat.py (L99-115)

```python
class Sets(Category_singleton):
    r"""
    The category of sets.

    The base category for collections of elements with = (equality).

    This is also the category whose objects are all parents.
    """
```

**File:** src/sage/categories/sets_cat.py (L302-800) — `SubcategoryMethods`

**File:** src/sage/categories/sets_cat.py (L957-1400) — `ParentMethods`

**File:** src/sage/categories/finite_sets.py (L16-107)

**File:** src/sage/categories/enumerated_sets.py (L21-94)

**File:** src/sage/categories/enumerated_sets.py (L156-600)

**File:** src/sage/categories/finite_enumerated_sets.py (L22-54)

**File:** src/sage/categories/finite_enumerated_sets.py (L81-150)

**File:** src/sage/categories/infinite_enumerated_sets.py (L19-114)

**File:** src/sage/categories/facade_sets.py (L16-80)

**File:** src/sage/sets/all.py (L1-16)

**File:** src/sage/sets/set.py (L209-316) — `Set_base`

**File:** src/sage/sets/set.py (L348-437) — `Set_boolean_operators`,
`Set_add_sub_operators`

**File:** src/sage/sets/set.py (L439-843) — `Set_object`

**File:** src/sage/sets/set.py (L845-1100) — `Set_object_enumerated`

**File:** src/sage/sets/finite_enumerated_set.py (L27-80)

**File:** src/sage/sets/integer_range.py (L28-80)

**File:** src/sage/sets/non_negative_integers.py (L17-80)

**File:** src/sage/sets/positive_integers.py (L15-92)

**File:** src/sage/sets/primes.py (L67-80)

**File:** src/sage/sets/real_set.py (L113-300)

**File:** src/sage/sets/recursively_enumerated_set.pyx (L1-100)

**File:** src/sage/sets/disjoint_union_enumerated_sets.py (L29-80)

**File:** src/sage/sets/cartesian_product.py (L32-80)

**File:** src/sage/sets/condition_set.py (L26-80)

**File:** src/sage/sets/image_set.py (L34-80)

**File:** src/sage/sets/totally_ordered_finite_set.py (L31-80)

**File:** src/sage/sets/finite_set_maps.py (L38-80)

**File:** src/sage/sets/disjoint_set.pyx (L1-100)

**File:** src/sage/sets/family.pyx (L58-100)

**File:** src/sage/sets/set_from_iterator.py (L73-80)

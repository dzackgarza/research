---
id: TASK-INTEGRATE-COMPLEX-MANIFOLDS-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY]]'
title: Research category integration for complex manifolds
status: complete
priority: high
description: Research and prepare the category-spec integration path for complex manifolds.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors, Hom/End/Aut
  surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation cards needed
  to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for complex manifolds

## Summary

Research and prepare the category-spec integration path for complex manifolds.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating complex manifolds.

Checked sources:

- Sage category docs, `Manifolds` and `ComplexManifolds`:
  https://doc.sagemath.org/html/en/reference/categories/sage/categories/manifolds.html
- Sage manifold constructor docs, `Manifold(field='complex', structure=...)`:
  https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/manifold.html
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/manifolds.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/manifolds/manifold.py`
- `TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY`: smooth-manifold source admission.
- `TASK-INTEGRATE-COMPLEX-VARIETIES-CATEGORY`: complex algebraic variety and
  analytification boundary.
- `theory/references/literature/huybrechts_k3_lectures.md`: complex K3, GAGA,
  compact Kähler, Hodge, and polarization context.

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Source Admission

A complex manifold is a manifold modeled on `CC^d` with a holomorphic atlas. Sage
records this directly in `ComplexManifolds`: a `d`-dimensional complex manifold has
underlying coordinate vector space `CC^d` and holomorphic transition functions. Sage
routes `Manifolds(CC).Complex()` to `ComplexManifolds(CC)` while preserving any
existing manifold axioms, and `ComplexManifolds(K)` has analytic manifolds as a
supercategory.

The project vocabulary should use:

- `Manifolds(CC).Complex()` or `ComplexManifolds(CC)` for analytic complex manifolds;
- `ComplexManifold` for the object noun;
- holomorphic maps as Hom elements in the complex-manifold Hom category;
- `AlmostComplex()` only for smooth manifolds with an almost-complex tensor `J`; it is
  not the same as a complex manifold unless integrability/holomorphic atlas data is
  present;
- compact, connected, Kähler, projective, complex-torus, K3, and hyperkähler
  refinements only under their own hypotheses.

Do not identify `ComplexManifolds()` with `ComplexVarieties()`. A smooth proper complex
algebraic variety has an associated analytic complex space/manifold under
analytification when the hypotheses hold, but this is a bridge construction, not an
inheritance relation.

## Sage Surface Survey

Sage provides category-level evidence:

- `Manifolds(CC).Complex()` returns the complex-manifold category over Sage's complex
  field object.
- `ComplexManifolds` is a distinct category class whose supercategory is
  `Manifolds(K).Analytic()`.
- `Manifold(n, name, field='complex', structure=...)` is the constructor-level entry
  point for complex-field manifolds.
- The underlying SageManifolds implementation supplies charts, maps, scalar fields,
  tangent/tensor/form surfaces, and Hom objects through the same manifold machinery
  surveyed in the smooth-manifold card.

Inference: the category-spec layer should preserve Sage's analytic complex-manifold
surface rather than deriving it from algebraic geometry. Sage is good implementation
evidence for local analytic/tensor calculus, while algebraic/coherent-sheaf methods
must stay on algebraic variety or analytification bridge surfaces.

## Mathematical Bridge Context

Huybrechts records the analytic/algebraic boundary for K3 surfaces: a complex K3
surface is a compact connected complex manifold of dimension two with trivial
`Omega_X^2` and `H^1(X, O_X)=0`; GAGA associates a complex analytic space to finite
type schemes over `C`, and for proper/projective hypotheses coherent sheaf categories
and cohomology agree. Smooth algebraic varieties over `C` analytify to complex
manifolds, but non-projective complex K3 surfaces and complex tori show that complex
manifolds are strictly broader than algebraic varieties.

Hodge-theoretic surfaces require stricter hypotheses. Compact Kähler manifolds carry
Hodge structures on cohomology; projective or rational/integral Kähler-class
hypotheses are needed for the polarization statements used in lattice and period-domain
work. Do not place Hodge numbers, Picard groups, divisor/sheaf cohomology, or algebraic
cycle methods on arbitrary complex manifolds.

## Method Ownership Guidance

Admit these owner directions for future spec rows:

- `holomorphic_map(...)`, `Hom(M,N)`, biholomorphism predicates, and composition:
  owned by `ComplexManifolds(CC).HomCategory()` or stricter analytic Hom surfaces.
- `holomorphic_chart`, holomorphic transition maps, and complex coordinate functions:
  owned by charted/presented complex-manifold refinements.
- `complex_dimension()` may be owned by finite-dimensional complex manifolds; avoid
  conflating it with real dimension except through an explicit `real_dimension = 2d`
  convention.
- `complex_structure()` / almost-complex tensor `J`: owned by almost-complex or complex
  manifold refinements with clear integrability status. `AlmostComplex()` is not a
  replacement for `Complex()`.
- `is_kahler()`, Kähler class, Hodge decomposition, period map, and polarization
  surfaces belong to compact Kähler, projective, K3, hyperkähler, or period-domain
  refinements after source admission.
- `analytification()` is a bridge method on suitable complex algebraic varieties or
  schemes, returning an analytic complex space/manifold object when smoothness permits.

## Dependency And Downstream Routing

Complex manifolds depend on the smooth-manifold surface, topological/complex field
ownership, Hom/End/Aut surfaces, and tensor/form vocabulary. Kähler, Hodge, period,
Picard, and K3 surfaces depend additionally on cohomology, sheaf, lattice, and
proof-audit-ready source cards.

Downstream work blocked or informed by this admission:

- K3 and complex-surface analytic bridges must distinguish complex K3 surfaces from
  algebraic/projective K3 surfaces.
- Period-domain and Hodge-theory specs must use compact Kähler/projective hypotheses,
  not arbitrary complex manifolds.
- Complex-variety tasks may refer to analytification/GAGA bridge surfaces but must not
  move algebraic Picard/divisor/sheaf methods into `ComplexManifolds()`.

No new follow-up card is needed from this pass. Existing complex-variety, complex
surface, K3/Coble geometry, lattice, and family/period-domain cards own the stricter
bridges and invariants.

## Smoke And Implementation Guidance

Future smoke examples should use small complex manifolds, simple holomorphic charts,
and Hom construction. Avoid using K3, torus quotient, period-domain, or sheaf-cohomology
examples as baseline complex-manifold smokes.

## Acceptance Criteria

- [x] Identify the mathematical definition and the intended project vocabulary for this category.
- [x] Survey relevant Sage or backend surfaces and local category-spec dependencies.
- [x] Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- [x] List downstream categories or tasks blocked by this integration.
- [x] Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Dependencies And Boundaries

This is a research/planning card, not an implementation card. Do not write category code or specs until the vocabulary, ownership boundaries, and dependencies are clear or an approved plan delegates that work.

## Review Log

### Review 2026-05-07 (Independent Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** None
**Outcome:** complete

#### Evidence
**Gate 1:** Stacks/sibling cards for complex manifold definition as locally ringed spaces locally isomorphic to complex polydiscs/domains.
**Gate 2:** [x] All 5 ACs checked. Definition, Sage/backend survey, category relationships, downstream work, follow-up routing completed.
**Gate 3-6:** No issues. Complex manifolds correctly differentiated from complex varieties (GAGA bridge noted). No complex-manifold-specific lattice/Picard/divisor/sheaf method invented.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for complex manifolds, recording the
  analytic `ComplexManifolds(CC)` owner, the distinction from complex algebraic
  varieties, the analytification bridge, and downstream Kähler/Hodge/K3 boundaries.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.

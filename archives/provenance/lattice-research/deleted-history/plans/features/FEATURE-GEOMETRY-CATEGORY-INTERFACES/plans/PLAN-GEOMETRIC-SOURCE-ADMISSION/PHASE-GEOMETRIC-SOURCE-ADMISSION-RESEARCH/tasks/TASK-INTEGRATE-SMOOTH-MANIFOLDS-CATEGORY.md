---
id: TASK-INTEGRATE-SMOOTH-MANIFOLDS-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn: []
title: Research category integration for smooth manifolds
status: complete
priority: high
description: Research and prepare the category-spec integration path for smooth manifolds.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this
  category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors,
  Hom/End/Aut surfaces, and smoke expectations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation
  cards needed to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for smooth manifolds

## Summary

Research and prepare the category-spec integration path for smooth manifolds.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating smooth manifolds.

Checked sources:

- Sage category docs, `Manifolds`: https://doc.sagemath.org/html/en/reference/categories/sage/categories/manifolds.html
- Sage manifold constructor docs, `TopologicalManifold` and `Manifold()`:
  https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/manifold.html
- Sage differentiable manifold docs:
  https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/differentiable/manifold.html
- Sage differentiable maps docs:
  https://doc.sagemath.org/html/en/reference/manifolds/diff_map.html
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/manifolds.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/manifolds/manifold.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/manifolds/differentiable/manifold.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/manifolds/differentiable/diff_map.py`

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Source Admission

A smooth manifold over a topological field `K` is a topological manifold over `K`
together with a smooth atlas. Sage's category source defines `Manifolds(k)` for
second-countable Hausdorff spaces locally homeomorphic to `k^d`, requires `k` to be a
topological field, places `Manifolds(k)` under topological spaces, and records `Smooth`
as the subcategory whose objects have a smooth atlas. The public project spelling
should therefore follow Sage's mathematical category path:

- `Manifolds(K)` for topological manifolds over a topological field `K`;
- `Manifolds(K).Differentiable()` for differentiable-atlas manifolds;
- `Manifolds(K).Smooth()` for smooth-atlas manifolds;
- `Manifolds(K).FiniteDimensional()`, `Connected()`, `Analytic()`, `Complex()`,
  `AlmostComplex()`, and metric/symplectic/Poisson refinements only as extra
  structure or stricter hypotheses.

Real and complex manifolds are the primary concrete targets. Sage allows a general
topological field `K`, but non-real/non-complex differentiability and calculus surfaces
must remain source-audited interop routes until their mathematical conventions are
specified.

The project noun should be `SmoothManifold`, with points as elements, open subsets as
smooth manifolds in their own right, and smooth maps as Hom elements. Do not use
`SmoothManifolds()` as a disconnected root if `Manifolds(K).Smooth()` can preserve the
Sage category refinement order.

## Sage Surface Survey

Sage provides strong implementation evidence through SageManifolds:

- `Manifold(n, name, field=..., structure='smooth')` is the constructor-level public
  route, with `structure='smooth'` the default.
- `DifferentiableManifold` implements differentiable and smooth manifolds; open subsets
  are also `DifferentiableManifold` objects.
- `Manifolds(K).Smooth().super_categories()` is `Manifolds(K).Differentiable()`;
  `Manifolds(K).super_categories()` is topological spaces.
- `DiffMap` implements differentiable maps between differentiable manifolds over the
  same topological field. Sage documents these as morphisms of the differentiable
  manifold category, with `Hom(M,N)` as their homset.
- The installed manifold subtree exposes charts, transition maps, scalar fields,
  tangent spaces and tangent vectors, vector fields, tensor fields, differential forms,
  de Rham cohomology, affine and bundle connections, vector bundles, pseudo-Riemannian
  metrics, symplectic and Poisson structures, curves, geodesics, and submanifolds.

Inference: Sage already has a mature smooth-manifold category and object surface. The
category-spec work should wrap and refine this surface rather than invent a parallel
manifold hierarchy. The spec still needs mathematical ownership rows because Sage's
large object API mixes constructors, coordinate presentations, tensor calculus, and
geometric structures on the same implementation classes.

## Method Ownership Guidance

Admit these owner directions for future spec rows:

- `dimension()`: owned by `Manifolds(K)` in Sage's source category: `Manifolds`
  is presented as the category of `d`-dimensional manifolds over a topological
  field, and `dimension()` is an abstract method on `Manifolds.ParentMethods`.
  `Manifolds(K).FiniteDimensional()` is a refinement selected by finite
  dimensionality, not the first owner of the method in Sage's category source.
- `chart()`, `atlas()`, `default_chart()`, transition maps, and coordinate restrictions:
  owned by presented/charted manifold refinements, not by arbitrary topological spaces.
- `open_subset(...)`: owned by manifolds; codomain is a manifold open subobject with
  inherited smooth structure when the ambient manifold is smooth.
- `point(...)` and containment: point construction and membership live on manifold
  parents and their open subobjects.
- `diff_map(N, ...)`, `Hom(M,N)`, identity maps, composition, and diffeomorphism
  predicates: owned by the smooth/differentiable manifold Hom category, not by raw
  set-map surfaces.
- `tangent_space(p)`, `tangent_vector`, vector fields, tensor fields, differential
  forms, and de Rham cohomology: owned by smooth or differentiable manifold refinements
  with the appropriate module/tensor/form codomains. Do not flatten these into generic
  helper functions.
- `metric`, `levi_civita_connection`, geodesic, curvature, symplectic form, Poisson
  tensor, and almost-complex structure methods belong to stricter structured-manifold
  refinements, not all smooth manifolds.

## Dependency And Bridge Guidance

Smooth manifolds depend on `Sets().Topological()`, topological fields, Hom/End/Aut
surfaces, and module/tensor/form vocabulary for tangent and tensor objects. This card
does not authorize implementation before those common surfaces can express maps,
sections, modules of fields, forms, and automorphisms.

Complex manifolds are a separate analytic refinement of manifolds over `CC`; they are
not complex algebraic varieties. A smooth complex algebraic variety may admit an
associated complex manifold/analytic space under an analytification bridge, but the
bridge must not move algebraic methods such as divisors, Picard groups, coherent sheaf
cohomology, or projective invariants onto `ComplexManifolds()` by default.

Downstream structured-manifold cards include complex manifolds, pseudo-Riemannian
manifolds, symplectic/Poisson manifolds, vector bundles, curve/geodesic interfaces,
period domains, and K3/complex-surface analytic bridges. Existing complex-manifold and
complex-variety cards already own the immediate bridge follow-up; no new decision card
is needed from this pass.

## Smoke And Implementation Guidance

Future smoke examples should use small SageManifolds objects such as the real line,
`RR^2`, or the sphere `S^2`, and should test category membership, Hom construction,
charts/open subsets, and one tangent-space or scalar-field surface. Do not use expensive
symbolic tensor examples as basic category smokes.

## Acceptance Criteria

- [x] Identify the mathematical definition and the intended project vocabulary for this category.
- [x] Survey relevant Sage or backend surfaces and local category-spec dependencies.
- [x] Determine how this category relates to existing planned categories, constructors, Hom/End/Aut surfaces, and smoke expectations.
- [x] List downstream categories or tasks blocked by this integration.
- [x] Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Dependencies And Boundaries

This is a research/planning card, not an implementation card. Do not write category code or specs until the vocabulary, ownership boundaries, and dependencies are clear or an approved plan delegates that work.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for smooth manifolds, recording the
  `Manifolds(K).Smooth()` owner, SageManifolds source surface, Hom-map ownership, and
  downstream bridge boundaries. Existing complex-manifold and complex-variety cards
  already own the immediate bridge follow-up, so no new card is needed from this pass.
- 2026-05-06: Reworked the `dimension()` owner guidance after Gate 1 review found
  that Sage grounds `dimension()` on `Manifolds.ParentMethods`, not on the
  `FiniteDimensional` axiom class.

## Review Log

### Review 2026-05-06 (Harvey)

**Gates passed:** none
**Gates failed:** Gate 1 Definition Grounding
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 1 Findings: Definition Grounding

- `dimension()` was incorrectly listed as owned by
  `Manifolds(K).FiniteDimensional()`. Installed Sage source places
  `dimension()` on `Manifolds.ParentMethods`, and the Sage category docstring
  defines `Manifolds(k)` using `d`-dimensional manifolds over a topological
  field. This was a method-owner grounding defect introduced in commit
  `57d93b7`.

### Re-review 2026-05-06 (Nietzsche)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** none
**Outcome:** independent re-review passed Gates 1-6; human approval still required before completion

#### Residual Risks

- This is source admission, not a final method spec. Future spec cards still need
  full signatures and codomains for charts, tangent spaces, tensor/form objects,
  structured-manifold refinements, and non-real/non-complex calculus conventions.

---
id: TASK-INTEGRATE-POLYTOPES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn: []
title: Research category integration for polytopes
status: complete
priority: high
description: Research and prepare the category-spec integration path for polytopes.
successCriteria:
- Identify the mathematical definition and the intended project vocabulary for this
  category.
- Survey relevant Sage or backend surfaces and local category-spec dependencies.
- Determine how this category relates to existing planned categories, constructors,
  Hom/End/Aut objects, and representative examples with category obligations.
- List downstream categories or tasks blocked by this integration.
- Create any concrete follow-up decision, spec, implementation, or source-curation
  cards needed to proceed.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-GEOMETRIC-SOURCE-ADMISSION
- PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH
---
# Research category integration for polytopes

## Summary

Research and prepare the category-spec integration path for polytopes.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating polytopes.

Checked sources:

- Sage polyhedron constructor docs:
  https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/constructor.html
- Sage lattice and reflexive polytope docs:
  https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/lattice_polytope.html
- Sage PALP package docs:
  https://doc.sagemath.org/html/en/reference/spkg/palp.html
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/polyhedra.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/constructor.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/parent.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/base.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/base0.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/base2.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/base_ZZ.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/base7.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/lattice_polytope.py`
- Local category-spec surface:
  `category_specs/types.py`
- Local lattice spec surface:
  `category_specs/modules/subcategories/integer_lattices.py`
- Local backend-routing memory:
  `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing`

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Source Admission

The category-spec surface should admit polyhedra first and polytopes as the bounded
subcategory. Sage's written docs define a polyhedron as a convex, possibly unbounded,
subset of Euclidean space cut out by finitely many linear inequalities and equations,
with equivalent H-representation and V-representation data. Sage explicitly defines a
polytope as a bounded polyhedron. The project vocabulary should therefore use:

- `Polyhedra(R, n)` or `Polyhedra(R).AmbientDimension(n)` for polyhedral subsets of a
  free `R`-module or vector space with finite H/V presentation;
- `Polytopes(R, n)` as the compact/bounded subcategory of `Polyhedra(R, n)`;
- `LatticePolytopes(n)` or `Polytopes(ZZ, n).Lattice()` for bounded polyhedra whose
  vertices are integral with respect to the chosen lattice;
- `ReflexivePolytopes(n)` as the lattice-polytope refinement whose polar is again a
  lattice polytope, with the origin/interior-point hypotheses made explicit;
- `PolytopeFace`, `Facet`, `Vertex`, `Ray`, `Line`, `Inequality`, and `Equation` as
  representation or face data, not disconnected root objects.

Do not make `Polytopes()` the root owner for unbounded polyhedral methods. Unbounded
polyhedra have rays and lines, and Sage warns that V-representation "vertices" may be
anchoring data rather than actual zero-dimensional faces when lines are present. That
nuance must survive in docstrings and optional diagnostic warnings.

## Sage Surface Survey

Sage already has a substantial polyhedral computation surface:

- `sage.geometry.polyhedron.constructor.Polyhedron(...)` accepts V-representation
  data (`vertices`, `rays`, `lines`) and H-representation data (`ieqs`, `eqns`), chooses
  a base ring/backend when possible, and minimizes redundant representation data.
- `sage.geometry.polyhedron.parent.Polyhedra(...)` constructs parent objects in fixed
  ambient dimension and base ring. Its backends include PPL, cdd, Normaliz, polymake,
  a generic field backend, and number-field handling where supported.
- Sage's category `PolyhedralSets(R)` is broad implementation evidence, but its current
  supercategories are additive/commutative magma surfaces. The project should not copy
  that as mathematical ownership for all methods; it should place convex-geometric
  operations on polyhedron/polytope categories.
- `Polyhedron_base0` owns basic representation and boundedness methods:
  `is_compact()`, `Hrepresentation()`, `Vrepresentation()`, `vertices()`,
  `vertices_list()`, `rays()`, `rays_list()`, `lines()`, `lines_list()`,
  inequalities, equations, and their generators.
- `Polyhedron_base` owns fan bridges such as `normal_fan()` and `face_fan()`, with
  rational, compact, full-dimensional, and interior-origin restrictions depending on
  the method.
- `Polyhedron_base2`, `Polyhedron_QQ`, and `Polyhedron_ZZ` own lattice-point and
  Ehrhart-style methods such as `is_lattice_polytope()`, `lattice_polytope()`,
  `integral_points()`, `integral_points_count()`, `ehrhart_polynomial()`, and
  `ehrhart_quasipolynomial()`, with compactness, rationality/integrality, backend, and
  lattice hypotheses.
- `Polyhedron_base7` owns triangulation and volume methods, with backend-specific
  routes through internal algorithms, TOPCOM, Normaliz, lrs, and LattE.
- `sage.geometry.lattice_polytope` supplies the older PALP-backed lattice/reflexive
  polytope surface, including reflexive-polytope databases and toric complete
  intersection context.
- The current local category-spec type surface only aliases `Polyhedron = SageParent`;
  this is a placeholder, not an adequate mathematical type surface.

Inference: Sage gives strong implementation evidence and backend routes, but the
project spec should normalize the mathematical owner hierarchy around
`Polyhedra -> Polytopes -> LatticePolytopes -> ReflexivePolytopes`, not around the
single Sage `Polyhedron` class or around backend availability.

## Method Ownership Guidance

Admit these owner directions for future spec rows:

- H/V representation methods, representation-object iteration, ambient dimension,
  dimension, containment, affine hull, faces, face lattice, facets, vertices, rays,
  lines, inequalities, and equations are owned by `Polyhedra(R, n)`.
- `is_compact()` or `is_bounded()` is a predicate on `Polyhedra(R, n)`.
  `Polytopes(R, n)` is the bounded subcategory selected by that predicate.
- `vertices()` has a surprise condition on unbounded polyhedra with lines: Sage's
  V-representation vertices may not coincide with zero-dimensional faces. Any spec
  docstring for this surface should say when the global category diagnostic logger
  may warn about this distinction.
- `normal_fan()` is owned by compact full-dimensional rational polytopes, returning a
  rational polyhedral fan. It should not be placed on arbitrary polyhedra or on
  non-rational exact polyhedra without a separate source-backed extension.
- `face_fan()` is owned by rational polytopes containing the origin as an interior
  point, returning a rational polyhedral fan.
- `polar()` is owned by full-dimensional polytopes with the required interior-origin
  or IP-property hypotheses. Reflexive-polytopes add the condition that the polar is
  again a lattice polytope.
- `integral_points()` and `integral_points_count()` belong to compact polyhedra after a
  lattice in the ambient space is specified. The `ZZ`/rational lattice-polytope
  refinements are the normal owners for exact project specs.
- `ehrhart_polynomial()` belongs to lattice polytopes. Rational polytopes should own
  `ehrhart_quasipolynomial()` or an explicitly named rational-polytope Ehrhart surface.
- `volume()` belongs to polytopes, with the measure convention (`ambient`, `induced`,
  `induced_rational`, `induced_lattice`) represented as named mathematical choices,
  not an untyped option bag.
- `triangulate()` belongs to polytopes or point-configuration-backed refinements, with
  fine/regular/star conditions represented as explicit named arguments.
- Toric bridges such as normal fans, face fans, reflexive polytopes, PALP data,
  lattice-point enumeration, and Hodge-data routes are bridge surfaces into fan, toric
  variety, and lattice categories; they do not create a special "toric lattice" type.

## Dependency And Downstream Routing

The polytope surface depends on free-module/vector-space vocabulary, finite
presentations of convex subsets, ordered finite families for representation objects,
face-poset vocabulary, lattice ambient spaces, rational polyhedral fans, and backend
routing for Normaliz, LattE, TOPCOM, lrs, cdd/PPL, polymake, and PALP.

Downstream work informed by this admission:

- The existing 2D polyhedra/polytope card should treat polygons as 2-dimensional
  polytopes and must not conflate all 2D polyhedra with bounded polygons.
- Poset `order_polytope()` and `chain_polytope()` should be source constructions whose
  codomain is a polytope object; their combinatorial source owner remains finite
  posets.
- Lattice `voronoi_cell()` may return a polyhedron/polytope object, but lattice
  methods do not own the polytope codomain's face, volume, or Ehrhart API.
- Toric-variety cards may use lattice/reflexive polytopes and normal fans as inputs,
  but toric origin does not change the underlying module/lattice/polytope category.
- Category-spec types need a real `Polyhedron`/`Polytope` type surface before
  implementation cards should expose polyhedral return values beyond the temporary
  `SageParent` alias.

No new decision card is needed from this pass. The remaining concrete follow-up is to
execute the existing 2D polyhedra/polytope source-admission card with the boundedness
distinction recorded here, then convert the admitted method ownership into the global
literal method inventory/spec surface.

## Representative Examples And Implementation Guidance

Future category-obligation examples should use very small examples: a segment, triangle, square, one
unbounded cone or half-plane, and one lattice square. Category-obligation checks should cover
category membership, compactness, H/V representations, faces, a normal fan only under
the rational/full-dimensional/compact hypotheses, and a lattice-point or Ehrhart call
only for a compact lattice polytope with an available backend.

Spec docstrings should identify user-surprise diagnostic sites for:

- V-representation vertices on unbounded polyhedra with lines;
- floating-point/RDF polyhedra where exactness is lost;
- backend-specific methods such as Normaliz, LattE, TOPCOM, lrs, cdd/PPL, polymake,
  and PALP;
- normal-fan, face-fan, polar, Ehrhart, and volume conventions whose hypotheses are
  stricter than "any polyhedron".

## Acceptance Criteria

- [x] Identify the mathematical definition and the intended project vocabulary for this category.
- [x] Survey relevant Sage or backend surfaces and local category-spec dependencies.
- [x] Determine how this category relates to existing planned categories, constructors, Hom/End/Aut objects, and representative examples with category obligations.
- [x] List downstream categories or tasks blocked by this integration.
- [x] Create any concrete follow-up decision, spec, implementation, or source-curation cards needed to proceed.

## Dependencies And Boundaries

This is a research/planning card, not an implementation card. Do not write category code or specs until the vocabulary, ownership boundaries, and dependencies are clear or an approved plan delegates that work.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for polytopes, recording
  `Polyhedra -> Polytopes -> LatticePolytopes -> ReflexivePolytopes`, Sage
  H/V-representation and backend evidence, diagnostic surprise sites, and downstream
  routing for 2D polygons, poset polytopes, lattice Voronoi cells, and toric bridges.

## Review Log

### Review 2026-05-06 (Confucius)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness
**Gates failed:** Gate 6 Style and Compliance under the then-current commit-history interpretation
**Outcome:** re-reviewed after review-kernel scope clarification

#### Gate 6 Finding: Commit-History Scope

- The first review found no mathematical or acceptance defect. It reported only
  historical `User-initiated Checkpoint` commits `c827bf9` and `769c718`, already
  ancestors of `origin/main`, as nonconforming commit messages touching this card.
  Review-kernel commit `a38ae53` clarified that such historical human checkpoints are
  provenance, not per-card Gate 6 failures, unless their content introduced a
  substantive defect covered by a review gate.

### Re-review 2026-05-06 (Heisenberg)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, Gate 3 Spec-Weakening, Gate 4 Gradient, Gate 5 Mathematical Correctness, Gate 6 Style and Compliance
**Gates failed:** none
**Outcome:** independent re-review passed Gates 1-6; human approval still required before completion

#### Residual Risks

- This is source admission, not a final method spec. Future work still needs full
  method signatures and codomains, exact backend availability checks, and conversion
  into the global method inventory/spec surface.

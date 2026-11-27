---
id: TASK-INTEGRATE-POLYHEDRA-2D-POLYTOPES-CATEGORY
trackerStatus:
  type: task
parents:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
dependsOn:
- '[[TASK-INTEGRATE-POLYTOPES-CATEGORY]]'
title: Research category integration for 2D polyhedra and polytopes
status: complete
priority: high
description: Research and prepare the category-spec integration path for polyhedra, specifically
  2D polyhedra, polygons, and lattice polygon refinements.
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
# Research category integration for 2D polyhedra and polytopes

## Summary

Research and prepare the category-spec integration path for 2D polyhedra, polygons,
and lattice polygon refinements.

## Source Provenance

Created from user directive on 2026-05-03: add high-priority todo cards for integrating polyhedra, specifically 2d polytopes.

Checked sources:

- `TASK-INTEGRATE-POLYTOPES-CATEGORY`: source admission for
  `Polyhedra -> Polytopes -> LatticePolytopes -> ReflexivePolytopes`.
- Sage polyhedron constructor docs:
  https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/constructor.html
- Sage polyhedra quick reference:
  https://doc.sagemath.org/html/en/thematic_tutorials/geometry/polyhedra_quickref.html
- Sage quick tutorial for polytopes:
  https://doc.sagemath.org/html/en/thematic_tutorials/geometry/polyhedra_quicktutorial.html
- Sage PPL lattice polygon docs:
  https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/ppl_lattice_polygon.html
- Sage lattice and reflexive polytope docs:
  https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/lattice_polytope.html
- Sage toric Weierstrass docs for 16 reflexive polygons:
  https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/toric/weierstrass.html
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/ppl_lattice_polygon.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/ppl_lattice_polytope.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/polyhedron/constructor.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/lattice_polytope.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/toric/weierstrass.py`
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/geometry/newton_polygon.py`

## Context

This is high-priority because specced vocabulary and mathematically correct foundations control downstream work. The card should establish definitions, Sage/backend surfaces, dependency relationships, and whether the work needs a plan, decision, spec card, implementation card, or research source curation before execution.

## Source Admission

This card should not admit a category called "polyhedra as 2D polytopes." A
2-dimensional polyhedron can be unbounded: cones, half-planes, strips, and the whole
ambient plane are 2D polyhedra but not polytopes. The correct category refinement is:

- `Polyhedra(R, 2)` for polyhedral subsets of a 2-dimensional free `R`-module or
  vector space;
- `Polytopes(R, 2)` for bounded 2D polyhedra;
- `Polygons(R)` as the conventional synonym for full-dimensional 2D polytopes;
- `DegeneratePolygons(R)` or a documented subcase of `Polytopes(R, 2)` for bounded
  polyhedra of affine dimension 0 or 1 in a 2D ambient space, when algorithms choose
  to support them;
- `LatticePolygons` for polygon objects whose vertices lie in the chosen lattice;
- `ReflexivePolygons` for 2D reflexive lattice polytopes, with the polar/reflexive
  hypotheses inherited from `ReflexivePolytopes`.

The public spec should prefer `Polygon` only when boundedness and the 2D/full
affine-dimension convention is clear. It should use `Polyhedron` for unbounded 2D
objects and `LatticePolygon` for PPL/PALP-backed lattice polygon algorithms.

## Sage Surface Survey

Sage has both general 2D polyhedron support and a specialized lattice-polygon layer:

- General 2D polyhedra are ordinary `Polyhedron` objects with ambient dimension 2.
  They may be bounded polygons, unbounded cones, strips, half-planes, lines, or empty
  polyhedra.
- Sage's quick tutorial constructs 2D polytopes with `Polyhedron(vertices=...)` and
  shows polar-dual conventions that differ by base ring; these are diagnostic-worthy
  API nuances, not category ownership changes.
- The PPL lattice polygon source says `LatticePolygon_PPL_class` is used in ambient
  dimension 2 or less. It includes 2-dimensional polytopes and degenerate 0- and
  1-dimensional lattice polygons.
- `ordered_vertices()` is the main polygon-specific method: it returns vertices in
  cyclic boundary order, with arbitrary first point, and returns the ordinary vertex
  tuple in affine dimension below 2.
- PPL lattice polygons also expose lattice isomorphism searches through
  `find_isomorphism()` and `is_isomorphic()`, returning or testing lattice Euclidean
  group elements.
- Sage's lattice/reflexive polytope module records that there are 16 reflexive
  polygons in dimension 2 and provides `ReflexivePolytope(2, n)` and
  `ReflexivePolytopes(2)`.
- Sage toric Weierstrass code uses the 16 reflexive polygons as toric Fano surfaces
  whose anticanonical hypersurfaces give toric elliptic curves. This is a toric bridge
  from reflexive polygons to toric geometry, not extra structure on all polygons.
- `sage.geometry.newton_polygon` implements finite and infinite Newton polygons. A
  Newton polygon is a source construction from valuation/polynomial data and may be
  unbounded; it should map into the polyhedron/polygon hierarchy rather than own the
  general polygon API.

Inference: the category-spec layer needs a local 2D refinement because cyclic ordering,
polygon isomorphism, reflexive-polygon databases, and toric elliptic-curve bridges are
genuinely 2D/lattice-specific. It must still inherit from the general polyhedron and
polytope surfaces rather than duplicating them.

## Method Ownership Guidance

Admit these owner directions for future spec rows:

- H/V representation, faces, facets, rays, lines, containment, compactness, affine
  dimension, and ordinary polyhedral transformations remain owned by
  `Polyhedra(R, 2)` or the general `Polyhedra(R, n)` surface.
- `Polygons(R)` owns full-dimensional bounded 2D-polytope conveniences such as cyclic
  boundary order, oriented edge traversal, polygon edge list, area conventions, and
  polygon-specific visual/smoke examples.
- `ordered_vertices()` belongs to `LatticePolygons` or a stricter
  cyclically-oriented polygon refinement, not to arbitrary unbounded 2D polyhedra.
  A docstring should say that the first vertex is arbitrary and that degenerate
  polygons return the ordinary vertex tuple.
- `find_isomorphism()` and `is_isomorphic()` for lattice polygons belong to
  `LatticePolygons`, with codomain/data in the lattice Euclidean group or lattice
  automorphism/Hom surfaces. Do not expose these as raw matrix searches.
- `ReflexivePolygons` owns access to the 16 two-dimensional reflexive polygon classes
  and their polar/fan/toric bridge data.
- `normal_fan()` and `face_fan()` stay on the rational/full-dimensional/origin-aware
  polytope surfaces admitted in the polytope card; reflexive polygons are a major
  source of examples, not the owner of the fan API.
- `NewtonPolygon` constructors belong to polynomial/valuation source surfaces. Their
  codomain is a finite or infinite 2D polyhedral object with slope/valuation
  conventions recorded separately.

## Dependency And Downstream Routing

This admission depends on the general polytope source-admission card. It also depends
on lattice objects, lattice Euclidean group/Hom vocabulary, rational fan surfaces,
toric-variety bridges, and polynomial/valuation source constructors for Newton
polygons.

Downstream work informed by this admission:

- Toric surface and elliptic-curve cards can use the 16 reflexive polygons as
  source-backed toric inputs, but this does not make all polygons toric objects.
- Poset order/chain polytopes in dimension 2 are still finite-poset source
  constructions returning polygon objects; the finite-poset method owner does not own
  polygon methods.
- Lattice Voronoi cells in dimension 2 may return polygons, but lattice code owns only
  the source construction and the polygon surface owns cyclic order, faces, volume,
  and lattice-point APIs.
- Newton polygon work must distinguish finite Newton polygons from infinite Newton
  polygons with a last slope; the latter are unbounded polyhedra, not polytopes.

No new decision card is needed from this pass. The admitted distinction is concrete
enough for the global method inventory/spec pass: use `Polyhedra(R, 2)` for unbounded
2D polyhedra, `Polygons(R)` for bounded full-dimensional 2D polytopes, and
`LatticePolygons`/`ReflexivePolygons` for lattice and toric-reflexive refinements.

## Smoke And Implementation Guidance

Future 2D smokes should be tiny:

- a triangle or square as a bounded polygon;
- a half-plane or cone as a 2D unbounded polyhedron;
- a segment or point as a degenerate bounded 2D-ambient polytope;
- one lattice square for `ordered_vertices()`;
- one `ReflexivePolytope(2, 0)` or equivalent minimal reflexive polygon only for
  reflexive/toric bridge smokes.

Spec docstrings should identify diagnostic-warning sites for:

- attempting polygon-only methods such as cyclic vertex order on unbounded 2D
  polyhedra;
- arbitrary choice of first vertex in cyclic order;
- degenerate 0- or 1-dimensional polygons in a 2D ambient space;
- polar-dual conventions that depend on base ring and origin/interior hypotheses;
- Newton polygons that are infinite/unbounded despite using the word "polygon."

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

**Gate 1 — Definition Grounding:** Sage polyhedra docs, OSCAR polymake/Normaliz backend docs, local category-spec dependencies.
**Gate 2 — Acceptance Criteria:** [x] All 5 ACs checked. Definition, survey, relationships, downstream list, and follow-up cards completed.
**Gate 3-6:** No issues. Correctly distinguishes 2D polytope refinements from general polyhedra. Correct caveats for degenerate polygons, polar-dual conventions, and Newton polygons.

---

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.
- 2026-05-06: Completed source-admission research for 2D polyhedra and polytopes,
  correcting the title-level conflation between unbounded 2D polyhedra and bounded
  polygons, and recording polygon/lattice-polygon/reflexive-polygon method ownership,
  Sage PPL evidence, toric-reflexive bridge routing, and diagnostic surprise sites.
- 2026-05-06: Added explicit DAG prerequisite edges for source-admission substrate dependencies. These are sequencing edges, not blockers; the card should wait until the prerequisite source cards are accepted.

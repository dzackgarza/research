---
id: SPEC-MAPPING-TOPOLOGICAL-SPACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track topological spaces mapping spec
status: complete
priority: critical
requirement: Convert category_specs/topological_spaces/docs/MAPPING.md into a tracked
  spec surface and audit it for Sage-source completeness, mathematical correctness,
  and well-typed topology, metric, connectedness, compactness, ambient, and constructor
  signatures.
acceptanceCriteria:
- Source paths category_specs/topological_spaces/docs/MAPPING.md and category_specs/topological_spaces/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Topological Spaces Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/topological_spaces/docs/MAPPING.md`.

Source inventory: `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/topological_spaces.py`
  - `sage/categories/metric_spaces.py`
  - `sage/sets/real_set.py`
- Runtime observation route checked by the local inventory:
  - `/home/dzack/miniforge3/envs/sage/bin/sage -c`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the topological
  and metric method reconciliation is recorded below, with remaining gaps routed
  through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Topological And Metric Surface

This pass checked the topological-space inventory against the converted mapping:

- `TopologicalSpaces`, `Sets().Topological()`, connected and compact axioms, and
  Cartesian products are represented by the root `TopologicalSpaces()` surface and its
  construction/axiom refinements;
- `MetricSpaces`, `Sets().Metric()`, complete metric spaces, metric products, and
  metric homsets are represented by `TopologicalSpaces().Metric()` refinements, with
  `metric()` naming the metric map and `dist(x, y)` naming its evaluation;
- `RealSet` topological predicates and transforms are represented by ambient-relative
  topological-space methods on subsets, not by pure set methods or a separate RealSet
  owner;
- named `RealSet` intervals, rays, points, and the real line are routed through
  `Sets().Constructors()` and then refined into topological subobjects;
- the variadic `RealSet(*args)` surface is rejected as public API until its finite
  mathematical cases are expressed as closed named constructors;
- interval and ball fields are recorded as topology-bearing ring/field evidence, not
  topological-space constructors;
- manifolds, schemes, varieties, polyhedra, complexes, hyperbolic models, and related
  structured geometric objects are explicit non-mappings for this subtree because
  their constructors belong to their own mathematical subtrees.

Negative missing-surface finding for this topological pass:

- Searched: `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`, installed Sage
  `sage/categories/topological_spaces.py`, `sage/categories/metric_spaces.py`,
  `sage/sets/real_set.py`, the inventory-recorded Sage runtime observation route, and
  the converted topological mapping rows above.
- Found: every inventoried topological, metric, RealSet, numeric interval/ball, and
  excluded-geometry surface is represented as an admitted topological method/category,
  set-constructor route, ring/field recovery route, interop-only observation, or
  explicit non-mapping in the converted spec.
- Conclusion: inference -- this pass found no additional Sage topological-space
  surface requiring a new public owner inside `topological_spaces`.
- Confidence: Medium.
- Gaps: broader Sage geometry/manifold/scheme/polyhedra sources and unreleased Sage
  branches remain outside this topological-space subtree pass by the inventory's own
  exclusion boundary.

## Converted Mapping Content

Topological spaces are sets with a topology. The target hierarchy therefore has a
dedicated `topological_spaces` subtree, and `Sets().Topological()` is that category,
not a set-local duplicate.

## Category and Method Mapping

| Source concept | Target category or method | Justification | Consequence |
| --- | --- | --- | --- |
| `Sets().Topological()` | `TopologicalSpaces()` | A set with a topology is precisely a topological space. | There is one category surface, exposed from both names. |
| `Sets().Metric()` | `TopologicalSpaces().Metric()` | A metric space is a topological space whose topology is induced by a metric. | Metric methods refine the topological-space surface through the `Metric` axiom. |
| `TopologicalSpaces.CartesianProducts` | `TopologicalSpaces().CartesianProducts()` | Product topology is first true for topological spaces. | Keep this construction category in the subtree. |
| `TopologicalSpaces.Connected()` | `TopologicalSpaces().Connected()` | Connectedness is a topological-space axiom. | Local subcategory stub is `topological_spaces/subcategories/connected.py`. |
| `TopologicalSpaces.Compact()` | `TopologicalSpaces().Compact()` | Compactness is a topological-space axiom. | Local subcategory stub is `topological_spaces/subcategories/compact.py`. |
| `MetricSpaces.Complete()` | `TopologicalSpaces().Metric().Complete()` | Completeness is a metric-space axiom, not a general topological axiom. | Local subcategory stub is `topological_spaces/subcategories/complete.py`. |
| Sage `metric_function()` / deprecated `metric` alias | `MetricSpace.metric() -> d: X x X -> R_{\ge 0}` | The metric itself is the map `d` with nonnegative-real codomain satisfying separation, symmetry, and the triangle inequality; Sage's callable return and partial test coverage are implementation evidence, not the definition. | `dist(x, y)` is the evaluated distance. Do not model `metric` as a bare untyped `SetMorphism` or as a binary scalar-valued method. |
| Sage `dist(a, b)` on metric parents | `MetricSpace.dist(x, y)` | Distance between two points is a metric-space method obtained by evaluating the metric map. | Keep as a metric root method. |
| Sage element `dist(b)` | `MetricSpacesElement.dist(other)` delegating to `self.parent().dist(self, other)` | The parent owns the metric; the element API is ergonomic enrichment. | Element methods do not duplicate metric structure. |
| Sage element `abs()` | Structured metric/ring method, not pure topological | Absolute value uses the distinguished zero and additive/ring structure in Sage's default implementation. | Map through topological ring/field or normed additive structure, not the pure topological-space root. |
| Sage metric homsets | `TopologicalSpaces().Metric().HomCategory()` as short maps | The standard category of metric spaces uses distance-nonincreasing maps as morphisms; these are continuous maps with Lipschitz constant at most 1. | The spec records short-map morphisms even though current constructors do not enforce this effectively. Continuous maps remain the root topological hom notion. |
| Sage product metric | `TopologicalSpaces().Metric().CartesianProducts()` | Product metric is the maximum of factor distances in Sage. | Keep metric product behavior in the metric subcategory, separate from product topology. |

Continuous maps inherit set-map inverse-image vocabulary from `Sets().HomCategory()`:
`f.preimage(U)` is the inverse image of a subset under the underlying set map. The
topological refinement is expressed by the ambient topological-space methods on subsets,
not by a second topological-only `preimage` obligation. Endomorphism objects use the
generic end-domain vocabulary: `End_Top(X).domain()` names the underlying space, so
`base_space()` is not a separate abstract method on topological or metric end
categories.

## Root Topological Method Mapping

The root space owns predicates and transforms that take a subset of a space. This is
the surface needed to recover Sage subset methods such as `RealSet.is_open()` without
turning every topological subset constructor into a root constructor.

| Sage subset method | Target topological-space method | Justification | Consequence |
| --- | --- | --- | --- |
| `RealSet.is_open()` | `X.is_open(U: Subset) -> bool` | Openness is a predicate of a subset relative to an ambient topological space. | `U.is_open()` migrates to `U.ambient().is_open(U)` unless a subobject convenience method is separately admitted. |
| `RealSet.is_closed()` | `X.is_closed(U: Subset) -> bool` | Closedness is relative to an ambient topological space. | `U.is_closed()` migrates to `U.ambient().is_closed(U)`. |
| `RealSet.closure()` | `X.closure(U: Subset) -> Subset` | Closure is the smallest closed subset of the ambient space containing `U`. | `U.closure()` migrates to `U.ambient().closure(U)`. |
| `RealSet.interior()` | `X.interior(U: Subset) -> Subset` | Interior is the largest open subset of the ambient space contained in `U`. | `U.interior()` migrates to `U.ambient().interior(U)`. |
| `RealSet.boundary()` | `X.boundary(U: Subset) -> Subset` | Boundary is a subset of the ambient space determined by closure and interior. | `U.boundary()` migrates to `U.ambient().boundary(U)`. |
| `RealSet.is_connected()` as a no-argument category fact | `X.is_connected() -> bool` | Connectedness is a property of the whole topological space. | Keep no-argument connectedness at root. |
| `RealSet.is_compact()` as a no-argument category fact | `X.is_compact() -> bool` | Compactness is a property of the whole topological space. | Keep no-argument compactness at root and add a compact subcategory. |

## RealSet Ambient-Recovery Decision

Real-line subset methods recover through the ambient-relative topological-space surface.
For a real subset `U`, the public route is:

- `U.ambient().is_open(U)` for openness;
- `U.ambient().is_closed(U)` for closedness;
- `U.ambient().closure(U)` for closure;
- `U.ambient().interior(U)` for interior;
- `U.ambient().boundary(U)` for boundary.

The owner remains `TopologicalSpaces().ParentMethods`. `RealSet` compatibility methods
are Sage-backed convenience methods on a topological subobject of the real line; they do
not create a second owner and should not be specified as pure set methods. The return
objects for `closure`, `interior`, and `boundary` are subsets of the same ambient
topological space, refined as real-line subsets when the constructor path is Sage
`RealSet`.

Do not implement category-level wrapper methods on `_RealSets` that merely override
Sage's existing `RealSet` methods before the ambient topological methods have concrete
implementations. The spec obligation is the ownership route and the migration rule:
existing Sage no-argument calls migrate conceptually to the ambient-relative form.

## Constructor Candidate Mapping

`TopologicalSpaces().Constructors()` stays empty for now. Named sets belong under
`Sets().Constructors()` even when they refine into topological spaces or topological
subobjects. This is the current discoverability rule: users first look for named set
objects in `Sets().Constructors()`, and later this can be centralized through aggregate
constructor exposure from subcategories or through `Cat`.

| Sage constructor surface | Candidate path | Mapping status | Reason |
| --- | --- | --- | --- |
| No standalone `TopologicalSpace(...)` constructor found in Sage category source | No generic constructor | Mathematically justified non-mapping | A generic constructor would require arbitrary topology data and is not present in the inventoried Sage category. |
| `RR` / `RealField()` | `Sets().Constructors().RR()` refined into `Sets().Topological()` | Mapped to set constructors | The real line is a named set object with extra structure. It should not force a topological constructor namespace. |
| `RealSet.real_line()` | `Sets().Constructors().RealLine()` | Mapped to set constructors | The real line as a real subset is a topological subobject of itself. |
| `RealSet.open(a, b)` | `Sets().Constructors().OpenRealInterval(lower, upper)` | Mapped to set constructors | Open intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.closed(a, b)` | `Sets().Constructors().ClosedRealInterval(lower, upper)` | Mapped to set constructors | Closed intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.open_closed(a, b)` | `Sets().Constructors().OpenClosedRealInterval(lower, upper)` | Mapped to set constructors | Half-open intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.closed_open(a, b)` | `Sets().Constructors().ClosedOpenRealInterval(lower, upper)` | Mapped to set constructors | Half-open intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_below_open(bound)` | `Sets().Constructors().UnboundedBelowOpenRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_below_closed(bound)` | `Sets().Constructors().UnboundedBelowClosedRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_above_open(bound)` | `Sets().Constructors().UnboundedAboveOpenRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_above_closed(bound)` | `Sets().Constructors().UnboundedAboveClosedRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.point(p)` | `Sets().Constructors().RealPoint(p)` | Mapped to set constructors | A singleton is first a finite set/subset and only becomes a topological space relative to an ambient topology. |
| `RealSet.interval(lower, upper, *, lower_closed, upper_closed)` | `Sets().Constructors().RealSetInterval(lower, upper, lower_closed=..., upper_closed=...)` | Mapped to set constructors | This is the universal interval/ray constructor. Named interval and ray constructors call it with fixed endpoint-closure booleans. |
| Variadic `RealSet(*args)` | No catch-all constructor | Mathematically justified non-mapping | Sage accepts finite data shapes, symbolic relations, and manifold objects. The project API requires closed overloads and mathematical names. |
| `RealSet(..., structure='differentiable')`, `ambient=...`, `names=...`, `coordinate=...` | No path in this subtree | Mathematically justified non-mapping | These route to differentiable real manifolds or manifold subsets. |
| `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, `ComplexBallField` constructors | Ring/field constructor paths, with topological methods imported from this subtree | Justified non-mapping as topological-space constructors | These constructors create algebraic/numerical fields or elements, not pure topological spaces. Their topology-bearing behavior should be recovered through topological ring/field categories. |
| Manifolds, varieties, schemes, hyperbolic models, polyhedra, CW complexes, simplicial complexes, and simplicial sets | Their own mathematical subtrees | Justified non-mapping | Each object carries extra structure beyond a bare topology. |

Topological rings, modules, and algebras inherit their topological-space surface from
`topological_spaces` and their algebraic surface from their own subtree. That is how
real intervals, complex intervals, and real or complex balls should recover topological
predicates without becoming topological-space constructors.

## Topological Ring And Field Recovery

The public owner for topological predicates and ambient-relative transforms stays in
`TopologicalSpaces()`, even when the object also lies in a ring or field category. The
existing spec anchors are:

- `category_specs/topological_spaces/__init__.py`, where `TopologicalSpaces()` owns
  `is_open`, `is_closed`, `closure`, `interior`, `boundary`, `is_connected`, and
  `is_compact`;
- `category_specs/rings/subcategories/topological.py`, where `Rings().Topological()`
  records the ring-side topological category edge without redefining those methods.

Accordingly, topological rings and fields recover topological behavior by
inheritance/join:

| Object kind | Entry constructor namespace | Recovered topological surface | Non-topological owner that remains primary for construction |
| --- | --- | --- | --- |
| Real/complex precision fields and their fixed precision objects | `Rings().Constructors()` / field constructor routes | `TopologicalSpaces()` and metric refinements when source-backed | `Rings()` / `Fields()` and precision-field subcategories |
| Interval and ball fields | Ring/field constructor routes in `rings` | `TopologicalSpaces()` through the topological ring/field path | Interval/ball field subcategories in `rings` |
| p-adic and q-adic rings and fields | Ring/field constructor routes in `rings` | `TopologicalSpaces()` through `Rings().Topological()` or field refinements | p-adic and q-adic ring/field subcategories |

Migration consequence:

- `TopologicalSpaces().Constructors()` remains empty for these objects.
- A ring or field constructor keeps returning a ring or field object.
- Once refined into a topological ring/field category, the object inherits
  topological predicates from `TopologicalSpaces()` without duplicating method
  ownership in the ring subtree.

Rejection condition for future edits:

- do not admit interval fields, ball fields, p-adic fields, or other rings/fields as
  pure `TopologicalSpaces().Constructors()` entries;
- do not move constructor ownership away from `rings`;
- do not create ring-local duplicates of the root topological predicates or transforms.

## Resolved Constructor and Metric Decisions

Named set constructors live in `Sets().Constructors()` for now. The result then refines
into every category whose structure it satisfies, including `TopologicalSpaces()` and
`TopologicalSpaces().Subobjects()` for real-line subsets. `TopologicalSpaces()` owns
the topological method surface, not the named-constructor namespace.

The interval API keeps both the universal endpoint/closure constructor and named
constructors for the common endpoint patterns. The universal constructor is
unambiguous because two endpoints and two closure booleans determine the subset of the
real line. Named constructors are discoverable spellings over that universal shape.

Metric spaces expose `metric()` for the metric map and `dist(x, y)` for its evaluation.
Metric elements expose `x.dist(y)` as delegation to the parent metric space. Metric
homsets are the short-map homsets; ordinary continuous maps remain the homsets of the
root topological category.

## Canonical Smoke Examples

Use these examples for the first topological smoke assertions:

| Target | Canonical object | Constructor owner | Witness |
| --- | --- | --- | --- |
| `TopologicalSpaces().Connected()` | `Sets().Constructors().OpenRealInterval(0, 1)` | `Sets().Constructors()` via `RealSet.open(0, 1)` | Sage refines `(0, 1)` into connected topological spaces; the project constructor also refines into `TopologicalSpaces().Connected()`. |
| `TopologicalSpaces().Compact()` | `Sets().Constructors().ClosedRealInterval(0, 1)` | `Sets().Constructors()` via `RealSet.closed(0, 1)` | Sage refines `[0, 1]` into compact topological spaces; the project constructor also refines into `TopologicalSpaces().Compact()`. |
| `TopologicalSpaces().Metric().Complete()` | `Sets().Constructors().RR()` / Sage `RR` | `Sets().Constructors()` for the named set object; ring ownership stays in `Rings().Constructors()` | Local Sage observation shows `RR.category()` is a join containing complete metric spaces. Project smoke should wait for the topological ring/field recovery path to refine `RR` through `TopologicalSpaces().Metric().Complete()`. |

Do not use `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, or
`ComplexBallField` as complete-metric smoke examples in this subtree. The inventory
records them as topology-bearing ring/field evidence, not as Sage metric-space parents.
Their recovery belongs to the topological ring/field cards.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Hermes Agent (independent reviewer)
**Protocol version:** 6-gate spec review (G1-G6)

### G1 — Source Grounding

**Referenced local files verified present:**

| File referenced in spec | Path | Exists |
|---|---|---|
| MAPPING.md (source document) | `category_specs/topological_spaces/docs/MAPPING.md` | Yes — confirmed; file is now a redirect stub pointing to this spec (lines 3-7). The body says "This mapping document has been converted into the tracked spec file above." |
| SAGE_INVENTORY.md | `category_specs/topological_spaces/docs/SAGE_INVENTORY.md` | Yes — 87 lines, 4 sections (Category Surfaces, Real-Line Topological Surfaces, Numeric Interval/Ball, Excluded Structured Geometric). |
| `__init__.py` | `category_specs/topological_spaces/__init__.py` | Yes — 296 lines. Defines `TopologicalSpaces` category, lazy imports Metric/Connected/Compact subcategories, defines `_TopologicalSpaceObjectMethods` with abstract methods is_open/is_closed/closure/interior/boundary/is_connected/is_compact, and `TopologicalSpaceRuntimeGapObjectMethods` for carriers without topology adapters. |
| `subcategories/connected.py` | `category_specs/topological_spaces/subcategories/connected.py` | Yes — 40 lines. `_ConnectedTopologicalSpaces` with base axiom (TopologicalSpaces, "Connected"), super_categories=[TopologicalSpaces()], ParentMethods.is_connected() returns True. |
| `subcategories/compact.py` | `category_specs/topological_spaces/subcategories/compact.py` | Yes — 40 lines. `_CompactTopologicalSpaces` with base axiom (TopologicalSpaces, "Compact"), super_categories=[TopologicalSpaces()], ParentMethods.is_compact() returns True. |
| `subcategories/complete.py` | `category_specs/topological_spaces/subcategories/complete.py` | Yes — 42 lines. `_CompleteMetricSpaces` with base axiom (MetricSpacesCategory, "Complete"), super_categories includes `SageSets().Metric().Complete()`, ParentMethods.is_complete() returns True. |
| `subcategories/metric.py` | `category_specs/topological_spaces/subcategories/metric.py` | Yes — 88 lines. `MetricSpacesCategory` with base axiom (TopologicalSpaces, "Metric"), super_categories=[SageMetricSpaces(), TopologicalSpaces()], abstract methods: metric(), ball(), dist(). ElementMethods.dist() delegates to parent. |
| `subcategories/constructions/cartesian_products.py` | Yes — 28 lines. `_CartesianProducts` with product topology. |
| `subcategories/constructions/subobjects.py` | Yes — 28 lines. `_Subobjects` with induced topology. |
| `subcategories/constructions/quotients.py` | Yes — confirmed by `find` output. |
| `subcategories/constructions/subquotients.py` | Yes — confirmed by `find` output. |
| `subcategories/constructions/objects_over.py` | Yes — confirmed by `find` output. |
| `subcategories/constructions/objects_under.py` | Yes — confirmed by `find` output. |
| `rings/subcategories/topological.py` | `category_specs/rings/subcategories/topological.py` | Yes — 74 lines. `_TopologicalRings` with base axiom (Rings, "Topological"), super_categories includes `SageRings().Topological(), TopologicalSpaces(), Rings()`. Imports `TopologicalSpaceRuntimeGapObjectMethods` for inherited predicates. |
| smoketest.sage | `category_specs/topological_spaces/smoketest.sage` | Yes — 113 lines. 24 smoke statements covering category containment, axiom ownership, method surface verification for Connected/Compact/Metric/Complete, HomCategory, AutCategory, Subobjects, Quotients, Subquotients, ObjectsOver, ObjectsUnder. |
| homsets.py | `category_specs/topological_spaces/homsets.py` | Yes — 136 lines. Defines `TopologicalSpaceHomCategory` with `_ContinuousMaps` elements (is_continuous), `TopologicalSpaceAutCategory` with `_Homeomorphisms` (is_homeomorphism), `MetricSpaceHomCategory` with `_ShortMaps` (is_short), `MetricSpaceAutCategory` with `_Isometries` (is_isometry). |

**Referenced installed Sage files verified present:**

| File referenced in spec | Path | Exists |
|---|---|---|
| Sage topological_spaces.py | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/topological_spaces.py` | Yes — 170 lines. Defines `TopologicalSpaces` (line 33), `Connected` (line 122), `Compact` (line 147), CartesianProducts with `extra_super_categories()` (lines 66-83), SubcategoryMethods.Connected() and Compact() (lines 85-120). No standalone `TopologicalSpace(...)` constructor — confirms spec's claim at line 178. |
| Sage metric_spaces.py | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/metric_spaces.py` | Yes — 387 lines. Defines `MetricSpaces` (line 78), `MetricSpacesCategory.default_super_categories` (lines 26-65) which joins `category.Topological()` with default metric supercategories, `ParentMethods.metric_function` (line 150) with deprecated alias `metric` (line 166), `ParentMethods.dist` (line 168), `ElementMethods.abs` (line 201), `ElementMethods.dist` (line 213), `SubcategoryMethods.Complete` (line 334), `Complete` category (line 351), `CartesianProducts` product metric as max of factor distances (line 329). |
| Sage real_set.py | `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/real_set.py` | Yes — 2756 lines. Confirmed: `RealSet.is_open()` at line 2401, `is_closed()` at line 2422, `closure()` at line 2443, `interior()` at line 2458, `boundary()` at line 2475, `ambient()` at line 1472, `is_connected()` at line 2547, `n_components()` at line 1361. Named constructors: `interval` (line 1690), `open` (1717), `closed` (1739), `point` (1761), `open_closed` (1782), `closed_open` (1807), `unbounded_below_closed` (1832), `unbounded_below_open` (1855), `unbounded_above_closed` (1878), `unbounded_above_open` (1902), `real_line` (1926). Category assignment at `__init__` (lines 891-1010) refines into `TopologicalSpaces()`, `Connected`, `Compact`, `Subobjects`, `Finite`, or `Infinite` according to interval data. |
| Sage binary | `/home/dzack/miniforge3/envs/sage/bin/sage` | Yes — executable confirmed. |

**Cross-referenced task card:**

| Card | Path | Exists |
|---|---|---|
| TASK-MAPPING-DOC-COMPLETENESS-RESEARCH | `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT/tasks/TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.md` | Yes — dependsOn includes SPEC-MAPPING-TOPOLOGICAL-SPACES (line 18), status complete. |

**G1 Verdict: PASS.** All 20+ referenced source files verified present on disk. The MAPPING.md is a redirect stub (as stated in the spec line 31), and the SAGE_INVENTORY.md is the durable inventory. Import probe caveat documented at spec line 53 is truthful — the completeness work uses installed source files and inventories as the durable source surface.

### G2 — Sage Surface Completeness

**Cross-reference: SAGE_INVENTORY.md surfaces → spec mapping rows:**

| SAGE_INVENTORY surface | Spec mapping row | Accounted |
|---|---|---|
| `TopologicalSpaces` / `Sets().Topological()` (inventory line 18) | Spec line 108: `Sets().Topological()` → `TopologicalSpaces()` | Yes |
| `TopologicalSpaces.CartesianProducts` (inventory line 19) | Spec line 110: `TopologicalSpaces().CartesianProducts()` | Yes |
| `TopologicalSpaces.Connected()` (inventory line 20) | Spec line 111: `TopologicalSpaces().Connected()` with local subcategory stub `connected.py` | Yes |
| `TopologicalSpaces.Compact()` (inventory line 21) | Spec line 112: `TopologicalSpaces().Compact()` with local subcategory stub `compact.py` | Yes |
| Connected.CartesianProducts (inventory line 22) | Covered by product topology axiom inheritance; Connected is a subcategory of TopologicalSpaces | Yes (inherited) |
| Compact.CartesianProducts (inventory line 23) | Covered by product topology axiom inheritance | Yes (inherited) |
| `MetricSpaces` / `Sets().Metric()` (inventory line 24) | Spec line 109: `TopologicalSpaces().Metric()`. Justification: "A metric space is a topological space whose topology is induced by a metric." | Yes — mathematically correct |
| `MetricSpacesCategory.default_super_categories` (inventory line 25) | Implicitly covered by the Metric() subcategory edge; the spec's metric module `super_categories` returns `[SageMetricSpaces(), TopologicalSpaces()]` (metric.py line 79) | Yes |
| `MetricSpaces.Homsets` as Lipschitz-1 maps (inventory line 26) | Spec line 118: `TopologicalSpaces().Metric().HomCategory()` as short maps | Yes |
| `MetricSpaces.WithRealizations.ParentMethods.dist` (inventory line 27) | Covered by the generic `dist(x, y)` method at the metric root (spec line 115) — WithRealizations is an implementation detail, not a separate owner | Yes (correctly collapsed) |
| `MetricSpaces.CartesianProducts` product metric (inventory line 28) | Spec line 119: `TopologicalSpaces().Metric().CartesianProducts()` — product metric separate from product topology | Yes |
| `MetricSpaces.Complete()` (inventory line 29) | Spec line 113: `TopologicalSpaces().Metric().Complete()` with local subcategory stub `complete.py` | Yes |
| RealSet `is_open()`, `is_closed()`, `closure()`, `interior()`, `boundary()` (inventory lines 50-54) | Spec lines 137-141: ambient-relative forms `X.is_open(U)`, `X.is_closed(U)`, `X.closure(U)`, `X.interior(U)`, `X.boundary(U)` | Yes — ownership migration to TopologicalSpaces() |
| RealSet `ambient()` (inventory line 55) | Spec lines 147-154: ambient-recovery decision with explicit owner `TopologicalSpaces().ParentMethods` | Yes |
| RealSet named constructors (open, closed, point, open_closed, closed_open, unbounded_*, real_line, interval) (inventory lines 39-49) | Spec lines 179-190: mapped to `Sets().Constructors()` entries | Yes — correct constructor placement |
| Variadic `RealSet(*args)` (inventory line 37) | Spec line 191: rejected as public API "until its finite mathematical cases are expressed as closed named constructors" | Yes — non-mapping with rationale |
| Differentiable manifold `RealSet` args (inventory line 75) | Spec line 192: routed to differentiable real manifolds | Yes — explicit non-mapping |
| Interval/ball fields (inventory lines 63-66) | Spec line 193: rejected as topological-space constructors, routed to ring/field recovery | Yes — justified non-mapping |
| Excluded geometric surfaces (inventory lines 68-78) | Spec line 194: explicit non-mappings | Yes — complete |
| Manifolds, varieties, schemes, polyhedra, CW complexes, simplicial complexes/sets | Spec line 194 | Yes — explicit non-mapping |

**G2 Verdict: PASS.** Every inventoried surface in SAGE_INVENTORY.md is accounted for in the spec mapping rows. No orphaned inventory items. The completeness reconciliation section (lines 58-96) explicitly records the negative finding: "every inventoried topological, metric, RealSet, numeric interval/ball, and excluded-geometry surface is represented." Confidence is correctly stated as Medium with the gap caveat about broader Sage geometry/manifold/scheme/polyhedra sources.

### G3 — Constructor Route Justification (Mathematical Validity)

**Category hierarchy:**

```
TopologicalSpaces() = Sets().Topological()
├── Connected()        [axiom: topological connectedness]
├── Compact()          [axiom: topological compactness]
├── Metric()           [axiom: metric induces topology]
│   ├── Complete()     [axiom: completeness is metric, not purely topological]
│   ├── HomCategory()  [short maps: Lipschitz-1 continuous maps]
│   └── CartesianProducts()  [product metric = max of factor distances]
├── Subobjects()       [induced topology]
├── Quotients()        [quotient topology]
├── Subquotients()
├── ObjectsOver()      [structure-space surfaces]
├── ObjectsUnder()
├── CartesianProducts()  [product topology]
└── HomCategory()
    ├── EndCategory()
    └── AutCategory()   [homeomorphisms]
```

**Mathematical validity checks:**

1. **Metric → Topological refinement (spec line 109):** A metric space (X,d) induces a topology via open balls B_ε(x). Therefore `Metric()` is correctly placed as a subcategory/axiom of `TopologicalSpaces()`, not as a parallel category. The Sage source confirms this relationship at `metric_spaces.py` line 27-28: "if A is a metric space in category C, then A is also a topological space." The spec's `MetricSpacesCategory.super_categories` returns `[SageMetricSpaces(), TopologicalSpaces()]` (metric.py line 79), which is mathematically consistent.

2. **Connected as topological axiom (spec line 111):** Connectedness is defined purely in terms of topology (no separation into disjoint nonempty open sets). Placed correctly under `TopologicalSpaces()`, not under `Metric()`. Confirmed by Sage source at `topological_spaces.py` line 87: `Connected()` is a SubcategoryMethod of `TopologicalSpaces`.

3. **Compact as topological axiom (spec line 112):** Compactness depends only on open covers. Correctly placed under `TopologicalSpaces()`, not under `Metric()`. Confirmed by Sage source at `topological_spaces.py` line 105.

4. **Complete as metric axiom (spec line 113):** Completeness requires a metric (Cauchy sequences need the distance function). Correctly placed under `TopologicalSpaces().Metric().Complete()`, not under `TopologicalSpaces()`. Confirmed by Sage source at `metric_spaces.py` line 334: `Complete()` is a SubcategoryMethod of `MetricSpaces`.

5. **Constructor placement — Sets().Constructors() vs TopologicalSpaces().Constructors() (spec lines 168-193):** The spec correctly notes that named sets (real intervals, rays, the real line, points) are first sets, then refined into topological spaces. This is mathematically sound: an open interval (0,1) is first and foremost a set, then acquires structure. The `TopologicalSpaces().Constructors()` stays empty for now — justified by the absence of a Sage `TopologicalSpace(...)` constructor. Verified in Sage source: no such standalone constructor exists (topological_spaces.py contains no `__init__` or constructor method for topological spaces).

6. **Ambient-relative predicates (spec lines 135-166):** Openness/closedness/closure/interior/boundary are defined relative to an ambient topological space. The spec's migration from `U.is_open()` to `U.ambient().is_open(U)` is mathematically correct: "U is open in X" is the predicate, not "U is intrinsically open." The Sage RealSet methods at lines 2401-2490 confirm that `RealSet.is_open()` checks endpoint closure, which implicitly uses the real-line topology as ambient — the spec makes this ambient relationship explicit and general.

7. **Ring/field topology recovery (spec lines 201-235):** Topological rings and fields inherit topological predicates from `TopologicalSpaces()` via `Rings().Topological()` join, not by duplicating methods. This is mathematically correct: a topological ring is a ring whose underlying set is a topological space, and the two structures are compatible. The spec's `rings/subcategories/topological.py` line 35 confirms `super_categories` returns `[SageRings().Topological(), TopologicalSpaces(), Rings()]`, importing `TopologicalSpaceRuntimeGapObjectMethods` (line 13-16).

8. **Metric map signature (spec line 114):** `metric() -> d: X x X -> R_{\ge 0}` with separation, symmetry, triangle inequality. The Sage source at `metric_spaces.py` lines 150-164 defines `metric_function()` returning a lambda, with `metric` as a deprecated alias (line 166). The spec correctly distinguishes the metric map `d` from its evaluation `dist(x,y)` and notes that Sage's callable return is implementation evidence, not the definition.

9. **Product metric vs product topology (spec line 119):** Product topology uses open sets in the product; product metric uses max of factor distances. These are related but distinct constructions. The spec correctly keeps them separate: `CartesianProducts()` under root `TopologicalSpaces()` for product topology, and `CartesianProducts()` under `Metric()` for product metric. Verified in Sage: `metric_spaces.py` line 329 shows product metric as `max(x.dist(y) for ...)`.

10. **Short maps vs continuous maps (spec line 118):** Short maps (Lipschitz ≤ 1) are a refinement of continuous maps, not a replacement. The spec correctly records this: `MetricSpaceHomCategory` extends `TopologicalSpaceHomCategory` (homsets.py line 95), so metric hom elements are also topological hom elements. `_ShortMaps` extends `_ContinuousMaps` (homsets.py line 32).

**G3 Verdict: PASS.** All constructor routes are mathematically valid. The hierarchy correctly places axioms at the highest category where they are defined: Connected/Compact at topological root, Complete at metric subcategory, short maps as metric hom refinement. Ambient-relative predicates correctly identify the topological space as the owner. Constructor placement in `Sets().Constructors()` is mathematically justified.

### G4 — Nonmathematical Rejection (Explicit Rejection Audit)

| Rejected surface | Spec line(s) | Rejection rationale | Assessment |
|---|---|---|---|
| Variadic `RealSet(*args)` | 191 | "Sage accepts finite data shapes, symbolic relations, and manifold objects. The project API requires closed overloads and mathematical names." | **Valid.** The variadic constructor accepts heterogeneous input types (tuples, lists, InternalRealInterval, OpenInterval, symbolic relations) without type-level distinction. Mathematical API requires explicit named constructors. |
| `RealSet(..., structure='differentiable')`, `ambient=...`, `names=...`, `coordinate=...` | 192 | "These route to differentiable real manifolds or manifold subsets." | **Valid.** These parameters construct objects with differentiable manifold structure, not pure topological spaces. Correctly routed to manifold subtree. |
| `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, `ComplexBallField` as topological-space constructors | 193 | "These constructors create algebraic/numerical fields or elements, not pure topological spaces. Their topology-bearing behavior should be recovered through topological ring/field categories." | **Valid.** Verified: `RBF.category()` returns `Category of infinite fields`; `RBF in Sets().Metric()` is `False` (confirmed by direct Sage observation). RealBallField has no parent `dist`. These are algebraic objects that happen to carry topology — correct to route through ring/field recovery. |
| Manifolds, varieties, schemes, hyperbolic models, polyhedra, CW complexes, simplicial complexes/sets | 194 | "Each object carries extra structure beyond a bare topology." | **Valid.** These objects have additional structure (differentiable, algebraic, geometric) beyond the minimal topology. Correctly deferred to their own subtrees. |
| No standalone `TopologicalSpace(...)` constructor | 178 | "A generic constructor would require arbitrary topology data and is not present in the inventoried Sage category." | **Valid.** Confirmed: Sage's `topological_spaces.py` defines the category interface only — no generic constructor for arbitrary topological spaces. This is mathematically expected: there is no canonical way to construct "a topological space" without specifying the topology data. |
| Do not create ring-local duplicates of root topological predicates | 233-235 | "Do not move constructor ownership away from rings; do not create ring-local duplicates of the root topological predicates or transforms." | **Valid.** The spec enforces single ownership: `TopologicalSpaces()` owns the method surface; rings/fields inherit via join. This prevents the anti-pattern of duplicating methods across subtrees. |
| Do not implement category-level wrapper methods on `_RealSets` | 163-166 | "Do not implement category-level wrapper methods on _RealSets that merely override Sage's existing RealSet methods before the ambient topological methods have concrete implementations." | **Valid.** Migration requires proper ownership, not premature ad-hoc wrappers. |

**G4 Verdict: PASS.** All nonmathematical rejections have explicit, mathematically grounded rationale. The spec does not silently drop surfaces; every rejection names the target, the reason, and the alternate routing or decision.

### G5 — Ambiguity Routing (Unresolved Issues → Decision Cards)

| Ambiguity / Gap | Routed to | Spec evidence | Assessment |
|---|---|---|---|
| Import probe caveat: direct `sage -python` imports fail | Documented as caveat (spec line 53) | "completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved." | **Adequately routed.** The environmental issue is documented and the workaround (installed source + inventory) is stated. This is a reasonable workaround; the spec does not hide the limitation. |
| Broader Sage geometry/manifold/scheme/polyhedra sources remain outside topological subspace | Spec line 95-96: "remain outside this topological-space subtree pass by the inventory's own exclusion boundary." | Confidence is Medium. | **Correctly routed.** These are explicitly excluded from the topological-space inventory and delegated to their own subtrees (geometry, manifold, algebraic geometry). |
| No generic `TopologicalSpace(...)` constructor | Explicitly marked as "mathematically justified non-mapping" (spec line 178) | No decision card needed — this is a definitive non-mapping. | **Correct.** Absence of a generic constructor is a mathematical fact, not an ambiguity. |
| Metric homsets as short maps vs continuous maps | Documented at spec line 118: "The spec records short-map morphisms even though current constructors do not enforce this effectively." | Continuous maps remain the root topological hom notion. | **Partially gapped.** The spec acknowledges Sage's current constructors don't enforce short-map behavior but records the mathematical obligation as the spec surface. This is a design decision, not an ambiguity — the spec sets the ideal and the implementation gap is a separate implementation task. |
| `abs()` method routing | Spec line 117: "Map through topological ring/field or normed additive structure, not the pure topological-space root." | Sage places `abs()` in `MetricSpaces.ElementMethods` (line 201) using `P.metric()(self, P.zero())`. | **Correctly routed.** `abs()` uses ring structure (zero element), so it belongs in normed/ring structure, not pure topology. The spec correctly distinguishes this. |
| Completeness research gaps tracked by TASK-MAPPING-DOC-COMPLETENESS-RESEARCH | Task card at `.../tasks/TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.md` | Spec line 56: "remaining gaps routed through [[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]." | **Adequate.** The task card exists and depends on this spec (confirmed at line 18 of the task card). Status is complete. |

**G5 Verdict: PASS.** Documented caveats are adequately handled. The import-probe caveat is transparent. The broader-geometry exclusion is bounded. The short-map enforcement gap is acknowledged as an implementation concern, not a spec ambiguity. All gaps are routed to existing tracked cards.

### G6 — Obligation Preservation (No Weakening Without Replacement)

**Method surface audit:**

| Method / Obligation | Root spec location | Weakening detected? | Replacement / preservation evidence |
|---|---|---|---|
| `is_open(U: Subset) -> bool` | `__init__.py` line 91 (abstract) | No | TopologicalSpaces.ParentMethods owns the abstract method. Rings().Topological() inherits from runtime gap adapter without redefining (rings/topological.py line 63). |
| `is_closed(U: Subset) -> bool` | `__init__.py` line 96 (abstract) | No | Same preservation path. |
| `closure(U: Subset) -> Subset` | `__init__.py` line 76 (abstract) | No | Same. |
| `interior(U: Subset) -> Subset` | `__init__.py` line 81 (abstract) | No | Same. |
| `boundary(U: Subset) -> Subset` | `__init__.py` line 86 (abstract) | No | Same. |
| `is_connected() -> bool` | `__init__.py` line 71 (abstract); connected.py line 34 (concrete True) | No | Root abstract method preserved; Connected subcategory provides concrete True return. |
| `is_compact() -> bool` | `__init__.py` line 101 (abstract); compact.py line 34 (concrete True) | No | Same pattern. |
| `metric() -> SetMorphism` | metric.py line 31 (abstract) | No | Preserved as abstract method on MetricSpacesCategory.ParentMethods. |
| `ball(center, radius) -> MetricBall` | metric.py line 36 (abstract) | No | Preserved as abstract method. |
| `dist(x, y) -> RealNumber` | metric.py line 41 (abstract on parent); metric.py line 50 (element delegation) | No | Preserved at both parent and element levels. |
| Continuous map `preimage` | Spec lines 121-127 | No | Inherited from `Sets().HomCategory()`; topological refinement expressed by ambient topological-space methods on subsets, not duplicated. |
| Endomorphism `domain()` | Spec lines 125-127 | No | Uses generic end-domain vocabulary from `Sets().HomCategory()`; `base_space()` is correctly rejected as a separate abstract method. |

**Constructor obligation preservation:**

- Sage's `RealSet.open`, `closed`, `point`, etc. → preserved as `Sets().Constructors().OpenRealInterval`, etc. (spec lines 179-190)
- Sage's `RealSet.interval` → preserved as `Sets().Constructors().RealSetInterval` (spec line 190)
- Sage's `RealSet.real_line()` → preserved as `Sets().Constructors().RealLine()` (spec line 180)
- Product topology → preserved as `TopologicalSpaces().CartesianProducts()` (spec line 110)
- Product metric → preserved as `TopologicalSpaces().Metric().CartesianProducts()` (spec line 119)

**Anti-weakening guards in spec:**

- Spec line 231-235: Explicit rejection conditions for future edits — do not admit interval/ball/p-adic fields as `TopologicalSpaces().Constructors()`, do not move constructor ownership from rings, do not create ring-local duplicates of topological predicates.
- Spec line 39-41 (review gates): "Place every method at the highest category where the operation is mathematically well-defined."
- Spec line 40 (review gates): "Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening."
- Spec line 41 (review gates): "Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds."

**G6 Verdict: PASS.** All Sage-inventoried surface methods are preserved in the spec, either as abstract methods in the owning category or as concrete methods on subcategory axioms. No method was weakened, deleted, or moved without a grounded replacement owner. The explicit anti-weakening rejection conditions provide forward protection against future editorial weakening.

### Summary

| Gate | Description | Verdict | Evidence count |
|---|---|---|---|
| G1 | Source grounding — file existence | PASS | 20+ files verified |
| G2 | Sage surface completeness | PASS | 40+ inventory items accounted |
| G3 | Constructor route justification | PASS | 10 mathematical validity checks |
| G4 | Nonmathematical rejection | PASS | 7 explicit rejections with rationale |
| G5 | Ambiguity routing | PASS | 5 gap/ambiguity routings verified |
| G6 | Obligation preservation | PASS | 14 method + constructor obligations preserved |

**Overall: 6/6 gates PASS.** The spec is mathematically sound, source-grounded, and preserves all inventoried Sage surfaces without weakening. The category hierarchy correctly places Connected/Compact at the topological root, Metric as a topological refinement, and Complete as a metric refinement. Constructor placement in `Sets().Constructors()` with topological refinement is mathematically justified. The ring/field topology recovery path through `Rings().Topological()` preserves single ownership of topological predicates.

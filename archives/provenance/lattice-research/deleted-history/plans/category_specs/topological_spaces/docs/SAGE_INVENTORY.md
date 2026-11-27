# Topological Spaces Sage Inventory

Sources for this pass:

- Sage docs: `sage.categories.topological_spaces`,
  `sage.categories.metric_spaces`, and `sage.sets.real_set`.
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/topological_spaces.py`,
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/metric_spaces.py`,
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/real_set.py`.
- Sage observation commands run with `/home/dzack/miniforge3/envs/sage/bin/sage -c`.

## Category Surfaces

| Sage surface | Source | Sage meaning | Method surface |
| --- | --- | --- |
| `sage.categories.topological_spaces.TopologicalSpaces` / `Sets().Topological()` | `sage/categories/topological_spaces.py` | Category of topological spaces; supercategory is `Sets()`. | No parent method mixin is defined in Sage. The category records the additional topological structure preserved by morphisms. |
| `TopologicalSpaces.CartesianProducts.extra_super_categories()` | `sage/categories/topological_spaces.py` | A finite Cartesian product of topological spaces is a topological space. | Construction-category edge only. |
| `TopologicalSpaces.SubcategoryMethods.Connected()` | `sage/categories/topological_spaces.py` | Full subcategory of connected topological spaces. | Returns the `Connected` axiom category. |
| `TopologicalSpaces.SubcategoryMethods.Compact()` | `sage/categories/topological_spaces.py` | Subcategory of compact topological spaces. | Returns the `Compact` axiom category. |
| `TopologicalSpaces.Connected.CartesianProducts.extra_super_categories()` | `sage/categories/topological_spaces.py` | A finite Cartesian product of connected topological spaces is connected. | Construction-category edge only. |
| `TopologicalSpaces.Compact.CartesianProducts.extra_super_categories()` | `sage/categories/topological_spaces.py` | A finite Cartesian product of compact topological spaces is compact. | Construction-category edge only. |
| `sage.categories.metric_spaces.MetricSpaces` / `Sets().Metric()` | `sage/categories/metric_spaces.py` | Category of metric spaces; Sage states that a metric space is a set with a distinguished metric. | `ParentMethods.metric_function`, deprecated alias `metric`, `ParentMethods.dist`, `ElementMethods.abs`, and `ElementMethods.dist`. |
| `MetricSpacesCategory.default_super_categories(category)` | `sage/categories/metric_spaces.py` | If an object is metric in category `C`, it is also topological in `C` and a metric space. | Builds the join of `category.Topological()` and the default metric supercategories. |
| `MetricSpaces.Homsets` | `sage/categories/metric_spaces.py` | Homsets of metric spaces consist of metric maps, described as Lipschitz maps with constant 1. | `_test_metric_map` checks `self(a).dist(self(b)) <= a.dist(b)`. |
| `MetricSpaces.WithRealizations.ParentMethods.dist(a, b)` | `sage/categories/metric_spaces.py` | Computes distance after converting into a realization. | `dist(a, b)`. |
| `MetricSpaces.CartesianProducts.ParentMethods.dist(a, b)` | `sage/categories/metric_spaces.py` | Product metric is the maximum of factor distances. | `dist(a, b)`. |
| `MetricSpaces.SubcategoryMethods.Complete()` | `sage/categories/metric_spaces.py` | Full subcategory of complete metric spaces. | Returns the `Complete` axiom category. |
| `MetricSpaces.Complete.CartesianProducts.extra_super_categories()` | `sage/categories/metric_spaces.py` | A finite Cartesian product of complete metric spaces is complete. | Construction-category edge only. |

## Real-Line Topological Surfaces

| Sage surface | Source | Sage meaning | Method or constructor surface |
| --- | --- | --- | --- |
| `sage.sets.real_set.InternalRealInterval` | `sage/sets/real_set.py` | Real interval. Sage docs say callers should use `RealSet` instead of constructing this class directly. | `closure`, `interior`, `boundary_points`, `contains`, `is_connected(other)`, endpoint accessors, and endpoint open/closed predicates. |
| `sage.sets.real_set.RealSet` | `sage/sets/real_set.py` | Subset of the real line, represented as a finite union of intervals. | Variadic constructor from two extended real numbers, finite data describing intervals, existing `RealSet` values, `InternalRealInterval` values, symbolic real relations, and selected manifold interval objects. |
| `RealSet.__init__` category assignment | `sage/sets/real_set.py` | Pure `RealSet` instances refine into `TopologicalSpaces()`, and into `Connected`, `Compact`, `Subobjects`, `Finite`, or `Infinite` according to interval data. | Category assignment, not a user-facing method. |
| `RealSet.interval(lower, upper, *, lower_closed, upper_closed, **kwds)` | `sage/sets/real_set.py` | Construct an interval with explicit endpoint closure data. | Named interval constructor. |
| `RealSet.open(lower, upper, **kwds)` | `sage/sets/real_set.py` | Construct `(a, b)`. | Named interval constructor. |
| `RealSet.closed(lower, upper, **kwds)` | `sage/sets/real_set.py` | Construct `[a, b]`. | Named interval constructor. |
| `RealSet.point(p, **kwds)` | `sage/sets/real_set.py` | Construct `{p}`. | Named point constructor. |
| `RealSet.open_closed(lower, upper, **kwds)` | `sage/sets/real_set.py` | Construct `(a, b]`. | Named interval constructor. |
| `RealSet.closed_open(lower, upper, **kwds)` | `sage/sets/real_set.py` | Construct `[a, b)`. | Named interval constructor. |
| `RealSet.unbounded_below_closed(bound, **kwds)` | `sage/sets/real_set.py` | Construct `(-oo, b]`. | Named ray constructor. |
| `RealSet.unbounded_below_open(bound, **kwds)` | `sage/sets/real_set.py` | Construct `(-oo, b)`. | Named ray constructor. |
| `RealSet.unbounded_above_closed(bound, **kwds)` | `sage/sets/real_set.py` | Construct `[a, +oo)`. | Named ray constructor. |
| `RealSet.unbounded_above_open(bound, **kwds)` | `sage/sets/real_set.py` | Construct `(a, +oo)`. | Named ray constructor. |
| `RealSet.real_line(**kwds)` | `sage/sets/real_set.py` | Construct the full real line `(-oo, +oo)`. | Named ambient-space constructor. |
| `RealSet.is_open()` | `sage/sets/real_set.py` | Test whether a real subset is open in the real-line topology. | Predicate on the subset object. |
| `RealSet.is_closed()` | `sage/sets/real_set.py` | Test whether a real subset is closed in the real-line topology. | Predicate on the subset object. |
| `RealSet.closure()` | `sage/sets/real_set.py` | Return topological closure as a new `RealSet`. | Subset transform. |
| `RealSet.interior()` | `sage/sets/real_set.py` | Return topological interior as a new `RealSet`. | Subset transform. |
| `RealSet.boundary()` | `sage/sets/real_set.py` | Return topological boundary as a new `RealSet`. | Subset transform. |
| `RealSet.ambient()` | `sage/sets/real_set.py` | Return the ambient real line. | Subobject method. |
| `RealSet.n_components()` and `RealSet.get_interval(i)` | `sage/sets/real_set.py` | Return connected-component data for normalized finite unions of intervals. | Real-line decomposition methods. |
| `RealSet.union`, `intersection`, `complement`, `difference`, `is_disjoint`, `is_subset`, `are_pairwise_disjoint`, `convex_hull` | `sage/sets/real_set.py` | Boolean and order operations on real subsets. | Set/subobject operations with real-line interval representations. |

## Numeric Interval and Ball Surfaces

| Sage surface | Source | Sage meaning | Observed topological or metric category surface |
| --- | --- | --- | --- |
| `RealIntervalField` / real interval elements | Sage numerical-field docs and `sage.rings.real_mpfi` extension module | Interval arithmetic over real intervals. | Existing local type anchor is `RealIntervalFieldElement`; topology-bearing ring ownership lives in ring/field categories. |
| `ComplexIntervalField` / complex interval elements | Sage numerical-field docs and `sage.rings.complex_interval` extension module | Complex interval arithmetic. | Existing local type anchor is `ComplexIntervalFieldElement`; topology-bearing ring ownership lives in ring/field categories. |
| `RealBallField` / real ball elements | Sage numerical-field docs and `sage.rings.real_arb` extension module | Real balls represent intervals `[m-r, m+r]`. | Observed `RBF.category()` is `Category of infinite fields`; `RBF in Sets().Metric()` is `False`; `RBF` has no parent `dist`. |
| `ComplexBallField` / complex ball elements | Sage numerical-field docs and `sage.rings.complex_arb` extension module | Complex balls are rectangular complex enclosures tracked by real and imaginary ball components. | Observed `CBF.category()` is `Category of infinite fields`; `CBF in Sets().Metric()` is `False`; `CBF` has no parent `dist`. Element methods include numerical enclosure operations such as `above_abs()` and `below_abs()`. |

## Excluded Structured Geometric Surfaces

The following Sage surfaces are visible in the same documentation/search space but are
outside this pure topological-space inventory by directive:

| Sage surface | Source evidence | Reason for exclusion from this inventory |
| --- | --- | --- |
| `RealSet(..., structure='differentiable')`, `RealSet(..., ambient=...)`, and coordinate-name keywords | `sage/sets/real_set.py` and the `RealSet` docs | These construct differentiable real manifolds or manifold subsets, not pure finite unions of real intervals. |
| `sage.manifolds` constructors such as `Manifold`, `RealLine`, `OpenInterval`, and manifold subsets | Sage manifold docs and `RealSet` conversion examples | These are structured manifold objects. |
| Hyperbolic-plane models used in `MetricSpaces` examples | Sage metric-space docs | These are structured geometric realizations used as examples for metric methods. |
| Schemes, varieties, polyhedra, CW complexes, simplicial complexes, and simplicial sets | Sage reference navigation and scheme/topology docs | These carry topological or geometric structure, but their constructors belong to their own mathematical subtrees. |

## Inventory Gaps

- Sage does not expose a standalone pure `TopologicalSpace(...)` constructor in the
  inventoried category source.
- The pure `RealSet` constructor is variadic. Its named interval constructors provide
  the finite candidate list for future closed overloads.
- Sage's numeric interval and ball rings are inventoried here only as topology-bearing
  evidence. Their algebraic constructors are owned by ring/field inventory.

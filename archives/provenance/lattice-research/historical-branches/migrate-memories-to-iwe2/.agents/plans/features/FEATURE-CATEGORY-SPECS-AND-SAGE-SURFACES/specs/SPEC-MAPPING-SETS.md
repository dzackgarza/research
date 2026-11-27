---
id: SPEC-MAPPING-SETS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track sets mapping spec
status: complete
priority: critical
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
constructorNameInventories:
- owner: category_specs.sets.Sets._Constructors
  sageConstructorNames:
  - Set
  - FiniteEnumeratedSet
  - IntegerRange
  - NonNegativeIntegers
  - PositiveIntegers
  - Primes
  - RealSet
  - interval
  - open
  - closed
  - point
  - open_closed
  - closed_open
  - unbounded_below_closed
  - unbounded_below_open
  - unbounded_above_closed
  - unbounded_above_open
  - real_line
  - RecursivelyEnumeratedSet
  - DisjointUnionEnumeratedSets
  - CartesianProduct
  - cartesian_product
  - TotallyOrderedFiniteSet
  - FiniteSetMaps
  - Family
  - EnumeratedSetFromIterator
  - ImageSubobject
  - SetPartitions
  - SetPartition
  - from_restricted_growth_word_blocks
  - from_restricted_growth_word_intertwining
  - from_arcs
  - from_rook_placement
  - from_rook_placement_gamma
  - from_rook_placement_rho
  - from_rook_placement_psi
---
## Review Log

### Independent Review - 2026-05-07 (fresh-context subagent)

**Gates passed:** Gate 1 Source Coverage, Gate 2 Highest Category Placement, Gate 3 Row
Completeness, Gate 4 Rejection of Nonmathematical Targets, Gate 5 Gap Routing, Gate 6
Overall Completeness

**Gates failed:** none

**Outcome:** complete.
All six gates pass.

- Gate 1: Every Sage surface from 742-line SAGE_INVENTORY.md mapped.
  All major surfaces accounted for.
- Gate 2: Every method placed at mathematically appropriate highest category.
  Inheritance respected.
- Gate 3: 5 table formats all provide caller context, hypotheses, return object, source
  evidence.
- Gate 4: 10+ explicit rejections of nonmathematical surfaces.
  No variadic option bags.
- Gate 5: 6 major ambiguities routed to decision cards/tasks.
  Residual gaps documented.
- Gate 6: All 33 subcategory files, homsets.py, axioms.py, and all referenced cards
  exist.

Verification: just plan-validate passes.
SPEC-MAPPING-SETS.md is a thorough mapping from Sage to project category surfaces.
requirement: Convert category_specs/sets/docs/MAPPING.md into a tracked spec surface and
audit it for Sage-source completeness, mathematical correctness, and well-typed set,
finite, enumerated, subobject, family, image, and constructor signatures.
acceptanceCriteria:
- Source paths category_specs/sets/docs/MAPPING.md and
  category_specs/sets/docs/SAGE_INVENTORY.md are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
  complexity: 85 tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
* * *
# Sets: Sage Category → Spec Hierarchy Mapping Spec

This tracked spec is the canonical mapping surface converted from
`category_specs/sets/docs/MAPPING.md`.

Source inventory: `category_specs/sets/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical
  surface, a named constructor path, a mathematically justified non-mapping, or a
  tracked decision.
- Place every method at the highest category where the operation is mathematically
  well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source
  evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option
  bags, and category-obligation example-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked
  decisions or tasks before implementation proceeds.

## Foundational Assumption: Computable Sets

This spec and all downstream category specs assume **Sets** means the category of
**computable sets**: sets whose elements admit algorithmic membership tests and, when
countable, an algorithmic enumeration.
See `theory/foundations/computable-sets.md` for the full justification.
In practice, this means:

- `EnumeratedSets` ↔ `Sets().Countable()` is an identification, not a weakening: a set
  is countable iff there exists an injection `X → ℕ`, which in our computational
  framework is witnessed by a Python iterator.
- Every Sage object already satisfies this (Sage cannot represent
  non-recursively-presentable sets), so this assumption does not exclude any object that
  can actually appear in Sage.
- The restriction is documented here and in `theory/foundations/computable-sets.md` as a
  foundational convention, not a mathematical claim about set theory.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/sets/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/sets_cat.py`
  - `sage/categories/finite_sets.py`
  - `sage/categories/enumerated_sets.py`
  - `sage/categories/finite_enumerated_sets.py`
  - `sage/categories/infinite_enumerated_sets.py`
  - `sage/categories/facade_sets.py`
  - `sage/sets/all.py`
  - `sage/sets/set.py`
  - `sage/sets/finite_enumerated_set.py`
  - `sage/sets/integer_range.py`
  - `sage/sets/non_negative_integers.py`
  - `sage/sets/positive_integers.py`
  - `sage/sets/primes.py`
  - `sage/sets/real_set.py`
  - `sage/sets/recursively_enumerated_set.pyx`
  - `sage/sets/disjoint_union_enumerated_sets.py`
  - `sage/sets/cartesian_product.py`
  - `sage/sets/condition_set.py`
  - `sage/sets/image_set.py`
  - `sage/sets/totally_ordered_finite_set.py`
  - `sage/sets/finite_set_maps.py`
  - `sage/sets/disjoint_set.pyx`
  - `sage/combinat/set_partition.py`
  - `sage/sets/family.pyx`
  - `sage/sets/set_from_iterator.py`
  - `sage/categories`
  - `sage/sets`
  - `sage/categories/isomorphic_objects.py`
  - `sage/categories/with_realizations.py`
  - `sage/categories/realizations.py`
  - additional installed source paths listed in
    `category_specs/sets/docs/SAGE_INVENTORY.md` beyond this ledger limit: 7
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*`
  modules raised `ImportError: cannot import name Category`; completeness work therefore
  uses installed source files and inventories as the durable source surface unless that
  environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Sets method
  reconciliation is recorded in `Completeness Reconciliation: Sets` below, with
  remaining gaps routed through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Converted Mapping Content

This file records, for each Sage category relevant to `Sets()`, the mathematical
justification for how it maps to our hierarchy.

## Sage `EnumeratedSets` → our `Sets().Countable()`

Sage's `EnumeratedSets` axiom captures: "there exists an explicit enumeration
(iteration) of the set's elements."
Countability is equivalent: a set is countable iff there exists an injection f: X → ℕ,
which is precisely an enumeration.
Every Sage enumerated set is countable, and every countable set in our hierarchy must
supply an iterator (via `__iter__`).

Consequence: objects that lie in `SageEnumeratedSets()` are refined to
`Sets().Countable()`. The spec class `_CountableSets` therefore declares
`super_categories = [Sets(), SageEnumeratedSets()]`. Project countability does not
include conversion to a finite Python collection: `list(ZZ)` and `tuple(ZZ)` have no
mathematical finite value.
Those conversions belong to finite countable sets.

### Enumeration Protocol Mapping

Countable-set enumeration should be specified through mathematical/Python protocol
surface, not through Sage's fallback helper names.

Python's built-in `list(X)` and `tuple(X)` conversions consume the iterable protocol;
there is no project category method to add for this behavior.
Do not define Sage-style `.list()`/`.tuple()` methods, and do not introduce `__list__`
or `__tuple__` hooks.
Finite countable sets only need to be iterable, with finite cardinality/length where the
protocol requires it.

| Sage surface | Project surface | Project call recovering Sage behavior | Mapping decision |
| --- | --- | --- | --- |
| `__iter__()` | `__iter__()` | `iter(X)` or `for x in X` | The iterator witnesses countability. |
| `unrank(n)` and `__getitem__(n)` | `X[n]` / `__getitem__(n: Integer)` | Replace `X.unrank(n)` with `X[n]`. | This is the nth-element map for the chosen enumeration. `unrank` is Sage vocabulary for the same map and should not be a second primary project method. |
| `rank(e)` | `rank(e)` | Keep `X.rank(e)`. | Keep this as the index-of map for the chosen enumeration: it is the partial inverse of `X[n]`. It is meaningful for infinite countable sets, but the spec makes no complexity promise. |
| `iterator_range(start, stop, step)` | no project method | Use `iter(X[start:stop:step])` when slice indexing is admitted, or `(X[n] for n in range(start, stop, step))`. | This is a range convenience over the enumeration, not independent category structure. |
| `unrank_range(start, stop, step)` | no project method | Use `list(X[start:stop:step])` for finite countable sets when slice indexing is admitted. | Materializing a whole range is a finite collection operation. It is not a countable-set obligation. |
| `first()` | no project method | Replace `X.first()` with `X[0]`. | The first element is the zeroth element of the chosen enumeration. |
| `next(e)` | no project method | Replace `X.next(e)` with `X[X.rank(e) + 1]` when `rank(e)` is defined. | This recovers Sage successor behavior from the rank and nth-element maps. |
| `last()` | no project method | Replace `X.last()` with `X[len(X) - 1]` on finite countable sets. | Last element is finite-only. |
| `tuple()` and `list()` | finite Python conversions | Replace `X.tuple()` with `tuple(X)` and `X.list()` with `list(X)` on finite countable sets. | These are finite Python conversions. They are not countable-set methods and are not admitted on infinite countable sets. |
| `set()` and `frozenset()` | no project method | No replacement. If a finite project set is needed, use the admitted finite-set constructor rather than Python hash-set export. | Python hash-set export loses the project/Sage set object and is not a category obligation. |
| `_first_from_iterator` | no project method | Recover with `next(iter(X))` or `X[0]` when indexing is available. | Sage fallback helper; inventory-only. |
| `_next_from_iterator(obj)` | no project method | Recover with `X[X.rank(obj) + 1]` when `rank(obj)` is available. | Sage fallback helper; inventory-only. |
| `_unrank_from_iterator(r)` and `_unrank_from_list(r)` | no project method | Recover with `X[r]`. | Sage fallback/cache helper; inventory-only. |
| `_rank_from_iterator(x)` | no project method | Recover with `X.rank(x)`. | Sage fallback helper; inventory-only. |
| `_iterator_from_list`, `_iterator_from_next`, `_iterator_from_unrank` | no project method | Recover with `iter(X)`. | Sage iterator-construction helpers; inventory-only. |
| `_tuple_from_iterator`, `_tuple_from_list` | no project method | Recover with `tuple(X)` on finite countable sets. | Sage finite materialization/cache helpers; inventory-only. |
| `_list_from_iterator` | no project method | Recover with `list(X)` on finite countable sets. | Sage finite materialization/cache helper; inventory-only. |
| `_cardinality_from_list`, `_cardinality_from_iterator` | no project method | Recover with `X.cardinality()` or `len(X)` when a finite Python length is needed. | Sage cache/fallback helpers; inventory-only. |
| `_some_elements_from_iterator`, `_random_element_from_unrank`, `_last_from_iterator`, `_last_from_unrank` | no project method | Recover through the named mathematical method, indexing, or finite Python conversion as appropriate. | Sage fallback/cache helpers; inventory-only. |

Sage's generic `_rank_from_iterator` is brute-force iteration: it returns the first
position where the element appears, and on an infinite enumerated set it need not
terminate when the element is absent.
Concrete Sage parents may and often do provide faster rank/unrank formulas, such as
arithmetic formulas for integer ranges or mixed radix formulas for finite Cartesian
products. The project spec records the semantic rank map, not the fallback algorithm.

## Sage `FiniteEnumeratedSets` → our `Sets().Countable().Finite()`

Finite enumerated sets are both finite and countable.

## Sage `InfiniteEnumeratedSets` → our `Sets().Countable().Infinite()`

Infinite enumerated sets are countably infinite.

## Sage `FacadeSets` → our `Sets().Facade()`

Facade sets represent their elements as elements of another parent.
Mapping is direct: `SageFacadeSets()` ↔ `Sets().Facade()`.

## Sage `TopologicalSpaces` → our `Sets().Topological()`

Sage's `TopologicalSpaces()` captures topological structure.
`RealSet` lives here.
The forward target is the dedicated `topological_spaces` subtree: `Sets().Topological()`
navigates to `TopologicalSpaces()`, and `Sets().Metric()` navigates to
`TopologicalSpaces().Metric()`.

## Sage `FiniteSets` → our `Sets().Finite()`

Direct: `SageFiniteSets()` ↔ `Sets().Finite()`.

## Local Surface → Target Spec Surface

The set subtree maps each Sage-backed or local surface to the target mathematical
subcategory file that owns its spec.

| Source surface | Target destination | Rationale |
| --- | --- | --- |
| Set axiom names | Root `category_specs/axioms.py` plus axiom classes under `sets/subcategories/` | Axiom names have one root registration point; set axiom classes own the mathematical method surfaces. |
| Specialized set-object surfaces | One mathematical subcategory file per Sage concept under `sets/subcategories/` | The file structure follows mathematical vocabulary, not implementation history. |
| Named set constructors | `Sets().Constructors()` on `sets/__init__.py` | Constructors are entry points, not subcategories. |
| Sage `Set(X)` / `Set_object` wrappers | no admitted wrapper category; method surface remapped below | Sage implements this surface, but arbitrary object wrapping is not a mathematical set constructor. Its methods are still evidence for project set surfaces, so each method is mapped explicitly instead of being silently dropped. |
| `_FiniteEnumeratedSetObjects` | `subcategories/finite_enumerated_set.py` | Finite enumerated sets have their own Sage-backed method surface. |
| `_IntegerRangeSets` | `subcategories/integer_range.py` | Integer ranges are arithmetic progressions with finite or infinite countable behavior. |
| `_NonNegativeIntegersSets` | `subcategories/non_negative_integers.py` | Nonnegative integers are a named countably infinite subset of `ZZ`. |
| `_PositiveIntegersSets` | `subcategories/positive_integers.py` | Positive integers are a named countably infinite integer range. |
| `_PrimesSets` | `subcategories/primes.py` | `Sets().Primes()` is the one-object category for the full Sage prime set. |
| `_RealSets` | `subcategories/real_set.py` | Real subsets, real open sets, and real intervals require distinct vocabulary in `types.py`. |
| `_RecursivelyEnumeratedSets` | `subcategories/recursively_enumerated.py` | Recursively enumerable sets and forests share the Sage constructor family. |
| `_DisjointUnionEnumeratedSets` | `subcategories/disjoint_union.py` | Disjoint unions are countable coproducts of indexed families. |
| `_CartesianProductSets` | `subcategories/cartesian_product.py` | Cartesian products have parent and element projection surfaces. |
| Sage `ConditionSet` backing | `subcategories/condition.py` through `subcategories/constructions/subobjects.py` | Predicate-defined subsets are subobjects. Sage `ConditionSet` is localized interop used behind `Sets().Subobjects().Of(...)`, not a public project category. |
| `_ImageSets` | `subcategories/image.py` | Images are constructive subobjects/subquotients under a map. The public surface includes `ambient`, `lift`, and `retract`; Sage's private `_map` and `_domain_subset` storage remains implementation detail unless a later source-backed need admits named accessors. |
| `_TotallyOrderedFiniteSets` | `subcategories/totally_ordered_finite.py` | Finite total orders have parent and element comparison surfaces. |
| `_FiniteSetMapsSets` | `subcategories/finite_set_maps.py` | Finite map sets own finite enumeration and element-construction surfaces. Generic homset data such as domain/codomain, and endomap identity for the endomap case, belong to the homset/endset refinement. |
| `_PartitionedSets` | `subcategories/partitioned.py` | A set partition of `X` is a subset of `P(X)` whose blocks are nonempty, pairwise disjoint, and cover `X`; Sage's fixed-base `SetPartitions(X)` is the Sage parent whose elements are these partitions. |
| `_FamilySets` | `subcategories/family.py` | Indexed families have finite, lazy, trivial, and enumerated variants. |
| `_EnumeratedSetsFromIterator` | `subcategories/enumerated_from_iterator.py` | Callable-backed enumerated sets expose iterator and cache surfaces. |
| Sage subquotient construction surface | `subcategories/constructions/subquotients.py` | Subobjects and quotients are special cases of constructive subquotients, so the parent construction must be explicit. |
| Sage isomorphic-object construction surface | `subcategories/constructions/isomorphic_objects.py` | Images by isomorphism are both subobjects and quotients in Sage and need their own construction file. |
| Sage realization surface | `subcategories/constructions/with_realizations.py` and `subcategories/constructions/realizations.py` | A set with multiple realizations and its concrete realization parents are construction categories, not named constructors. |
| Sage homset/endset surface | `Sets().HomCategory()` / `Sets().EndCategory()` in `sets/homsets.py` plus top-level `homsets/` | The project surface names the categories `HomCategory` and `EndCategory`; their objects are set-level hom and end objects. Automorphism categories derive from end categories at the top level. |
| `SetsWithGrading()` | `subcategories/graded.py`; canonical navigation `Sets().Graded()` | A graded set is a set equipped with a grading map to a grading set. Sage's own TODO asks for this to live under `Sets()`, and the project uses the uniform axiomatic name `Graded`. |
| `GSets(G)` | `subcategories/group_actions.py`; public navigation `Sets().GSets(G)` | A `G`-set is a set equipped with an action of the fixed group `G`. Sage's category is parameterized by `G` and has `Sets()` as its supercategory. |
| `Posets()`, `LatticePosets()`, `FiniteLatticePosets()` | promoted `posets/` subtree; `sets` docs keep only cross-navigation | Posets have an independent order-theoretic method surface. Lattice posets here are order-theoretic meet/join lattices, not module lattices or quadratic lattices. |

Target subcategory file names follow mathematical vocabulary.
Groupings by constructor history, implementation convenience, or named-object families
are not target subcategory boundaries.

## Sage Category → Project Category Decisions

| Sage category | Project category | Justification | Consequence |
| --- | --- | --- | --- |
| `SetsWithPartialMaps()` | `Sets()` inherited through Sage | Sage places `Sets()` below sets with partial maps. The project does not need a separate public partial-map category for the set-object inventory. | `Sets.super_categories()` keeps `SageSets()`, so Sage's inherited category behavior remains available. |
| `Sets()` | `Sets()` | Base category of parents whose elements support membership and basic element construction. | Root method surface includes operations meaningful for arbitrary sets, including union. Ambient-dependent operations such as intersection, difference, symmetric difference, and complement use `Subset` vocabulary under `Subsets = Subobjects`. |
| `Sets().Algebras(R)` / plain-set `S.algebra(R)` | no set/algebra subcategory; route to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)` | Sage's existing path constructs the free `R`-module with basis indexed by `S`; it is not the free associative `R`-algebra on generators `S`. | Project code uses `S.free_module(R)` to recover this Sage functionality. The true free algebra on `S` uses `S.free_algebra(R)` and routes through `Algebras(R).Constructors().FreeAlgebra(generators=S)`. |
| `EnumeratedSets()` | `Sets().Countable()` | Sage defines enumerated sets as finite or countable sets/multisets with a canonical enumeration. Countability is the set-level mathematical property; enumeration methods are the computable witness. | Countable sets declare iteration, nth-element/indexing, and rank. Sage `unrank` maps to `__getitem__`; Sage fallback helpers stay inventory-only. Full finite collection conversions are not countability data. Multiset caveat remains a documented boundary. |
| `FiniteSets()` | `Sets().Finite()` | Finite sets have finite cardinality independent of enumeration. | `Finite` declares `is_finite() -> True`, cardinality, `len(X)`, finite random element generation, and finite subquotient behavior. |
| `FiniteEnumeratedSets()` | `Sets().Countable().Finite()` | Finite enumerated sets combine finite cardinality with explicit enumeration. | The finite-countable subcategory owns finite cardinality, `len(X)`, and finite random element generation. Python conversions such as `list(X)` and `tuple(X)` consume iteration; Sage list/range/cache helper names stay inventory-only. |
| `InfiniteEnumeratedSets()` | `Sets().Countable().Infinite()` | Infinite enumerated sets are countably infinite, not listable as finite collections. | Infinite-countable declarations keep iteration, indexing, and rank semantics, but do not admit Sage's eager `tuple`/`list` methods as project category obligations. |
| `FacadeSets()` | `Sets().Facade()` | Elements are represented by elements of another parent. | `facade_for`, facade element construction, and facade parent checks belong here. |
| Sage `TopologicalSpaces()` for `RealSet` | `TopologicalSpaces()` / `Sets().Topological()` plus `Sets().Subobjects()` when an ambient real line is present | A `RealSet` is a topological subset of the real line, and a set with a topology is precisely a topological space. | `RealSet` refinement preserves Sage's finite-interval-normalized Boolean operations. Generic subobject/subquotient methods such as `ambient`, `lift`, and `retract`, and root comparison methods such as `is_subset`, are inherited from `Sets().Subobjects()`, `Sets().Subquotients()`, and `Sets()`. |
| Sage `Set_base` boolean mixins | Root set operations and `Sets().Subobjects()` / `Subsets` | Sage's boolean mixins are implementation artifacts, not mathematical subcategories. A set has union with any other set in `Sets()`. Intersections, differences, symmetric differences, and complements require a common ambient set and therefore live on subsets/subobjects. | Do not introduce a project `WithBooleanOps` axiom. Map Sage mixin methods to the mathematical operation surface they actually represent. |
| `SubobjectsCategory` | `Sets().Subobjects()` / alias `Subsets` | In the category of sets, subobjects are exactly subsets. Predicate-defined subsets are constructed as `Sets().Subobjects().Of(ambient, predicates)` and backed by Sage `ConditionSet` under the hood. The same construction must remain attachable to arbitrary set subcategories via Sage's functorial construction/category-of machinery. | The set subtree exposes `Subsets = Subobjects` and uses `Subset` type vocabulary in signatures. Its implementation lives in `subcategories/constructions/subobjects.py`, not a monolithic `constructions.py`. Raw Sage `ConditionSet.arguments()` stays inventory-only. |
| `SetPartitions(s)` fixed-base parents | `Sets().Partitioned()` | A partition of `s` is represented as a subset of the powerset of `s`. The fixed-base parent `SetPartitions(s)` is the set of all such partition subobjects and its elements are the actual `SetPartition` objects. | `sets/subcategories/partitioned.py` owns the partition method surface. `Sets().Constructors().SetPartitions(...)` is the public constructor path for all Sage `SetPartitions` overload cases. `SetPartition` remains anchored to Sage's element class in `types.py`. |
| `SetPartitions(s)` with `s` a finite totally ordered set | `Sets().Partitioned().FiniteTotallyOrderedBase()` | The extra hypothesis lives on the fixed base set returned by `base_set()`: Sage's crossing/nesting/atomic surfaces use the induced order on `s`, not a total order on the set of partitions itself. | This is an axiom on `Sets().Partitioned()`, not a meet with `Sets().TotallyOrdered()`. The owner records that the partition parent is finite and that its base set carries the relevant total order. |
| `SetPartitions()` all finite partitions | `Sets().Countable()` | There is no fixed base set, hence no single powerset ambient object. Sage represents this as the countable parent of all finite set partitions. | The constructor path is `Sets().Constructors().SetPartitions()`. It is not refined into `Sets().Partitioned()` because the fixed-base powerset ambient is absent. |
| `QuotientsCategory` | `Sets().Quotients()` | Quotient sets are equivalence-class objects. Like subobjects, quotient categories are attachable construction categories, not singleton categories. | `subcategories/constructions/quotients.py` owns the set-specific quotient scaffold and `types.py` exposes `QuotientSet`. |
| `SubquotientsCategory` | `Sets().Subquotients()` | Sage's constructive subquotients are the primitive construction behind quotients and subobjects: an object has an ambient object, a lift, and a retract. | `subcategories/constructions/subquotients.py` owns the ambient/lift/retract surface. |
| `IsomorphicObjectsCategory` | `Sets().IsomorphicObjects()` | An isomorphic image is simultaneously a subobject and a quotient in Sage. | `subcategories/constructions/isomorphic_objects.py` owns the lift/retract/isomorphism convention. |
| `WithRealizationsCategory` / `RealizationsCategory` | `Sets().WithRealizations()` and `Sets().Realizations()` | A parent with realizations is a set whose elements may live in several concrete realization parents; Sage makes it a facade set. | `with_realizations.py` and `realizations.py` own the construction surfaces; realization names are not constructors. |
| `HomsetsCategory` | `SetHomCategory`, `SetEndCategory`, `SetAutCategory` | Morphisms between sets are functions; endomorphisms have equal domain/codomain; automorphisms are bijections. | Generic `AutCategory` wiring belongs at the repository top level, but set-specific hom categories declare function-level methods and delegate aut construction rather than reimplement condition-set machinery. Inverse images of subsets belong to set maps as `preimage(subset)`. `Sets().HomCategory()` and `Sets().EndCategory()` are public category navigation surfaces. |
| `Homsets().Endset()` | `SetEndCategory` | End categories have objects `End(X) = Hom(X, X)`; Sage makes generic endsets monoids. | `sets/homsets.py` exposes the set-specific end category and inherits generic end-category methods. The former `base_set()` alias is represented by the generic hom-object `domain()` on `End_Sets(X)`. |
| Sage generic hom/end surface plus project aut target | `SetAutCategory` backed by generic `AutCategory` | `Aut(X)` is the subset of `End(X)` consisting of bijections. | This project vocabulary is wired once at the top level and specialized in `sets/homsets.py`; upstream category-naming follow-up belongs in the tracker item that cites this mapping row. |
| `Sets.MorphismMethods` | set-morphism element surface | A morphism in `Sets()` is a function. Injectivity, inverse maps when they exist, and image subobjects are properties or constructions of set maps, not properties of the result category. | Sage `is_injective()` maps to a set-map predicate; `__invert__()` maps to `inverse()` on isomorphisms or invertible maps; `image(domain_subset=None)` constructs an `ImageSubobject(f, domain_subset)` whose result is typed by `Sets().Subobjects()`/`Sets().Subquotients()`. |
| `SetsWithGrading()` | `Sets().Graded()` | A graded set is a disjoint union of graded components indexed by a grading set, with a grading map sending each element to its grade. | `subcategories/graded.py` owns `grading_set`, `graded_component`, optional `subset`, `grading`, `generating_series`, and `_test_graded_components`. |
| `GSets(G)` | `Sets().GSets(G)` | A `G`-set is a set with an action of the fixed group `G`; Sage's source records `GSets(G).super_categories() == [Sets()]`. | `subcategories/group_actions.py` owns the parameterized category. `types.py` needs `GSet` and group-action vocabulary anchored to Sage group/action objects. |
| `Posets()` | top-level `posets/` subtree, cross-linked from `sets` | A poset is a set with a partial order. Sage's required parent method is `le`; it also exposes `lt`, `ge`, `gt`, covers, order ideals, filters, chains, and antichains. | Do not bury this under ordinary set subcategories. The promoted subtree owns order methods and its own finite/lattice refinements. |
| `LatticePosets()` / `FiniteLatticePosets()` | `posets/subcategories/lattice.py` and `posets/subcategories/finite_lattice.py` | These are order-theoretic lattices: posets in which every pair has a meet and join. | Keep separate from module/quadratic-form lattice vocabulary; finite lattice posets add irreducibles and lattice-morphism checks. |

## Sets Homset Mirroring Audit

The Sets subtree does not treat Sage generic homset inheritance as an implicit public
contract. Sage homset, set-morphism, image, and finite-map surfaces are retained only
where they belong to project-owned set Hom/End/Aut vocabulary or to a separate
finite-map/image-set construction owner.

| Sage source surface | Source evidence | Project owner and outcome |
| --- | --- | --- |
| Generic homset `domain()`, `codomain()`, `natural_map()`, `identity()`, `one()`, and `reversed()` | `sage/categories/homset.py:1136-1249` | Routed to the generic project homset semantic base. Sets uses these as Hom/End infrastructure; they are not set-specific methods. |
| Homset-category `is_endomorphism_set()` and generic endset monoid structure | `sage/categories/homsets.py:330-355`; inventory rows for `Sets().Endsets()` | Routed through `Sets().EndCategory()` and the generic `EndCategory`. The endomap monoid law belongs to the generic end layer; set-specific refinements add function predicates, not a new monoid owner. |
| `Sets.MorphismMethods.__invert__()` | `sage/categories/sets_cat.py:1781-1828`; `sage/categories/morphism.pyx:509-569`, `:779-884` | Retained as generic inverse/isomorphism behavior on invertible morphisms, with set automorphisms routed to `Sets().AutCategory()`. It is not reintroduced as `MorphismMethods` in the project set object category. |
| `Sets.MorphismMethods.is_injective()` and Sage morphism `is_surjective()` | `sage/categories/sets_cat.py:1829-1847`; `sage/categories/morphism.pyx:546-569`, `:871-884` | Retained on `Sets().HomCategory().ElementMethods` as set-map predicates. `is_bijective()` is the project derived predicate and promotes automorphism membership through `Sets().AutCategory()`. |
| `Sets.MorphismMethods.image(domain_subset=None)` | `sage/categories/sets_cat.py:1848-1885`; `sage/sets/image_set.py:90-320` | Routed to image-subobject construction: the set map element owns the operation, while the result lies in `Sets().Subobjects()` / `Sets().Subquotients()`. Sage callable wrapping, `PoorManMap`, and arbitrary `Set(X)` fallback are interop-only constructor plumbing. |
| `ImageSubobject.ambient()`, `lift()`, and `retract()` | `sage/sets/image_set.py:242-320`; existing ImageSubobject admission section below | Retained on the image/subquotient object owner, not on the hom object. These methods describe the constructed image object after the set-map operation has produced it. |
| `FiniteSetMaps(domain, codomain)` domain/codomain, cardinality, iteration, `from_dict`, `_from_list_`, and element construction from callables | `sage/sets/finite_set_maps.py:38-202`, `:240-476`; `sage/sets/finite_set_map_cy.pyx:1-180`, `:450-510` | Split ownership: finite enumeration and finite constructor surfaces belong to `FiniteSetMapSets`; Hom object data `domain()`/`codomain()` belongs to the set hom layer; callable/dict/list element construction is retained only as finite set-map constructor evidence with explicit finite-domain/codomain hypotheses. Private `_from_list_` stays interop/internal. |
| Finite endomap `one()` and composition/power operations | `sage/sets/finite_set_maps.py:479-587`; `sage/sets/finite_set_map_cy.pyx:600-690` | Routed to `Sets().EndCategory()` for identity and generic endomorphism composition, with finite enumeration retained by `FiniteSetMapSets`. Sage's `one()` spelling is implementation evidence for end identity, not a finite-set-only category method. |
| Finite map element `image_set()` and `fibers()` | `sage/sets/finite_set_map_cy.pyx:287-330`, `:490-510` | `image_set()` refines the same image-subobject result for finite maps. `fibers()` is not admitted as generic set-hom surface here; it requires a separately named finite-fiber/preimage-family owner if later work needs it. |

## Constructor Mapping Decisions

| Sage constructor | Project subcategory | Notes |
| --- | --- | --- |
| finite iterable input formerly routed through `Set([..])`, `Set(tuple(..))`, ordered dictionaries, or other finite iterable wrappers | `Sets().Constructors().Set(elements=elements)` | This recovers Sage `Set(X)` for finite iterable input. The project spelling forces the input role to be named and does not expose Sage's optional `category=` argument. |
| singleton finite set `{x}` | `Sets().Constructors().Set(elements=(x,))` | A singleton set is recovered through the Sage `Set(X)` constructor applied to a one-element finite iterable; no separate `SingletonSet` constructor exists in Sage. |
| `FiniteEnumeratedSet(elements)` | `FiniteEnumeratedSetObjects` | Tuple-backed finite facade set. Include `__call__` and element construction in the spec. Sage enumeration conveniences map to countable-set indexing and finite Python conversion protocols. |
| `IntegerRange(...)` | `IntegerRangeSets` | Arithmetic progression of integers. Finite/infinite status depends on bounds; the one-object category should refine through countable facade sets and let Sage/category membership expose finiteness. |
| `NonNegativeIntegers()` | `NonNegativeIntegerSets` | Countably infinite facade subset of `ZZ`. |
| `PositiveIntegers()` | `PositiveIntegerSets` | Positive integer range; inherits most integer-range behavior and supplies Sage's `an_element`/`_sympy_`. |
| `Primes()` | `PrimesSets` | `Sets().Primes()` is the one-object category whose object is Sage's set of prime integers. `PrimeSubset` and `PrimesInArithmeticProgressions` are types of subobjects of that prime set, not separate top-level categories unless Sage exposes distinct parent objects with required methods. |
| `RR` / `RealField()` | `Rings().Constructors().RR()` / `Rings().Constructors().RealField(...)`, with topological refinements applied there | The real floating-point field is a ring/field constructor surface in Sage and in this spec. Its underlying set/topological-space structure is recovered by refinement of the ring object, not by duplicating a `Sets().Constructors()` entry. |
| `RealSet(...)` finite interval-union input | `Sets().Constructors().RealSet(intervals=intervals)` refined through `RealSets` | A real set is a subset of the real line. The project constructor admits a named sequence of `InternalRealInterval` components rather than exposing Sage's variadic surface or normalization option bag; the wrapper delegates internally to Sage's documented constructor route before refinement. Real intervals and real open sets are distinct mathematical notions: open intervals are basis elements for the Euclidean topology, while open subsets may be unions such as `(1, 2) ∪ (3, 4)`. |
| `RealSet.interval(lower, upper, lower_closed=..., upper_closed=...)` | `Sets().Constructors().interval(lower, upper, lower_closed=..., upper_closed=...)` | This is the universal interval/ray constructor. The two endpoints and two closure booleans unambiguously determine the real subset, including `[p, q)`, `[p, q]`, rays, and the whole real line when infinite endpoints are used. |
| `RealSet` static interval constructors | same-named real-subset interval constructors | Sage methods such as `RealSet.open(a, b)` and `RealSet.closed(a, b)` construct interval-shaped real subsets, not arbitrary open or closed real subsets. Static Sage constructors map to `Sets().Constructors()` entries such as `open`, `closed`, and `real_line`; each named constructor delegates to `interval` with the corresponding endpoint-closure booleans. Open interval constructors return `RealOpenSet` because an open interval is an open real subset, but a general `RealOpenSet` need not be an interval. |
| `RealSet.open_closed(a, b)` / `closed_open(a, b)` | same-named half-open interval constructors | These are interval-shaped real subsets with exactly one closed endpoint. They are not generic open/closed-set constructors. |
| `RealSet.unbounded_below_closed/open(b)` and `unbounded_above_closed/open(a)` | same-named real-ray constructors | Rays are subsets of the real line with one infinite endpoint and one endpoint-closure convention. They route through `interval` with explicit endpoint data. |
| `RealSet.real_line()` | `Sets().Constructors().real_line()` | The real line is the ambient real set and the universe object for `RealSet` Boolean operations. It also refines through the appropriate topological and ordered structures supplied elsewhere. |
| Real intervals, rays, real line, and future complex-ball-like named subsets | `Sets().Constructors()` first, then refinement into topological subobjects | These are named set constructions. The constructor result must refine not only into `Sets()` but also into the relevant subset/subobject and topological-space categories, e.g. real intervals refine through `RealSets`, `Sets().Subobjects()`, `TopologicalSpaces()`, and `TopologicalSpaces().Subobjects()`. Where Sage's real-subset category data proves connectedness or compactness, the result also refines into `TopologicalSpaces().Connected()` or `TopologicalSpaces().Compact()`. |
| `RecursivelyEnumeratedSet(...)` | `RecursivelyEnumeratedSets` | Recursively enumerable countable sets and forests. The forest-specific methods are part of the same Sage constructor family. |
| `DisjointUnionEnumeratedSets(family)` | `DisjointUnionSets` | Countable coproduct/disjoint union of an indexed family. |
| `CartesianProduct(sets, category, flatten=False)` | `Sets().Constructors().CartesianProduct(factors=factors, category=category, flatten=flatten)` refined through `CartesianProductSets` | Sage's product parent constructor takes the finite factor collection under the original constructor name. The project surface keeps the Sage constructor name, forces the factor role to be named, and does not invent a `FromFactors` constructor. |
| `cartesian_product(factors)` | `Sets().Constructors().cartesian_product(factors=factors)` refined through `CartesianProductSets` | Lowercase Sage functor compatibility path for finite factor collections; it delegates to the same named `CartesianProduct(factors=...)` overload. |
| `ConditionSet(universe, predicates...)` | internal backing for `Sets().Subobjects().Of(universe, predicates)` | A condition set is Sage's implementation of a predicate-defined subset. The public project API names the mathematical object as a subobject/subset of its ambient set; Sage `arguments()` and raw predicate tuple plumbing remain inventory-only. |
| `ImageSubobject(f, X)` | `ImageSets` | Sage image subobject under a map; must include `ambient`, `lift`, and `retract`. Public project input is a set morphism `f` and a domain subset `X`; Sage's generic callable wrapping and arbitrary `Set(X)` fallback are interop details, not public constructor shapes. |
| `TotallyOrderedFiniteSet(elements)` | `TotallyOrderedFiniteSets` | Finite set with order relation `le`; element comparison methods are mathematical when elements are non-facade. |
| `FiniteSetMaps(domain, codomain)` | `FiniteSetMapSets` plus the set homset/endset refinement | Finite set of functions. The finite-set subcategory owns finite enumeration and constructor surfaces; the homset layer owns `domain`/`codomain`, and the endset layer owns identity for endomap variants. Sage's `one()` remains inventory evidence for the endset identity surface, not a finite-set-only method. |
| `SetPartitions()` | `Sets().Constructors().SetPartitions()` | Countable set of all finite set partitions. This Sage parent has no fixed base set and therefore does not refine into `Partitioned`. |
| `SetPartitions(s)` | `Sets().Constructors().SetPartitions(base_set=s)` | Fixed-base set partitions. The result refines through `Sets().Partitioned()` because each element is a partition subobject of `P(s)`. |
| `SetPartitions(s, k)` | `Sets().Constructors().SetPartitions(base_set=s, block_count=k)` | Fixed-base partitions with exactly `k` blocks. The block count is a named constructor parameter, not Sage's positional `part` overload. |
| `SetPartitions(s, part)` | `Sets().Constructors().SetPartitions(base_set=s, block_sizes=part)` | Fixed-base partitions whose block sizes are the integer partition `part`. This is the second finite Sage `part` case, separated from block count. |
| `SetPartition(blocks, check=True)` | `Sets().Constructors().SetPartition(blocks, check=check)` | Construct the original Sage `SetPartition` element. Elements cannot be refined with `refine_category`, so the constructor returns Sage's element class while `Partitioned.ElementMethods` records the required partition surface. |
| `SetPartitions().from_restricted_growth_word_blocks(w)` | `Sets().Constructors().from_restricted_growth_word_blocks(word=w)` | Element constructor from a restricted-growth word using Sage's block convention. |
| `SetPartitions().from_restricted_growth_word_intertwining(w)` | `Sets().Constructors().from_restricted_growth_word_intertwining(word=w)` | Element constructor from a restricted-growth word using Sage's intertwining convention. |
| `SetPartitions().from_arcs(arcs, n)` | `Sets().Constructors().from_arcs(arcs=arcs, base_set_cardinality=n)` | Element constructor from arcs. |
| `from_rook_placement(..., "arcs"/"gamma"/"rho"/"psi", n)` | same-named rook-placement constructors on `Sets().Constructors()` | Sage's `from_rook_placement` dispatch and its `from_rook_placement_gamma`, `from_rook_placement_rho`, and `from_rook_placement_psi` named variants are preserved under their Sage names. |
| `Family(indices, function)` | `Families` | Indexed family object. Include `items`, `hidden_keys`, `has_key`, and `inverse_family`. |
| `Family.keys()`, `items()`, `values()` | `Families` indexed-family accessors | The keys are the index set, and values are the family entries. These are family methods, not ordinary set-enumeration methods. |
| `Family.zip(other)` | `Families.zip_with(other)` | Zipping two families is an indexed-family operation over a common index set. The project name should expose the indexed construction rather than Python container vocabulary alone. |
| `Family.map(function)` | `Families.map(function)` | Mapping a function over entries preserves the same index set and changes the value family. This belongs to indexed families. |
| `EnumeratedSetFromIterator(f)` | `IteratorEnumeratedSets` | Callable-backed countable set. The project constructor admits a nullary iterator factory. Sage's `args`/`kwds` parameterization is arbitrary callable plumbing, not set-theoretic data, so it is not exposed as a public constructor shape. Sage `clear_cache` resets a lazy-list implementation cache and remains private interop, not public set structure. |

Existing Sage calls of the form `EnumeratedSetFromIterator(f, args=..., kwds=...)` are
recovered by closing over those arguments before constructing the project object: the
resulting nullary iterator factory is the set-theoretic input.
The old `args`/`kwds` plumbing remains migration guidance only and is not a
category-spec signature.

## Sage `ImageSubobject` Admission Decision

Sage's `ImageSubobject(f, X)` is the image of a set map on a domain subset:
`{f(x) | x in X}`. It is a subobject of the map codomain and a constructive subquotient
object with `ambient`, `lift`, and `retract`.

Project admission:

- The constructor path is
  `Sets().Constructors().ImageSubobject(f: SetMorphism, domain_subset: Subset)`.
- The result refines through `_ImageSets`, whose supercategories are
  `Sets().Subobjects()` and `Sets().Subquotients()`.
- `ambient()` returns the codomain ambient set containing the image.
- `lift(x)` includes an image element into the ambient set.
- `retract(x)` retracts an ambient element to the image when defined.

Rejected public routes:

- do not expose generic Sage `Set(X)` wrapping as a project constructor fallback;
- do not treat Sage's arbitrary callable-to-map conversion as a public signature;
- do not admit a free-floating image helper outside the subobject/subquotient
  construction vocabulary.

## Sage `RealSet` Method Mapping Decisions

Sage `RealSet` represents finite unions of intervals in the real line.
The mathematical object is a real subset with topology inherited from the ambient real
line. Each Sage method is placed at the highest category where the operation is
mathematically well-defined.

### Operations owned by `Sets()`

These are set-level operations inherited by every object in `Sets()`; RealSet need not
re-declare them.

| Sage surface | Project owner | Decision |
| --- | --- | --- |
| `__contains__(x)` / `contains(x)` | `Sets().ParentMethods.__contains__` | Membership is root set structure. |
| `cardinality()` | `Sets().ParentMethods.cardinality` | Every set has a cardinality. |
| `is_empty()` | `Sets().ParentMethods.is_empty` | Every set can be empty. |
| `is_finite()` | `Sets().ParentMethods.is_finite` | Every set is finite or not. |
| `is_subset(other)` | `Sets().ParentMethods.is_subset` | Subset relation is set-level. |
| `_an_element_()` | `Sets().ParentMethods._an_element_` | Sage test surface. |
| `_sympy_()` | `Sets().ParentMethods._sympy_` | Sage interop. |

### Operations owned by `Sets().Subobjects()` (subsets)

These are subobject operations that require an ambient set; inherited by every subset.

| Sage surface | Project owner | Decision |
| --- | --- | --- |
| `ambient()` | `Subsets.ParentMethods.ambient` | Every subobject has an ambient set. |
| `lift(x)` / `retract(x)` | `Subsets.ParentMethods` subquotient surface | Inherited from subquotient structure. |
| `union(X)` | `Subsets.ParentMethods.union` | Set-theoretic union of subsets within a common ambient. |
| `intersection(X)` | `Subsets.ParentMethods.intersection` | Set-theoretic intersection. |
| `complement()` | `Subsets.ParentMethods.complement` | Complement within the ambient set. |
| `difference(X)` | `Subsets.ParentMethods.difference` | Set difference. |
| `symmetric_difference(X)` | `Subsets.ParentMethods.symmetric_difference` | Symmetric difference. |
| `is_universe()` | `Subsets.ParentMethods.is_universe` | Returns `self == self.ambient()`. |

### Operations owned by `TopologicalSpaces()`

| Sage surface | Project owner | Decision |
| --- | --- | --- |
| `is_connected()` | `TopologicalSpaces().ParentMethods.is_connected` | Connectedness is a topological property. |

### Operations owned by `TopologicalSpaces().Subobjects()` (subspaces)

These are self-centric subspace operations owned by the topological subobject category.

| Sage surface | Project owner | Decision |
| --- | --- | --- |
| `is_open()` | `TopologicalSpaces().Subobjects().ParentMethods.is_open` | Whether this subspace is open in its ambient. |
| `is_closed()` | `TopologicalSpaces().Subobjects().ParentMethods.is_closed` | Whether this subspace is closed. |
| `closure()` | `TopologicalSpaces().Subobjects().ParentMethods.closure` | Closure of this subspace. |
| `interior()` | `TopologicalSpaces().Subobjects().ParentMethods.interior` | Interior of this subspace. |
| `boundary()` | `TopologicalSpaces().Subobjects().ParentMethods.boundary` | Boundary of this subspace. |

### Operations owned by `_RealSets` (this spec)

These operations are genuinely new for a real subset with a canonical interval-basis
expression. Sage's implementation methods are recovered from spec surface + standard
category operations.

| Sage surface | Project mapping | Recovery |
| --- | --- | --- |
| `__iter__()` (yields `InternalRealInterval` components) | `interval_components() -> FiniteSet[RealInterval]` | `iter(real_set.interval_components())` |
| `n_components()` | `interval_components().cardinality()` | Cardinality of the finite interval-component set. |
| `get_interval(i)` | `interval_components()[i]` | nth-element on the finite set of intervals. |
| `inf()` | `_RealSets.ParentMethods.inf` | Direct. |
| `sup()` | `_RealSets.ParentMethods.sup` | Direct. |
| `is_compact()` | `_RealSets.ParentMethods.is_compact` (concrete `@override`) | Heine-Borel; depends on `inf`/`sup`. |
| `is_disjoint(other)` | `Sets().ParentMethods.is_disjoint` | `self.intersection(other).is_empty()` |
| `are_pairwise_disjoint(real_sets)` | `Sets().ParentMethods.are_pairwise_disjoint` | Pairwise `is_disjoint` over a finite collection. |
| `convex_hull()` | `_RealSets.ParentMethods.convex_hull` (concrete) | `RealSet.closed(min(s.inf()), max(s.sup()))` |
| `boundary_points()` | `{p for I in interval_components() for p in I.boundary()}` | Requires `RealInterval.boundary() -> tuple[RealNumber, RealNumber]`. |
| `measure()` | `_RealSets.ParentMethods.measure` (abstract) | Lebesgue length of a finite union of intervals. |
| `normalize(...)` / `_scan*` / `_prep` | (private; not public Sage surface) | Implementation detail. |
| `_repr_condition` / `_sympy_condition` | `Sets().ParentMethods._sympy_` | Sage backend interop. |

## Sage `SetPartition` Method Mapping Decisions

Sage `SetPartition` is the element class for the fixed-base `SetPartitions(s)` parent.
The mathematical object is a partition of a base set, equivalently a subset of the
powerset of that base set.

| Sage surface | Project mapping | Decision |
| --- | --- | --- |
| `base_set()` | `Partitioned.ElementMethods.base_set` | The base set is the union of all blocks. |
| `base_set_cardinality()` / `size` | `Partitioned.ElementMethods.base_set_cardinality` | This is the size of the underlying base set. |
| `cardinality()` | block cardinality | Sage uses `cardinality()` for the number of blocks because a partition is itself a finite set of blocks. This remains finite-set cardinality. |
| iteration over blocks | `Partitioned.ElementMethods.blocks()` and normal iteration | The project names the mathematical subset of `P(base_set())` as `blocks()`. Iteration is implementation/protocol access to the same blocks. |
| `__mul__()` / `inf` | `Partitioned.ElementMethods.meet(other)` | This is the meet in the refinement lattice. The Sage operator is mapped to the named lattice operation. |
| `sup(t)` | `Partitioned.ElementMethods.join(other)` | This is the join in the refinement lattice. |
| parent `is_less_than(s, t)` / `lt(s, t)` | `s.strictly_refines(t)` | Sage's parent-level comparison is the strict refinement relation on partition elements. |
| `standard_form()` | `Partitioned.ElementMethods.standard_form` | Ordered-block display data remains available as a partition element method. |
| `shape()` / `shape_partition()` / `to_partition()` | integer partition of block sizes | This maps to the integer-partition surface once that set-combinatorics subtree is admitted. Until then, keep the Sage `IntegerPartition` type alias in `types.py`. |
| `arcs()`, `openers()`, `closers()` | partition arc-diagram surface | These are combinatorial views of an ordered finite set partition. They remain partition element methods, not poset or graph constructors. |
| `to_restricted_growth_word_*`, `to_rook_placement_*` | named encoding/export methods on partition elements | These are encodings of a partition. Inverse construction routes through `Sets().Constructors()` named constructors. |
| `to_permutation()` | finite ordered-base partition encoding | Sage maps a partition to a permutation by cycling entries inside each block using the induced order. This is an encoding/export method on partition elements with the finite ordered-base hypothesis. |
| `to_rook_placement(bijection=...)` and `to_rook_placement_gamma/rho/psi()` | named rook-placement encodings | The project keeps separate names for the finite set of bijection conventions rather than exposing a string-dispatched option. |
| `apply_permutation(perm)` | finite ordered-base partition transform | Applying a permutation relabels the base set and returns another partition element. The operation is not a permutation method; it is a partition element transform parameterized by a permutation of the base set. |
| `conjugate()` / `pre_conjugate()` | partition involution/auxiliary transform | The public method is the partition conjugation operation when the ordered-base hypotheses are met. `pre_conjugate()` is an implementation helper for Sage's convention and stays compatibility-only unless independently grounded. |
| `crossings()`, `nestings()` | `Partitioned.ElementMethods.crossings()` and `Partitioned.ElementMethods.nestings()` | Sage defines these on `SetPartition` elements, not on the parent. They return witness data for a single partition: lists of pairs of arcs. The definitions require the finite base set to be totally ordered because the arcs are drawn by placing the ground-set elements in order on a line and linking consecutive elements in each block. |
| `crossings_iterator()`, `nestings_iterator()` | lazy variants of crossings/nestings | These are generator forms of the same ordered-base element invariants, not separate mathematical structures. |
| `number_of_crossings()`, `number_of_nestings()` | cardinalities of crossings/nestings | These are finite counts of the corresponding witness sets. |
| `is_noncrossing()`, `is_nonnesting()` | `Partitioned.ElementMethods.is_noncrossing()` and `Partitioned.ElementMethods.is_nonnesting()` | These are boolean predicates on a single partition element, with the same finite totally ordered base-set hypothesis as `crossings()` and `nestings()`. They do not yet induce admitted category axioms because `Sets().Partitioned()` alone does not encode the required order hypothesis on the base set. |
| `is_atomic()` | `Partitioned.ElementMethods.is_atomic()` | Sage defines atomicity for a nonempty standard set partition by pipe-indecomposability, ordering blocks by minimal element and asking whether the partition splits as `B |
| `max_block_size()` | `Partitioned.ElementMethods.max_block_size()` | Maximum block cardinality is an invariant of a finite partition element. |
| parent `number_of_blocks()` | constructor/counting family for fixed block count | This is counting/enumeration data for the parent `SetPartitions(s, k)`, not a method on arbitrary sets. It remains under set-partition constructor/enumeration vocabulary. |
| `standardization()`, `restriction(I)` | partition element transforms | These return new partition elements and remain partition methods. |
| parent `is_strict_refinement(s, t)` | strict refinement relation | This is the non-reflexive refinement predicate on partition elements. It belongs with the fixed-base partition parent relation surface. |
| `refinements()`, `coarsenings()` | Sage compatibility methods; project finite-set methods are `Partitioned.ElementMethods.refinement_set()` and `Partitioned.ElementMethods.coarsening_set()` | These are finite refinement-lattice neighborhoods of a partition element. Sage returns Python lists on concrete `SetPartition` elements. The project finite-set surfaces therefore use separate names and route those lists through set constructors; both finite sets include `self`. |
| `strict_coarsenings()` | Sage compatibility method; project finite-set method is `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods.ordered_coarsening_closure()` | Sage's name does not mean "proper coarsenings." It is the reflexive-transitive closure of merging two ordered-compatible blocks with `max(A_i) < min(A_j)`, so it requires the finite totally ordered base-set owner and includes `self`. The project name avoids reusing Sage's misleading concrete method name while preserving the ordered closure semantics. |
| module-level `cyclic_permutations_of_set_partition*` | combinatorial iterator helpers | These are helper algorithms used by partition combinatorics. They should not become public category methods unless a source-grounded partition-action surface requires them. |
| `ordered_set_partition_action(...)` | ordered partition action surface requiring separate grounding | The operation is real Sage evidence, but the target category and action law need a dedicated source-grounded mapping before admission. |
| `plot(...)` and LaTeX/display helpers | no category method | Display output is not set-theoretic structure. |

Admission decision for partition subclass predicates:

- Expose `crossings()`, `nestings()`, `is_noncrossing()`, `is_nonnesting()`, and
  `is_atomic()` now on `Sets().Partitioned().ElementMethods`, with docstrings that state
  the finite totally ordered base-set hypothesis explicitly.
- Admit the missing hypothesis owner as
  `Sets().Partitioned().FiniteTotallyOrderedBase()`. This is an axiom on the
  partitioned-set category because it constrains `base_set()`, and it also refines
  through `Sets().Countable().Finite()` because a fixed-base partition parent is finite
  when the base set is finite.
- Do not admit `Sets().Partitioned().Noncrossing()`,
  `Sets().Partitioned().Nonnesting()`, or `Sets().Partitioned().Atomic()` yet.
  Those later subclass owners must sit over
  `Sets().Partitioned().FiniteTotallyOrderedBase()` rather than over bare
  `Sets().Partitioned()`.
- If a future pass needs the subclass objects themselves, construct them first as
  predicate-defined subobjects of a fixed partition parent in
  `Sets().Partitioned().FiniteTotallyOrderedBase()`, not as global axioms on
  `Sets().Partitioned()`. Full axiom admission for `Noncrossing`, `Nonnesting`, or
  `Atomic` still needs a later source-grounded pass that fixes the exact registration
  shape above this owner.

Admission decision for partition refinement neighborhoods:

- Keep Sage's concrete `refinements()`, `coarsenings()`, and `strict_coarsenings()`
  names as Sage compatibility methods, because ordinary category `ElementMethods` cannot
  override those methods on the installed Sage `SetPartition` element class.
- Expose `refinement_set()` and `coarsening_set()` on
  `Sets().Partitioned().ElementMethods`, returning finite set objects of partition
  elements rather than Sage's raw Python lists.
- Expose `ordered_coarsening_closure()` on
  `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`. Its definition uses
  ordered block comparisons through `max` and `min`, and its closure is reflexive, so
  the method includes `self`.
- Do not use `strict_coarsenings()` as the project name for ordinary proper coarsenings
  or for the project finite-set wrapper.
  If proper coarsenings are needed later, they require a separately named predicate or
  set-constructor surface.

## Sage `Set_object` Method Mapping Decisions

Sage's `Set_object` and `Set_object_enumerated` method surface is inventoried in
`SAGE_INVENTORY.md`. The generic wrapper category is not admitted, but the methods are
mapped to the mathematical surfaces they witness.

| Sage surface | Project mapping | Decision |
| --- | --- | --- |
| `object()` | no public project method | The wrapped Python object is Sage implementation state, not mathematical structure. Named constructors expose their mathematical data directly instead of exposing a generic underlying object. |
| `__contains__(x)` | `Sets.ParentMethods.__contains__` | Membership is part of every set. |
| `some_elements()` | `Sets.ParentMethods.some_elements()` | Producing a finite sample is a root set convenience and test witness, not a finiteness claim. |
| `random_element()` | root or finite-set random element surface depending on source owner | Random selection is implemented for many concrete parents. The method should live where a mathematically meaningful distribution or finite uniform distribution is specified; otherwise the Sage method remains compatibility behavior. |
| `is_parent_of(x)` | membership/parent predicate compatibility | The mathematical question is whether `x` is an element of the parent set. Keep the Sage spelling as compatibility only if needed by upstream interop. |
| `__iter__()` | `Sets().Countable().ParentMethods.__iter__` | Iteration witnesses countability, not arbitrary sethood. |
| `_an_element_()` / `an_element()` | `Sets.ParentMethods.an_element` | Producing an element is a root set method. |
| `cardinality()` | `Sets.ParentMethods.cardinality` | Cardinality is defined for every set. |
| `is_empty()` / `is_finite()` | `Sets.ParentMethods.is_empty` and `Sets.ParentMethods.is_finite` | These predicates are defined for every set. |
| `subsets(size=None)` / `subsets_lattice()` | `Sets.ParentMethods.subsets`; `Sets().Finite().ParentMethods.subsets_lattice() -> Posets().Lattice().Finite()` | The power set is a set-theoretic construction. The subset lattice returned by the checked Sage wrapper is finite-only and has finite lattice-poset codomain; any ideal infinite power-set poset requires a separate ordered-complete-poset surface rather than this finite Sage method row. |
| `algebra(R, category=None)` on plain sets | `free_module(R)` routed to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=self)` | Sage's plain-set path is the free module on the set, not an algebra constructor. Sage's `category=` keyword remains inventory for structured source-category dispatch; it is not a project API shape. |
| `free_module(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=self)` | This is the project spelling for the existing Sage plain-set `S.algebra(R)` functionality. |
| `free_algebra(R)` | `Algebras(R).Constructors().FreeAlgebra(generators=self)` | This is the mathematical free associative unital `R`-algebra generated by the set. |
| `_sympy_()` | interop-only SymPy export | SymPy conversion is import/export plumbing, not mathematical set structure. Keep it as compatibility behavior where Sage supplies it, but do not make `_sympy_` a public category method obligation. |
| `_repr_()`, `_latex_()`, `__hash__()` | no independent project method | Display and hashing belong to concrete parent implementation behavior. They do not define set-theoretic structure and are not category obligations. |
| `union(other)` | `Sets.ParentMethods.union` | Union is defined for any two objects in the category of sets. |
| `intersection`, `difference`, `symmetric_difference`, `complement` | `Sets().Subobjects()` / `Subsets` | These require a common ambient set, so they are subset/subobject operations. |
| `Set_object_union`, `Set_object_intersection`, `Set_object_difference`, `Set_object_symmetric_difference` | operation result parents, not public project category names | These Sage classes witness concrete outputs of set operations. The project maps their method surface to union on `Sets()` and subobject operations on `Sets().Subobjects()` rather than exposing the wrapper class names. |
| `__or__`, `__add__` | `Sets.ParentMethods.union` | Python operators are Sage compatibility spellings for union. The named mathematical method is the public surface. |
| `__and__` | subset/subobject intersection | Intersection requires a common ambient set and therefore routes through `Sets().Subobjects()`. |
| `__sub__` | subset/subobject difference | Difference requires a common ambient set and therefore routes through `Sets().Subobjects()`. |
| `__xor__` | subset/subobject symmetric difference | Symmetric difference is a Boolean operation in a common ambient set. |
| `__rmul__` | Cartesian product or repeated product compatibility | Sage operator behavior is not admitted as a public set method without a source-grounded product signature. Use named product constructors. |
| `__richcmp__`, `issubset`, `issuperset` | root set comparison surface | The project exposes rich comparison with set-theoretic semantics: equality is equality of elements, `<=` is subset, `<` is proper subset, `>=` is superset, and `>` is proper superset. This replaces Sage wrapper comparison semantics. |
| `__bool__`, `__len__`, `__eq__`, `__ne__` | Python protocols over emptiness, finite cardinality, and equality | Keep protocol support where Sage/Python interop requires it, but the category methods are named predicates/cardinality/equality surfaces. |
| `list()`, `tuple()` on finite wrappers | `list(X)`, `tuple(X)` for finite countable sets | Finite enumerated sets may expose finite enumeration through Python conversion protocols. Do not make Sage's `.list()` and `.tuple()` names primary project methods. |
| `set()`, `frozenset()` on finite wrappers | no project method | Python hash-set export is not a project set object and is not admitted as category vocabulary. |
| `rank`, `unrank`, `first`, `last`, `next` | `rank(e)` and indexed access | `rank(e)` is the index-of map and remains meaningful for infinite countable sets. Sage `unrank(n)` maps to `X[n]`; `first`, `last`, and `next` are derived enumeration conveniences and are not project method names. |

## Rich Comparison Mapping Decisions

Sage exposes rich comparison through several surfaces: `Set_object.__richcmp__`,
`Set_object_enumerated.__richcmp__`, finite wrapper `issubset`/`issuperset`, and
ordered-set element `_richcmp_`.

The project mapping is:

- Set-object rich comparison belongs on `Sets()` and is redefined set-theoretically.
  It must not inherit Sage's arbitrary-wrapper comparison behavior.
- Subset order is comparison of set objects by inclusion: `A <= B` means `A` is a subset
  of `B`, and `A < B` means proper subset.
- Poset element comparison remains separate: `Posets.ParentMethods.le/lt/ge/gt` and
  ordered-set element comparisons compare elements of an ordered set, not set objects by
  inclusion.
- Finite enumerated wrapper equality and Python `set`/`frozenset` comparison behavior
  are not copied as implementation quirks; finite set comparison uses the same
  set-theoretic comparison surface as every set.

## Signature Typing Decisions

Rank, unrank, projection index, component index, and recursion-depth parameters are
mathematically integer-valued.
The spec uses `Integer`, and uses `Integer | InfinityElement` only where Sage's written
documentation explicitly allows infinite bounds, such as `IntegerRange` begin/end values
and recursive-enumeration depth bounds.
It does not introduce an `IntegerRangeBound` alias because that only renames a simple
union without adding mathematical vocabulary.

Cartesian product element construction is typed as a sequence of set elements.
This matches the product object mathematically: an element of `X_1 x ... x X_n` is an
ordered tuple-like family with one component in each factor, not an unstructured
variadic call surface.

Real-set method signatures use `RealSubset` and `RealInterval`. The former is the
mathematical object for finite Boolean operations on subsets of the real line; the
latter is the mathematical object returned by interval accessors.
Endpoint tuples are Sage constructor data, not a subcategory or type vocabulary item, so
they appear only through explicit constructor methods such as `interval`,
`open`, and `closed`.

Sage forwarding, display, import/export, source-introspection, and test-suite hooks are
inventory items, not mathematical method surface.
This includes `_test_*`, `example`, `extra_super_categories`, `__classcall__`,
`__classcall_private__`, `_element_constructor_*`, `_sage_argspec_`, `_sage_input_`,
`_sage_src_`, `_sage_src_lines_`, `_instancedoc_`, display and LaTeX-option helpers, and
`Sets.ParentMethods._element_constructor_from_element_class(*args, **keywords)`. The
last forwards to an arbitrary element-class constructor, so it has no finite
mathematical signature.
`SetsWithGrading.ParentMethods._test_graded_components(**options)` is Sage `TestSuite`
plumbing. These are omitted from the public spec surface rather than preserved as
variadic API.

## Completeness Reconciliation: Sets

- Searched: local source inventory `category_specs/sets/docs/SAGE_INVENTORY.md`;
  installed Sage 10.7 source files `sage/categories/sets_cat.py`, `finite_sets.py`,
  `enumerated_sets.py`, `finite_enumerated_sets.py`, `infinite_enumerated_sets.py`,
  `facade_sets.py`, `sets_with_grading.py`, `g_sets.py`, `sage/sets/set.py`,
  `finite_enumerated_set.py`, `integer_range.py`, `non_negative_integers.py`,
  `positive_integers.py`, `primes.py`, `real_set.py`, `cartesian_product.py`,
  `condition_set.py`, `image_set.py`, `totally_ordered_finite_set.py`,
  `finite_set_maps.py`, `disjoint_union_enumerated_sets.py`, `set_from_iterator.py`,
  `sage/combinat/set_partition.py`, and `sage/sets/family.pyx`; static method-name
  comparisons between those files and this spec.
- Found: previously unmapped public surfaces in set morphisms, real subsets, set
  partitions, families, generic set wrappers, finite/countable protocols, and Sage
  runtime hooks. The spec now maps them to set, subset/subobject, topological-subobject,
  partitioned-set, family, homset, constructor, compatibility, private, or
  source-grounding-deferred targets.
- Conclusion: inference based on the checked installed Sage corpus: the core Sets
  mapping is source-reconciled for the files named above, and remaining unmatched names
  are either Python protocol/private/runtime hooks, display/backend interop, or surfaces
  that require later source-grounding outside this Sets mapping file.
- Confidence: Medium.
- Gaps: I did not exhaust every combinatorics module whose filename contains "set",
  every import in `sage/sets/all.py`, Sage development-branch history, or downstream
  constructor category-obligation example behavior.
  The ordered-partition action and full noncrossing/nonnesting/atomic subclass surfaces
  still require dedicated source-grounded admission work before implementation.

## Sage Primes Source Note

- Searched: Context7 `/sagemath/documentation`, DeepWiki `sagemath/sage`, hosted Sage
  docs for `Primes`, and installed source `sage/sets/primes.py`.
- Found: Hosted docs describe prime subsets selected by congruence data (`modulus`,
  `classes`, and `exceptions`); the installed source at
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/primes.py`
  exposes only `Primes(proof=True)` for the full set of prime integers.
- Conclusion: I believe the online docs and installed source are version-skewed.
  Mathematically, congruence-class prime subsets should be represented as subobjects of
  `Primes()`, with vocabulary such as `PrimesInArithmeticProgressions` only where method
  signatures require that refinement.
- Confidence: Medium.
- Gaps: I have not searched Sage git history or package metadata for the exact
  documentation/source version boundary.

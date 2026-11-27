# Sets: Sage Category → Spec Hierarchy Mapping

This file records, for each Sage category relevant to `Sets()`, the mathematical
justification for how it maps to our hierarchy.

## Sage `EnumeratedSets` → our `Sets().Countable()`

Sage's `EnumeratedSets` axiom captures: "there exists an explicit enumeration
(iteration) of the set's elements." Countability is equivalent: a set is countable
iff there exists an injection f: X → ℕ, which is precisely an enumeration.
Every Sage enumerated set is countable, and every countable set in our hierarchy
must supply an iterator (via `__iter__`).

Consequence: objects that lie in `SageEnumeratedSets()` are refined to
`Sets().Countable()`. The spec class `_CountableSets` therefore declares
`super_categories = [Sets(), SageEnumeratedSets()]`.
Project countability does not include conversion to a finite Python collection:
`list(ZZ)` and `tuple(ZZ)` have no mathematical finite value. Those conversions
belong to finite countable sets.

### Enumeration Protocol Mapping

Countable-set enumeration should be specified through mathematical/Python protocol
surface, not through Sage's fallback helper names.

Python's built-in `list(X)` and `tuple(X)` conversions consume the iterable protocol;
there is no project category method to add for this behavior. Do not define Sage-style
`.list()`/`.tuple()` methods, and do not introduce `__list__` or `__tuple__` hooks.
Finite countable sets only need to be iterable, with finite cardinality/length where
the protocol requires it.

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
terminate when the element is absent. Concrete Sage parents may and often do provide
faster rank/unrank formulas, such as arithmetic formulas for integer ranges or mixed
radix formulas for finite Cartesian products. The project spec records the semantic
rank map, not the fallback algorithm.

## Sage `FiniteEnumeratedSets` → our `Sets().Countable().Finite()`

Finite enumerated sets are both finite and countable.

## Sage `InfiniteEnumeratedSets` → our `Sets().Countable().Infinite()`

Infinite enumerated sets are countably infinite.

## Sage `FacadeSets` → our `Sets().Facade()`

Facade sets represent their elements as elements of another parent.
Mapping is direct: `SageFacadeSets()` ↔ `Sets().Facade()`.

## Sage `TopologicalSpaces` → our `Sets().Topological()`

Sage's `TopologicalSpaces()` captures topological structure. `RealSet` lives here.
The forward target is the dedicated `topological_spaces` subtree:
`Sets().Topological()` navigates to `TopologicalSpaces()`, and
`Sets().Metric()` navigates to `TopologicalSpaces().Metric()`.

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
| `_ImageSets` | `subcategories/image.py` | Images are subobjects under a map. |
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

Target subcategory file names follow mathematical vocabulary. Groupings by constructor
history, implementation convenience, or named-object families are not target
subcategory boundaries.

## Sage Category → Project Category Decisions

| Sage category | Project category | Justification | Consequence |
| --- | --- | --- | --- |
| `SetsWithPartialMaps()` | `Sets()` inherited through Sage | Sage places `Sets()` below sets with partial maps. The project does not need a separate public partial-map category for the set-object inventory. | `Sets.super_categories()` keeps `SageSets()`, so Sage's inherited category behavior remains available. |
| `Sets()` | `Sets()` | Base category of parents whose elements support membership and basic element construction. | Root method surface includes operations meaningful for arbitrary sets, including union. Ambient-dependent operations such as intersection, difference, symmetric difference, and complement use `Subset` vocabulary under `Subsets = Subobjects`. |
| `Sets().Algebras(R)` / plain-set `S.algebra(R)` | no set/algebra subcategory; route to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)` | Sage's existing path constructs the free `R`-module with basis indexed by `S`; it is not the free associative `R`-algebra on generators `S`. | Project code uses `S.free_module(R)` to recover this Sage functionality. The true free algebra on `S` uses `S.free_algebra(R)` and routes through `Algebras(R).Constructors().free_algebra_from_set(S)`. |
| `EnumeratedSets()` | `Sets().Countable()` | Sage defines enumerated sets as finite or countable sets/multisets with a canonical enumeration. Countability is the set-level mathematical property; enumeration methods are the computable witness. | Countable sets declare iteration, nth-element/indexing, and rank. Sage `unrank` maps to `__getitem__`; Sage fallback helpers stay inventory-only. Full finite collection conversions are not countability data. Multiset caveat remains a documented boundary. |
| `FiniteSets()` | `Sets().Finite()` | Finite sets have finite cardinality independent of enumeration. | `Finite` declares `is_finite() -> True`, cardinality, `len(X)`, finite random element generation, and finite subquotient behavior. |
| `FiniteEnumeratedSets()` | `Sets().Countable().Finite()` | Finite enumerated sets combine finite cardinality with explicit enumeration. | The finite-countable subcategory owns finite cardinality, `len(X)`, and finite random element generation. Python conversions such as `list(X)` and `tuple(X)` consume iteration; Sage list/range/cache helper names stay inventory-only. |
| `InfiniteEnumeratedSets()` | `Sets().Countable().Infinite()` | Infinite enumerated sets are countably infinite, not listable as finite collections. | Infinite-countable declarations keep iteration, indexing, and rank semantics, but do not admit Sage's eager `tuple`/`list` methods as project category obligations. |
| `FacadeSets()` | `Sets().Facade()` | Elements are represented by elements of another parent. | `facade_for`, facade element construction, and facade parent checks belong here. |
| Sage `TopologicalSpaces()` for `RealSet` | `TopologicalSpaces()` / `Sets().Topological()` plus `Sets().Subobjects()` when an ambient real line is present | A `RealSet` is a topological subset of the real line, and a set with a topology is precisely a topological space. | `RealSet` refinement preserves Sage's finite-interval-normalized Boolean operations. Generic subobject/subquotient methods such as `ambient`, `lift`, and `retract`, and root comparison methods such as `is_subset`, are inherited from `Sets().Subobjects()`, `Sets().Subquotients()`, and `Sets()`. |
| Sage `Set_base` boolean mixins | Root set operations and `Sets().Subobjects()` / `Subsets` | Sage's boolean mixins are implementation artifacts, not mathematical subcategories. A set has union with any other set in `Sets()`. Intersections, differences, symmetric differences, and complements require a common ambient set and therefore live on subsets/subobjects. | Do not introduce a project `WithBooleanOps` axiom. Map Sage mixin methods to the mathematical operation surface they actually represent. |
| `SubobjectsCategory` | `Sets().Subobjects()` / alias `Subsets` | In the category of sets, subobjects are exactly subsets. Predicate-defined subsets are constructed as `Sets().Subobjects().Of(ambient, predicates)` and backed by Sage `ConditionSet` under the hood. The same construction must remain attachable to arbitrary set subcategories via Sage's functorial construction/category-of machinery. | The set subtree exposes `Subsets = Subobjects` and uses `Subset` type vocabulary in signatures. Its implementation lives in `subcategories/constructions/subobjects.py`, not a monolithic `constructions.py`. Raw Sage `ConditionSet.arguments()` stays inventory-only. |
| `SetPartitions(s)` fixed-base parents | `Sets().Partitioned()` | A partition of `s` is represented as a subset of the powerset of `s`. The fixed-base parent `SetPartitions(s)` is the set of all such partition subobjects and its elements are the actual `SetPartition` objects. | `sets/subcategories/partitioned.py` owns the partition method surface. `Sets().Constructors().SetPartitions(...)` and its fixed-block variants are the public constructor paths. `SetPartition` remains anchored to Sage's element class in `types.py`. |
| `SetPartitions()` all finite partitions | `Sets().Countable()` | There is no fixed base set, hence no single powerset ambient object. Sage represents this as the countable parent of all finite set partitions. | The constructor path is `Sets().Constructors().AllSetPartitions()`. It is not refined into `Sets().Partitioned()` because the fixed-base powerset ambient is absent. |
| `QuotientsCategory` | `Sets().Quotients()` | Quotient sets are equivalence-class objects. Like subobjects, quotient categories are attachable construction categories, not singleton categories. | `subcategories/constructions/quotients.py` owns the set-specific quotient scaffold and `types.py` exposes `QuotientSet`. |
| `SubquotientsCategory` | `Sets().Subquotients()` | Sage's constructive subquotients are the primitive construction behind quotients and subobjects: an object has an ambient object, a lift, and a retract. | `subcategories/constructions/subquotients.py` owns the ambient/lift/retract surface. |
| `IsomorphicObjectsCategory` | `Sets().IsomorphicObjects()` | An isomorphic image is simultaneously a subobject and a quotient in Sage. | `subcategories/constructions/isomorphic_objects.py` owns the lift/retract/isomorphism convention. |
| `WithRealizationsCategory` / `RealizationsCategory` | `Sets().WithRealizations()` and `Sets().Realizations()` | A parent with realizations is a set whose elements may live in several concrete realization parents; Sage makes it a facade set. | `with_realizations.py` and `realizations.py` own the construction surfaces; realization names are not constructors. |
| `HomsetsCategory` | `SetHomCategory`, `SetEndCategory`, `SetAutCategory` | Morphisms between sets are functions; endomorphisms have equal domain/codomain; automorphisms are bijections. | Generic `AutCategory` wiring belongs at the repository top level, but set-specific hom categories declare function-level methods and delegate aut construction rather than reimplement condition-set machinery. Inverse images of subsets belong to set maps as `preimage(subset)`. `Sets().HomCategory()` and `Sets().EndCategory()` are public category navigation surfaces. |
| `Homsets().Endset()` | `SetEndCategory` | End categories have objects `End(X) = Hom(X, X)`; Sage makes generic endsets monoids. | `sets/homsets.py` exposes the set-specific end category and inherits generic end-category methods. The former `base_set()` alias is represented by the generic hom-object `domain()` on `End_Sets(X)`. |
| Sage generic hom/end surface plus project aut target | `SetAutCategory` backed by generic `AutCategory` | `Aut(X)` is the subset of `End(X)` consisting of bijections. | This project vocabulary is wired once at the top level and specialized in `sets/homsets.py`; upstream category-naming follow-up belongs in the tracker item that cites this mapping row. |
| `SetsWithGrading()` | `Sets().Graded()` | A graded set is a disjoint union of graded components indexed by a grading set, with a grading map sending each element to its grade. | `subcategories/graded.py` owns `grading_set`, `graded_component`, optional `subset`, `grading`, `generating_series`, and `_test_graded_components`. |
| `GSets(G)` | `Sets().GSets(G)` | A `G`-set is a set with an action of the fixed group `G`; Sage's source records `GSets(G).super_categories() == [Sets()]`. | `subcategories/group_actions.py` owns the parameterized category. `types.py` needs `GSet` and group-action vocabulary anchored to Sage group/action objects. |
| `Posets()` | top-level `posets/` subtree, cross-linked from `sets` | A poset is a set with a partial order. Sage's required parent method is `le`; it also exposes `lt`, `ge`, `gt`, covers, order ideals, filters, chains, and antichains. | Do not bury this under ordinary set subcategories. The promoted subtree owns order methods and its own finite/lattice refinements. |
| `LatticePosets()` / `FiniteLatticePosets()` | `posets/subcategories/lattice.py` and `posets/subcategories/finite_lattice.py` | These are order-theoretic lattices: posets in which every pair has a meet and join. | Keep separate from module/quadratic-form lattice vocabulary; finite lattice posets add irreducibles and lattice-morphism checks. |

## Constructor Mapping Decisions

| Sage constructor | Project subcategory | Notes |
| --- | --- | --- |
| `Set(X)` | not admitted as a project constructor | The generic Sage wrapper does not define a mathematical construction from an arbitrary object to a set. Cases are enumerated into non-variadic, named paths: `Set(ZZ)` is replaced by `ZZ in Sets()` because `ZZ` is already a set object; finite explicit iterables use `Sets().Constructors().from_iterable(elements)`; real-line subsets use the `RealSet` constructors; other valid cases must receive their own named constructors before admission. |
| finite iterable input formerly routed through `Set([..])`, `Set(tuple(..))`, ordered dictionaries, or other finite iterable wrappers | `Sets().Constructors().from_iterable(elements)` | This constructor creates a finite enumerated set by enumeration. It is the project replacement for finite iterable wrapping, and it keeps the public API non-variadic and mathematically explicit. |
| `FiniteEnumeratedSet(elements)` | `FiniteEnumeratedSetObjects` | Tuple-backed finite facade set. Include `__call__` and element construction in the spec. Sage enumeration conveniences map to countable-set indexing and finite Python conversion protocols. |
| `IntegerRange(...)` | `IntegerRangeSets` | Arithmetic progression of integers. Finite/infinite status depends on bounds; the one-object category should refine through countable facade sets and let Sage/category membership expose finiteness. |
| `NonNegativeIntegers()` | `NonNegativeIntegerSets` | Countably infinite facade subset of `ZZ`. |
| `PositiveIntegers()` | `PositiveIntegerSets` | Positive integer range; inherits most integer-range behavior and supplies Sage's `an_element`/`_sympy_`. |
| `Primes()` | `PrimesSets` | `Sets().Primes()` is the one-object category whose object is Sage's set of prime integers. `PrimeSubset` and `PrimesInArithmeticProgressions` are types of subobjects of that prime set, not separate top-level categories unless Sage exposes distinct parent objects with required methods. |
| `RR` / `RealField()` | `Sets().Constructors().RR()` refined into `Sets().Topological()` | Named ambient sets belong under `Sets().Constructors()` even when they carry topology, algebra, order, or metric structure. `Sets().Constructors()` is the main discoverability interface for named objects for now; later this may be replaced by an aggregate constructor surface exposed from all categories, or moved upward to `Cat`. |
| `RealSet(...)` finite interval-union input | `Sets().Constructors().RealSet(intervals=...)` refined through `RealSets` | A real set is a subset of the real line. The project constructor admits a named sequence of `InternalRealInterval` components rather than exposing Sage's variadic surface; the wrapper delegates internally to Sage's documented constructor route before refinement. Real intervals and real open sets are distinct mathematical notions: open intervals are basis elements for the Euclidean topology, while open subsets may be unions such as `(1, 2) ∪ (3, 4)`. |
| `RealSet.interval(lower, upper, lower_closed=..., upper_closed=...)` | `Sets().Constructors().RealSetInterval(lower, upper, lower_closed=..., upper_closed=...)` | This is the universal interval/ray constructor. The two endpoints and two closure booleans unambiguously determine the real subset, including `[p, q)`, `[p, q]`, rays, and the whole real line when infinite endpoints are used. |
| `RealSet` static interval constructors | named real-subset interval constructors | Sage methods such as `RealSet.open(a, b)` and `RealSet.closed(a, b)` construct interval-shaped real subsets, not arbitrary open or closed real subsets. Static Sage constructors map to `Sets().Constructors()` entries such as `OpenRealInterval`, `ClosedRealInterval`, and `RealLine`; each named constructor delegates to `RealSetInterval` with the corresponding endpoint-closure booleans. Open interval constructors return `RealOpenSet` because an open interval is an open real subset, but a general `RealOpenSet` need not be an interval. |
| Real intervals, rays, real line, and future complex-ball-like named subsets | `Sets().Constructors()` first, then refinement into topological subobjects | These are named set constructions. The constructor result must refine not only into `Sets()` but also into the relevant subset/subobject and topological-space categories, e.g. real intervals refine through `RealSets`, `Sets().Subobjects()`, `TopologicalSpaces()`, and `TopologicalSpaces().Subobjects()`. Where Sage's real-subset category data proves connectedness or compactness, the result also refines into `TopologicalSpaces().Connected()` or `TopologicalSpaces().Compact()`. |
| `RecursivelyEnumeratedSet(...)` | `RecursivelyEnumeratedSets` | Recursively enumerable countable sets and forests. The forest-specific methods are part of the same Sage constructor family. |
| `DisjointUnionEnumeratedSets(family)` | `DisjointUnionSets` | Countable coproduct/disjoint union of an indexed family. |
| `CartesianProduct(...)` / `cartesian_product(...)` | `CartesianProductSets` | Product of sets; element projections belong to element methods. |
| `ConditionSet(universe, predicates...)` | internal backing for `Sets().Subobjects().Of(universe, predicates)` | A condition set is Sage's implementation of a predicate-defined subset. The public project API names the mathematical object as a subobject/subset of its ambient set; Sage `arguments()` and raw predicate tuple plumbing remain inventory-only. |
| `ImageSubobject(f, X)` | `ImageSets` | Image subobject under a map; must include `ambient`, `lift`, and `retract`. |
| `TotallyOrderedFiniteSet(elements)` | `TotallyOrderedFiniteSets` | Finite set with order relation `le`; element comparison methods are mathematical when elements are non-facade. |
| `FiniteSetMaps(domain, codomain)` | `FiniteSetMapSets` plus the set homset/endset refinement | Finite set of functions. The finite-set subcategory owns finite enumeration and constructor surfaces; the homset layer owns `domain`/`codomain`, and the endset layer owns identity for endomap variants. Sage's `one()` remains inventory evidence for the endset identity surface, not a finite-set-only method. |
| `SetPartitions()` | `Sets().Constructors().AllSetPartitions()` | Countable set of all finite set partitions. This Sage parent has no fixed base set and therefore does not refine into `Partitioned`. |
| `SetPartitions(s)` | `Sets().Constructors().SetPartitions(base_set=s)` | Fixed-base set partitions. The result refines through `Sets().Partitioned()` because each element is a partition subobject of `P(s)`. |
| `SetPartitions(s, k)` | `Sets().Constructors().SetPartitionsWithBlockCount(base_set=s, block_count=k)` | Fixed-base partitions with exactly `k` blocks. The block count is a named constructor parameter, not Sage's positional `part` overload. |
| `SetPartitions(s, part)` | `Sets().Constructors().SetPartitionsWithBlockSizes(base_set=s, block_sizes=part)` | Fixed-base partitions whose block sizes are the integer partition `part`. This is the second finite Sage `part` case, separated from block count. |
| `SetPartition(blocks, check=True)` | `Sets().Constructors().SetPartition(blocks, check=check)` | Construct the original Sage `SetPartition` element. Elements cannot be refined with `refine_category`, so the constructor returns Sage's element class while `Partitioned.ElementMethods` records the required partition surface. |
| `SetPartitions().from_restricted_growth_word_blocks(w)` | `Sets().Constructors().SetPartitionFromRestrictedGrowthWordBlocks(word=w)` | Element constructor from a restricted-growth word using Sage's block convention. |
| `SetPartitions().from_restricted_growth_word_intertwining(w)` | `Sets().Constructors().SetPartitionFromRestrictedGrowthWordIntertwining(word=w)` | Element constructor from a restricted-growth word using Sage's intertwining convention. |
| `SetPartitions().from_arcs(arcs, n)` | `Sets().Constructors().SetPartitionFromArcs(arcs=arcs, base_set_cardinality=n)` | Element constructor from arcs. |
| `from_rook_placement(..., "arcs"/"gamma"/"rho"/"psi", n)` | named rook-placement constructors on `Sets().Constructors()` | Sage's string-dispatched rook-placement constructor is split into non-variadic named constructors: `SetPartitionFromRookPlacementArcs`, `SetPartitionFromRookPlacementGamma`, `SetPartitionFromRookPlacementRho`, and `SetPartitionFromRookPlacementPsi`. |
| `Family(indices, function)` | `Families` | Indexed family object. Include `items`, `hidden_keys`, `has_key`, and `inverse_family`. |
| `EnumeratedSetFromIterator(f)` | `IteratorEnumeratedSets` | Callable-backed countable set. The project constructor admits a nullary iterator factory. Sage's `args`/`kwds` parameterization is arbitrary callable plumbing, not set-theoretic data, so it is not exposed as a public constructor shape. Include `clear_cache` because caching is part of the Sage-backed parent behavior. |

Existing Sage calls of the form `EnumeratedSetFromIterator(f, args=..., kwds=...)`
are recovered by closing over those arguments before constructing the project object:
the resulting nullary iterator factory is the set-theoretic input. The old
`args`/`kwds` plumbing remains migration guidance only and is not a category-spec
signature.

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
| `crossings`, `nestings`, `is_noncrossing`, `is_nonnesting`, `is_atomic` | future axiomatic subcategories of partitioned sets when admitted | These predicates describe stricter combinatorial subclasses. They are mapped, but not scaffolded until a pass admits the corresponding subcategories. |
| `standardization()`, `restriction(I)` | partition element transforms | These return new partition elements and remain partition methods. |
| `refinements()`, `coarsenings()`, `strict_coarsenings()` | finite sets of partition elements | These return finite subsets of the partition lattice and should refine through set constructors in a later implementation pass. |
| `plot(...)` and LaTeX/display helpers | no category method | Display output is not set-theoretic structure. |

## Sage `Set_object` Method Mapping Decisions

Sage's `Set_object` and `Set_object_enumerated` method surface is inventoried in
`SAGE_INVENTORY.md`. The generic wrapper category is not admitted, but the methods are
mapped to the mathematical surfaces they witness.

| Sage surface | Project mapping | Decision |
| --- | --- | --- |
| `object()` | no public project method | The wrapped Python object is Sage implementation state, not mathematical structure. Named constructors expose their mathematical data directly instead of exposing a generic underlying object. |
| `__contains__(x)` | `Sets.ParentMethods.__contains__` | Membership is part of every set. |
| `__iter__()` | `Sets().Countable().ParentMethods.__iter__` | Iteration witnesses countability, not arbitrary sethood. |
| `_an_element_()` / `an_element()` | `Sets.ParentMethods.an_element` | Producing an element is a root set method. |
| `cardinality()` | `Sets.ParentMethods.cardinality` | Cardinality is defined for every set. |
| `is_empty()` / `is_finite()` | `Sets.ParentMethods.is_empty` and `Sets.ParentMethods.is_finite` | These predicates are defined for every set. |
| `subsets(size=None)` / `subsets_lattice()` | `Sets.ParentMethods.subsets` and `Sets.ParentMethods.subsets_lattice` | The power set and subset lattice are set-theoretic constructions, not wrapper-specific methods. |
| `algebra(R, category=None)` on plain sets | `free_module(R)` routed to `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=self)` | Sage's plain-set path is the free module on the set, not an algebra constructor. Sage's `category=` keyword remains inventory for structured source-category dispatch; it is not a project API shape. |
| `free_module(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=self)` | This is the project spelling for the existing Sage plain-set `S.algebra(R)` functionality. |
| `free_algebra(R)` | `Algebras(R).Constructors().free_algebra_from_set(self)` | This is the mathematical free associative unital `R`-algebra generated by the set. |
| `_sympy_()` | `Sets.ParentMethods._sympy_` | SymPy conversion is a general set export surface where available. |
| `_repr_()`, `_latex_()`, `__hash__()` | no independent project method | Display and hashing belong to concrete parent implementation behavior. They do not define set-theoretic structure and are not category obligations. |
| `union(other)` | `Sets.ParentMethods.union` | Union is defined for any two objects in the category of sets. |
| `intersection`, `difference`, `symmetric_difference`, `complement` | `Sets().Subobjects()` / `Subsets` | These require a common ambient set, so they are subset/subobject operations. |
| `Set_object_union`, `Set_object_intersection`, `Set_object_difference`, `Set_object_symmetric_difference` | operation result parents, not public project category names | These Sage classes witness concrete outputs of set operations. The project maps their method surface to union on `Sets()` and subobject operations on `Sets().Subobjects()` rather than exposing the wrapper class names. |
| `__richcmp__`, `issubset`, `issuperset` | root set comparison surface | The project exposes rich comparison with set-theoretic semantics: equality is equality of elements, `<=` is subset, `<` is proper subset, `>=` is superset, and `>` is proper superset. This replaces Sage wrapper comparison semantics. |
| `list()`, `tuple()` on finite wrappers | `list(X)`, `tuple(X)` for finite countable sets | Finite enumerated sets may expose finite enumeration through Python conversion protocols. Do not make Sage's `.list()` and `.tuple()` names primary project methods. |
| `set()`, `frozenset()` on finite wrappers | no project method | Python hash-set export is not a project set object and is not admitted as category vocabulary. |
| `rank`, `unrank`, `first`, `last`, `next` | `rank(e)` and indexed access | `rank(e)` is the index-of map and remains meaningful for infinite countable sets. Sage `unrank(n)` maps to `X[n]`; `first`, `last`, and `next` are derived enumeration conveniences and are not project method names. |

## Rich Comparison Mapping Decisions

Sage exposes rich comparison through several surfaces:
`Set_object.__richcmp__`, `Set_object_enumerated.__richcmp__`, finite wrapper
`issubset`/`issuperset`, and ordered-set element `_richcmp_`.

The project mapping is:

- Set-object rich comparison belongs on `Sets()` and is redefined set-theoretically.
  It must not inherit Sage's arbitrary-wrapper comparison behavior.
- Subset order is comparison of set objects by inclusion: `A <= B` means `A` is a
  subset of `B`, and `A < B` means proper subset.
- Poset element comparison remains separate: `Posets.ParentMethods.le/lt/ge/gt` and
  ordered-set element comparisons compare elements of an ordered set, not set objects
  by inclusion.
- Finite enumerated wrapper equality and Python `set`/`frozenset` comparison behavior
  are not copied as implementation quirks; finite set comparison uses the same
  set-theoretic comparison surface as every set.

## Signature Typing Decisions

Rank, unrank, projection index, component index, and recursion-depth parameters are
mathematically integer-valued. The spec uses `Integer`, and uses
`Integer | InfinityElement` only where Sage's written documentation explicitly allows
infinite bounds, such as `IntegerRange` begin/end values and recursive-enumeration
depth bounds. It does not introduce an `IntegerRangeBound` alias because that only
renames a simple union without adding mathematical vocabulary.

Cartesian product element construction is typed as a sequence of set elements. This
matches the product object mathematically: an element of `X_1 x ... x X_n` is an
ordered tuple-like family with one component in each factor, not an unstructured
variadic call surface.

Real-set method signatures use `RealSubset` and `RealInterval`. The former is the
mathematical object for finite Boolean operations on subsets of the real line; the
latter is the mathematical object returned by interval accessors. Endpoint tuples are
Sage constructor data, not a subcategory or type vocabulary item, so they appear only
through explicit constructor methods such as `RealSetInterval`, `OpenRealInterval`, and
`ClosedRealInterval`.

Sage forwarding and test-suite hooks are inventory items, not mathematical method
surface. `Sets.ParentMethods._element_constructor_from_element_class(*args,
**keywords)` forwards to an arbitrary element-class constructor, so it has no finite
mathematical signature. `SetsWithGrading.ParentMethods._test_graded_components(**options)`
is Sage `TestSuite` plumbing. Both are omitted from the public spec surface rather than
preserved as variadic API.

## Sage Primes Source Note

- Searched: Context7 `/sagemath/documentation`, DeepWiki `sagemath/sage`, hosted Sage docs for `Primes`, and installed source `sage/sets/primes.py`.
- Found: Hosted docs describe prime subsets selected by congruence data (`modulus`, `classes`, and `exceptions`); the installed source at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/primes.py` exposes only `Primes(proof=True)` for the full set of prime integers.
- Conclusion: I believe the online docs and installed source are version-skewed. Mathematically, congruence-class prime subsets should be represented as subobjects of `Primes()`, with vocabulary such as `PrimesInArithmeticProgressions` only where method signatures require that refinement.
- Confidence: Medium.
- Gaps: I have not searched Sage git history or package metadata for the exact documentation/source version boundary.

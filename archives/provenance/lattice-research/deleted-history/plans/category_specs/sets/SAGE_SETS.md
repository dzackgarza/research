# SageMath Set Implementations: Comprehensive Reference

## 1. Category Hierarchy for Sets

The category framework for sets is rooted in `Sets` (`sets_cat.py`) and forms the
following hierarchy:

```mermaid
graph TD
  "Objects" --> "SetsWithPartialMaps"
  "SetsWithPartialMaps" --> "Sets"
  "Sets" --> "Sets.Finite (FiniteSets)"
  "Sets" --> "Sets.Infinite"
  "Sets" --> "Sets.Enumerated (EnumeratedSets)"
  "Sets.Enumerated (EnumeratedSets)" --> "FiniteEnumeratedSets"
  "Sets.Enumerated (EnumeratedSets)" --> "InfiniteEnumeratedSets"
  "Sets" --> "Sets.Facade (FacadeSets)"
  "Sets" --> "Sets.CartesianProducts"
  "Sets" --> "Sets.Subquotients"
  "Sets" --> "Sets.Quotients"
  "Sets" --> "Sets.Subobjects"
  "Sets" --> "Sets.IsomorphicObjects"
  "Sets" --> "Sets.Topological"
  "Sets" --> "Sets.Metric"
  "Sets" --> "Sets.Algebras(base_ring)"
```

[1](#0-0)

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

[2](#0-1)

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

[3](#0-2)

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

[4](#0-3)

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

[5](#0-4) [6](#0-5)

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

[7](#0-6) [8](#0-7)

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

[9](#0-8)

* * *

### `FacadeSets` — `src/sage/categories/facade_sets.py`

Axiom: `Facade`. A facade set represents its elements as elements of another parent.

`ParentMethods`:
- `_element_constructor_(element)` — coerces element from any facade parent

[10](#0-9)

* * *

## 3. Concrete Set Implementations in `sage.sets`

All public exports are listed in `src/sage/sets/all.py`:

[11](#0-10)

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

[12](#0-11) [13](#0-12)

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

[14](#0-13)

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

[15](#0-14)

#### Binary set operation classes

All extend `Set_object` and are created lazily by `Set_base` methods:

| Class | Operation |
| --- | --- |
| `Set_object_union` | `A ∪ B` |
| `Set_object_intersection` | `A ∩ B` |
| `Set_object_difference` | `A \ B` |
| `Set_object_symmetric_difference` | `A △ B` |

[16](#0-15)

* * *

### `FiniteEnumeratedSet` — `src/sage/sets/finite_enumerated_set.py`

Category: `FiniteEnumeratedSets().Facade()`. Backed by a tuple stored in memory.
Unique representation.
Key methods: `list()`, `cardinality()`, `random_element()`, `first()`, `__iter__()`,
`__contains__()`, `rank()`, `unrank()`.

[17](#0-16)

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

[18](#0-17)

* * *

### `NonNegativeIntegers` — `src/sage/sets/non_negative_integers.py`

Category: `InfiniteEnumeratedSets().Facade()`. Elements are plain `Integer` objects with
parent `ZZ`. Key methods: `__iter__()`, `first()`, `next(x)`, `cardinality()`,
`__contains__()`, `an_element()`.

[19](#0-18)

* * *

### `PositiveIntegers` — `src/sage/sets/positive_integers.py`

Subclass of `IntegerRangeInfinite`. Category: `InfiniteEnumeratedSets().Facade()`.
Additional methods: `_repr_()`, `an_element()` (returns 42), `_sympy_()` (returns SymPy
`Naturals`).

[20](#0-19)

* * *

### `Primes` — `src/sage/sets/primes.py`

Category: `InfiniteEnumeratedSets().Facade()` (or `FiniteEnumeratedSets().Facade()` for
finite subsets via congruence conditions).
Supports congruence conditions via `modulus` and `classes` arguments.
Key methods: `__contains__(x)`, `__iter__()`, `cardinality()`, `first()`, `next(x)`,
`an_element()`, `unrank(n)`.

[21](#0-20)

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

[22](#0-21)

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

[23](#0-22)

* * *

### `DisjointUnionEnumeratedSets` — `src/sage/sets/disjoint_union_enumerated_sets.py`

Category: `FiniteEnumeratedSets()` or `InfiniteEnumeratedSets()` depending on the
family. Options: `keepkey=True` (returns `(key, element)` pairs), `facade=False` (wraps
elements). Key methods: `__iter__()`, `cardinality()`, `an_element()`, `first()`,
`__contains__()`.

[24](#0-23)

* * *

### `CartesianProduct` — `src/sage/sets/cartesian_product.py`

Raw data structure for Cartesian products.
Use `cartesian_product(...)` at the user level.
Key methods: `cartesian_factors()`, `cardinality()`, `random_element()`, `an_element()`,
`__iter__()`, `__contains__()`, `_cartesian_product_of_elements(...)`.

[25](#0-24)

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

[26](#0-25)

* * *

### `ImageSubobject` — `src/sage/sets/image_set.py`

The image `{f(x) | x ∈ X}` of a set under a map.
Options: `is_injective` (`None`, `False`, `True`, `'check'`), `inverse`. Key methods:
`__iter__()`, `__contains__(x)`, `cardinality()`, `an_element()`.

[27](#0-26)

* * *

### `TotallyOrderedFiniteSet` — `src/sage/sets/totally_ordered_finite_set.py`

A finite set with a user-specified total order.
Category: `FiniteEnumeratedSets()` and `Posets()`. Elements are
`TotallyOrderedFiniteSetElement` objects (when `facade=False`) supporting `<`, `<=`,
`>`, `>=`. Key methods: `__iter__()`, `cardinality()`, `rank(x)`, `unrank(n)`,
`__contains__()`.

[28](#0-27)

* * *

### `FiniteSetMaps` — `src/sage/sets/finite_set_maps.py`

The set of all maps between two finite sets.
Category: `FiniteMonoids()` (for endo-maps) or `FiniteEnumeratedSets()`. Key methods:
`cardinality()`, `__iter__()`, `an_element()`, `identity()` (for endo-maps), `__mul__`
(composition).

[29](#0-28)

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

[30](#0-29)

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

[31](#0-30)

* * *

### `EnumeratedSetFromIterator` — `src/sage/sets/set_from_iterator.py`

Builds an enumerated set from a callable that returns an iterator.
Supports optional caching.
Also provides decorators `@set_from_function` and `@set_from_method`. Key methods:
`__iter__()`, `cardinality()`, `an_element()`, `unrank(n)`.

[32](#0-31)

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

[11](#0-10)

* * *

## 5. Citation Index

This section maps reference markers to their source files and line numbers.

| Marker | File | Lines | Description |
| --- | --- | --- | --- |
| [1](#0-0) | `src/sage/categories/sets_cat.py` | 99-115 | `Sets` category class definition and super_categories |
| [2](#0-1) | `src/sage/categories/sets_cat.py` | 302-800 | `SubcategoryMethods` class with CartesianProducts, Subquotients, Quotients, Subobjects, IsomorphicObjects, Topological, Metric, Algebras, Finite, Infinite, Enumerated, Facade |
| [3](#0-2) | `src/sage/categories/sets_cat.py` | 957-1400 | `ParentMethods` class with *element_constructor*, is_parent_of, **contains**, an_element, _test_an_element, _test_elements, *test_elements_eq**, some_elements, _test_some_elements |
| [4](#0-3) | `src/sage/categories/finite_sets.py` | 16-107 | `FiniteSets` category with SubcategoryMethods.Infinite, ParentMethods.is_finite, Subquotients extra_super_categories, Algebras extra_super_categories |
| [5](#0-4) | `src/sage/categories/enumerated_sets.py` | 21-94 | `EnumeratedSets` category docstring and class definition |
| [6](#0-5) | `src/sage/categories/enumerated_sets.py` | 156-600 | `ParentMethods` with **iter**, is_empty, iterator_range, unrank_range, **getitem**, **len**, tuple, list, cardinality, _tuple_from_iterator, _tuple_from_list, _list_default |
| [7](#0-6) | `src/sage/categories/finite_enumerated_sets.py` | 22-54 | `FiniteEnumeratedSets` category class definition |
| [8](#0-7) | `src/sage/categories/finite_enumerated_sets.py` | 81-150 | `ParentMethods` with **len**, _cardinality_from_iterator, _cardinality_from_list, _list_from_iterator, etc. |
| [9](#0-8) | `src/sage/categories/infinite_enumerated_sets.py` | 19-114 | `InfiniteEnumeratedSets` category with ParentMethods.random_element, tuple, list |
| [10](#0-9) | `src/sage/categories/facade_sets.py` | 16-80 | `FacadeSets` category with ParentMethods.*element_constructor* |
| [11](#0-10) | `src/sage/sets/all.py` | 1-16 | Public exports: RealSet, Set, IntegerRange, NonNegativeIntegers, PositiveIntegers, FiniteEnumeratedSet, RecursivelyEnumeratedSet, TotallyOrderedFiniteSet, DisjointUnionEnumeratedSets, Primes, Family, DisjointSet, ConditionSet, FiniteSetMaps |
| [12](#0-11) | `src/sage/sets/set.py` | 209-316 | `Set_base` class with union, intersection, difference, symmetric_difference |
| [13](#0-12) | `src/sage/sets/set.py` | 348-437 | `Set_boolean_operators` and `Set_add_sub_operators` mix-ins |
| [14](#0-13) | `src/sage/sets/set.py` | 439-843 | `Set_object` class with **init**, **hash**, *latex*, *repr*, **iter**, *an_element*, **contains**, __richcmp, cardinality, is_empty, is_finite, object, subsets, subsets_lattice, *sympy* |
| [15](#0-14) | `src/sage/sets/set.py` | 845-1100 | `Set_object_enumerated` class with random_element, is_finite, cardinality, **len**, **iter**, *latex*, *repr*, list, set, frozenset, **hash**, __richcmp |
| [16](#0-15) | `src/sage/sets/set.py` | (referenced in Set_base methods) | Binary operation classes: Set_object_union, Set_object_intersection, Set_object_difference, Set_object_symmetric_difference |
| [17](#0-16) | `src/sage/sets/finite_enumerated_set.py` | 27-80 | `FiniteEnumeratedSet` class description |
| [18](#0-17) | `src/sage/sets/integer_range.py` | 28-80 | `IntegerRange` class with IntegerRangeFinite, IntegerRangeInfinite, IntegerRangeFromMiddle subclasses |
| [19](#0-18) | `src/sage/sets/non_negative_integers.py` | 17-80 | `NonNegativeIntegers` class |
| [20](#0-19) | `src/sage/sets/positive_integers.py` | 15-92 | `PositiveIntegers` class extending IntegerRangeInfinite |
| [21](#0-20) | `src/sage/sets/primes.py` | 67-80 | `Primes` class with modulus/classes arguments |
| [22](#0-21) | `src/sage/sets/real_set.py` | 113-300 | `InternalRealInterval` class with bounds and closedness methods |
| [23](#0-22) | `src/sage/sets/recursively_enumerated_set.pyx` | 1-100 | `RecursivelyEnumeratedSet` with structure types and enumeration iterators |
| [24](#0-23) | `src/sage/sets/disjoint_union_enumerated_sets.py` | 29-80 | `DisjointUnionEnumeratedSets` with keepkey and facade options |
| [25](#0-24) | `src/sage/sets/cartesian_product.py` | 32-80 | `CartesianProduct` raw data structure |
| [26](#0-25) | `src/sage/sets/condition_set.py` | 26-80 | `ConditionSet` with universe and predicates |
| [27](#0-26) | `src/sage/sets/image_set.py` | 34-80 | `ImageSubobject` with is_injective and inverse options |
| [28](#0-27) | `src/sage/sets/totally_ordered_finite_set.py` | 31-80 | `TotallyOrderedFiniteSetElement` with comparison operators |
| [29](#0-28) | `src/sage/sets/finite_set_maps.py` | 38-80 | `FiniteSetMaps` for maps between finite sets |
| [30](#0-29) | `src/sage/sets/disjoint_set.pyx` | 1-100 | `DisjointSet` union-find data structure (not a Parent) |
| [31](#0-30) | `src/sage/sets/family.pyx` | 58-100 | `Family` factory with TrivialFamily, FiniteFamily, LazyFamily, EnumeratedFamily |
| [32](#0-31) | `src/sage/sets/set_from_iterator.py` | 73-80 | `EnumeratedSetFromIterator` with caching and decorators |

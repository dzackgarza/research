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

from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.sets import Sets
from category_specs.sets.subcategories.constructions.isomorphic_objects import _IsomorphicObjects
from category_specs.sets.subcategories.constructions.quotients import _Quotients
from category_specs.sets.subcategories.constructions.realizations import _Realizations
from category_specs.sets.subcategories.constructions.with_realizations import SetsWithRealizations
from category_specs.sets.subcategories.countable import _CountableSets, _FiniteCountableSets, _InfiniteCountableSets
from category_specs.sets.subcategories.disjoint_union import _DisjointUnionEnumeratedSets
from category_specs.sets.subcategories.facade import _FacadeSets
from category_specs.sets.subcategories.family import _FamilySets
from category_specs.sets.subcategories.finite import _FiniteSets
from category_specs.sets.subcategories.finite_set_maps import _FiniteSetMapsSets
from category_specs.sets.subcategories.graded import (
    GradedSetsCategory,
    GradedSetsElement,
    GradedSetsMorphism,
    GradedSetsObject,
)
from category_specs.sets.subcategories.infinite import _InfiniteSets
from category_specs.sets.subcategories.partitioned import (
    PartitionsCategory,
    PartitionedSetsCategory,
)
from category_specs.sets.homsets import SetHomCategory
from category_specs.sets.subcategories.totally_ordered import _TotallyOrdered
from category_specs.sets.subcategories.recursively_enumerated import _RecursivelyEnumeratedSets
from category_specs.sets.subcategories.uncountable import _UncountableSets
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_category_statements
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as SageFiniteEnumeratedSets
from sage.sets.set import Set as SageSet
from sage.sets.real_set import RealSet as SageRealSet


C = Sets().Constructors()


def fixed_ordered_partition():
    return C.SetPartitions(base_set=3)([[1, 3], [2]])


def real_open_interval_01():
    return C.open(lower=0, upper=1)


def real_closed_interval_01():
    return C.closed(lower=0, upper=1)


def single_block_ordered_partition():
    return C.SetPartitions(base_set=3)([[1, 2, 3]])


def finite_image_subobject_with_ambient():
    domain = C.IntegerRange(3)
    codomain = C.IntegerRange(5)
    f = Hom(domain, codomain, category=Sets())(lambda n: n + 1)
    return C.ImageSubobject(f, domain)


def symmetric_group_action_category():
    return Sets().GSets(SymmetricGroup(3))


def abstract_method_has_name(method, name):
    return method.__name__ == name


CATEGORY_STATEMENTS = (
    ("ZZ is already an object of Sets()", lambda _: ZZ in Sets()),
    ("ZZ is not finite as a set", lambda _: not ZZ.is_finite()),
    (
        "Set(elements=[1, 2, 3]) is a finite countable set",
        lambda _: C.Set(elements=[1, 2, 3]) in Sets().Countable().Finite(),
    ),
    (
        "Set(elements=[1, 2, 3]) has cardinality 3",
        lambda _: C.Set(elements=[1, 2, 3]).cardinality() == 3,
    ),
    (
        "Set(elements=[1, 2, 3]) ranks 1 as 2",
        lambda _: C.Set(elements=[1, 2, 3])[1] == 2,
    ),
    (
        "Set(elements=[1, 2, 3]) is a subset of ZZ",
        lambda _: C.Set(elements=[1, 2, 3]).is_subset(ZZ),
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) is a finite countable set",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]) in Sets().Countable().Finite(),
    ),
    (
        "finite/countable/infinite set category classes route through Sets",
        lambda _: Sets.Finite is _FiniteSets
        and Sets.Infinite is _InfiniteSets
        and Sets.Countable is _CountableSets
        and _FiniteCountableSets._base_category_class_and_axiom == (_CountableSets, "Finite")
        and _InfiniteCountableSets._base_category_class_and_axiom == (_CountableSets, "Infinite"),
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) has cardinality 3",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]).cardinality() == 3,
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) reports countability",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]).is_countable(),
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) ranks 1 as 2",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3])[1] == 2,
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) is a subset of ZZ",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]).is_subset(ZZ),
    ),
    (
        "Set(elements=[7]) is the one-element finite set {7}",
        lambda _: C.Set(elements=[7]).cardinality() == 1 and 7 in C.Set(elements=[7]) and 8 not in C.Set(elements=[7]),
    ),
    ("IntegerRange(5) is a finite countable set", lambda _: C.IntegerRange(5) in Sets().Countable().Finite()),
    ("IntegerRange(5) has cardinality 5", lambda _: C.IntegerRange(5).cardinality() == 5),
    ("IntegerRange(5) ranks 2 as 2", lambda _: C.IntegerRange(5)[2] == 2),
    ("IntegerRange(5) is a subset of ZZ", lambda _: C.IntegerRange(5).is_subset(ZZ)),
    (
        "NonNegativeIntegers() is a countably infinite set",
        lambda _: C.NonNegativeIntegers() in Sets().Countable().Infinite(),
    ),
    ("NonNegativeIntegers() reports countability", lambda _: C.NonNegativeIntegers().is_countable()),
    ("0 is a nonnegative integer", lambda _: 0 in C.NonNegativeIntegers()),
    ("-1 is not a nonnegative integer", lambda _: -1 not in C.NonNegativeIntegers()),
    ("NonNegativeIntegers() is not finite", lambda _: not C.NonNegativeIntegers().is_finite()),
    (
        "PositiveIntegers() is a countably infinite set",
        lambda _: C.PositiveIntegers() in Sets().Countable().Infinite(),
    ),
    ("1 is a positive integer", lambda _: 1 in C.PositiveIntegers()),
    ("0 is not a positive integer", lambda _: 0 not in C.PositiveIntegers()),
    ("PositiveIntegers() is not finite", lambda _: not C.PositiveIntegers().is_finite()),
    ("Primes() is a countably infinite set", lambda _: C.Primes() in Sets().Countable().Infinite()),
    ("2 is prime", lambda _: 2 in C.Primes()),
    ("4 is not prime", lambda _: 4 not in C.Primes()),
    ("Primes() indexes its first element as 2", lambda _: C.Primes()[0] == 2),
    (
        "RealSet(open interval) is a topological set",
        lambda _: C.RealSet(intervals=[SageRealSet.open(0, 1).get_interval(0)]) in Sets().Topological(),
    ),
    (
        "RealSet(open interval) is a subobject",
        lambda _: C.RealSet(intervals=[SageRealSet.open(0, 1).get_interval(0)]) in Sets().Subobjects(),
    ),
    (
        "RealSet(open interval) contains 1/2",
        lambda _: C.RealSet(intervals=[SageRealSet.open(0, 1).get_interval(0)]).contains(1 / 2),
    ),
    (
        "RealSet(open interval) does not contain 2",
        lambda _: not C.RealSet(intervals=[SageRealSet.open(0, 1).get_interval(0)]).contains(2),
    ),
    (
        "RealSet(open interval) is open through its ambient real line",
        lambda _: (lambda U: U.ambient_real_line().is_open_subset(U))(real_open_interval_01()),
    ),
    (
        "RealSet(open interval) is not closed through its ambient real line",
        lambda _: (lambda U: not U.ambient_real_line().is_closed_subset(U))(real_open_interval_01()),
    ),
    (
        "RealSet(open interval) closes through its ambient real line",
        lambda _: (lambda U: U.ambient_real_line().closure_subset(U) == real_closed_interval_01())(real_open_interval_01()),
    ),
    (
        "RealSet(closed interval) has interior through its ambient real line",
        lambda _: (lambda U: U.ambient_real_line().interior_subset(U) == real_open_interval_01())(real_closed_interval_01()),
    ),
    (
        "RealSet(open interval) has boundary through its ambient real line",
        lambda _: (lambda U: U.ambient_real_line().boundary_subset(U) == SageRealSet.point(0).union(SageRealSet.point(1)))(
            real_open_interval_01()
        ),
    ),
    (
        "RealSet(open interval) has one component",
        lambda _: C.RealSet(intervals=[SageRealSet.open(0, 1).get_interval(0)]).n_components() == 1,
    ),
    ("real_line() is the universe real subset", lambda _: C.real_line().is_universe()),
    (
        "closed(0, 1) is disjoint from open(2, 3)",
        lambda _: C.closed(lower=0, upper=1).is_disjoint(C.open(lower=2, upper=3)),
    ),
    (
        "real intervals detect pairwise-disjoint families",
        lambda _: C.closed(lower=0, upper=1).are_pairwise_disjoint(
            C.open(lower=2, upper=3), C.open(lower=4, upper=5)
        ),
    ),
    (
        "real intervals compute convex hulls of finite real-subset families",
        lambda _: C.closed(lower=0, upper=1).__class__.convex_hull(
            C.closed(lower=0, upper=1), C.open(lower=2, upper=3)
        )
        == SageRealSet.closed_open(0, 3),
    ),
    (
        "interval(0, 1, open) is a connected topological subobject",
        lambda _: C.interval(0, 1, lower_closed=False, upper_closed=False) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "open(0, 1) is an open real subobject",
        lambda _: C.open(lower=0, upper=1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "closed(0, 1) is a compact connected real subobject",
        lambda _: C.closed(lower=0, upper=1) in TopologicalSpaces().Compact().Connected().Subobjects(),
    ),
    (
        "point(0) is a compact connected real subobject",
        lambda _: C.point(point=0) in TopologicalSpaces().Compact().Connected().Subobjects(),
    ),
    (
        "open_closed(0, 1) is a connected real subobject",
        lambda _: C.open_closed(lower=0, upper=1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "closed_open(0, 1) is a connected real subobject",
        lambda _: C.closed_open(lower=0, upper=1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "unbounded_below_closed(1) is a connected real subobject",
        lambda _: C.unbounded_below_closed(bound=1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "unbounded_below_open(1) is a connected real subobject",
        lambda _: C.unbounded_below_open(bound=1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "unbounded_above_closed(0) is a connected real subobject",
        lambda _: C.unbounded_above_closed(bound=0) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "unbounded_above_open(0) is a connected real subobject",
        lambda _: C.unbounded_above_open(bound=0) in TopologicalSpaces().Connected().Subobjects(),
    ),
    ("real_line() is a connected real subobject", lambda _: C.real_line() in TopologicalSpaces().Connected().Subobjects()),
    (
        "RecursivelyEnumeratedSet([0], successors) is countable",
        lambda _: C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth") in Sets().Countable(),
    ),
    (
        "0 lies in RecursivelyEnumeratedSet([0], successors)",
        lambda _: 0 in C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth"),
    ),
    (
        "3 lies in RecursivelyEnumeratedSet([0], successors)",
        lambda _: 3 in C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth"),
    ),
    (
        "-1 does not lie in bounded RecursivelyEnumeratedSet([0], successors)",
        lambda _: -1 not in C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth", max_depth=3),
    ),
    (
        "RecursivelyEnumeratedSet([0], successors) ranks 3 as 3",
        lambda _: C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth")[3] == 3,
    ),
    (
        "RecursivelyEnumeratedSet([0], successors) exposes children through the successor function",
        lambda _: C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth", max_depth=3).children(1)
        == [2],
    ),
    (
        "RecursivelyEnumeratedSet([0], successors) exports a bounded successor digraph",
        lambda _: C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth", max_depth=3)
        .to_digraph(max_depth=2)
        .has_edge(0, 1)
        and C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth", max_depth=3)
        .to_digraph(max_depth=2)
        .has_edge(1, 2),
    ),
    (
        "recursively enumerated sets own naive traversal as a Sage traversal surface",
        lambda _: abstract_method_has_name(_RecursivelyEnumeratedSets.ParentMethods.naive_search_iterator, "naive_search_iterator"),
    ),
    (
        "DisjointUnionEnumeratedSets has finite countable category",
        lambda _: C.DisjointUnionEnumeratedSets(
            C.Family([0, 1], lambda i: C.FiniteEnumeratedSet([i, i + 1]))
        )
        in Sets().Countable().Finite(),
    ),
    (
        "DisjointUnionEnumeratedSets has sum cardinality",
        lambda _: C.DisjointUnionEnumeratedSets(
            C.Family([0, 1], lambda i: C.FiniteEnumeratedSet([i, i + 1]))
        ).cardinality()
        == 4,
    ),
    (
        "DisjointUnionEnumeratedSets recognizes its canonical element",
        lambda _: C.DisjointUnionEnumeratedSets(
            C.Family([0, 1], lambda i: C.FiniteEnumeratedSet([i, i + 1]))
        )._is_a(
            C.DisjointUnionEnumeratedSets(C.Family([0, 1], lambda i: C.FiniteEnumeratedSet([i, i + 1]))).an_element()
        ),
    ),
    (
        "disjoint unions own Sage element-constructor hooks",
        lambda _: abstract_method_has_name(
            _DisjointUnionEnumeratedSets.ParentMethods._element_constructor_default,
            "_element_constructor_default",
        )
        and abstract_method_has_name(
            _DisjointUnionEnumeratedSets.ParentMethods._element_constructor_facade,
            "_element_constructor_facade",
        ),
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) is finite countable",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)]) in Sets().Countable().Finite(),
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) has product cardinality",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)]).cardinality() == 6,
    ),
    (
        "IntegerRange(2).cartesian_product(IntegerRange(3)) has product cardinality",
        lambda _: C.IntegerRange(2).cartesian_product(C.IntegerRange(3)).cardinality() == 6,
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) exposes its factor keys",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)])._sets_keys() == C.IntegerRange(2),
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) has first projection",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)]).cartesian_projection(0)(
            C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)])((1, 2))
        )
        == 1,
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) coerces from itself",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)])._coerce_map_from_(
            C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)])
        )
        is True,
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) elements expose coordinate projections",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)])((1, 2)).cartesian_projection(0) == 1,
    ),
    (
        "sets own free_algebra as the set-indexed free-algebra constructor surface",
        lambda _: abstract_method_has_name(Sets.ParentMethods.free_algebra, "free_algebra"),
    ),
    (
        "Sets().WithRealizations() routes to the set realization construction category",
        lambda _: Sets.WithRealizations is SetsWithRealizations
        and Sets().WithRealizations().is_subcategory(Sets())
        and Sets().WithRealizations().__class__.__base__ is SetsWithRealizations,
    ),
    (
        "Sets().Realizations() routes to the set realization-object construction category",
        lambda _: Sets.Realizations is _Realizations
        and Sets().Realizations().is_subcategory(Sets())
        and Sets().Realizations().__class__.__base__ is _Realizations,
    ),
    (
        "sets with realizations own realization-parent surfaces",
        lambda _: abstract_method_has_name(SetsWithRealizations.ParentMethods.a_realization, "a_realization")
        and abstract_method_has_name(SetsWithRealizations.ParentMethods.realizations, "realizations")
        and abstract_method_has_name(SetsWithRealizations.ParentMethods.inject_shorthands, "inject_shorthands"),
    ),
    (
        "set realization objects own parent and change-of-realization surfaces",
        lambda _: abstract_method_has_name(_Realizations.ParentMethods.parent_with_realization, "parent_with_realization")
        and abstract_method_has_name(_Realizations.ParentMethods.realization_of, "realization_of")
        and abstract_method_has_name(_Realizations.ParentMethods.to_realization, "to_realization")
        and abstract_method_has_name(_Realizations.ElementMethods.to_realization, "to_realization"),
    ),
    (
        "set quotients own ambient-set and equivalence-class surfaces",
        lambda _: abstract_method_has_name(_Quotients.ParentMethods.ambient_set, "ambient_set")
        and abstract_method_has_name(_Quotients.ParentMethods.equivalence_class, "equivalence_class"),
    ),
    (
        "set isomorphic objects own the distinguished-isomorphism surface",
        lambda _: Sets().IsomorphicObjects().__class__.__base__ is _IsomorphicObjects
        and abstract_method_has_name(_IsomorphicObjects.ParentMethods.isomorphism, "isomorphism"),
    ),
    ("even subobject of ZZ is a subobject", lambda _: Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,)) in Sets().Subobjects()),
    ("2 lies in the even subobject of ZZ", lambda _: 2 in Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,))),
    ("3 does not lie in the even subobject of ZZ", lambda _: 3 not in Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,))),
    ("even subobject of ZZ has ambient ZZ", lambda _: Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,)).ambient() == ZZ),
    ("ImageSubobject(n + 1, IntegerRange(3)) is a subobject", lambda _: C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3)) in Sets().Subobjects()),
    ("1 lies in ImageSubobject(n + 1, IntegerRange(3))", lambda _: 1 in C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3))),
    ("0 does not lie in ImageSubobject(n + 1, IntegerRange(3))", lambda _: 0 not in C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3))),
    ("ImageSubobject(n + 1, IntegerRange(3)) has cardinality 3", lambda _: C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3)).cardinality() == 3),
    ("ImageSubobject with codomain records its ambient", lambda _: finite_image_subobject_with_ambient().ambient() == C.IntegerRange(5)),
    ("ImageSubobject with codomain lifts into ambient", lambda _: finite_image_subobject_with_ambient().lift(1) == C.IntegerRange(5)(1)),
    ("ImageSubobject with codomain retracts ambient elements", lambda _: finite_image_subobject_with_ambient().retract(1) == 1),
    (
        "TotallyOrderedFiniteSet(['a', 'b', 'c']) is finite countable",
        lambda _: C.TotallyOrderedFiniteSet(["a", "b", "c"]) in Sets().Countable().Finite(),
    ),
    (
        "facade, totally ordered, and uncountable set category classes route through Sets",
        lambda _: Sets.Facade is _FacadeSets
        and Sets.TotallyOrdered is _TotallyOrdered
        and Sets.Uncountable is _UncountableSets
        and abstract_method_has_name(_FacadeSets.ParentMethods.is_facade, "is_facade")
        and abstract_method_has_name(_UncountableSets.ParentMethods.is_countable, "is_countable")
        and abstract_method_has_name(_UncountableSets.ParentMethods.is_uncountable, "is_uncountable"),
    ),
    (
        "TotallyOrderedFiniteSet(['a', 'b', 'c']) reports total ordering",
        lambda _: C.TotallyOrderedFiniteSet(["a", "b", "c"]).is_totally_ordered(),
    ),
    (
        "TotallyOrderedFiniteSet(['a', 'b', 'c']) has cardinality 3",
        lambda _: C.TotallyOrderedFiniteSet(["a", "b", "c"]).cardinality() == 3,
    ),
    (
        "TotallyOrderedFiniteSet(['a', 'b', 'c']) has a <= b",
        lambda _: C.TotallyOrderedFiniteSet(["a", "b", "c"]).le("a", "b"),
    ),
    (
        "TotallyOrderedFiniteSet(['a', 'b', 'c']) does not have c <= a",
        lambda _: not C.TotallyOrderedFiniteSet(["a", "b", "c"]).le("c", "a"),
    ),
    (
        "FiniteSetMaps(IntegerRange(2), IntegerRange(2)) is finite",
        lambda _: C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2)) in Sets().Finite(),
    ),
    (
        "FiniteSetMaps(IntegerRange(2), IntegerRange(2)) has domain IntegerRange(2)",
        lambda _: C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2)).domain() == C.IntegerRange(2),
    ),
    (
        "FiniteSetMaps(IntegerRange(2), IntegerRange(2)) has codomain IntegerRange(2)",
        lambda _: C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2)).codomain() == C.IntegerRange(2),
    ),
    (
        "FiniteSetMaps(IntegerRange(2), IntegerRange(2)) has cardinality 4",
        lambda _: C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2)).cardinality() == 4,
    ),
    (
        "FiniteSetMaps(IntegerRange(2), IntegerRange(2))._from_list_ builds the transposition",
        lambda _: C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2))._from_list_([1, 0])(0) == 1
        and C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2))._from_list_([1, 0])(1) == 0
        and abstract_method_has_name(_FiniteSetMapsSets.ParentMethods._from_list_, "_from_list_"),
    ),
    ("Family(IntegerRange(3), i^2) is a set", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2) in Sets()),
    ("Family(IntegerRange(3), i^2) maps 2 to 4", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2)[2] == 4),
    ("Family(IntegerRange(3), i^2) has cardinality 3", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2).cardinality() == 3),
    ("Family(IntegerRange(3), i^2) has key 2", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2).has_key(2)),
    (
        "families own inverse_family as a bijective-indexing surface",
        lambda _: abstract_method_has_name(_FamilySets.ParentMethods.inverse_family, "inverse_family"),
    ),
    (
        "EnumeratedSetFromIterator([0, 1, 2]) is finite countable",
        lambda _: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2]), category=SageFiniteEnumeratedSets())
        in Sets().Countable().Finite(),
    ),
    (
        "EnumeratedSetFromIterator([0, 1, 2]) has cardinality 3",
        lambda _: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2]), category=SageFiniteEnumeratedSets()).cardinality()
        == 3,
    ),
    (
        "EnumeratedSetFromIterator([0, 1, 2]) ranks 2 as 2",
        lambda _: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2]), category=SageFiniteEnumeratedSets())[2] == 2,
    ),
    (
        "1 lies in EnumeratedSetFromIterator([0, 1, 2])",
        lambda _: 1 in C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2]), category=SageFiniteEnumeratedSets()),
    ),
    (
        "Sets().Graded() records graded-set ownership and standard type package aliases",
        lambda _: GradedSetsCategory._base_category_class_and_axiom == (Sets, "Graded")
        and GradedSetsObject is GradedSetsCategory.ParentMethods
        and GradedSetsElement is GradedSetsCategory.ElementMethods
        and GradedSetsMorphism is SetHomCategory.ElementMethods,
    ),
    (
        "graded-set category owns grade component and generating-series surfaces",
        lambda _: abstract_method_has_name(GradedSetsCategory.ParentMethods.grading_set, "grading_set")
        and abstract_method_has_name(GradedSetsCategory.ParentMethods.grading, "grading")
        and abstract_method_has_name(GradedSetsCategory.ParentMethods.generating_series, "generating_series"),
    ),
    ("SetPartitions() is countable", lambda _: C.SetPartitions() in Sets().Countable()),
    ("SetPartitions() is not fixed-base partitioned", lambda _: C.SetPartitions() not in Sets().Partitioned()),
    ("SetPartitions(base_set=[1, 2, 3]) is partitioned", lambda _: C.SetPartitions(base_set=[1, 2, 3]) in Sets().Partitioned()),
    (
        "SetPartitions(3) has finite totally ordered base",
        lambda _: C.SetPartitions(base_set=3) in Sets().Partitioned(),
    ),
    (
        "SetPartitions(FiniteEnumeratedSet([1, 2, 3])) is partitioned",
        lambda _: C.SetPartitions(base_set=C.FiniteEnumeratedSet([1, 2, 3])) in Sets().Partitioned(),
    ),
    (
        "SetPartitions(base_set=[1, 2, 3], block_count=2) is partitioned",
        lambda _: C.SetPartitions(base_set=[1, 2, 3], block_count=2) in Sets().Partitioned(),
    ),
    (
        "SetPartitions(base_set=3, block_count=2) has finite totally ordered base",
        lambda _: C.SetPartitions(base_set=3, block_count=2) in Sets().Partitioned(),
    ),
    (
        "SetPartitions(base_set=[1, 2, 3], block_sizes=[2, 1]) is partitioned",
        lambda _: C.SetPartitions(base_set=[1, 2, 3], block_sizes=[2, 1]) in Sets().Partitioned(),
    ),
    (
        "SetPartitions(base_set=3, block_sizes=[2, 1]) has finite totally ordered base",
        lambda _: C.SetPartitions(base_set=3, block_sizes=[2, 1]) in Sets().Partitioned(),
    ),
    ("SetPartition([[1, 3], [2]]) lies over {1,2,3}", lambda _: C.SetPartition([[1, 3], [2]]) in C.SetPartitions(base_set=[1, 2, 3])),
    (
        "fixed-base set partitions expose blocks as subsets of the powerset",
        lambda _: fixed_ordered_partition().as_subset_of_powerset() == SageSet([SageSet([1, 3]), SageSet([2])]),
    ),
    (
        "fixed-base set partitions compare by refinement order",
        lambda _: fixed_ordered_partition().refines(single_block_ordered_partition())
        and fixed_ordered_partition().strictly_refines(single_block_ordered_partition())
        and not single_block_ordered_partition().strictly_refines(fixed_ordered_partition()),
    ),
    (
        "finite totally ordered set partitions expose ordered arc invariants",
        lambda _: fixed_ordered_partition().standard_form() == [[1, 3], [2]]
        and fixed_ordered_partition().crossings() == []
        and fixed_ordered_partition().nestings() == []
        and fixed_ordered_partition().is_noncrossing()
        and fixed_ordered_partition().is_nonnesting(),
    ),
    (
        "partitioned-set category owns ordered finite partition statistic surfaces",
        lambda _: abstract_method_has_name(PartitionsCategory.ElementMethods.standard_form, "standard_form")
        and abstract_method_has_name(PartitionsCategory.ElementMethods.crossings, "crossings")
        and abstract_method_has_name(PartitionsCategory.ElementMethods.nestings, "nestings")
        and abstract_method_has_name(PartitionsCategory.ElementMethods.is_noncrossing, "is_noncrossing")
        and abstract_method_has_name(PartitionsCategory.ElementMethods.is_nonnesting, "is_nonnesting"),
    ),
    (
        "partition refinement_set() is a finite countable set",
        lambda _: fixed_ordered_partition().refinement_set() in Sets().Countable().Finite(),
    ),
    (
        "Sets().GSets(G) owns orbit and stabilizer surfaces through the public category route",
        lambda _: symmetric_group_action_category().acting_group() == SymmetricGroup(3)
        and abstract_method_has_name(symmetric_group_action_category().ParentMethods.orbit, "orbit")
        and abstract_method_has_name(symmetric_group_action_category().ParentMethods.orbits, "orbits")
        and abstract_method_has_name(symmetric_group_action_category().ParentMethods.orbit_representatives, "orbit_representatives")
        and abstract_method_has_name(symmetric_group_action_category().ParentMethods.stabilizer, "stabilizer")
        and abstract_method_has_name(symmetric_group_action_category().ParentMethods.fixed_points, "fixed_points")
        and abstract_method_has_name(symmetric_group_action_category().ElementMethods.act_by, "act_by"),
    ),
    (
        "partition refinement_set() contains the source partition",
        lambda _: fixed_ordered_partition() in fixed_ordered_partition().refinement_set(),
    ),
    (
        "partition coarsening_set() is a finite countable set",
        lambda _: fixed_ordered_partition().coarsening_set() in Sets().Countable().Finite(),
    ),
    (
        "partition coarsening_set() contains the source partition",
        lambda _: fixed_ordered_partition() in fixed_ordered_partition().coarsening_set(),
    ),
    (
        "partition ordered_coarsening_closure() is a finite countable set",
        lambda _: fixed_ordered_partition().ordered_coarsening_closure() in Sets().Countable().Finite(),
    ),
    (
        "partition ordered_coarsening_closure() contains the source partition",
        lambda _: fixed_ordered_partition() in fixed_ordered_partition().ordered_coarsening_closure(),
    ),
    (
        "from_restricted_growth_word_blocks([0, 1, 0]) lies over {1,2,3}",
        lambda _: C.from_restricted_growth_word_blocks([0, 1, 0]) in C.SetPartitions(base_set=[1, 2, 3]),
    ),
    (
        "from_restricted_growth_word_intertwining([0, 1, 0]) lies over {1,2,3}",
        lambda _: C.from_restricted_growth_word_intertwining([0, 1, 0]) in C.SetPartitions(base_set=[1, 2, 3]),
    ),
    ("from_arcs([(1, 3)], 3) lies over {1,2,3}", lambda _: C.from_arcs([(1, 3)], 3) in C.SetPartitions(base_set=[1, 2, 3])),
    (
        "from_rook_placement([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.from_rook_placement([(1, 2)], base_set_cardinality=3) in C.SetPartitions(base_set=[1, 2, 3]),
    ),
    (
        "from_rook_placement_gamma([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.from_rook_placement_gamma([(1, 2)], 3) in C.SetPartitions(base_set=[1, 2, 3]),
    ),
    (
        "from_rook_placement_rho([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.from_rook_placement_rho([(1, 2)], 3) in C.SetPartitions(base_set=[1, 2, 3]),
    ),
    (
        "from_rook_placement_psi([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.from_rook_placement_psi([(1, 2)], 3) in C.SetPartitions(base_set=[1, 2, 3]),
    ),
    (
        "cartesian_product([IntegerRange(2), IntegerRange(3)]) is finite countable",
        lambda _: C.cartesian_product([C.IntegerRange(2), C.IntegerRange(3)]) in Sets().Countable().Finite(),
    ),
    (
        "cartesian_product([IntegerRange(2), IntegerRange(3)]) has product cardinality",
        lambda _: C.cartesian_product([C.IntegerRange(2), C.IntegerRange(3)]).cardinality() == 6,
    ),
    (
        "CartesianProduct(factors=[IntegerRange(2), IntegerRange(3)]) has product cardinality",
        lambda _: C.CartesianProduct(factors=[C.IntegerRange(2), C.IntegerRange(3)]).cardinality() == 6,
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)

from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_smoke_statements
from sage.sets.real_set import RealSet as SageRealSet


C = Sets().Constructors()

SMOKE_STATEMENTS = (
    ("ZZ is already an object of Sets()", lambda _: ZZ in Sets()),
    ("ZZ is not finite as a set", lambda _: not ZZ.is_finite()),
    (
        "from_iterable([1, 2, 3]) is a finite countable set",
        lambda _: C.from_iterable([1, 2, 3]) in Sets().Countable().Finite(),
    ),
    (
        "from_iterable([1, 2, 3]) has cardinality 3",
        lambda _: C.from_iterable([1, 2, 3]).cardinality() == 3,
    ),
    (
        "from_iterable([1, 2, 3]) ranks 1 as 2",
        lambda _: C.from_iterable([1, 2, 3])[1] == 2,
    ),
    (
        "from_iterable([1, 2, 3]) is a subset of ZZ",
        lambda _: C.from_iterable([1, 2, 3]).is_subset(ZZ),
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) is a finite countable set",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]) in Sets().Countable().Finite(),
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) has cardinality 3",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]).cardinality() == 3,
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) ranks 1 as 2",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3])[1] == 2,
    ),
    (
        "FiniteEnumeratedSet([1, 2, 3]) is a subset of ZZ",
        lambda _: C.FiniteEnumeratedSet([1, 2, 3]).is_subset(ZZ),
    ),
    ("IntegerRange(5) is a finite countable set", lambda _: C.IntegerRange(5) in Sets().Countable().Finite()),
    ("IntegerRange(5) has cardinality 5", lambda _: C.IntegerRange(5).cardinality() == 5),
    ("IntegerRange(5) ranks 2 as 2", lambda _: C.IntegerRange(5)[2] == 2),
    ("IntegerRange(5) is a subset of ZZ", lambda _: C.IntegerRange(5).is_subset(ZZ)),
    (
        "NonNegativeIntegers() is a countably infinite set",
        lambda _: C.NonNegativeIntegers() in Sets().Countable().Infinite(),
    ),
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
        lambda _: C.RealSet([SageRealSet.open(0, 1).get_interval(0)]) in Sets().Topological(),
    ),
    (
        "RealSet(open interval) is a subobject",
        lambda _: C.RealSet([SageRealSet.open(0, 1).get_interval(0)]) in Sets().Subobjects(),
    ),
    (
        "RealSet(open interval) contains 1/2",
        lambda _: C.RealSet([SageRealSet.open(0, 1).get_interval(0)]).contains(1 / 2),
    ),
    (
        "RealSet(open interval) does not contain 2",
        lambda _: not C.RealSet([SageRealSet.open(0, 1).get_interval(0)]).contains(2),
    ),
    (
        "RealSet(open interval) is open",
        lambda _: C.RealSet([SageRealSet.open(0, 1).get_interval(0)]).is_open(),
    ),
    (
        "RealSet(open interval) has one component",
        lambda _: C.RealSet([SageRealSet.open(0, 1).get_interval(0)]).n_components() == 1,
    ),
    (
        "RealSetInterval(0, 1, open) is a connected topological subobject",
        lambda _: C.RealSetInterval(0, 1, lower_closed=False, upper_closed=False) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "OpenRealInterval(0, 1) is an open real subobject",
        lambda _: C.OpenRealInterval(0, 1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "ClosedRealInterval(0, 1) is a compact connected real subobject",
        lambda _: C.ClosedRealInterval(0, 1) in TopologicalSpaces().Compact().Connected().Subobjects(),
    ),
    (
        "RealPoint(0) is a compact connected real subobject",
        lambda _: C.RealPoint(0) in TopologicalSpaces().Compact().Connected().Subobjects(),
    ),
    (
        "OpenClosedRealInterval(0, 1) is a connected real subobject",
        lambda _: C.OpenClosedRealInterval(0, 1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "ClosedOpenRealInterval(0, 1) is a connected real subobject",
        lambda _: C.ClosedOpenRealInterval(0, 1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "UnboundedBelowClosedRealInterval(1) is a connected real subobject",
        lambda _: C.UnboundedBelowClosedRealInterval(1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "UnboundedBelowOpenRealInterval(1) is a connected real subobject",
        lambda _: C.UnboundedBelowOpenRealInterval(1) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "UnboundedAboveClosedRealInterval(0) is a connected real subobject",
        lambda _: C.UnboundedAboveClosedRealInterval(0) in TopologicalSpaces().Connected().Subobjects(),
    ),
    (
        "UnboundedAboveOpenRealInterval(0) is a connected real subobject",
        lambda _: C.UnboundedAboveOpenRealInterval(0) in TopologicalSpaces().Connected().Subobjects(),
    ),
    ("RealLine() is a connected real subobject", lambda _: C.RealLine() in TopologicalSpaces().Connected().Subobjects()),
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
        "-1 does not lie in RecursivelyEnumeratedSet([0], successors)",
        lambda _: -1 not in C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth"),
    ),
    (
        "RecursivelyEnumeratedSet([0], successors) ranks 3 as 3",
        lambda _: C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth")[3] == 3,
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
        "CartesianProduct([IntegerRange(2), IntegerRange(3)]) is finite countable",
        lambda _: C.CartesianProduct([C.IntegerRange(2), C.IntegerRange(3)]) in Sets().Countable().Finite(),
    ),
    (
        "CartesianProduct([IntegerRange(2), IntegerRange(3)]) has product cardinality",
        lambda _: C.CartesianProduct([C.IntegerRange(2), C.IntegerRange(3)]).cardinality() == 6,
    ),
    ("even subobject of ZZ is a subobject", lambda _: Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,)) in Sets().Subobjects()),
    ("2 lies in the even subobject of ZZ", lambda _: 2 in Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,))),
    ("3 does not lie in the even subobject of ZZ", lambda _: 3 not in Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,))),
    ("even subobject of ZZ has ambient ZZ", lambda _: Sets().Subobjects().Of(ZZ, (lambda n: n % 2 == 0,)).ambient() == ZZ),
    ("ImageSubobject(n + 1, IntegerRange(3)) is a subobject", lambda _: C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3)) in Sets().Subobjects()),
    ("1 lies in ImageSubobject(n + 1, IntegerRange(3))", lambda _: 1 in C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3))),
    ("0 does not lie in ImageSubobject(n + 1, IntegerRange(3))", lambda _: 0 not in C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3))),
    ("ImageSubobject(n + 1, IntegerRange(3)) has cardinality 3", lambda _: C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3)).cardinality() == 3),
    (
        "TotallyOrderedFiniteSet(['a', 'b', 'c']) is finite countable",
        lambda _: C.TotallyOrderedFiniteSet(["a", "b", "c"]) in Sets().Countable().Finite(),
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
    ("Family(IntegerRange(3), i^2) is a set", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2) in Sets()),
    ("Family(IntegerRange(3), i^2) maps 2 to 4", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2)[2] == 4),
    ("Family(IntegerRange(3), i^2) has cardinality 3", lambda _: C.Family(C.IntegerRange(3), lambda i: i**2).cardinality() == 3),
    (
        "EnumeratedSetFromIterator([0, 1, 2]) is finite countable",
        lambda _: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2])) in Sets().Countable().Finite(),
    ),
    (
        "EnumeratedSetFromIterator([0, 1, 2]) has cardinality 3",
        lambda _: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2])).cardinality() == 3,
    ),
    (
        "EnumeratedSetFromIterator([0, 1, 2]) ranks 2 as 2",
        lambda _: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2]))[2] == 2,
    ),
    (
        "1 lies in EnumeratedSetFromIterator([0, 1, 2])",
        lambda _: 1 in C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2])),
    ),
    ("AllSetPartitions() is countable", lambda _: C.AllSetPartitions() in Sets().Countable()),
    ("SetPartitions([1, 2, 3]) is partitioned", lambda _: C.SetPartitions([1, 2, 3]) in Sets().Partitioned()),
    (
        "SetPartitionsWithBlockCount([1, 2, 3], 2) is partitioned",
        lambda _: C.SetPartitionsWithBlockCount([1, 2, 3], 2) in Sets().Partitioned(),
    ),
    (
        "SetPartitionsWithBlockSizes([1, 2, 3], [2, 1]) is partitioned",
        lambda _: C.SetPartitionsWithBlockSizes([1, 2, 3], [2, 1]) in Sets().Partitioned(),
    ),
    ("SetPartition([[1, 3], [2]]) lies over {1,2,3}", lambda _: C.SetPartition([[1, 3], [2]]) in C.SetPartitions([1, 2, 3])),
    (
        "SetPartitionFromRestrictedGrowthWordBlocks([0, 1, 0]) lies over {1,2,3}",
        lambda _: C.SetPartitionFromRestrictedGrowthWordBlocks([0, 1, 0]) in C.SetPartitions([1, 2, 3]),
    ),
    (
        "SetPartitionFromRestrictedGrowthWordIntertwining([0, 1, 0]) lies over {1,2,3}",
        lambda _: C.SetPartitionFromRestrictedGrowthWordIntertwining([0, 1, 0]) in C.SetPartitions([1, 2, 3]),
    ),
    ("SetPartitionFromArcs([(1, 3)], 3) lies over {1,2,3}", lambda _: C.SetPartitionFromArcs([(1, 3)], 3) in C.SetPartitions([1, 2, 3])),
    (
        "SetPartitionFromRookPlacementArcs([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.SetPartitionFromRookPlacementArcs([(1, 2)], 3) in C.SetPartitions([1, 2, 3]),
    ),
    (
        "SetPartitionFromRookPlacementGamma([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.SetPartitionFromRookPlacementGamma([(1, 2)], 3) in C.SetPartitions([1, 2, 3]),
    ),
    (
        "SetPartitionFromRookPlacementRho([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.SetPartitionFromRookPlacementRho([(1, 2)], 3) in C.SetPartitions([1, 2, 3]),
    ),
    (
        "SetPartitionFromRookPlacementPsi([(1, 2)], 3) lies over {1,2,3}",
        lambda _: C.SetPartitionFromRookPlacementPsi([(1, 2)], 3) in C.SetPartitions([1, 2, 3]),
    ),
    (
        "cartesian_product([IntegerRange(2), IntegerRange(3)]) is finite countable",
        lambda _: C.cartesian_product([C.IntegerRange(2), C.IntegerRange(3)]) in Sets().Countable().Finite(),
    ),
    (
        "cartesian_product([IntegerRange(2), IntegerRange(3)]) has product cardinality",
        lambda _: C.cartesian_product([C.IntegerRange(2), C.IntegerRange(3)]).cardinality() == 6,
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

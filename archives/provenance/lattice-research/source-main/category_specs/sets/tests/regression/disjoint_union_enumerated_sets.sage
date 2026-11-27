# Tests for Sets().Constructors().DisjointUnionEnumeratedSets()
# Assertions sourced from sage.sets.disjoint_union_enumerated_sets doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import infinity

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# List input: two FiniteEnumeratedSets  (class docstring)
# ---------------------------------------------------------------------------

U1 = NS.DisjointUnionEnumeratedSets((
    NS.FiniteEnumeratedSet([1, 2, 3]),
    NS.FiniteEnumeratedSet([4, 5, 6])))
assert U1.list() == [1, 2, 3, 4, 5, 6]
assert U1.cardinality() == 6

# ---------------------------------------------------------------------------
# Dictionary input  (class docstring)
# ---------------------------------------------------------------------------

U2 = NS.DisjointUnionEnumeratedSets({
    1: NS.FiniteEnumeratedSet([1, 2, 3]),
    2: NS.FiniteEnumeratedSet([4, 5, 6])})
assert U2.list() == [1, 2, 3, 4, 5, 6]
assert U2.cardinality() == 6

# ---------------------------------------------------------------------------
# UniqueRepresentation: same dict gives same object  (__classcall__ doctest)
# ---------------------------------------------------------------------------

U1a = NS.DisjointUnionEnumeratedSets({
    1: NS.FiniteEnumeratedSet([1, 2, 3]),
    2: NS.FiniteEnumeratedSet([4, 5, 6])})
U1b = NS.DisjointUnionEnumeratedSets({
    1: NS.FiniteEnumeratedSet([1, 2, 3]),
    2: NS.FiniteEnumeratedSet([4, 5, 6])})
assert U1a == U1b
assert U1a is U1b

# ---------------------------------------------------------------------------
# Containment  (class docstring, __contains__)
# ---------------------------------------------------------------------------

assert 1 in U1
assert 4 in U1
assert 7 not in U1

# ---------------------------------------------------------------------------
# Iteration order from family  (__iter__ doctest — finite case)
# ---------------------------------------------------------------------------

U_iter = NS.DisjointUnionEnumeratedSets((
    NS.FiniteEnumeratedSet([10, 11]),
    NS.FiniteEnumeratedSet([20, 21])))
assert list(U_iter) == [10, 11, 20, 21]

# ---------------------------------------------------------------------------
# Cardinality from Family([0,1,2,3], Permutations)  (cardinality doctest)
# ---------------------------------------------------------------------------

from sage.combinat.permutation import Permutations

U_perm = NS.DisjointUnionEnumeratedSets(NS.Family([0, 1, 2, 3], Permutations))
# 1 + 1 + 2 + 6 = 10
assert U_perm.cardinality() == 10

# ---------------------------------------------------------------------------
# Infinite union cardinality  (cardinality doctest)
# ---------------------------------------------------------------------------

U_inf = NS.DisjointUnionEnumeratedSets(NS.Family(NS.NonNegativeIntegers(), Permutations))
assert U_inf.cardinality() == infinity

# ---------------------------------------------------------------------------
# Iteration prefix of infinite union  (class docstring)
# ---------------------------------------------------------------------------

it = iter(U_inf)
assert [next(it) for _ in range(6)] == [[], [1], [1, 2], [2, 1], [1, 2, 3], [1, 3, 2]]

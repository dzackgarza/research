# Tests for Sets().Constructors().IntegerRange()
# Assertions sourced from sage.sets.integer_range doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import Integer, Infinity, infinity

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# Basic finite ranges  (class docstring)
# ---------------------------------------------------------------------------

assert list(NS.IntegerRange(5)) == [0, 1, 2, 3, 4]
assert list(NS.IntegerRange(2, 5)) == [2, 3, 4]

I = NS.IntegerRange(2, 100, 5)
assert list(I) == [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]

# Equivalence with Python range  (class docstring)
assert list(NS.IntegerRange(4, 105, 3)) == list(range(4, 105, 3))
assert list(NS.IntegerRange(-54, 13, 12)) == list(range(-54, 13, 12))

# Elements are Sage Integers  (class docstring)
assert type(NS.IntegerRange(-54, 13, 12)[0]) == Integer

# ---------------------------------------------------------------------------
# Cardinality  (IntegerRangeFinite.cardinality doctest)
# ---------------------------------------------------------------------------

assert NS.IntegerRange(123, 12, -4).cardinality() == 28
assert NS.IntegerRange(-57, 12, 8).cardinality() == 9
assert NS.IntegerRange(123, 12, 4).cardinality() == 0

# ---------------------------------------------------------------------------
# __contains__  (IntegerRangeFinite.__contains__ doctest)
# ---------------------------------------------------------------------------

I = NS.IntegerRange(123, 12, -4)
assert 123 in I
assert 127 not in I
assert 12 not in I
assert 15 in I
assert 11 not in I

# ---------------------------------------------------------------------------
# rank / unrank  (IntegerRangeFinite.rank doctest)
# ---------------------------------------------------------------------------

I = NS.IntegerRange(-57, 36, 8)
assert I.rank(23) == 10
assert I.unrank(10) == 23

# ---------------------------------------------------------------------------
# __getitem__ with positive and negative indices  (doctest)
# ---------------------------------------------------------------------------

I = NS.IntegerRange(1, 13, 5)
assert I[0] == 1 and I[1] == 6 and I[2] == 11
assert I[-1] == 11

# ---------------------------------------------------------------------------
# Infinite ranges  (class docstring)
# ---------------------------------------------------------------------------

I_inf = NS.IntegerRange(54, Infinity, 3)
p = iter(I_inf)
assert [next(p) for _ in range(6)] == [54, 57, 60, 63, 66, 69]

I_neg = NS.IntegerRange(54, -Infinity, -3)
p = iter(I_neg)
assert [next(p) for _ in range(6)] == [54, 51, 48, 45, 42, 39]

# ---------------------------------------------------------------------------
# Middle-point enumeration  (class docstring)
# ---------------------------------------------------------------------------

I_mid = NS.IntegerRange(123, -12, -14)
assert list(I_mid) == [123, 109, 95, 81, 67, 53, 39, 25, 11, -3]

J_mid = NS.IntegerRange(123, -12, -14, 25)
assert list(J_mid) == [25, 11, 39, -3, 53, 67, 81, 95, 109, 123]

# ---------------------------------------------------------------------------
# Iteration over finite range  (IntegerRangeFinite.__iter__ doctest)
# ---------------------------------------------------------------------------

I = NS.IntegerRange(123, 12, -4)
p = iter(I)
assert [next(p) for _ in range(8)] == [123, 119, 115, 111, 107, 103, 99, 95]

I = NS.IntegerRange(-57, 12, 8)
p = iter(I)
assert [next(p) for _ in range(8)] == [-57, -49, -41, -33, -25, -17, -9, -1]

# ---------------------------------------------------------------------------
# Input normalisation: IntegerRange(1,6,2) is IntegerRange(1,7,2)  (NOTE in docstring)
# ---------------------------------------------------------------------------

assert NS.IntegerRange(1, 6, 2) == NS.IntegerRange(1, 7, 2)
assert NS.IntegerRange(1, 8, 3) == NS.IntegerRange(1, 10, 3)

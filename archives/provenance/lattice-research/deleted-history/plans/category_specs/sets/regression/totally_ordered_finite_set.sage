# Tests for Sets().NamedSets().TotallyOrderedFiniteSet()
# Assertions sourced from sage.sets.totally_ordered_finite_set doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import ZZ

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# Basic construction, cardinality  (class docstring)
# ---------------------------------------------------------------------------

S = NS.TotallyOrderedFiniteSet([1, 2, 3])
assert S.cardinality() == 3

# ---------------------------------------------------------------------------
# Facade mode (default): elements retain their original parent  (class docstring)
# ---------------------------------------------------------------------------

assert S(1).parent() == ZZ

# ---------------------------------------------------------------------------
# Duplicate removal  (class docstring)
# ---------------------------------------------------------------------------

D = NS.TotallyOrderedFiniteSet([1, 1, 2, 1, 2, 2, 5, 4])
assert list(D) == [1, 2, 5, 4]

# ---------------------------------------------------------------------------
# UniqueRepresentation: list, tuple, range give the same object  (__classcall__)
# ---------------------------------------------------------------------------

S1 = NS.TotallyOrderedFiniteSet([1, 2, 3])
S2 = NS.TotallyOrderedFiniteSet((1, 2, 3))
S3 = NS.TotallyOrderedFiniteSet(range(1, 4))
assert S1 is S2
assert S2 is S3

# ---------------------------------------------------------------------------
# Non-facade mode: custom ordering respected  (class docstring)
# ---------------------------------------------------------------------------

A = NS.TotallyOrderedFiniteSet([3, 2, 0, 'a', 7, (0, 0), 1], facade=False)
assert A.cardinality() == 7

x = A.an_element()
assert x.parent() is A

# Ordering follows rank (position), not natural value order
assert A(3) < A(2)       # 3 is rank 0, 2 is rank 1 → 3 < 2 in this order
assert A('a') < A(7)     # 'a' is rank 3, 7 is rank 4
assert not (A(3) > A(2))
assert not (A(1) < A(3)) # 1 is rank 6 (last), 3 is rank 0
assert A(3) == A(3)

# ---------------------------------------------------------------------------
# Non-facade equality is strict: cross-parent comparisons are always False
# ---------------------------------------------------------------------------

assert (A(1) == 1) is False
assert (A('a') == 'a') is False

# ---------------------------------------------------------------------------
# le()  (TotallyOrderedFiniteSet.le doctest)
# ---------------------------------------------------------------------------

T = NS.TotallyOrderedFiniteSet([1, 3, 2], facade=False)
T1, T3, T2 = T.list()
assert T.le(T1, T3) is True
assert T.le(T3, T2) is True
assert T.le(T2, T3) is False

# ---------------------------------------------------------------------------
# Non-facade element operations: _richcmp_  (TotallyOrderedFiniteSetElement)
# ---------------------------------------------------------------------------

B = NS.TotallyOrderedFiniteSet([3, 2, 7], facade=False)
assert B(3) < B(2) and B(3) <= B(2) and B(2) <= B(2)
assert B(2) > B(3) and B(2) >= B(3) and B(7) >= B(7)
assert not (B(3) >= B(7))
assert not (B(2) > B(2))
assert not (B(7) < B(2))
assert not (B(2) <= B(3))
assert not (B(2) < B(2))

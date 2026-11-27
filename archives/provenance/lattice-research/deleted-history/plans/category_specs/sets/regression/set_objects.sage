# Tests for Sets().NamedSets().Set()
# Assertions sourced from sage.sets.set doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import ZZ, QQ

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# Basic construction, duplicate removal  (Set function docstring)
# ---------------------------------------------------------------------------

X = NS.Set([1, 2, 3])
assert 1 in X
assert 2 in X
assert 5 not in X

# Duplicates are silently removed: {1,1,1,5,6} has 3 elements
D = NS.Set([1, 1, 1, 5, 6])
assert D.cardinality() == 3

# Snapshot semantics: mutating original list does not affect the set
v = [1, 2, 3]
XV = NS.Set(v)
v.append(5)
assert 5 not in XV

# ---------------------------------------------------------------------------
# Cardinality  (Set_object_enumerated.cardinality doctest)
# ---------------------------------------------------------------------------

assert NS.Set([1, 1]).cardinality() == 1
assert NS.Set([1, 2, 3]).cardinality() == 3

# ---------------------------------------------------------------------------
# is_empty  (Set_object.is_empty doctest)
# ---------------------------------------------------------------------------

assert NS.Set([]).is_empty() is True
assert NS.Set([0]).is_empty() is False
assert NS.Set(list(range(1, 101))).is_empty() is False

# ---------------------------------------------------------------------------
# is_finite  (Set_object.is_finite doctest)
# ---------------------------------------------------------------------------

assert NS.Set([1, 'a', ZZ]).is_finite() is True

# ---------------------------------------------------------------------------
# __contains__  (Set_object.__contains__ doctest)
# ---------------------------------------------------------------------------

Xz = NS.Set(ZZ)
assert 5 in Xz
assert (2/1) in Xz
assert (2/3) not in Xz

# ---------------------------------------------------------------------------
# list / frozenset  (Set_object_enumerated.list doctest)
# ---------------------------------------------------------------------------

L = NS.Set([3, 1, 2])
assert set(L.list()) == {1, 2, 3}
assert isinstance(L.list(), list)

# ---------------------------------------------------------------------------
# union / intersection / difference / symmetric_difference  (Set_base docs)
# ---------------------------------------------------------------------------

A = NS.Set([1, 2, 3, 4])
B = NS.Set([1, 2])

assert set(A.difference(B).list()) == {3, 4}
assert set(A.symmetric_difference(B).list()) == {3, 4}
assert set(A.intersection(B).list()) == {1, 2}
assert set(A.union(B).list()) == {1, 2, 3, 4}

# Set([2,3]) | Set([3,4]) → {2, 3, 4}
assert set((NS.Set([2, 3]) | NS.Set([3, 4])).list()) == {2, 3, 4}

# Set([2,3]) & Set([3,4]) → {3}
assert set((NS.Set([2, 3]) & NS.Set([3, 4])).list()) == {3}

# symmetric_difference via ^ operator
X4 = NS.Set([1, 2, 3, 4])
Y2 = NS.Set([1, 2])
assert set((X4 ^ Y2).list()) == {3, 4}

# ---------------------------------------------------------------------------
# issubset / issuperset  (Set_object_enumerated.issubset doctest)
# ---------------------------------------------------------------------------

X135 = NS.Set([1, 3, 5])
Y01235 = NS.Set([0, 1, 2, 3, 5, 7])
assert X135.issubset(Y01235) is True
assert Y01235.issubset(X135) is False
assert X135.issubset(X135) is True
assert Y01235.issuperset(X135) is True
assert X135.issuperset(Y01235) is False
assert X135.issuperset(X135) is True

# ---------------------------------------------------------------------------
# subsets  (Set_object.subsets doctest)
# ---------------------------------------------------------------------------

X3 = NS.Set([1, 2, 3])
assert len(list(X3.subsets())) == 8
assert len(list(X3.subsets(2))) == 3

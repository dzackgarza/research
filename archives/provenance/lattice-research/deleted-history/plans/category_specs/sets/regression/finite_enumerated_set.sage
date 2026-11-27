# Tests for Sets().NamedSets().FiniteEnumeratedSet()
# Assertions sourced from sage.sets.finite_enumerated_set.FiniteEnumeratedSet doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import ZZ

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# Basic construction, list, cardinality, first  (class docstring)
# ---------------------------------------------------------------------------

S = NS.FiniteEnumeratedSet([1, 2, 3])
assert S.list() == [1, 2, 3]
assert S.cardinality() == 3
assert S.first() == 1

# Order matters: (1,2,3) and (2,1,3) are distinct enumerated sets
S1 = NS.FiniteEnumeratedSet((1, 2, 3))
S2 = NS.FiniteEnumeratedSet((2, 1, 3))
assert S1 == S
assert S2 != S

# Elements are plain Sage integers; their parent is ZZ, not the set  (class docstring)
assert S.first().parent() == ZZ

# ---------------------------------------------------------------------------
# __contains__  (doctest)
# ---------------------------------------------------------------------------

assert 1 in S
assert 2 in S
assert 4 not in S
assert ZZ not in S

# ---------------------------------------------------------------------------
# __iter__  (doctest)
# ---------------------------------------------------------------------------

assert list(S) == [1, 2, 3]

# ---------------------------------------------------------------------------
# first / last  (doctest)
# ---------------------------------------------------------------------------

T = NS.FiniteEnumeratedSet([0, 'a', 1.23, 'd'])
assert T.first() == 0
assert T.last() == 'd'

# ---------------------------------------------------------------------------
# rank / index  (doctest — rank and index are aliases)
# ---------------------------------------------------------------------------

Sa = NS.FiniteEnumeratedSet(['a', 'b', 'c'])
assert Sa.rank('b') == 1
assert Sa.index('b') == 1

# ---------------------------------------------------------------------------
# unrank / __getitem__  (doctest)
# ---------------------------------------------------------------------------

Su = NS.FiniteEnumeratedSet([1, 'a', -51])
assert Su[0] == 1
assert Su[1] == 'a'
assert Su[2] == -51
assert Su[-1] == -51
assert Su[-3] == 1

# ---------------------------------------------------------------------------
# random_element  (doctest)
# ---------------------------------------------------------------------------

assert S.random_element() in S

# ---------------------------------------------------------------------------
# an_element  (doctest)
# ---------------------------------------------------------------------------

assert S.an_element() == 1

# ---------------------------------------------------------------------------
# bool conversion  (doctest)
# ---------------------------------------------------------------------------

assert bool(NS.FiniteEnumeratedSet('abc')) is True
assert bool(NS.FiniteEnumeratedSet([])) is False

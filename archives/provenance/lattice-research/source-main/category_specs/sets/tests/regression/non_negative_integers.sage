# Tests for Sets().Constructors().NonNegativeIntegers() and .PositiveIntegers()
# Assertions sourced from sage.sets.non_negative_integers and positive_integers doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import ZZ, QQbar, RIF, infinity

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# NonNegativeIntegers  (class docstring and method doctests)
# ---------------------------------------------------------------------------

NN = NS.NonNegativeIntegers()

assert NN.cardinality() == infinity

# iteration  (class docstring)
it = iter(NN)
assert [next(it), next(it), next(it), next(it), next(it)] == [0, 1, 2, 3, 4]

assert NN.first() == 0

# an_element  (doctest)
assert NN.an_element() == 42

# some_elements  (doctest)
assert NN.some_elements() == [0, 1, 3, 42]

# next  (doctest)
assert NN.next(3) == 4

# unrank  (doctest)
assert NN.unrank(100) == 100

# __contains__  (doctest)
assert 1 in NN
assert -1 not in NN

# elements are plain Sage integers with parent ZZ  (class docstring)
x = NN(15)
assert x.parent() == ZZ
assert x + 3 == 18

# ---------------------------------------------------------------------------
# PositiveIntegers  (sage.sets.positive_integers)
# ---------------------------------------------------------------------------

PP = NS.PositiveIntegers()

assert PP.cardinality() == infinity
assert 1 in PP
assert 0 not in PP
assert -1 not in PP
assert PP.first() == 1
assert PP.next(8) == 9
assert PP.unrank(0) == 1
assert PP.an_element() in PP

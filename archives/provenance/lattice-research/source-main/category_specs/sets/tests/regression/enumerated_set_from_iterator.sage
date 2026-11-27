# Tests for Sets().Constructors().EnumeratedSetFromIterator()
# Assertions sourced from sage.sets.set_from_iterator.EnumeratedSetFromIterator doctests.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import FiniteEnumeratedSets, InfiniteEnumeratedSets, infinity, xsrange
from itertools import count

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# Finite set from xsrange  (EnumeratedSetFromIterator.__init__ doctest)
# ---------------------------------------------------------------------------

S_fin = NS.EnumeratedSetFromIterator(
    lambda: xsrange(1, 200, -1), category=FiniteEnumeratedSets())
# xsrange(1, 200, -1) is empty (step negative, start < stop), so list is []
assert S_fin in Sets().Finite()
assert S_fin.cardinality() == 0
assert list(S_fin) == []

# ---------------------------------------------------------------------------
# Infinite set with cache: count from 0  (TESTS in class docstring)
# ---------------------------------------------------------------------------

E_inf = NS.EnumeratedSetFromIterator(
    lambda: count(0), category=InfiniteEnumeratedSets(), cache=True)
assert E_inf.cardinality() == infinity

e1 = iter(E_inf)
e2 = iter(E_inf)
assert next(e1) == 0 and next(e1) == 1
assert next(e2) == 0 and next(e2) == 1 and next(e2) == 2
assert next(e1) == 2 and next(e1) == 3
assert next(e2) == 3

# ---------------------------------------------------------------------------
# Finite set from xsrange with cache  (TESTS in class docstring)
# ---------------------------------------------------------------------------

E_fin2 = NS.EnumeratedSetFromIterator(
    lambda: xsrange(10), category=FiniteEnumeratedSets(), cache=True)
assert list(E_fin2) == list(range(10))

# ---------------------------------------------------------------------------
# Custom name  (class docstring)
# ---------------------------------------------------------------------------

from sage.graphs.graph_generators import graphs

E_graphs = NS.EnumeratedSetFromIterator(
    lambda: graphs(3),
    category=FiniteEnumeratedSets(),
    name="Graphs on 3 vertices")
assert repr(E_graphs) == "Graphs on 3 vertices"

# ---------------------------------------------------------------------------
# __contains__: membership test  (__contains__ doctest)
# ---------------------------------------------------------------------------

from sage.combinat.partition import Partitions

P12 = Partitions(12, min_part=2, max_part=5)
E_parts = NS.EnumeratedSetFromIterator(P12.__iter__)
assert P12([5, 5, 2]) in E_parts

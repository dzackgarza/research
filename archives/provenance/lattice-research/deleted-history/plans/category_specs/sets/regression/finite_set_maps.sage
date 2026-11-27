# Tests for Sets().NamedSets().FiniteSetMaps()
# Assertions sourced from sage.sets.finite_set_maps.FiniteSetMaps doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# Maps from {a,b} to {3,4,5}  (class docstring)
# ---------------------------------------------------------------------------

M = NS.FiniteSetMaps(["a", "b"], [3, 4, 5])
assert M.cardinality() == 9
assert set(M.domain().list()) == {'a', 'b'}
assert set(M.codomain().list()) == {3, 4, 5}

# All 9 maps enumerated
maps_list = list(M)
assert len(maps_list) == 9

# Construct a map from a function
f = M(lambda c: ord(c) - 94)
assert f == M.from_dict({'a': 3, 'b': 4})

# from_dict
g = M.from_dict({'a': 3, 'b': 5})
assert g in M

# ---------------------------------------------------------------------------
# Endomorphisms: FiniteSetMaps([1,2,3]) forms a monoid  (class docstring)
# ---------------------------------------------------------------------------

Endo = NS.FiniteSetMaps([1, 2, 3])
f2 = Endo.from_dict({1: 2, 2: 1, 3: 3})
g2 = Endo.from_dict({1: 2, 2: 3, 3: 1})

# f2 * g2: first apply g2, then f2 (left action / composition from right)
assert f2 * g2 == Endo.from_dict({1: 1, 2: 3, 3: 2})

# identity element of the monoid
assert Endo.one() == Endo.from_dict({1: 1, 2: 2, 3: 3})

# ---------------------------------------------------------------------------
# Integer shorthand: FiniteSetMaps(2, 3)  (class docstring)
# ---------------------------------------------------------------------------

M23 = NS.FiniteSetMaps(2, 3)
assert M23.cardinality() == 9
# Elements printed as [f(0), f(1)]
all_maps = list(M23)
assert len(all_maps) == 9
assert [0, 0] in all_maps

# ---------------------------------------------------------------------------
# Cardinality formula: |cod|^|dom|  (FiniteSetMaps.cardinality doctest)
# ---------------------------------------------------------------------------

assert NS.FiniteSetMaps(4, 3).cardinality() == 81

# Tests for Sets().Constructors().CartesianProduct()
# Assertions sourced from sage.sets.cartesian_product.CartesianProduct doctests.
# Note: Sage's product constructor takes a finite factor collection; the project
# constructor keeps that name and forces the factor role to be named.

import sys
sys.path.insert(0, '/home/dzack/research/plans')
sys.path.insert(0, '/home/dzack/research')
from category_specs.sets import Sets
from sage.all import ZZ, QQ, GF

NS = Sets().Constructors()

# ---------------------------------------------------------------------------
# cartesian_factors  (class docstring)
# ---------------------------------------------------------------------------

G = NS.CartesianProduct(factors=[GF(5), ZZ])
assert G.cartesian_factors() == (GF(5), ZZ)

# ---------------------------------------------------------------------------
# cardinality: small finite product  (class docstring example scaled down)
# ---------------------------------------------------------------------------

G2 = NS.CartesianProduct(factors=[GF(5), NS.IntegerRange(3)])
assert G2.cardinality() == 15

# ---------------------------------------------------------------------------
# __contains__  (__contains__ doctest)
# ---------------------------------------------------------------------------

C = NS.CartesianProduct(factors=[NS.IntegerRange(5), NS.IntegerRange(5)])
assert (1, 1) in C
assert (1, 6) not in C

# ---------------------------------------------------------------------------
# _element_constructor_  (doctest)
# ---------------------------------------------------------------------------

Cprod = NS.CartesianProduct(factors=[GF(5), GF(3)])
x = Cprod((1, 3))
assert x[0].parent() == GF(5)
assert x[1].parent() == GF(3)
# (1, 3) in GF(5) × GF(3): 3 mod 3 = 0
assert x == Cprod((1, 0))

# An iterable also works
x2 = Cprod(i for i in range(2))
assert x2 == Cprod((0, 1))

# ---------------------------------------------------------------------------
# CartesianProduct of (QQ, ZZ, ZZ) — an_element  (__init__ doctest)
# ---------------------------------------------------------------------------

C_QZZ = NS.CartesianProduct(factors=[QQ, ZZ, ZZ])
assert C_QZZ.an_element() == (QQ.an_element(), ZZ.an_element(), ZZ.an_element())

# ---------------------------------------------------------------------------
# Comparison: ZZ×ZZ coerces from ZZ×ZZ  (_coerce_map_from_ doctest)
# ---------------------------------------------------------------------------

Z = NS.cartesian_product([ZZ])
Qq = NS.cartesian_product([QQ])
assert Qq.has_coerce_map_from(Z)
assert not Z.has_coerce_map_from(Qq)

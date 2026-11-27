# Tests for Sets().NamedSets().Primes()
# Assertions sourced from sage.sets.primes.Primes doctests.
# Each assertion verifies the wrapped object recovers the same behaviour
# as the underlying Sage Primes() object.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import ZZ, infinity

P = Sets().NamedSets().Primes()

# ---------------------------------------------------------------------------
# Cardinality and membership  (Primes class docstring)
# ---------------------------------------------------------------------------

assert P.cardinality() == infinity
assert 5 in P
assert 100 not in P

# ---------------------------------------------------------------------------
# first / next / unrank  (individual method doctests)
# ---------------------------------------------------------------------------

assert P.first() == 2

assert P.next(5) == 7

assert P.unrank(0) == 2
assert P.unrank(5) == 13
assert P.unrank(42) == 191

# ---------------------------------------------------------------------------
# an_element  (_an_element_ doctest)
# ---------------------------------------------------------------------------

assert P.an_element() == 43

# ---------------------------------------------------------------------------
# Uniqueness: two calls return the same object  (__classcall__ doctest)
# ---------------------------------------------------------------------------

assert Sets().NamedSets().Primes() == P

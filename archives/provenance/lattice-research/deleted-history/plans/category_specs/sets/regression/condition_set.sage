# Tests for Sets().NamedSets().ConditionSet()
# Assertions sourced from sage.sets.condition_set.ConditionSet doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.sets import Sets
from sage.all import ZZ, is_even, is_odd, is_prime, IntegerModRing

NS = Sets().NamedSets()

# ---------------------------------------------------------------------------
# Basic predicate: even integers  (class docstring)
# ---------------------------------------------------------------------------

Evens = NS.ConditionSet(ZZ, is_even)
assert 2 in Evens
assert 3 not in Evens
assert 2.0 in Evens

# ---------------------------------------------------------------------------
# Union of two condition sets  (class docstring)
# ---------------------------------------------------------------------------

Odds = NS.ConditionSet(ZZ, is_odd)
EvensAndOdds = Evens | Odds
assert 5 in EvensAndOdds
assert (7/2) not in EvensAndOdds

# ---------------------------------------------------------------------------
# Iteration via iterator_range over integers  (class docstring)
# ---------------------------------------------------------------------------

assert list(Odds.iterator_range(stop=6)) == [1, -1, 3, -3, 5, -5]

# ---------------------------------------------------------------------------
# Finite universe: ring of integers modulo 8, filtered by is_prime
# ---------------------------------------------------------------------------

R = IntegerModRing(8)
R_primes = NS.ConditionSet(R, is_prime)
assert R_primes.is_finite() is True
assert list(R_primes) == [2, 6]

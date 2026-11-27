# Tests for Rings().Constructors().ZZ()
# Assertions sourced from sage.rings.integer_ring and sage.rings.integer doctests.
# Verifies the wrapped ZZ still recovers all documented mathematical behaviour.

import sys
sys.path.insert(0, '/home/dzack/research')
from category_specs.rings import Rings
from sage.all import ZZ as _ZZ, factor

NR = Rings().Constructors()
ZZ = NR.ZZ()

# ---------------------------------------------------------------------------
# Ring predicates  (IntegerRing class docstring and method doctests)
# ---------------------------------------------------------------------------

assert ZZ.is_commutative_ring() is True
assert ZZ.is_integral_domain() is True
assert ZZ.characteristic() == 0
assert ZZ.is_euclidean_domain() is True
assert ZZ.is_pid() is True
assert ZZ.is_unique_factorization_domain() is True
assert ZZ.is_field() is False
assert ZZ.is_finite() is False
assert ZZ.is_noetherian() is True

# ---------------------------------------------------------------------------
# Element arithmetic  (Integer doctests)
# ---------------------------------------------------------------------------

assert ZZ(3) + ZZ(4) == ZZ(7)
assert ZZ(3) * ZZ(4) == ZZ(12)
assert ZZ(7) - ZZ(3) == ZZ(4)
assert ZZ(12) // ZZ(4) == ZZ(3)
assert ZZ(13) % ZZ(5) == ZZ(3)
assert ZZ(2) ** 10 == ZZ(1024)

# ---------------------------------------------------------------------------
# Units, zero, one  (Integer.is_unit, is_zero, is_one doctests)
# ---------------------------------------------------------------------------

assert ZZ(1).is_unit() is True
assert ZZ(-1).is_unit() is True
assert ZZ(0).is_unit() is False
assert ZZ(2).is_unit() is False
assert ZZ(0).is_zero() is True
assert ZZ(1).is_one() is True

# ---------------------------------------------------------------------------
# GCD / LCM / XGCD  (sage.rings.integer_ring doctests)
# ---------------------------------------------------------------------------

assert ZZ.gcd(12, 18) == 6
assert ZZ.gcd(0, 5) == 5
assert ZZ.lcm(4, 6) == 12

g, u, v = ZZ.xgcd(12, 18)
assert g == 6
assert 12 * u + 18 * v == g

# ---------------------------------------------------------------------------
# Factoring and primality  (Integer.factor, is_prime, is_irreducible doctests)
# ---------------------------------------------------------------------------

assert ZZ(5).is_prime() is True
assert ZZ(4).is_prime() is False
assert ZZ(1).is_prime() is False
assert ZZ(-5).is_prime() is False  # negative integers are not prime in Sage

f12 = ZZ(12).factor()
assert dict(f12) == {2: 2, 3: 1}   # 2^2 * 3

f_neg = ZZ(-12).factor()
assert f_neg.unit() == -1

# ---------------------------------------------------------------------------
# Ideals  (IntegerRing.ideal doctest)
# ---------------------------------------------------------------------------

I6 = ZZ.ideal(6)
assert I6.gens() == (6,)
assert ZZ(12) in I6
assert ZZ(7) not in I6

I_triv = ZZ.ideal(0)
assert I_triv.is_zero() is True

# ---------------------------------------------------------------------------
# Powers and roots  (Integer.nth_root, sqrt doctests)
# ---------------------------------------------------------------------------

assert ZZ(8).nth_root(3) == 2
assert ZZ(4).sqrt() == 2
assert ZZ(25).is_square() is True
assert ZZ(3).is_square() is False

# ---------------------------------------------------------------------------
# Additive and multiplicative orders  (Integer.additive_order doctest)
# ---------------------------------------------------------------------------

assert ZZ(5).additive_order() == _ZZ(0)  # infinite order in ZZ → returns 0
assert ZZ(0).additive_order() == 1        # 0 has additive order 1

# ---------------------------------------------------------------------------
# Nilpotency  (Integer.is_nilpotent doctest)
# ---------------------------------------------------------------------------

assert ZZ(0).is_nilpotent() is True
assert ZZ(5).is_nilpotent() is False

# ---------------------------------------------------------------------------
# Fraction field  (IntegralDomain.fraction_field doctest)
# ---------------------------------------------------------------------------

from sage.all import QQ
assert ZZ.fraction_field() is QQ

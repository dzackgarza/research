# Tests for Rings().NamedRings().GF() / .FiniteField()
# Assertions sourced from sage.rings.finite_rings doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.rings import Rings
from sage.all import ZZ, GF as _GF

NR = Rings().NamedRings()

# ---------------------------------------------------------------------------
# Prime fields GF(p)  (FiniteField_prime_modn class docstring)
# ---------------------------------------------------------------------------

F2 = NR.GF(2)
assert F2.characteristic() == 2
assert F2.order() == 2
assert F2.degree() == 1
assert F2.is_field() is True
assert F2.is_finite() is True
assert F2.is_prime_field() is True

F7 = NR.GF(7)
assert F7.characteristic() == 7
assert F7.order() == 7

# Arithmetic in GF(7)
assert F7(3) + F7(5) == F7(1)    # 8 mod 7 = 1
assert F7(3) * F7(3) == F7(2)    # 9 mod 7 = 2
assert F7(3).inverse() == F7(5)  # 3 * 5 = 15 ≡ 1 (mod 7)
assert F7(0).is_zero() is True
assert F7(1).is_one() is True
assert F7(3).is_unit() is True
assert F7(0).is_unit() is False

# Additive order of nonzero element = characteristic
assert F7(1).additive_order() == 7

# Multiplicative order: GF(7)* is cyclic of order 6
assert F7(3).multiplicative_order() == 6   # 3 is a primitive root mod 7

# ---------------------------------------------------------------------------
# GF(p^n) — extension fields  (FiniteField class docstring)
# ---------------------------------------------------------------------------

F9 = NR.GF(9, 'a')
assert F9.characteristic() == 3
assert F9.order() == 9
assert F9.degree() == 2
assert F9.is_prime_field() is False

a = F9.gen()
# a satisfies the defining polynomial over GF(3)
assert a.minpoly().degree() == 2
# Frobenius: a^3 is the image of a under Frobenius
assert a ** 3 == a.frobenius()

F25 = NR.GF(25, 'b')
assert F25.order() == 25
assert F25.characteristic() == 5
assert F25.degree() == 2

b = F25.gen()
assert b ** 25 == b   # Frobenius fixed-point identity

# ---------------------------------------------------------------------------
# FiniteField alias  (same as GF)
# ---------------------------------------------------------------------------

K = NR.FiniteField(49, 'c')
assert K.order() == 49
assert K.characteristic() == 7
assert K.degree() == 2

# ---------------------------------------------------------------------------
# Multiplicative generator / primitive element
# ---------------------------------------------------------------------------

F8 = NR.GF(8, 'g')
g = F8.multiplicative_generator()
assert g.multiplicative_order() == 7   # |GF(8)*| = 7

g_F7 = F7.multiplicative_generator()
assert g_F7.multiplicative_order() == 6

# ---------------------------------------------------------------------------
# Modulus  (defining polynomial)
# ---------------------------------------------------------------------------

F9b = NR.GF(9, 'a')
assert F9b.modulus().degree() == 2
assert F9b.modulus().base_ring() is _GF(3)

# ---------------------------------------------------------------------------
# Galois group  (finite field automorphism group = cyclic Frobenius)
# ---------------------------------------------------------------------------

G = F9.galois_group()
assert G.order() == 2   # Gal(GF(9)/GF(3)) ≅ Z/2Z

# ---------------------------------------------------------------------------
# factored_order  (FiniteField.factored_order)
# ---------------------------------------------------------------------------

assert dict(F9.factored_order()) == {3: 2}
assert dict(F25.factored_order()) == {5: 2}

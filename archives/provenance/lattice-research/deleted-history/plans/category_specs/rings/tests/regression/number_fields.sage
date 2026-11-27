# Tests for Rings().Constructors().NumberField() / .QuadraticField() / .CyclotomicField()
# Assertions sourced from sage.rings.number_field.number_field doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.rings import Rings
from sage.all import ZZ, QQ, polygen, sqrt, CyclotomicField as _CyclotomicField

NR = Rings().Constructors()
x = polygen(QQ, 'x')

# ---------------------------------------------------------------------------
# NumberField: basic quadratic  (NumberField class docstring)
# ---------------------------------------------------------------------------

K = NR.NumberField(x**2 + 1, 'i')
i = K.gen()

assert K.degree() == 2
assert K.absolute_degree() == 2
assert K.signature() == (0, 1)    # no real embeddings, one complex pair
assert K.discriminant() == -4
assert K.is_field() is True
assert K.is_number_field() is True
assert K.characteristic() == 0

# Generator satisfies the defining relation
assert i**2 == -1
assert i**2 + 1 == 0

# Class number of Z[i] is 1 (Gaussian integers are a PID)
assert K.class_number() == 1

# Ring of integers is Z[i]
OK = K.ring_of_integers()
assert OK.is_dedekind_domain() is True

# Real and complex embeddings
assert len(K.real_embeddings()) == 0
assert len(K.complex_embeddings()) == 2

# Norm and trace of i
assert i.norm() == 1
assert i.trace() == 0

# Minpoly of i is x^2 + 1
assert i.minpoly() == x**2 + 1

# ---------------------------------------------------------------------------
# QuadraticField  (QuadraticField docstring)
# ---------------------------------------------------------------------------

L = NR.QuadraticField(5, 'a')
a = L.gen()

assert L.degree() == 2
assert L.signature() == (2, 0)    # real quadratic field (d = 5 > 0)
assert L.discriminant() == 5
assert L.is_field() is True
assert L.is_number_field() is True

# a = sqrt(5), so a^2 = 5
assert a**2 == 5

# Class number of Q(sqrt(5)) is 1
assert L.class_number() == 1

# Fundamental discriminant: 5 ≡ 1 (mod 4), so disc = 5
OL = L.ring_of_integers()
assert OL.is_dedekind_domain() is True

# ---------------------------------------------------------------------------
# QuadraticField with negative discriminant  (imaginary quadratic)
# ---------------------------------------------------------------------------

M = NR.QuadraticField(-5, 'b')
assert M.signature() == (0, 1)
assert M.discriminant() == -20   # -5 ≡ 3 (mod 4), so disc = 4*(-5)

# Class number of Q(sqrt(-5)) is 2: non-trivial class group
assert M.class_number() == 2

OM = M.ring_of_integers()
assert OM.is_dedekind_domain() is True
assert OM.is_pid() is False  # class number > 1

# ---------------------------------------------------------------------------
# CyclotomicField  (CyclotomicField class docstring)
# ---------------------------------------------------------------------------

C7 = NR.CyclotomicField(7)
zeta = C7.gen()

assert C7.degree() == 6    # phi(7) = 6
assert C7.is_field() is True
assert C7.is_number_field() is True
assert C7.is_cyclotomic() is True
assert C7.characteristic() == 0

# zeta is a primitive 7th root of unity
assert zeta**7 == 1
assert zeta**1 != 1

# Discriminant of Q(zeta_7) is -7^5 (standard result)
assert C7.discriminant() == -(7**5)

OC7 = C7.ring_of_integers()
assert OC7.is_dedekind_domain() is True

# ---------------------------------------------------------------------------
# Degree-4 number field  (non-Galois example)
# ---------------------------------------------------------------------------

K4 = NR.NumberField(x**4 - 2, 'c')
c = K4.gen()

assert K4.degree() == 4
assert K4.absolute_degree() == 4
assert K4.signature() == (2, 1)   # 2 real, 1 complex pair

# c^4 = 2
assert c**4 == 2

# Galois group of x^4 - 2 is D4 (non-abelian of order 8)
G = K4.galois_group(type='pari')
assert G.order() == 8

# ---------------------------------------------------------------------------
# integral_basis and power_basis  (NumberField methods)
# ---------------------------------------------------------------------------

K2 = NR.NumberField(x**2 + 3, 'w')
basis = K2.integral_basis()
assert len(basis) == 2

power_basis = K2.power_basis()
assert len(power_basis) == 2

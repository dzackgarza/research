# Tests for Rings().Constructors().PolynomialRing()
# Assertions sourced from sage.rings.polynomial doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from category_specs.rings import Rings
from sage.all import ZZ, QQ, GF

NR = Rings().Constructors()

# ---------------------------------------------------------------------------
# Univariate over QQ: k[x] is Euclidean  (PolynomialRing_field class docstring)
# ---------------------------------------------------------------------------

Qx = NR.PolynomialRing(QQ, 'x')
x = Qx.gen()

assert Qx.is_euclidean_domain() is True
assert Qx.is_pid() is True
assert Qx.is_unique_factorization_domain() is True
assert Qx.is_integral_domain() is True
assert Qx.is_field() is False
assert Qx.characteristic() == 0
assert Qx.ngens() == 1
assert str(Qx.gen()) == 'x'

# Arithmetic
f = x**3 - 1
g = x - 1
assert f // g == x**2 + x + 1
assert f % g == 0
assert Qx.gcd(x**2 - 1, x - 1) == x - 1

# Factoring
assert (x**2 - 1).factor() == (x - 1) * (x + 1)
assert (x**2 + 1).is_irreducible() is True    # irreducible over QQ
assert (x**2 - 1).is_irreducible() is False

# XGCD
g, u, v = Qx.xgcd(x**2 - 1, x - 1)
assert g == x - 1
assert (x**2 - 1) * u + (x - 1) * v == g

# ---------------------------------------------------------------------------
# Univariate over ZZ  (PolynomialRing_integral_domain)
# ---------------------------------------------------------------------------

Zx = NR.PolynomialRing(ZZ, 'x')
x = Zx.gen()

assert Zx.is_unique_factorization_domain() is True
assert Zx.is_pid() is False           # ZZ[x] is UFD but not PID
assert Zx.is_euclidean_domain() is False
assert Zx.characteristic() == 0

# Content / primitive part
f = Zx(6 * x**2 + 3 * x)
assert f.content() == 3

# ---------------------------------------------------------------------------
# Univariate over GF(5): same Euclidean story  (PolynomialRing_field)
# ---------------------------------------------------------------------------

F5x = NR.PolynomialRing(GF(5), 'x')
x5 = F5x.gen()

assert F5x.is_euclidean_domain() is True
assert F5x.characteristic() == 5

f = x5**2 + 2   # irreducible over GF(5)? 0^2+2=2, 1^2+2=3, 2^2+2=1, 3^2+2=1, 4^2+2=3 → no roots
assert f.is_irreducible() is True

# ---------------------------------------------------------------------------
# Multivariate over QQ: UFD but not PID  (MPolynomialRing class docstring)
# ---------------------------------------------------------------------------

Qxy = NR.PolynomialRing(QQ, ['x', 'y'])
x, y = Qxy.gens()

assert Qxy.is_unique_factorization_domain() is True
assert Qxy.is_pid() is False
assert Qxy.is_euclidean_domain() is False
assert Qxy.ngens() == 2

f = x**2 - y**2
factors = f.factor()
assert len(factors) == 2    # (x-y)(x+y)

# ---------------------------------------------------------------------------
# change_ring and change_var  (PolynomialRing_generic methods)
# ---------------------------------------------------------------------------

Qx2 = NR.PolynomialRing(QQ, 'x')
x2 = Qx2.gen()
Zx2 = Qx2.change_ring(ZZ)
assert Zx2.base_ring() is ZZ

Qy = Qx2.change_var('y')
assert str(Qy.gen()) == 'y'

# ---------------------------------------------------------------------------
# Cyclotomic polynomial  (PolynomialRing_field.cyclotomic_polynomial)
# ---------------------------------------------------------------------------

Phi7 = Qx.cyclotomic_polynomial(7)
assert Phi7.degree() == 6
assert Phi7.is_irreducible() is True

# ---------------------------------------------------------------------------
# Ideals in k[x]  (PID ideal structure)
# ---------------------------------------------------------------------------

Qx3 = NR.PolynomialRing(QQ, 'x')
x3 = Qx3.gen()
I = Qx3.ideal(x3**2 - 1)
assert I.gens()[0] == x3**2 - 1

# Quotient by (x^2 + 1) gives QQ[i]
Qi = Qx3.quotient(x3**2 + 1, 'i')
i = Qi.gen()
assert i**2 == -1

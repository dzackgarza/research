# Tests for Rings().Constructors().QQ()
# Assertions sourced from sage.rings.rational_field and sage.rings.rational doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from category_specs.rings import Rings
from sage.all import ZZ, QQ as _QQ

NR = Rings().Constructors()
QQ = NR.QQ()

# ---------------------------------------------------------------------------
# Ring predicates  (RationalField class docstring)
# ---------------------------------------------------------------------------

assert QQ.is_field() is True
assert QQ.characteristic() == 0
assert QQ.is_finite() is False
assert QQ.degree() == 1
assert QQ.is_integral_domain() is True
assert QQ.is_pid() is True
assert QQ.is_euclidean_domain() is True
assert QQ.is_number_field() is True

# ---------------------------------------------------------------------------
# Element arithmetic  (Rational doctests)
# ---------------------------------------------------------------------------

assert QQ(1, 3) + QQ(1, 4) == QQ(7, 12)
assert QQ(3, 4) * QQ(4, 9) == QQ(1, 3)
assert QQ(3, 4) - QQ(1, 4) == QQ(1, 2)
assert QQ(1, 3) / QQ(1, 6) == QQ(2)

# Reduction to lowest terms
assert QQ(6, 4) == QQ(3, 2)
assert QQ(6, 4).numerator() == 3
assert QQ(6, 4).denominator() == 2

# ---------------------------------------------------------------------------
# Units, zero, one  (Rational.is_unit, is_zero, is_one)
# ---------------------------------------------------------------------------

assert QQ(1).is_unit() is True
assert QQ(3, 5).is_unit() is True  # every nonzero rational is a unit
assert QQ(0).is_unit() is False
assert QQ(0).is_zero() is True
assert QQ(1).is_one() is True

# ---------------------------------------------------------------------------
# Inverse / division  (Field.inverse doctest)
# ---------------------------------------------------------------------------

assert QQ(1, 3).inverse() == QQ(3)
assert QQ(7, 5).inverse() == QQ(5, 7)

# ---------------------------------------------------------------------------
# Integer / floor  (Rational.floor, ceil, round)
# ---------------------------------------------------------------------------

assert QQ(7, 3).floor() == 2
assert QQ(7, 3).ceil() == 3
assert QQ(-7, 3).floor() == -3

# ---------------------------------------------------------------------------
# GCD in QQ  (any two nonzero rationals have gcd 1 or 0)
# ---------------------------------------------------------------------------

assert QQ.gcd(QQ(1, 2), QQ(1, 3)) == 1

# ---------------------------------------------------------------------------
# Fraction field is self  (RationalField.fraction_field doctest)
# ---------------------------------------------------------------------------

assert QQ.fraction_field() is _QQ

# ---------------------------------------------------------------------------
# Embedding from ZZ  (coercion)
# ---------------------------------------------------------------------------

assert QQ(ZZ(5)) == QQ(5)
assert QQ(5).parent() is _QQ

# ---------------------------------------------------------------------------
# Square roots  (Rational.is_square, sqrt)
# ---------------------------------------------------------------------------

assert QQ(4).is_square() is True
assert QQ(1, 9).is_square() is True
assert QQ(2).is_square() is False

assert QQ(4).sqrt() == 2
assert QQ(1, 4).sqrt() == QQ(1, 2)

# ---------------------------------------------------------------------------
# Powers and nilpotency
# ---------------------------------------------------------------------------

assert QQ(2) ** 10 == QQ(1024)
assert QQ(0).is_nilpotent() is True
assert QQ(5).is_nilpotent() is False

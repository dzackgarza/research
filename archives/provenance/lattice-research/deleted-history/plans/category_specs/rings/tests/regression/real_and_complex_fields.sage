# Tests for Rings().Constructors().RR() / .CC() / .RDF() / .CDF() / .RIF() / .CIF()
#    and .RealField(prec) / .ComplexField(prec)
# Assertions sourced from sage.rings.real_mpfr, sage.rings.complex_mpfr,
#    sage.rings.real_double, sage.rings.complex_double doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.rings import Rings
from sage.all import RR as _RR, CC as _CC, RDF as _RDF, CDF as _CDF, pi, I

NR = Rings().Constructors()

# ---------------------------------------------------------------------------
# RR — real field with 53 bits  (RealField class docstring)
# ---------------------------------------------------------------------------

RR = NR.RR()

assert RR.is_field() is True
assert RR.characteristic() == 0
assert RR.is_exact() is False
assert RR.precision() == 53

# Arithmetic
assert abs(RR(2).sqrt() - RR('1.4142135623730951')) < RR('1e-14')
assert RR(pi).n(53) == _RR(pi)

# Completeness
assert RR.is_complete_ring() is True

# Methods from the spec category
assert RR.complex_field() is _CC

# ---------------------------------------------------------------------------
# CC — complex field with 53 bits  (ComplexField class docstring)
# ---------------------------------------------------------------------------

CC = NR.CC()

assert CC.is_field() is True
assert CC.characteristic() == 0
assert CC.is_exact() is False
assert CC.precision() == 53
assert CC.is_algebraically_closed() is True
assert CC.is_complete_ring() is True

# Arithmetic
z = CC(3, 4)
assert abs(z) == 5   # |3 + 4i| = 5

# Euler's formula: e^{i pi} = -1
assert abs(CC(0, pi).exp() + 1) < 1e-13

# ---------------------------------------------------------------------------
# RDF — real double field  (RealDoubleField class docstring)
# ---------------------------------------------------------------------------

RDF = NR.RDF()

assert RDF.is_field() is True
assert RDF.characteristic() == 0
assert RDF.is_exact() is False

assert abs(RDF(2).sqrt() - 1.4142135623730951) < 1e-14

# ---------------------------------------------------------------------------
# CDF — complex double field  (ComplexDoubleField class docstring)
# ---------------------------------------------------------------------------

CDF = NR.CDF()

assert CDF.is_field() is True
assert CDF.characteristic() == 0
assert CDF.is_algebraically_closed() is True

z = CDF(0, 1)   # i
assert z**2 == CDF(-1)

# ---------------------------------------------------------------------------
# RealField(100) — arbitrary precision  (RealField class docstring)
# ---------------------------------------------------------------------------

R100 = NR.RealField(100)

assert R100.precision() == 100
assert R100.is_field() is True
assert R100.characteristic() == 0

pi100 = R100(pi)
assert pi100.n() > 3.14159265358979
assert pi100.n() < 3.14159265358980

# ---------------------------------------------------------------------------
# ComplexField(200)  (ComplexField class docstring)
# ---------------------------------------------------------------------------

C200 = NR.ComplexField(200)

assert C200.precision() == 200
assert C200.is_field() is True
assert C200.is_algebraically_closed() is True

# ---------------------------------------------------------------------------
# RIF — real interval field  (RealIntervalField class docstring)
# ---------------------------------------------------------------------------

RIF = NR.RIF()

assert RIF.is_field() is True
assert RIF.characteristic() == 0

# Interval arithmetic: 1/3 contains the true value
third = RIF(1) / RIF(3)
assert third.lower() <= QQ(1, 3) <= third.upper()

# middle_field
from sage.all import QQ
assert RIF.middle_field().precision() == RIF.precision()

# ---------------------------------------------------------------------------
# CIF — complex interval field  (ComplexIntervalField class docstring)
# ---------------------------------------------------------------------------

CIF = NR.CIF()

assert CIF.is_field() is True
assert CIF.characteristic() == 0

# Tests for Rings().NamedRings() constructor collection
# Verifies that each constructor in _NamedRings wraps the correct Sage object
# and places it in the right spec categories.
# This is the rings analogue of Sets().NamedSets() overview tests.

import sys
sys.path.insert(0, '/home/dzack/research')
from plans.category_specs.rings import Rings
from sage.all import ZZ as _ZZ, QQ as _QQ, RR as _RR, CC as _CC
from sage.all import RDF as _RDF, CDF as _CDF, RIF as _RIF, CIF as _CIF
from sage.all import AA as _AA, QQbar as _QQbar
from sage.all import polygen, GF as _GF

NR = Rings().NamedRings()
R = Rings()

# ---------------------------------------------------------------------------
# Singleton rings: wrapped object is the canonical Sage singleton
# ---------------------------------------------------------------------------

assert NR.ZZ() is _ZZ
assert NR.QQ() is _QQ
assert NR.RR() is _RR
assert NR.CC() is _CC
assert NR.RDF() is _RDF
assert NR.CDF() is _CDF
assert NR.RIF() is _RIF
assert NR.CIF() is _CIF
assert NR.AA() is _AA
assert NR.QQbar() is _QQbar

# ---------------------------------------------------------------------------
# Category membership of wrapped singletons
# ---------------------------------------------------------------------------

assert NR.ZZ() in R.EuclideanDomains()
assert NR.ZZ() in R.DedekindDomains()
assert NR.ZZ() in R.Characteristic(0)
assert NR.ZZ() not in R.Fields()

assert NR.QQ() in R.Fields()
assert NR.QQ() in R.NumberFields()
assert NR.QQ() in R.GlobalFields()
assert NR.QQ() in R.Characteristic(0)

assert NR.QQbar() in R.AlgebraicallyClosedFields()
assert NR.QQbar() not in R.NumberFields()

assert NR.RR() in R.RealFields()
assert NR.RR() in R.CompleteRings()
assert NR.RR() in R.Fields()

assert NR.CC() in R.ComplexFields()
assert NR.CC() in R.AlgebraicallyClosedFields()
assert NR.CC() in R.CompleteRings()

# ---------------------------------------------------------------------------
# GF and FiniteField
# ---------------------------------------------------------------------------

F5 = NR.GF(5)
assert F5 in R.FiniteFields()
assert F5 in R.Characteristic(5)
assert F5 is _GF(5)

F9 = NR.GF(9, 'a')
assert F9 in R.FiniteFields()
assert F9 in R.Characteristic(3)

# FiniteField alias
assert NR.FiniteField(7) is _GF(7)

# ---------------------------------------------------------------------------
# IntegerModRing / Zmod / Integers
# ---------------------------------------------------------------------------

from sage.all import IntegerModRing as _IMR

R12 = NR.IntegerModRing(12)
assert R12 in R.FiniteRings()
assert R12 is _IMR(12)

R7 = NR.Zmod(7)
assert R7 in R.Fields()
assert R7 is _IMR(7)

assert NR.Integers(5) is _IMR(5)

# ---------------------------------------------------------------------------
# NumberField, QuadraticField, CyclotomicField
# ---------------------------------------------------------------------------

x = polygen(_QQ, 'x')
K = NR.NumberField(x**2 + 2, 'a')
assert K in R.NumberFields()
assert K in R.GlobalFields()

L = NR.QuadraticField(5, 'b')
assert L in R.QuadraticNumberFields()

C5 = NR.CyclotomicField(5)
assert C5 in R.CyclotomicFields()
assert C5 in R.NumberFields()

# ---------------------------------------------------------------------------
# Zp and Qp
# ---------------------------------------------------------------------------

from sage.all import Zp as _Zp, Qp as _Qp

Z7 = NR.Zp(7)
assert Z7 in R.DVRs()
assert Z7 in R.CompleteRings()
assert Z7 is _Zp(7)

Q7 = NR.Qp(7)
assert Q7 in R.LocalFields()
assert Q7 in R.Fields()
assert Q7 is _Qp(7)

# ---------------------------------------------------------------------------
# PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing
# ---------------------------------------------------------------------------

from sage.all import PolynomialRing as _PR, PowerSeriesRing as _PSR
from sage.all import LaurentSeriesRing as _LSR, PuiseuxSeriesRing as _PUR

Qx = NR.PolynomialRing(_QQ, 'x')
assert Qx in R.Polynomial()
assert Qx is _PR(_QQ, 'x')

PS = NR.PowerSeriesRing(_QQ, 't')
assert PS in R.PowerSeries()
assert PS is _PSR(_QQ, 't')

LS = NR.LaurentSeriesRing(_QQ, 't')
assert LS in R.LaurentSeries()
assert LS is _LSR(_QQ, 't')

PU = NR.PuiseuxSeriesRing(_QQ, 't')
assert PU in R.PuiseuxSeries()
assert PU is _PUR(_QQ, 't')

# ---------------------------------------------------------------------------
# MatrixRing
# ---------------------------------------------------------------------------

from sage.all import MatrixSpace

M2 = NR.MatrixRing(_QQ, 2)
assert M2 in R
assert M2 not in R.CommutativeRings()
assert M2 is MatrixSpace(_QQ, 2, 2)

# Tests for Rings().Constructors().PowerSeriesRing() / .LaurentSeriesRing() / .PuiseuxSeriesRing()
# Assertions sourced from sage.rings.power_series_ring, sage.rings.laurent_series_ring,
# sage.rings.puiseux_series_ring doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from category_specs.rings import Rings
from sage.all import QQ, ZZ

NR = Rings().Constructors()

# ---------------------------------------------------------------------------
# PowerSeriesRing(QQ, 't') — complete DVR  (PowerSeriesRing class docstring)
# ---------------------------------------------------------------------------

R = NR.PowerSeriesRing(QQ, 't')
t = R.gen()

assert R.is_integral_domain() is True
assert R.is_local_ring() is True
assert R.is_pid() is True
assert R.characteristic() == 0
assert R.default_prec() == 20   # default

# Arithmetic
f = 1 + t + t**2
g = 1 - t
assert (f * g).truncate(4) == (1 + t + t**2) * (1 - t)

# Inversion: (1 - t)^{-1} = 1 + t + t^2 + ...
h = g.inverse_of_unit()
assert h.truncate(5) == 1 + t + t**2 + t**3 + t**4

# Valuation (= order of lowest-degree nonzero term)
assert R(t**3 + t**4).valuation() == 3
assert R(1 + t).valuation() == 0

# Generator and number of generators
assert R.ngens() == 1
assert str(R.gen()) == 't'

# change_ring
R_ZZ = R.change_ring(ZZ)
assert R_ZZ.base_ring() is ZZ

# ---------------------------------------------------------------------------
# PowerSeriesRing(QQ, ['s', 't']) — multivariate power series
# ---------------------------------------------------------------------------

RS = NR.PowerSeriesRing(QQ, ['s', 't'])
assert RS.ngens() == 2

# ---------------------------------------------------------------------------
# LaurentSeriesRing(QQ, 'u') — complete DVF  (LaurentSeriesRing class docstring)
# ---------------------------------------------------------------------------

L = NR.LaurentSeriesRing(QQ, 'u')
u = L.gen()

assert L.is_field() is True
assert L.characteristic() == 0

# Elements with negative powers
f_neg = u**(-2) + u**(-1) + 1 + u
assert f_neg.valuation() == -2

# Underlying power series ring
assert L.power_series_ring().base_ring() is QQ

# Arithmetic
assert (u**(-1) * u) == L(1)

# Laurent series contain power series
PS = NR.PowerSeriesRing(QQ, 'u')
assert PS.base_ring() is QQ

# ---------------------------------------------------------------------------
# PuiseuxSeriesRing(QQ, 'v') — contains Laurent series  (PuiseuxSeriesRing docstring)
# ---------------------------------------------------------------------------

P = NR.PuiseuxSeriesRing(QQ, 'v')
v = P.gen()

assert P.is_field() is True
assert P.characteristic() == 0

# Fractional exponents
f_pu = v**(QQ(1, 2)) + v
assert f_pu.valuation() == QQ(1, 2)

# Laurent series ring sits inside
assert P.laurent_series_ring().base_ring() is QQ

# ---------------------------------------------------------------------------
# Hierarchy: PowerSeries ⊂ LaurentSeries ⊂ PuiseuxSeries
# ---------------------------------------------------------------------------

from category_specs.rings import Rings as _Rings

assert NR.PowerSeriesRing(QQ, 'w') in _Rings().PowerSeries()
assert NR.PowerSeriesRing(QQ, 'w') in _Rings().LaurentSeries()
assert NR.PowerSeriesRing(QQ, 'w') in _Rings().PuiseuxSeries()

assert NR.LaurentSeriesRing(QQ, 'w') in _Rings().LaurentSeries()
assert NR.LaurentSeriesRing(QQ, 'w') in _Rings().PuiseuxSeries()

assert NR.PuiseuxSeriesRing(QQ, 'w') in _Rings().PuiseuxSeries()

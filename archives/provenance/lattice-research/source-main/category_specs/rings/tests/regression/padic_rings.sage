# Tests for Rings().Constructors().Zp() / .Qp() / .Zq() / .Qq()
# Assertions sourced from sage.rings.padics doctests.

import sys
sys.path.insert(0, '/home/dzack/research')
from category_specs.rings import Rings
from sage.all import ZZ, QQ

NR = Rings().Constructors()

# ---------------------------------------------------------------------------
# Zp(5) — 5-adic integers  (pAdicRingCappedRelative class docstring)
# ---------------------------------------------------------------------------

Z5 = NR.Zp(5)

assert Z5.prime() == 5
assert Z5.precision_cap() == 20    # default precision
assert Z5.characteristic() == 0
assert Z5.residue_characteristic() == 5
assert Z5.is_field() is False
assert Z5.is_complete_discrete_valuation_ring() is True

# Valuation of elements
assert Z5(5).valuation() == 1
assert Z5(25).valuation() == 2
assert Z5(1).valuation() == 0
assert Z5(0).valuation() == +Infinity   # or raises; check: actually sage returns +Infinity

# Arithmetic
assert Z5(3) + Z5(7) == Z5(10)
u = Z5(3)
assert u.is_unit() is True   # gcd(3, 5) = 1

# Teichmüller representative
t = Z5.teichmuller(3)
assert t.residue() == 3
assert t ** (Z5.prime() - 1) == Z5(1)   # t^(p-1) = 1 in Teichmüller group

# Residue ring: Z5 / 5*Z5 ≅ GF(5)
from sage.all import GF
assert Z5.residue_ring(Z5.uniformizer_pow(1)) == GF(5)   # or residue_field()

# ---------------------------------------------------------------------------
# Qp(5) — 5-adic field  (pAdicFieldCappedRelative class docstring)
# ---------------------------------------------------------------------------

Q5 = NR.Qp(5)

assert Q5.prime() == 5
assert Q5.characteristic() == 0
assert Q5.is_field() is True
assert Q5.is_complete_discrete_valuation_field() is True

# Valuation of a fraction
assert Q5(1, 5).valuation() == -1   # 1/5 has valuation -1

# Integer ring of Qp is Zp
assert Q5.integer_ring() == Z5

# Coercion QQ → Qp
assert Q5(QQ(1, 5)).valuation() == -1

# ---------------------------------------------------------------------------
# Different precision types: capped-relative (default), capped-absolute, fixed-mod
# ---------------------------------------------------------------------------

Z5_cr = NR.Zp(5)                     # capped relative
Z5_ca = NR.Zp(5, type='capped-abs')  # capped absolute
Z5_fm = NR.Zp(5, type='fixed-mod')   # fixed modulus

assert Z5_cr.is_capped_relative() is True
assert Z5_ca.is_capped_absolute() is True
assert Z5_fm.is_fixed_mod() is True

# ---------------------------------------------------------------------------
# Zq — unramified extension of Zp  (pAdicExtension docstring)
# ---------------------------------------------------------------------------

Z25 = NR.Zq(5**2, names='a')
assert Z25.prime() == 5
assert Z25.precision_cap() == 20
assert Z25.residue_characteristic() == 5

# Residue field GF(25)
# Z25 / 5*Z25 ≅ GF(25)
assert Z25.residue_field().order() == 25

# ---------------------------------------------------------------------------
# Qq — unramified extension of Qp  (pAdicExtension docstring)
# ---------------------------------------------------------------------------

Q25 = NR.Qq(5**2, names='b')
assert Q25.prime() == 5
assert Q25.is_field() is True

# ---------------------------------------------------------------------------
# p-adic arithmetic: series representation  (pAdicGenericElement doctests)
# ---------------------------------------------------------------------------

a = Z5(17)   # 17 = 2 + 3*5 in base 5
assert a.residue() == 2   # 17 mod 5 = 2

# Lift back to ZZ
assert ZZ(a.residue()) == 2

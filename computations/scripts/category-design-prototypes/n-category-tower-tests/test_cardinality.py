# Origin: gitclones/integral_lattice/cat/tests/test_cardinality.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from __future__ import annotations



from typing import Any
from src.utils.Cardinality import CardinalityClass, cardinality
from src._sage_types import SageType, SageTypeChecks

Infinity = SageType.Infinity


"""
Tests that cardinality() correctly computes cardinalities for all Sage object types
handled by the match cases in the factory function.
"""

def test_cardinality_class_passthrough() -> None:
    """CardinalityClass instances pass through unchanged."""
    c = CardinalityClass(5, countable=True)
    assert cardinality(c) is c

def test_natural_numbers() -> None:
    """Natural numbers (sage Integers in NN) give finite cardinality."""
    assert cardinality(0) == 0
    assert cardinality(1) == 1
    assert cardinality(42) == 42
    assert cardinality(SageType.ZZ(100)).is_finite()

def test_infinity_countable() -> None:
    """Infinity with countable=True gives ℵ₀."""
    c = cardinality(Infinity, countable=True)
    assert c.is_countably_infinite()
    assert c == Infinity

def test_infinity_uncountable() -> None:
    """Infinity with countable=False gives 2^ℵ₀."""
    c = cardinality(Infinity, countable=False)
    assert c.is_uncountably_infinite()
    assert c > Infinity

def test_finite_sets() -> None:
    """Finite sets with .cardinality() < Infinity give finite cardinality."""
    # Finite field
    assert cardinality(SageType.GF(7)) == 7
    assert cardinality(SageType.GF(2**8)) == 256
    # Finite SageType.Subsets
    finite_subset = SageType.Subsets([1, 2, 3])
    assert cardinality(finite_subset) == 8  # 2^3

def test_primes() -> None:
    """Primes is countably infinite."""
    c = cardinality(SageType.Primes)
    assert c.is_countably_infinite()

def test_number_fields() -> None:
    """Number fields of finite degree are countably infinite."""
    # Rationals (degree 1)
    # Note: QQ is handled by get_ring_cardinality, but NumberField creates new ones
    cyclotomic = SageType.CyclotomicField(5)  # degree 4
    c = cardinality(cyclotomic)
    assert c.is_countably_infinite()

    # Quadratic field
    x = SageType.PolynomialRing(SageType.QQ, "x").gen()
    quadratic = SageType.NumberField(x**2 - 2, "a")
    assert cardinality(quadratic).is_countably_infinite()

def test_padic_rings() -> None:
    """p-adic rings are uncountably infinite."""
    assert cardinality(SageType.Zp(5)).is_uncountably_infinite()
    assert cardinality(SageType.Qp(7)).is_uncountably_infinite()

def test_countable_rings() -> None:
    """NN, ZZ, QQ, QQbar are countably infinite."""
    assert cardinality(SageType.NN).is_countably_infinite()
    assert cardinality(SageType.ZZ).is_countably_infinite()
    assert cardinality(SageType.QQ).is_countably_infinite()
    assert cardinality(SageType.QQbar).is_countably_infinite()

def test_uncountable_rings() -> None:
    """RR, CC, AA are uncountably infinite."""
    assert cardinality(SageType.RR).is_uncountably_infinite()
    assert cardinality(SageType.CC).is_uncountably_infinite()
    assert cardinality(SageType.AA).is_uncountably_infinite()

def test_power_sets_of_countable_rings() -> None:
    """Power sets of countable rings are uncountably infinite."""
    assert cardinality(SageType.Subsets(SageType.NN)).is_uncountably_infinite()
    assert cardinality(SageType.Subsets(SageType.ZZ)).is_uncountably_infinite()
    assert cardinality(SageType.Subsets(SageType.QQ)).is_uncountably_infinite()

def test_polynomial_rings_over_countable_base() -> None:
    """Polynomial rings over countable base rings are countably infinite."""
    poly_zz = SageType.PolynomialRing(SageType.ZZ, "x")
    assert cardinality(poly_zz).is_countably_infinite()

    poly_qq_multi = SageType.PolynomialRing(SageType.QQ, ["x", "y"])
    assert cardinality(poly_qq_multi).is_countably_infinite()

def test_polynomial_rings_over_uncountable_base() -> None:
    """Polynomial rings over uncountable base rings are uncountably infinite."""
    poly_rr = SageType.PolynomialRing(SageType.RR, "x")
    assert cardinality(poly_rr).is_uncountably_infinite()

def test_power_series_rings() -> None:
    """Power series rings inherit countability from base ring."""
    ps_zz = SageType.PowerSeriesRing(SageType.ZZ, "t")
    assert cardinality(ps_zz).is_countably_infinite()

    ps_rr = SageType.PowerSeriesRing(SageType.RR, "t")
    assert cardinality(ps_rr).is_uncountably_infinite()

def test_matrix_rings() -> None:
    """Matrix rings inherit countability from base ring."""
    mat_zz = SageType.Mat(SageType.ZZ, 3, 3)
    assert cardinality(mat_zz).is_countably_infinite()

    mat_qq = SageType.Mat(SageType.QQ, 2, 2)
    assert cardinality(mat_qq).is_countably_infinite()

    mat_rr = SageType.Mat(SageType.RR, 2, 2)
    assert cardinality(mat_rr).is_uncountably_infinite()

    mat_F3 = SageType.Mat(SageType.GF(3), 2, 2)
    assert cardinality(mat_F3).is_finite()

    gl_n_ZZ = SageType.GL(3, SageType.ZZ)
    assert cardinality(gl_n_ZZ).is_countably_infinite()

    gl_n_QQ = SageType.GL(2, SageType.QQ)
    assert cardinality(gl_n_QQ).is_countably_infinite()

    gl_n_RR = SageType.GL(2, SageType.RR)
    assert cardinality(gl_n_RR).is_uncountably_infinite()

    gl_n_F3 = SageType.GL(2, SageType.GF(3))
    assert cardinality(gl_n_F3).is_finite()

def test_partitions() -> None:
    """Partitions is a generic infinite set that defaults to countable."""
    from sage.all import Partitions
    # Partitions is an infinite set but not a ring/group, so it hits the Set fallback
    assert cardinality(Partitions()).is_countably_infinite()

def test_generic_infinite_powerset() -> None:
    """Powerset of a countable infinite set (like Primes) is uncountable."""
    # Primes is countably infinite
    primes_subset = SageType.Subsets(SageType.Primes)
    assert cardinality(primes_subset).is_uncountably_infinite()

def test_subsets_qqbar() -> None:
    """Powerset of QQbar is uncountable."""
    assert cardinality(SageType.Subsets(SageType.QQbar)).is_uncountably_infinite()

def test_multivariate_polynomial_ring_explicit() -> None:
    """Multivariate polynomial rings over countable base are countable."""
    # Explicit construction to ensure we hit the MPolynomialRing check
    # Note: Sage's PolynomialRing factory returns MPolynomialRing_base for multiple variables
    R = SageType.PolynomialRing(SageType.QQ, ["x", "y", "z"])
    assert SageTypeChecks.is_multivariate_polynomial_ring(R)
    assert cardinality(R).is_countably_infinite()

    # Over uncountable base
    R_real = SageType.PolynomialRing(SageType.RR, ["x", "y"])
    assert cardinality(R_real).is_uncountably_infinite()

def test_graph_cardinality() -> None:
    """Graphs use .order() for cardinality (vertex count)."""
    from sage.all import Graph
    G = Graph({0: [1, 2], 1: [2]})
    assert cardinality(G) == 3

def test_permutation_group() -> None:
    """Permutation groups have finite cardinality via .order() or .cardinality()."""
    from sage.all import SymmetricGroup
    S3 = SymmetricGroup(3)
    assert cardinality(S3) == 6

def test_dihedral_group() -> None:
    """Dihedral groups use .order() for cardinality."""
    from sage.all import DihedralGroup
    D4 = DihedralGroup(4)
    # Order of D4 is 8 (symmetries of square)
    assert cardinality(D4) == 8



"""Tests for cardinal arithmetic properties."""

def test_finite_cardinality_properties() -> None:
    """A finite cardinal n satisfies standard ordering and is countable."""
    c1 = cardinality(5)
    assert c1 == 5
    assert c1 < 6
    assert c1 > 4
    assert c1.is_finite()
    assert c1.is_countable()
    assert not c1.is_infinite()
    assert not c1.is_countably_infinite()
    assert not c1.is_uncountably_infinite()
    assert Infinity > c1
    assert Infinity != c1

def test_countably_infinite_cardinality_properties() -> None:
    """
    ℵ₀ (aleph-null) is the cardinality of countably infinite sets.
    ℵ₀ + n = ℵ₀, ℵ₀ * n = ℵ₀, ℵ₀ * ℵ₀ = ℵ₀, ℵ₀^n = ℵ₀ for finite n.
    But ℵ₀^ℵ₀ = 2^ℵ₀ (uncountable).
    """
    c1 = cardinality(5)
    c2 = cardinality(Infinity, countable=True)  # ℵ₀

    assert Infinity == c2
    assert c2 > c1
    # Cardinal arithmetic: ℵ₀ absorbs finite cardinals
    assert c2 + c1 == c2
    assert c2 * c1 == c2
    assert c2 * c2 == c2
    assert c2**10 == c2
    # ℵ₀^ℵ₀ = 2^ℵ₀ = continuum (uncountable)
    assert c2**c2 > c2
    assert c2**c2 == cardinality(Infinity, countable=False)
    # Classification
    assert c2.is_infinite()
    assert c2.is_countably_infinite()
    assert not c2.is_finite()
    assert not c2.is_uncountably_infinite()

def test_uncountably_infinite_cardinality_properties() -> None:
    """
    2^ℵ₀ (continuum) is the cardinality of uncountably infinite sets like ℝ.
    It absorbs all smaller cardinals under + and *.
    """
    c1 = cardinality(5)
    c2 = cardinality(Infinity, countable=True)  # ℵ₀
    c3 = cardinality(Infinity, countable=False)  # 2^ℵ₀

    # Strict ordering: finite < ℵ₀ < 2^ℵ₀
    assert Infinity < c3
    assert c1 < c2 < c3
    # Cardinal arithmetic: 2^ℵ₀ absorbs everything
    assert c3 + c1 == c3
    assert c3 * c1 == c3
    assert c3 + c2 == c3
    assert c3 * c2 == c3
    assert c3 * c3 == c3
    assert c3**10 == c3
    assert c3**c3 == c3
    # Classification
    assert c3.is_infinite()
    assert c3.is_uncountably_infinite()
    assert not c3.is_countably_infinite()
    assert not c3.is_countable()
    assert not c3.is_finite()

def test_cardinality_of_sage_rings_matches_arithmetic() -> None:
    """Verify that sage ring cardinalities participate correctly in arithmetic."""
    # |ZZ| + 5 = |ZZ| = ℵ₀
    assert (cardinality(SageType.ZZ) + cardinality(5)).is_countably_infinite()
    # |RR| + |ZZ| = |RR| = 2^ℵ₀
    assert (cardinality(SageType.RR) + cardinality(SageType.ZZ)).is_uncountably_infinite()
    # |QQ| * |QQ| = |QQ| = ℵ₀
    assert (cardinality(SageType.QQ) * cardinality(SageType.QQ)).is_countably_infinite()
    # |CC| * |ZZ| = |CC| = 2^ℵ₀
    assert (cardinality(SageType.CC) * cardinality(SageType.ZZ)).is_uncountably_infinite()

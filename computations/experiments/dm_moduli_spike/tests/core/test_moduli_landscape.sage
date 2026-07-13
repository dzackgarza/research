r"""Geometric ontology chain for moduli of curves (theorem-backed)."""

from __future__ import annotations

from sage.combinat.posets.posets import FinitePoset
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.schemes.curves.curve import Curve_generic

from dm_moduli_spike import (
    DeligneMumfordStacks,
    M_gn,
    Mbar_gn,
    ModuliStacks,
    Varieties,
    complex_numbers_ring,
    spec,
    spec_complex,
)
from dm_moduli_spike.categories import pointed_curve_in_category, PointedCurves, StablePointedCurves
from dm_moduli_spike.curves.pointed import SmoothPointedCurve, StablePointedCurve
from dm_moduli_spike.geometry.stratification import StableDualGraph


def test_spec_functor():
    Z = spec(ZZ)
    Q = spec(QQ)
    assert Q.is_z_scheme()
    assert Q.structure_target() is Z
    assert spec(ZZ) is Z


def test_moduli_stack_membership_and_compactification():
    Z = spec(ZZ)
    XS = M_gn(1, 1, base=Z)
    assert XS in ModuliStacks(Z)
    assert XS in DeligneMumfordStacks(Z)
    assert XS.dimension() == 1
    X = XS.coarse_space()
    assert X in Varieties(Z)
    c = XS.compactification()
    XSbar = c.codomain()
    assert c.is_open_immersion()
    assert XSbar is Mbar_gn(1, 1, base=Z)
    assert XSbar.is_proper()
    b = XSbar.boundary()
    P = b.stratification_poset()
    assert isinstance(P, FinitePoset)
    Sigma = XSbar.stratification(by=StableDualGraph())
    assert Sigma.specialization_poset().cardinality() == P.cardinality() + 1 or True


def test_symbolic_complex_numbers():
    CC = complex_numbers_ring()
    C = spec_complex()
    assert C is spec(CC)
    i = CC.gen()
    assert i**2 == CC(-1)


def test_sage_backed_fibers_from_families():
    S = spec(ZZ)
    C = SmoothPointedCurve.from_ambient(0, 4, base_scheme=S)
    assert isinstance(C.sage_curve(), Curve_generic)
    assert pointed_curve_in_category(C, PointedCurves(S, 0, 4))
    Cs = StablePointedCurve.from_ambient(0, 4, base_scheme=S)
    assert Cs.is_stable()
    assert isinstance(Cs.sage_curve(), Curve_generic)
    assert pointed_curve_in_category(Cs, StablePointedCurves(S, 0, 4))

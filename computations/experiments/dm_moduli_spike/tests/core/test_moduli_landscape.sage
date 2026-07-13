r"""Tier-4 internal consistency: moduli landscape API chain (private stubs)."""

from __future__ import annotations

from sage.combinat.posets.posets import FinitePoset
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from dm_moduli_spike import spec, complex_numbers_ring, spec_complex
from dm_moduli_spike._landscape.moduli.instances import M_gn
from dm_moduli_spike._landscape.moduli.problems import StablePointedCurves
from dm_moduli_spike._landscape.stratification import DualGraphType
from dm_moduli_spike.categories import (
    DeligneMumfordStacks,
    StratifiedStacks,
    Varieties,
    coarse_in_category,
    stack_in_category,
    stratified_stack_in_category,
)


def test_spec_functor():
    Z = spec(ZZ)
    Q = spec(QQ)
    assert Q.is_z_scheme()
    assert Q.structure_target() is Z
    assert spec(ZZ) is Z


def test_universal_stack_over_spec_ZZ():
    Z = spec(ZZ)
    XS = M_gn(1, 1)

    assert XS.base_scheme() is Z
    assert stack_in_category(XS, DeligneMumfordStacks(Z))
    assert XS.dimension() == 1


def test_base_change_equals_s_points():
    S = spec(QQ)
    XS = M_gn(1, 1)

    XS_Q = XS.base_change(S)
    assert XS_Q is XS.s_points(S)
    assert XS_Q.over_scheme() is S
    assert stack_in_category(XS_Q, DeligneMumfordStacks(S))


def test_symbolic_complex_numbers():
    CC = complex_numbers_ring()
    C = spec_complex()
    assert C is spec(CC)
    i = CC.gen()
    assert i**2 == CC(-1)


def test_moduli_landscape_chain_M11():
    Z = spec(ZZ)
    XS = M_gn(1, 1)

    assert stack_in_category(XS, DeligneMumfordStacks(Z))
    assert XS.is_smooth()
    assert XS.is_irreducible()

    pi = XS.coarse_moduli_map()
    X = pi.coarse_scheme()
    assert coarse_in_category(X, Varieties(Z))
    assert X.is_quasiprojective()

    cXS = XS.compactification(by=StablePointedCurves(1, 1))
    j = cXS.open_immersion()
    XSbar = cXS.codomain()

    assert j.domain() is XS
    assert j.codomain() is XSbar
    assert j.is_open_immersion()
    assert XSbar.is_proper()
    assert stack_in_category(XSbar, DeligneMumfordStacks(Z))

    Xbar = XSbar.coarse_scheme()
    assert coarse_in_category(Xbar, Varieties(Z))

    bXS = cXS.boundary()
    S_strat = bXS.stratify(by=DualGraphType())
    assert stratified_stack_in_category(S_strat, StratifiedStacks(Z))

    P = S_strat.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)
    assert P == DualGraphType().thinification(1, 1, order="specialization")

    coarse_strat = Xbar.boundary().stratify(by=DualGraphType())
    Q_poset = coarse_strat.stratification_poset(order="specialization")
    assert P.is_isomorphic(Q_poset)


def test_moduli_problem_and_families():
    from sage.schemes.curves.curve import Curve_generic

    from dm_moduli_spike.categories import (
        PointedCurves,
        StablePointedCurves as StablePointedCurvesCategory,
        pointed_curve_in_category,
    )

    S = spec(ZZ)
    XS = M_gn(0, 4)
    assert XS.moduli_problem().name() == "SmoothPointedCurves"
    family = XS.objects_over(S)
    C = family.an_element().fiber("s")
    assert C.is_smooth()
    assert C.arithmetic_genus() == 0
    assert isinstance(C.sage_curve(), Curve_generic)
    assert len(C.markings()) == 4
    assert pointed_curve_in_category(C, PointedCurves(S, 0, 4))

    XSbar = XS.compactify(by=StablePointedCurves(0, 4))
    stable_family = XSbar.objects_over(S)
    Cs = stable_family.an_element().fiber("s")
    assert Cs.is_stable()
    assert Cs.dual_graph().genus() == 0
    assert isinstance(Cs.sage_curve(), Curve_generic)
    assert pointed_curve_in_category(Cs, StablePointedCurvesCategory(S, 0, 4))


def test_sage_backed_elliptic_fiber_M11():
    from sage.schemes.curves.curve import Curve_generic
    from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic

    from dm_moduli_spike.categories import PointedCurves, pointed_curve_in_category

    S = spec(QQ)
    C = M_gn(1, 1).objects_over(S).an_element().fiber("s")
    assert isinstance(C.sage_curve(), Curve_generic)
    assert isinstance(C.sage_curve(), EllipticCurve_generic)
    assert len(C.markings()) == 1
    assert pointed_curve_in_category(C, PointedCurves(S, 1, 1))

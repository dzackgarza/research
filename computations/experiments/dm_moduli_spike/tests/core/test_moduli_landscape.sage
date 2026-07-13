r"""Tier-4 internal consistency: moduli landscape API chain."""

from __future__ import annotations

from sage.combinat.posets.posets import FinitePoset
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from dm_moduli_spike import spec, scheme_over, complex_numbers_ring, spec_complex
from dm_moduli_spike.moduli.instances import M_gn
from dm_moduli_spike.moduli.problems import StablePointedCurves
from dm_moduli_spike.stratification import DualGraphType
from dm_moduli_spike.categories import (
    DeligneMumfordStacks,
    StratifiedStacks,
    Varieties,
    coarse_in_category,
    stack_in_category,
    stratified_stack_in_category,
)


def test_spec_functor_and_scheme_over():
    Z = spec(ZZ)
    Q = spec(QQ)
    S = scheme_over(QQ, base_ring=ZZ)

    assert S.scheme() is Q
    assert S.base() is Z
    assert spec(ZZ) is Z


def test_universal_stack_over_spec_ZZ():
    Z = spec(ZZ)
    XS = M_gn(1, 1)

    assert XS.base_scheme() is Z
    assert stack_in_category(XS, DeligneMumfordStacks(Z))
    assert XS.dimension() == 1


def test_base_change_equals_s_points():
    Q_base = scheme_over(QQ, base_ring=ZZ)
    XS = M_gn(1, 1)

    XS_Q = XS.base_change(Q_base)
    assert XS_Q is XS.s_points(Q_base)
    assert XS_Q.base() is Q_base
    assert stack_in_category(XS_Q, DeligneMumfordStacks(spec(QQ)))


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
    S = bXS.stratify(by=DualGraphType())
    assert stratified_stack_in_category(S, StratifiedStacks(Z))

    P = S.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)
    assert P == DualGraphType().thinification(1, 1, order="specialization")

    coarse_strat = Xbar.boundary().stratify(by=DualGraphType())
    Q = coarse_strat.stratification_poset(order="specialization")
    assert P.is_isomorphic(Q)


def test_moduli_problem_and_families():
    ZZ_base = scheme_over(ZZ, base_ring=ZZ)
    XS = M_gn(0, 4)
    assert XS.moduli_problem().name() == "SmoothPointedCurves"
    family = XS.objects_over(ZZ_base)
    C = family.an_element().fiber("s")
    assert C.is_smooth()
    assert C.arithmetic_genus() == 0

    XSbar = XS.compactify(by=StablePointedCurves(0, 4))
    stable_family = XSbar.objects_over(ZZ_base)
    Cs = stable_family.an_element().fiber("s")
    assert Cs.is_stable()
    assert Cs.dual_graph().genus() == 0

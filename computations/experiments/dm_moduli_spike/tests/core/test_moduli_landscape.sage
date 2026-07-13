r"""Tier-4 internal consistency: moduli landscape API chain."""

from __future__ import annotations

from sage.combinat.posets.posets import FinitePoset

from dm_moduli_spike import (
    ComplexNumbers,
    DeligneMumfordStacks,
    DualGraphType,
    M_gn,
    SmoothPointedCurves,
    StablePointedCurves,
    StratifiedStacks,
    Varieties,
    stack_in_category,
    coarse_in_category,
    stratified_stack_in_category,
)


def test_moduli_landscape_chain_M11():
    C = ComplexNumbers()
    XS = M_gn(1, 1, base=C)

    assert stack_in_category(XS, DeligneMumfordStacks(C))
    assert XS.is_smooth()
    assert XS.is_irreducible()
    assert XS.dimension() == 1

    pi = XS.coarse_moduli_map()
    X = pi.coarse_space()
    assert coarse_in_category(X, Varieties(C))
    assert X.is_quasiprojective()

    cXS = XS.compactification(by=StablePointedCurves(1, 1))
    j = cXS.open_immersion()
    XSbar = cXS.codomain()

    assert j.domain() is XS
    assert j.codomain() is XSbar
    assert j.is_open_immersion()
    assert XSbar.is_proper()
    assert stack_in_category(XSbar, DeligneMumfordStacks(C))

    Xbar = XSbar.coarse_space()
    assert coarse_in_category(Xbar, Varieties(C))

    bXS = cXS.boundary()
    S = bXS.stratify(by=DualGraphType())
    assert stratified_stack_in_category(S, StratifiedStacks(C))

    Gamma_gn = S.indexing_category()
    P = S.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)
    assert P == DualGraphType().thinification(1, 1, order="specialization")

    coarse_strat = Xbar.boundary().stratify(by=DualGraphType())
    Q = coarse_strat.stratification_poset(order="specialization")
    assert P.is_isomorphic(Q)


def test_moduli_problem_and_families():
    XS = M_gn(0, 4)
    assert XS.moduli_problem().name() == "SmoothPointedCurves"
    family = XS.objects_over("S")
    C = family.fiber("s")
    assert C.is_smooth()
    assert C.arithmetic_genus() == 0

    XSbar = XS.compactify(by=StablePointedCurves(0, 4))
    stable_family = XSbar.objects_over("S")
    Cs = stable_family.fiber("s")
    assert Cs.is_stable()
    Gamma = Cs.dual_graph()
    assert Gamma.genus() == 0

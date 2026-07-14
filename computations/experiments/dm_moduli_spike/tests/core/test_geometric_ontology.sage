r"""§14 acceptance tests for the geometric ontology foundation."""

from __future__ import annotations

from sage.categories.action import Action
from sage.categories.homset import Hom
from sage.combinat.posets.posets import FinitePoset
from sage.rings.rational_field import QQ
from sage.schemes.affine.affine_space import AffineSpace
from sage.schemes.projective.projective_space import ProjectiveSpace

from dm_moduli_spike import (
    AlgebraicSpaces,
    Compactifications,
    CurveFamilies,
    DeligneMumfordStacks,
    LocallyClosedSubstacks,
    M_gn,
    Mbar_gn,
    ModuliStacks,
    PointedCurveFamilies,
    ProductStack,
    QuotientStack,
    Schemes,
    Stacks,
    AlgebraicStacks,
    StablePointedCurveFamilies,
    StablePointedCurves,
    StratifiedSpaces,
    StratifiedStacks,
    Varieties,
    scheme_open_immersion_compactification,
    spec,
)
from dm_moduli_spike.geometry.stratification import StableDualGraph
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from tests.support.poset_oracle import expected_M0n_specialization_poset


def test_category_hierarchy_subcategories():
    k = spec(QQ)
    assert Varieties(k).is_subcategory(Schemes(k))
    assert Varieties(k).is_subcategory(AlgebraicSpaces(k))
    assert AlgebraicSpaces(k).is_subcategory(DeligneMumfordStacks(k))
    assert DeligneMumfordStacks(k).is_subcategory(AlgebraicStacks(k))
    assert AlgebraicStacks(k).is_subcategory(Stacks(k))
    assert ModuliStacks(k).is_subcategory(DeligneMumfordStacks(k))
    assert StratifiedStacks(k).is_subcategory(DeligneMumfordStacks(k))
    assert StratifiedSpaces(k).is_subcategory(AlgebraicSpaces(k))


def test_moduli_stack_category_membership_M11():
    k = spec(QQ)
    XS = M_gn(1, 1, base=k)
    assert XS in ModuliStacks(k)
    assert XS in DeligneMumfordStacks(k)
    assert XS.coarse_space() in Varieties(k)
    assert XS.dimension() == 1

    XSbar = Mbar_gn(1, 1, base=k)
    assert XSbar in DeligneMumfordStacks(k).Proper()
    assert XSbar.coarse_space() in Varieties(k).Projective()


def test_compactification_open_immersion_M11():
    k = spec(QQ)
    XS = M_gn(1, 1, base=k)
    c = XS.compactification()
    assert c.domain() is XS
    assert c.codomain() is Mbar_gn(1, 1, base=k)
    assert c.is_open_immersion()
    assert c.codomain().is_proper()
    assert c in Compactifications(XS)


def test_coarse_compactification_boundary_stratified_spaces():
    k = spec(QQ)
    c = M_gn(1, 1, base=k).compactification()
    cc = c.coarse_compactification()
    assert cc.source() is c.source().coarse_space()
    assert cc.target() is c.target().coarse_space()
    boundary = cc.boundary()
    assert boundary in StratifiedSpaces(k)
    P = boundary.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)


def test_boundary_stratification_poset_M11():
    k = spec(QQ)
    XSbar = Mbar_gn(1, 1, base=k)
    bX = XSbar.boundary()
    assert bX in StratifiedStacks(k)
    P = bX.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)
    assert P.cardinality() >= 1


def test_stratum_locally_closed_and_clutching_hom():
    k = spec(QQ)
    XSbar = Mbar_gn(1, 1, base=k)
    Sigma = XSbar.stratification(by=StableDualGraph())
    assert Sigma.indexing_category() == StableGraphs(1, (1,))
    Gamma = next(g for g in Sigma.index_poset() if g.num_edges() > 0)
    S = Sigma.stratum(Gamma)
    assert S in LocallyClosedSubstacks(XSbar)
    assert isinstance(S.underlying_stack(), QuotientStack)
    xi = S.clutching_morphism()
    assert xi is not None
    assert xi in Hom(xi.domain(), XSbar)
    assert xi.codomain() is XSbar
    assert isinstance(xi.domain(), ProductStack)
    assert xi.domain() is ProductStack(xi.domain().factors(), base=k)


def test_stable_graphs_actions_and_hom_contraction():
    graphs = StableGraphs(1, (1,))
    smooth = graphs.smooth()
    nodal = next(g for g in graphs if g.num_edges() > 0)
    assert isinstance(nodal.action_on_half_edges(), Action)
    assert isinstance(nodal.action_on_edges(), Action)
    assert isinstance(nodal.action_on_vertices(), Action)
    morph = Hom(nodal, smooth).an_element()
    assert morph.is_contraction()
    assert not morph.is_isomorphism() or nodal == smooth


def test_moduli_fiber_family_and_dual_graph():
    k = spec(QQ)
    I = (1,)
    assert CurveFamilies(k).is_subcategory(Schemes(k))
    assert PointedCurveFamilies(k, I).is_subcategory(CurveFamilies(k))
    assert StablePointedCurveFamilies(k, 1, I).is_subcategory(PointedCurveFamilies(k, I))

    family = Mbar_gn(1, 1, base=k)(k).an_element()
    assert family in StablePointedCurveFamilies(k, 1, I)
    C = family.fiber("t")
    assert C in StablePointedCurves(k, 1, I)
    assert C.is_stable()
    Gamma = C.dual_graph()
    assert Gamma in StableGraphs(1, I)
    phi = family.dual_graph_specialization()
    assert phi.is_contraction()
    assert phi in Hom(
        StableGraphs(1, I)(phi.domain()),
        StableGraphs(1, I)(phi.codomain()),
    )


def test_g0_boundary_poset_matches_compatible_splits():
    k = spec(QQ)
    n = 4
    XSbar = Mbar_gn(0, n, base=k)
    P = XSbar.boundary().stratification_poset(order="specialization")
    # Full dual-graph specialization poset (including smooth) matches the oracle;
    # boundary drops the smooth stratum, so compare to the induced subposet.
    full = XSbar.stratification(by=StableDualGraph()).specialization_poset()
    oracle = expected_M0n_specialization_poset(n)
    assert full.is_isomorphic(oracle)
    assert isinstance(P, FinitePoset)
    assert P.cardinality() == oracle.cardinality() - 1


def test_independent_A1_P1_compactification_and_stratification():
    A1 = AffineSpace(QQ, 1)
    P1 = ProjectiveSpace(QQ, 1)
    c = scheme_open_immersion_compactification(A1, P1)
    assert c.target().is_proper()
    b = c.boundary()
    Sigma = c.target().stratify([c.source(), b])
    P = Sigma.specialization_poset()
    assert isinstance(P, FinitePoset)
    assert P.is_isomorphic(posets.ChainPoset(2))

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
    StableGraphCategory,
    StablePointedCurveFamilies,
    StablePointedCurves,
    StratifiedSpaces,
    StratifiedStacks,
    Varieties,
    scheme_open_immersion_compactification,
    spec,
)
from dm_moduli_spike.geometry.stratification import StableDualGraph, Strata, Stratifications
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.poset_oracle import expected_M0n_specialization_poset


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
    assert c.parent() is Compactifications(XS)
    assert c.domain() is XS
    assert c.codomain() is Mbar_gn(1, 1, base=k)
    assert c.is_open_immersion()
    assert c.open_immersion() in Hom(XS, c.codomain())
    assert c.codomain().is_proper()
    assert c in Compactifications(XS)


def test_coarse_compactification_boundary_stratified_spaces():
    k = spec(QQ)
    XS = M_gn(1, 1, base=k)
    c = XS.compactification()
    cc = c.coarse_compactification()
    assert c.coarse_moduli_square_commutes()
    assert cc.source() is XS.coarse_moduli_morphism().space()
    assert cc.target() is c.target().coarse_moduli_morphism().space()
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
    assert Sigma.parent() is Stratifications(XSbar)
    assert Sigma in Stratifications(XSbar)
    assert Sigma.indexing_category() == StableGraphs(1, (1,))
    Gamma = next(g for g in Sigma.index_poset() if g.num_edges() > 0)
    S = Sigma.stratum(Gamma)
    assert isinstance(S.parent(), Strata)
    assert S.parent() is Strata(Sigma)
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
    target, morph, _size = nodal.elementary_contractions()[0]
    assert morph.parent() is Hom(nodal, target)
    assert morph.is_contraction()
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
    assert C.is_smooth()
    Cs = family.fiber("special")
    Cg = family.fiber("generic")
    assert Cs.is_nodal()
    assert Cg.is_smooth()
    assert Cs.dual_graph().num_edges() > Cg.dual_graph().num_edges()
    Gamma = C.dual_graph()
    assert Gamma in StableGraphs(1, I)
    phi = family.dual_graph_specialization()
    assert phi.is_contraction()
    assert not phi.is_isomorphism()
    assert phi.domain().num_edges() == Cs.dual_graph().num_edges()
    assert phi.codomain().num_edges() == Cg.dual_graph().num_edges()
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
    assert c.parent() is Compactifications(c.source())
    assert c.open_immersion() in Hom(c.source(), c.target())
    assert c.target().is_proper()
    b = c.boundary()
    Sigma = c.target().stratify([c.source(), b])
    assert Sigma.parent() is Stratifications(c.target())
    P = Sigma.specialization_poset()
    assert isinstance(P, FinitePoset)
    assert P.is_isomorphic(posets.ChainPoset(2))


def test_quotient_stack_outside_moduli():
    r"""QuotientStack is a general construction, not Mbar-specific."""
    from sage.groups.perm_gps.permgroup_named import SymmetricGroup

    from dm_moduli_spike.geometry.compactification import SchemeStack

    k = spec(QQ)
    space = SchemeStack(
        AffineSpace(QQ, 1),
        k,
        name="A1",
        axioms=frozenset({"FiniteType", "Separated"}),
    )
    G = SymmetricGroup(2)
    Q = QuotientStack(space, G, None)
    assert isinstance(Q, QuotientStack)
    assert Q.space() is space
    assert Q.group() is G
    assert Q in DeligneMumfordStacks(k)


def test_gamma_objects_and_hom_domain_are_stable_graphs():
    Gamma = StableGraphCategory(1, 1)
    objects = Gamma.objects()
    assert objects
    assert all(isinstance(g, StableGraphs(1, (1,)).element_class) for g in objects)
    assert all(g.parent() is StableGraphs(1, (1,)) for g in objects)
    G, H = objects[0], objects[-1]
    HomGH = Hom(G, H)
    assert HomGH.domain() is G or HomGH.domain() == G
    assert isinstance(HomGH.domain(), type(G))
    assert HomGH.domain().parent() is StableGraphs(1, (1,))


def test_typed_parents_have_element_constructors():
    from dm_moduli_spike.objects.stable_graphs import Edge, HalfEdge, Leg, Vertex

    Gamma = StableGraphCategory(0, 4)
    g = next(g for g in Gamma.stable_graphs() if g.num_edges() > 0)
    v = g.vertices()(0)
    assert isinstance(v, Vertex)
    assert v == 0
    h = g.half_edges()(0)
    assert isinstance(h, HalfEdge)
    assert h == 0
    e = next(iter(g.edges()))
    assert isinstance(g.edges()(e), Edge)
    assert g.edges()(e) == e
    assert g.edges()(e.half_edges()) == e
    leg = next(iter(g.legs()))
    assert isinstance(g.legs()(leg), Leg)
    assert g.legs()(leg) == leg
    assert g.legs()(leg.label()) == leg


def test_stable_graph_canonical_record_is_private():
    Gamma = StableGraphCategory(0, 4)
    g = next(iter(Gamma.stable_graphs()))
    assert "canonical_representative" not in dir(g)
    assert hasattr(g, "_canonical_record")

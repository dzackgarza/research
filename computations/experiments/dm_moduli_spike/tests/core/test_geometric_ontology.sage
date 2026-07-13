r"""§14 acceptance tests for the geometric ontology foundation."""

from __future__ import annotations

from sage.combinat.posets.posets import FinitePoset
from sage.rings.rational_field import QQ
from sage.schemes.affine.affine_space import AffineSpace
from sage.schemes.projective.projective_space import ProjectiveSpace

from dm_moduli_spike import (
    AlgebraicSpaces,
    Compactifications,
    DeligneMumfordStacks,
    M_gn,
    Mbar_gn,
    ModuliStacks,
    ProductStack,
    QuotientStack,
    Schemes,
    Stacks,
    AlgebraicStacks,
    Varieties,
    scheme_open_immersion_compactification,
    spec,
)
from dm_moduli_spike.geometry.stratification import StableDualGraph
from dm_moduli_spike.objects.stable_graphs import StableGraphs


def test_category_hierarchy_subcategories():
    k = spec(QQ)
    assert Varieties(k).is_subcategory(Schemes(k))
    assert Varieties(k).is_subcategory(AlgebraicSpaces(k))
    assert AlgebraicSpaces(k).is_subcategory(DeligneMumfordStacks(k))
    assert DeligneMumfordStacks(k).is_subcategory(AlgebraicStacks(k))
    assert AlgebraicStacks(k).is_subcategory(Stacks(k))


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


def test_boundary_stratification_poset_M11():
    k = spec(QQ)
    XSbar = Mbar_gn(1, 1, base=k)
    bX = XSbar.boundary()
    P = bX.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)
    assert P.cardinality() >= 1


def test_stratum_is_quotient_stack_and_clutching_hom():
    k = spec(QQ)
    XSbar = Mbar_gn(1, 1, base=k)
    Sigma = XSbar.stratification(by=StableDualGraph())
    Gamma = next(g for g in Sigma.index_poset() if g.num_edges() > 0)
    S = Sigma.stratum(Gamma)
    assert isinstance(S.underlying_stack(), QuotientStack)
    xi = S.clutching_morphism()
    assert xi is not None
    assert xi in xi.parent()
    assert xi.codomain() is XSbar
    assert isinstance(xi.domain(), ProductStack)


def test_stable_graphs_parent_and_fiber_dual_graph():
    k = spec(QQ)
    I = (1,)
    graphs = StableGraphs(1, I)
    Gamma = graphs.an_element()
    assert Gamma.num_edges() == 0
    assert Gamma in graphs or Gamma.parent() is graphs

    family = Mbar_gn(1, 1, base=k)(k).an_element()
    # fiber via moduli family API
    from dm_moduli_spike.curves.families import StablePointedCurveFamily

    fam = StablePointedCurveFamily(k, "C", (), genus=1, marking_set=I)
    C = fam.fiber("t")
    assert C.is_stable()
    assert C.dual_graph().genus() == 1


def test_independent_A1_P1_compactification_and_stratification():
    A1 = AffineSpace(QQ, 1)
    P1 = ProjectiveSpace(QQ, 1)
    c = scheme_open_immersion_compactification(A1, P1)
    assert c.target().is_proper()
    b = c.boundary()
    Sigma = c.target().stratify([c.source(), b])
    P = Sigma.specialization_poset()
    assert isinstance(P, FinitePoset)
    assert P.cardinality() == 2

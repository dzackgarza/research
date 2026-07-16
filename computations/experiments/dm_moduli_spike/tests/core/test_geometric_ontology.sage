r"""§14 / review Wave-1 acceptance tests for the geometric ontology foundation."""

from __future__ import annotations

from sage.categories.action import Action
from sage.categories.homset import Hom
from sage.categories.schemes import Schemes
from sage.combinat.posets.posets import FinitePoset
from sage.rings.rational_field import QQ
from sage.schemes.affine.affine_space import AffineSpace
from sage.schemes.projective.projective_space import ProjectiveSpace
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet

from dm_moduli_spike import (
    AlgebraicSpaces,
    AlgebraicStacks,
    Compactifications,
    CurveFamilies,
    DeligneMumfordStacks,
    LocallyClosedSubstacks,
    M_gI,
    M_gn,
    Mbar_gI,
    Mbar_gn,
    ModuliStacks,
    PointedCurveFamilies,
    ProductStack,
    QuotientStack,
    Stacks,
    StableGraphCategory,
    StablePointedCurveFamilies,
    StablePointedCurves,
    StratifiedSpaces,
    StratifiedStacks,
    Varieties,
    scheme_open_immersion_compactification,
    spec,
)
from dm_moduli_spike.categories.curves import SmoothCurves
from dm_moduli_spike.categories.schemes import schemes_over
from dm_moduli_spike.geometry.stratification import StableDualGraph, Strata, Stratifications
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.poset_oracle import expected_M0n_specialization_poset


def test_category_hierarchy_subcategories():
    k = spec(QQ)
    assert Varieties(k).is_subcategory(schemes_over(k))
    assert Varieties(k).is_subcategory(AlgebraicSpaces(k))
    assert AlgebraicSpaces(k).is_subcategory(DeligneMumfordStacks(k))
    assert DeligneMumfordStacks(k).is_subcategory(AlgebraicStacks(k))
    assert AlgebraicStacks(k).is_subcategory(Stacks(k))
    # Equipped moduli stacks are NOT a subcategory of DM stacks.
    assert not ModuliStacks(k).is_subcategory(DeligneMumfordStacks(k))
    assert ModuliStacks(k).is_subcategory(Stacks(k))
    assert StratifiedStacks(k).is_subcategory(DeligneMumfordStacks(k))
    assert StratifiedSpaces(k).is_subcategory(AlgebraicSpaces(k))
    # Stratified stacks do not inherit into algebraic spaces via StratifiedSpaces.
    assert not StratifiedStacks(k).is_subcategory(StratifiedSpaces(k))
    assert not StratifiedStacks(k).is_subcategory(AlgebraicSpaces(k))


def test_moduli_stack_category_membership_M11():
    k = spec(QQ)
    XS = M_gn(1, 1, base=k)
    assert XS in ModuliStacks(k)
    assert XS in DeligneMumfordStacks(k)
    assert XS.coarse_space() in AlgebraicSpaces(k)
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
    assert bX not in AlgebraicSpaces(k)
    P = bX.stratification_poset(order="specialization")
    assert isinstance(P, FinitePoset)
    assert P.cardinality() >= 1


def test_stratum_locally_closed_and_clutching_hom():
    k = spec(QQ)
    XSbar = Mbar_gn(1, 1, base=k)
    Sigma = XSbar.stratification(by=StableDualGraph())
    assert Sigma.parent() is Stratifications(XSbar)
    assert Sigma in Stratifications(XSbar)
    assert Sigma.indexing_category() is StableGraphCategory(1, 1)
    assert Sigma.indexing_category().objects() is StableGraphs(1, (1,))
    Gamma = next(g for g in Sigma.index_poset() if g.num_edges() > 0)
    S = Sigma.stratum(Gamma)
    assert isinstance(S.parent(), Strata)
    assert S.parent() is Strata(Sigma)
    assert S in LocallyClosedSubstacks(XSbar)
    assert isinstance(S.underlying_stack(), QuotientStack)
    from dm_moduli_spike.geometry.stratification import AutProductStackAction

    open_quot = S.underlying_stack()
    open_action = open_quot.action()
    assert open_action is not None
    assert isinstance(open_action, AutProductStackAction)
    assert open_action.acts_on_product_stack()
    assert open_action.domain() is open_quot.covering_product()
    assert open_action.codomain() is open_quot.covering_product()
    assert open_action.set() is open_quot.space()
    open_factors = open_quot.covering_product().factors()
    assert all(isinstance(F, type(M_gI(0, (1,), base=k))) or F.genus() >= 0 for F in open_factors)
    for F in open_factors:
        assert not F.is_proper()
    # QuotientStack consumes the action: étale atlas domain is the covering product.
    q_etale = open_quot.etale_atlas()
    assert q_etale.is_etale()
    assert q_etale.domain() is open_quot.covering_product()
    assert q_etale.domain() is open_quot.covering_space()
    assert q_etale.domain() is not open_quot
    assert q_etale.covering_kind() == "quotient_cover"
    assert q_etale.is_quotient_presentation_atlas()
    assert not q_etale.is_coarse_atlas()
    assert q_etale.domain_is_representable()
    assert q_etale.covering_space() is open_quot.covering_space()
    assert q_etale.quotient_group() is open_quot.group()
    assert q_etale.evidence() is not None
    assert q_etale.evidence().dm_diagonal_unramified_stamp()
    assert q_etale.evidence().links_dm_diagonal_axioms()
    # Fail-closed: product-of-moduli covering has no affine equation-level certs.
    assert q_etale.evidence().domain_affine_cover() == ()
    assert q_etale.evidence().scheme_certificates() == ()
    assert not q_etale.has_equation_level_etale_certificate()
    assert open_quot.group_is_finite()
    assert open_quot.group_order() == int(open_quot.group().order())
    assert q_etale.evidence().finite_etale_groupoid()
    assert q_etale.evidence().links_finite_etale_groupoid()
    assert q_etale.evidence().covering_unramified_stamp()
    assert q_etale.evidence().covering_smooth_stamp()
    assert q_etale.evidence().covering_formally_etale_stamp()
    assert q_etale.evidence().group_order() == open_quot.group_order()
    assert q_etale.covering_data()["finite_etale_groupoid"] is True
    assert q_etale.covering_data()["links_finite_etale_groupoid"] is True
    groupoid = open_quot.finite_etale_groupoid_presentation()
    assert groupoid is not None
    assert groupoid["finite_etale_groupoid"] is True
    assert groupoid["group_order"] == open_quot.group_order()
    presentation = open_quot.quotient_presentation()
    assert presentation["covering_space"] is open_quot.covering_space()
    assert presentation["atlas_domain_is_covering"] is True
    assert presentation["group_is_finite"] is True
    assert "finite_etale_groupoid_presentation" in presentation
    assert isinstance(open_action, Action)
    xi = S.clutching_morphism()
    assert xi is not None
    assert xi in Hom(xi.domain(), XSbar)
    assert xi.codomain() is XSbar
    assert isinstance(xi.domain(), ProductStack)
    for F in xi.domain().factors():
        assert F.is_proper()
    assert S.closure_normalization() is not None
    assert isinstance(S.closure_normalization(), QuotientStack)
    closure_action = S.closure_normalization().action()
    assert isinstance(closure_action, AutProductStackAction)
    assert closure_action.domain() is S.closure_normalization().covering_product()


def test_aut_product_stack_action_permutes_equal_type_factors():
    r"""Aut(Γ) acts on ∏ M by factor permutation; identity acts as id.

    Hardened on an equal-type 2-vertex graph: the nontrivial Aut element must
    return a ProductStack with swapped factors (not the original product).
    """
    from dm_moduli_spike import ProductStack, QuotientStack, StableGraphs, M_gI
    from dm_moduli_spike.geometry.stratification import AutProductStackAction

    k = spec(QQ)
    graphs = StableGraphs(2, 0)
    graph = next(
        g
        for g in graphs
        if g.num_vertices() == 2
        and g.vertex_genus(0) == 1
        and g.vertex_genus(1) == 1
        and g.automorphism_group(on="half_edges").order() == 2
    )
    assert graph.vertex_genus(0) == graph.vertex_genus(1)
    factors = tuple(M_gI(graph.vertex_genus(v), graph.flags_at(v), base=k) for v in range(2))
    # Equal-type factors are UniqueRepresentation-equal when markings match type.
    product = ProductStack(factors, base=k)
    aut = graph.automorphism_group(on="half_edges")
    action = AutProductStackAction(aut, product, graph)
    assert isinstance(action, Action)
    assert action.actor() is aut
    assert action.domain() is product
    assert action.codomain() is product
    identity = aut.one()
    swap = next(g for g in aut if g.order() == 2)

    assert action.factor_permutation_of(identity) == (0, 1)
    assert action.act(identity) is product
    assert action(identity) is product
    assert action._act_(identity) is product
    assert action._act_(identity, product) is product

    assert action.factor_permutation_of(swap) == (1, 0)
    swapped = action.act(swap)
    assert isinstance(swapped, ProductStack)
    assert swapped is not product
    assert swapped.factors() == (factors[1], factors[0])
    assert swapped.factors()[0] is factors[1]
    assert swapped.factors()[1] is factors[0]
    assert action.permute_factors(0) == (factors[1], factors[0])
    assert action(swap, product) is swapped

    iso = action.induced_isomorphism(swap)
    assert iso.domain() is product
    assert iso.codomain() is swapped

    quot = QuotientStack(product, aut, action)
    assert quot.covering_space() is product
    assert quot.act_on_covering(identity) is product
    assert quot.act_on_covering(swap) is swapped
    assert quot.etale_atlas().domain() is product
    assert quot.etale_atlas().domain() is quot.covering_space()
    induced = quot.induced_covering_automorphism(swap)
    assert induced.domain() is product
    assert induced.codomain() is swapped
    assert induced.kind() == "quotient_covering_automorphism"


def test_boundary_restrict_drops_smooth_stratum():
    k = spec(QQ)
    XSbar = Mbar_gn(1, 1, base=k)
    Sigma = XSbar.stratification(by=StableDualGraph())
    Sigma_D = Sigma.restrict(XSbar.boundary())
    assert set(Sigma_D.index_poset()) == {G for G in Sigma.index_poset() if G.num_edges() > 0}


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
    assert CurveFamilies(k).is_subcategory(schemes_over(k))
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
    assert Cs not in SmoothCurves(k)
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


def test_quotient_stack_requires_action():
    r"""QuotientStack requires a genuine action; actionless DM stamps are forbidden."""
    from sage.groups.perm_gps.permgroup_named import SymmetricGroup
    from sage.structure.unique_representation import UniqueRepresentation

    from dm_moduli_spike.geometry.compactification import SchemeStack

    k = spec(QQ)
    space = SchemeStack(
        AffineSpace(QQ, 1),
        k,
        name="A1",
        axioms=frozenset({"FiniteType", "Separated"}),
    )
    G = SymmetricGroup(2)
    try:
        QuotientStack(space, G, None)
        assert False, "expected TypeError for action=None"
    except TypeError:
        pass

    class FormalAction(UniqueRepresentation):
        def __init__(self, group, X):
            self._group = group
            self._X = X

    rho = FormalAction(G, space)
    Q = QuotientStack(space, G, rho)
    assert isinstance(Q, QuotientStack)
    assert Q.space() is space
    assert Q.group() is G
    assert Q.action() is rho


def test_stack_fiber_and_hom_2_isomorphisms():
    r"""2-isomorphisms relate 1-morphisms; they are not Hom-set elements."""
    from dm_moduli_spike import ModuliProblem, Stack, Stack2Isomorphism, StackObjectIsomorphism
    from dm_moduli_spike.geometry.stacks import StackHomset

    k = spec(QQ)
    XS = M_gn(1, 1, base=k)
    assert isinstance(XS.moduli_problem(), ModuliProblem)

    X = Stack(k, name="X", axioms=frozenset({"FiniteType"}))
    fiber = X.fiber(k)
    a = fiber.an_element()
    b = fiber.an_element()
    iso = fiber.isomorphism(a, b)
    assert isinstance(iso, StackObjectIsomorphism)
    assert iso.source() is a
    assert iso.target() is b

    HomXX = StackHomset(XS, XS)
    f = HomXX.an_element()
    g = HomXX(kind="morphism")
    two = HomXX.isomorphism(f, g)
    assert isinstance(two, Stack2Isomorphism)
    assert two not in HomXX
    assert two.source() is f
    assert two.target() is g

    from dm_moduli_spike.geometry.stacks import (
        AlgebraicSpace,
        AtlasChart,
        AtlasEvidence,
        AtlasMorphism,
        BaseChangeStack,
        FiberProductMediatingMorphism,
        FiberProductStack,
        FormallyEtaleSchemeCertificate,
        ModuliBaseChangeStack,
        ProductStack,
        PullbackMediatingMorphism,
        PullbackStack,
        StackMorphism,
    )

    Delta = XS.diagonal()
    assert Delta.domain() is XS
    fp = XS.fiber_product(XS)
    assert isinstance(fp, FiberProductStack)
    assert Delta.codomain() == fp
    assert fp.left_factor() is XS
    assert fp.right_factor() is XS
    assert fp.over_scheme() is XS.base_scheme()
    pi1, pi2 = fp.projections()
    assert pi1.domain() is fp and pi1.codomain() is XS
    assert pi2.domain() is fp and pi2.codomain() is XS
    assert fp.square_corners() == (fp, XS, XS, XS.base_scheme())
    Z = Stack(k, name="Z_for_fp", axioms=frozenset({"FiniteType"}))
    a_fp = StackMorphism(Z, XS, kind="fp_leg_left")
    b_fp = StackMorphism(Z, XS, kind="fp_leg_right")
    m_fp = fp.mediating_morphism(a_fp, b_fp)
    assert isinstance(m_fp, FiberProductMediatingMorphism)
    assert m_fp.recovers_legs()
    assert m_fp.composed_with_projection_left().kind() == "fp_leg_left"
    assert m_fp.composed_with_projection_right().kind() == "fp_leg_right"

    atlas = XS.atlas()
    assert isinstance(atlas, AtlasMorphism)
    assert isinstance(atlas.domain(), AlgebraicSpace)
    assert atlas.domain() is XS.coarse_space()
    assert atlas.domain() is not XS
    assert atlas.codomain() is XS
    assert atlas in Hom(atlas.domain(), XS)
    assert not atlas.is_etale()
    assert atlas.is_covering()
    assert atlas.domain_is_representable()
    assert atlas.covering_kind() == "coarse_moduli"
    assert atlas.is_coarse_atlas()
    assert atlas.distinguishes_etale_from_coarse()
    assert atlas.covering_data()["covering_kind"] == "coarse_moduli"
    assert atlas.covering_data()["is_coarse_atlas"] is True

    etale = XS.etale_atlas()
    assert isinstance(etale, AtlasMorphism)
    assert etale.is_etale()
    from dm_moduli_spike.geometry.stacks import AffineAlgebraicSpace, _TrivialCoveringAction

    # M_{1,1}: owned Legendre finite étale cover U → M_{1,1} ≅ [U/S₃] (2 invertible).
    assert isinstance(etale.domain(), AffineAlgebraicSpace)
    assert etale.domain() is not XS
    assert etale.domain() is not XS.coarse_space()
    assert etale.codomain() is XS
    assert etale in Hom(etale.domain(), XS)
    assert etale.is_covering()
    assert etale.domain_is_representable()
    assert etale.covering_kind() == "legendre_finite_etale_cover"
    assert etale.is_quotient_presentation_atlas()
    assert not etale.is_coarse_atlas()
    assert etale.distinguishes_etale_from_coarse()
    # Fail-closed: étale atlas must not silently become the coarse atlas.
    assert etale.domain() is not atlas.domain()
    assert etale.covering_kind() != atlas.covering_kind()
    ev = etale.evidence()
    assert isinstance(ev, AtlasEvidence)
    assert ev.etale_stamp()
    assert ev.representable_domain()
    assert ev.dm_diagonal_unramified_stamp()
    assert ev.dm_diagonal_representable_stamp()
    assert ev.links_dm_diagonal_axioms()
    assert ev.diagonal() is not None
    assert ev.diagonal().domain() is XS
    assert ev.diagonal().codomain() == XS.fiber_product(XS)
    assert etale.covering_data()["dm_diagonal_unramified_stamp"] is True
    assert etale.covering_data()["diagonal"] is ev.diagonal()
    assert etale.covering_data()["links_dm_diagonal_axioms"] is True
    assert ev.finite_etale_groupoid()
    assert ev.links_finite_etale_groupoid()
    assert ev.group_order() == 6
    assert etale.covering_space() is etale.domain()
    assert int(etale.quotient_group().order()) == 6
    cert = ev.scheme_certificate()
    assert isinstance(cert, FormallyEtaleSchemeCertificate)
    assert cert.is_flat() and cert.is_unramified() and cert.is_formally_etale()
    assert cert.reason() == "identity_ring_map_isomorphism"
    assert etale.domain().affine_cover() != ()
    assert etale.has_equation_level_etale_certificate()
    assert etale.equation_level_etale()
    assert not atlas.has_equation_level_etale_certificate()
    presentation = XS.legendre_quotient_presentation()
    assert presentation is not None
    assert presentation["group_order"] == 6
    assert presentation["covering_space"] is etale.domain()
    assert presentation["finite_etale_groupoid"] is True
    assert presentation["degree"] == 6

    # M_{0,4}: owned cross-ratio affine étale atlas (ℙ¹ ∖ {0,1,∞}).
    YS = M_gn(0, 4, base=k)
    ys_atlas = YS.atlas()
    ys_etale = YS.etale_atlas()
    assert ys_atlas.covering_kind() == "coarse_moduli"
    assert not ys_atlas.is_etale()
    assert not ys_atlas.has_equation_level_etale_certificate()
    assert ys_etale.is_etale()
    assert isinstance(ys_etale.domain(), AffineAlgebraicSpace)
    assert ys_etale.domain() is not YS
    assert ys_etale.domain() is not YS.coarse_space()
    assert ys_etale.covering_kind() == "moduli_affine_etale_chart"
    assert ys_etale.domain().affine_cover() != ()
    assert ys_etale.has_equation_level_etale_certificate()
    assert ys_etale.equation_level_etale()
    ys_certs = ys_etale.evidence().scheme_certificates()
    assert ys_certs
    assert any(c.reason() == "identity_ring_map_isomorphism" for c in ys_certs)
    assert all(
        any(c.domain_scheme() is chart or c.domain_scheme().ring() == chart.ring() for c in ys_certs)
        for chart in ys_etale.evidence().domain_affine_cover()
    )

    # M_{0,3}: point Spec(R) — owned affine identity chart.
    ZS = M_gn(0, 3, base=k)
    zs_etale = ZS.etale_atlas()
    assert isinstance(zs_etale.domain(), AffineAlgebraicSpace)
    assert zs_etale.domain().as_affine_scheme() is k
    assert zs_etale.covering_kind() == "moduli_affine_etale_chart"
    assert zs_etale.has_equation_level_etale_certificate()

    # Mbar_{0,3}: same point Spec(R) — stack ≅ scheme ≅ Spec(R).
    Mbar03 = Mbar_gn(0, 3, base=k)
    mbar03_etale = Mbar03.etale_atlas()
    assert isinstance(mbar03_etale.domain(), AffineAlgebraicSpace)
    assert mbar03_etale.domain().as_affine_scheme() is k
    assert mbar03_etale.covering_kind() == "moduli_affine_etale_chart"
    assert mbar03_etale.has_equation_level_etale_certificate()
    assert mbar03_etale.domain() is not Mbar03.coarse_space()

    # Mbar_{0,4}: stack ≅ ℙ¹ — owned standard affine cover (not the coarse map).
    from dm_moduli_spike.geometry.stacks import ProjectiveLineAlgebraicSpace

    Mbar04 = Mbar_gn(0, 4, base=k)
    mbar_etale = Mbar04.etale_atlas()
    assert mbar_etale.is_etale()
    assert isinstance(mbar_etale.domain(), ProjectiveLineAlgebraicSpace)
    assert mbar_etale.domain().role() == "Mbar_0_4"
    assert mbar_etale.domain() is not Mbar04
    assert mbar_etale.domain() is not Mbar04.coarse_space()
    assert mbar_etale.covering_kind() == "moduli_scheme_affine_cover"
    assert len(mbar_etale.domain().affine_cover()) == 2
    assert mbar_etale.has_equation_level_etale_certificate()
    assert mbar_etale.equation_level_etale()
    assert not mbar_etale.is_coarse_atlas()
    mbar_certs = mbar_etale.evidence().scheme_certificates()
    assert mbar_certs
    assert all(
        any(c.domain_scheme() is chart or c.domain_scheme().ring() == chart.ring() for c in mbar_certs)
        for chart in mbar_etale.evidence().domain_affine_cover()
    )
    # Coarse atlas of Mbar_{0,4} remains non-equation-level (coarse ≠ étale).
    assert Mbar04.atlas().covering_kind() == "coarse_moduli"
    assert not Mbar04.atlas().has_equation_level_etale_certificate()

    # Mbar_{1,1}: Mbar(Γ(2)) ≅ ℙ¹ with S₃ finite étale groupoid (2 invertible).
    Mbar11 = Mbar_gn(1, 1, base=k)
    mbar11_etale = Mbar11.etale_atlas()
    assert isinstance(mbar11_etale.domain(), ProjectiveLineAlgebraicSpace)
    assert mbar11_etale.domain().role() == "Mbar_Gamma2"
    assert mbar11_etale.domain() is not Mbar11.coarse_space()
    assert mbar11_etale.domain() is not mbar_etale.domain()
    assert mbar11_etale.covering_kind() == "legendre_compact_finite_etale_cover"
    assert mbar11_etale.is_quotient_presentation_atlas()
    assert mbar11_etale.has_equation_level_etale_certificate()
    assert mbar11_etale.evidence().finite_etale_groupoid()
    assert mbar11_etale.evidence().group_order() == 6
    mbar11_pres = Mbar11.legendre_quotient_presentation()
    assert mbar11_pres is not None
    assert mbar11_pres["group_order"] == 6
    assert mbar11_pres["covering_space"] is mbar11_etale.domain()
    assert mbar11_pres["level_structure"] == "Mbar(Gamma(2))"
    assert "P1" in str(mbar11_pres["presentation"])

    # M_{0,5}: Knudsen configuration Spec(R[λ,μ]_{λ(λ-1)μ(μ-1)(λ-μ)}).
    M05 = M_gn(0, 5, base=k)
    m05_etale = M05.etale_atlas()
    assert isinstance(m05_etale.domain(), AffineAlgebraicSpace)
    assert m05_etale.domain() is not M05
    assert m05_etale.domain() is not M05.coarse_space()
    assert m05_etale.covering_kind() == "moduli_affine_etale_chart"
    assert m05_etale.domain().affine_cover() != ()
    assert m05_etale.has_equation_level_etale_certificate()
    assert m05_etale.equation_level_etale()
    assert M05.etale_atlas_gap() is None
    m05_ring = m05_etale.domain().as_affine_scheme().ring()
    assert len(m05_ring.gens()) == 2
    # Mbar_{0,5}: Kapranov Bl₄(ℙ²) — owned twelve-chart affine cover (stack ≅ scheme).
    from dm_moduli_spike.geometry.stacks import KapranovBlowupFourPointsP2AlgebraicSpace

    Mbar05 = Mbar_gn(0, 5, base=k)
    mbar05_etale = Mbar05.etale_atlas()
    assert isinstance(mbar05_etale.domain(), KapranovBlowupFourPointsP2AlgebraicSpace)
    assert mbar05_etale.domain() is not Mbar05
    assert mbar05_etale.domain() is not Mbar05.coarse_space()
    assert mbar05_etale.covering_kind() == "moduli_scheme_affine_cover"
    assert mbar05_etale.has_equation_level_etale_certificate()
    assert mbar05_etale.equation_level_etale()
    assert Mbar05.etale_atlas_gap() is None
    assert len(mbar05_etale.domain().affine_cover()) == 12
    assert mbar05_etale.domain().role() == "Mbar_0_5"
    assert mbar05_etale.domain().blown_up_points() == ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1))
    assert all(len(c.ring().gens()) == 2 for c in mbar05_etale.domain().affine_cover())
    # Coarse atlas of Mbar_{0,5} remains non-equation-level (coarse ≠ étale).
    assert Mbar05.atlas().covering_kind() == "coarse_moduli"
    assert not Mbar05.atlas().has_equation_level_etale_certificate()

    # M_{0,6}: Knudsen configuration Spec(R[λ,μ,ν]_{… diagonals / {0,1} …}).
    M06 = M_gn(0, 6, base=k)
    m06_etale = M06.etale_atlas()
    assert isinstance(m06_etale.domain(), AffineAlgebraicSpace)
    assert m06_etale.domain() is not M06
    assert m06_etale.domain() is not M06.coarse_space()
    assert m06_etale.covering_kind() == "moduli_affine_etale_chart"
    assert m06_etale.domain().affine_cover() != ()
    assert m06_etale.has_equation_level_etale_certificate()
    assert m06_etale.equation_level_etale()
    assert M06.etale_atlas_gap() is None
    m06_ring = m06_etale.domain().as_affine_scheme().ring()
    assert len(m06_ring.gens()) == 3
    # Parametric open Knudsen: M_{0,7} / M_{0,8} equation-level True (dim n-3).
    M07 = M_gn(0, 7, base=k)
    m07_etale = M07.etale_atlas()
    assert isinstance(m07_etale.domain(), AffineAlgebraicSpace)
    assert m07_etale.covering_kind() == "moduli_affine_etale_chart"
    assert m07_etale.has_equation_level_etale_certificate()
    assert m07_etale.equation_level_etale()
    assert M07.etale_atlas_gap() is None
    assert len(m07_etale.domain().as_affine_scheme().ring().gens()) == 4
    M08 = M_gn(0, 8, base=k)
    m08_etale = M08.etale_atlas()
    assert m08_etale.has_equation_level_etale_certificate()
    assert m08_etale.equation_level_etale()
    assert M08.etale_atlas_gap() is None
    assert len(m08_etale.domain().as_affine_scheme().ring().gens()) == 5
    # Mbar_{0,6}: Kapranov Bl(ℙ³) at 5 points + 10 lines — owned 288-chart cover.
    from dm_moduli_spike.geometry.stacks import KapranovBlowupFivePointsP3AlgebraicSpace

    Mbar06 = Mbar_gn(0, 6, base=k)
    mbar06_etale = Mbar06.etale_atlas()
    assert isinstance(mbar06_etale.domain(), KapranovBlowupFivePointsP3AlgebraicSpace)
    assert mbar06_etale.domain() is not Mbar06
    assert mbar06_etale.domain() is not Mbar06.coarse_space()
    assert mbar06_etale.covering_kind() == "moduli_scheme_affine_cover"
    assert mbar06_etale.has_equation_level_etale_certificate()
    assert mbar06_etale.equation_level_etale()
    assert Mbar06.etale_atlas_gap() is None
    assert len(mbar06_etale.domain().affine_cover()) == 288
    assert mbar06_etale.domain().role() == "Mbar_0_6"
    assert mbar06_etale.domain().blown_up_points() == (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (1, 1, 1, 1),
    )
    assert all(len(c.ring().gens()) == 3 for c in mbar06_etale.domain().affine_cover())
    assert Mbar06.atlas().covering_kind() == "coarse_moduli"
    assert not Mbar06.atlas().has_equation_level_etale_certificate()
    # Mbar_{0,7}: Kapranov Bl(ℙ⁴) — lazy owned cover (cardinality 17280; sample certs).
    from dm_moduli_spike.geometry.stacks import KapranovIteratedBlowupPnMinus3AlgebraicSpace
    from dm_moduli_spike.geometry.stacks import _kapranov_Ad_chart_count

    Mbar07 = Mbar_gn(0, 7, base=k)
    mbar07_etale = Mbar07.etale_atlas()
    assert isinstance(mbar07_etale.domain(), KapranovIteratedBlowupPnMinus3AlgebraicSpace)
    assert mbar07_etale.domain() is not Mbar07
    assert mbar07_etale.domain() is not Mbar07.coarse_space()
    assert mbar07_etale.covering_kind() == "moduli_scheme_affine_cover"
    assert mbar07_etale.has_equation_level_etale_certificate()
    assert mbar07_etale.equation_level_etale()
    assert Mbar07.etale_atlas_gap() is None
    assert mbar07_etale.domain().role() == "Mbar_0_7"
    assert mbar07_etale.domain().number_of_markings() == 7
    assert mbar07_etale.domain().projective_dimension() == 4
    assert len(mbar07_etale.domain().blown_up_points()) == 6
    assert mbar07_etale.domain().affine_cover_cardinality() == 5 * _kapranov_Ad_chart_count(4)
    assert mbar07_etale.domain().affine_cover_cardinality() == 17280
    mbar07_sample = mbar07_etale.domain().affine_cover_sample()
    assert len(mbar07_sample) == 5
    assert all(len(c.ring().gens()) == 4 for c in mbar07_sample)
    assert len(mbar07_etale.domain().affine_chart(0).ring().gens()) == 4
    assert len(mbar07_etale.domain().affine_chart(17279).ring().gens()) == 4
    assert Mbar07.atlas().covering_kind() == "coarse_moduli"
    assert not Mbar07.atlas().has_equation_level_etale_certificate()
    # Mbar_{0,8}: Kapranov Bl(ℙ⁵) — lazy owned cover (cardinality 2073600; sample certs).
    Mbar08 = Mbar_gn(0, 8, base=k)
    mbar08_etale = Mbar08.etale_atlas()
    assert isinstance(mbar08_etale.domain(), KapranovIteratedBlowupPnMinus3AlgebraicSpace)
    assert mbar08_etale.domain() is not Mbar08
    assert mbar08_etale.domain() is not Mbar08.coarse_space()
    assert mbar08_etale.covering_kind() == "moduli_scheme_affine_cover"
    assert mbar08_etale.has_equation_level_etale_certificate()
    assert mbar08_etale.equation_level_etale()
    assert Mbar08.etale_atlas_gap() is None
    assert mbar08_etale.domain().role() == "Mbar_0_8"
    assert mbar08_etale.domain().number_of_markings() == 8
    assert mbar08_etale.domain().projective_dimension() == 5
    assert len(mbar08_etale.domain().blown_up_points()) == 7
    assert mbar08_etale.domain().affine_cover_cardinality() == 6 * _kapranov_Ad_chart_count(5)
    assert mbar08_etale.domain().affine_cover_cardinality() == 2073600
    mbar08_sample = mbar08_etale.domain().affine_cover_sample()
    assert len(mbar08_sample) == 6
    assert all(len(c.ring().gens()) == 5 for c in mbar08_sample)
    assert len(mbar08_etale.domain().affine_chart(0).ring().gens()) == 5
    assert len(mbar08_etale.domain().affine_chart(2073599).ring().gens()) == 5
    assert Mbar08.atlas().covering_kind() == "coarse_moduli"
    assert not Mbar08.atlas().has_equation_level_etale_certificate()
    # Mbar_{0,n} for n>8: not owned (Kapranov chart bound) — fail-closed.
    Mbar09 = Mbar_gn(0, 9, base=k)
    assert not Mbar09.etale_atlas().has_equation_level_etale_certificate()
    gap_mbar09 = Mbar09.etale_atlas_gap()
    assert gap_mbar09 is not None
    assert gap_mbar09["reason"] == "no_owned_affine_etale_presentation"
    assert gap_mbar09["registry_owned_type"] is False
    assert isinstance(Mbar09.etale_atlas().domain(), AtlasChart)
    alts09 = gap_mbar09["alternate_proving_sets"]
    assert alts09[0]["proper_m0n_gap_construction"] == "kapranov_iterated_blowup_P_{n-3}"
    assert alts09[0]["proper_m0n_owned_max"] == 8
    assert alts09[0]["parametric_proper_m0n"] is True

    # M_{1,2} (open, 2 invertible): Legendre universal-curve Weierstrass affine, S₃ cover.
    M12 = M_gn(1, 2, base=k)
    m12_etale = M12.etale_atlas()
    assert isinstance(m12_etale.domain(), AffineAlgebraicSpace)
    assert m12_etale.domain() is not M12
    assert m12_etale.domain() is not M12.coarse_space()
    assert m12_etale.covering_kind() == "legendre_universal_curve_finite_etale_cover"
    assert m12_etale.is_quotient_presentation_atlas()
    assert m12_etale.has_equation_level_etale_certificate()
    assert m12_etale.equation_level_etale()
    assert m12_etale.evidence().finite_etale_groupoid()
    assert m12_etale.evidence().group_order() == 6
    assert M12.etale_atlas_gap() is None
    m12_pres = M12.legendre_quotient_presentation()
    assert m12_pres is not None
    assert m12_pres["group_order"] == 6
    assert m12_pres["degree"] == 6
    assert m12_pres["level_structure"] == "Gamma(2)_universal_curve"
    assert m12_pres["covering_space"] is m12_etale.domain()
    assert "univ_curve" in str(m12_pres["presentation"]) or "S3" in str(m12_pres["presentation"])
    m12_ring = m12_etale.domain().as_affine_scheme().ring()
    assert len(m12_ring.gens()) == 3
    # Open M_{1,3} / M_{1,4}: parametric Legendre marked-configuration pullback.
    M13 = M_gn(1, 3, base=k)
    m13_etale = M13.etale_atlas()
    assert isinstance(m13_etale.domain(), AffineAlgebraicSpace)
    assert m13_etale.covering_kind() == "legendre_marked_configuration_finite_etale_cover"
    assert m13_etale.is_quotient_presentation_atlas()
    assert m13_etale.has_equation_level_etale_certificate()
    assert m13_etale.equation_level_etale()
    assert m13_etale.evidence().finite_etale_groupoid()
    assert m13_etale.evidence().group_order() == 6
    assert M13.etale_atlas_gap() is None
    assert len(m13_etale.domain().as_affine_scheme().ring().gens()) == 5  # λ,x1,y1,x2,y2
    m13_pres = M13.legendre_quotient_presentation()
    assert m13_pres is not None
    assert m13_pres["level_structure"] == "Gamma(2)_marked_configuration"
    M14 = M_gn(1, 4, base=k)
    m14_etale = M14.etale_atlas()
    assert m14_etale.covering_kind() == "legendre_marked_configuration_finite_etale_cover"
    assert m14_etale.has_equation_level_etale_certificate()
    assert m14_etale.equation_level_etale()
    assert M14.etale_atlas_gap() is None
    assert len(m14_etale.domain().as_affine_scheme().ring().gens()) == 7  # λ + 3·(x,y)
    # Mbar_{1,2} (2 invertible): compactified Legendre universal-curve affine cover.
    from dm_moduli_spike.geometry.stacks import CompactifiedUniversalCurveAlgebraicSpace

    Mbar12 = Mbar_gn(1, 2, base=k)
    mbar12_etale = Mbar12.etale_atlas()
    assert isinstance(mbar12_etale.domain(), CompactifiedUniversalCurveAlgebraicSpace)
    assert mbar12_etale.domain() is not Mbar12
    assert mbar12_etale.domain() is not Mbar12.coarse_space()
    assert mbar12_etale.covering_kind() == "legendre_compact_universal_curve_finite_etale_cover"
    assert mbar12_etale.is_quotient_presentation_atlas()
    assert mbar12_etale.has_equation_level_etale_certificate()
    assert mbar12_etale.equation_level_etale()
    assert mbar12_etale.evidence().finite_etale_groupoid()
    assert mbar12_etale.evidence().group_order() == 6
    assert len(mbar12_etale.domain().affine_cover()) == 2
    assert mbar12_etale.domain().role() == "Mbar_Gamma2_univ_curve"
    assert Mbar12.etale_atlas_gap() is None
    mbar12_pres = Mbar12.legendre_quotient_presentation()
    assert mbar12_pres is not None
    assert mbar12_pres["group_order"] == 6
    assert mbar12_pres["degree"] == 6
    assert mbar12_pres["level_structure"] == "Mbar(Gamma(2))_universal_curve"
    assert mbar12_pres["covering_space"] is mbar12_etale.domain()
    assert "compact" in str(mbar12_pres["presentation"]) or "S3" in str(mbar12_pres["presentation"])
    assert Mbar12.hesse_quotient_presentation() is None
    # Mbar_{1,3} / Mbar_{1,4}: parametric compact Legendre marked-configuration cover.
    Mbar13 = Mbar_gn(1, 3, base=k)
    mbar13_etale = Mbar13.etale_atlas()
    assert isinstance(mbar13_etale.domain(), CompactifiedUniversalCurveAlgebraicSpace)
    assert mbar13_etale.covering_kind() == "legendre_compact_marked_configuration_finite_etale_cover"
    assert mbar13_etale.is_quotient_presentation_atlas()
    assert mbar13_etale.has_equation_level_etale_certificate()
    assert mbar13_etale.equation_level_etale()
    assert mbar13_etale.evidence().finite_etale_groupoid()
    assert mbar13_etale.evidence().group_order() == 6
    assert len(mbar13_etale.domain().affine_cover()) == 2
    assert mbar13_etale.domain().role() == "Mbar_Gamma2_marked_configuration"
    assert Mbar13.etale_atlas_gap() is None
    assert len(mbar13_etale.domain().affine_cover()[0].ring().gens()) == 5  # λ,x1,y1,x2,y2
    mbar13_pres = Mbar13.legendre_quotient_presentation()
    assert mbar13_pres is not None
    assert mbar13_pres["level_structure"] == "Mbar(Gamma(2))_marked_configuration"
    assert mbar13_pres["covering_space"] is mbar13_etale.domain()
    Mbar14 = Mbar_gn(1, 4, base=k)
    mbar14_etale = Mbar14.etale_atlas()
    assert mbar14_etale.covering_kind() == "legendre_compact_marked_configuration_finite_etale_cover"
    assert mbar14_etale.has_equation_level_etale_certificate()
    assert mbar14_etale.equation_level_etale()
    assert Mbar14.etale_atlas_gap() is None
    assert len(mbar14_etale.domain().affine_cover()) == 2
    assert mbar14_etale.domain().role() == "Mbar_Gamma2_marked_configuration"
    assert len(mbar14_etale.domain().affine_cover()[0].ring().gens()) == 7  # λ + 3·(x,y)

    # Char 2: Legendre unavailable; Hesse Γ(3) owns open / proper M_{1,1} (3=1 invertible).
    from sage.rings.finite_rings.finite_field_constructor import GF

    M11_char2 = M_gn(1, 1, base=spec(GF(2)))
    m11_c2 = M11_char2.etale_atlas()
    assert isinstance(m11_c2.domain(), AffineAlgebraicSpace)
    assert m11_c2.domain() is not M11_char2
    assert m11_c2.domain() is not M11_char2.coarse_space()
    assert m11_c2.covering_kind() == "hesse_finite_etale_cover"
    assert m11_c2.is_quotient_presentation_atlas()
    assert m11_c2.has_equation_level_etale_certificate()
    assert m11_c2.equation_level_etale()
    assert m11_c2.evidence().finite_etale_groupoid()
    assert m11_c2.evidence().group_order() == 24
    assert M11_char2.legendre_quotient_presentation() is None
    assert M11_char2.etale_atlas_gap() is None
    hesse_pres = M11_char2.hesse_quotient_presentation()
    assert hesse_pres is not None
    assert hesse_pres["group_order"] == 24
    assert hesse_pres["degree"] == 24
    assert hesse_pres["level_structure"] == "Gamma(3)"
    assert hesse_pres["covering_space"] is m11_c2.domain()
    assert "Hesse" in str(hesse_pres["presentation"]) or "SL2" in str(hesse_pres["presentation"])
    m11_c2_ring = m11_c2.domain().as_affine_scheme().ring()
    assert len(m11_c2_ring.gens()) == 1

    Mbar11_char2 = Mbar_gn(1, 1, base=spec(GF(2)))
    mbar11_c2 = Mbar11_char2.etale_atlas()
    assert isinstance(mbar11_c2.domain(), ProjectiveLineAlgebraicSpace)
    assert mbar11_c2.covering_kind() == "hesse_compact_finite_etale_cover"
    assert mbar11_c2.is_quotient_presentation_atlas()
    assert mbar11_c2.has_equation_level_etale_certificate()
    assert mbar11_c2.evidence().group_order() == 24
    assert Mbar11_char2.legendre_quotient_presentation() is None
    assert Mbar11_char2.etale_atlas_gap() is None
    mbar_hesse = Mbar11_char2.hesse_quotient_presentation()
    assert mbar_hesse is not None
    assert mbar_hesse["level_structure"] == "Mbar(Gamma(3))"
    assert mbar_hesse["covering_space"] is mbar11_c2.domain()

    # Char 2 open M_{1,2}: Hesse universal-curve affine (3 invertible).
    M12_char2 = M_gn(1, 2, base=spec(GF(2)))
    m12_c2 = M12_char2.etale_atlas()
    assert isinstance(m12_c2.domain(), AffineAlgebraicSpace)
    assert m12_c2.covering_kind() == "hesse_universal_curve_finite_etale_cover"
    assert m12_c2.is_quotient_presentation_atlas()
    assert m12_c2.has_equation_level_etale_certificate()
    assert m12_c2.evidence().group_order() == 24
    assert M12_char2.legendre_quotient_presentation() is None
    assert M12_char2.etale_atlas_gap() is None
    m12_hesse = M12_char2.hesse_quotient_presentation()
    assert m12_hesse is not None
    assert m12_hesse["level_structure"] == "Gamma(3)_universal_curve"
    assert m12_hesse["covering_space"] is m12_c2.domain()
    assert len(m12_c2.domain().as_affine_scheme().ring().gens()) == 3
    # Char 2 open M_{1,3}: Hesse marked-configuration pullback.
    M13_char2 = M_gn(1, 3, base=spec(GF(2)))
    m13_c2 = M13_char2.etale_atlas()
    assert m13_c2.covering_kind() == "hesse_marked_configuration_finite_etale_cover"
    assert m13_c2.has_equation_level_etale_certificate()
    assert m13_c2.evidence().group_order() == 24
    assert M13_char2.etale_atlas_gap() is None
    assert len(m13_c2.domain().as_affine_scheme().ring().gens()) == 5

    # Char 2 proper Mbar_{1,2}: compactified Hesse universal-curve cover.
    Mbar12_char2 = Mbar_gn(1, 2, base=spec(GF(2)))
    mbar12_c2 = Mbar12_char2.etale_atlas()
    assert isinstance(mbar12_c2.domain(), CompactifiedUniversalCurveAlgebraicSpace)
    assert mbar12_c2.covering_kind() == "hesse_compact_universal_curve_finite_etale_cover"
    assert mbar12_c2.is_quotient_presentation_atlas()
    assert mbar12_c2.has_equation_level_etale_certificate()
    assert mbar12_c2.evidence().group_order() == 24
    assert len(mbar12_c2.domain().affine_cover()) == 2
    assert mbar12_c2.domain().role() == "Mbar_Gamma3_univ_curve"
    assert Mbar12_char2.legendre_quotient_presentation() is None
    assert Mbar12_char2.etale_atlas_gap() is None
    mbar12_hesse = Mbar12_char2.hesse_quotient_presentation()
    assert mbar12_hesse is not None
    assert mbar12_hesse["level_structure"] == "Mbar(Gamma(3))_universal_curve"
    assert mbar12_hesse["covering_space"] is mbar12_c2.domain()
    # Char 2 proper Mbar_{1,3}: compact Hesse marked-configuration pullback.
    Mbar13_char2 = Mbar_gn(1, 3, base=spec(GF(2)))
    mbar13_c2 = Mbar13_char2.etale_atlas()
    assert isinstance(mbar13_c2.domain(), CompactifiedUniversalCurveAlgebraicSpace)
    assert mbar13_c2.covering_kind() == "hesse_compact_marked_configuration_finite_etale_cover"
    assert mbar13_c2.has_equation_level_etale_certificate()
    assert mbar13_c2.evidence().group_order() == 24
    assert mbar13_c2.domain().role() == "Mbar_Gamma3_marked_configuration"
    assert Mbar13_char2.etale_atlas_gap() is None
    assert len(mbar13_c2.domain().affine_cover()[0].ring().gens()) == 5

    # Char 3: Hesse unavailable; Legendre still owns (2 invertible). Prefer Legendre over Hesse.
    M11_char3 = M_gn(1, 1, base=spec(GF(3)))
    assert M11_char3.etale_atlas().covering_kind() == "legendre_finite_etale_cover"
    assert M11_char3.etale_atlas().has_equation_level_etale_certificate()
    assert M11_char3.hesse_quotient_presentation() is None
    assert M11_char3.legendre_quotient_presentation() is not None
    assert M11_char3.etale_atlas_gap() is None

    # Spec(Z): neither 2 nor 3 is a unit — Weierstrass 𝔾_m owned as fail-closed
    # evidence (infinite group ⇒ not finite étale equation-level). Igusa ordinary-only.
    from sage.rings.integer_ring import ZZ as _ZZ_atlas

    Z = spec(_ZZ_atlas)
    M11_Z = M_gn(1, 1, base=Z)
    Mbar11_Z = Mbar_gn(1, 1, base=Z)
    M12_Z = M_gn(1, 2, base=Z)
    Mbar12_Z = Mbar_gn(1, 2, base=Z)
    M13_Z = M_gn(1, 3, base=Z)
    M14_Z = M_gn(1, 4, base=Z)
    Mbar13_Z = Mbar_gn(1, 3, base=Z)
    Mbar14_Z = Mbar_gn(1, 4, base=Z)
    assert isinstance(M11_Z.etale_atlas().domain(), AtlasChart)
    assert not M11_Z.etale_atlas().has_equation_level_etale_certificate()
    gap_Z = M11_Z.etale_atlas_gap()
    assert gap_Z is not None
    assert gap_Z["reason"] == "legendre_and_hesse_unavailable"
    assert gap_Z["equation_level"] is False
    assert gap_Z["pre_225_remaining_after_this"] == "general_(g,n)_only"
    assert gap_Z["base_hypothesis"]["two_invertible"] is False
    assert gap_Z["base_hypothesis"]["three_invertible"] is False
    alts_Z = gap_Z["alternate_proving_sets"]
    assert alts_Z[0]["name"] == "weierstrass_gm_quotient"
    assert alts_Z[0]["status"] == "owned_not_finite_etale"
    assert alts_Z[1]["name"] == "igusa_ordinary_a6_chart"
    assert alts_Z[1]["status"] == "incomplete_ordinary_only"
    wei = M11_Z.weierstrass_gm_presentation()
    assert wei is not None
    assert alts_Z[0]["presentation"]["covering_space"] is wei["covering_space"]
    assert alts_Z[0]["presentation"]["covering_kind"] == wei["covering_kind"]
    assert alts_Z[0]["presentation"]["finite_etale_groupoid"] is False
    assert wei["group_kind"] == "Gm"
    assert wei["group_infinite"] is True
    assert wei["finite_etale_groupoid"] is False
    assert wei["equation_level"] is False
    assert wei["covering_kind"] == "weierstrass_gm_smooth_quotient"
    assert wei["covering_smooth_stamp"] is True
    assert wei["covering_formally_etale_stamp"] is False
    assert isinstance(wei["covering_space"], AffineAlgebraicSpace)
    assert wei["covering_space"].affine_cover() != ()
    assert "infinite" in wei["proof_not_finite_etale"].lower() or "Gm" in wei["proof_not_finite_etale"]
    # Fields never hit both-unavailable: char 2 ⇒ Hesse; char 3 ⇒ Legendre.
    assert XS.weierstrass_gm_presentation() is None
    assert M11_char2.weierstrass_gm_presentation() is None
    assert M11_char3.weierstrass_gm_presentation() is None
    gap_mbar11_Z = Mbar11_Z.etale_atlas_gap()
    assert gap_mbar11_Z is not None
    assert gap_mbar11_Z["reason"] == "legendre_and_hesse_unavailable"
    assert Mbar11_Z.weierstrass_gm_presentation() is not None
    assert Mbar11_Z.weierstrass_gm_presentation()["finite_etale_groupoid"] is False
    gap_m12_Z = M12_Z.etale_atlas_gap()
    assert gap_m12_Z is not None
    assert gap_m12_Z["reason"] == "m_1_2_legendre_and_hesse_unavailable"
    assert M12_Z.weierstrass_gm_presentation()["covering_space"].affine_cover() != ()
    gap_mbar12_Z = Mbar12_Z.etale_atlas_gap()
    assert gap_mbar12_Z is not None
    assert gap_mbar12_Z["reason"] == "mbar_1_2_legendre_and_hesse_unavailable"
    assert gap_mbar12_Z["pre_225_remaining_after_this"] == "general_(g,n)_only"
    # Open M_{1,3}/M_{1,4} on Spec(Z): owned type, fail-closed (no Weierstrass n≥3 chart).
    assert not M13_Z.etale_atlas().has_equation_level_etale_certificate()
    gap_m13_Z = M13_Z.etale_atlas_gap()
    assert gap_m13_Z is not None
    assert gap_m13_Z["reason"] == "m_1_n_legendre_and_hesse_unavailable"
    assert gap_m13_Z["registry_owned_type"] is True
    assert M13_Z.weierstrass_gm_presentation() is None
    assert gap_m13_Z["alternate_proving_sets"][0]["status"] == "owned_not_finite_etale_for_n_le_2_only"
    assert not M14_Z.etale_atlas().has_equation_level_etale_certificate()
    assert M14_Z.etale_atlas_gap()["reason"] == "m_1_n_legendre_and_hesse_unavailable"
    # Compact Mbar_{1,3}/Mbar_{1,4} on Spec(Z): owned type, fail-closed.
    assert not Mbar13_Z.etale_atlas().has_equation_level_etale_certificate()
    gap_mbar13_Z = Mbar13_Z.etale_atlas_gap()
    assert gap_mbar13_Z is not None
    assert gap_mbar13_Z["reason"] == "mbar_1_n_legendre_and_hesse_unavailable"
    assert gap_mbar13_Z["registry_owned_type"] is True
    assert Mbar13_Z.weierstrass_gm_presentation() is None
    assert not Mbar14_Z.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar14_Z.etale_atlas_gap()["reason"] == "mbar_1_n_legendre_and_hesse_unavailable"
    # General (g,n) remains the only pre-#225 atlas gap class beyond this sharpening.
    # Ownership registry: single inspectable source for owned (g,n,proper) presentations.
    from dm_moduli_spike.moduli.atlas_ownership import (
        OwnedAtlasPresentation,
        is_owned_etale_atlas_type,
        lookup_owned_etale_atlas,
        owned_etale_atlas_cardinality,
        owned_etale_atlas_presentations,
        owned_etale_atlas_type_keys,
        resolve_owned_etale_atlas,
    )

    rows = owned_etale_atlas_presentations()
    # Parametric open M0n + 2 open M1n + 2 compact M1n + 1 proper Kapranov
    # + open Igusa M20 + compact Igusa Mbar2 + parametric open M2n
    # + parametric compact M2n + open del Pezzo M30 + hyp locus M30
    # + compact del Pezzo Mbar3 + hyp locus Mbar3 + parametric open del Pezzo M3n
    # + parametric open hyp locus M3n + parametric compact del Pezzo M3n
    # + parametric compact hyp locus M3n + open canonical M40 + trigonal locus M40
    # + compact Petri Mbar4 = 21.
    assert owned_etale_atlas_cardinality() == 21
    assert len(rows) == 21
    assert all(isinstance(r, OwnedAtlasPresentation) for r in rows)
    assert sum(1 for r in rows if r.parametric_open_m0n) == 1
    assert sum(1 for r in rows if r.parametric_open_m1n) == 2
    assert sum(1 for r in rows if r.parametric_compact_m1n) == 2
    assert sum(1 for r in rows if r.parametric_proper_m0n) == 1
    assert sum(1 for r in rows if r.parametric_open_m2n) == 1
    assert sum(1 for r in rows if r.parametric_compact_m2n) == 1
    assert sum(1 for r in rows if r.construction == "igusa_binary_sextic_PGL2") == 1
    assert sum(1 for r in rows if r.construction == "igusa_mbar06_s6") == 1
    assert sum(1 for r in rows if r.construction == "del_pezzo_degree2_seven_points_PGL3") == 1
    assert sum(1 for r in rows if r.construction == "del_pezzo_compact_seven_points_PGL3") == 1
    assert sum(1 for r in rows if r.construction == "hyperelliptic_binary_octic_M08_S8") == 1
    assert sum(1 for r in rows if r.construction == "hyperelliptic_mbar08_s8") == 1
    assert sum(1 for r in rows if r.construction == "genus4_canonical_quadric_cubic_P3") == 1
    assert sum(1 for r in rows if r.construction == "genus4_trigonal_cone_cubic_P3") == 1
    assert sum(1 for r in rows if r.construction == "genus4_compact_canonical_petri_P9") == 1
    assert sum(1 for r in rows if r.parametric_open_m3n) == 2
    assert sum(1 for r in rows if r.parametric_compact_m3n) == 2
    assert sum(1 for r in rows if r.locus_only) == 5
    expanded = owned_etale_atlas_presentations(
        expand_open_m0n_through=8,
        expand_open_m1n_through=4,
        expand_compact_m1n_through=4,
        expand_proper_m0n_through=8,
        expand_open_m2n_through=4,
        expand_compact_m2n_through=4,
        expand_open_m3n_through=4,
        expand_compact_m3n_through=4,
    )
    assert (
        owned_etale_atlas_cardinality(
            expand_open_m0n_through=8,
            expand_open_m1n_through=4,
            expand_compact_m1n_through=4,
            expand_proper_m0n_through=8,
            expand_open_m2n_through=4,
            expand_compact_m2n_through=4,
            expand_open_m3n_through=4,
            expand_compact_m3n_through=4,
        )
        == 61
    )
    assert len(expanded) == 61
    assert all(
        not r.parametric_open_m0n
        and not r.parametric_open_m1n
        and not r.parametric_compact_m1n
        and not r.parametric_proper_m0n
        and not r.parametric_open_m2n
        and not r.parametric_compact_m2n
        and not r.parametric_open_m3n
        and not r.parametric_compact_m3n
        for r in expanded
    )
    type_keys = owned_etale_atlas_type_keys()
    # Open M0n n=3..8 + open M1n n=1..4 + compact M1n n=1..4 + proper (0,3..8)
    # + (2,0,False) + (2,0,True) + open M2n n=1..4 + compact M2n n=1..4
    # + (3,0,False) + (3,0,True) + open M3n n=1..4 + compact M3n n=1..4
    # + (4,0,False) + (4,0,True).
    assert len(type_keys) == 42
    assert type_keys == (
        (0, 3, False),
        (0, 4, False),
        (0, 5, False),
        (0, 6, False),
        (0, 7, False),
        (0, 8, False),
        (1, 1, False),
        (1, 2, False),
        (1, 3, False),
        (1, 4, False),
        (1, 1, True),
        (1, 2, True),
        (1, 3, True),
        (1, 4, True),
        (0, 3, True),
        (0, 4, True),
        (0, 5, True),
        (0, 6, True),
        (0, 7, True),
        (0, 8, True),
        (2, 0, False),
        (2, 0, True),
        (2, 1, False),
        (2, 2, False),
        (2, 3, False),
        (2, 4, False),
        (2, 1, True),
        (2, 2, True),
        (2, 3, True),
        (2, 4, True),
        (3, 0, False),
        (3, 0, True),
        (3, 1, False),
        (3, 2, False),
        (3, 3, False),
        (3, 4, False),
        (3, 1, True),
        (3, 2, True),
        (3, 3, True),
        (3, 4, True),
        (4, 0, False),
        (4, 0, True),
    )
    assert is_owned_etale_atlas_type(0, 4, proper=False)
    assert is_owned_etale_atlas_type(1, 1, proper=True)
    assert is_owned_etale_atlas_type(0, 6, proper=False)
    assert is_owned_etale_atlas_type(0, 7, proper=False)
    assert is_owned_etale_atlas_type(0, 9, proper=False)  # parametric: all n≥3
    assert is_owned_etale_atlas_type(1, 3, proper=False)
    assert is_owned_etale_atlas_type(1, 4, proper=False)
    assert is_owned_etale_atlas_type(1, 9, proper=False)  # parametric open: all n≥1
    assert is_owned_etale_atlas_type(1, 3, proper=True)
    assert is_owned_etale_atlas_type(1, 4, proper=True)
    assert is_owned_etale_atlas_type(1, 9, proper=True)  # parametric compact: all n≥1
    assert is_owned_etale_atlas_type(2, 0, proper=False)  # Igusa open M_{2,0}
    assert is_owned_etale_atlas_type(2, 0, proper=True)  # Igusa compact Mbar_2
    assert is_owned_etale_atlas_type(2, 1, proper=False)  # Igusa marked open
    assert is_owned_etale_atlas_type(2, 9, proper=False)  # parametric marked open
    assert is_owned_etale_atlas_type(2, 1, proper=True)  # Igusa compact marked
    assert is_owned_etale_atlas_type(2, 9, proper=True)  # parametric compact marked
    assert is_owned_etale_atlas_type(3, 0, proper=False)  # del Pezzo open M_{3,0}
    assert is_owned_etale_atlas_type(3, 0, proper=True)  # compact del Pezzo Mbar_3
    assert is_owned_etale_atlas_type(3, 1, proper=False)  # marked del Pezzo open
    assert is_owned_etale_atlas_type(3, 9, proper=False)  # parametric marked open
    assert is_owned_etale_atlas_type(3, 1, proper=True)  # marked del Pezzo compact
    assert is_owned_etale_atlas_type(3, 9, proper=True)  # parametric marked compact
    assert is_owned_etale_atlas_type(4, 0, proper=False)  # canonical CI open M_{4,0}
    assert is_owned_etale_atlas_type(4, 0, proper=True)  # compact Petri Mbar_4
    assert not is_owned_etale_atlas_type(4, 1, proper=False)
    assert is_owned_etale_atlas_type(0, 6, proper=True)
    assert is_owned_etale_atlas_type(0, 7, proper=True)
    assert is_owned_etale_atlas_type(0, 8, proper=True)
    assert not is_owned_etale_atlas_type(0, 9, proper=True)
    assert lookup_owned_etale_atlas(0, 5, proper=False) is not None
    assert lookup_owned_etale_atlas(0, 5, proper=False).construction == "knudsen_configuration"
    assert lookup_owned_etale_atlas(0, 5, proper=True).covering_kind == "moduli_scheme_affine_cover"
    assert lookup_owned_etale_atlas(0, 6, proper=False).construction == "knudsen_configuration"
    assert lookup_owned_etale_atlas(0, 6, proper=False).covering_kind == "moduli_affine_etale_chart"
    assert lookup_owned_etale_atlas(0, 6, proper=True).construction == "kapranov_blowup_five_points_p3"
    assert lookup_owned_etale_atlas(0, 6, proper=True).covering_kind == "moduli_scheme_affine_cover"
    assert lookup_owned_etale_atlas(0, 7, proper=True).construction == "kapranov_iterated_blowup_P_{n-3}"
    assert lookup_owned_etale_atlas(0, 7, proper=True).covering_kind == "moduli_scheme_affine_cover"
    assert lookup_owned_etale_atlas(0, 8, proper=True).construction == "kapranov_iterated_blowup_P_{n-3}"
    assert lookup_owned_etale_atlas(0, 8, proper=True).covering_kind == "moduli_scheme_affine_cover"
    assert lookup_owned_etale_atlas(0, 7, proper=False).construction == "knudsen_configuration"
    assert lookup_owned_etale_atlas(0, 3, proper=False).construction == "point_spec"
    assert lookup_owned_etale_atlas(1, 3, proper=False).construction == "legendre_marked_configuration"
    assert lookup_owned_etale_atlas(1, 3, proper=True).construction == "legendre_marked_configuration_compact"
    assert lookup_owned_etale_atlas(2, 0, proper=False).construction == "igusa_binary_sextic_PGL2"
    assert lookup_owned_etale_atlas(2, 0, proper=False).covering_kind == "igusa_binary_sextic_finite_etale_cover"
    assert lookup_owned_etale_atlas(2, 0, proper=False).groupoid == "igusa_s6"
    assert lookup_owned_etale_atlas(2, 0, proper=True).construction == "igusa_mbar06_s6"
    assert lookup_owned_etale_atlas(2, 0, proper=True).covering_kind == "igusa_compact_finite_etale_cover"
    assert lookup_owned_etale_atlas(2, 0, proper=True).groupoid == "igusa_s6"
    assert lookup_owned_etale_atlas(2, 1, proper=False).construction == "igusa_rosenhain_universal_curve"
    assert lookup_owned_etale_atlas(2, 1, proper=False).covering_kind == "igusa_universal_curve_finite_etale_cover"
    assert lookup_owned_etale_atlas(2, 2, proper=False).construction == "igusa_rosenhain_marked_configuration"
    assert lookup_owned_etale_atlas(2, 2, proper=False).covering_kind == "igusa_marked_configuration_finite_etale_cover"
    assert lookup_owned_etale_atlas(2, 1, proper=True).construction == "igusa_compact_rosenhain_universal_curve"
    assert lookup_owned_etale_atlas(2, 1, proper=True).covering_kind == "igusa_compact_universal_curve_finite_etale_cover"
    assert lookup_owned_etale_atlas(2, 2, proper=True).construction == "igusa_compact_rosenhain_marked_configuration"
    assert lookup_owned_etale_atlas(2, 2, proper=True).covering_kind == "igusa_compact_marked_configuration_finite_etale_cover"
    assert lookup_owned_etale_atlas(3, 0, proper=False).construction == "del_pezzo_degree2_seven_points_PGL3"
    assert lookup_owned_etale_atlas(3, 0, proper=False).covering_kind == "del_pezzo_seven_points_finite_etale_cover"
    assert lookup_owned_etale_atlas(3, 0, proper=False).groupoid == "weyl_e7"
    assert lookup_owned_etale_atlas(3, 0, proper=True).construction == "del_pezzo_compact_seven_points_PGL3"
    assert lookup_owned_etale_atlas(3, 0, proper=True).covering_kind == "del_pezzo_compact_seven_points_finite_etale_cover"
    assert lookup_owned_etale_atlas(3, 0, proper=True).groupoid == "weyl_e7"
    assert lookup_owned_etale_atlas(4, 0, proper=False).construction == "genus4_canonical_quadric_cubic_P3"
    assert lookup_owned_etale_atlas(4, 0, proper=False).covering_kind == "genus4_canonical_ci_affine_chart"
    assert lookup_owned_etale_atlas(4, 0, proper=False).groupoid == "none"
    assert lookup_owned_etale_atlas(4, 0, proper=True).construction == "genus4_compact_canonical_petri_P9"
    assert lookup_owned_etale_atlas(4, 0, proper=True).covering_kind == "genus4_compact_canonical_ci_affine_cover"
    assert lookup_owned_etale_atlas(3, 1, proper=False).construction == "del_pezzo_universal_curve"
    assert lookup_owned_etale_atlas(3, 2, proper=False).construction == "del_pezzo_marked_configuration"
    assert lookup_owned_etale_atlas(3, 1, proper=True).construction == "del_pezzo_compact_universal_curve"
    assert lookup_owned_etale_atlas(3, 2, proper=True).construction == "del_pezzo_compact_marked_configuration"
    assert resolve_owned_etale_atlas(XS) is not None
    assert XS.owned_etale_atlas_presentation().covering_kind == "legendre_finite_etale_cover"
    assert resolve_owned_etale_atlas(YS).construction == "knudsen_cross_ratio"
    assert resolve_owned_etale_atlas(M06).construction == "knudsen_configuration"
    assert resolve_owned_etale_atlas(M07).construction == "knudsen_configuration"
    assert resolve_owned_etale_atlas(M13).construction == "legendre_marked_configuration"
    assert resolve_owned_etale_atlas(Mbar13).construction == "legendre_marked_configuration_compact"
    # Owned types stay equation-level True under matching base hypotheses.
    assert XS.etale_atlas().has_equation_level_etale_certificate()
    assert YS.etale_atlas().has_equation_level_etale_certificate()
    assert M05.etale_atlas().has_equation_level_etale_certificate()
    assert M06.etale_atlas().has_equation_level_etale_certificate()
    assert M07.etale_atlas().has_equation_level_etale_certificate()
    assert M08.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar05.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar06.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar07.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar08.etale_atlas().has_equation_level_etale_certificate()
    assert M12.etale_atlas().has_equation_level_etale_certificate()
    assert M13.etale_atlas().has_equation_level_etale_certificate()
    assert M14.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar12.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar13.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar14.etale_atlas().has_equation_level_etale_certificate()

    # Proper unmarked Mbar_2: Kapranov Mbar_{0,6} / S₆ cover (2 invertible).
    from dm_moduli_spike.geometry.stacks import KapranovBlowupFivePointsP3AlgebraicSpace

    M20 = Mbar_gn(2, 0, base=k)
    mbar20_etale = M20.etale_atlas()
    assert M20.etale_atlas_gap() is None
    assert isinstance(mbar20_etale.domain(), KapranovBlowupFivePointsP3AlgebraicSpace)
    assert mbar20_etale.has_equation_level_etale_certificate()
    assert mbar20_etale.covering_kind() == "igusa_compact_finite_etale_cover"
    assert mbar20_etale.is_quotient_presentation_atlas()
    assert M20.owned_etale_atlas_presentation().construction == "igusa_mbar06_s6"
    assert M20.owned_etale_atlas_presentation().groupoid == "igusa_s6"
    assert mbar20_etale.domain().role() == "Mbar_2_via_Mbar_0_6"
    assert mbar20_etale.domain().affine_cover() != ()
    igusa_compact_pres = M20.igusa_quotient_presentation()
    assert igusa_compact_pres is not None
    assert igusa_compact_pres["finite_etale_groupoid"] is True
    assert igusa_compact_pres["group_order"] == 720
    assert igusa_compact_pres["degree"] == 720
    assert igusa_compact_pres["construction"] == "igusa_mbar06_s6"
    assert igusa_compact_pres["coverage"] == "proper_Mbar_2"
    assert igusa_compact_pres["covering_space"] is mbar20_etale.domain()
    # Proper marked Mbar_{2,1} / Mbar_{2,2}: Kapranov fiber-product Rosenhain covers.
    from dm_moduli_spike.geometry.stacks import IgusaCompactMarkedM2nAlgebraicSpace

    Mbar21 = Mbar_gn(2, 1, base=k)
    mbar21_etale = Mbar21.etale_atlas()
    assert Mbar21.etale_atlas_gap() is None
    assert isinstance(mbar21_etale.domain(), IgusaCompactMarkedM2nAlgebraicSpace)
    assert mbar21_etale.has_equation_level_etale_certificate()
    assert mbar21_etale.covering_kind() == "igusa_compact_universal_curve_finite_etale_cover"
    assert mbar21_etale.is_quotient_presentation_atlas()
    assert Mbar21.owned_etale_atlas_presentation().construction == "igusa_compact_rosenhain_universal_curve"
    assert Mbar21.owned_etale_atlas_presentation().groupoid == "igusa_s6"
    assert mbar21_etale.domain().role() == "Mbar_2_1_via_Mbar_0_6"
    assert mbar21_etale.domain().affine_cover_cardinality() == 288
    assert len(mbar21_etale.domain().affine_cover_sample()) == 4
    assert mbar21_etale.domain().kapranov_base().role() == "Mbar_2_via_Mbar_0_6"
    igusa_mbar21 = Mbar21.igusa_quotient_presentation()
    assert igusa_mbar21 is not None
    assert igusa_mbar21["construction"] == "igusa_compact_rosenhain_universal_curve"
    assert igusa_mbar21["coverage"] == "proper_Mbar_2_1"
    assert igusa_mbar21["degree"] == 720
    Mbar22 = Mbar_gn(2, 2, base=k)
    mbar22_etale = Mbar22.etale_atlas()
    assert Mbar22.etale_atlas_gap() is None
    assert isinstance(mbar22_etale.domain(), IgusaCompactMarkedM2nAlgebraicSpace)
    assert mbar22_etale.has_equation_level_etale_certificate()
    assert mbar22_etale.covering_kind() == "igusa_compact_marked_configuration_finite_etale_cover"
    assert Mbar22.owned_etale_atlas_presentation().construction == "igusa_compact_rosenhain_marked_configuration"
    # Open M_{3,0}: owned del Pezzo / 7-points finite étale cover (2 invertible).
    M30 = M_gn(3, 0, base=k)
    m30_etale = M30.etale_atlas()
    assert isinstance(m30_etale.domain(), AffineAlgebraicSpace)
    assert M30.etale_atlas_gap() is None
    assert m30_etale.has_equation_level_etale_certificate()
    assert m30_etale.covering_kind() == "del_pezzo_seven_points_finite_etale_cover"
    assert m30_etale.is_quotient_presentation_atlas()
    assert M30.owned_etale_atlas_presentation().construction == "del_pezzo_degree2_seven_points_PGL3"
    assert M30.owned_etale_atlas_presentation().groupoid == "weyl_e7"
    assert m30_etale.domain().affine_cover() != ()
    assert len(m30_etale.domain().affine_cover()[0].ring().gens()) == 6  # a..f
    del_pezzo_pres = M30.del_pezzo_quotient_presentation()
    assert del_pezzo_pres is not None
    assert del_pezzo_pres["finite_etale_groupoid"] is True
    assert del_pezzo_pres["group_order"] == 2903040
    assert del_pezzo_pres["degree"] == 2903040
    assert del_pezzo_pres["construction"] == "del_pezzo_degree2_seven_points_PGL3"
    assert del_pezzo_pres["coverage"] == "dense_open_nonhyperelliptic_of_open_M_3"
    assert del_pezzo_pres["covering_space"] is m30_etale.domain()
    assert not M30.atlas().has_equation_level_etale_certificate()
    # Hyperelliptic locus presentation on open M_3 (parallel to del Pezzo etale_atlas).
    hyp_pres = M30.hyperelliptic_quotient_presentation()
    assert hyp_pres is not None
    assert hyp_pres["construction"] == "hyperelliptic_binary_octic_M08_S8"
    assert hyp_pres["coverage"] == "hyperelliptic_locus_of_open_M_3"
    assert hyp_pres["group_order"] == 40320
    assert len(hyp_pres["covering_space"].affine_cover()[0].ring().gens()) == 5  # t1..t5
    # Proper Mbar_3: owned compact del Pezzo / (P²)³ seven-points (lazy sample).
    from dm_moduli_spike.geometry.stacks import DelPezzoCompactSevenPointsAlgebraicSpace

    Mbar30 = Mbar_gn(3, 0, base=k)
    assert Mbar30.etale_atlas_gap() is None
    mbar30_etale = Mbar30.etale_atlas()
    assert isinstance(mbar30_etale.domain(), DelPezzoCompactSevenPointsAlgebraicSpace)
    assert mbar30_etale.has_equation_level_etale_certificate()
    assert mbar30_etale.covering_kind() == "del_pezzo_compact_seven_points_finite_etale_cover"
    assert mbar30_etale.is_quotient_presentation_atlas()
    assert Mbar30.owned_etale_atlas_presentation().construction == "del_pezzo_compact_seven_points_PGL3"
    assert Mbar30.owned_etale_atlas_presentation().groupoid == "weyl_e7"
    assert mbar30_etale.domain().role() == "Mbar_3_nh_via_seven_points"
    assert mbar30_etale.domain().affine_cover_cardinality() == 27
    assert len(mbar30_etale.domain().affine_cover_sample()) == 3
    del_pezzo_mbar30 = Mbar30.del_pezzo_quotient_presentation()
    assert del_pezzo_mbar30 is not None
    assert del_pezzo_mbar30["coverage"] == "dense_open_nonhyperelliptic_of_proper_Mbar_3"
    assert del_pezzo_mbar30["degree"] == 2903040
    # Hyperelliptic locus of Mbar_3 remains inspectable (locus-only; not etale_atlas).
    hyp_mbar30 = Mbar30.hyperelliptic_quotient_presentation()
    assert hyp_mbar30 is not None
    assert hyp_mbar30["coverage"] == "hyperelliptic_locus_of_proper_Mbar_3"
    assert hyp_mbar30["construction"] == "hyperelliptic_mbar08_s8"
    assert hyp_mbar30["degree"] == 40320
    # Marked open/compact M_{3,1}: del Pezzo fiber product (hyp locus-only).
    from dm_moduli_spike.geometry.stacks import DelPezzoCompactMarkedM3nAlgebraicSpace

    M31 = M_gn(3, 1, base=k)
    m31_etale = M31.etale_atlas()
    assert M31.etale_atlas_gap() is None
    assert m31_etale.has_equation_level_etale_certificate()
    assert m31_etale.covering_kind() == "del_pezzo_universal_curve_finite_etale_cover"
    assert len(m31_etale.domain().affine_cover()[0].ring().gens()) == 8  # a..f,s,t
    assert M31.owned_etale_atlas_presentation().groupoid == "weyl_e7"
    del_pezzo_m31 = M31.del_pezzo_quotient_presentation()
    assert del_pezzo_m31["coverage"] == "dense_open_nonhyperelliptic_of_open_M_3_1"
    hyp_m31 = M31.hyperelliptic_quotient_presentation()
    assert hyp_m31["coverage"] == "hyperelliptic_locus_of_open_M_3_1"
    Mbar31 = Mbar_gn(3, 1, base=k)
    mbar31_etale = Mbar31.etale_atlas()
    assert Mbar31.etale_atlas_gap() is None
    assert isinstance(mbar31_etale.domain(), DelPezzoCompactMarkedM3nAlgebraicSpace)
    assert mbar31_etale.has_equation_level_etale_certificate()
    assert mbar31_etale.covering_kind() == "del_pezzo_compact_universal_curve_finite_etale_cover"
    assert len(mbar31_etale.domain().affine_cover_sample()) == 3
    # Open M_{4,0}: owned Petri canonical (2,3)-CI dense open (2 invertible).
    M40 = M_gn(4, 0, base=k)
    m40_etale = M40.etale_atlas()
    assert M40.etale_atlas_gap() is None
    assert isinstance(m40_etale.domain(), AffineAlgebraicSpace)
    assert m40_etale.has_equation_level_etale_certificate()
    assert m40_etale.covering_kind() == "genus4_canonical_ci_affine_chart"
    assert M40.owned_etale_atlas_presentation().construction == "genus4_canonical_quadric_cubic_P3"
    assert len(m40_etale.domain().affine_cover()[0].ring().gens()) == 9  # c1..c9
    m40_pres = M40.genus4_canonical_quotient_presentation()
    assert m40_pres is not None
    assert m40_pres["coverage"] == "dense_open_nontrigonal_of_open_M_4"
    assert m40_pres["finite_etale_groupoid"] is False
    trig_pres = M40.trigonal_quotient_presentation()
    assert trig_pres is not None
    assert trig_pres["coverage"] == "trigonal_locus_of_open_M_4"
    assert len(trig_pres["covering_space"].affine_cover()[0].ring().gens()) == 8  # d1..d8
    # Proper Mbar_4: owned compact Petri ℙ⁹ (lazy sample).
    from dm_moduli_spike.geometry.stacks import Genus4CompactCanonicalAlgebraicSpace

    Mbar40 = Mbar_gn(4, 0, base=k)
    assert Mbar40.etale_atlas_gap() is None
    mbar40_etale = Mbar40.etale_atlas()
    assert isinstance(mbar40_etale.domain(), Genus4CompactCanonicalAlgebraicSpace)
    assert mbar40_etale.has_equation_level_etale_certificate()
    assert mbar40_etale.covering_kind() == "genus4_compact_canonical_ci_affine_cover"
    assert mbar40_etale.domain().affine_cover_cardinality() == 10
    assert len(mbar40_etale.domain().affine_cover_sample()) == 2
    mbar40_pres = Mbar40.genus4_canonical_quotient_presentation()
    assert mbar40_pres["coverage"] == "dense_open_nontrigonal_of_proper_Mbar_4"
    # g≥5 stays fail-closed with registry alts.
    M50 = M_gn(5, 0, base=k)
    gap_gen = M50.etale_atlas_gap()
    assert gap_gen is not None
    assert gap_gen["reason"] == "no_owned_affine_etale_presentation"
    alts_gen = gap_gen["alternate_proving_sets"]
    assert alts_gen[0]["name"] == "general_dm_moduli_etale_atlas"
    assert alts_gen[0]["parametric_open_m3n"] is True
    assert alts_gen[0]["parametric_compact_m3n"] is True
    assert alts_gen[0]["open_m30_del_pezzo"] is True
    assert alts_gen[0]["open_m30_hyperelliptic_locus"] is True
    assert alts_gen[0]["compact_m30_del_pezzo"] is True
    assert alts_gen[0]["compact_m30_hyperelliptic_locus"] is True
    assert alts_gen[0]["open_m40_canonical"] is True
    assert alts_gen[0]["open_m40_trigonal_locus"] is True
    assert alts_gen[0]["compact_m40_canonical"] is True
    assert alts_gen[0]["owned_registry_cardinality"] == 21
    assert (3, 0, False) in [tuple(t) for t in alts_gen[0]["owned_registry_type_keys"]]
    assert (3, 0, True) in [tuple(t) for t in alts_gen[0]["owned_registry_type_keys"]]
    assert (3, 1, False) in [tuple(t) for t in alts_gen[0]["owned_registry_type_keys"]]
    assert (3, 1, True) in [tuple(t) for t in alts_gen[0]["owned_registry_type_keys"]]
    assert (4, 0, False) in [tuple(t) for t in alts_gen[0]["owned_registry_type_keys"]]
    assert (4, 0, True) in [tuple(t) for t in alts_gen[0]["owned_registry_type_keys"]]
    assert alts_gen[0]["proper_m0n_owned_max"] == 8
    # Open M_{2,0}: owned Igusa / Rosenhain finite étale cover (2 invertible).
    M20_open = M_gn(2, 0, base=k)
    m20_etale = M20_open.etale_atlas()
    assert isinstance(m20_etale.domain(), AffineAlgebraicSpace)
    assert M20_open.etale_atlas_gap() is None
    assert m20_etale.has_equation_level_etale_certificate()
    assert m20_etale.covering_kind() == "igusa_binary_sextic_finite_etale_cover"
    assert m20_etale.is_quotient_presentation_atlas()
    assert M20_open.owned_etale_atlas_presentation().construction == "igusa_binary_sextic_PGL2"
    assert M20_open.owned_etale_atlas_presentation().groupoid == "igusa_s6"
    assert m20_etale.domain().affine_cover() != ()
    assert len(m20_etale.domain().affine_cover()[0].ring().gens()) == 3  # λ,μ,ν
    igusa_pres = M20_open.igusa_quotient_presentation()
    assert igusa_pres is not None
    assert igusa_pres["finite_etale_groupoid"] is True
    assert igusa_pres["group_order"] == 720
    assert igusa_pres["degree"] == 720
    assert igusa_pres["construction"] == "igusa_binary_sextic_PGL2"
    assert igusa_pres["coverage"] == "dense_open_of_open_M_2"
    assert igusa_pres["covering_space"] is m20_etale.domain()
    assert not M20_open.atlas().has_equation_level_etale_certificate()
    # Marked open M_{2,1} / M_{2,2}: Rosenhain universal curve / marked config.
    M21_open = M_gn(2, 1, base=k)
    m21_etale = M21_open.etale_atlas()
    assert M21_open.etale_atlas_gap() is None
    assert isinstance(m21_etale.domain(), AffineAlgebraicSpace)
    assert m21_etale.has_equation_level_etale_certificate()
    assert m21_etale.covering_kind() == "igusa_universal_curve_finite_etale_cover"
    assert m21_etale.is_quotient_presentation_atlas()
    assert M21_open.owned_etale_atlas_presentation().construction == "igusa_rosenhain_universal_curve"
    assert len(m21_etale.domain().affine_cover()[0].ring().gens()) == 5  # λ,μ,ν,x,y
    igusa_m21 = M21_open.igusa_quotient_presentation()
    assert igusa_m21 is not None
    assert igusa_m21["construction"] == "igusa_rosenhain_universal_curve"
    assert igusa_m21["coverage"] == "dense_open_of_open_M_2_1"
    M22_open = M_gn(2, 2, base=k)
    m22_etale = M22_open.etale_atlas()
    assert M22_open.etale_atlas_gap() is None
    assert m22_etale.has_equation_level_etale_certificate()
    assert m22_etale.covering_kind() == "igusa_marked_configuration_finite_etale_cover"
    assert M22_open.owned_etale_atlas_presentation().construction == "igusa_rosenhain_marked_configuration"
    assert len(m22_etale.domain().affine_cover()[0].ring().gens()) == 7  # λ,μ,ν + 2·(x,y)
    # Spec(Z) / char 2: owned Igusa types but 2 not a unit → structured gap.
    M20_Z = M_gn(2, 0, base=Z)
    gap_m20_Z = M20_Z.etale_atlas_gap()
    assert gap_m20_Z is not None
    assert gap_m20_Z["reason"] == "igusa_requires_two_invertible"
    assert gap_m20_Z["registry_owned_type"] is True
    assert not M20_Z.etale_atlas().has_equation_level_etale_certificate()
    assert M20_Z.igusa_quotient_presentation() is None
    Mbar20_Z = Mbar_gn(2, 0, base=Z)
    assert Mbar20_Z.etale_atlas_gap()["reason"] == "igusa_requires_two_invertible"
    assert Mbar20_Z.igusa_quotient_presentation() is None
    M21_Z = M_gn(2, 1, base=Z)
    assert M21_Z.etale_atlas_gap()["reason"] == "igusa_requires_two_invertible"
    Mbar21_Z = Mbar_gn(2, 1, base=Z)
    assert Mbar21_Z.etale_atlas_gap()["reason"] == "igusa_requires_two_invertible"
    assert Mbar21_Z.igusa_quotient_presentation() is None
    M20_char2 = M_gn(2, 0, base=spec(GF(2)))
    assert M20_char2.etale_atlas_gap()["reason"] == "igusa_requires_two_invertible"
    assert not M20_char2.etale_atlas().has_equation_level_etale_certificate()
    # Spec(Z) / char 2: owned del Pezzo M_{3,0} but 2 not a unit → structured gap.
    M30_Z = M_gn(3, 0, base=Z)
    gap_m30_Z = M30_Z.etale_atlas_gap()
    assert gap_m30_Z is not None
    assert gap_m30_Z["reason"] == "del_pezzo_requires_two_invertible"
    assert gap_m30_Z["registry_owned_type"] is True
    assert not M30_Z.etale_atlas().has_equation_level_etale_certificate()
    assert M30_Z.del_pezzo_quotient_presentation() is None
    M30_char2 = M_gn(3, 0, base=spec(GF(2)))
    assert M30_char2.etale_atlas_gap()["reason"] == "del_pezzo_requires_two_invertible"
    assert not M30_char2.etale_atlas().has_equation_level_etale_certificate()
    assert M30_Z.hyperelliptic_quotient_presentation() is None
    Mbar30_Z = Mbar_gn(3, 0, base=Z)
    assert Mbar30_Z.etale_atlas_gap()["reason"] == "del_pezzo_requires_two_invertible"
    assert Mbar30_Z.del_pezzo_quotient_presentation() is None
    assert Mbar30_Z.hyperelliptic_quotient_presentation() is None
    M31_Z = M_gn(3, 1, base=Z)
    assert M31_Z.etale_atlas_gap()["reason"] == "del_pezzo_requires_two_invertible"
    M40_Z = M_gn(4, 0, base=Z)
    assert M40_Z.etale_atlas_gap()["reason"] == "genus4_canonical_requires_two_invertible"
    assert M40_Z.genus4_canonical_quotient_presentation() is None
    Mbar40_Z = Mbar_gn(4, 0, base=Z)
    assert Mbar40_Z.etale_atlas_gap()["reason"] == "genus4_canonical_requires_two_invertible"

    # Owned proving-set stacks expose no gap record.
    assert XS.etale_atlas_gap() is None
    assert YS.etale_atlas_gap() is None
    assert M06.etale_atlas_gap() is None
    assert M07.etale_atlas_gap() is None
    assert M08.etale_atlas_gap() is None
    assert M12.etale_atlas_gap() is None
    assert M13.etale_atlas_gap() is None
    assert M14.etale_atlas_gap() is None
    assert Mbar12.etale_atlas_gap() is None
    assert Mbar13.etale_atlas_gap() is None
    assert Mbar14.etale_atlas_gap() is None
    assert Mbar04.etale_atlas_gap() is None
    assert Mbar05.etale_atlas_gap() is None
    assert Mbar06.etale_atlas_gap() is None
    assert Mbar07.etale_atlas_gap() is None
    assert Mbar08.etale_atlas_gap() is None
    assert Mbar11.etale_atlas_gap() is None
    assert M11_char2.etale_atlas_gap() is None
    assert Mbar11_char2.etale_atlas_gap() is None
    assert M12_char2.etale_atlas_gap() is None
    assert Mbar12_char2.etale_atlas_gap() is None
    assert Mbar13_char2.etale_atlas_gap() is None
    assert M20_open.etale_atlas_gap() is None
    assert M20.etale_atlas_gap() is None
    assert M21_open.etale_atlas_gap() is None
    assert M22_open.etale_atlas_gap() is None
    assert Mbar21.etale_atlas_gap() is None
    assert Mbar22.etale_atlas_gap() is None
    assert M30.etale_atlas_gap() is None
    assert Mbar30.etale_atlas_gap() is None
    assert M31.etale_atlas_gap() is None
    assert Mbar31.etale_atlas_gap() is None
    assert M40.etale_atlas_gap() is None
    assert Mbar40.etale_atlas_gap() is None

    # Product of owned charts: M_{1,1} × M_{0,4} both equation-level → product True.
    prod = ProductStack((XS, YS), base=k)
    prod_etale = prod.etale_atlas()
    assert prod_etale.is_etale()
    assert prod_etale.covering_kind() == "product_of_etale_atlases"
    assert isinstance(prod_etale.domain(), ProductStack)
    assert prod_etale.domain() is not prod
    assert prod_etale.domain() is not prod.atlas().domain()
    factor_eas = prod_etale.factor_atlases()
    assert factor_eas is not None
    assert len(factor_eas) == 2
    assert all(ea.is_etale() for ea in factor_eas)
    assert prod_etale.domain().factors() == (factor_eas[0].domain(), factor_eas[1].domain())
    assert not prod_etale.is_coarse_atlas()
    assert prod.atlas().covering_kind() == "product_of_coarse"
    assert not prod.atlas().is_etale()
    assert factor_eas[0].has_equation_level_etale_certificate() is True
    assert factor_eas[1].has_equation_level_etale_certificate() is True
    assert prod_etale.has_equation_level_etale_certificate()

    # Product of owned Kapranov Mbar_{0,5} with owned M_{0,4}: equation-level.
    prod_mbar05 = ProductStack((Mbar05, YS), base=k)
    prod_mbar05_etale = prod_mbar05.etale_atlas()
    assert prod_mbar05_etale.factor_atlases()[0].has_equation_level_etale_certificate() is True
    assert prod_mbar05_etale.factor_atlases()[1].has_equation_level_etale_certificate() is True
    assert prod_mbar05_etale.has_equation_level_etale_certificate()

    # Product fails closed when a factor still has a formal AtlasChart (unowned (g,n)).
    M50_formal = M_gn(5, 0, base=k)
    assert isinstance(M50_formal.etale_atlas().domain(), AtlasChart)
    prod_formal = ProductStack((M50_formal, YS), base=k)
    prod_formal_etale = prod_formal.etale_atlas()
    assert prod_formal_etale.factor_atlases()[0].has_equation_level_etale_certificate() is False
    assert prod_formal_etale.factor_atlases()[1].has_equation_level_etale_certificate() is True
    assert not prod_formal_etale.has_equation_level_etale_certificate()

    # Affine covering + finite G: equation-level étale certificate on U → [U/G].
    from sage.groups.perm_gps.permgroup_named import CyclicPermutationGroup

    U_aff = AffineAlgebraicSpace(spec(QQ))
    G2 = CyclicPermutationGroup(2)
    quot_aff = QuotientStack(U_aff, G2, _TrivialCoveringAction(G2, U_aff))
    aff_etale = quot_aff.etale_atlas()
    assert aff_etale.is_etale()
    assert aff_etale.domain() is U_aff
    assert aff_etale.domain() is quot_aff.covering_space()
    assert aff_etale.has_equation_level_etale_certificate()
    assert aff_etale.equation_level_etale()
    assert aff_etale.evidence().domain_affine_cover() == (spec(QQ),)
    assert aff_etale.covering_data()["has_equation_level_etale_certificate"] is True

    from sage.rings.integer_ring import ZZ

    S_prime = spec(ZZ)
    assert S_prime is not XS.base_scheme()
    pb = XS.pullback(S_prime)
    assert isinstance(pb, BaseChangeStack)
    assert isinstance(pb, PullbackStack)
    assert isinstance(pb, ModuliBaseChangeStack)
    assert PullbackStack is BaseChangeStack
    assert pb is not XS
    assert pb is BaseChangeStack(XS, S_prime)
    assert pb is ModuliBaseChangeStack(XS, S_prime)
    assert pb.original_stack() is XS
    assert pb.base_morphism() is S_prime
    assert pb.genus() == XS.genus()
    assert pb.marking_set() == XS.marking_set()
    assert pb.moduli_problem() is not XS.moduli_problem()
    assert pb.moduli_problem().base_scheme() is S_prime
    assert pb.new_base() is S_prime
    pi = pb.projection()
    assert pi.domain() is pb
    assert pi.codomain() is XS
    assert pi in Hom(pb, XS)
    pi2 = pb.structure_morphism_to_new_base()
    assert pi2 is pb.pullback_of_structure_morphism()
    assert pi2.domain() is pb
    assert pi2.codomain() is S_prime
    projs = pb.projections()
    assert len(projs) == 2
    assert projs[0].domain() is pb and projs[0].codomain() is XS
    assert projs[1].domain() is pb and projs[1].codomain() is S_prime
    corners = pb.square_corners()
    assert corners == (pb, XS, S_prime, XS.base_scheme())
    assert pb is BaseChangeStack(XS, S_prime)

    # Pullback universal property: mediating morphism recovers legs via π₁, π₂.
    Y = Stack(k, name="Y", axioms=frozenset({"FiniteType"}))
    a = StackMorphism(Y, XS, kind="test_leg_to_X")
    b = StackMorphism(Y, S_prime, kind="test_leg_to_Sprime")
    m = pb.mediating_morphism(a, b)
    assert isinstance(m, PullbackMediatingMorphism)
    assert m.domain() is Y
    assert m.codomain() is pb
    assert m.recorded_leg_to_original() is a
    assert m.recorded_leg_to_new_base() is b
    assert m.recovers_legs()
    c1 = m.composed_with_projection()
    c2 = m.composed_with_structure_morphism()
    assert c1.domain() is Y and c1.codomain() is XS
    assert c2.domain() is Y and c2.codomain() is S_prime
    two_cells = m.projection_2_isomorphisms()
    assert len(two_cells) == 2
    assert isinstance(two_cells[0], Stack2Isomorphism)
    assert isinstance(two_cells[1], Stack2Isomorphism)


def test_formally_etale_proving_set_expanded():
    r"""Owned equation-level certificates: identity, localization opens, finite étale."""
    from sage.rings.finite_rings.finite_field_constructor import GF
    from sage.rings.integer_ring import ZZ
    from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

    from dm_moduli_spike.categories.base import AffineScheme
    from dm_moduli_spike.geometry.stacks import FormallyEtaleSchemeCertificate

    # Identity Spec(R)→Spec(R)
    id_cert = FormallyEtaleSchemeCertificate.identity_affine(spec(QQ))
    assert id_cert.is_formally_etale()
    assert id_cert.kahler_differentials_vanish()
    assert id_cert.reason() == "identity_ring_map_isomorphism"
    assert id_cert.domain_scheme() is spec(QQ)

    # Standard open D(f)→Spec(R) via localization (QQ[x]_x → QQ[x])
    R = PolynomialRing(QQ, "x")
    x = R.gen()
    loc = FormallyEtaleSchemeCertificate.localization_open(R, x)
    assert loc.is_formally_etale()
    assert loc.is_open_immersion()
    assert loc.kahler_differentials_vanish()
    assert loc.localizing_element() == x
    assert loc.reason() == "localization_standard_open_immersion"
    assert isinstance(loc.domain_scheme(), AffineScheme)
    assert isinstance(loc.codomain_scheme(), AffineScheme)
    assert loc.codomain_scheme() is AffineScheme(R)
    # AffineScheme.standard_open matches the localization domain.
    open_spec = AffineScheme(R).standard_open(x)
    assert open_spec is loc.domain_scheme()

    # ZZ localization at 2
    zz_loc = FormallyEtaleSchemeCertificate.localization_open(ZZ, 2)
    assert zz_loc.is_formally_etale() and zz_loc.is_open_immersion()
    assert ZZ(2).is_unit() is False
    assert zz_loc.domain_scheme().ring()(2).is_unit()

    # Finite étale Spec(k[t]/(t^2-1)) → Spec(k) over QQ and GF(7)
    A = PolynomialRing(QQ, "t")
    t = A.gen()
    fin = FormallyEtaleSchemeCertificate.separable_finite_etale(QQ, t**2 - 1)
    assert fin.is_formally_etale()
    assert fin.is_finite_etale()
    assert fin.kahler_differentials_vanish()
    assert fin.reason() == "separable_finite_etale_jacobian"
    assert fin.separable_polynomial() == t**2 - 1

    k = GF(7)
    Ak = PolynomialRing(k, "u")
    u = Ak.gen()
    fin_ff = FormallyEtaleSchemeCertificate.separable_finite_etale(k, u**2 - 1)
    assert fin_ff.is_finite_etale() and fin_ff.is_formally_etale()

    # Fail-closed: inseparable polynomial rejected
    try:
        FormallyEtaleSchemeCertificate.separable_finite_etale(GF(2), PolynomialRing(GF(2), "v").gen() ** 2)
    except AssertionError:
        pass
    else:
        raise AssertionError("expected AssertionError for inseparable polynomial over GF(2)")


def test_arbitrary_marking_set():
    I = FiniteEnumeratedSet(("p", "q", "r", "s"))
    graphs = StableGraphs(0, I)
    assert graphs.marking_set() == ("p", "q", "r", "s")
    G = graphs.from_vertices(
        genera=(0, 0),
        markings=(("p", "q"), ("r", "s")),
        edges=((0, 1),),
    )
    assert G.genus() == 0
    assert set(graphs.marking_set()) == {"p", "q", "r", "s"}
    M = M_gI(0, I, base=spec(QQ))
    assert M.marking_set() == ("p", "q", "r", "s")


def test_gamma_objects_and_hom_domain_are_stable_graphs():
    Gamma = StableGraphCategory(1, 1)
    objects = Gamma.objects()
    assert objects is StableGraphs(1, 1)
    smooth = next(iter(objects))
    assert smooth.parent() is StableGraphs(1, 1)
    end = Gamma.end(smooth)
    assert end.domain() is smooth or end.domain() == smooth
    assert end.codomain() == smooth

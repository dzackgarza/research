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
    # Mbar_{0,5}: blowup / del Pezzo cover not owned — fail-closed with named gap.
    Mbar05 = Mbar_gn(0, 5, base=k)
    assert isinstance(Mbar05.etale_atlas().domain(), AtlasChart)
    assert not Mbar05.etale_atlas().has_equation_level_etale_certificate()
    mbar05_gap = Mbar05.etale_atlas_gap()
    assert mbar05_gap is not None
    assert mbar05_gap["reason"] == "mbar_0_5_needs_blowup_affine_cover"
    assert mbar05_gap["alternate_proving_sets"][0]["name"] == "kapranov_blowup_P2"

    # General (g,n) and char-2 (1,1): remain fail-closed.
    M12 = M_gn(1, 2, base=k)
    assert isinstance(M12.etale_atlas().domain(), AtlasChart)
    assert not M12.etale_atlas().has_equation_level_etale_certificate()
    m12_gap = M12.etale_atlas_gap()
    assert m12_gap is not None
    assert m12_gap["reason"] == "m_1_2_needs_universal_curve_second_mark"

    # Char 2: Legendre form unavailable — M_{1,1} / Mbar_{1,1} fail-closed formal chart.
    from sage.rings.finite_rings.finite_field_constructor import GF

    M11_char2 = M_gn(1, 1, base=spec(GF(2)))
    assert isinstance(M11_char2.etale_atlas().domain(), AtlasChart)
    assert not M11_char2.etale_atlas().has_equation_level_etale_certificate()
    assert M11_char2.legendre_quotient_presentation() is None
    char2_gap = M11_char2.etale_atlas_gap()
    assert char2_gap is not None
    assert char2_gap["reason"] == "legendre_requires_2_invertible"
    alt_names = {a["name"] for a in char2_gap["alternate_proving_sets"]}
    assert alt_names == {"hesse_gamma3", "weierstrass_gm_quotient", "igusa_ordinary_a6_chart"}
    Mbar11_char2 = Mbar_gn(1, 1, base=spec(GF(2)))
    assert isinstance(Mbar11_char2.etale_atlas().domain(), AtlasChart)
    assert not Mbar11_char2.etale_atlas().has_equation_level_etale_certificate()
    assert Mbar11_char2.legendre_quotient_presentation() is None
    assert Mbar11_char2.etale_atlas_gap()["reason"] == "legendre_requires_2_invertible"

    # Owned proving-set stacks expose no gap record.
    assert XS.etale_atlas_gap() is None
    assert YS.etale_atlas_gap() is None
    assert Mbar04.etale_atlas_gap() is None
    assert Mbar11.etale_atlas_gap() is None

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

    # Product fails closed when a factor still has a formal AtlasChart.
    prod_formal = ProductStack((M12, YS), base=k)
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

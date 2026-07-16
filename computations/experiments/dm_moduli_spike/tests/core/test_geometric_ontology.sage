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
    assert q_etale.domain() is not open_quot
    assert q_etale.covering_kind() == "quotient_cover"
    assert q_etale.domain_is_representable()
    assert q_etale.evidence() is not None
    assert q_etale.evidence().dm_diagonal_unramified_stamp()
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
    r"""Aut(Γ) acts on ∏ M by factor permutation; identity acts as id."""
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
    factors = tuple(M_gI(graph.vertex_genus(v), graph.flags_at(v), base=k) for v in range(2))
    product = ProductStack(factors, base=k)
    aut = graph.automorphism_group(on="half_edges")
    action = AutProductStackAction(aut, product, graph)
    identity = aut.one()
    swap = next(g for g in aut if g.order() == 2)

    assert action.factor_permutation_of(identity) == (0, 1)
    assert action.act(identity) is product
    assert action(identity) is product
    assert action._act_(identity) is product

    assert action.factor_permutation_of(swap) == (1, 0)
    swapped = action.act(swap)
    assert isinstance(swapped, ProductStack)
    assert swapped is not product
    assert swapped.factors() == (factors[1], factors[0])
    assert action.permute_factors(0) == (factors[1], factors[0])

    iso = action.induced_isomorphism(swap)
    assert iso.domain() is product
    assert iso.codomain() is swapped

    quot = QuotientStack(product, aut, action)
    assert quot.act_on_covering(identity) is product
    assert quot.act_on_covering(swap) is swapped
    assert quot.etale_atlas().domain() is product


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

    Delta = XS.diagonal()
    assert Delta.domain() is XS
    assert Delta.codomain() == XS.fiber_product(XS)

    from dm_moduli_spike.geometry.stacks import (
        AlgebraicSpace,
        AtlasChart,
        AtlasEvidence,
        AtlasMorphism,
        BaseChangeStack,
        ModuliBaseChangeStack,
        PullbackStack,
    )

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
    assert atlas.covering_data()["covering_kind"] == "coarse_moduli"

    etale = XS.etale_atlas()
    assert isinstance(etale, AtlasMorphism)
    assert etale.is_etale()
    assert isinstance(etale.domain(), AtlasChart)
    assert etale.domain().is_etale_chart()
    assert etale.domain() is not XS
    assert etale.domain() is not XS.coarse_space()
    assert etale.codomain() is XS
    assert etale in Hom(etale.domain(), XS)
    assert etale.is_covering()
    assert etale.domain_is_representable()
    assert etale.covering_kind() == "etale_atlas_chart"
    ev = etale.evidence()
    assert isinstance(ev, AtlasEvidence)
    assert ev.etale_stamp()
    assert ev.representable_domain()
    assert ev.dm_diagonal_unramified_stamp()
    assert ev.diagonal() is not None
    assert ev.diagonal().domain() is XS
    assert ev.diagonal().codomain() == XS.fiber_product(XS)
    assert etale.covering_data()["dm_diagonal_unramified_stamp"] is True
    assert etale.covering_data()["diagonal"] is ev.diagonal()

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

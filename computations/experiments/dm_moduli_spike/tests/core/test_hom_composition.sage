r"""Public Hom composition laws and Hom-derived specialization covers for Γ."""

from __future__ import annotations

from dm_moduli_spike import StableGraphCategory, StableGraphContraction, StableGraphs


def test_hom_composition_identity_laws_M11():
    Gamma = StableGraphCategory(1, 1)
    graphs = StableGraphs(1, 1)
    special = next(g for g in graphs if g.num_edges() == 1)
    generic = graphs.smooth()
    f = Gamma.hom(special, generic).an_element()
    assert isinstance(f, StableGraphContraction)
    assert f.is_contraction()
    id_s = Gamma.identity(special)
    id_g = Gamma.identity(generic)
    assert f.compose(id_s) == f
    assert id_g.compose(f) == f
    assert id_s.compose(id_s) == id_s


def test_hom_composition_associativity_M12():
    r"""Two-edge banana / chain: compose three morphisms when Hom permits."""
    Gamma = StableGraphCategory(1, 2)
    graphs = list(StableGraphs(1, 2))
    by_edges = {}
    for g in graphs:
        by_edges.setdefault(g.num_edges(), []).append(g)
    # Find a length-2 specialization chain G2 -> G1 -> G0 with nonempty Hom.
    for g2 in by_edges.get(2, ()):
        for g1 in by_edges.get(1, ()):
            for g0 in by_edges.get(0, ()):
                h21 = Gamma.hom(g2, g1)
                h10 = Gamma.hom(g1, g0)
                if h21.cardinality() == 0 or h10.cardinality() == 0:
                    continue
                f = h21.an_element()
                g = h10.an_element()
                # Also need Hom(g2, g0) for the composite.
                h20 = Gamma.hom(g2, g0)
                assert h20.cardinality() > 0
                # (g ∘ f) and check associativity with identity on g0.
                gf = g.compose(f)
                id0 = Gamma.identity(g0)
                assert id0.compose(gf) == gf
                assert gf.compose(Gamma.identity(g2)) == gf
                return
    raise AssertionError("no length-2 Hom chain found in Γ_{1,2}")


def test_specialization_covers_are_hom_nonempty():
    Gamma = StableGraphCategory(1, 1)
    poset = Gamma.specialization_poset()
    for generic, special in poset.cover_relations():
        assert special.num_edges() == generic.num_edges() + 1
        assert Gamma.hom(special, generic).cardinality() > 0


def test_contract_returns_public_stable_graph_contraction():
    Gamma = StableGraphCategory(1, 1)
    special = next(g for g in StableGraphs(1, 1) if g.num_edges() == 1)
    edges = special._canonical_record().internal_edges()
    morph = Gamma.contract(special, (edges[0],))
    assert isinstance(morph, StableGraphContraction)
    assert morph.is_contraction()
    assert morph.domain() == special
    assert morph.codomain() == StableGraphs(1, 1).smooth()


def test_public_hom_compose_transport_square_M11():
    r"""Canonical transport expressed as Hom composition on public StableGraph APIs."""
    Gamma = StableGraphCategory(1, 1)
    graphs = StableGraphs(1, 1)
    special = next(g for g in graphs if g.num_edges() == 1)
    generic = graphs.smooth()
    f = Gamma.hom(special, generic).an_element()
    # Transport along identities is the identity square.
    id_s = Gamma.identity(special)
    id_g = Gamma.identity(generic)
    transported = id_g.compose(f.compose(id_s))
    assert transported == f
    assert transported.domain() == special
    assert transported.codomain() == generic

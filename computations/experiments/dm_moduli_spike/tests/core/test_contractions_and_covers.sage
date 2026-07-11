r"""Contraction morphisms and the covers they witness."""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel, StableCurveTypes
from dm_moduli_spike.objects.contractions import contract_edges


def test_loop_contraction_adds_one_to_genus():
    types = StableCurveTypes(1, 1)
    loop = types.from_vertices(genera=(0,), markings=((1,),), edges=((0, 0),))
    edge = loop.internal_edges()[0]
    image, contraction = loop.contract(edge)
    assert image.is_smooth()
    assert image.total_genus() == 1
    assert image.vertex_genera() == (1,)
    assert contraction.domain() == loop
    assert contraction.codomain() == image
    assert contraction.num_contracted_edges() == 1


def test_nonloop_contraction_merges_and_sums_genera():
    types = StableCurveTypes(1, 2)
    gamma = types.from_vertices(genera=(1, 0), markings=((), (1, 2)), edges=((0, 1),))
    edge = gamma.internal_edges()[0]
    image, contraction = gamma.contract(edge)
    assert image.is_smooth()
    assert image.total_genus() == 1
    assert image.vertex_genera() == (1,)
    assert len(contraction.vertex_fibres()) == 1
    assert contraction.vertex_fibres()[0] == frozenset({0, 1})


def test_every_contraction_preserves_total_genus_and_stability():
    for g, n in [(0, 4), (1, 1), (0, 5), (1, 2), (2, 0), (2, 1)]:
        model = DMCompactificationModel(g, n)
        for level in model.stratification().curve_type_levels():
            for gamma in level:
                for edge in gamma.internal_edges():
                    image, _ = gamma.contract(edge)
                    assert image.total_genus() == gamma.total_genus()
                    assert image.is_stable()
                    assert image.num_edges() == gamma.num_edges() - 1


def test_covers_change_edge_count_by_one_and_carry_a_valid_witness():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification()
    for generic, special in stratification.covers():
        assert special.codimension() == generic.codimension() + 1
    for witness in stratification.contraction_witnesses():
        assert witness.num_contracted_edges() == 1
        assert witness.codomain().num_edges() == witness.domain().num_edges() - 1
        # the witnessed contraction really lands on its recorded codomain
        image, _ = witness.domain().contract(witness.contracted_edges()[0])
        assert image == witness.codomain()


def test_contraction_composition_contracts_the_union_of_edges():
    types = StableCurveTypes(0, 5)
    # A chain of two edges: three genus-0 vertices in a path.
    gamma = types.from_vertices(
        genera=(0, 0, 0),
        markings=((1, 2), (3,), (4, 5)),
        edges=((0, 1), (1, 2)),
    )
    edges = gamma.internal_edges()
    _, first = gamma.contract(edges[0])
    # contract the surviving edge of the intermediate graph
    second_edge = first.codomain().internal_edges()[0]
    _, second = first.codomain().contract(second_edge)
    composite = first.compose(second)
    assert composite.domain() == gamma
    assert composite.num_contracted_edges() == 2
    assert composite.codomain().is_smooth()
    # contracting both edges directly agrees with the composite
    direct, _ = contract_edges(gamma, edges)
    assert direct == composite.codomain()

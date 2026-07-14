r"""Tier-4 internal consistency: Hasse diagrams, order, rank/dimension, closure duality."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.testing_support.support.poset_oracle import specialization_poset


@pytest.mark.parametrize(
    "g,n",
    [
        (0, 4),
        (1, 1),
        (1, 2),
    ],
)
def test_hasse_diagram_equals_elementary_contraction_relation(g, n):
    poset = specialization_poset(g, n)

    by_key = {stratum.canonical_key(): stratum for stratum in poset}
    expected_covers: set[tuple[object, object]] = set()

    for special in poset:
        delta_graph = special.canonical_representative()
        for edge in delta_graph.internal_edges():
            generic_type, _ = delta_graph.contract(edge)
            generic = by_key[generic_type.canonical_key()]
            expected_covers.add((generic, special))

    actual_covers = set(map(tuple, poset.cover_relations()))
    assert actual_covers == expected_covers


def test_order_relation_is_contraction_reachability():
    poset = specialization_poset(2, 0)

    for generic in poset:
        for special in poset:
            reachable = special.admits_contraction_to(generic)
            assert poset.is_lequal(generic, special) == reachable


@pytest.mark.parametrize(
    "g,n",
    [(0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (2, 0)],
)
def test_rank_codimension_and_dimension_on_every_stratum(g, n):
    poset = specialization_poset(g, n)
    Gamma = StableGraphCategory(g, n)

    assert poset.is_graded()

    for stratum in poset:
        graph = stratum  # specialization_poset elements are StableGraph classes
        edge_count = graph.num_edges()

        assert poset.rank(stratum) == edge_count
        assert Gamma.codimension(stratum) == edge_count
        assert Gamma.stratum_dimension(stratum) == 3 * g - 3 + n - edge_count

        local_dimension = sum(
            3 * graph.vertex_genus(vertex) - 3 + graph.valence(vertex)
            for vertex in range(graph.num_vertices())
        )
        assert Gamma.stratum_dimension(stratum) == local_dimension


def test_poset_covers_reference_stable_graph_classes():
    from dm_moduli_spike.objects.stable_graphs import StableGraphs

    Gamma = StableGraphCategory(1, 2)
    poset = Gamma.specialization_poset()
    by_curve_type = {stratum: stratum for stratum in poset}
    level_representatives = {gamma.canonical_key(): gamma for gamma in StableGraphs(1, 2)}
    for generic, special in poset.cover_relations():
        assert generic is level_representatives[generic.canonical_key()]
        assert special is level_representatives[special.canonical_key()]
        assert [by_curve_type[generic], by_curve_type[special]] in poset.cover_relations()


def test_closure_and_specialization_orders_are_identity_dual():
    Gamma = StableGraphCategory(1, 2)

    specialization = Gamma.specialization_poset()
    closure = Gamma.closure_poset()

    assert set(specialization) == set(closure)

    for left in specialization:
        for right in specialization:
            assert specialization.is_lequal(left, right) == closure.is_lequal(right, left)

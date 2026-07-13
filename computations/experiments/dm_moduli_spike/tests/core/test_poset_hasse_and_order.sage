r"""Tier-4 internal consistency: Hasse diagrams, order, rank/dimension, closure duality."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import DMCompactificationModel

from tests.support.poset_oracle import specialization_poset


@pytest.mark.parametrize(
    "g,n",
    [
        (0, 4),
        (1, 1),
        (1, 2),
    ],
)
def test_hasse_diagram_equals_elementary_contraction_relation(g, n):
    stratification = DMCompactificationModel(g, n).stratification()
    poset = stratification.specialization_poset()

    by_key = {stratum.curve_type().canonical_key(): stratum for stratum in poset}
    expected_covers: set[tuple[object, object]] = set()

    for special in poset:
        delta_graph = special.curve_type().canonical_representative()
        for edge in delta_graph.internal_edges():
            generic_type, _ = delta_graph.contract(edge)
            generic = by_key[generic_type.canonical_key()]
            expected_covers.add((generic, special))

    actual_covers = set(map(tuple, poset.cover_relations()))
    assert actual_covers == expected_covers


def test_order_relation_is_contraction_reachability():
    stratification = DMCompactificationModel(2, 0).stratification()
    poset = stratification.specialization_poset()

    for generic in poset:
        for special in poset:
            reachable = special.curve_type().admits_contraction_to(generic.curve_type())
            assert poset.is_lequal(generic, special) == reachable


@pytest.mark.parametrize(
    "g,n",
    [(0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (2, 0)],
)
def test_rank_codimension_and_dimension_on_every_stratum(g, n):
    poset = specialization_poset(g, n)

    assert poset.is_graded()

    for stratum in poset:
        gamma = stratum.curve_type()
        graph = gamma.canonical_representative()
        edge_count = gamma.num_edges()

        assert poset.rank(stratum) == edge_count
        assert stratum.codimension() == edge_count
        assert stratum.dimension() == 3 * g - 3 + n - edge_count

        local_dimension = sum(
            3 * graph.vertex_genus(vertex) - 3 + graph.valence(vertex)
            for vertex in graph.vertices()
        )
        assert stratum.dimension() == local_dimension


def test_poset_covers_reference_level_representatives():
    stratification = DMCompactificationModel(1, 2).stratification()
    poset = stratification.specialization_poset()
    by_curve_type = {stratum.curve_type(): stratum for stratum in poset}
    level_representatives = {
        gamma.canonical_key(): gamma
        for level in stratification.curve_type_levels()
        for gamma in level
    }
    for generic, special in stratification.covers():
        generic_type = generic.curve_type()
        special_type = special.curve_type()
        assert generic_type is level_representatives[generic_type.canonical_key()]
        assert [by_curve_type[generic_type], by_curve_type[special_type]] in poset.cover_relations()


def test_closure_and_specialization_orders_are_identity_dual():
    stratification = DMCompactificationModel(1, 2).stratification()

    specialization = stratification.specialization_poset()
    closure = stratification.closure_poset()

    assert set(specialization) == set(closure)

    for left in specialization:
        for right in specialization:
            assert specialization.is_lequal(left, right) == closure.is_lequal(right, left)

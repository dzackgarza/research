r"""CI-tier Hasse diagram checks on larger stratifications."""

from __future__ import annotations

import pytest

from dm_moduli_spike.testing_support.support.poset_oracle import specialization_poset

pytestmark = pytest.mark.ci


@pytest.mark.parametrize(
    "g,n",
    [
        (0, 5),
        (0, 6),
        (2, 0),
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

r"""Tier-1 literature oracle: published complete posets for `\overline{\mathcal M}_{1,2}` and `\overline{\mathcal M}_{2,0}`.

Primary evidence: Markwig Example 2.2 / Figure 2 and Example 2.7 / Figure 5 (`M_{1,2}`);
Chan Figure 3 (`M_{2,0}`) graph-to-stratum contraction incidences.

Young-diagram isomorphisms are tier-2 checksums only.
"""

from __future__ import annotations

import pytest

from collections import Counter

from sage.all import posets

from dm_moduli_spike import DMCompactificationModel
from dm_moduli_spike.objects.edge_orbits import contraction_target_multiset
from tests.support.fixtures import CHAN_M20_COVERS, m11_types, m12_types, m20_types
from tests.support.poset_oracle import specialization_poset

pytestmark = pytest.mark.ci


def test_M11_is_two_element_chain():
    assert specialization_poset(1, 1).is_isomorphic(posets.ChainPoset(2))


def test_M11_unique_cover_is_loop_contraction():
    stratification = DMCompactificationModel(1, 1).stratification()
    poset = stratification.specialization_poset()
    smooth, nodal = m11_types(stratification)

    assert poset.cover_relations() == [[smooth, nodal]]

    nodal_graph = nodal.curve_type().canonical_representative()
    contractions = list(nodal_graph.internal_edges())
    assert len(contractions) == 1
    _, contraction = nodal_graph.contract(contractions[0])
    assert contraction.target_type() == smooth.curve_type()


def test_M12_exact_semantic_cover_relations():
    stratification = DMCompactificationModel(1, 2).stratification()
    poset = stratification.specialization_poset()
    types = m12_types(stratification)

    expected_covers = {
        (types["A"], types["B"]),
        (types["A"], types["C"]),
        (types["B"], types["D"]),
        (types["B"], types["E"]),
        (types["C"], types["D"]),
    }

    assert set(map(tuple, poset.cover_relations())) == expected_covers


def test_M20_exact_cover_relations_from_chan_figure():
    stratification = DMCompactificationModel(2, 0).stratification()
    types = m20_types(stratification)

    expected_covers = {
        (types[child], types[parent])
        for parent, children in CHAN_M20_COVERS.items()
        for child in children
    }

    poset = stratification.specialization_poset()
    assert set(map(tuple, poset.cover_relations())) == expected_covers


def test_M12_young_diagram_poset_checksum():
    r"""Secondary checksum only — not the primary literature fact."""
    actual = specialization_poset(1, 2)
    expected = posets.YoungDiagramPoset([3, 2])
    assert actual.is_isomorphic(expected)


def test_M20_young_diagram_poset_checksum():
    r"""Secondary checksum only — not the primary literature fact."""
    actual = specialization_poset(2, 0)
    expected = posets.YoungDiagramPoset([4, 3])
    assert actual.is_isomorphic(expected)


def test_M12_parallel_edges_give_two_contraction_witnesses():
    stratification = DMCompactificationModel(1, 2).stratification()
    types = m12_types(stratification)

    multiplicities = Counter(
        target.canonical_key() for target, _size in contraction_target_multiset(types["E"].curve_type())
    )
    assert multiplicities == Counter({types["B"].curve_type().canonical_key(): 1})


def test_M20_contraction_multiplicities():
    stratification = DMCompactificationModel(2, 0).stratification()
    types = m20_types(stratification)

    assert Counter(
        target.canonical_key() for target, _size in contraction_target_multiset(types["I"].curve_type())
    ) == Counter({types["III"].curve_type().canonical_key(): 1})
    assert Counter(
        target.canonical_key() for target, _size in contraction_target_multiset(types["II"].curve_type())
    ) == Counter(
        {
            types["III"].curve_type().canonical_key(): 1,
            types["IV"].curve_type().canonical_key(): 1,
        }
    )
    assert Counter(
        target.canonical_key() for target, _size in contraction_target_multiset(types["III"].curve_type())
    ) == Counter({types["V"].curve_type().canonical_key(): 1})

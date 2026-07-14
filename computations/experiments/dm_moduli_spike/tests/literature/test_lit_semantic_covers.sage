r"""Tier-1 literature oracle: published complete posets for `\overline{\mathcal M}_{1,2}` and `\overline{\mathcal M}_{2,0}`.

Primary evidence: Markwig Example 2.2 / Figure 2 and Example 2.7 / Figure 5 (`M_{1,2}`);
Chan Figure 3 (`M_{2,0}`) graph-to-stratum contraction incidences.

Young-diagram isomorphisms are tier-2 checksums only.
"""

from __future__ import annotations

from collections import Counter

import pytest
from sage.all import posets


from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.testing_support.support.fixtures import CHAN_M20_COVERS, m11_types, m12_types, m20_types
from dm_moduli_spike.testing_support.support.poset_oracle import specialization_poset

pytestmark = pytest.mark.ci


def test_M11_is_two_element_chain():
    r"""Markwig Ex. 2.2 / Fig. 2: `\overline{\mathcal M}_{1,1}` is a two-element chain."""
    assert specialization_poset(1, 1).is_isomorphic(posets.ChainPoset(2))


def test_M11_unique_cover_is_loop_contraction():
    r"""Markwig Ex. 2.2 / Fig. 2: the unique cover contracts the loop edge."""
    poset = StableGraphCategory(1, 1).specialization_poset()
    smooth, nodal = m11_types()

    assert poset.cover_relations() == [[smooth, nodal]]

    nodal_graph = nodal._canonical_record()
    contractions = list(nodal_graph.internal_edges())
    assert len(contractions) == 1
    _, contraction = nodal_graph.contract(contractions[0])
    assert contraction.target_type() == smooth


def test_M12_exact_semantic_cover_relations():
    r"""Markwig Ex. 2.2 / Fig. 2: primary evidence is the exact cover set for `\overline{\mathcal M}_{1,2}`."""
    poset = StableGraphCategory(1, 2).specialization_poset()
    types = m12_types()

    expected_covers = {
        (types["A"], types["B"]),
        (types["A"], types["C"]),
        (types["B"], types["D"]),
        (types["B"], types["E"]),
        (types["C"], types["D"]),
    }

    assert set(map(tuple, poset.cover_relations())) == expected_covers


def test_M20_exact_cover_relations_from_chan_figure():
    r"""Chan Fig. 3: primary evidence is the exact cover set for `\overline{\mathcal M}_{2,0}`."""
    types = m20_types()

    # CHAN_M20_COVERS maps generic -> special covers in the specialization order.
    expected_covers = {
        (types[generic], types[special])
        for generic, specials in CHAN_M20_COVERS.items()
        for special in specials
    }

    poset = StableGraphCategory(2, 0).specialization_poset()
    assert set(map(tuple, poset.cover_relations())) == expected_covers


def test_M12_young_diagram_poset_checksum():
    r"""Tier-2 checksum only (Markwig Ex. 2.2 / Fig. 2 Young diagram `[3,2]`) — not primary literature evidence."""
    actual = specialization_poset(1, 2)
    expected = posets.YoungDiagramPoset([3, 2])
    assert actual.is_isomorphic(expected)


def test_M20_young_diagram_poset_checksum():
    r"""Tier-2 checksum only (Chan Fig. 3 Young diagram `[4,3]`) — not primary literature evidence."""
    actual = specialization_poset(2, 0)
    expected = posets.YoungDiagramPoset([4, 3])
    assert actual.is_isomorphic(expected)


def test_M12_parallel_edges_give_two_contraction_witnesses():
    r"""Markwig Ex. 2.2 / Fig. 2: type E parallel edges contribute orbit multiplicity two."""
    types = m12_types()

    multiplicities = Counter(
        target.canonical_key() for target, _size in types["E"].contraction_target_multiset()
    )
    assert multiplicities == Counter({types["B"].canonical_key(): 1})


def test_M20_contraction_multiplicities():
    r"""Chan Fig. 3: orbit multiplicities for types I–III contraction targets."""
    types = m20_types()

    assert Counter(
        target.canonical_key() for target, _size in types["I"].contraction_target_multiset()
    ) == Counter({types["III"].canonical_key(): 1})
    assert Counter(
        target.canonical_key() for target, _size in types["II"].contraction_target_multiset()
    ) == Counter(
        {
            types["III"].canonical_key(): 1,
            types["IV"].canonical_key(): 1,
        }
    )
    assert Counter(
        target.canonical_key() for target, _size in types["III"].contraction_target_multiset()
    ) == Counter({types["V"].canonical_key(): 1})

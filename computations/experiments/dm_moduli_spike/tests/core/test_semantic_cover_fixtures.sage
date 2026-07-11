r"""Named semantic fixtures: Mbar(1,1), Mbar(1,2), Mbar(2), and multiplicities."""

from __future__ import annotations

from collections import Counter

from sage.all import posets

from dm_moduli_spike import DMCompactificationModel
from tests.support.fixtures import m11_types, m12_types, m20_types
from tests.support.poset_oracle import specialization_poset


def contraction_target_multiplicities(gamma):
    return Counter(
        contraction.codomain().canonical_key()
        for contraction in gamma.elementary_contractions()
    )


def test_M11_is_two_element_chain():
    assert specialization_poset(1, 1).is_isomorphic(posets.ChainPoset(2))


def test_M11_unique_cover_is_loop_contraction():
    stratification = DMCompactificationModel(1, 1).stratification()
    poset = stratification.specialization_poset()
    smooth, nodal = m11_types(stratification)

    assert poset.cover_relations() == [[smooth, nodal]]

    contractions = nodal.curve_type().elementary_contractions()
    assert len(contractions) == 1
    assert contractions[0].codomain() == smooth.curve_type()


def test_M12_is_young_diagram_poset_3_2():
    actual = specialization_poset(1, 2)
    expected = posets.YoungDiagramPoset([3, 2])
    assert actual.is_isomorphic(expected)


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


def test_M20_is_young_diagram_poset_4_3():
    actual = specialization_poset(2, 0)
    expected = posets.YoungDiagramPoset([4, 3])
    assert actual.is_isomorphic(expected)


def test_M20_exact_cover_relations():
    stratification = DMCompactificationModel(2, 0).stratification()
    poset = stratification.specialization_poset()
    types = m20_types(stratification)

    expected_covers = {
        (types["VII"], types["V"]),
        (types["VII"], types["VI"]),
        (types["V"], types["III"]),
        (types["V"], types["IV"]),
        (types["VI"], types["IV"]),
        (types["III"], types["I"]),
        (types["III"], types["II"]),
        (types["IV"], types["II"]),
    }

    assert set(map(tuple, poset.cover_relations())) == expected_covers


def test_M12_parallel_edges_give_two_contraction_witnesses():
    stratification = DMCompactificationModel(1, 2).stratification()
    types = m12_types(stratification)

    multiplicities = contraction_target_multiplicities(types["E"].curve_type())
    assert multiplicities == Counter({types["B"].curve_type().canonical_key(): 2})


def test_M20_contraction_multiplicities():
    stratification = DMCompactificationModel(2, 0).stratification()
    types = m20_types(stratification)

    assert contraction_target_multiplicities(types["I"].curve_type()) == Counter(
        {types["III"].curve_type().canonical_key(): 3}
    )
    assert contraction_target_multiplicities(types["II"].curve_type()) == Counter(
        {
            types["III"].curve_type().canonical_key(): 1,
            types["IV"].curve_type().canonical_key(): 2,
        }
    )
    assert contraction_target_multiplicities(types["III"].curve_type()) == Counter(
        {types["V"].curve_type().canonical_key(): 2}
    )

r"""Induced subposets from arbitrary stable-type subsets."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import induced_specialization_poset, strata_by_codimension

pytestmark = pytest.mark.ci


def test_intermediate_deletion_adds_direct_cover():
    smooth = StableGraphs(2, 1).smooth()
    codim_two = strata_by_codimension(2, 1)[2][0]
    poset = induced_specialization_poset((smooth, codim_two))
    assert len(poset.cover_relations()) == 1
    generic, special = poset.cover_relations()[0]
    assert generic == smooth
    assert special == codim_two
    assert poset.is_lequal(generic, special)


def test_induced_subposet_rank_differs_from_ambient_codimension():
    smooth = StableGraphs(2, 1).smooth()
    codim_two = strata_by_codimension(2, 1)[2][0]
    poset = induced_specialization_poset((smooth, codim_two))
    _, special = poset.cover_relations()[0]
    assert special.codimension() == 2
    assert poset.rank(special) == 1
    # multi-edge contraction path: some Aut orbit witness contracts more than one edge overall
    targets = {target for target, _witness, _size in special.elementary_contractions()}
    assert smooth not in targets  # no single-edge cover to smooth
    assert special.contracts_to(smooth)


def test_adjacent_rank_mode_requires_one_edge_covers():
    smooth = StableGraphs(2, 1).smooth()
    codim_two = strata_by_codimension(2, 1)[2][0]
    one_edge_covers = [
        (target, gamma)
        for gamma in (smooth, codim_two)
        for target, _witness, _size in gamma.elementary_contractions()
        if target in (smooth, codim_two)
    ]
    assert one_edge_covers == []

r"""CI-tier public API checks that require full Mbar(2, 1) stratification."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.objects.stable_graphs import StableGraphs
from dm_moduli_spike.testing_support.support.fixtures import rank_sizes

pytestmark = pytest.mark.ci


def test_stable_graphs_and_gamma_poset_summary_api():
    assert StableGraphs(2, 1).cardinality() == 16
    assert rank_sizes(2, 1) == (1, 2, 5, 5, 3)
    specialization = StableGraphCategory(2, 1).specialization_poset()
    closure = StableGraphCategory(2, 1).closure_poset()
    assert closure == specialization.dual()
    assert specialization.hasse_diagram().num_verts() == 16

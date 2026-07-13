r"""CI-tier public API checks that require full Mbar(2, 1) stratification."""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import DMCompactificationModel


pytestmark = pytest.mark.ci


def test_stratification_summary_api():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification(backend="admcycles-stable", max_codim=None)
    assert stratification.is_complete()
    assert stratification.rank_sizes() == (1, 2, 5, 5, 3)
    assert stratification.cardinality() == 16
    specialization = stratification.specialization_poset()
    closure = stratification.closure_poset()
    assert closure == specialization.dual()
    assert specialization.hasse_diagram().num_verts() == 16

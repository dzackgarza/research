r"""The user-facing API surface described in the spike plan (section 7)."""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel


def test_model_scalar_api():
    model = DMCompactificationModel(2, 1)
    assert model.genus() == 2
    assert model.number_of_markings() == 1
    assert model.dimension() == 4
    assert model.is_stable_range()


def test_stratification_summary_api():
    model = DMCompactificationModel(2, 1)
    stratification = model.stratification(backend="admcycles-stable", max_codim=None)
    assert stratification.is_complete()
    assert stratification.rank_sizes() == (1, 2, 5, 5, 3)
    assert stratification.cardinality() == 16
    specialization = stratification.specialization_poset()
    closure = stratification.closure_poset()
    assert closure.sage_poset() == specialization.sage_poset().dual()
    assert specialization.hasse_diagram().num_verts() == 16


def test_direct_stable_graph_constructor_and_stratum():
    model = DMCompactificationModel(0, 4)
    types = model.curve_types()
    gamma = types.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
    assert gamma.total_genus() == 0
    assert gamma.num_edges() == 1
    assert gamma.codimension() == 1
    assert gamma.stratum_dimension() == 0
    assert gamma.is_stable()
    stratum = model.stratum(gamma)
    presentation = stratum.open_stack_presentation()
    assert presentation.dimension() == 0


def test_strata_and_boundary_filters():
    model = DMCompactificationModel(1, 2)
    assert len(model.strata(codim=1)) == 2
    assert len(model.boundary_strata()) == 4  # codim 1 and 2 strata: 2 + 2


def test_unknown_backend_is_rejected():
    with pytest.raises(AssertionError):
        DMCompactificationModel(1, 1).stratification(backend="julia")


def test_out_of_stable_range_is_rejected():
    with pytest.raises(AssertionError):
        DMCompactificationModel(0, 2)
    with pytest.raises(AssertionError):
        DMCompactificationModel(1, 0)

r"""Backend adapters: no third-party class leaks into the public API."""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel, StableCurveType
from dm_moduli_spike.backends.admcycles_decorated import AdmcyclesDecoratedGraphBackend
from dm_moduli_spike.backends.admcycles_stable import AdmcyclesStableGraphBackend


def test_stable_backend_returns_owned_curve_types_only():
    backend = AdmcyclesStableGraphBackend()
    assert backend.is_available()
    types = DMCompactificationModel(1, 2).curve_types()
    produced = backend.stable_curve_types(types)
    assert all(isinstance(gamma, StableCurveType) for gamma in produced)
    assert all(gamma.parent() == types for gamma in produced)


def test_decorated_backend_is_behind_an_adapter_and_fails_loudly_when_absent():
    backend = AdmcyclesDecoratedGraphBackend()
    # The experimental decorated_graph module is absent in current admcycles
    # releases; the adapter must not silently degrade -- it either works or
    # raises a clear ImportError.
    if backend.is_available():
        types = DMCompactificationModel(1, 1).curve_types()
        produced = backend.stable_curve_types(types)
        assert all(isinstance(gamma, StableCurveType) for gamma in produced)
    else:
        with pytest.raises(ImportError):
            DMCompactificationModel(1, 1).stratification(backend="admcycles-decorated")

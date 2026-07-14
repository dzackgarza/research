r"""Private combinatorial enumeration helpers for dual-graph stratifications.

Prefer :class:`~dm_moduli_spike.objects.gamma.StableGraphCategory` and
:class:`~dm_moduli_spike.objects.stable_graphs.StableGraphs` for the public
combinatorial API. Landscape stubs live under
``computations/scripts/dm_moduli_landscape``.
"""

from __future__ import annotations

from .stable_graphs import StableGraph, StableGraphs
from .stratification import (
    _build_stratification,
    _build_stratification_from_types,
    _CombinatorialStratification,
)

_BACKENDS = ("auto", "pure-sage", "admcycles-stable", "admcycles-decorated")


def _curve_type_keys(stratification: _CombinatorialStratification) -> frozenset[object]:
    return frozenset(gamma.canonical_key() for level in stratification.curve_type_levels() for gamma in level)


def _resolve_backend(backend: str) -> str:
    if backend != "auto":
        return backend
    from ..backends.admcycles_decorated import AdmcyclesDecoratedGraphBackend
    from ..backends.admcycles_stable import AdmcyclesStableGraphBackend

    if AdmcyclesDecoratedGraphBackend().is_available():
        return "admcycles-decorated"
    if AdmcyclesStableGraphBackend().is_available():
        return "admcycles-stable"
    return "pure-sage"


def _enumerate_stable_graph_levels(
    g: int,
    n: int,
    *,
    backend: str = "auto",
    max_codim: int | None = None,
    verify_against: str | None = None,
) -> _CombinatorialStratification:
    r"""Private oracle-speed enumeration of combinatorial stratification levels.

    Not a public API. Prefer ``StableGraphs(g, n)`` / ``StableGraphCategory(g, n)``.
    """
    g = int(g)
    n = int(n)
    assert g >= 0 and n >= 0, f"(g, n) must be nonnegative; (g, n)=({g}, {n})"
    assert 2 * g - 2 + n > 0, f"(g, n)=({g}, {n}) is not in the stable range 2g - 2 + n > 0"
    assert backend in _BACKENDS, f"unknown backend {backend!r}; choose one of {_BACKENDS}"
    resolved = _resolve_backend(backend)
    if verify_against is not None:
        assert verify_against in _BACKENDS, f"unknown verify backend {verify_against!r}; choose one of {_BACKENDS}"
        verify_resolved = _resolve_backend(verify_against)
    else:
        verify_resolved = None
    graph_types = StableGraphs(g, n)
    dimension = graph_types.dimension()
    is_effective_full = max_codim is None or int(max_codim) >= dimension
    if resolved == "pure-sage":
        result = _build_stratification(graph_types, max_codim=max_codim)
    elif resolved == "admcycles-stable":
        from ..backends.admcycles_stable import AdmcyclesStableGraphBackend

        types = AdmcyclesStableGraphBackend().stable_curve_types(graph_types, max_codim=max_codim)
        result = _build_stratification_from_types(
            graph_types,
            types,
            max_codim=max_codim,
            exhaustive=is_effective_full,
            backend=resolved,
        )
    else:
        from ..backends.admcycles_decorated import AdmcyclesDecoratedGraphBackend

        types = AdmcyclesDecoratedGraphBackend().stable_curve_types(graph_types, max_codim=max_codim)
        result = _build_stratification_from_types(
            graph_types,
            types,
            max_codim=max_codim,
            exhaustive=is_effective_full,
            backend=resolved,
        )
    if verify_resolved is not None:
        reference = _enumerate_stable_graph_levels(g, n, backend=verify_resolved, max_codim=max_codim)
        assert _curve_type_keys(result) == _curve_type_keys(reference), f"backend {resolved!r} disagrees with reference {verify_resolved!r} on canonical-key set"
    return result


def _validate_stable_graph(g: int, n: int, curve_type: StableGraph) -> StableGraph:
    if not isinstance(curve_type, StableGraph):
        raise TypeError(f"expected a StableGraph; found {type(curve_type)}")
    expected = StableGraphs(g, n)
    parent = curve_type.parent()
    if parent is not expected and parent != expected:
        raise ValueError(f"curve type belongs to {parent}, not to StableGraphs({g}, {n})")
    return curve_type

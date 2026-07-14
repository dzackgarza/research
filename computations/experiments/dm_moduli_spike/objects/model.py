r"""Internal combinatorial enumeration backend for dual-graph stratification.

This class is **not** a Deligne--Mumford stack or compactification. Prefer
:class:`~dm_moduli_spike.objects.gamma.StableGraphCategory` for the public
combinatorial API. Landscape stubs live under
``computations/scripts/dm_moduli_landscape``.
"""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation

from .graph_types import StableGraphType, StableGraphTypes
from .stratification import DMStratification, build_stratification, build_stratification_from_types

_BACKENDS = ("auto", "pure-sage", "admcycles-stable", "admcycles-decorated")
_RESOLVED_BACKENDS = ("pure-sage", "admcycles-stable", "admcycles-decorated")


def _curve_type_keys(stratification: DMStratification) -> frozenset[object]:
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


class StableGraphStratificationEnumerator(UniqueRepresentation):
    r"""Internal combinatorial stratification enumerator for type `(g, n)`.

    Prefer :class:`~dm_moduli_spike.objects.gamma.StableGraphCategory` for the
    public combinatorial API.  This class remains as the enumeration backend
    for literature/oracle tests.
    """

    def __init__(self, g: int, n: int) -> None:
        g = int(g)
        n = int(n)
        assert g >= 0 and n >= 0, f"(g, n) must be nonnegative; (g, n)=({g}, {n})"
        assert 2 * g - 2 + n > 0, f"(g, n)=({g}, {n}) is not in the stable range 2g - 2 + n > 0"
        self._g = g
        self._n = n

    def genus(self) -> int:
        return self._g

    def number_of_markings(self) -> int:
        return self._n

    def dimension(self) -> int:
        return 3 * self._g - 3 + self._n

    def is_stable_range(self) -> bool:
        return 2 * self._g - 2 + self._n > 0

    def graph_types(self) -> StableGraphTypes:
        return StableGraphTypes(self._g, self._n)

    def validate_type(self, curve_type: StableGraphType) -> StableGraphType:
        if not isinstance(curve_type, StableGraphType):
            raise TypeError(f"expected a StableGraphType; found {type(curve_type)}")
        expected = self.graph_types()
        parent = curve_type.parent()
        if parent is not expected and parent != expected:
            raise ValueError(f"curve type belongs to {parent}, not to this model's {expected}")
        return curve_type

    def stratification(
        self,
        backend: str = "auto",
        max_codim: int | None = None,
        verify_against: str | None = None,
    ) -> DMStratification:
        assert backend in _BACKENDS, f"unknown backend {backend!r}; choose one of {_BACKENDS}"
        resolved = _resolve_backend(backend)
        if verify_against is not None:
            assert verify_against in _BACKENDS, f"unknown verify backend {verify_against!r}; choose one of {_BACKENDS}"
            verify_resolved = _resolve_backend(verify_against)
        else:
            verify_resolved = None
        graph_types = self.graph_types()
        dimension = graph_types.dimension()
        is_effective_full = max_codim is None or int(max_codim) >= dimension
        if resolved == "pure-sage":
            result = build_stratification(graph_types, max_codim=max_codim)
        elif resolved == "admcycles-stable":
            from ..backends.admcycles_stable import AdmcyclesStableGraphBackend

            types = AdmcyclesStableGraphBackend().stable_curve_types(graph_types, max_codim=max_codim)
            result = build_stratification_from_types(
                graph_types,
                types,
                max_codim=max_codim,
                exhaustive=is_effective_full,
                backend=resolved,
            )
        else:
            from ..backends.admcycles_decorated import AdmcyclesDecoratedGraphBackend

            types = AdmcyclesDecoratedGraphBackend().stable_curve_types(graph_types, max_codim=max_codim)
            result = build_stratification_from_types(
                graph_types,
                types,
                max_codim=max_codim,
                exhaustive=is_effective_full,
                backend=resolved,
            )
        if verify_resolved is not None:
            reference = self.stratification(backend=verify_resolved, max_codim=max_codim)
            assert _curve_type_keys(result) == _curve_type_keys(reference), f"backend {resolved!r} disagrees with reference {verify_resolved!r} on canonical-key set"
        return result

    def strata(self, codim: int | None = None) -> tuple[StableGraphType, ...]:
        return self.stratification().strata(codim=codim)

    def boundary_strata(self) -> tuple[StableGraphType, ...]:
        return self.stratification().boundary_strata()

    def _repr_(self) -> str:
        return f"StableGraphStratificationEnumerator({self._g}, {self._n})"

    def __repr__(self) -> str:
        return self._repr_()

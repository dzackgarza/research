r"""The typed ambient model of :math:`\overline{\mathcal M}_{g,n}`.

:class:`DMCompactificationModel` is a stack-aware *combinatorial* model of the
Deligne-Mumford compactification.  It models strata, dimensions, automorphisms,
clutching presentations and closure incidence exactly, while making no claim to
implement the algebraic stack as a functor of points.
"""

from __future__ import annotations

from sage.structure.unique_representation import UniqueRepresentation

from .curve_types import StableCurveType, StableCurveTypes
from .strata import DMStratum
from .stratification import DMStratification, build_stratification, build_stratification_from_types

_BACKENDS = ("pure-sage", "admcycles-stable", "admcycles-decorated")


class DMCompactificationModel(UniqueRepresentation):
    r"""The typed ambient :math:`\overline{\mathcal M}_{g,n}` model for a stable
    pair ``(g, n)``."""

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
        r""":math:`3g - 3 + n`."""
        return 3 * self._g - 3 + self._n

    def is_stable_range(self) -> bool:
        return 2 * self._g - 2 + self._n > 0

    def curve_types(self) -> StableCurveTypes:
        return StableCurveTypes(self._g, self._n)

    def stratum(self, curve_type: StableCurveType) -> DMStratum:
        assert isinstance(curve_type, StableCurveType), f"expected a StableCurveType; found {type(curve_type)}"
        assert curve_type.parent() is self.curve_types() or curve_type.parent() == self.curve_types(), f"curve type belongs to {curve_type.parent()}, not to this model's {self.curve_types()}"
        return DMStratum(curve_type, self._g, self._n)

    def stratification(
        self,
        backend: str = "pure-sage",
        max_codim: int | None = None,
    ) -> DMStratification:
        assert backend in _BACKENDS, f"unknown backend {backend!r}; choose one of {_BACKENDS}"
        curve_types = self.curve_types()
        if backend == "pure-sage":
            return build_stratification(curve_types, max_codim=max_codim)
        if backend == "admcycles-stable":
            from ..backends.admcycles_stable import AdmcyclesStableGraphBackend

            types = AdmcyclesStableGraphBackend().stable_curve_types(curve_types, max_codim=max_codim)
            return build_stratification_from_types(curve_types, types, max_codim=max_codim)
        from ..backends.admcycles_decorated import AdmcyclesDecoratedGraphBackend

        types = AdmcyclesDecoratedGraphBackend().stable_curve_types(curve_types, max_codim=max_codim)
        return build_stratification_from_types(curve_types, types, max_codim=max_codim)

    def strata(self, codim: int | None = None) -> tuple[DMStratum, ...]:
        return self.stratification().strata(codim=codim)

    def boundary_strata(self) -> tuple[DMStratum, ...]:
        return self.stratification().boundary_strata()

    def _repr_(self) -> str:
        return f"Deligne-Mumford compactification model Mbar({self._g}, {self._n}) of dimension {self.dimension()}"

    def __repr__(self) -> str:
        return self._repr_()

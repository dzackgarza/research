r"""PowerSeriesRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ._sage_ring_classes import _SAGE_POWER_SERIES_RING_CLASSES
from .laurent_series_ring import _LaurentSeriesRings as _LaurentSeriesRings

if TYPE_CHECKING:
    from ...types import (
        Ring,
        RingElement,
        RingMorphism,
    )


class _PowerSeriesRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().PuiseuxSeries().LaurentSeries().PowerSeries()``."""

    _base_category_class_and_axiom = (_LaurentSeriesRings, "PowerSeries")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "power series rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_LaurentSeriesRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_POWER_SERIES_RING_CLASSES)
            or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        @override
        @final
        def is_power_series_ring(self) -> bool:
            return True

        @override
        @final
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            *,
            latex_name: str | None = None,
            latex_names: str | Sequence[str] | None = None,
            map: bool = False,
            embedding: RingMorphism | None = None,
        ) -> Ring:
            base_ext = self.base_ring().extension(
                poly,
                name=name,
                names=names,
                latex_name=latex_name,
                latex_names=latex_names,
                map=map,
                embedding=embedding,
            )
            return self.change_ring(base_ext)

        @abstractmethod
        def default_prec(self) -> Integer: ...

        @abstractmethod
        def gen(self, n: Integer = 0) -> RingElement: ...

        @abstractmethod
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def ngens(self) -> Integer: ...

        @abstractmethod
        def laurent_series_ring(self) -> Ring: ...

        @abstractmethod
        def change_ring(self, R: Ring) -> Ring: ...

        @abstractmethod
        def change_var(self, var: str) -> Ring: ...

    class ElementMethods: ...

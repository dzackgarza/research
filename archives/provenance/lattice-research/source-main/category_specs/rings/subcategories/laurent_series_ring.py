r"""LaurentSeriesRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ._sage_ring_classes import _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES
from .puiseux_series_ring import _PuiseuxSeriesRings as _PuiseuxSeriesRings

if TYPE_CHECKING:
    from ...types import (
        Ring,
        RingElement,
        RingMorphism,
    )


class _LaurentSeriesRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().PuiseuxSeries().LaurentSeries()``."""

    _base_category_class_and_axiom = (_PuiseuxSeriesRings, "LaurentSeries")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "Laurent series rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_PuiseuxSeriesRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_LAURENT_SERIES_CONTAINMENT_CLASSES)
            or isinstance(R, self.parent_class)
        )

    PowerSeries = LazyImport(
        "category_specs.rings.subcategories.power_series_ring", "_PowerSeriesRings"
    )

    class SubcategoryMethods:
        @final
        def PowerSeries(self) -> Category:
            return self._with_axiom("PowerSeries")

    class ParentMethods:
        @override
        @final
        def is_laurent_series_ring(self) -> bool:
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
        def power_series_ring(self) -> Ring: ...

        @abstractmethod
        def change_ring(self, R: Ring) -> Ring: ...

    class ElementMethods: ...

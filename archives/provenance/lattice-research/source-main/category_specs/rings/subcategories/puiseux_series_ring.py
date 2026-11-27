r"""PuiseuxSeriesRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings
from ._sage_ring_classes import _SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES

if TYPE_CHECKING:
    from ...types import (
        Ring,
        RingElement,
        RingMorphism,
    )


class _PuiseuxSeriesRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().PuiseuxSeries()``."""

    _base_category_class_and_axiom = (Rings, "PuiseuxSeries")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "Puiseux series rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_PUISEUX_SERIES_CONTAINMENT_CLASSES)
            or isinstance(R, self.parent_class)
        )

    LaurentSeries = LazyImport(
        "category_specs.rings.subcategories.laurent_series_ring",
        "_LaurentSeriesRings",
    )

    class SubcategoryMethods:
        @final
        def LaurentSeries(self) -> Category:
            return self._with_axiom("LaurentSeries")

    class ParentMethods:
        @override
        @final
        def is_puiseux_series_ring(self) -> bool:
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
        def change_ring(self, R: Ring) -> Ring: ...

        @abstractmethod
        def gen(self, n: Integer = 0) -> RingElement: ...

        @abstractmethod
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def ngens(self) -> Integer: ...

        @abstractmethod
        def laurent_series_ring(self) -> Ring: ...

        @abstractmethod
        def default_prec(self) -> Integer: ...

    class ElementMethods: ...

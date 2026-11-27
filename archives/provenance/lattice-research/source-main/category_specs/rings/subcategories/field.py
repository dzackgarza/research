r"""Fields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.fields import Fields as SageFields
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings
from ._lazy_subcategories import (
    _CC,
    _QQ,
    _RR,
    _DivisionRings,
    _IntegrallyClosedDomains,
    _NoetherianRings,
    _ReducedRings,
)
from .euclidean_domain import _EuclideanDomains as _EuclideanDomains

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Field,
        Ideal,
        RingElement,
    )


class _Fields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field()``."""

    _base_category_class_and_axiom = (_EuclideanDomains, "Field")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            SageFields(),
            _DivisionRings(),
            _EuclideanDomains(),
            _IntegrallyClosedDomains(),
            _NoetherianRings(),
            _ReducedRings(),
            Rings().KrullDimension(0),
        ]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageFields() or (R in self.base_category() and R.is_field())

    Finite = LazyImport(
        "category_specs.rings.subcategories.finite_field", "_FiniteFields"
    )
    AlgebraicallyClosed = LazyImport(
        "category_specs.rings.subcategories.algebraically_closed_field",
        "_AlgebraicallyClosedFields",
    )
    LocalFields = LazyImport(
        "category_specs.rings.subcategories.local_field", "_LocalFields"
    )
    GlobalFields = LazyImport(
        "category_specs.rings.subcategories.global_field", "_GlobalFields"
    )

    class SubcategoryMethods:
        @final
        def NumberFields(self) -> Category:
            return self.GlobalFields().NumberFields()
        @final
        def AlgebraicallyClosed(self) -> Category:
            return self._with_axiom("AlgebraicallyClosed")
        @final
        def LocalFields(self) -> Category:
            return self._with_axiom("LocalFields")
        @final
        def GlobalFields(self) -> Category:
            return self._with_axiom("GlobalFields")
    @final
    def QQ(self) -> Any:
        return _QQ()
    @final
    def RR(self) -> Any:
        return _RR()
    @final
    def CC(self) -> Any:
        return _CC()

    class ParentMethods:
        @abstractmethod
        def zero(self) -> RingElement: ...

        @abstractmethod
        def one(self) -> RingElement: ...

        @abstractmethod
        def is_algebraically_closed(self) -> bool: ...

        @abstractmethod
        def algebraic_closure(self) -> Field: ...

        @override
        @final
        def completion(self, ideal: Ideal) -> CompleteRing:
            # Field case split: only the zero and unit ideals exist.
            if ideal.is_zero():
                return self
            return Rings().Constructors().ZeroRing()

    class ElementMethods:
        @abstractmethod
        def inverse(self) -> RingElement: ...

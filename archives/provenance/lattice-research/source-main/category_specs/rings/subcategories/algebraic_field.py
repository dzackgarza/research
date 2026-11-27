r"""AlgebraicFields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from .. import Rings
from ._lazy_subcategories import _Fields

if TYPE_CHECKING:
    from ...types import (
        AlgebraicPolynomial,
        ComplexInterval,
        Polynomial,
        RealInterval,
        RingElement,
    )


class _AlgebraicFields(Category_singleton):
    r"""Common category for Sage's ``AA`` and ``QQbar`` parents.

    Constructor target: ``Rings().Constructors().AA()`` and
    ``Rings().Constructors().QQbar()`` refine into this fixed algebraic-field
    family.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "algebraic real and complex fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_Fields(), Rings().Characteristic(0)]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import AA, QQbar

        return x is AA or x is QQbar

    class ParentMethods:
        @abstractmethod
        def default_interval_prec(self) -> Integer: ...

        @abstractmethod
        def common_polynomial(self, poly: Polynomial) -> AlgebraicPolynomial: ...

        @abstractmethod
        def polynomial_root(
            self,
            poly: Polynomial,
            interval: RealInterval | ComplexInterval,
            multiplicity: Integer = 1,
        ) -> RingElement: ...

    class ElementMethods: ...

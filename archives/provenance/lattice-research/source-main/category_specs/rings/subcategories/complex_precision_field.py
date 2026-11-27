r"""ComplexPrecisionFields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, cast, final, override

from sage.rings.abc import ComplexBallField as SageComplexBallField
from sage.rings.abc import ComplexDoubleField as SageComplexDoubleField
from sage.rings.abc import ComplexField as SageComplexField
from sage.rings.abc import ComplexIntervalField as SageComplexIntervalField
from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from .. import Rings
from ._lazy_subcategories import (
    _CompleteRings,
    _LocalFields,
)
from .approximate import ApproximateRingsCategory

if TYPE_CHECKING:
    from ...types import Field


class _ComplexPrecisionFields(Category_singleton):
    r"""Common category for Sage complex approximate fields with fixed precision.

    Constructor target: complex floating, interval, ball, and double-field
    constructors refine through this precision-family category.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complex precision fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            ApproximateRingsCategory(),
            _CompleteRings(),
            _LocalFields(),
            Rings().Characteristic(0),
        ]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(
            R,
            (
                SageComplexField,
                SageComplexDoubleField,
                SageComplexIntervalField,
                SageComplexBallField,
            ),
        )

    class ParentMethods:
        @abstractmethod
        def precision(self) -> Integer: ...

        @override
        @final
        def change_precision(
            self, precision: Integer, precision_type: str | None = None
        ) -> Field:
            assert precision_type is None, (
                "Sage complex precision-field change is source-backed for default "
                "precision type"
            )
            if isinstance(
                self,
                (SageComplexField, SageComplexDoubleField, SageComplexIntervalField),
            ):
                return cast("Field", self.to_prec(precision))
            assert isinstance(self, SageComplexBallField)
            return cast("Field", self.__class__(precision))

    class ElementMethods: ...

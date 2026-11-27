r"""ScientificNotationFields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import ComplexField as SageComplexField
from sage.rings.abc import ComplexIntervalField as SageComplexIntervalField
from sage.rings.abc import RealField as SageRealField
from sage.rings.abc import RealIntervalField as SageRealIntervalField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _Fields

if TYPE_CHECKING:
    pass


class _ScientificNotationFields(Category_singleton):
    r"""Approximate fields whose display mode supports scientific notation.

    Constructor target: real and complex floating or interval field
    constructors refine here when Sage exposes scientific notation control.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "scientific-notation fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_Fields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(
            R,
            (
                SageRealField,
                SageComplexField,
                SageRealIntervalField,
                SageComplexIntervalField,
            ),
        )

    class ParentMethods:
        @abstractmethod
        def scientific_notation(self, status: bool | None = None) -> bool: ...

    class ElementMethods: ...

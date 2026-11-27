r"""RealIntervalFields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import RealIntervalField as SageRealIntervalField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _RealPrecisionFields,
    _ScientificNotationFields,
)

if TYPE_CHECKING:
    from ...types import (
        Field,
    )


class _RealIntervalFields(Category_singleton):
    r"""Category of Sage real interval fields ``RealIntervalField(prec)``.

    Constructor target: ``Rings().Constructors().RealIntervalField(prec)`` and
    the fixed ``RIF`` constructor refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "real interval fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields(), _ScientificNotationFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageRealIntervalField)

    class ParentMethods:
        @abstractmethod
        def middle_field(self) -> Field: ...

    class ElementMethods: ...

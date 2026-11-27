r"""RealBallFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import RealBallField as SageRealBallField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _RealPrecisionFields

if TYPE_CHECKING:
    pass


class _RealBallFields(Category_singleton):
    r"""Category of Sage real ball fields ``RealBallField(prec)``.

    Constructor target: ``Rings().Constructors().RealBallField(prec)`` refines
    here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "real ball fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageRealBallField)

    class ParentMethods: ...

    class ElementMethods: ...

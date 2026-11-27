r"""ComplexBallFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import ComplexBallField as SageComplexBallField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _ComplexPrecisionFields

if TYPE_CHECKING:
    pass


class _ComplexBallFields(Category_singleton):
    r"""Category of Sage complex ball fields ``ComplexBallField(prec)``.

    Constructor target: ``Rings().Constructors().ComplexBallField(prec)``
    refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complex ball fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageComplexBallField)

    class ParentMethods: ...

    class ElementMethods: ...

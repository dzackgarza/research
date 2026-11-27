r"""Approximate rings with explicit precision control."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import ComplexBallField as SageComplexBallField
from sage.rings.abc import ComplexDoubleField as SageComplexDoubleField
from sage.rings.abc import ComplexField as SageComplexField
from sage.rings.abc import ComplexIntervalField as SageComplexIntervalField
from sage.rings.abc import RealBallField as SageRealBallField
from sage.rings.abc import RealDoubleField as SageRealDoubleField
from sage.rings.abc import RealField as SageRealField
from sage.rings.abc import RealIntervalField as SageRealIntervalField
from sage.rings.padics.generic_nodes import pAdicFieldGeneric, pAdicRingGeneric

from ...cat import Category, Category_singleton
from ..homsets import RingHomCategory

if TYPE_CHECKING:
    from ...types import Integer, Ring


class ApproximateRingsCategory(Category_singleton):
    r"""Rings whose elements are represented with finite or capped precision.

    Constructor target: precision and p-adic ring constructors under
    ``Rings().Constructors()`` refine here when they carry mutable precision
    data.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "approximate rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        from .. import Rings

        return [Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(
            R,
            (
                SageRealField,
                SageRealDoubleField,
                SageRealIntervalField,
                SageRealBallField,
                SageComplexField,
                SageComplexDoubleField,
                SageComplexIntervalField,
                SageComplexBallField,
                pAdicRingGeneric,
                pAdicFieldGeneric,
            ),
        )

    class ParentMethods:
        @abstractmethod
        def change_precision(
            self, precision: Integer, precision_type: str | None = None
        ) -> Ring:
            r"""Return the same approximate ring with the requested precision."""
            ...

    class ElementMethods: ...


ApproximateRingsObject = ApproximateRingsCategory.ParentMethods
ApproximateRingsElement = ApproximateRingsCategory.ElementMethods
ApproximateRingsMorphism = RingHomCategory.ElementMethods

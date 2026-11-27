r"""Qp ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CompleteDiscreteValuationFields,
    _LocalFields,
    _PAdicRings,
)

if TYPE_CHECKING:
    from ...types import (
        Field,
        RingElement,
    )


class _Qp(Category_singleton):
    r"""Category of p-adic fields (all primes p, all precision types).

    Constructor target: ``Rings().Constructors().Qp(...)`` and compatible
    p-adic field constructors refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "p-adic fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_PAdicRings(), _CompleteDiscreteValuationFields(), _LocalFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.rings.padics.generic_nodes import pAdicFieldGeneric

        return isinstance(R, pAdicFieldGeneric)

    class ParentMethods:
        @abstractmethod
        def composite(self, subfield1: Field, subfield2: Field) -> Field:
            ...

        @abstractmethod
        def subfield(self, generators: Sequence[RingElement]) -> Field: ...

        @abstractmethod
        def subfields_of_degree(self, n: Integer) -> Integer: ...

        @abstractmethod
        def exact_field(self) -> Field: ...

    class ElementMethods: ...

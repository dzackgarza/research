r"""IntegerModRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.structure.factorization import Factorization

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _CommutativeRings,
    _FiniteRings,
)

if TYPE_CHECKING:
    from ...types import (
        RingElement,
    )


class _IntegerModRings(Category_singleton):
    r"""Category of Sage rings ``IntegerModRing(n)`` and aliases.

    Constructor target: ``IntegerModRing``, ``Zmod``, and ``Integers``
    methods on ``Rings().Constructors()`` refine here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "integer residue class rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_FiniteRings(), _CommutativeRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, IntegerModRing_generic)

    class ParentMethods:
        @abstractmethod
        def modulus(self) -> RingElement: ...

        @abstractmethod
        def factored_order(self) -> Factorization: ...

        @abstractmethod
        def unit_gens(self, algorithm: str = "sage") -> tuple[RingElement, ...]: ...

        @abstractmethod
        def multiplicative_generator(self) -> RingElement: ...

    class ElementMethods: ...

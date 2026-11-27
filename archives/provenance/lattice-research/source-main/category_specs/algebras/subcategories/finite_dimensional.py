r"""Finite-dimensional algebras."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.infinity import infinity

from ...cat import Category, CategoryWithAxiom_over_base_ring
from .. import Algebras

if TYPE_CHECKING:
    from ...types import Algebra, AlgebraElement, AlgebraIdeal, Integer


class _FiniteDimensionalAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras that are finite-dimensional over their base ring.

    Canonical chain: ``Algebras(R).FiniteDimensional()``.
    """

    _base_category_class_and_axiom = (Algebras, "FiniteDimensional")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return the ambient algebra category over the same base ring."""
        return [Algebras(self.base_ring())]

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is an algebra of finite base-ring dimension."""
        return A in self.base_category() and A.dimension() < infinity

    class ParentMethods:
        @abstractmethod
        def dimension(self) -> Integer:
            r"""Return the dimension of this algebra as a module over its base ring."""
            ...

        @override
        @abstractmethod
        def radical(self) -> AlgebraIdeal:
            r"""Return the Jacobson radical of this finite-dimensional algebra."""
            ...

        @override
        @abstractmethod
        def semisimple_quotient(self) -> Algebra:
            r"""Return the semisimple quotient by the Jacobson radical."""
            ...

        @override
        @abstractmethod
        def idempotent_lift(self, x: AlgebraElement) -> AlgebraElement:
            r"""Lift the idempotent ``x`` from the semisimple quotient."""
            ...

    class ElementMethods: ...

r"""Quotient algebras."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraElement, AlgebraMorphism


class _Quotients(QuotientsCategory):
    r"""Quotient objects in a category of algebras.

    Canonical chain: ``Algebras(R).Quotients()``.
    """

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Algebra:
            r"""Return the algebra being quotiented."""
            ...

        @abstractmethod
        def lift(self, x: AlgebraElement) -> AlgebraElement:
            r"""Choose a representative of ``x`` in the ambient algebra."""
            ...

        @abstractmethod
        def retract(self, x: AlgebraElement) -> AlgebraElement:
            r"""Apply the quotient map to ``x`` from the ambient algebra."""
            ...

        @abstractmethod
        def quotient_projection(self) -> AlgebraMorphism:
            r"""Return the quotient projection from the ambient algebra."""
            ...

    class ElementMethods: ...

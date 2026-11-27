r"""Subalgebras."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraElement, AlgebraMorphism


class _Subobjects(SubobjectsCategory):
    r"""Subobjects in a category of algebras.

    Canonical chain: ``Algebras(R).Subobjects()``.
    """

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Algebra:
            r"""Return the ambient algebra containing this subalgebra."""
            ...

        @abstractmethod
        def retract(self, x: AlgebraElement) -> AlgebraElement:
            r"""Project an ambient element onto this subalgebra when defined."""
            ...

        @abstractmethod
        def inclusion(self) -> AlgebraMorphism:
            r"""Return the inclusion morphism into the ambient algebra."""
            ...

    class ElementMethods: ...

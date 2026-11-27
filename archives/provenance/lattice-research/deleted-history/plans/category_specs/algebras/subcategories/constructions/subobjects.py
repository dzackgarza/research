r"""Subalgebras."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.abstract_method import abstract_method

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraElement, AlgebraMorphism


class _Subobjects(SubobjectsCategory):
    r"""Subobjects in a category of algebras.

    Canonical chain: ``Algebras(R).Subobjects()``.
    """

    class ParentMethods:
        @abstract_method
        def ambient(self) -> Algebra:
            r"""Return the ambient algebra containing this subalgebra."""
            ...

        @abstract_method
        def lift(self, x: AlgebraElement) -> AlgebraElement:
            r"""Include ``x`` into the ambient algebra."""
            ...

        @abstract_method
        def retract(self, x: AlgebraElement) -> AlgebraElement:
            r"""Project an ambient element onto this subalgebra when defined."""
            ...

        @abstract_method
        def inclusion(self) -> AlgebraMorphism:
            r"""Return the inclusion morphism into the ambient algebra."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...

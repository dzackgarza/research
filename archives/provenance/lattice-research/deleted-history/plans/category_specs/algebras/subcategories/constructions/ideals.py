r"""Algebra ideals as module subobjects."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category, Category_module
from ....modules import Modules

if TYPE_CHECKING:
    from ....types import Algebra


class AlgebraIdealsCategory(Category_module):
    r"""``R``-submodules that are ideals in an ``R``-algebra.

    Canonical chain: ``Algebras(R).Ideals(A)``.
    """

    @final
    def __init__(self, algebra: Algebra) -> None:
        self._algebra = algebra
        Category_module.__init__(self, algebra.base_ring())

    @final
    def algebra(self) -> Algebra:
        r"""Return the algebra whose ideals this category contains."""
        return self._algebra

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"ideals of {self.algebra()}"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return the module-subobject category containing algebra ideals."""
        return [Modules(self.base_ring()).Subobjects()]

    class ParentMethods:
        @abstract_method
        def is_left_ideal(self) -> bool:
            r"""Return whether this ideal is closed under left multiplication."""
            ...

        @abstract_method
        def is_right_ideal(self) -> bool:
            r"""Return whether this ideal is closed under right multiplication."""
            ...

        @final
        def is_two_sided_ideal(self) -> bool:
            r"""Return whether this ideal is both a left and right ideal."""
            return self.is_left_ideal() and self.is_right_ideal()

    class ElementMethods: ...
    class MorphismMethods: ...


AlgebraIdealsObject = AlgebraIdealsCategory.ParentMethods
AlgebraIdealsElement = AlgebraIdealsCategory.ElementMethods
AlgebraIdealsMorphism = AlgebraIdealsCategory.MorphismMethods

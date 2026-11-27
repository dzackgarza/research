r"""Modules equipped with a specified semigroup or group action."""

from __future__ import annotations

import operator
from collections.abc import Callable
from typing import TYPE_CHECKING, final, Literal, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Algebra, CategoryElement, Group, Matrix, Monoid, RModule, RModuleElement



class _RepresentationModules(Category_over_base_ring):
    r"""Modules carrying a left, right, or two-sided action.

    Constructor target: Sage representation constructors refine here as
    modules equipped with the specified semigroup, group, or monoid action.
    """

    @override
    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).Free(),
            Modules(R).WithOrderedGeneratingSet(),
        ]

    class ParentMethods:
        @override
        @final
        def is_representation_module(self) -> bool:
            return True

        @abstract_method
        def semigroup(self) -> Group | Monoid: ...

        @abstract_method
        def side(self) -> Literal["left", "right", "twosided"]: ...

        @abstract_method
        def algebra(self) -> Algebra: ...

        @abstract_method
        def representation_matrix(
            self,
            g: CategoryElement,
            side: Literal["left", "right"] | None = None,
            sparse: bool = False,
        ) -> Matrix: ...

        @abstract_method
        def invariant_module(
            self,
            S: Group | None = None,
            action: Callable[[CategoryElement, RModuleElement], RModuleElement] = operator.mul,
            action_on_basis: Callable[[CategoryElement, CategoryElement], RModuleElement] | None = None,
            side: Literal["left", "right"] | None = None,
        ) -> RModule: ...

        @abstract_method
        def cell_module(
            self,
            index: CategoryElement,
            prefix: str = "W",
            names: str | tuple[str, ...] | None = None,
        ) -> RModule: ...

    class ElementMethods: ...
    class MorphismMethods: ...

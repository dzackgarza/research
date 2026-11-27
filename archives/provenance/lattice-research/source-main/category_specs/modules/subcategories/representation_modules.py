r"""Modules equipped with a specified semigroup or group action."""

from __future__ import annotations

import operator
from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, Literal, final, override

from sage.categories.category import Category

from ...cat import Cat, Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import (
        Algebra,
        CategoryElement,
        Group,
        Matrix,
        Monoid,
        RModule,
        RModuleElement,
    )


class _RepresentationModules(Category_over_base_ring):
    r"""Modules carrying a left, right, or two-sided action.

    Constructor target: Sage representation constructors refine here as
    modules equipped with the specified semigroup, group, or monoid action.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Cat().join(
                [
                    Modules(R).Free(),
                    Modules(R).WithOrderedGeneratingSet(),
                ]
            )
        ]

    class ParentMethods:
        @override
        @final
        def is_representation_module(self) -> bool:
            return True

        @abstractmethod
        def semigroup(self) -> Group | Monoid: ...

        @abstractmethod
        def side(self) -> Literal["left", "right", "twosided"]: ...

        @abstractmethod
        def algebra(self) -> Algebra: ...

        @abstractmethod
        def representation_matrix(
            self,
            g: CategoryElement,
            side: Literal["left", "right"] | None = None,
            sparse: bool = False,
        ) -> Matrix: ...

        @abstractmethod
        def invariant_module(
            self,
            S: Group | None = None,
            action: Callable[
                [CategoryElement, RModuleElement], RModuleElement
            ] = operator.mul,
            action_on_basis: Callable[
                [CategoryElement, CategoryElement], RModuleElement
            ]
            | None = None,
            side: Literal["left", "right"] | None = None,
        ) -> RModule: ...

        @abstractmethod
        def cell_module(
            self,
            index: CategoryElement,
            prefix: str = "W",
            names: str | tuple[str, ...] | None = None,
        ) -> RModule: ...

    class ElementMethods: ...

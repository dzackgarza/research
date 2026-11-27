r"""Vector spaces and modules over fields."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal, final, override

from sage.categories.category import Category

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import RModuleElement


class _OverField(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).OverField()``."""

    _base_category_class_and_axiom = (Modules, "OverField")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().OverPID()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_field()

    class ParentMethods:
        @override
        @final
        def is_over_field(self) -> bool:
            return True

        @abstractmethod
        def linear_dependence(
            self,
            vectors: Sequence[RModuleElement],
            zeros: Literal["left", "right"] = "left",
            check: bool = True,
        ) -> list[RModuleElement]:
            ...

    class ElementMethods: ...

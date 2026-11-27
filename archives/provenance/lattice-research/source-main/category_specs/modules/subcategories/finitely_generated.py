r"""Finitely generated modules."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import FiniteSet, RModule


class _FinitelyGenerated(CategoryWithAxiom_over_base_ring):
    r"""Modules admitting a surjection from ``R^n`` for some finite ``n``.

    Canonical chain: ``Modules(R).FinitelyGenerated()``.
    """

    _base_category_class_and_axiom = (Modules, "FinitelyGenerated")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_generated()

    class ParentMethods:
        @override
        @final
        def is_finitely_generated(self) -> bool:
            return True

        @abstractmethod
        def generating_set(self) -> FiniteSet:
            r"""Return a finite generating set witnessing finite generation."""
            ...

        @abstractmethod
        def with_generating_set(self, S: FiniteSet) -> RModule:
            r"""Equip this module with the specified finite generating set."""
            ...

    class ElementMethods: ...

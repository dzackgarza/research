r"""Graded modules."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _Graded(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a grading.

    Canonical chain: ``Modules(R).Graded()``.
    """

    _base_category_class_and_axiom = (Modules, "Graded")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_graded()

    class ParentMethods:
        @override
        @final
        def is_graded(self) -> bool:
            return True

    class ElementMethods: ...

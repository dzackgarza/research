r"""Modules over complete rings."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverCompleteRing(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).OverCompleteRing()``."""
    _base_category_class_and_axiom = (Modules, "OverCompleteRing")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_complete_ring()

    class ParentMethods:
        @override
        @final
        def is_over_complete_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...

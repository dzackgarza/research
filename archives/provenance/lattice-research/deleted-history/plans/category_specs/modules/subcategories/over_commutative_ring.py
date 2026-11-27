r"""Modules over commutative rings."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverCommutativeRing(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).OverCommutativeRing()``."""
    _base_category_class_and_axiom = (Modules, "OverCommutativeRing")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_commutative_ring()

    class ParentMethods:
        @override
        @final
        def is_over_commutative_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...

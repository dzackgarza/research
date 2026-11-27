r"""Projective modules."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _Projective(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).Projective()``."""

    _base_category_class_and_axiom = (Modules, "Projective")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_projective()

    class ParentMethods:
        @override
        @final
        def is_projective(self) -> bool:
            return True

    class ElementMethods: ...

r"""Ideals of the base ring as modules."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _RIdeals(CategoryWithAxiom_over_base_ring):
    r"""Ideals of ``R`` viewed as submodules of the rank-one module ``R``.

    Canonical chain: ``Modules(R).RIdeals()``.
    """

    _base_category_class_and_axiom = (Modules, "RIdeals")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().Subobjects()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_ideal()

    class ParentMethods:
        @override
        @final
        def is_ideal(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...

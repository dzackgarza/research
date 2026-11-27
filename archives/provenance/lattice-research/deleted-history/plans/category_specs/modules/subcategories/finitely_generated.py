r"""Finitely generated modules."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _FinitelyGenerated(CategoryWithAxiom_over_base_ring):
    r"""Modules admitting a surjection from ``R^n`` for some finite ``n``.

    Canonical chain: ``Modules(R).FinitelyGenerated()``.
    """

    _base_category_class_and_axiom = (Modules, "FinitelyGenerated")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().WithOrderedGeneratingSet()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_finitely_generated()

    class ParentMethods:
        @override
        @final
        def is_finitely_generated(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...

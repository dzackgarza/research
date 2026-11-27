r"""Modules over Dedekind domains."""

from __future__ import annotations

from typing import Any, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules


class _OverDedekindDomain(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).OverDedekindDomain()``."""
    _base_category_class_and_axiom = (Modules, "OverDedekindDomain")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().OverIntegralDomain()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_dedekind_domain()

    class ParentMethods:
        @override
        @final
        def is_over_dedekind_domain(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...

r"""Modules over integral domains."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import SubModule


class _OverIntegralDomain(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).OverIntegralDomain()``."""
    _base_category_class_and_axiom = (Modules, "OverIntegralDomain")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_integral_domain()

    class ParentMethods:
        @override
        @final
        def is_over_integral_domain(self) -> bool:
            return True

        @abstract_method
        def saturation(self) -> SubModule: ...

    class ElementMethods: ...

    class MorphismMethods: ...

r"""Modules over principal ideal domains."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Cardinality, RModule


class _OverPID(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).OverPID()``."""
    _base_category_class_and_axiom = (Modules, "OverPID")

    @override
    @final
    def extra_super_categories(self):
        return [self.base_category().OverDedekindDomain()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_over_pid()

    class ParentMethods:
        @override
        @final
        def is_over_pid(self) -> bool:
            return True

        @abstract_method
        def index_in(self, other: RModule) -> Cardinality: ...

    class ElementMethods: ...

    class MorphismMethods: ...

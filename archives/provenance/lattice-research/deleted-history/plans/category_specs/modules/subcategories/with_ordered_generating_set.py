r"""Modules with an ordered generating set."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction
from .. import Modules

if TYPE_CHECKING:
    from ...types import Cardinality, Integer, RModuleElement, RModuleMorphism


class _WithOrderedGeneratingSet(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).WithOrderedGeneratingSet()``."""
    _base_category_class_and_axiom = (Modules, "WithOrderedGeneratingSet")

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_generating_set()

    class ParentMethods:
        @override
        @final
        def has_ordered_generating_set(self) -> bool:
            return True

        @abstract_method
        def gens(self) -> Sequence[RModuleElement]: ...

        @final
        def ngens(self) -> Cardinality:
            return self.gens().cardinality()

        @final
        def gen(self, i: Integer) -> RModuleElement:
            return self.gens()[i]

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstract_method
            def from_function(self, f: Callable[[RModuleElement], RModuleElement]) -> RModuleMorphism: ...

        class ElementMethods: ...
        class MorphismMethods: ...

    class ElementMethods: ...

    class MorphismMethods:
        @abstract_method
        def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...

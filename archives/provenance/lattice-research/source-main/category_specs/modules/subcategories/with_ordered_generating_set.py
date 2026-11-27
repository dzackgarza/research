r"""Modules with an ordered generating set."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category import Category
from sage.rings.integer import Integer as SageInteger

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction
from .. import Modules

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        FiniteSet,
        Integer,
        RModule,
        RModuleElement,
        RModuleMorphism,
    )


class _WithOrderedGeneratingSet(CategoryWithAxiom_over_base_ring):
    r"""Canonical chain: ``Modules(R).WithOrderedGeneratingSet()``."""

    _base_category_class_and_axiom = (Modules, "WithOrderedGeneratingSet")

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().FinitelyGenerated()]

    @override
    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_generating_set()

    class ParentMethods:
        @override
        @final
        def has_ordered_generating_set(self) -> bool:
            return True

        @abstractmethod
        def gens(self) -> Sequence[RModuleElement]: ...

        @override
        @abstractmethod
        def generating_set(self) -> FiniteSet: ...

        @override
        @abstractmethod
        def with_generating_set(self, S: FiniteSet) -> RModule: ...

        @final
        def ngens(self) -> Cardinality:
            return SageInteger(len(self.gens()))

        @final
        def gen(self, i: Integer) -> RModuleElement:
            return self.gens()[int(i)]

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstractmethod
            def from_images(
                self, images: Sequence[RModuleElement]
            ) -> RModuleMorphism:
                r"""Return the morphism determined by images of ordered generators."""
                ...

            @abstractmethod
            def from_function(
                self, f: Callable[[RModuleElement], RModuleElement]
            ) -> RModuleMorphism: ...

        class ElementMethods:
            @abstractmethod
            def generator_images(self) -> tuple[RModuleElement, ...]:
                r"""Return the images of the domain's ordered generators."""
                ...

            @abstractmethod
            def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...

    class ElementMethods: ...

r"""Free graded modules."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, final, override

from sage.categories.category import Category

from ...cat import Cat, Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import (
        Integer,
        Matrix,
        ModuleBasis,
        RModule,
        RModuleElement,
        RModuleMorphism,
    )


class _FreeGradedModules(Category_over_base_ring):
    r"""Free graded modules over connected graded algebras.

    Constructor target: ``Modules(R).Constructors().FreeGradedModule(...)``
    refines here as ``Modules(R).Graded().Free()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [Cat().join([Modules(R).Free(), Modules(R).Graded()])]

    class ParentMethods:
        @override
        @final
        def is_graded(self) -> bool:
            return True

        @override
        @final
        def is_free_graded_module(self) -> bool:
            return True

        @abstractmethod
        def generator_degrees(self) -> tuple[Integer, ...]: ...

        @abstractmethod
        def basis(self, degree: Integer | None = None) -> ModuleBasis: ...

        @abstractmethod
        def suspension(self, t: Integer = 1) -> RModule: ...

        @abstractmethod
        def hom(
            self,
            codomain: RModule,
            values: RModuleMorphism
            | Matrix
            | Sequence[RModuleElement]
            | Mapping[RModuleElement, RModuleElement],
            check: bool = True,
        ) -> RModuleMorphism: ...

    class ElementMethods: ...

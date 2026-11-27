r"""Finitely presented graded modules."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, final, Literal, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from sage.categories.category import Category

    from ...types import (
        CategoryElement,
        FreeResolution,
        Integer,
        Matrix,
        Ring,
        RingElement,
        RModule,
        RModuleElement,
        RModuleMorphism,
    )



class _FinitelyPresentedGradedModules(Category_over_base_ring):
    r"""Cokernels of maps between free graded modules.

    Constructor target: ``Modules(R).Constructors().FPModule(...)`` refines
    here as ``Modules(R).Graded().FinitelyPresented()``.
    """

    @override
    @final
    def super_categories(self):
        R = self.base_ring()
        return [
            Modules(R).FinitelyPresented(),
            Modules(R).Graded(),
        ]

    class ParentMethods:
        @override
        @final
        def is_finitely_presented_graded_module(self) -> bool:
            return True

        @abstract_method
        def generator_degrees(self) -> tuple[Integer, ...]: ...

        @abstract_method
        def relations(self) -> tuple[RModuleElement, ...]: ...

        @abstract_method
        def presentation(self) -> RModule: ...

        @abstract_method
        def free_resolution(
            self,
            name: str = "S",
            *,
            graded: bool = False,
            degrees: Sequence[Integer] | None = None,
            shifts: Sequence[Integer] | None = None,
            algorithm: str = "heuristic",
        ) -> FreeResolution: ...

        @abstract_method
        def module_morphism(
            self,
            on_basis: Callable[[CategoryElement], RModuleElement] | None = None,
            matrix: Matrix | None = None,
            function: Callable[[RModuleElement], RModuleElement] | None = None,
            diagonal: Callable[[CategoryElement], RingElement] | None = None,
            triangular: Literal["upper", "lower"] | None = None,
            unitriangular: bool | Literal["upper", "lower"] = False,
            *,
            codomain: RModule | Ring | None = None,
            category: Category | None = None,
            zero: RModuleElement | RingElement | None = None,
            position: Integer = 0,
            side: Literal["left", "right"] = "left",
        ) -> RModuleMorphism: ...

    class ElementMethods: ...
    class MorphismMethods: ...

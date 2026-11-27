r"""Free graded modules."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Integer, Matrix, ModuleBasis, RModule, RModuleElement, RModuleMorphism



class _FreeGradedModules(Category_over_base_ring):
    r"""Free graded modules over connected graded algebras.

    Constructor target: ``Modules(R).Constructors().FreeGradedModule(...)``
    refines here as ``Modules(R).Graded().Free()``.
    """

    @override
    @final
    def super_categories(self):
        R = self.base_ring()
        return [Modules(R).Free(), Modules(R).Graded()]

    class ParentMethods:
        @override
        @final
        def is_free_graded_module(self) -> bool:
            return True

        @abstract_method
        def generator_degrees(self) -> tuple[Integer, ...]: ...

        @abstract_method
        def basis(self, degree: Integer | None = None) -> ModuleBasis: ...

        @abstract_method
        def suspension(self, t: Integer = 1) -> RModule: ...

        @abstract_method
        def hom(
            self,
            codomain: RModule,
            values: RModuleMorphism | Matrix | Sequence[RModuleElement] | Mapping[RModuleElement, RModuleElement],
            check: bool = True,
        ) -> RModuleMorphism: ...

    class ElementMethods: ...
    class MorphismMethods: ...

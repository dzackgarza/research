"""Spec class for the ``Torsion`` axiom."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import final

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.structure.element import RingElement
from sage.structure.parent import Parent

from .homsets import ModulesWithFormsHomsets


class TorsionModulesWithForms(CategoryWithAxiom_over_base_ring):
    r"""External category class for the ``Torsion`` axiom."""

    # @override CategoryWithAxiom_over_base_ring.super_categories
    @final
    def super_categories(self):
        from .modules_with_forms import ModulesWithForms

        return [ModulesWithForms(self.base_ring())]

    # @override CategoryWithAxiom_over_base_ring._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "torsion modules with forms"

    # @override CategoryWithAxiom_over_base_ring._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        @abstractmethod
        def invariants(self) -> tuple[RingElement, ...]:
            ...

        @abstractmethod
        def p_part(self, p: RingElement) -> Parent:
            ...

        @abstractmethod
        def is_p_elementary(self, p: RingElement) -> bool:
            ...

    class ElementMethods(ABC):
        @abstractmethod
        def order(self) -> RingElement:
            ...

    class MorphismMethods(ABC):
        ...

    class Homsets(ModulesWithFormsHomsets):
        class ParentMethods(ModulesWithFormsHomsets.ParentMethods):
            ...

        class ElementMethods(ModulesWithFormsHomsets.ElementMethods):
            ...

        class MorphismMethods(ModulesWithFormsHomsets.MorphismMethods):
            ...

        class Endset(ModulesWithFormsHomsets.Endset):
            class ParentMethods(ModulesWithFormsHomsets.Endset.ParentMethods):
                ...

            class ElementMethods(ModulesWithFormsHomsets.Endset.ElementMethods):
                ...

            class MorphismMethods(ModulesWithFormsHomsets.Endset.MorphismMethods):
                ...

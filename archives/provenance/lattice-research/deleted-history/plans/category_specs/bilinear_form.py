"""Spec class for the bilinear-form stratum."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.morphism import Morphism
from sage.rings.integer import Integer
from sage.structure.element import Element, Matrix
from sage.structure.parent import Parent

from .homsets import ModulesWithFormsHomsets

if TYPE_CHECKING:
    from .modules_with_forms import QuadraticForm


class BilinearForms(CategoryWithAxiom_over_base_ring):
    r"""Spec class for symmetric bilinear form objects in ``ModulesWithForms``."""

    # @override CategoryWithAxiom_over_base_ring.super_categories
    @final
    def super_categories(self):
        from .modules_with_forms import ModulesWithForms

        return [ModulesWithForms(self.base_ring()).Bilinear()]

    # @override CategoryWithAxiom_over_base_ring._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "bilinear forms"

    # @override CategoryWithAxiom_over_base_ring._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        @abstractmethod
        def ambient_module(self) -> Parent:
            ...

        @abstractmethod
        def domain(self) -> Parent:
            ...

        @abstractmethod
        def codomain(self) -> Parent:
            ...

        @final
        def tensor_degree(self) -> Integer:
            return Integer(2)

        @abstractmethod
        def scalar_action_endomorphism(self) -> Morphism:
            ...

        @final
        def arity(self) -> int:
            return 2

        @abstractmethod
        def gram_matrix(self) -> Matrix:
            ...

        @abstractmethod
        def evaluate(self, left: Element, right: Element | None = None) -> Element:
            ...

        @abstractmethod
        def associated_quadratic_form(self) -> QuadraticForm:
            ...

        @abstractmethod
        def _repr_(self) -> str:
            ...

        @abstractmethod
        def _latex_(self) -> str:
            ...

    class ElementMethods(ABC):
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

"""Spec class for dual objects in ``ModulesWithForms(R)``."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, final

if TYPE_CHECKING:
    from .types import (
        BilinearForm,
        RingElement,
        RModHomsetElement,
        RModuleElement,
        RModuleWithForm,
    )

from sage.categories.dual import DualObjectsCategory

from .homsets import ModulesWithFormsHomsets


class ModulesWithFormsDualObjects(DualObjectsCategory):
    r"""
    Dual objects of modules with forms.

    For an object ``(L, b)`` in the base category, the dual object is the
    pair ``(L^*, b^*)`` with ``L^* := Hom_R(L, R)`` regarded as an actual
    homset of ``R``-modules and with ``b`` identified with the tensor
    ``sum_{i,j} b(e_i, e_j) e_i^* \otimes e_j^*`` in ``L^* \otimes_R L^*``
    for the formal dual basis attached to the chosen generators ``e_i`` of
    ``L``.
    """

    # @override DualObjectsCategory.extra_super_categories
    @final
    def extra_super_categories(self):
        return [self.base_category().Homsets()]

    # @override DualObjectsCategory._repr_object_names
    @final
    def _repr_object_names(self) -> str:
        return "dual objects of modules with forms"

    # @override DualObjectsCategory._latex_
    def _latex_(self) -> str:
        ...

    class ParentMethods(ABC):
        # @override DualObjectsCategory.ParentMethods.dual_of
        @abstractmethod
        def dual_of(self) -> RModuleWithForm:
            ...

        # @override DualObjectsCategory.ParentMethods.natural_pairing
        @abstractmethod
        def natural_pairing(self) -> BilinearForm:
            ...

        @final
        def formal_dual_basis(self) -> tuple[RModHomsetElement, ...]:
            return self.gens()

        @abstractmethod
        def source_form_as_dual_tensor(self) -> RModuleElement:
            ...

        @abstractmethod
        def _repr_(self) -> str:
            ...

        @abstractmethod
        def _latex_(self) -> str:
            ...

    class ElementMethods(ABC):
        @abstractmethod
        def __call__(self, value: RModuleElement) -> RingElement:
            ...

        @abstractmethod
        def __mul__(self, value: RModuleElement | RModHomsetElement) -> RingElement:
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

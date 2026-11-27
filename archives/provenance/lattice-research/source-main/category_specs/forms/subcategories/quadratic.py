r"""Modules equipped with quadratic forms."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Protocol, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .with_forms import (
    FormedModulesCategory,
    FormedModulesMorphism,
    OverPIDFormedModulesCategory,
    OverPIDFormedModulesMorphism,
)

if TYPE_CHECKING:
    from ...types import RModuleElement


class _QuadraticForm(Protocol):
    def q(self, v: RModuleElement) -> RModuleElement: ...


class QuadraticModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Pairs ``(M, q)`` with ``q`` quadratic on ``M``.

    Canonical chain: ``Modules(R).WithForms().Quadratic()``.
    """

    _base_category_class_and_axiom = (FormedModulesCategory, "Quadratic")
    _defining_predicates = ("is_quadratic",)

    class ParentMethods:
        @abstractmethod
        def form(self) -> _QuadraticForm: ...

        @override
        @final
        def is_quadratic(self) -> bool:
            return True

        @final
        def q(self, v: RModuleElement) -> RModuleElement:
            r"""Introduced here: evaluate the quadratic form on a module element."""
            return self.form().q(v)

    class ElementMethods: ...



class OverPIDQuadraticModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Quadratic formed modules over a PID.

    Canonical chain: ``Modules(R).OverPID().WithForms().Quadratic()``.
    """

    _base_category_class_and_axiom = (OverPIDFormedModulesCategory, "Quadratic")
    _defining_predicates = ("is_quadratic",)

    ParentMethods = QuadraticModulesCategory.ParentMethods
    ElementMethods = QuadraticModulesCategory.ElementMethods


QuadraticModulesObject = QuadraticModulesCategory.ParentMethods
QuadraticModulesElement = QuadraticModulesCategory.ElementMethods
QuadraticModulesMorphism = FormedModulesMorphism
OverPIDQuadraticModulesObject = OverPIDQuadraticModulesCategory.ParentMethods
OverPIDQuadraticModulesElement = OverPIDQuadraticModulesCategory.ElementMethods
OverPIDQuadraticModulesMorphism = OverPIDFormedModulesMorphism

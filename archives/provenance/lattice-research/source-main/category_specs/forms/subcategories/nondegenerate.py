r"""Nondegenerate bilinear modules.

Canonical chain: ``Modules(R).WithForms().Bilinear().Nondegenerate()``.

A bilinear form ``b`` is *nondegenerate* iff the map
``\phi: M \to M^* = \mathrm{Hom}_R(M, R)`` sending ``v \mapsto b(v, -)``
is injective.  For free modules of finite rank over a domain this is
equivalent to ``\det(G) \neq 0``.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import (
    BilinearModulesCategory,
    BilinearModulesMorphism,
    OverPIDBilinearModulesCategory,
    OverPIDBilinearModulesMorphism,
)

if TYPE_CHECKING:
    from ...types import SubModule


class NondegenerateBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a nondegenerate bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Nondegenerate()``.

    Nondegeneracy means the map ``v \mapsto b(v, -)`` is injective.
    For free finitely generated modules over an integral domain this is
    equivalent to ``\det(\text{Gram matrix}) \ne 0``.

    .. NOTE::

        Nondegeneracy does NOT imply the form is symmetric, alternating,
        positive-definite, or integral.  Those are separate axioms.
    """

    _base_category_class_and_axiom = (BilinearModulesCategory, "Nondegenerate")
    _defining_predicates = ("is_nondegenerate",)

    class ParentMethods:
        @override
        @final
        def is_nondegenerate(self) -> bool:
            return True

        @abstractmethod
        def radical(self) -> SubModule:
            r"""Return the radical ``\{v \in M : b(v, w) = 0 \,\forall w \in M\}``.

            For a nondegenerate form this is the zero submodule, but
            the abstract method is declared here so implementations can
            verify it.
            """
            ...

    class ElementMethods:
        @abstractmethod
        def is_anisotropic(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) \ne 0``.

            For a symmetric nondegenerate form, most elements are anisotropic;
            isotropic elements form the *null cone* (light cone in physics).
            """
            ...



NondegenerateBilinearModulesObject = NondegenerateBilinearModulesCategory.ParentMethods
NondegenerateBilinearModulesElement = (
    NondegenerateBilinearModulesCategory.ElementMethods
)
NondegenerateBilinearModulesMorphism = (
    BilinearModulesMorphism
)


class OverPIDNondegenerateBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Nondegenerate bilinear modules over a PID.

    Canonical chain: ``Modules(R).OverPID().WithForms().Bilinear().Nondegenerate()``.
    """

    _base_category_class_and_axiom = (OverPIDBilinearModulesCategory, "Nondegenerate")
    _defining_predicates = ("is_nondegenerate",)

    ParentMethods = NondegenerateBilinearModulesCategory.ParentMethods
    ElementMethods = NondegenerateBilinearModulesCategory.ElementMethods


OverPIDNondegenerateBilinearModulesObject = (
    OverPIDNondegenerateBilinearModulesCategory.ParentMethods
)
OverPIDNondegenerateBilinearModulesElement = (
    OverPIDNondegenerateBilinearModulesCategory.ElementMethods
)
OverPIDNondegenerateBilinearModulesMorphism = (
    OverPIDBilinearModulesMorphism
)

r"""Rational bilinear modules: ``Modules(R).WithForms().Bilinear().Rational()``.

A bilinear form ``b: M \times M \to K`` is *rational* iff the codomain is
``K = \mathrm{Frac}(R)``.  This is weaker than integral (``S = R \subsetneq K``)
and strictly contains the torsion case (``S = K/R``).

Rational lattices are the primary objects of study in the theory of
quadratic forms over ``\mathbb{Q}``.
"""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final, override, TypeAlias

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import (
    BilinearModulesCategory,
    BilinearModulesMorphism,
    OverPIDBilinearModulesCategory,
    OverPIDBilinearModulesMorphism,
)

if TYPE_CHECKING:
    from ...types import IntegralRescaling


class RationalBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules with a ``K = \mathrm{Frac}(R)``-valued bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Rational()``.

    The form takes values in the fraction field of ``R``, not necessarily
    in ``R`` itself.  An integral form is always rational; a rational form
    need not be integral.

    The primary example is a rational lattice: a free ``\mathbb{Z}``-module
    of finite rank with a ``\mathbb{Q}``-valued symmetric bilinear form.
    """

    _base_category_class_and_axiom = (BilinearModulesCategory, "Rational")
    _defining_predicates = ("is_rational",)

    class ParentMethods:
        @override
        @final
        def is_rational(self) -> bool:
            return True

        @abstractmethod
        def integral_rescaling(self) -> IntegralRescaling:
            r"""Return the smallest positive integer ``n`` such that ``n \cdot b``
            is integral, together with the rescaled module.

            EXAMPLES::

                sage: G = matrix(QQ, [[1/2, 0], [0, 1/2]])   # not tested
                sage: L = RationalLattice(G)                 # not tested
                sage: L.integral_rescaling()   # not tested
                (2, IntegralLattice(...))
            """
            ...

    class ElementMethods: ...



RationalBilinearModulesObject : TypeAlias = RationalBilinearModulesCategory.ParentMethods
RationalBilinearModulesElement : TypeAlias = RationalBilinearModulesCategory.ElementMethods
RationalBilinearModulesMorphism : TypeAlias = BilinearModulesMorphism


class OverPIDRationalBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Rational bilinear modules over a PID.

    Canonical chain: ``Modules(R).OverPID().WithForms().Bilinear().Rational()``.
    """

    _base_category_class_and_axiom = (OverPIDBilinearModulesCategory, "Rational")
    _defining_predicates = ("is_rational",)

    ParentMethods : TypeAlias = RationalBilinearModulesCategory.ParentMethods
    ElementMethods : TypeAlias = RationalBilinearModulesCategory.ElementMethods


OverPIDRationalBilinearModulesObject = (
    OverPIDRationalBilinearModulesCategory.ParentMethods
)
OverPIDRationalBilinearModulesElement = (
    OverPIDRationalBilinearModulesCategory.ElementMethods
)
OverPIDRationalBilinearModulesMorphism = (
    OverPIDBilinearModulesMorphism
)

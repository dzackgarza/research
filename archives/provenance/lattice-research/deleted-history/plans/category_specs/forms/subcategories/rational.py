r"""Rational bilinear modules: ``Modules(R).WithForms().Bilinear().Rational()``.

A bilinear form ``b: M \times M \to K`` is *rational* iff the codomain is
``K = \mathrm{Frac}(R)``.  This is weaker than integral (``S = R \subsetneq K``)
and strictly contains the torsion case (``S = K/R``).

Rational lattices are the primary objects of study in the theory of
quadratic forms over ``\mathbb{Q}``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import BilinearModulesCategory

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

        @abstract_method
        def integral_rescaling(self) -> IntegralRescaling:
            r"""Return the smallest positive integer ``n`` such that ``n \cdot b``
            is integral, together with the rescaled module.

            EXAMPLES::

                sage: L = RationalLattice(matrix(QQ, [[1/2, 0], [0, 1/2]]))   # not tested
                sage: L.integral_rescaling()   # not tested
                (2, IntegralLattice(...))
            """
            ...

    class ElementMethods: ...
    class MorphismMethods: ...


RationalBilinearModulesObject = RationalBilinearModulesCategory.ParentMethods
RationalBilinearModulesElement = RationalBilinearModulesCategory.ElementMethods
RationalBilinearModulesMorphism = RationalBilinearModulesCategory.MorphismMethods

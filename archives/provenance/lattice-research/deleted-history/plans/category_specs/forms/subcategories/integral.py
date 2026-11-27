r"""Integral bilinear modules: ``Modules(R).WithForms().Bilinear().Integral()``.

A bilinear form ``b: M \times M \to K`` is *integral* iff ``b(v, w) \in R``
for all ``v, w \in M`` (i.e. the codomain is ``R``, not a proper extension).
For lattices over ``\mathbb{Z}`` this means the Gram matrix has integer entries.

This is the minimal tier at which the *dual* is constructible:

    ``L^* = \{v \in L \otimes_R K : b(v, L) \subseteq R\}``

because the condition ``b(v, L) \subseteq R`` requires both that ``b`` is
``R``-valued (integral) and that ``R`` is an integral domain (to form
``K = \mathrm{Frac}(R)`` and ``L_K = L \otimes_R K``).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import BilinearModulesCategory

if TYPE_CHECKING:
    from ...types import DiscriminantGroup, Lattice, RModuleMorphism


class IntegralBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules with an ``R``-valued (integral) bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Integral()``.

    *Integral* means the form ``b: M \times M \to S`` has ``S = R``, as
    opposed to ``S = K = \mathrm{Frac}(R)`` (rational) or a quotient
    ``K/R`` (torsion/discriminant).

    For free finitely generated modules this is equivalent to requiring
    that the Gram matrix has entries in ``R``.

    **New at this tier:**

    - ``dual_lattice()`` — ``L^* = \{v \in L_K : b(v, L) \subseteq R\}``
    - ``inclusion_morphism()`` — the canonical map ``\iota: L \to L^*``
    - ``discriminant_group()`` — the finite quotient ``L^*/L``
    - ``is_even()`` — whether ``b(v, v) \in 2R`` for all ``v``
    - ``is_unimodular()`` — whether ``L = L^*``

    .. NOTE::

        Over ``\mathbb{Z}`` this is the standard notion: the Gram matrix
        is an integer matrix.  A rational lattice has Gram matrix over
        ``\mathbb{Q}``; it is integral iff the denominators are trivial.
    """

    _base_category_class_and_axiom = (BilinearModulesCategory, "Integral")
    _defining_predicates = ("is_integral",)

    class ParentMethods:
        @override
        @final
        def is_integral(self) -> bool:
            return True

        @override
        @final
        def is_rational(self) -> bool:
            r"""Every integral form is rational (``R \subseteq K``)."""
            return True

        @abstract_method
        def dual_lattice(self) -> Lattice:
            r"""Return the dual ``L^* = \{v \in L \otimes_R K : b(v, L) \subseteq R\}``.

            Here ``K = \mathrm{Frac}(R)`` is the fraction field and
            ``L_K = L \otimes_R K``.  Requires ``R`` to be an integral domain.
            The inclusion ``L \hookrightarrow L^*`` is given by
            ``v \mapsto b(v, -) \in \mathrm{Hom}_R(L, R) \cong L^*``.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: L.dual_lattice()   # not tested; U is unimodular
                Integer lattice of rank 2 ...
                sage: L.dual_lattice() == L   # not tested
                True
            """
            ...

        @abstract_method
        def inclusion_morphism(self) -> RModuleMorphism:
            r"""Return the canonical inclusion ``\iota: L \hookrightarrow L^*``
            sending ``v`` to ``b(v, -) \in \mathrm{Hom}_R(L, R) \cong L^*``.

            The cokernel of ``\iota`` is the discriminant group ``L^*/L``.
            """
            ...

        @abstract_method
        def discriminant_group(self) -> DiscriminantGroup:
            r"""Return the discriminant group ``A_L = L^*/L``.

            This is a finite torsion ``R``-module equipped with a
            ``K/R``-valued bilinear form descending from ``b``.  It is
            trivial iff ``L`` is unimodular.

            EXAMPLES::

                sage: Lattice.E(8).discriminant_group()   # not tested
                Trivial group
                sage: Lattice.A(2).discriminant_group()   # not tested
                Abelian group of order 3
            """
            ...

        @final
        def is_unimodular(self) -> bool:
            r"""Return ``True`` iff ``L = L^*`` (i.e. ``|\det(G)| = 1``)."""
            return self.discriminant_group().is_trivial()

        @abstract_method
        def is_even(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) \in 2R`` for all ``v \in L``.

            An integral lattice is *even* iff all diagonal entries of the
            Gram matrix are even.  Over ``\mathbb{Z}`` this means
            ``b(v, v) \equiv 0 \pmod{2}`` for all ``v``.

            EXAMPLES::

                sage: Lattice.E(8).is_even()   # not tested
                True
                sage: Lattice.A(1).is_even()   # not tested
                False
            """
            ...

    class ElementMethods: ...

    class MorphismMethods: ...


IntegralBilinearModulesObject = IntegralBilinearModulesCategory.ParentMethods
IntegralBilinearModulesElement = IntegralBilinearModulesCategory.ElementMethods
IntegralBilinearModulesMorphism = IntegralBilinearModulesCategory.MorphismMethods

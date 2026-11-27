r"""Free bilinear modules: ``Modules(R).Free().Bilinear()``.

A *free bilinear module* is a free ``R``-module of finite rank equipped with
a bilinear form ``b: M \times M \to S``.  Having a basis means the form can
be recorded as a Gram matrix ``G_{ij} = b(e_i, e_j) \in S``.

This is the first tier at which ``gram_matrix()`` is well-defined as a
genuine matrix (entries in ``S``), and the first tier at which
``signature_pair()`` is computable (via base-change to an ordered field).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import BilinearModulesCategory

if TYPE_CHECKING:
    from ...types import (
        Integer,
        Matrix,
        Ring,
        RingElement,
        RModule,
        RModuleElement,
        SetFamily,
        SubModule,
    )


class FreeBilinearModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Free ``R``-modules of finite rank equipped with a bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Free()``.

    Objects are pairs ``(M, b)`` where ``M \cong R^n`` is free of finite rank
    and ``b: M \times M \to S`` is an ``R``-bilinear form.  Morphisms are
    ``R``-module maps; isometries additionally preserve ``b``.

    **New at this tier** (compared to ``Modules(R).WithForms().Bilinear()``):

    - ``gram_matrix()`` — matrix ``G`` with ``G_{ij} = b(e_i, e_j)``
    - ``rank()`` — the rank ``n`` of ``M \cong R^n``
    - ``determinant()`` — ``\det(G)``
    - ``discriminant()`` — ``(-1)^r \det(G)``
    - ``direct_sum(other)`` — orthogonal direct sum with block-diagonal Gram matrix
    - ``tensor_product(other)`` — tensor product with Kronecker product Gram matrix
    - ``span(gens)`` — sub-bilinear-module spanned by generators
    - ``base_change_to(ring)`` — reinterpret over a different ring

    EXAMPLES::

        sage: L = Modules(ZZ).Constructors().FreeQuadraticModuleFromRows(   # not tested
        ...     rank=2,
        ...     inner_product_rows=[[2, -1], [-1, 2]],
        ... )
        sage: L in Modules(ZZ).WithForms().Bilinear().Free()   # not tested
        True
        sage: L.gram_matrix()   # not tested
        [2 -1]
        [-1  2]
    """

    _base_category_class_and_axiom = (BilinearModulesCategory, "Free")
    _defining_predicates = ("is_free",)

    class ParentMethods:
        @override
        @final
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Integer:
            r"""Return the rank of the underlying free ``R``-module.

            EXAMPLES::

                sage: Lattice.U().rank()   # not tested
                2
            """
            ...

        @override
        @abstract_method
        def gram_matrix(self) -> Matrix:
            r"""Return the Gram matrix ``G`` with ``G_{ij} = b(e_i, e_j)``.

            The Gram matrix is computed with respect to ``self.gens()``.
            It is an ``n \times n`` matrix over the form's codomain ``S``.

            EXAMPLES::

                sage: Lattice.A(2).gram_matrix()   # not tested
                [-2  1]
                [ 1 -2]
            """
            ...

        @override
        @abstract_method
        def inner_product_matrix(self) -> Matrix:
            r"""Return the inner product matrix (alias / alternative encoding).

            May differ from ``gram_matrix()`` by a factor of 2 depending on
            convention (Gram matrix ``G_{ij} = b(e_i, e_j)`` vs. inner
            product matrix used by Sage's ``FreeQuadraticModule``).
            """
            ...

        @final
        def determinant(self) -> RingElement:
            r"""Introduced here: return ``\det(G)``, the determinant of the Gram matrix.

            EXAMPLES::

                sage: Lattice.U().determinant()   # not tested
                -1
                sage: Lattice.A(2).determinant()   # not tested
                3
            """
            return self.gram_matrix().determinant()

        @final
        def discriminant(self) -> RingElement:
            r"""Introduced here: return ``(-1)^r \det(G)`` where ``r = \mathrm{rank}(M)``.

            This is the sign convention used by Sage's
            ``FreeQuadraticModule_generic.discriminant()``.
            """
            r = self.rank()
            return (-1) ** r * self.determinant()

        @abstract_method
        def direct_sum(self, other: RModule) -> RModule:
            r"""Return the orthogonal direct sum ``M \oplus N``.

            The form on ``M \oplus N`` is ``b_{M \oplus N}((v_1, v_2), (w_1, w_2))
            = b_M(v_1, w_1) + b_N(v_2, w_2)``.  The Gram matrix is block-diagonal.

            EXAMPLES::

                sage: U = Lattice.U()   # not tested
                sage: (U.direct_sum(U)).gram_matrix()   # not tested
                [0 1 0 0]
                [1 0 0 0]
                [0 0 0 1]
                [0 0 1 0]
            """
            ...

        @abstract_method
        def tensor_product(self, other: RModule) -> RModule:
            r"""Return the tensor product ``M \otimes_R N`` with the form
            ``b_{M \otimes N}(v_1 \otimes v_2, w_1 \otimes w_2)``
            equal to ``b_M(v_1, w_1) \cdot b_N(v_2, w_2)``.

            The Gram matrix is the Kronecker product ``G_M \otimes G_N``.
            """
            ...

        @abstract_method
        def span(self, gens: SetFamily) -> RModule:
            r"""Return the sub-bilinear-module spanned by ``gens``.

            The result is a subobject in ``Modules(R).Free().Bilinear().Subobjects()``
            equipped with the restricted form.
            """
            ...

        @abstract_method
        def base_change_to(self, ring: Ring) -> RModule:
            r"""Return the free bilinear module over ``ring`` obtained by
            extending (or restricting) scalars.

            EXAMPLES::

                sage: L = Lattice.E(8)   # not tested
                sage: L.base_change_to(QQ)   # not tested
                Free bilinear module of rank 8 over Rational Field
            """
            ...

        @abstract_method
        def twist(self, scalar: RingElement) -> RModule:
            r"""Return the free bilinear module with the form scaled by ``scalar``.

            The Gram matrix of ``twist(s)`` is ``s \cdot G``.
            """
            ...

    class ElementMethods:
        @abstract_method
        def divisibility(self) -> RingElement:
            r"""Return the divisibility of ``v``:
            ``\gcd\{a \in R : v = a \cdot w \text{ for some } w \in M\}``.

            An element is *primitive* iff its divisibility is a unit.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e = L.gen(0)   # not tested
                sage: e.divisibility()   # not tested
                1
            """
            ...

        @final
        def is_primitive(self) -> bool:
            r"""Refine the module-element primitive predicate using divisibility."""
            return self.divisibility().is_unit()

        @abstract_method
        def perp(self) -> SubModule:
            r"""Return the orthogonal complement ``v^\perp = \{w \in M : b(v,w) = 0\}``.

            This is the element-level version; the parent-level version is
            ``M.orthogonal_complement(S)`` for a submodule ``S``.

            EXAMPLES::

                sage: U = Lattice.U()   # not tested
                sage: e = U.gen(0)   # not tested
                sage: e.perp()   # not tested
                Rank-1 lattice spanned by ...
            """
            ...

        @final
        def self_product(self) -> RingElement:
            r"""Introduced here: return ``b(v, v)``."""
            return self.parent().b(self, self)

    class MorphismMethods:
        @abstract_method
        def to_matrix(self) -> Matrix:
            r"""Return the matrix of this morphism with respect to canonical
            generators of domain and codomain."""
            ...

        @abstract_method
        def is_isometry(self) -> bool:
            r"""Return ``True`` iff this morphism preserves the bilinear form:
            ``b_N(f(v), f(w)) = b_M(v, w)`` for all ``v, w \in M``."""
            ...


FreeBilinearModulesObject = FreeBilinearModulesCategory.ParentMethods
FreeBilinearModulesElement = FreeBilinearModulesCategory.ElementMethods
FreeBilinearModulesMorphism = FreeBilinearModulesCategory.MorphismMethods

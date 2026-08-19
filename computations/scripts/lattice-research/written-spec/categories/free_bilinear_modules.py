r"""
Free Bilinear Modules

A *free bilinear module* is a bilinear module `(M, \beta)` whose
underlying `R`-module `M` is free of finite rank.

This is the ``BilinearModules(R).Free()`` subcategory.

EXAMPLES::

    sage: BilinearModules(ZZ).Free()   # not tested
    Category of free bilinear modules over Integer Ring
"""
# ****************************************************************************
#  Copyright (C) 2024  The research project authors
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport
from sage.rings.infinity import Infinity


class FreeBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""
    The category of free bilinear modules over a commutative ring `R`.

    A *free bilinear module* is a finitely generated free `R`-module
    equipped with a symmetric `R`-bilinear form.  Morphisms are
    `R`-module maps; isometries additionally preserve the form.

    The axiom name is ``"Free"``; use
    ``BilinearModules(R).Free()`` or ``BilinearModules(R)._with_axiom("Free")``.

    EXAMPLES::

        sage: BilinearModules(ZZ).Free()   # not tested
        Category of free bilinear modules over Integer Ring
        sage: BilinearModules(ZZ).Free().super_categories()   # not tested
        [Category of bilinear modules over Integer Ring]

    .. SEEALSO::

        :class:`~src.lattices.categories.lattices.Lattices`,
        :class:`~src.lattices.categories.rational_lattices.RationalLattices`
    """

    # Subcategories available on free bilinear modules
    Lattices = LazyImport("src.lattices.categories.lattices", "Lattices")
    RationalLattices = LazyImport("src.lattices.categories.rational_lattices", "RationalLattices")

    class SubcategoryMethods:
        @cached_method
        def NonDegenerate(self):
            r"""
            Return the full subcategory of nondegenerate objects.

            A bilinear form is *nondegenerate* iff the map
            `M \to M^* = \mathrm{Hom}_R(M, R)` sending `v \mapsto
            \beta(v, -)` is injective.  For free modules of finite rank
            it is nondegenerate iff the determinant of the Gram matrix
            is a unit in `R`.

            EXAMPLES::

                sage: BilinearModules(ZZ).Free().NonDegenerate()   # not tested
                Category of nondegenerate free bilinear modules over Integer Ring
            """
            return self._with_axiom("NonDegenerate")

    class ParentMethods:
        r"""
        Additional interface for free bilinear modules beyond
        :class:`~src.lattices.categories.bilinear_modules.BilinearModules.ParentMethods`.
        """

        @abstract_method
        def rank(self):
            r"""
            Return the rank of the underlying free `R`-module.

            EXAMPLES::

                sage: Lattice.U().rank()   # not tested
                2
            """

        # --- Derived overrides of abstract parent methods ---

        def free_part(self):
            r"""
            Return the free part of this module.

            For a free bilinear module, this is ``self``.
            """
            return self

        def torsion_part(self):
            r"""
            Return the torsion submodule.

            For a free bilinear module over an integral domain, the
            torsion submodule is the zero module.
            """
            ...  # return zero module

        def cardinality(self):
            r"""
            Return the cardinality of the underlying set.

            A free module of positive rank over an infinite ring has
            infinite cardinality.

            EXAMPLES::

                sage: Lattice.U().cardinality()   # not tested
                +Infinity
            """
            if self.rank() == 0:
                return 1
            return Infinity

        # --- New methods on free modules ---

        @abstract_method
        def is_nondegenerate(self):
            r"""
            Return ``True`` iff the bilinear form is nondegenerate.

            The form is nondegenerate iff the Gram matrix has nonzero
            determinant.  For lattices over `\mathbb{Z}`, this means
            ``det(G) != 0``.

            EXAMPLES::

                sage: Lattice.U().is_nondegenerate()   # not tested
                True
            """

        @abstract_method
        def is_positive_definite(self):
            r"""
            Return ``True`` iff the form is positive definite.

            .. WARNING::

                Most Sage lattice algorithms were written only for
                positive-definite forms and may give wrong results for
                indefinite inputs.  This method exists so callers can
                check and dispatch appropriately.
            """

        @abstract_method
        def is_negative_definite(self):
            r"""Return ``True`` iff the form is negative definite."""

        def is_definite(self):
            r"""Return ``True`` iff the form is definite (positive or negative)."""
            return self.is_positive_definite() or self.is_negative_definite()

        def is_indefinite(self):
            r"""Return ``True`` iff the form is indefinite."""
            return not self.is_definite()

    class ElementMethods:
        r"""
        Additional interface for elements of free bilinear modules.
        """

        @abstract_method
        def divisibility(self):
            r"""
            Return the divisibility of this element.

            The divisibility of `v \in M` is
            `\gcd\{a \in R \mid v = a \cdot w \text{ for some } w \in M\}`.
            For `v` with coordinate vector `(c_1, \ldots, c_n)`, this
            is `\gcd(c_1, \ldots, c_n)`.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e, f = L.gens()   # not tested
                sage: e.divisibility()   # not tested
                1
            """

        def is_primitive(self):
            r"""
            Return ``True`` iff this element is primitive, i.e., has
            divisibility 1.

            Equivalently, `v` is not a proper multiple `a \cdot w` for
            `a \in R \setminus R^\times`.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: L.gens()[0].is_primitive()   # not tested
                True
            """
            R = self.parent().base_ring()
            return self.divisibility() in R.units()

        def discriminant_class(self):
            r"""
            Return the image of this element in the discriminant group.

            For a lattice `L`, every element `v \in L` maps to zero in
            `A_L = L^* / L` under the natural map `L \hookrightarrow
            L^* \to A_L`.

            EXAMPLES::

                sage: L = Lattice.U().twist(2)   # not tested
                sage: e = L.gens()[0]   # not tested
                sage: e.discriminant_class() == L.discriminant_group().zero()   # not tested
                True
            """
            ...

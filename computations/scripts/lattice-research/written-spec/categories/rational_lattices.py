r"""
Rational Lattices

A *rational lattice* is a free `\mathbb{Q}`-module of finite rank
equipped with a nondegenerate symmetric `\mathbb{Q}`-bilinear form.

Alternatively, a rational lattice is an integral lattice
`(L, \beta)` after tensoring with `\mathbb{Q}`: the base change
`L \otimes_{\mathbb{Z}} \mathbb{Q}` with the extended form.

The dual lattice `L^*` of an integral lattice `L` is a rational
lattice: it is the `\mathbb{Z}`-submodule of `L \otimes \mathbb{Q}`
consisting of vectors whose inner product with every lattice vector
is integral.

EXAMPLES::

    sage: RationalLattices(QQ)   # not tested
    Category of rational lattices over Rational Field
"""
# ****************************************************************************
#  Copyright (C) 2024  The research project authors
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method


class RationalLattices(CategoryWithAxiom_over_base_ring):
    r"""
    The category of rational lattices (free bilinear modules over `\mathbb{Q}`
    with nondegenerate form).

    Formally: the full subcategory of
    ``FreeBilinearModules(QQ).NonDegenerate()``.

    Rational lattices serve two roles:

    1. The ambient space `L \otimes \mathbb{Q}` of an integral lattice.
    2. The dual lattice `L^*`, whose elements are the `\mathbb{Z}`-linear
       functionals on `L`.

    EXAMPLES::

        sage: L = Lattice.U()   # not tested
        sage: L.rational_span() in RationalLattices(QQ)   # not tested
        True
        sage: L.dual() in RationalLattices(QQ)   # not tested
        True

    .. SEEALSO::

        :class:`~src.lattices.categories.lattices.Lattices`
    """

    def super_categories(self):
        from sage.rings.rational_field import QQ
        from src.lattices.categories.free_bilinear_modules import FreeBilinearModules

        return [FreeBilinearModules(QQ)]

    class ParentMethods:
        @abstract_method
        def signature_pair(self):
            r"""
            Return the signature `(p, q)` where `p` (resp. `q`) is the
            number of positive (resp. negative) eigenvalues of the Gram
            matrix over `\mathbb{R}`.

            EXAMPLES::

                sage: Lattice.U().rational_span().signature_pair()   # not tested
                (1, 1)
            """

        def signature(self):
            r"""
            Return the signature `p - q` (the *index*).

            EXAMPLES::

                sage: Lattice.U().rational_span().signature()   # not tested
                0
            """
            p, q = self.signature_pair()
            return p - q

        def is_positive_definite(self):
            r"""Return ``True`` iff the form is positive definite."""
            p, q = self.signature_pair()
            return q == 0

        def is_negative_definite(self):
            r"""Return ``True`` iff the form is negative definite."""
            p, q = self.signature_pair()
            return p == 0

        @abstract_method
        def base_change_to(self, ring):
            r"""
            Return this rational lattice with base ring extended to
            ``ring``.

            EXAMPLES::

                sage: V = Lattice.U().rational_span()   # not tested
                sage: V.base_change_to(RR).signature_pair()   # not tested
                (1, 1)
            """

        @abstract_method
        def orthogonal_complement_of(self, sublattice):
            r"""
            Return the orthogonal complement of ``sublattice`` in ``self``.

            INPUT:

            - ``sublattice`` -- a sub-rational-lattice of ``self``

            OUTPUT: the sub-rational-lattice
            `S^\perp = \{v \in M \mid \beta(v, w) = 0 \text{ for all } w \in S\}`.

            EXAMPLES::

                sage: V = Lattice.U().rational_span()   # not tested
                sage: e = V.gens()[0]   # not tested
                sage: V.orthogonal_complement_of(e.span())   # not tested
                Rational span of <e>
            """

    class ElementMethods:
        @abstract_method
        def is_integral(self):
            r"""
            Return ``True`` iff this element lies in the underlying
            integral lattice.

            Only meaningful when ``self`` is viewed as an element of
            `L \otimes \mathbb{Q}` for some integral lattice `L`.
            """

        def perp(self):
            r"""
            Return the orthogonal complement of ``self`` in the parent.

            Shorthand for ``self.parent().orthogonal_complement_of(self.span())``.
            """
            return self.parent().orthogonal_complement_of(self.span())

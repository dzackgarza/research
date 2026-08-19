r"""
Torsion Bilinear Modules

A *torsion bilinear module* is a bilinear module `(T, \beta)` whose
underlying `R`-module `T` is a finitely generated torsion module:
every element has finite additive order.

The prototypical example is the discriminant group `A_L = L^*/L` of
an integral lattice `L`, equipped with its discriminant bilinear form
`b: A_L \times A_L \to \mathbb{Q}/\mathbb{Z}`.

This is the ``BilinearModules(R).Torsion()`` subcategory.
"""
# ****************************************************************************
#  Copyright (C) 2024  The research project authors
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport


class TorsionBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""
    The category of torsion bilinear modules over a commutative ring `R`.

    An object is a finitely generated torsion `R`-module `T` equipped
    with a symmetric `R`-bilinear form `\beta: T \times T \to C`
    where `C` is a quotient of `R.\mathrm{fraction\_field}()`, e.g.
    `\mathbb{Q}/\mathbb{Z}` for `R = \mathbb{Z}`.

    The axiom name is ``"Torsion"``; use
    ``BilinearModules(R).Torsion()`` or ``BilinearModules(R)._with_axiom("Torsion")``.

    .. SEEALSO::

        :class:`~src.lattices.categories.quadratic_modules.TorsionQuadraticModules`
    """

    # Discriminant forms (torsion modules equipped with a quadratic form
    # taking values in QQ/2ZZ) are a further subcategory.
    DiscriminantForms = LazyImport("src.lattices.categories.quadratic_modules", "TorsionQuadraticModules")

    class ParentMethods:
        r"""
        Additional interface for torsion bilinear modules.
        """

        @abstract_method
        def invariants(self):
            r"""
            Return the invariant factors `(d_1, \ldots, d_k)` of the
            underlying torsion module.

            The underlying module is isomorphic to
            `\mathbb{Z}/d_1 \oplus \cdots \oplus \mathbb{Z}/d_k`
            with `d_1 \mid d_2 \mid \cdots \mid d_k`.

            EXAMPLES::

                sage: T = TorsionBilinearModule.from_invariants_and_gram(   # not tested
                ....:     [2, 4], matrix(QQ, [[0, QQ(1,4)], [QQ(1,4), 0]]))   # not tested
                sage: T.invariants()   # not tested
                (2, 4)
            """

        @abstract_method
        def is_p_elementary(self, p):
            r"""
            Return ``True`` iff ``self`` is `p`-elementary, i.e., every
            element has order dividing `p`.

            Equivalently, `p \cdot T = 0`.

            EXAMPLES::

                sage: A_L = Lattice.U().twist(2).discriminant_group()   # not tested
                sage: A_L.is_p_elementary(2)   # not tested
                True
            """

        @abstract_method
        def p_part(self, p):
            r"""
            Return the `p`-primary part `T_{(p)} = \{v \in T \mid
            p^k v = 0 \text{ for some } k\}` as a bilinear module.

            EXAMPLES::

                sage: T.p_part(2)   # not tested
                ...
            """

        # --- Derived overrides ---

        def free_part(self):
            r"""
            Return the free part.

            A torsion module has trivial free part (the zero module).
            """
            ...  # return zero free module

        def torsion_part(self):
            r"""
            Return the torsion submodule.

            For a torsion module, this is ``self``.
            """
            return self

        def cardinality(self):
            r"""
            Return the cardinality of the underlying set.

            A finitely generated torsion module is finite; its cardinality
            is the product of its invariant factors.

            EXAMPLES::

                sage: A_L = Lattice.U().twist(2).discriminant_group()   # not tested
                sage: A_L.cardinality()   # not tested
                4
            """
            from sage.misc.misc_c import prod

            return prod(self.invariants())

        @abstract_method
        def jordan_decomposition(self):
            r"""
            Return the Jordan decomposition of this torsion bilinear
            module.

            For `R = \mathbb{Z}`, the Jordan decomposition expresses
            `T` as an orthogonal direct sum of `p`-elementary pieces
            of a specific local normal form.

            OUTPUT: a list of `(p, block_matrix, rank)` triples.
            """

    class ElementMethods:
        r"""
        Additional interface for elements of torsion bilinear modules.
        """

        @abstract_method
        def additive_order(self):
            r"""
            Return the additive order of this element.

            EXAMPLES::

                sage: g = A_L.gens()[0]   # not tested
                sage: g.additive_order()   # not tested
                2
            """

        @abstract_method
        def lift(self):
            r"""
            Return a lift of this element to the dual lattice.

            For a discriminant group element `\bar{v} \in A_L = L^*/L`,
            this returns a representative `\tilde{v} \in L^*` satisfying
            `\pi(\tilde{v}) = \bar{v}`, where `\pi: L^* \to A_L` is the
            projection.

            OUTPUT: an element of `L^*` (a dual lattice element).

            EXAMPLES::

                sage: g = A_L.gens()[0]   # not tested
                sage: g.lift() in L.dual()   # not tested
                True
                sage: A_L(g.lift()) == g   # not tested
                True
            """

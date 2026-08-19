r"""
Lattices

A *lattice* is a free `\mathbb{Z}`-module of finite rank equipped with
a nondegenerate symmetric `\mathbb{Z}`-bilinear form.

Formally: an object of ``FreeBilinearModules(ZZ).NonDegenerate()``.

This category covers the lattices appearing in algebraic geometry
(Nikulin, Looijenga, Miranda-Morrison): indefinite, unimodular,
hyperbolic, K3 lattice, etc.  It does **not** assume positive
definiteness.

EXAMPLES::

    sage: Lattice.U() in Lattices(ZZ)   # not tested
    True
    sage: Lattices(ZZ)   # not tested
    Category of lattices over Integer Ring
"""
# ****************************************************************************
#  Copyright (C) 2024  The research project authors
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport


class Lattices(CategoryWithAxiom_over_base_ring):
    r"""
    The category of integral lattices (free `\mathbb{Z}`-modules with
    nondegenerate symmetric bilinear form).

    An object is a pair `(L, \beta)` where `L \cong \mathbb{Z}^n` and
    `\beta: L \times L \to \mathbb{Z}` is symmetric and nondegenerate.
    Nondegeneracy means `\det(G_L) \neq 0`.

    Morphisms are `\mathbb{Z}`-linear maps; isometries additionally
    satisfy `\beta_M(f(v), f(w)) = \beta_L(v, w)`.

    EXAMPLES::

        sage: Lattices(ZZ)   # not tested
        Category of lattices over Integer Ring
        sage: Lattice.U() in Lattices(ZZ)   # not tested
        True

    .. SEEALSO::

        :mod:`src.lattices.categories.free_bilinear_modules`,
        :mod:`src.lattices.categories.rational_lattices`
    """

    def super_categories(self):
        from sage.rings.integer_ring import ZZ
        from src.lattices.categories.free_bilinear_modules import FreeBilinearModules

        return [FreeBilinearModules(ZZ)]

    # -----------------------------------------------------------------------
    # Notable subcategories
    # -----------------------------------------------------------------------

    EvenLattices = LazyImport("src.lattices.categories.even_lattices", "EvenLattices")
    UnimodularLattices = LazyImport("src.lattices.categories.unimodular_lattices", "UnimodularLattices")
    RootLattices = LazyImport("src.lattices.categories.root_lattices", "RootLattices")

    class SubcategoryMethods:
        @cached_method
        def Even(self):
            r"""
            Return the full subcategory of even lattices.

            A lattice is *even* iff `\beta(v, v) \in 2\mathbb{Z}` for
            all `v`.  Equivalently, all diagonal entries of the Gram
            matrix are even.

            EXAMPLES::

                sage: Lattices(ZZ).Even()   # not tested
                Category of even lattices over Integer Ring
            """
            return self._with_axiom("Even")

        @cached_method
        def Unimodular(self):
            r"""
            Return the full subcategory of unimodular lattices.

            A lattice is *unimodular* iff `|\det(G_L)| = 1`.
            Equivalently, `L = L^*`.

            EXAMPLES::

                sage: Lattice.II(0, 8).is_unimodular()   # not tested
                True
            """
            return self._with_axiom("Unimodular")

    # -----------------------------------------------------------------------
    # ParentMethods
    # -----------------------------------------------------------------------

    class ParentMethods:
        r"""
        Abstract interface for integral lattices.
        """

        # --- Invariants ---

        @abstract_method
        def signature_pair(self):
            r"""
            Return the signature `(p, q)` where `p` (resp. `q`) is the
            number of positive (resp. negative) eigenvalues of the Gram
            matrix over `\mathbb{R}`.

            EXAMPLES::

                sage: Lattice.U().signature_pair()   # not tested
                (1, 1)
                sage: Lattice.E(8).signature_pair()   # not tested
                (8, 0)
            """

        def signature(self):
            r"""
            Return the signature `p - q` (the index).

            EXAMPLES::

                sage: Lattice.U().signature()   # not tested
                0
                sage: Lattice.E(8).signature()   # not tested
                8
            """
            p, q = self.signature_pair()
            return p - q

        @abstract_method
        def determinant(self):
            r"""
            Return `\det(G_L)`, the determinant of the Gram matrix.

            EXAMPLES::

                sage: Lattice.U().determinant()   # not tested
                -1
                sage: Lattice.A(1).determinant()   # not tested
                -2
            """

        def discriminant(self):
            r"""
            Return the discriminant `|\det(G_L)|`.

            EXAMPLES::

                sage: Lattice.U().discriminant()   # not tested
                1
            """
            return abs(self.determinant())

        @abstract_method
        def is_even(self):
            r"""
            Return ``True`` iff this lattice is even:
            `\beta(v, v) \in 2\mathbb{Z}` for all `v`.

            EXAMPLES::

                sage: Lattice.U().is_even()   # not tested
                True
                sage: Lattice.Z().is_even()   # not tested
                False
            """

        def is_odd(self):
            r"""Return ``True`` iff this lattice is not even."""
            return not self.is_even()

        def is_unimodular(self):
            r"""Return ``True`` iff `|\det(G_L)| = 1`."""
            return self.discriminant() == 1

        @abstract_method
        def nikulin_invariants(self):
            r"""
            Return the Nikulin invariants `(l, \delta)` of the discriminant
            group, where:

            - `l` = minimal number of generators of `A_L`
            - `\delta = 0` if `A_L` is 2-elementary with `q(v) \in
              \mathbb{Z}/\mathbb{Z}` for all `v`; `\delta = 1` otherwise

            EXAMPLES::

                sage: Lattice.U().twist(2).nikulin_invariants()   # not tested
                (2, 2, 0)
            """

        # --- Discriminant descent: L → L* → A_L ---

        @abstract_method
        def dual(self):
            r"""
            Return the dual lattice `L^* = \mathrm{Hom}_{\mathbb{Z}}(L,
            \mathbb{Z})`.

            `L^*` is a rational lattice.  As a `\mathbb{Z}`-submodule of
            `L \otimes \mathbb{Q}`, it consists of vectors `v` such that
            `\beta(v, w) \in \mathbb{Z}` for all `w \in L`.

            The inclusion `\iota_L: L \hookrightarrow L^*` sends
            `v \mapsto \beta(v, \cdot)`.

            EXAMPLES::

                sage: L = Lattice.U().twist(2)   # not tested
                sage: Lstar = L.dual()   # not tested
                sage: L.gram_matrix()   # not tested
                [0 2]
                [2 0]
                sage: Lstar.gram_matrix()   # not tested
                [0 1/2]
                [1/2 0]
            """

        @abstract_method
        def inclusion_morphism(self):
            r"""
            Return the inclusion `\iota_L: L \to L^*`.

            The map `\iota_L` sends `v \mapsto \beta(v, \cdot)`, a
            `\mathbb{Z}`-linear functional.  Its matrix w.r.t. canonical
            generators is the Gram matrix `G_L`.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: iota = L.inclusion_morphism()   # not tested
                sage: iota.to_matrix()   # not tested
                [0 1]
                [1 0]
            """

        @abstract_method
        def discriminant_group(self):
            r"""
            Return the discriminant group `A_L = L^* / L`.

            `A_L` is a finite abelian group, computed as the cokernel of
            `\iota_L: L \to L^*`.  It is equipped with:

            - A bilinear form `b: A_L \times A_L \to \mathbb{Q}/\mathbb{Z}`
            - A quadratic form `q: A_L \to \mathbb{Q}/2\mathbb{Z}` (the
              *discriminant form*)

            EXAMPLES::

                sage: A = Lattice.U().twist(2).discriminant_group()   # not tested
                sage: A.cardinality()   # not tested
                4
                sage: A.invariants()   # not tested
                (2, 2)
            """

        # --- Isometry comparisons ---

        @abstract_method
        def is_isometric_to(self, other, witness=False):
            r"""
            Return whether ``self`` is isometric to ``other``.

            An isometry is an `R`-module isomorphism preserving the
            bilinear form.

            INPUT:

            - ``other`` -- a lattice
            - ``witness`` -- boolean (default: ``False``); if ``True``,
              return a pair ``(bool, isometry_or_None)``

            EXAMPLES::

                sage: Lattice.U().is_isometric_to(Lattice.U())   # not tested
                True
                sage: L, w = Lattice.U().is_isometric_to(Lattice.U(), witness=True)   # not tested
                sage: w in Lattice.U().O()   # not tested
                True
            """

        @abstract_method
        def is_rationally_isometric_to(self, other):
            r"""
            Return whether ``self`` and ``other`` are isometric as
            rational lattices (i.e., after tensoring with `\mathbb{Q}`).

            EXAMPLES::

                sage: U2 = Lattice.U().twist(2)   # not tested
                sage: U2_split = Lattice.from_gram(diagonal_matrix(ZZ, [2, -2]))   # not tested
                sage: U2.is_rationally_isometric_to(U2_split)   # not tested
                True
            """

        @abstract_method
        def is_locally_isometric_to(self, other, p):
            r"""
            Return whether ``self`` and ``other`` are `p`-adically
            isometric (isometric over `\mathbb{Z}_p`).

            EXAMPLES::

                sage: U2.is_locally_isometric_to(U2_split, 2)   # not tested
                False
            """

        def genus(self):
            r"""
            Return the genus of ``self``: the set of all lattices locally
            isometric to ``self`` at all primes and over `\mathbb{R}`.

            EXAMPLES::

                sage: Lattice.U().genus()   # not tested
                Genus of U
            """
            ...

        # --- Orthogonal group ---

        def O(self):
            r"""
            Return the orthogonal group `O(L)` of ``self``.

            `O(L)` consists of all isometries `L \to L`.

            EXAMPLES::

                sage: O = Lattice.U().O()   # not tested
                sage: O.cardinality()   # not tested
                4
            """
            return self.End().Aut()

        def orthogonal_group(self):
            r"""Alias for :meth:`O`."""
            return self.O()

        # --- Subobjects ---

        @abstract_method
        def rational_span(self):
            r"""
            Return `L \otimes_{\mathbb{Z}} \mathbb{Q}`, the ambient
            rational lattice.

            EXAMPLES::

                sage: Lattice.U().rational_span().base_ring()   # not tested
                Rational Field
            """

        @abstract_method
        def to_quadratic_module(self):
            r"""
            Return the quadratic module associated to ``self``.

            For an even lattice `(L, \beta)`, returns the quadratic
            module `(L, q)` where `q(v) = \beta(v, v) / 2`.

            Raises ``ValueError`` for odd lattices (where
            `\beta(v,v)/2 \notin \mathbb{Z}` for some `v`).

            EXAMPLES::

                sage: Q = Lattice.E(8).to_quadratic_module()   # not tested
                sage: Q.quadratic_gram_matrix().diagonal()   # not tested
                (1, 1, 1, 1, 1, 1, 1, 1)
            """

    # -----------------------------------------------------------------------
    # ElementMethods
    # -----------------------------------------------------------------------

    class ElementMethods:
        r"""
        Additional interface for elements of integral lattices.
        """

        @abstract_method
        def norm(self):
            r"""
            Return `\beta(v, v)`, the self-product of this element.

            This is an element of `\mathbb{Z}`.  For even lattices, the
            quadratic form value is `q(v) = \mathrm{norm}(v) / 2`.

            EXAMPLES::

                sage: e, f = Lattice.U().gens()   # not tested
                sage: e.norm()   # not tested
                0
            """

        def is_isotropic(self):
            r"""
            Return ``True`` iff `\beta(v, v) = 0`.

            EXAMPLES::

                sage: Lattice.U().gens()[0].is_isotropic()   # not tested
                True
            """
            return self.norm() == 0

        @abstract_method
        def is_root(self):
            r"""
            Return ``True`` iff `v` is a root: `\beta(v, v) \in \{-2, 2\}`.

            EXAMPLES::

                sage: (Lattice.A(1).gens()[0]).is_root()   # not tested
                True
            """

        def reflection(self):
            r"""
            Return the reflection through ``self``.

            The reflection `s_v: L \to L` is defined by
            `s_v(w) = w - \frac{2\beta(v,w)}{\beta(v,v)} v`.

            Requires `\beta(v, v) \neq 0`.

            EXAMPLES::

                sage: v = (Lattice.A(1).gens()[0])   # not tested
                sage: s = v.reflection()   # not tested
                sage: s(v) == -v   # not tested
                True
            """
            ...

        def perp(self):
            r"""
            Return the orthogonal complement of ``self`` in the parent.

            `v^\perp = \{w \in L \mid \beta(v, w) = 0\}`.

            EXAMPLES::

                sage: e, f = Lattice.U().gens()   # not tested
                sage: e.perp()   # not tested
                Sublattice generated by e in U
            """
            return self.parent().span([g for g in self.parent().gens() if self.parent().b(self, g) == 0])

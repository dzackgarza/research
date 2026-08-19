r"""
Bilinear Modules

A *bilinear module* over a commutative ring `R` is an `R`-module `M`
equipped with a symmetric `R`-bilinear form

.. MATH::

    \beta: M \times M \to C

where `C` is a subring of `K := R.\mathrm{fraction\_field}()`, or a
quotient thereof (e.g. `\mathbb{Q}/\mathbb{Z}` for torsion modules).

This category supersedes Sage's fragmented lattice/module hierarchy
(`FreeModule`, `FGP_Module`, `TorsionQuadraticModule`, `QuadraticForm`,
`IntegralLattice`, ...) with a unified DSL suited to indefinite lattice
theory in algebraic geometry (Nikulin, Looijenga, Miranda-Morrison).

The internal Sage objects carried by any concrete parent are
*calculation engines*, never the public API.  Methods on concrete
parents must use mathematical names (``gram_matrix``, not
``inner_product_matrix``; ``Hom``, not ``_Hom_``).
"""
# ****************************************************************************
#  Copyright (C) 2024  The research project authors
#
#  Distributed under the terms of the GNU General Public License (GPL)
# ****************************************************************************

from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport


class BilinearModules(Category_module):
    r"""
    The category of bilinear modules over a commutative ring `R`.

    An object is a pair `(M, \beta)` where `M` is an `R`-module and
    `\beta: M \times M \to C` is a symmetric `R`-bilinear form,
    with `C` a subring of `K = R.\mathrm{fraction\_field}()` (or a
    quotient, e.g. `\mathbb{Q}/\mathbb{Z}`).

    A morphism `f: (M, \beta_M) \to (N, \beta_N)` is an `R`-module map.
    An *isometry* is a morphism additionally satisfying
    `\beta_N(f(v), f(w)) = \beta_M(v, w)` for all `v, w \in M`.

    EXAMPLES::

        sage: BilinearModules(ZZ)   # not tested
        Category of bilinear modules over Integer Ring

    .. SEEALSO::

        :class:`~src.lattices.categories.free_bilinear_modules.FreeBilinearModules`,
        :class:`~src.lattices.categories.torsion_bilinear_modules.TorsionBilinearModules`,
        :class:`~src.lattices.categories.quadratic_modules.QuadraticModules`,
        :class:`~src.lattices.categories.lattices.Lattices`
    """

    def super_categories(self):
        """
        Return the immediate super categories.

        EXAMPLES::

            sage: BilinearModules(ZZ).super_categories()   # not tested
            [Category of modules over Integer Ring]
        """
        return [Modules(self.base_ring())]

    def additional_structure(self):
        r"""
        Return ``None``.

        A module morphism between two bilinear modules is not automatically
        an isometry; the bilinear structure is additional data.

        EXAMPLES::

            sage: BilinearModules(ZZ).additional_structure()   # not tested
        """
        return None

    # -----------------------------------------------------------------------
    # Subcategory declarations (lazy to avoid import cycles)
    # -----------------------------------------------------------------------

    Free = LazyImport("src.lattices.categories.free_bilinear_modules", "FreeBilinearModules")
    Torsion = LazyImport("src.lattices.categories.torsion_bilinear_modules", "TorsionBilinearModules")
    WithQuadraticForm = LazyImport("src.lattices.categories.quadratic_modules", "QuadraticModules")

    # -----------------------------------------------------------------------
    # SubcategoryMethods  (available on any subcategory of BilinearModules)
    # -----------------------------------------------------------------------

    class SubcategoryMethods:
        @cached_method
        def base_ring(self):
            r"""
            Return the base ring for ``self``.

            Delegates upward through super-categories until a
            ``base_ring`` attribute is found.

            EXAMPLES::

                sage: BilinearModules(ZZ).Free().base_ring()   # not tested
                Integer Ring
            """
            for C in self.super_categories():
                if hasattr(C, "base_ring"):
                    return C.base_ring()
            raise AttributeError(f"no super category of {self} has a base_ring")

        @cached_method
        def Free(self):
            r"""
            Return the full subcategory of free objects in ``self``.

            EXAMPLES::

                sage: BilinearModules(ZZ).Free()   # not tested
                Category of free bilinear modules over Integer Ring
            """
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
            r"""
            Return the full subcategory of torsion objects in ``self``.

            EXAMPLES::

                sage: BilinearModules(ZZ).Torsion()   # not tested
                Category of torsion bilinear modules over Integer Ring
            """
            return self._with_axiom("Torsion")

        @cached_method
        def WithQuadraticForm(self):
            r"""
            Return the subcategory of objects equipped with a quadratic form.

            EXAMPLES::

                sage: BilinearModules(ZZ).WithQuadraticForm()   # not tested
                Category of quadratic modules over Integer Ring
            """
            return self._with_axiom("WithQuadraticForm")

    # -----------------------------------------------------------------------
    # ParentMethods
    # -----------------------------------------------------------------------

    class ParentMethods:
        r"""
        Abstract interface for parents in :class:`BilinearModules`.

        Every parent must implement all ``@abstract_method`` entries.
        The remaining methods are derived from those.

        A bilinear form ``β: M × M → C`` has codomain ``C`` a subring
        of ``R.fraction_field()`` (or a quotient such as ``QQ/ZZ``).
        Concretely: ``ZZ`` for integral lattices, ``QQ`` for rational
        lattices, ``QQ/ZZ`` for discriminant groups.  The codomain is
        obtained as ``self.bilinear_form().codomain()``.
        """

        @abstract_method
        def bilinear_form(self):
            r"""
            Return the bilinear form `\beta` on this module.

            OUTPUT: a ``BilinearForm`` object whose ``codomain()`` is a
            subring of ``self.base_ring().fraction_field()`` (or a
            quotient thereof).

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: L.bilinear_form()   # not tested
                Bilinear form on U with Gram matrix [0 1 / 1 0]
            """

        @abstract_method
        def gens(self):
            r"""
            Return the canonical generators of this module as a tuple.

            OUTPUT: a tuple of :class:`BilinearModuleElement` objects.
            The ordering is consistent but not necessarily canonical
            in any further sense.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: L.gens()   # not tested
                (e, f)
            """

        @abstract_method
        def zero(self):
            r"""
            Return the additive identity of this module.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: L.zero()   # not tested
                0
            """

        @abstract_method
        def base_ring(self):
            r"""
            Return the base ring `R`.

            EXAMPLES::

                sage: Lattice.U().base_ring()   # not tested
                Integer Ring
            """

        @abstract_method
        def free_part(self):
            r"""
            Return the free part of this module as a bilinear module.

            - For free modules: returns ``self``.
            - For torsion modules: returns the rank-0 zero module.

            EXAMPLES::

                sage: Lattice.U().free_part()   # not tested
                U
            """

        @abstract_method
        def torsion_part(self):
            r"""
            Return the torsion submodule as a bilinear module.

            - For free modules: returns the zero module.
            - For torsion modules: returns ``self``.

            EXAMPLES::

                sage: Lattice.U().torsion_part()   # not tested
                0
            """

        @abstract_method
        def Hom(self, other):
            r"""
            Return the hom space ``Hom(self, other)`` in
            ``BilinearModules(R)``.

            This is the **public** API.  Internally it may use the
            stored Sage object's ``_Hom_`` hook, but that is an
            implementation detail never exposed.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: H = L.Hom(L)   # not tested
                sage: H   # not tested
                Hom(U, U) in Category of lattices over Integer Ring
            """

        @abstract_method
        def dual(self):
            r"""
            Return the dual module ``Hom_R(M, R)``.

            For a lattice `L`, the dual `L^* = \{v \in L \otimes K
            \mid \beta(v, L) \subseteq R\}` is a rational lattice whose
            elements are `R`-linear functionals on `L`.

            EXAMPLES::

                sage: Lattice.U().dual()   # not tested
                Dual of U
            """

        @abstract_method
        def twist(self, scalar):
            r"""
            Return this module with its form scaled by ``scalar``.

            The underlying `R`-module is unchanged; only the bilinear
            form changes: `\beta_{\mathrm{new}}(v, w) = s \cdot \beta(v, w)`.
            The Gram matrix becomes ``scalar * G``.

            .. WARNING::

                This is **NOT** the same as ``scalar * self``.
                ``scalar * self`` is the submodule `\{s \cdot v \mid v
                \in M\}` with Gram matrix ``scalar^2 * G``.

            EXAMPLES::

                sage: Lattice.U().twist(2).gram_matrix()   # not tested
                [0 2]
                [2 0]
            """

        @abstract_method
        def span(self, elements):
            r"""
            Return the sub-bilinear-module generated by ``elements``,
            with the bilinear form restricted from ``self``.

            OUTPUT: a bilinear module `S \hookrightarrow M` with the
            same base ring.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e, f = L.gens()   # not tested
                sage: L.span([e])   # not tested
                Sublattice of rank 1 in U
            """

        @abstract_method
        def cardinality(self):
            r"""
            Return the cardinality of the underlying set.

            Every set has a cardinality; this method is axiomatic.

            - For free modules: returns ``Infinity``.
            - For finite torsion modules: returns a positive integer.

            EXAMPLES::

                sage: Lattice.U().cardinality()   # not tested
                +Infinity
            """

        # --- Derived methods (not abstract) ---

        def b(self, v, w):
            r"""
            Evaluate the bilinear form: `\beta(v, w)`.

            Convenience wrapper for
            ``self.bilinear_form().evaluate(v, w)``.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e, f = L.gens()   # not tested
                sage: L.b(e, f)   # not tested
                1
            """
            return self.bilinear_form().evaluate(v, w)

        def gram_matrix(self):
            r"""
            Return the Gram matrix `G_{ij} = \beta(e_i, e_j)` for the
            canonical generators.

            Entries lie in ``self.bilinear_form().codomain()``.

            EXAMPLES::

                sage: Lattice.U().gram_matrix()   # not tested
                [0 1]
                [1 0]
            """
            return self.bilinear_form().gram_matrix()

        def End(self):
            r"""
            Return the endomorphism algebra ``End(M) = Hom(M, M)``.

            EXAMPLES::

                sage: Lattice.U().End()   # not tested
                End(U) in Category of lattices over Integer Ring
            """
            return self.Hom(self)

        def symbolic_form(self, variable_names=None):
            r"""
            Return the bilinear form as a polynomial expression
            `x^T G y` in symbolic variables.

            The bilinear form `\beta` on a free module of rank `n` is
            represented as a symmetric matrix `G` (the Gram matrix).
            The symbolic form is the polynomial

            .. MATH::

                \beta(x, y) = \sum_{i,j} G_{ij} x_i y_j

            in `2n` variables `(x_1, \ldots, x_n, y_1, \ldots, y_n)`.

            INPUT:

            - ``variable_names`` -- list of `2n` names, or ``None`` for
              ``['x0',...,'x{n-1}','y0',...,'y{n-1}']``

            EXAMPLES::

                sage: Lattice.U().symbolic_form()   # not tested
                x0*y1 + x1*y0
            """
            ...

        def direct_sum(self, other):
            r"""
            Return the direct sum `M \oplus N` with block-diagonal form.

            Prefer the ``+`` operator; this is its implementation hook.

            EXAMPLES::

                sage: Lattice.U().direct_sum(Lattice.U()).rank()   # not tested
                4
            """
            ...

        def __add__(self, other):
            r"""
            Return the direct sum `M \oplus N`.

            EXAMPLES::

                sage: (Lattice.U() + Lattice.U()).rank()   # not tested
                4
            """
            return self.direct_sum(other)

        def __pow__(self, n):
            r"""
            Return the `n`-fold direct sum `M^{\oplus n}`.

            EXAMPLES::

                sage: (Lattice.U()^3).rank()   # not tested
                6
            """
            if n == 0:
                ...  # return zero module
            result = self
            for _ in range(n - 1):
                result = result.direct_sum(self)
            return result

        def __mul__(self, scalar):
            r"""
            Return the submodule `\{s \cdot v \mid v \in M\}`.

            This is **not** ``self.twist(scalar)``.  The submodule has
            Gram matrix ``scalar^2 * G`` and is isometric to
            ``self.twist(scalar^2)``.

            For `M = R` as an `R`-module, ``scalar * M`` is the ideal
            `(scalar)` in `R`.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: (2 * L).gram_matrix()   # not tested
                [0 4]
                [4 0]
                sage: L.twist(2).gram_matrix()   # not tested
                [0 2]
                [2 0]
            """
            ...

        def __rmul__(self, scalar):
            r"""Return the submodule ``{scalar * v : v in self}``."""
            return self.__mul__(scalar)

    # -----------------------------------------------------------------------
    # ElementMethods
    # -----------------------------------------------------------------------

    class ElementMethods:
        r"""
        Abstract interface for elements of bilinear modules.
        """

        @abstract_method
        def parent(self):
            r"""Return the parent bilinear module of this element."""

        @abstract_method
        def __add__(self, other):
            r"""Return ``self + other`` in the parent module."""

        @abstract_method
        def __neg__(self):
            r"""Return ``-self``."""

        @abstract_method
        def __rmul__(self, scalar):
            r"""Return ``scalar * self``."""

        @abstract_method
        def __eq__(self, other):
            r"""Return whether ``self == other``."""

        @abstract_method
        def __hash__(self):
            r"""Return a hash consistent with ``__eq__``."""

        @abstract_method
        def to_vector(self):
            r"""
            Return the coordinate vector w.r.t. ``self.parent().gens()``.

            This is a basis-dependent extraction; the basis is given
            by the canonical generators.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e, f = L.gens()   # not tested
                sage: e.to_vector()   # not tested
                (1, 0)
            """

        # --- Derived ---

        def __mul__(self, other):
            r"""
            Return `\beta(\mathrm{self}, \mathrm{other})`, the bilinear
            product of ``self`` and ``other``.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e, f = L.gens()   # not tested
                sage: e * f   # not tested
                1
            """
            return self.parent().b(self, other)

        def self_product(self):
            r"""
            Return `\beta(v, v)`, the bilinear self-product.

            .. WARNING::

                This is **not** a quadratic form value.  A quadratic
                form `q` satisfies `\beta_q(v, v) = 2q(v)`, so
                `q(v) = \beta(v,v)/2` only when 2 is invertible.
                In ``QuadraticModules``, use ``.q()`` instead.

                Over `\mathbb{Z}`, for an even lattice, the quadratic
                form value is ``self.norm() // 2``.

            EXAMPLES::

                sage: L = Lattice.U()   # not tested
                sage: e, f = L.gens()   # not tested
                sage: e.self_product()   # not tested
                0
            """
            return self.parent().b(self, self)

        def is_isotropic(self):
            r"""
            Return ``True`` iff `\beta(v, v) = 0` for this element.

            For a quadratic module, use ``.q() == 0`` instead (the two
            conditions agree iff `2` is invertible in the base ring).

            EXAMPLES::

                sage: Lattice.U().gens()[0].is_isotropic()   # not tested
                True
            """
            return self.self_product() == 0

        def span(self):
            r"""
            Return the sub-bilinear-module generated by ``self``.

            EXAMPLES::

                sage: e = Lattice.U().gens()[0]   # not tested
                sage: e.span()   # not tested
                Sublattice of rank 1 in U
            """
            return self.parent().span([self])

        def __sub__(self, other):
            r"""Return ``self - other = self + (-other)``."""
            return self + (-other)

    # -----------------------------------------------------------------------
    # MorphismMethods
    # -----------------------------------------------------------------------

    class MorphismMethods:
        r"""
        Abstract interface for morphisms in :class:`BilinearModules`.

        Mixed into the element class of every
        ``Hom(M, N)`` in this category.

        A morphism is an `R`-linear map `f: M \to N`.
        An *isometry* additionally satisfies
        `\beta_N(f(v), f(w)) = \beta_M(v, w)`.
        """

        @abstract_method
        def domain(self):
            r"""Return the domain module `M`."""

        @abstract_method
        def codomain(self):
            r"""Return the codomain module `N`."""

        @abstract_method
        def __call__(self, v):
            r"""
            Evaluate the morphism: return `f(v) \in N`.

            Must satisfy additivity and `R`-linearity:
            ``f(v + w) == f(v) + f(w)`` and ``f(r*v) == r*f(v)``.
            """

        @abstract_method
        def to_matrix(self):
            r"""
            Return the matrix of `f` w.r.t. the canonical generators
            of domain and codomain.

            Column `j` contains the coordinates of `f(e_j)` in
            ``codomain().gens()``.
            """

        @abstract_method
        def kernel(self):
            r"""
            Return `\ker(f)` as a bilinear module, with the form
            restricted from the domain.
            """

        @abstract_method
        def image(self):
            r"""
            Return `\mathrm{im}(f)` as a bilinear module, with the form
            restricted from the codomain.
            """

        @abstract_method
        def cokernel(self):
            r"""
            Return `\mathrm{coker}(f) = N / \mathrm{im}(f)` as a
            bilinear module, with the descended form.

            Automatic category promotion applies: if `f = \iota_L: L
            \to L^*`, the cokernel is promoted to a
            ``DiscriminantGroup``.
            """

        @abstract_method
        def is_isometry(self):
            r"""
            Return ``True`` iff `f` preserves the bilinear form:
            `\beta_N(f(v), f(w)) = \beta_M(v, w)` for all `v, w`.
            """

        # --- Derived ---

        def is_injective(self):
            r"""Return ``True`` iff ``self.kernel()`` is the zero module."""
            return self.kernel() == self.domain().category()(self.domain().base_ring()).zero()

        def is_surjective(self):
            r"""Return ``True`` iff ``self.cokernel()`` is the zero module."""
            return self.cokernel() == self.codomain().category()(self.codomain().base_ring()).zero()

        def is_bijective(self):
            r"""Return ``True`` iff ``self`` is injective and surjective."""
            return self.is_injective() and self.is_surjective()

        def is_isomorphism(self):
            r"""Return ``True`` iff ``self`` is a bijective morphism."""
            return self.is_bijective()

        def __mul__(self, other):
            r"""
            Return the composition `(\mathrm{self} \circ \mathrm{other})(v)
            = \mathrm{self}(\mathrm{other}(v))`.
            """
            ...

        def direct_sum(self, other):
            r"""
            Return the direct sum morphism
            `f \oplus g: M_1 \oplus M_2 \to N_1 \oplus N_2`.
            """
            ...

    # -----------------------------------------------------------------------
    # Homsets
    # -----------------------------------------------------------------------

    class Homsets(HomsetsCategory):
        r"""
        The category of hom sets `\mathrm{Hom}(M, N)` for bilinear modules.

        Each hom set is itself an `R`-module (morphisms can be added and
        scaled).  Morphisms in an *isometry* hom set additionally satisfy
        the form-preservation condition checked in ``__contains__``.
        """

        def extra_super_categories(self):
            r"""
            A hom set of `R`-bilinear modules is an `R`-module.

            EXAMPLES::

                sage: BilinearModules(ZZ).Homsets().extra_super_categories()   # not tested
                [Category of modules over Integer Ring]
            """
            return [Modules(self.base_category().base_ring())]

        def base_ring(self):
            r"""Return the base ring of this homset category."""
            return self.base_category().base_ring()

        class ParentMethods:
            r"""
            Abstract interface for hom sets ``Hom(M, N)``.
            """

            @cached_method
            def base_ring(self):
                r"""Return the base ring from the domain."""
                return self.domain().base_ring()

            @abstract_method
            def element_from_dict(self, mapping):
                r"""
                Construct a morphism from a ``{generator: image}`` dict.

                This is the **preferred** construction: it names the
                images of each generator explicitly.

                INPUT:

                - ``mapping`` -- dict from ``self.domain().gens()`` to
                  elements of ``self.codomain()``

                EXAMPLES::

                    sage: L = Lattice.U()   # not tested
                    sage: e, f = L.gens()   # not tested
                    sage: H = L.Hom(L)   # not tested
                    sage: swap = H.element_from_dict({e: f, f: e})   # not tested
                """

            @abstract_method
            def element_from_matrix(self, M):
                r"""
                Construct a morphism from a matrix `M` w.r.t. the
                canonical generators of domain and codomain.

                Column `j` of `M` gives the image of the `j`-th
                generator of ``self.domain()``.

                EXAMPLES::

                    sage: H = Lattice.U().Hom(Lattice.U())   # not tested
                    sage: H.element_from_matrix(matrix(ZZ, [[0,1],[1,0]]))   # not tested
                """

            @abstract_method
            def element_from_images(self, images):
                r"""
                Construct a morphism from an ordered list of images of
                the domain generators.

                EXAMPLES::

                    sage: H = Lattice.U().Hom(Lattice.U())   # not tested
                    sage: e, f = Lattice.U().gens()   # not tested
                    sage: H.element_from_images([f, e])   # not tested
                """

            @abstract_method
            def __contains__(self, f):
                r"""
                Return ``True`` iff ``f`` is a valid morphism in this
                hom set.

                For plain hom sets: checks that ``f`` is an `R`-module
                map ``M → N``.

                For isometry hom sets: additionally checks the
                form-preservation condition
                `\beta_N(f(v), f(w)) = \beta_M(v, w)`.

                .. NOTE::

                    Matrices are **not** elements of hom sets::

                        sage: matrix(ZZ, [[0,1],[1,0]]) not in Lattice.U().Hom(Lattice.U())  # not tested
                        True
                """

            def identity(self):
                r"""
                Return the identity morphism ``id: M → M``.

                Only defined when ``self.domain() == self.codomain()``.
                """
                assert self.domain() == self.codomain(), "identity requires domain == codomain"
                from sage.matrix.constructor import identity_matrix

                n = len(self.domain().gens())
                return self.element_from_matrix(identity_matrix(self.domain().base_ring(), n))

            def zero(self):
                r"""Return the zero morphism ``0: M → N``."""
                from sage.matrix.constructor import zero_matrix

                n = len(list(self.domain().gens()))
                m = len(list(self.codomain().gens()))
                return self.element_from_matrix(zero_matrix(self.domain().base_ring(), m, n))

        class Endset(CategoryWithAxiom_over_base_ring):
            r"""
            The category of endomorphism sets ``End(M)`` for a bilinear
            module `M`.

            ``End(M)`` is a (non-commutative) ring; its unit group
            ``Aut(M)`` is the automorphism group of `M`.
            """

            def extra_super_categories(self):
                r"""
                ``End(M)`` is a magmatic algebra over `R`.

                EXAMPLES::

                    sage: BilinearModules(ZZ).Endsets().extra_super_categories()   # not tested
                    [Category of magmatic algebras over Integer Ring]
                """
                from sage.categories.magmatic_algebras import MagmaticAlgebras

                return [MagmaticAlgebras(self.base_category().base_ring())]

            class ParentMethods:
                @abstract_method
                def Aut(self):
                    r"""
                    Return the automorphism group of the underlying module.

                    For a lattice, ``L.End().Aut()`` is the *isometry*
                    group.  For a general bilinear module it is the group
                    of invertible module endomorphisms.
                    """

    # -----------------------------------------------------------------------
    # CartesianProducts
    # -----------------------------------------------------------------------

    class CartesianProducts(CartesianProductsCategory):
        r"""
        Bilinear modules constructed as (external) direct products.

        The direct product `M_1 \times M_2` carries the bilinear form
        `\beta((v_1, v_2), (w_1, w_2)) = \beta_1(v_1, w_1) +
        \beta_2(v_2, w_2)`.  This coincides with the direct sum when
        both factors are finitely generated.
        """

        def extra_super_categories(self):
            r"""
            A Cartesian product of bilinear modules is a bilinear module.

            EXAMPLES::

                sage: BilinearModules(ZZ).CartesianProducts().extra_super_categories()   # not tested
                [Category of bilinear modules over Integer Ring]
            """
            return [self.base_category()]

        class ParentMethods:
            @abstract_method
            def summands(self):
                r"""Return the tuple of summands `(M_1, \ldots, M_k)`."""

        class ElementMethods:
            def _lmul_(self, scalar):
                r"""Return ``scalar * self`` component-wise."""
                return self.parent()._cartesian_product_of_elements(scalar * v for v in self.cartesian_factors())

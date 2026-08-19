r"""
Quadratic Modules

A *quadratic module* over a commutative ring `R` is an `R`-module `M`
equipped with a quadratic form

.. MATH::

    q: M \to C

where `C` is a subring of `K = R.\mathrm{fraction\_field}()` (or a
quotient such as `\mathbb{Q}/2\mathbb{Z}`), satisfying:

1. `q(r \cdot v) = r^2 \cdot q(v)` for all `r \in R`, `v \in M`
2. The map `\beta_q: M \times M \to C` defined by
   `\beta_q(v, w) = q(v + w) - q(v) - q(w)` is `R`-bilinear.

The bilinear form `\beta_q` is the *associated* or *polar* form of `q`.
Note `\beta_q(v, v) = q(2v) - 2q(v) = 2q(v)` (using homogeneity); so
`\beta_q(v, v) = 2q(v)`, **not** `q(v)` in general.

Quadratic forms and symmetric bilinear forms are *distinct* structures
when `2 \notin R^\times`.  There is a natural map

.. MATH::

    \phi: \mathrm{Quad}_R(M) \to \mathrm{Bil}_R(M), \quad q \mapsto \beta_q

and a map in the other direction (only when `2` is a unit):

.. MATH::

    \psi: \mathrm{Bil}_R(M) \to \mathrm{Quad}_R(M), \quad
    \beta \mapsto q_\beta \text{ where } q_\beta(v) = \tfrac{1}{2}\beta(v, v)

Over `\mathbb{Z}`, this distinction matters:

- An *even* integral lattice `(L, \beta)` has `\beta(v, v) \in 2\mathbb{Z}`,
  so `q(v) = \beta(v, v) / 2 \in \mathbb{Z}` is a well-defined integral
  quadratic form.
- An *odd* integral lattice has `\beta(v, v) \in \mathbb{Z}` but
  `\beta(v, v) / 2 \notin \mathbb{Z}` for some `v`.
- The discriminant group of any integral lattice carries a canonical
  quadratic form `q: A_L \to \mathbb{Q}/2\mathbb{Z}` (while its bilinear
  form takes values in `\mathbb{Q}/\mathbb{Z}`).

Matrix and symbolic representations
------------------------------------

A quadratic form on a free module of rank `n` has two equivalent
representations:

1. **Matrix representation**: a symmetric matrix `M` such that
   `q(v) = v^T M v` for coordinate vectors `v`.  Note the matrix of
   the polar form `\beta_q` is `M + M^T = 2M` (for symmetric `M`).

2. **Symbolic representation**: the polynomial `q(x_1, \ldots, x_n) =
   \sum_{i \le j} m_{ij} x_i x_j` obtained by substituting a vector of
   variables.  Recovering `M` from the symbolic form: `m_{ij} =
   \partial^2 q / \partial x_i \partial x_j` for `i < j` (off-diagonal),
   `m_{ii} = q(e_i)` (diagonal).

Passing between bilinear and quadratic representations
-------------------------------------------------------

Use ``quadratic_module.associated_bilinear_module()`` to get the
associated bilinear module `(M, \beta_q)`.

Use ``bilinear_module.to_quadratic_module()`` to get a quadratic
module from a bilinear one (requires that `q(v) = \beta(v,v)/2` is
well-defined, e.g., for even lattices).
"""
# ****************************************************************************
#  Copyright (C) 2024  The research project authors
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method


class QuadraticModules(CategoryWithAxiom_over_base_ring):
    r"""
    The category of quadratic modules over a commutative ring `R`.

    Objects are pairs `(M, q)` where `q: M \to C` is a quadratic form.
    The axiom name is ``"WithQuadraticForm"``; use
    ``BilinearModules(R).WithQuadraticForm()``.

    Every quadratic module is also a bilinear module via the polar form
    `\beta_q(v, w) = q(v+w) - q(v) - q(w)`.

    .. SEEALSO::

        :mod:`src.lattices.categories.bilinear_modules`
    """

    class ParentMethods:
        r"""
        Abstract interface for quadratic modules.

        A quadratic module `(M, q)` carries both the quadratic form
        `q: M \to C` and the associated bilinear form `\beta_q`.
        """

        @abstract_method
        def quadratic_form(self):
            r"""
            Return the quadratic form `q` on this module.

            OUTPUT: a ``QuadraticForm`` object with ``codomain()`` a
            subring of ``self.base_ring().fraction_field()`` (or a
            quotient such as ``QQ/2ZZ``).

            EXAMPLES::

                sage: A_L = Lattice.U().twist(2).discriminant_group()   # not tested
                sage: A_L.quadratic_form()   # not tested
                Quadratic form on A_L with values in QQ/2ZZ
            """

        @abstract_method
        def quadratic_gram_matrix(self):
            r"""
            Return the matrix `M` such that `q(v) = v^T M v` for
            coordinate vectors `v`.

            For a quadratic form on a free module of rank `n`, this is a
            symmetric `n \times n` matrix over the codomain ring.

            Note the matrix of the polar form `\beta_q` is `M + M^T = 2M`.

            EXAMPLES::

                sage: L = Lattice.E(8)   # not tested
                sage: Q = L.to_quadratic_module()   # not tested
                sage: Q.quadratic_gram_matrix()   # not tested
                # (diagonal entries are q(e_i) = 1 for E8)
            """

        def associated_bilinear_module(self):
            r"""
            Return the bilinear module `(M, \beta_q)` associated to
            ``self`` via the polar form.

            The polar form is `\beta_q(v, w) = q(v+w) - q(v) - q(w)`.
            Note: `\beta_q(v, v) = 2q(v)`, so the associated bilinear
            form is the *double* of what one might naively expect.

            EXAMPLES::

                sage: Q = Lattice.E(8).to_quadratic_module()   # not tested
                sage: B = Q.associated_bilinear_module()   # not tested
                sage: B.gram_matrix() == 2 * Q.quadratic_gram_matrix()   # not tested
                True
            """
            ...

        def symbolic_form(self, variable_names=None):
            r"""
            Return the quadratic form as a polynomial in ``n`` variables.

            INPUT:

            - ``variable_names`` -- list of variable names, or ``None``
              for ``['x0', ..., 'x{n-1}']``

            OUTPUT: a polynomial ``sum_{i <= j} m_ij * xi * xj``
            where `M = (m_{ij})` is the Gram matrix.

            EXAMPLES::

                sage: Q.symbolic_form(['x', 'y'])   # not tested
                x^2 + x*y + y^2
            """
            ...

    class ElementMethods:
        r"""
        Abstract interface for elements of quadratic modules.
        """

        @abstract_method
        def q(self):
            r"""
            Return the quadratic value `q(\mathrm{self})`.

            This is the value of the quadratic form, **not** the bilinear
            product `\beta(\mathrm{self}, \mathrm{self})`.  The two are
            related by `\beta_q(v, v) = 2 q(v)` when `\beta_q` is the
            polar form of `q`.

            EXAMPLES::

                sage: A_L = Lattice.U().twist(2).discriminant_group()   # not tested
                sage: g = A_L.gens()[0]   # not tested
                sage: g.q()   # a value in QQ/2ZZ   # not tested
                0
            """

        def is_isotropic(self):
            r"""
            Return ``True`` iff `q(\mathrm{self}) = 0` in the
            quadratic module.

            For modules where `2` is a unit this is equivalent to
            `\beta(v, v) = 0`; over `\mathbb{Z}` these can differ.

            EXAMPLES::

                sage: g = A_L.gens()[0]   # not tested
                sage: g.is_isotropic()   # not tested
                True
            """
            return self.q() == 0


class TorsionQuadraticModules(CategoryWithAxiom_over_base_ring):
    r"""
    The category of torsion quadratic modules (discriminant forms).

    A *torsion quadratic module* is a finitely generated torsion
    `R`-module `T` equipped with a quadratic form `q: T \to C`
    where `C` is typically `\mathbb{Q}/2\mathbb{Z}` (for `R =
    \mathbb{Z}`), together with the associated bilinear form
    `b: T \times T \to \mathbb{Q}/\mathbb{Z}`.

    The prototypical example is the discriminant form of an integral
    lattice: for an integral lattice `(L, \beta)`, the discriminant
    group `A_L = L^*/L` carries:

    - A bilinear form `b: A_L \times A_L \to \mathbb{Q}/\mathbb{Z}`,
      `b(\bar{u}, \bar{v}) = \beta(u, v) \mod \mathbb{Z}` for lifts
      `u, v \in L^*`.
    - A quadratic form `q: A_L \to \mathbb{Q}/2\mathbb{Z}`,
      `q(\bar{v}) = \beta(v, v) \mod 2\mathbb{Z}` for a lift `v \in L^*`.

    This is the discriminant form of `L`.
    """

    class ParentMethods:
        @abstract_method
        def signature_pair(self):
            r"""
            Return the signature `(p, q)` of the discriminant form,
            where `p - q \equiv \sigma(L) \pmod{8}` for the associated
            lattice `L`.

            This is an invariant in `\mathbb{Z}/8\mathbb{Z}`.
            """

        @abstract_method
        def isotropic_elements(self):
            r"""
            Return the set of isotropic elements `\{v \in T \mid q(v) = 0\}`.

            EXAMPLES::

                sage: A_L = Lattice.U().twist(2).discriminant_group()   # not tested
                sage: A_L.isotropic_elements()   # not tested
                {0, g1, g2}
            """

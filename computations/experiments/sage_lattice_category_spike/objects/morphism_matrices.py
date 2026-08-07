r"""The matrix extracted from a morphism of free R-modules.

A ``MorphismMatrix`` is the matrix of a morphism $f:M\to N$ of free
$R$-modules with respect to chosen generating sets: its rows express
$f(e_i)$ in the generators of $N$.  It is *extracted from* a morphism and
means nothing without one.

It is categorically different from a ``GramMatrix``, which is the array
$[b(e_i,e_j)]$ of a form $M\otimes M\to W$ and represents no morphism at
all.  That the correlation $c:L\to L^\vee$, $v\mapsto b(v,-)$, is
represented by a matrix coinciding with the Gram matrix in dual generating
sets is a coincidence of coordinates, not an identity of objects.  The two
types exist to stop that conflation.

Kernels are the seam.  A *morphism* has a kernel: a module with its own
abstract generators, together with the inclusion recording how those
generators are written in $M$'s.  A *matrix* has only a nullspace, and Sage
hands it back as a submodule spanned by a basis inside an ambient module --
which is what forces the ambient-module bookkeeping this repo eschews.  So
``_left_kernel_matrix`` and ``_right_kernel_matrix`` are private: they
return matrices, never modules, and only a morphism calls them.

Consequently this class does not subclass Sage's ``Matrix``.  Sage builds
the result of every operation through the ``MatrixSpace`` parent, so a
subclass is silently discarded by ``+``, ``*`` and every factory -- the
banned surface would reappear on the first arithmetic step.  Composition
holds the invariant: an operation exists here or it does not exist at all.
"""

from __future__ import annotations

from copy import copy
from typing import Any, TYPE_CHECKING

from sage.matrix.constructor import matrix as _matrix
from sage.structure.element import Matrix


if TYPE_CHECKING:
    from ..lexicon import (
        Element,
        BaseRing,
        Cardinal,
        CategoryMorphism,
        Integer,
        Rational,
        RawMorphismMatrix,
        Ring,
    )

__all__ = ["MorphismMatrix"]


class MorphismMatrix:
    r"""The matrix of a morphism of free $R$-modules in chosen generating sets."""

    def __init__(self, entries: "RawMorphismMatrix", base_ring: "BaseRing" = None) -> None:
        match entries:
            case MorphismMatrix():
                built = entries._matrix
            case Matrix():
                built = entries
            case _:
                assert base_ring is not None, (
                    "a morphism matrix built from raw entries needs its base ring"
                )
                built = _matrix(base_ring, entries)
        if base_ring is not None and built.base_ring() is not base_ring:
            built = built.change_ring(base_ring)
        self._matrix = built

    # -- the private escape ------------------------------------------------
    #
    # Reading the underlying Sage matrix is how the DSL's own constructions
    # (a form pulled back along a morphism, a presentation stacked onto its
    # relations) do their linear algebra.  It is private because a caller
    # that holds a raw Sage matrix holds ``basis`` and ``left_kernel`` again.

    def _sage_matrix(self) -> Matrix:
        r"""Return the underlying Sage matrix. DSL-internal."""
        return self._matrix

    def _matrix_(self, base_ring: "Ring" = None) -> Matrix:
        r"""Sage's conversion protocol, so ``M in G`` works as containment.

        Asking whether a morphism matrix lies in a matrix group is ordinary
        containment and should read as ``M in G``.  Sage's parents convert
        through this protocol, so declaring it is what makes the plain idiom
        work -- rather than a bespoke predicate that would say the same thing
        in a name only this repo knows.
        """
        return self._matrix if base_ring is None else self._matrix.change_ring(base_ring)

    # -- shape and entries -------------------------------------------------

    def base_ring(self) -> "Ring":
        return self._matrix.base_ring()

    def nrows(self) -> int:
        return self._matrix.nrows()

    def ncols(self) -> int:
        return self._matrix.ncols()

    def dimensions(self) -> tuple:
        r"""Return ``(nrows, ncols)``: the sizes of the two framings."""
        return (self.nrows(), self.ncols())

    def rank(self) -> "Cardinal":
        return self._matrix.rank()

    def det(self) -> "Rational":
        return self._matrix.det()

    def trace(self) -> "Element":
        r"""Return $\operatorname{tr}$ of the endomorphism this presents.

        A conjugation invariant, so the value belongs to the endomorphism and
        not to the generating set it is written in.  That is exactly what
        makes $g\mapsto\operatorname{tr}\rho(g)$ constant on conjugacy classes
        and so a class function on $G$.
        """
        return self._matrix.trace()

    def is_zero(self) -> bool:
        return bool(self._matrix.is_zero())

    def is_one(self) -> bool:
        r"""Return whether this is the matrix of an identity morphism.

        Asked instead of comparing against ``identity_matrix``: equality here
        holds only between morphism matrices, so a raw identity would compare
        unequal to everything.
        """
        return bool(self._matrix.is_one())

    def rows(self) -> list:
        return self._matrix.rows()

    def list(self) -> list:
        return self._matrix.list()

    def __getitem__(self, key: "Integer") -> "Element":
        return self._matrix[key]

    # -- operations that stay morphism matrices ----------------------------

    def transpose(self) -> "MorphismMatrix":
        r"""Return the matrix of the dual morphism $f^t:N^\vee\to M^\vee$.

        A morphism has no "transpose" as such; what it has is a dual, and
        the dual's matrix in the dual generating sets is this one.
        """
        return MorphismMatrix(self._matrix.transpose())

    def inverse(self) -> "MorphismMatrix":
        r"""Return the matrix of the inverse morphism."""
        return MorphismMatrix(self._matrix.inverse())

    def change_ring(self, ring: "Ring") -> "MorphismMatrix":
        return MorphismMatrix(self._matrix.change_ring(ring))

    def stack(self, other: object) -> "MorphismMatrix":
        return MorphismMatrix(self._matrix.stack(_underlying(other)))

    def hermite_form(
        self, transformation: bool = False, **kwargs: Any
    ) -> "MorphismMatrix | tuple":
        r"""Return the Hermite form, with its transformation when asked.

        ``transformation=True`` makes Sage return the pair $(H,U)$ with
        $H=UA$, so the pair is rewrapped rather than handed to the
        constructor as one object.
        """
        if transformation:
            reduced, transform = self._matrix.hermite_form(
                transformation=True, **kwargs
            )
            return (MorphismMatrix(reduced), MorphismMatrix(transform))
        return MorphismMatrix(self._matrix.hermite_form(**kwargs))

    def normal_form(self, include_zero_rows: bool = False) -> "MorphismMatrix":
        r"""Return the row-reduced form appropriate to the base ring.

        Which normal form reduces a family of rows is a fact about the base
        ring -- Hermite over a PID, echelon over a field -- and not about the
        caller.  Every site that needs "these rows, reduced" asks here, so
        that branch is written once instead of being restated wherever a
        span, an index, or a presentation is computed.
        """
        base_ring = self._matrix.base_ring()
        if base_ring.is_field():
            reduced = self._matrix.echelon_form()
            if not include_zero_rows:
                reduced = reduced.matrix_from_rows(
                    [i for i, row in enumerate(reduced.rows()) if not row.is_zero()]
                )
            return MorphismMatrix(reduced)
        return MorphismMatrix(
            self._matrix.hermite_form(include_zero_rows=include_zero_rows)
        )

    def smith_form(self) -> tuple:
        normal, left, right = self._matrix.smith_form()
        return (
            MorphismMatrix(normal),
            MorphismMatrix(left),
            MorphismMatrix(right),
        )

    def __mul__(self, other: object) -> "CategoryMorphism":
        product = self._matrix * _underlying(other)
        return MorphismMatrix(product) if isinstance(product, Matrix) else product

    def __rmul__(self, other: object) -> "MorphismMatrix":
        product = _underlying(other) * self._matrix
        return MorphismMatrix(product) if isinstance(product, Matrix) else product

    # -- nullspaces: private, and matrices ---------------------------------

    def _left_kernel_matrix(self) -> "MorphismMatrix":
        r"""Return the rows spanning $\{x : xA = 0\}$. Callers: morphisms only."""
        return MorphismMatrix(self._matrix.left_kernel_matrix())

    def _right_kernel_matrix(self) -> "MorphismMatrix":
        r"""Return the rows spanning $\{x : Ax = 0\}$. Callers: morphisms only."""
        return MorphismMatrix(self._matrix.right_kernel_matrix())

    # -- subdivisions are display data -------------------------------------

    def subdivide(self, *args: Any) -> None:
        self._matrix.subdivide(*args)

    def subdivisions(self) -> tuple:
        return self._matrix.subdivisions()

    # -- identity ----------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        return isinstance(other, MorphismMatrix) and self._matrix == other._matrix

    def __hash__(self) -> int:
        # Sage refuses to hash a mutable matrix, and the wrapped matrix stays
        # mutable because ``subdivide`` writes display data onto it.  So the
        # entries are hashed through a frozen copy.
        entries = copy(self._matrix)
        entries.set_immutable()
        return hash(("MorphismMatrix", entries))

    def __repr__(self) -> str:
        return repr(self._matrix)

    def _latex_(self) -> "str":
        from sage.misc.latex import latex

        return latex(self._matrix)


def matrix_group(generators: "Iterable[MorphismMatrix]") -> Any:
    r"""Return the GAP-backed matrix group these generate.

    Handing a group to GAP is the one legitimate reason to unwrap these
    matrices, and it happens here because this module owns the wrapping.  A
    caller that did the unwrapping itself would hold raw Sage matrices --
    ``basis`` and ``left_kernel`` and all -- which is what ``_sage_matrix``
    is private to prevent.  Callers ask for the group and translate GAP's
    answers back into their own elements.
    """
    from sage.groups.matrix_gps.finitely_generated import MatrixGroup

    generators = tuple(generators)
    assert generators, "a matrix group needs a generator"
    assert all(
        isinstance(generator, MorphismMatrix) for generator in generators
    ), "a matrix group here is generated by morphism matrices"
    return MatrixGroup([generator._matrix for generator in generators])


def _underlying(value: "Element") -> "Matrix":
    return value._sage_matrix() if isinstance(value, MorphismMatrix) else value

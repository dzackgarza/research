"""Matrix-algebra categories."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from ..algebras import Algebras
from ..cat import Category
from ..modules import Modules
from .subcategories.constructions.parameterized import _Category_over_base_integer_pair

if TYPE_CHECKING:
    from collections.abc import Sequence

    from ..types import FreeModule, Matrix, MatrixSpace, Ring, RingElement


class _MatrixAlgebras(_Category_over_base_integer_pair):
    r"""Category of rings of square matrices over a base ring.

    ``_MatrixAlgebras(R, n, n)`` is the category whose single object is
    ``MatrixSpace(R, n, n)``.

    Constructor target: square ``Rings().Constructors().MatrixRing(R, n)`` and
    square matrix-space constructors refine here.
    """

    def __init__(self, base_ring: Ring, n: Integer, m: Integer):
        assert Integer(n) == Integer(m), "matrix rings require square matrix spaces"
        super().__init__(base_ring, n, m)

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"rings of {self._n} by {self._n} matrices over {self._base_ring}"

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        from sage.matrix.matrix_space import MatrixSpace

        return (
            isinstance(R, MatrixSpace)
            and R.base_ring() == self.base_ring()
            and Integer(R.nrows()) == self.nrows()
            and Integer(R.ncols()) == self.ncols()
        )

    @final
    def object(self) -> Ring:
        from sage.matrix.matrix_space import MatrixSpace

        return MatrixSpace(self.base_ring(), self.nrows(), self.ncols())

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        cats: list[Category] = [
            Algebras(R),
            Modules(R).Free().FiniteRank(),
        ]
        if self._n == 1:
            from .subcategories.commutative import _CommutativeRings

            if R in _CommutativeRings():
                cats.append(_CommutativeRings())
        return cats

    class ParentMethods:
        @abstract_method
        def nrows(self) -> Integer: ...

        @abstract_method
        def ncols(self) -> Integer: ...

        @abstract_method
        def dims(self) -> tuple[Integer, Integer]: ...

        @abstract_method
        def matrix_from_matrix(self, matrix: Matrix, *, coerce: bool = True) -> RingElement:
            r"""Return the matrix-algebra element represented by ``matrix``."""
            ...

        @abstract_method
        def matrix_from_entries(self, entries: Sequence[RingElement], *, coerce: bool = True) -> RingElement:
            r"""Return the matrix whose entries are listed in row-major order."""
            ...

        @abstract_method
        def matrix_from_rows(self, rows: Sequence[Sequence[RingElement]], *, coerce: bool = True) -> RingElement:
            r"""Return the matrix whose rows are ``rows``."""
            ...

        @abstract_method
        def scalar_matrix(self, scalar: RingElement, *, coerce: bool = True) -> RingElement:
            r"""Return the scalar matrix determined by ``scalar``."""
            ...

        @abstract_method
        def rank(self) -> Integer: ...

        @abstract_method
        def echelon_form(
            self,
            algorithm: str | None = "default",
            cutoff: Integer = Integer(0),
            height_guess: Integer | None = None,
            proof: bool | None = None,
            include_zero_rows: bool = True,
            transformation: bool = False,
            D: RingElement | None = None,
        ) -> RingElement | tuple[RingElement, RingElement]: ...

        @abstract_method
        def column_space(self) -> FreeModule: ...

        @abstract_method
        def row_space(self) -> FreeModule: ...

        @abstract_method
        def diagonal_matrix(self, entries: Sequence[RingElement]) -> RingElement: ...

        @abstract_method
        def identity_matrix(self) -> RingElement: ...

        @abstract_method
        def zero_matrix(self) -> RingElement: ...

        @abstract_method
        def matrix_space(
            self,
            nrows: Integer | None = None,
            ncols: Integer | None = None,
            sparse: bool = False,
        ) -> MatrixSpace: ...

        @abstract_method
        def from_vector(
            self,
            vector: RingElement,
            order: Sequence[tuple[Integer, Integer]] | None = None,
            coerce: bool = True,
        ) -> RingElement: ...

        @abstract_method
        def is_dense(self) -> bool: ...

        @abstract_method
        def is_sparse(self) -> bool: ...

    class ElementMethods: ...
    class MorphismMethods: ...

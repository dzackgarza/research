"""Matrix-algebra categories."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ..algebras import Algebras
from ..cat import Category
from ..modules import Modules
from .subcategories.constructions.parameterized import _Category_over_base_integer_pair

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

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

        matrix_space_type: type[Any] = MatrixSpace
        return (
            isinstance(R, matrix_space_type)
            and R.base_ring() == self.base_ring()
            and Integer(R.nrows()) == self.nrows()
            and Integer(R.ncols()) == self.ncols()
        )

    @final
    def object(self) -> Ring:
        from sage.matrix.matrix_space import MatrixSpace

        matrix_space_factory: Callable[[Ring, Integer, Integer], Ring] = MatrixSpace
        return matrix_space_factory(self.base_ring(), self.nrows(), self.ncols())

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
        @final
        def is_commutative_ring(self) -> bool:
            if self.nrows() == 1:
                return bool(self.base_ring().is_commutative())
            try:
                return bool(self.base_ring().is_zero())
            except NotImplementedError:
                return False

        @final
        def is_integral_domain(self) -> bool:
            return self.nrows() == 1 and bool(self.base_ring().is_integral_domain())

        @final
        def is_field(self) -> bool:
            return self.nrows() == 1 and bool(self.base_ring().is_field())

        @final
        def nrows(self) -> Integer:
            from sage.matrix.matrix_space import MatrixSpace

            return MatrixSpace.nrows(self)

        @final
        def ncols(self) -> Integer:
            from sage.matrix.matrix_space import MatrixSpace

            return MatrixSpace.ncols(self)

        @final
        def dims(self) -> tuple[Integer, Integer]:
            from sage.matrix.matrix_space import MatrixSpace

            dims_method: Callable[[Any], tuple[Integer, Integer]] = MatrixSpace.dims
            return dims_method(self)

        @final
        def matrix_from_matrix(
            self, matrix: Matrix, *, coerce: bool = True
        ) -> RingElement:
            r"""Return the matrix-algebra element represented by ``matrix``."""
            from sage.matrix.matrix_space import MatrixSpace

            matrix_method: Callable[..., RingElement] = MatrixSpace.matrix
            return matrix_method(self, matrix, coerce=coerce)

        @final
        def matrix_from_entries(
            self, entries: Sequence[RingElement], *, coerce: bool = True
        ) -> RingElement:
            r"""Return the matrix whose entries are listed in row-major order."""
            from sage.matrix.matrix_space import MatrixSpace

            matrix_method: Callable[..., RingElement] = MatrixSpace.matrix
            return matrix_method(self, entries, coerce=coerce)

        @final
        def matrix_from_rows(
            self, rows: Sequence[Sequence[RingElement]], *, coerce: bool = True
        ) -> RingElement:
            r"""Return the matrix whose rows are ``rows``."""
            from sage.matrix.matrix_space import MatrixSpace

            matrix_method: Callable[..., RingElement] = MatrixSpace.matrix
            return matrix_method(self, rows, coerce=coerce)

        @final
        def scalar_matrix(
            self, scalar: RingElement, *, coerce: bool = True
        ) -> RingElement:
            r"""Return the scalar matrix determined by ``scalar``."""
            from sage.matrix.matrix_space import MatrixSpace

            matrix_method: Callable[..., RingElement] = MatrixSpace.matrix
            return matrix_method(self, scalar, coerce=coerce)

        @final
        def rank(self) -> Integer:
            return Integer(self.nrows() * self.ncols())

        @abstractmethod
        def echelon_form(
            self,
            algorithm: str | None = "default",
            cutoff: Integer = Integer(0),
            height_guess: Integer | None = None,
            proof: bool | None = None,
            include_zero_rows: bool = True,
            transformation: bool = False,
            D: RingElement | None = None,
        ) -> RingElement | tuple[RingElement, RingElement]:
            ...

        @final
        def column_space(self) -> FreeModule:
            from sage.matrix.matrix_space import MatrixSpace

            column_space_method: Callable[[Any], FreeModule] = MatrixSpace.column_space
            return column_space_method(self)

        @final
        def row_space(self) -> FreeModule:
            from sage.matrix.matrix_space import MatrixSpace

            row_space_method: Callable[[Any], FreeModule] = MatrixSpace.row_space
            return row_space_method(self)

        @final
        def diagonal_matrix(self, entries: Sequence[RingElement]) -> RingElement:
            from sage.matrix.matrix_space import MatrixSpace

            diagonal_method: Callable[[Any, Sequence[RingElement]], RingElement] = (
                MatrixSpace.diagonal_matrix
            )
            return diagonal_method(self, entries)

        @final
        def identity_matrix(self) -> RingElement:
            from sage.matrix.matrix_space import MatrixSpace

            matrix_method: Callable[..., RingElement] = MatrixSpace.matrix
            return matrix_method(self, self.base_ring().one())

        @final
        def zero_matrix(self) -> RingElement:
            from sage.matrix.matrix_space import MatrixSpace

            matrix_method: Callable[..., RingElement] = MatrixSpace.matrix
            return matrix_method(self, self.base_ring().zero())

        @final
        def matrix_space(
            self,
            nrows: Integer | None = None,
            ncols: Integer | None = None,
            sparse: bool = False,
        ) -> MatrixSpace:
            from sage.matrix.matrix_space import MatrixSpace

            return MatrixSpace.matrix_space(
                self, nrows=nrows, ncols=ncols, sparse=sparse
            )

        @final
        def from_vector(
            self,
            vector: RingElement,
            order: Sequence[tuple[Integer, Integer]] | None = None,
            coerce: bool = True,
        ) -> RingElement:
            from sage.matrix.matrix_space import MatrixSpace

            from_vector_method: Callable[..., RingElement] = MatrixSpace.from_vector
            return from_vector_method(self, vector, order=order, coerce=coerce)

        @final
        def is_dense(self) -> bool:
            from sage.matrix.matrix_space import MatrixSpace

            is_dense_method: Callable[[Any], bool] = MatrixSpace.is_dense
            return is_dense_method(self)

        @final
        def is_sparse(self) -> bool:
            from sage.matrix.matrix_space import MatrixSpace

            is_sparse_method: Callable[[Any], bool] = MatrixSpace.is_sparse
            return is_sparse_method(self)

    class ElementMethods: ...

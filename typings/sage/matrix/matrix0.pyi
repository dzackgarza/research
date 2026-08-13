# Repo-scoped stubs; see lexicon/README.md.
#
# Sage's concrete matrix base, declaring the mathematically true MRO edge to
# ``sage.structure.element.Matrix`` (sage/matrix/matrix0.pyx:
# ``cdef class Matrix(sage.structure.element.Matrix)``), which is the lexicon
# noun ``Matrix``. Modules that import the matrix class from here therefore
# get the noun itself, and the matrix contract shared by every
# ``sage.structure.element.Matrix`` stays stated once, on the noun. Members
# below are the exception: they are defined only in the concrete
# matrix0 < matrix1 < matrix2 chain this class models, so the noun cannot
# honestly carry them.
from typing import Generic, overload

from typing_extensions import TypeVar

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import Matrix as _NounMatrix
from sage.structure.element import RingElement, Vector

_Scalar = TypeVar("_Scalar", bound=RingElement, default=Integer | Rational)

class Matrix(_NounMatrix[_Scalar], Generic[_Scalar]):
    # matrix2.pyx:15783 / matrix2.pyx:15657 — definiteness of a symmetric
    # matrix, decided on the block-diagonal decomposition.
    def is_positive_definite(self) -> bool: ...
    def is_positive_semidefinite(self) -> bool: ...
    # element.pyx:3617 (the noun's __mul__), restated with the return
    # narrowed to this class: a product of concrete matrices is a concrete
    # matrix, so products keep the chain members above.
    @overload
    def __mul__(self, other: _NounMatrix[_Scalar]) -> Matrix[_Scalar]: ...
    @overload
    def __mul__(self, other: Vector[_Scalar]) -> Vector[_Scalar]: ...
    @overload
    def __mul__(self, other: int | _Scalar) -> Matrix[_Scalar]: ...

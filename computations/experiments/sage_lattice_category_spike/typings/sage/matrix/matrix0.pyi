# Repo-scoped stubs; see lexicon/README.md.
#
# Sage's concrete matrix base, declaring the mathematically true MRO edge to
# ``sage.structure.element.Matrix`` (sage/matrix/matrix0.pyx:
# ``cdef class Matrix(sage.structure.element.Matrix)``), which is the lexicon
# noun ``Matrix``. Modules that import the matrix class from here therefore
# get the noun itself, and the whole matrix contract stays stated once, on
# the noun.
from typing import Generic

from typing_extensions import TypeVar

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import Matrix as _NounMatrix
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=Integer | Rational)

class Matrix(_NounMatrix[_Scalar], Generic[_Scalar]): ...

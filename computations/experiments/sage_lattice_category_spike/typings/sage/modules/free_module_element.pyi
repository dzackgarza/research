# General vector-element contract; generic in the scalar with the exact
# ZZ/QQ regime as default (see structure/element.pyi). Verified by
# lexicon/verify_against_sage.py.
from typing import Any, Generic, overload

from typing_extensions import TypeVar

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import Matrix, RingElement, Vector

_Scalar = TypeVar("_Scalar", bound=RingElement, default=Integer | Rational)

class FreeModuleElement(Vector[_Scalar], Generic[_Scalar]):
    # Arithmetic is closed on concrete free-module elements.
    def __neg__(self) -> FreeModuleElement[_Scalar]: ...
    def __add__(self, other: Vector[_Scalar]) -> FreeModuleElement[_Scalar]: ...
    def __sub__(self, other: Vector[_Scalar]) -> FreeModuleElement[_Scalar]: ...
    @overload
    def __mul__(self, other: Matrix[_Scalar]) -> FreeModuleElement[_Scalar]: ...
    @overload
    def __mul__(self, other: Vector[_Scalar]) -> _Scalar: ...
    @overload
    def __mul__(self, other: int | _Scalar) -> FreeModuleElement[_Scalar]: ...
    def __rmul__(self, other: int | _Scalar) -> FreeModuleElement[_Scalar]: ...

# The exact ZZ/QQ regime is this repo's default scalar union (INVENTORY III):
# entries of exact vectors are Integer | Rational whichever exact base ring
# built them, so composition with default-parametrized Matrix/Vector is seamless.
def vector(*args: Any, **kwds: Any) -> FreeModuleElement[Integer | Rational]: ...

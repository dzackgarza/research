# General vector-element contract; generic in the scalar, defaulting to its
# bound RingElement — the entries of a vector over R are elements of R (see
# structure/element.pyi). Verified by lexicon/verify_against_sage.py.
from collections.abc import Iterable
from typing import Generic, TypeVar, overload

from sage.modules.free_module import FreeModule_generic
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import Matrix, RingElement, Vector
from sage.categories.rings import Rings

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class FreeModuleElement(Vector[_Scalar], Generic[_Scalar]):
    def parent(self) -> FreeModule_generic[_Scalar]: ...
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
    def __floordiv__(self, other: int | _Scalar) -> FreeModuleElement[_Scalar]: ...
    def norm(self) -> _Scalar: ...

# The exact ZZ/QQ regime, stated explicitly (INVENTORY III): entries of exact
# vectors are Integer | Rational whichever exact base ring built them.
@overload
def vector(
    entries: Iterable[int | Integer | Rational],
    *,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[Integer | Rational]: ...
@overload
def vector(
    base_ring: Rings.ParentMethods[_Scalar],
    entries: Iterable[int | _Scalar],
    *,
    sparse: bool | None = ...,
    immutable: bool = ...,
) -> FreeModuleElement[_Scalar]: ...

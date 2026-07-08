# General vector-element contract; generic in the scalar with the exact
# ZZ/QQ regime as default (see structure/element.pyi). Verified by
# lexicon/verify_against_sage.py.
from typing import Any, Generic

from typing_extensions import TypeVar

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import RingElement, Vector

_Scalar = TypeVar("_Scalar", bound=RingElement, default=Integer | Rational)

class FreeModuleElement(Vector[_Scalar], Generic[_Scalar]): ...

def vector(*args: Any, **kwds: Any) -> FreeModuleElement[Any]: ...

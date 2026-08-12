# Repo-scoped stubs; see lexicon/README.md.
#
# An ideal of a principal ideal domain: generic in the ring's element type,
# with the exact ZZ regime as the default (INVENTORY.md Part III, scalar
# parametrization). A PID ideal is exactly its one generator.
from typing import Generic

from typing_extensions import TypeVar

from sage.rings.integer import Integer
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=Integer)

class Ideal_pid(Generic[_Scalar]):
    def gen(self, i: int = ...) -> _Scalar: ...
    def gens(self) -> tuple[_Scalar, ...]: ...
    def is_zero(self) -> bool: ...

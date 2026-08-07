# Repo-scoped stubs; see lexicon/README.md.
from sage.structure.element import RingElement

# The extended reals: negation is an endomap (involution) of the set
# R u {+oo, -oo}; +oo and -oo are elements of one type, and -(x) is an
# element of the same type, never of the opposite pole's class.
class PlusInfinity(RingElement):
    def __neg__(self) -> PlusInfinity | MinusInfinity: ...

class MinusInfinity(RingElement):
    def __neg__(self) -> PlusInfinity | MinusInfinity: ...

Infinity: PlusInfinity

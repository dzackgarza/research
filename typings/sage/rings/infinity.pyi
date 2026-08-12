# Repo-scoped stubs; see lexicon/README.md.
from sage.structure.element import RingElement

# The extended reals: negation exchanges the poles, -(+oo) = -oo.  That is
# more precise than any LSP-compatible signature (the supertype returns its
# own class), so the override is the mathematics and carries the exception.
class PlusInfinity(RingElement):
    def __neg__(self) -> MinusInfinity: ...

class MinusInfinity(RingElement):
    def __neg__(self) -> PlusInfinity: ...

Infinity: PlusInfinity
infinity: PlusInfinity

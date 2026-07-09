# Repo-scoped stubs; see lexicon/README.md.
from sage.structure.element import RingElement

class PlusInfinity(RingElement):
    def __neg__(self) -> MinusInfinity: ...

class MinusInfinity(RingElement):
    def __neg__(self) -> PlusInfinity: ...

Infinity: PlusInfinity

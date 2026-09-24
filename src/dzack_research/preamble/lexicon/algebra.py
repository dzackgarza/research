"""General algebra nouns used by active preamble signatures."""

from typing import Any

from sage.rings.ring import Ring
from sage.structure.element import Element, Matrix, ModuleElement, RingElement

BaseRing = Ring

# An object of the owned category of monoids.  The active grading surface admits
# both multiplicative and additive monoids, whose generated ObjectType classes
# are selected from the runtime grading datum.
type MonoidObject = Any

__all__ = [
    "BaseRing",
    "Element",
    "Matrix",
    "ModuleElement",
    "MonoidObject",
    "RingElement",
]

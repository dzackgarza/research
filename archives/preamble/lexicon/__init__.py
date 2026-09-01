r"""The lexicon: single import surface for the preamble's typed language.

Re-export only — every noun is defined in exactly one module. Downstream
preamble code draws from here:

    from ..lexicon import Element, Matrix, OrderedSet

The dependency runs one way: ``objects`` draws on ``lexicon``, and the
lexicon draws on nothing but Sage. The nouns ``objects`` itself defines are
therefore imported from their own modules, never re-exported here. Doing so would make
``lexicon`` and ``objects`` import each other, a cycle that survives only
under one hand-arranged import order.
"""

from .algebra import (
    BaseRing,
    Element,
    Matrix,
    ModuleElement,
    RingElement,
)
from .foundations import (
    CartanType,
    GramMatrix,
    Integer,
    LatticeName,
    OrderedSet,
    Rational,
    RealApproximation,
    RealNumber,
    SignaturePair,
    SymbolicExpression,
)
from .geometry import (
    CoxeterMatrix,
    Graph,
    Polyhedron,
)
from .interop import (
    SageCategory,
    SageElement,
    SageMorphism,
    SageParent,
    SageUniqueRepresentation,
)

__all__ = [
    # foundations
    "CartanType",
    "GramMatrix",
    "Integer",
    "LatticeName",
    "OrderedSet",
    "Rational",
    "RealApproximation",
    "RealNumber",
    "SignaturePair",
    "SymbolicExpression",
    # general algebra
    "BaseRing",
    "Element",
    "Matrix",
    "ModuleElement",
    "RingElement",
    # geometry and combinatorics
    "CoxeterMatrix",
    "Graph",
    "Polyhedron",
    # Sage interop
    "SageCategory",
    "SageElement",
    "SageMorphism",
    "SageParent",
    "SageUniqueRepresentation",
]

"""Single import surface for mathematical nouns used by the preamble."""

from dzack_research.preamble.lexicon.algebra import (
    BaseRing,
    Element,
    Matrix,
    ModuleElement,
    RingElement,
)
from dzack_research.preamble.lexicon.foundations import (
    CartanType,
    GramMatrix,
    Integer,
    LatticeName,
    MatrixData,
    OrderedSet,
    Rational,
    RealApproximation,
    RealNumber,
    SignaturePair,
    SymbolicExpression,
)
from dzack_research.preamble.lexicon.geometry import CoxeterMatrix, Graph, Polyhedron
from dzack_research.preamble.lexicon.interop import (
    SageCategory,
    SageElement,
    SageMorphism,
    SageParent,
    SageUniqueRepresentation,
)

__all__ = [
    "BaseRing",
    "CartanType",
    "CoxeterMatrix",
    "Element",
    "GramMatrix",
    "Graph",
    "Integer",
    "LatticeName",
    "Matrix",
    "MatrixData",
    "ModuleElement",
    "OrderedSet",
    "Polyhedron",
    "Rational",
    "RealApproximation",
    "RealNumber",
    "RingElement",
    "SageCategory",
    "SageElement",
    "SageMorphism",
    "SageParent",
    "SageUniqueRepresentation",
    "SignaturePair",
    "SymbolicExpression",
]

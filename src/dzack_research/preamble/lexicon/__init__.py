"""Single import surface for mathematical nouns used by the preamble."""

from dzack_research.preamble.lexicon.algebra import (
    AlgebraHomomorphism,
    BaseRing,
    Element,
    Matrix,
    ModuleElement,
    MonoidObject,
    RingElement,
)
from dzack_research.preamble.lexicon.category_theory import (
    ElementOfCategoryObject,
    ObjectOfCategory,
)
from dzack_research.preamble.lexicon.foundations import (
    CartanType,
    GramMatrix,
    Integer,
    LatticeName,
    MatrixData,
    OrderedSet,
    Rational,
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
from dzack_research.preamble.lexicon.set_theory import SetObject

__all__ = [
    "AlgebraHomomorphism",
    "BaseRing",
    "CartanType",
    "CoxeterMatrix",
    "Element",
    "ElementOfCategoryObject",
    "GramMatrix",
    "Graph",
    "Integer",
    "LatticeName",
    "Matrix",
    "MatrixData",
    "ModuleElement",
    "MonoidObject",
    "OrderedSet",
    "ObjectOfCategory",
    "Polyhedron",
    "Rational",
    "RingElement",
    "SageCategory",
    "SageElement",
    "SageMorphism",
    "SageParent",
    "SageUniqueRepresentation",
    "SetObject",
    "SignaturePair",
    "SymbolicExpression",
]

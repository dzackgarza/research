r"""The lexicon: single import surface for the preamble's typed language.

Re-export only — every noun is defined in exactly one module. Downstream
preamble code draws from here:

    from ..lexicon import Element, Matrix, Module, OrderedSet

The dependency runs one way: ``objects`` draws on ``lexicon``, and the
lexicon draws on nothing but Sage. The nouns ``objects`` itself defines
(``Cardinal``, ``Character``, ``MorphismMatrix``) are therefore imported from
their own modules, never re-exported here — re-exporting them would make
``lexicon`` and ``objects`` import each other, a cycle that survives only
under one hand-arranged import order.
"""

from .algebra import (
    BaseRing,
    Element,
    FreeModule,
    Group,
    GroupElement,
    Matrix,
    Module,
    ModuleElement,
    Ring,
    RingElement,
    TorsionModule,
    Vector,
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
    Set,
    SignaturePair,
    SymbolicExpression,
)
from .interop import (
    SageCategory,
    SageElement,
    SageFunctor,
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
    "Set",
    "SignaturePair",
    "SymbolicExpression",
    # general algebra
    "BaseRing",
    "Element",
    "FreeModule",
    "Group",
    "GroupElement",
    "Matrix",
    "Module",
    "ModuleElement",
    "Ring",
    "RingElement",
    "TorsionModule",
    "Vector",
    # Sage interop
    "SageCategory",
    "SageElement",
    "SageFunctor",
    "SageMorphism",
    "SageParent",
    "SageUniqueRepresentation",
]

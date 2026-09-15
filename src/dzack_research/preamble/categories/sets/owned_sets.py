"""Compatibility exports for the owned Set category spine.

Internal code imports these objects from :mod:`set_categories`, their defining
module.
"""

from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    CountableSets,
    CountablyInfiniteSets,
    FinitelySupportedFunctionSets,
    FiniteSets,
    InfiniteSets,
    NaturalNumber,
    NaturalNumbers,
    PartiallyOrderedSets,
    Sets,
    SetSubcategoryMethods,
    TotallyOrderedSets,
    UncountableSets,
    register_set_axioms,
)

__all__ = [
    "CountableSets", "CountablyInfiniteSets", "FiniteSets",
    "FinitelySupportedFunctionSets", "InfiniteSets", "NaturalNumber",
    "NaturalNumbers", "NN", "PartiallyOrderedSets", "SetSubcategoryMethods",
    "Sets", "TotallyOrderedSets", "UncountableSets",
    "register_set_axioms",
]

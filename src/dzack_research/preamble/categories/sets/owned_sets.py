"""Compatibility exports for the owned Set category spine.

Internal code imports these objects from :mod:`set_categories`, their defining
module.
"""

from dzack_research.preamble.categories.sets.set_categories import (
    CountableSets,
    CountablyInfiniteSets,
    FiniteSets,
    FinitelySupportedFunctionSets,
    InfiniteSets,
    NaturalNumber,
    NaturalNumbers,
    NN,
    PartiallyOrderedSets,
    SetSubcategoryMethods,
    Sets,
    TotallyOrderedSets,
    UncountableSets,
    placement_of,
    register_set_axioms,
)

__all__ = [
    "CountableSets", "CountablyInfiniteSets", "FiniteSets",
    "FinitelySupportedFunctionSets", "InfiniteSets", "NaturalNumber",
    "NaturalNumbers", "NN", "PartiallyOrderedSets", "SetSubcategoryMethods",
    "Sets", "TotallyOrderedSets", "UncountableSets", "placement_of",
    "register_set_axioms",
]

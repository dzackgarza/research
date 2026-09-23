r"""The archived owned-set axiom hierarchy, expressed by the live categories.

The archive modeled these as Set axioms.  The live preamble owns them as
mathematical subcategories instead; this file reconciles the semantics rather
than the old Sage-global axiom implementation.
"""


from dzack_research.preamble.all import (
    NN,
    CountableSets,
    CountablyInfiniteSets,
    InfiniteSets,
    UncountableSets,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/sets/owned_sets.py",
    "live_owner": "src/dzack_research/preamble/categories/sets/set_categories.py",
    "owner_overrides": {
        "SetSubcategoryMethods.product_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "SetSubcategoryMethods.coproduct_functor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "SetSubcategoryMethods.ExponentialFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.InverseImagePowerSetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.FinitePowerSetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.FixedCardinalitySubsetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.CardinalityFunctor": "src/dzack_research/preamble/categories/functors/cardinality.py",
    },
    "disposition": "reconciled-live-owner",
}









def test_archived_uncountable_sets_are_infinite_and_not_countable() -> None:
    continuum_set = NN.power_set()

    assert continuum_set in UncountableSets()
    assert continuum_set in InfiniteSets()
    assert continuum_set not in CountableSets()
    assert continuum_set not in CountablyInfiniteSets()





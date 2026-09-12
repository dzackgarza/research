r"""The archived owned-set axiom hierarchy, expressed by the live categories.

The archive modeled these as Set axioms.  The live preamble owns them as
mathematical subcategories instead; this file reconciles the semantics rather
than the old Sage-global axiom implementation.
"""

from dzack_research.preamble.all import (
    NN,
    CountableSets,
    CountablyInfiniteSets,
    EnumeratedSets,
    FiniteSets,
    InfiniteSets,
    PartiallyOrderedSets,
    PowerSet,
    Sets,
    TotallyOrderedSets,
    UncountableSets,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/sets/owned_sets.py",
    "live_owner": "src/dzack_research/preamble/categories/sets/set_categories.py",
    "owner_overrides": {
        "SetSubcategoryMethods.ProductFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "SetSubcategoryMethods.CoproductFunctor": "src/dzack_research/preamble/categories/abstract_categories/functors.py",
        "SetSubcategoryMethods.ExponentialFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.InverseImagePowerSetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.FinitePowerSetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.FixedCardinalitySubsetFunctor": "src/dzack_research/preamble/categories/functors/set_constructions.py",
        "SetSubcategoryMethods.CardinalityFunctor": "src/dzack_research/preamble/categories/functors/cardinality.py",
    },
    "disposition": "reconciled-live-owner",
}



def test_archived_finite_sets_are_countable_without_becoming_infinite() -> None:
    finite = Sets.Δ[4]

    assert finite in FiniteSets()
    assert finite in CountableSets()
    assert finite not in InfiniteSets()
    assert finite not in CountablyInfiniteSets()
    assert finite not in UncountableSets()


def test_archived_countably_infinite_is_the_countable_infinite_intersection() -> None:
    assert NN in CountableSets()
    assert NN in InfiniteSets()
    assert NN in CountablyInfiniteSets()
    assert NN not in FiniteSets()
    assert NN not in UncountableSets()


def test_archived_uncountable_sets_are_infinite_and_not_countable() -> None:
    continuum_set = PowerSet(NN)

    assert continuum_set in UncountableSets()
    assert continuum_set in InfiniteSets()
    assert continuum_set not in CountableSets()
    assert continuum_set not in CountablyInfiniteSets()


def test_archived_total_order_refines_partial_order_without_cardinality_claim() -> None:
    assert NN in TotallyOrderedSets()
    assert NN in PartiallyOrderedSets()
    assert TotallyOrderedSets().is_subcategory(PartiallyOrderedSets())
    assert not TotallyOrderedSets().is_subcategory(FiniteSets())


def test_countability_and_a_chosen_enumeration_are_distinct_live_structures() -> None:
    assert not CountableSets().is_subcategory(EnumeratedSets())
    assert NN in CountableSets()
    assert NN in EnumeratedSets()
    assert NN.ranking_map().inverse()(7) == NN(7)

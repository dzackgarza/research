r"""Public session vocabulary and rejected legacy operation globals.

These are mathematical constructors deliberately used by the construction and
archive proof surfaces.  The session exports owner/category/specimen names, but
does not publish owner-in-argument operations as free functions.
"""

import dzack_research.preamble.all as session
from dzack_research.preamble.all import (
    AdicCompletions,
    DividedPowerAlgebraOf,
    DividedPowerAlgebraOn,
    DividedPowerAlgebras,
    OwnedCategoryOverBaseRing,
    QuadraticMap,
    finite_ordered_set,
    ring_morphism,
)


def test_terminal_collection_vocabulary_is_public() -> None:
    names = (
        AdicCompletions,
        DividedPowerAlgebraOf,
        DividedPowerAlgebraOn,
        DividedPowerAlgebras,
        OwnedCategoryOverBaseRing,
        QuadraticMap,
        finite_ordered_set,
        ring_morphism,
    )

    assert all(name is not None for name in names)


def test_owner_in_argument_universal_operations_are_not_session_globals() -> None:
    forbidden = (
        "Biproduct",
        "Coproduct",
        "Product",
        "Pushout",
        "TensorProduct",
        "TensorSquare",
        "Kernel",
        "Cokernel",
        "Equalizer",
        "Coequalizer",
        "EqualizerOfFamily",
        "CoequalizerOfFamily",
        "FiberProduct",
        "Subobjects",
        "Core",
        "ProductConstruction",
        "CoproductConstruction",
        "EqualizerConstruction",
        "CoequalizerConstruction",
        "FractionField",
        "Localization",
        "PrimeLocalization",
        "QuotientRing",
        "ResidueField",
        "AdicCompletion",
        "Ideal",
        "OppositeCategory",
        "ProductCategory",
        "SliceOver",
        "CosliceUnder",
        "SubobjectsOf",
        "SuperobjectsOf",
        "CoveringObjectsOf",
        "CoveredObjectsOf",
        "ArrowCategory",
        "FunctorCategory",
        "HomCategoryOf",
        "EndCategoryOf",
        "MonoCategoryOf",
        "EpiCategoryOf",
        "IsoCategoryOf",
        "AutCategoryOf",
        "SliceCategory",
        "CosliceCategory",
        "SubobjectCategory",
        "SuperobjectCategory",
        "CoveringObjectCategory",
        "CoveredObjectCategory",
        "CochainComplex",
        "CochainComplexFromFamily",
        "Cycles",
        "Boundaries",
        "Cohomology",
        "cochain_homset",
        "algebra_homset",
        "group_homset",
        "g_set_homset",
        "commutative_algebra_coproduct",
        "commutative_algebra_pushout",
        "centralizer",
        "predicate_subgroup",
        "DeRhamAlgebra",
        "KahlerDifferentials",
    )

    assert all(not hasattr(session, name) for name in forbidden)

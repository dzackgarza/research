r"""Public session names whose absence broke terminal collection.

These are mathematical constructors deliberately used by the construction and
archive proof surfaces.  Importing this module is the regression: each name
must be exported by ``dzack_research.preamble.all`` rather than reached through
an implementation module.
"""

from dzack_research.preamble.all import (
    AdicCompletion,
    AdicCompletions,
    Biproduct,
    CochainComplexFromFamily,
    Coproduct,
    Core,
    DividedPowerAlgebraOf,
    DividedPowerAlgebraOn,
    DividedPowerAlgebras,
    Localization,
    OwnedCategoryOverBaseRing,
    Product,
    Pushout,
    QuadraticMap,
    QuotientRing,
    TensorProduct,
    TensorSquare,
    finite_ordered_set,
    ring_morphism,
)


def test_terminal_collection_vocabulary_is_public() -> None:
    names = (
        AdicCompletion,
        AdicCompletions,
        Biproduct,
        CochainComplexFromFamily,
        Coproduct,
        Core,
        DividedPowerAlgebraOf,
        DividedPowerAlgebraOn,
        DividedPowerAlgebras,
        Localization,
        OwnedCategoryOverBaseRing,
        Product,
        Pushout,
        QuadraticMap,
        QuotientRing,
        TensorProduct,
        TensorSquare,
        finite_ordered_set,
        ring_morphism,
    )

    assert all(name is not None for name in names)

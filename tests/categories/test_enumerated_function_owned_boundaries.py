r"""Function-enumeration refinements live in the owned category graph."""

from dzack_research.preamble.all import (
    EnumeratedByIntegers,
    EnumeratedByNaturals,
    FunctionEnumeratedSets,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.enumerated.hermite_polynomials import (
    HermitePolynomials,
)
from dzack_research.preamble.categories.sets.enumerated.laurent_monomials import (
    LaurentMonomials,
)


def test_function_enumeration_categories_are_owned_refinements() -> None:
    assert isinstance(FunctionEnumeratedSets(), OwnedCategory)
    assert isinstance(EnumeratedByNaturals(), OwnedCategory)
    assert isinstance(EnumeratedByIntegers(), OwnedCategory)

    hermite = HermitePolynomials()
    laurent = LaurentMonomials()
    assert hermite in FunctionEnumeratedSets()
    assert hermite in EnumeratedByNaturals()
    assert laurent in FunctionEnumeratedSets()
    assert laurent in EnumeratedByIntegers()


def test_owned_category_conversion_preserves_indexing_maps() -> None:
    hermite = HermitePolynomials()
    laurent = LaurentMonomials()

    assert hermite.function(3) == hermite[3]
    assert laurent.function(-2) == laurent[4]
    assert laurent.ranking_map()(laurent.function(-2)) == 4

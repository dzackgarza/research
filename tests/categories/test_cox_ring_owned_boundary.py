r"""Cox-ring categories are owned and parameterized by represented toric schemes."""

import pytest

from dzack_research.preamble.all import PolynomialRing, QQ, Spec
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.divisors.cox_rings import CoxRing, CoxRings
from dzack_research.preamble.categories.schemes.toric.toric_schemes import (
    RepresentedToricSchemes,
    ToricSchemes,
)


def test_cox_ring_category_uses_the_actual_toric_scheme_parameter() -> None:
    plane = ToricSchemes(QQ).an_object()
    category = CoxRings(plane)
    cox = CoxRing(plane)

    assert plane in RepresentedToricSchemes()
    assert isinstance(category, OwnedParameterizedCategory)
    assert category.scheme() is plane
    assert category.base() is plane
    assert CoxRings(plane) is category
    assert cox in category
    assert cox.grading_monoid() is plane.class_group()


def test_cox_ring_category_rejects_a_nontoric_scheme_parameter() -> None:
    algebra = PolynomialRing(QQ, "x")
    affine_line = Spec(algebra)

    assert affine_line not in RepresentedToricSchemes()
    with pytest.raises(AssertionError):
        CoxRings(affine_line)

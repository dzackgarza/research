r"""Cox-ring categories are parameterized by toric schemes over their own base."""

import pytest

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.divisors.cox_rings import CoxRings
from dzack_research.preamble.categories.schemes.toric.toric_schemes import (
    ToricSchemes,
)


def test_cox_ring_category_uses_the_actual_toric_scheme_parameter() -> None:
    plane = ToricSchemes(QQ).an_object()
    category = CoxRings(plane)
    cox = plane.cox_ring()

    assert plane in ToricSchemes(QQ)
    assert isinstance(category, OwnedParameterizedCategory)
    assert category.scheme() is plane
    assert category.base() is plane
    assert CoxRings(plane) is category
    assert cox in category
    assert cox.grading_monoid() is plane.class_group()


def test_cox_ring_category_rejects_a_nontoric_scheme_parameter() -> None:
    algebra = QQ.polynomial_ring("x")
    affine_line = (algebra).affine_spectrum()

    assert affine_line not in ToricSchemes(QQ)
    with pytest.raises(AssertionError):
        CoxRings(affine_line)

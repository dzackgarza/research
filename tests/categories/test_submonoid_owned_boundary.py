r"""Public submonoids are parameterized only by owned ambient monoids."""

import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.group.submonoids import (
    Submonoids,
    predicate_submonoid,
)
from dzack_research.preamble.rings.unit_interval import UnitInterval


def test_predicate_submonoid_retains_owned_ambient_and_inclusion() -> None:
    identity = UnitInterval.one()
    submonoid = predicate_submonoid(
        UnitInterval,
        lambda element: element == identity,
        "the identity submonoid",
    )

    assert submonoid in Submonoids(UnitInterval)
    assert submonoid.ambient_monoid() is UnitInterval
    assert submonoid.one() == identity
    assert submonoid.inclusion().codomain() is UnitInterval


def test_raw_sage_monoid_is_not_a_public_submonoid_ambient() -> None:
    with pytest.raises(TypeError, match="owned monoid"):
        predicate_submonoid(
            SageZZ,
            lambda _element: True,
            "raw Sage ambient",
        )

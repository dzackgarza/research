r"""The exact real field is placed only through the owned category graph."""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedFields
from dzack_research.preamble.categories.sets.cardinals import continuum
from dzack_research.preamble.categories.sets.set_categories import UncountableSets
from dzack_research.preamble.rings import RR


def test_exact_real_field_retains_field_uncountability_and_ring_operations() -> None:
    assert RR in OwnedFields()
    assert RR in UncountableSets()
    assert RR.cardinality() == continuum
    assert RR.zero() + RR.one() == RR.one()
    assert RR(2) * RR(3) == RR(6)
    assert RR.base_ring() is RR

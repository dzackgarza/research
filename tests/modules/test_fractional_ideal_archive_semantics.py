r"""Archive reconciliation for fractional-ideal coefficient and submodule semantics."""

import pytest

from dzack_research.preamble.all import QQ, ZZ


def test_integral_ideal_retains_its_ring_and_is_its_owned_submodule() -> None:
    ideal = ZZ.ideal(6)

    assert ideal.ring() is ZZ
    submodule = ideal.as_submodule()
    assert submodule is ideal
    assert submodule.inclusion().domain() is ideal
    assert submodule.inclusion().codomain().base_ring() is ZZ
    generator = ideal.module_generators()[0]
    assert submodule.inclusion()(generator) == ZZ(6)


def test_nonintegral_fractional_ideal_is_not_relabelled_as_a_submodule_of_the_ring() -> None:
    half = QQ(1) / 2
    fractional = ZZ.fractional_ideal(half)

    assert fractional.ring() is ZZ
    assert fractional.fraction_field() is QQ
    with pytest.raises(ValueError, match="submodule of Frac"):
        fractional.as_submodule()

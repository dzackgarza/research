r"""Fractional ideals use the owned categorical meet for their placement."""

from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.modules.fractional_ideals import (
    FractionalIdeals,
    Ideals,
)
from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedModules


def test_integral_and_fractional_ideals_share_owned_module_placement_without_conflation() -> None:
    integral = ZZ.ideal(6)
    fractional = ZZ.fractional_ideal(QQ(1) / 2)

    assert integral in FractionalIdeals(ZZ)
    assert integral in Ideals(ZZ)
    assert integral in FinitelyGeneratedModules(ZZ)
    assert fractional in FractionalIdeals(ZZ)
    assert fractional in FinitelyGeneratedModules(ZZ)
    assert fractional not in Ideals(ZZ)
    assert integral.ring() is ZZ
    assert fractional.ring() is ZZ
    assert fractional.fraction_field() is QQ

r"""Fractional ideals use the owned categorical meet for their placement."""

from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.modules.fractional_ideals import FractionalIdeals
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedModules,
    Modules,
)
from dzack_research.preamble.categories.rings.commutative_ideals import CommutativeIdeals


def test_integral_and_fractional_ideals_share_owned_module_placement_without_conflation() -> None:
    integral = ZZ.ideal(6)
    fractional = ZZ.fractional_ideal(QQ(1) / 2)
    extended = CommutativeIdeals(ZZ).extension_to_fraction_field()(integral)

    assert extended in FractionalIdeals(ZZ)
    assert integral in CommutativeIdeals(ZZ)
    assert integral in FinitelyGeneratedModules(ZZ)
    assert fractional in FractionalIdeals(ZZ)
    assert fractional in FinitelyGeneratedModules(ZZ)
    assert fractional in Modules(ZZ).Projective()
    assert fractional not in CommutativeIdeals(ZZ)
    assert integral.ring() is ZZ
    assert fractional.ring() is ZZ
    assert fractional.fraction_field() is QQ

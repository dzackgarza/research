r"""Ring parents dispatch ``Mor`` through Ring rather than inherited module Mor."""

from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_ring_parent_mor_selects_ring_mor_while_module_parent_mor_stays_linear() -> None:
    inclusion = ZZ.Mor(QQ)(lambda integer: QQ(integer))

    assert inclusion.domain() is ZZ
    assert inclusion.codomain() is QQ
    assert inclusion(ZZ(7)) == QQ(7)

    line = ZZ.free_module(finite_ordered_set(("e",)))
    doubling = line.Mor(line)({"e": 2 * line.module_generator("e")})
    assert doubling.domain() is line
    assert doubling.codomain() is line
    assert doubling(line.module_generator("e")) == 2 * line.module_generator("e")

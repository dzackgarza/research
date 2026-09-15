r"""Archive reconciliation for the formed-element representation predicate."""

from dzack_research.preamble.all import QQ, FreeModule


def test_formed_element_represents_exactly_its_norm_value() -> None:
    module = FreeModule(QQ, 2)
    formed = module.equip_bilinear_form(QQ, [[2, 0], [0, 3]])
    first, second = tuple(formed.module_generators())
    vector = first + second

    assert vector.q() == 5
    assert vector.represents(5)
    assert not vector.represents(4)


def test_zero_element_represents_zero() -> None:
    module = FreeModule(QQ, 1)
    formed = module.equip_bilinear_form(QQ, [[7]])

    assert formed.zero().represents(QQ.zero())

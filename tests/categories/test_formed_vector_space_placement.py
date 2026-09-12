"""Formed copies retain vector-space placement over a field."""

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    BilinearForm,
    FreeModule,
    VectorSpaces,
)


def test_a_formed_copy_of_a_rational_vector_space_is_still_a_vector_space() -> None:
    module = FreeModule(QQ, 2)
    formed = BilinearForm(module, QQ, [[1, 0], [0, 1]])

    assert module in VectorSpaces(QQ)
    assert formed in VectorSpaces(QQ)
    assert formed.unformed_module() is module


def test_base_change_of_an_integral_form_to_a_field_has_vector_space_placement() -> None:
    integral = BilinearForm(FreeModule(ZZ, 2), ZZ, [[2, 1], [1, 2]])
    rational = integral.base_change(ZZ.Mor(QQ)(lambda scalar: QQ(scalar)))
    mod_three = integral.base_change(ZZ.Mor(GF(3))(lambda scalar: GF(3)(scalar)))

    assert rational in VectorSpaces(QQ)
    assert mod_three in VectorSpaces(GF(3))
    assert integral.base_ring() is ZZ

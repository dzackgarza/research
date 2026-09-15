"""Archive reconciliation for rationalization of framed and formed modules."""

from dzack_research.preamble.all import QQ, ZZ, FormModules
from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces


def test_framed_free_module_vector_space_is_fraction_field_base_change() -> None:
    module = ZZ.free_module(("e", "f"))
    rationalized = module.vector_space()

    assert rationalized.base_ring() is QQ
    assert rationalized in VectorSpaces(QQ)
    assert rationalized.module_generating_set() is module.module_generating_set()


def test_formed_module_vector_space_transports_the_form() -> None:
    module = ZZ.free_module(("e", "f"))
    formed = FormModules(ZZ)(module.bilinear_forms(ZZ)([[2, 1], [1, -2]]))
    rationalized = formed.vector_space()

    assert rationalized.base_ring() is QQ
    assert rationalized in VectorSpaces(QQ)
    assert rationalized.module_generating_set() is formed.module_generating_set()
    labels = rationalized.module_generating_set()
    assert rationalized.b(
        rationalized.module_generator(labels[0]),
        rationalized.module_generator(labels[1]),
    ) == QQ.one()
    assert rationalized.gram_tensor()[0, 0] == QQ(2)
    assert rationalized.gram_tensor()[1, 1] == QQ(-2)

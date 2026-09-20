r"""Finitely many determining elements suffice without chosen relations."""

import pytest
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import Algebras, Modules, QQ
from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.owned_category import _object_of


def _framed_rationals_without_a_chosen_presentation():
    free = QQ.free_module(1)
    module = _object_of(
        Cat().meet((GeneralModules(QQ), FramedModules(QQ))),
        base_ring=QQ, underlying_set=QQ,
        addition=lambda x, y: x + y, zero=QQ.zero(), negation=lambda x: -x,
        scalar_action=lambda r, x: r * x,
        module_generating_set=free.module_generating_set(),
        module_generator_function=lambda _: module(QQ.one()), framing_source=free,
    )
    return module


def test_linear_maps_and_tensor_classifiers_use_the_finite_frame():
    module = _framed_rationals_without_a_chosen_presentation()
    morphisms = Modules(QQ).Mor(module, module)
    first = morphisms.elementwise(lambda x: x)
    second = morphisms.elementwise(lambda x: module(QQ(1)) + (x - module(QQ(1))))
    twice = morphisms.elementwise(lambda x: x + x)
    assert module._selected_presentation_rows() is None
    assert first.linearity_decision() is Unknown
    assert (first == second) is Unknown
    assert first != twice
    tensor = Modules(QQ).tensor_product((module, module))
    product = tensor.from_bilinear_map(module, lambda x, y: module(x.underlying_element() * y.underlying_element()))
    same = tensor.from_bilinear_map(module, lambda x, y: module(y.underlying_element() * x.underlying_element()))
    assert product == same
    assert product != product + product
    algebra = Algebras(QQ)(module, product)
    linear = Modules(QQ).Mor(algebra, algebra).identity()
    identity = Algebras(QQ).Mor(algebra, algebra)(linear)
    assert identity.is_multiplicative() is True
    doubled = Modules(QQ).Mor(algebra, algebra).scalar_multiple(QQ(2), linear)
    with pytest.raises(AssertionError, match="preserve the multiplication"):
        Algebras(QQ).Mor(algebra, algebra)(doubled)


def test_no_finite_generating_data_still_means_unknown_not_sampling():
    module = GeneralModules(QQ).from_operations(QQ,
        addition=lambda x, y: x + y, zero=QQ.zero(), negation=lambda x: -x,
        scalar_action=lambda r, x: r * x)
    morphisms = Modules(QQ).Mor(module, module)
    first = morphisms.elementwise(lambda x: x)
    second = morphisms.elementwise(lambda x: x)
    assert (first == second) is Unknown
    assert (first != second) is Unknown

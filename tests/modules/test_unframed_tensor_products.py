r"""Tensor classifiers do not require a module framing."""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import Modules, QQ
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.sets.set_categories import Set


def _rationals_without_framing():
    return GeneralModules(QQ).from_operations(
        Set(QQ), addition=lambda x, y: x + y, zero=QQ.zero(),
        negation=lambda x: -x, scalar_action=lambda r, x: r * x,
        verify=False,
    )


def test_unframed_tensor_has_its_universal_bilinear_classifier() -> None:
    module = _rationals_without_framing()
    tensor = Modules(QQ).tensor_product((module, module))
    pairing = lambda x, y: module(x.underlying_element() * y.underlying_element())
    classified = tensor.from_bilinear_map(module, pairing)
    x, y = module(QQ(2)), module(QQ(3))
    pure = tensor.pure_tensor(x, y)

    assert classified.domain() is tensor
    assert classified.codomain() is module
    assert classified(pure) == module(QQ(6))
    assert pure + (-pure) == tensor.zero()
    assert tensor.pure_tensor(x + x, y) == pure + pure
    assert classified(tensor.pure_tensor(module.scalar_multiple(QQ(5), x), y)) == classified(
        tensor.pure_tensor(x, module.scalar_multiple(QQ(5), y))
    )


def test_unframed_tensor_map_uses_the_supplied_factor_maps() -> None:
    module = _rationals_without_framing()
    tensor = Modules(QQ).tensor_product((module, module))
    scale = module.module_category().Mor(module, module).elementwise(
        lambda x: module.scalar_multiple(QQ(2), x), verify_linearity=False,
    )
    induced = scale.tensor_product_map(scale, source=tensor, target=tensor)
    classified = tensor.from_bilinear_map(module, lambda x, y: module(x.underlying_element() * y.underlying_element()))
    pure = tensor.pure_tensor(module(QQ(2)), module(QQ(3)))

    assert classified(induced(pure)) == module(QQ(24))
    assert (tensor.pure_tensor(module(QQ(1)), module(QQ(1))) == tensor.zero()) is Unknown

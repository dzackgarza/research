r"""Tensor classifiers do not require a module framing."""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import Modules, QQ
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Set


def _rationals_without_framing():
    return GeneralModules(QQ).from_operations(
        Set(QQ), addition=lambda x, y: x + y, zero=QQ.zero(),
        negation=lambda x: -x, scalar_action=lambda r, x: r * x,
    )


def test_unframed_tensor_has_its_universal_bilinear_classifier() -> None:
    module = _rationals_without_framing()
    tensor = Modules(QQ).tensor_product((module, module))
    pairing = lambda x, y: module(x.underlying_element() * y.underlying_element())
    classified = tensor.from_bilinear_map(module, pairing)
    universal = tensor.universal_bilinear_map()
    pairing_hom = module.pairings_with(module, module)(pairing)
    x, y = module(QQ(2)), module(QQ(3))
    pure = tensor.pure_tensor(x, y)

    assert universal(x, y) == pure
    assert universal.linearity_decision() is True
    assert classified.domain() is tensor
    assert classified.codomain() is module
    assert classified.linearity_decision() is Unknown
    assert pairing_hom.parent() is tensor.module_category().Mor(tensor, module)
    assert pairing_hom.domain() is tensor
    assert pairing_hom.codomain() is module
    assert pairing_hom.linearity_decision() is Unknown
    assert classified(pure) == module(QQ(6))
    assert pairing_hom(x, y) == module(QQ(6))
    assert pure + (-pure) == tensor.zero()
    assert tensor.pure_tensor(x + x, y) == pure + pure
    assert classified(tensor.pure_tensor(module.scalar_multiple(QQ(5), x), y)) == classified(
        tensor.pure_tensor(x, module.scalar_multiple(QQ(5), y))
    )


def test_unframed_tensor_map_uses_the_supplied_factor_maps() -> None:
    module = _rationals_without_framing()
    tensor = Modules(QQ).tensor_product((module, module))
    endomorphisms = module.module_category().Mor(module, module)
    scale = endomorphisms.scalar_multiple(
        QQ(2),
        endomorphisms.identity(),
    )
    induced = scale.tensor_product_map(scale, source=tensor, target=tensor)
    classified = tensor.from_bilinear_map(module, lambda x, y: module(x.underlying_element() * y.underlying_element()))
    pure = tensor.pure_tensor(module(QQ(2)), module(QQ(3)))

    assert classified(induced(pure)) == module(QQ(24))
    assert (tensor.pure_tensor(module(QQ(1)), module(QQ(1))) == tensor.zero()) is Unknown


def test_algebraic_tensor_and_adic_completion_keep_distinct_defining_data() -> None:
    ring = QQ.polynomial_ring("t")
    t = ring.algebra_generator("t")
    module = ring.free_module(finite_ordered_set(("e",)))
    algebraic = Modules(ring).tensor_product((module, module))
    completion = ring.adic_completion(ring.ideal(t), precision=6)
    completed = module.base_change_to_completion(completion)
    extension = Modules(ring).base_change_adjunction(
        completion.completion_map()
    ).left_adjoint()

    assert algebraic.base_ring() is ring
    assert algebraic.tensor_factor(0) is module
    assert algebraic.tensor_factor(1) is module
    assert completed is extension(module)
    assert completed.base_ring() is completion

"""Archive reconciliation for the base bilinear/quadratic form surface."""

from dzack_research.preamble.all import (
    ZZ,
    BilinearForms,
    QuadraticMap,
    ring_as_module,
)


def _rank_one_module():
    return ring_as_module(ZZ)


def _generator(module):
    return module.module_generator(module.module_generating_set()[0])


def _doubling(module):
    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    return module.module_category().Mor(module, module)({label: 2 * generator})


def test_archived_bilinear_form_is_the_live_tensor_hom_with_gram_and_pullback() -> None:
    module = _rank_one_module()
    generator = _generator(module)
    form = BilinearForms(module, ZZ)([[ZZ.one()]])

    assert form.module() is module
    assert form.codomain() is ZZ
    assert form(generator, generator) == ZZ.one()
    assert form.norm(generator) == ZZ.one()
    assert form.gram_tensor()[0, 0] == ZZ.one()

    pulled = form.pullback(_doubling(module))
    assert pulled(generator, generator) == ZZ(4)


def test_archived_quadratic_form_is_classified_by_divided_square_and_polarizes() -> None:
    module = _rank_one_module()
    generator = _generator(module)
    quadratic = QuadraticMap(
        module,
        ZZ,
        lambda element: element.to_tuple()[0] ** 2,
    )

    assert quadratic.module() is module
    assert quadratic.codomain() is ZZ
    assert quadratic(generator) == ZZ.one()
    assert quadratic.polar_form()(generator, generator) == ZZ(2)

    pulled = quadratic.pullback(_doubling(module))
    assert pulled(generator) == ZZ(4)

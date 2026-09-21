"""Archive reconciliation for the base bilinear/quadratic form surface."""

from dzack_research.preamble.all import (
    ZZ,
)


def _rank_one_module():
    return ZZ.regular_module()


def _generator(module):
    return module.module_generator(module.module_generating_set()[0])


def _doubling(module):
    label = module.module_generating_set()[0]
    generator = module.module_generator(label)
    return module.module_category().Mor(module, module)({label: 2 * generator})


def test_archived_bilinear_form_is_the_live_tensor_hom_with_gram_and_pullback() -> None:
    module = _rank_one_module()
    generator = _generator(module)
    form = module.bilinear_forms(ZZ)([[ZZ.one()]])

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
    label = module.module_generating_set()[0]
    quadratic = module.quadratic_map(
        ZZ,
        lambda element: module.framing_coefficients(element).get(label, ZZ.zero()) ** 2,
    )

    assert quadratic.module() is module
    assert quadratic.codomain() is ZZ
    assert quadratic(generator) == ZZ.one()
    assert quadratic.polar_form()(generator, generator) == ZZ(2)

    pulled = quadratic.pullback(_doubling(module))
    assert pulled(generator) == ZZ(4)


def test_unframed_forms_have_the_pointwise_module_operations() -> None:
    import operator
    from dzack_research.preamble.all import QQ, Modules
    from dzack_research.preamble.categories.modules.general_modules import GeneralModules

    module = GeneralModules(QQ).from_operations(
        QQ, addition=operator.add, zero=QQ.zero(), negation=operator.neg,
        scalar_action=operator.mul,
    )
    x, y = module(QQ(2)), module(QQ(3))
    bilinear = module.bilinear_forms(QQ)
    product = bilinear(lambda left, right: left.underlying_element() * right.underlying_element())
    assert bilinear in Modules(QQ)
    assert bilinear.zero()(x, y) == QQ.zero()
    assert (product + product)(x, y) == QQ(12)
    assert (-product)(x, y) == QQ(-6)
    assert bilinear.scalar_multiple(QQ(3), product)(x, y) == QQ(18)

    quadratic = module.quadratic_forms(QQ)
    square = quadratic.from_quadratic_map(lambda point: point.underlying_element() ** 2)
    assert quadratic in Modules(QQ)
    assert (square + square)(x) == QQ(8)
    assert square.polar_form()(x, y) == QQ(12)


def test_coordinate_ingress_rejects_extra_infinite_rows_and_entries() -> None:
    from itertools import repeat
    import pytest
    from dzack_research.preamble.categories.sets import Sets
    from dzack_research.preamble.categories.sets.coordinate_families import _coordinate_family_from_rows

    label = Sets.Δ[0]
    for rows in (repeat((ZZ.one(),)), (repeat(ZZ.one()),)):
        with pytest.raises(ValueError, match="shape 1 x 1"):
            _coordinate_family_from_rows(label, label, ZZ, rows, name="Malformed coordinates")

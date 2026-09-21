r"""Archive reconciliation for bilinear-form value tables and image modules."""

from dzack_research.preamble.all import ZZ


def _generator(module):
    return module.module_generator(module.module_generating_set()[0])


def test_bilinear_value_matrix_and_image_keep_the_scale_submodule() -> None:
    module = ZZ.regular_module()
    generator = _generator(module)
    form = module.bilinear_forms(ZZ)([[ZZ(2)]])

    values = form.values_matrix()
    assert values.index_set().cardinality() == 1
    assert tuple(values) == (ZZ(2),)
    image = form.image()
    assert image.inclusion().codomain() is ZZ.regular_module()
    image_generator = image.module_generators()[0]
    assert image.inclusion()(image_generator) == ZZ(2)
    assert ZZ(2) in image
    assert ZZ.one() not in image
    assert form(generator, generator) == ZZ(2)

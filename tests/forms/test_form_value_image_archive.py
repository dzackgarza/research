r"""Archive reconciliation for bilinear-form value tables and image modules."""

from dzack_research.preamble.all import BilinearForms, ZZ, ring_as_module


def _generator(module):
    return module.module_generator(module.module_generating_set()[0])


def test_bilinear_value_matrix_and_image_keep_the_scale_submodule() -> None:
    module = ring_as_module(ZZ)
    generator = _generator(module)
    form = BilinearForms(module, ZZ)([[ZZ(2)]])

    assert form.values_matrix() == ((ZZ(2),),)
    image = form.image()
    assert image.inclusion().codomain() is ring_as_module(ZZ)
    image_generator = image.module_generators()[0]
    assert image.inclusion()(image_generator) == ZZ(2)
    assert ZZ(2) in image
    assert ZZ.one() not in image
    assert form(generator, generator) == ZZ(2)

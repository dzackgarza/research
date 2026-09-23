r"""Archive reconciliation for formed-object constructor obligations."""

from dzack_research.preamble.all import ZZ, Lattices, Modules


def test_archived_bilinear_form_is_an_actual_morphism_to_its_value_module() -> None:
    module = ZZ.free_module(2)
    formed = module.equip_bilinear_form(ZZ, [[2, 1], [1, 2]])
    morphism = formed.form()
    tensor_square = Modules(ZZ).tensor_product((module, module))

    assert morphism.domain() is tensor_square
    assert morphism.codomain() is formed.value_module()
    first, second = tuple(module.module_generators())
    assert morphism(tensor_square.pure_tensor(first, second)) == (
        formed.value_module().module_generator(0)
    )


def test_archived_torsion_discriminant_form_retains_its_quotient_value_module() -> None:
    form = Lattices(ZZ)("A2").discriminant_bilinear_form()
    morphism = form.form()

    assert morphism.codomain() is form.value_module()
    assert form.value_module() is not form.base_ring()
    assert form.value_module().modulus() == 1


def test_archived_scale_submodule_is_the_ideal_generated_by_pairing_values() -> None:
    lattice = Lattices(ZZ)("A2")
    scale = lattice.scale_submodule()
    twisted_scale = lattice.twist(3).scale_submodule()

    assert scale.ring() is ZZ
    assert twisted_scale.ring() is ZZ
    assert scale == ZZ.ideal(1)
    assert twisted_scale == ZZ.ideal(3)

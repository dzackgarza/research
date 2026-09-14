r"""Archive reconciliation for formed-object constructor obligations."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.all import ZZ, BilinearForm, FreeModule, Lattices, TensorSquare


def test_archived_bilinear_form_is_an_actual_morphism_to_its_value_module() -> None:
    module = FreeModule(ZZ, 2)
    formed = BilinearForm(module, ZZ, [[2, 1], [1, 2]])
    morphism = formed.form()

    assert morphism.domain() is TensorSquare(module)
    assert morphism.codomain() is formed.value_module()
    first, second = tuple(module.module_generators())
    assert morphism(TensorSquare(module).pure_tensor(first, second)) == (
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

    assert lattice.scale_submodule() == SageZZ.ideal(1)
    assert lattice.twist(3).scale_submodule() == SageZZ.ideal(3)

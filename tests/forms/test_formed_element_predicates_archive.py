r"""Archive reconciliation for isotropy and left orthogonality of formed elements."""

from dzack_research.preamble.all import ZZ, FormModule, FreeModule


def test_isotropy_and_left_orthogonality_are_element_predicates() -> None:
    module = FreeModule(ZZ, 2)
    formed = FormModule(module.bilinear_forms(ZZ)([[0, 1], [0, 0]]))
    first, second = tuple(formed.module_generators())

    assert first.is_isotropic()
    assert second.is_isotropic()
    assert not first.is_orthogonal_to(second)
    assert second.is_orthogonal_to(first)


def test_nonisotropic_element_is_detected_from_its_actual_norm() -> None:
    module = FreeModule(ZZ, 1)
    formed = FormModule(module.bilinear_forms(ZZ)([[2]]))
    generator = formed.module_generators()[0]

    assert not generator.is_isotropic()
    assert not generator.is_orthogonal_to(generator)

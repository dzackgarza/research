import pytest

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
    DiscriminantBilinearModules,
    DiscriminantQuadraticModules,
)


def test_forgetting_quadratic_refinement_retains_discriminant_provenance() -> None:
    lattice = Lattices(ZZ)("A2")
    quadratic = lattice.discriminant_quadratic_form()
    bilinear = quadratic.associated_bilinear_form()

    assert bilinear in DiscriminantBilinearModules(ZZ)
    assert bilinear not in DiscriminantQuadraticModules(ZZ)
    assert bilinear.source_lattice() is lattice
    assert bilinear.dual_lattice() is quadratic.dual_lattice()
    assert bilinear.unformed_module() is quadratic.unformed_module()
    assert lattice.discriminant_bilinear_form() is bilinear


def test_even_discriminant_bilinear_form_recovers_canonical_quadratic_refinement() -> None:
    lattice = Lattices(ZZ)("A2")
    bilinear = lattice.discriminant_bilinear_form()

    assert bilinear.associated_quadratic_form() is lattice.discriminant_quadratic_form()


def test_odd_source_lattice_has_no_quadratic_refinement() -> None:
    lattice = Lattices(ZZ)([[1]])
    bilinear = lattice.discriminant_bilinear_form()

    with pytest.raises(ValueError):
        bilinear.associated_quadratic_form()

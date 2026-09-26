r"""A lattice refines an explicitly framed sublattice to a vector configuration."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_hyperbolic_basis_vectors_form_a_vector_configuration() -> None:
    lattice = NamedLattices.U
    e = lattice.basis_vector(0)
    f = lattice.basis_vector(1)
    configuration = lattice.vector_configuration((e, f))

    assert configuration in VectorConfigurations(ZZ)
    assert configuration.ambient_lattice() is lattice
    assert configuration.module_rank() == cardinal(2)


def test_vector_configuration_retains_the_selected_inclusion() -> None:
    lattice = NamedLattices.U
    e = lattice.basis_vector(0)
    configuration = lattice.vector_configuration((e,))

    assert configuration.inclusion()(configuration.module_generator(0)) == e

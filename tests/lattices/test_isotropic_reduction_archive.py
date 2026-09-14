r"""Archive reconciliation for the historical isotropic-quotient entrypoints."""

from dzack_research.preamble.all import NamedLattices


def test_vector_e_perp_mod_e_is_the_owned_isotropic_reduction() -> None:
    lattice = NamedLattices.TEn
    e = lattice.module_generators()[0]

    archived = e.e_perp_mod_e()
    owned = e.isotropic_reduction()

    assert archived.is_isometric(owned) is True
    assert archived.module_rank() == 10
    assert archived.is_isometric(NamedLattices.E10_2) is True


def test_parent_I_perp_mod_I_retains_the_rank_two_Enriques_reduction() -> None:
    lattice = NamedLattices.TEn
    basis = lattice.module_generators()
    e = basis[0]
    e_prime = basis[2]

    reduction = lattice.I_perp_mod_I((e, e_prime))

    assert reduction.module_rank() == 8
    assert reduction.is_isometric(NamedLattices.E8_2) is True
    assert reduction.isotropic_embedding().codomain() is lattice

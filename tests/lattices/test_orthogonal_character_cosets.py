r"""Finite-character right cosets retain live orthogonal-group lifts."""

from dzack_research.preamble.all import NamedLattices


def test_special_orthogonal_group_has_two_right_cosets_in_O_A1() -> None:
    lattice = NamedLattices.A1
    subgroup = lattice.SO()
    quotient = subgroup.finite_character_quotient()
    representatives = quotient.right_coset_transversal()

    assert len(quotient.image_keys()) == 2
    assert len(quotient.subgroup_image_keys()) == 1
    assert representatives.cardinality() == 2
    assert all(representative.parent() is lattice.Aut() for representative in representatives)

    representative_images = tuple(
        quotient.image(representative) for representative in representatives
    )
    assert len(set(representative_images)) == 2
    assert set(representative_images) == set(quotient.image_keys())
    assert sum(representative in subgroup for representative in representatives) == 1


def test_each_right_coset_representative_is_a_live_lattice_isometry() -> None:
    lattice = NamedLattices.A1
    root = lattice.module_generator(0)
    subgroup = lattice.SO()
    representatives = subgroup.finite_character_quotient().right_coset_transversal()

    images = tuple(representative(root) for representative in representatives)
    assert len(images) == 2
    assert root in images
    assert -root in images

r"""Finite-character right cosets retain live orthogonal-group lifts."""

from dzack_research.preamble.all import NamedLattices, finite_ordered_set


def test_special_orthogonal_group_has_two_right_cosets_in_O_A1() -> None:
    lattice = NamedLattices.A1
    subgroup = lattice.SO()
    quotient = subgroup.finite_character_quotient()
    representatives = quotient.right_coset_transversal()

    assert tuple(quotient.image_space().index_set()) == ("determinant",)
    assert quotient.image_keys().cardinality() == 2
    assert quotient.subgroup_image_keys().cardinality() == 1
    assert representatives.cardinality() == 2
    assert all(representative.parent() is lattice.Aut() for representative in representatives)

    representative_images = finite_ordered_set(
        [quotient.image(representative) for representative in representatives]
    )
    assert all(image.parent() is quotient.image_space() for image in representative_images)
    assert representative_images.cardinality() == 2
    assert representative_images == quotient.image_keys()
    assert sum(representative in subgroup for representative in representatives) == 1


def test_each_right_coset_representative_is_a_live_lattice_isometry() -> None:
    lattice = NamedLattices.A1
    root = lattice.basis_vector(0)
    subgroup = lattice.SO()
    representatives = subgroup.finite_character_quotient().right_coset_transversal()

    images = finite_ordered_set(
        [representative(root) for representative in representatives]
    )
    assert images.cardinality() == 2
    assert root in images
    assert -root in images

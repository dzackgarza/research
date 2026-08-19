from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import (
    DiscriminantOrthogonalGroup,
    Lattice,
    LatticeDiscriminantGroup,
    LatticeElement,
    LatticeOrthogonalSubgroup,
    OrthogonalGroup,
    StableOrthogonalGroup,
)


def test_lattice_group_accessors_have_explicit_types():
    """
    method: stable_orthogonal_group

    Group-accessor contract:
    lattice exposes O(L), O^+(L), and O(A_L) with explicitly typed accessors.
    """
    lattice: Lattice = Lattice.hyperbolic(rank=3)
    full_group: OrthogonalGroup = lattice.orthogonal_group()
    stable_group: StableOrthogonalGroup = lattice.stable_orthogonal_group()
    discr_group: DiscriminantOrthogonalGroup = lattice.discriminant_orthogonal_group()
    discr_data: LatticeDiscriminantGroup = lattice.discriminant()
    discr_group_from_discriminant: DiscriminantOrthogonalGroup = discr_data.orthogonal_group()
    root = lattice.vinberg().simple_roots()[0]
    nontrivial_isometry = lattice.reflection(root)

    assert_equal(
        discr_group == discr_group_from_discriminant,
        True,
        "Lattice.discriminant_orthogonal_group should match L.discriminant().orthogonal_group()",
    )
    assert_equal(
        full_group.contains(nontrivial_isometry),
        True,
        "Orthogonal group should contain nontrivial root reflection isometry",
    )
    assert_equal(
        stable_group.contains(nontrivial_isometry),
        True,
        "Stable orthogonal group should contain nontrivial root reflection isometry",
    )


def test_lattice_set_stabilizer_accessor_with_optional_subgroup():
    """
    method: orthogonal_set_stabilizer

    Stabilizer contract:
    lattice-level set stabilizer accepts optional subgroup and returns subgroup of O(L).
    """
    lattice: Lattice = Lattice.hyperbolic(rank=3)
    e1: LatticeElement = lattice.element((1, 0, 0))
    e2: LatticeElement = lattice.element((0, 1, 0))
    vectors: tuple[LatticeElement, LatticeElement] = (e1, e2)
    stable_group: StableOrthogonalGroup = lattice.stable_orthogonal_group()
    root = lattice.vinberg().simple_roots()[0]
    nontrivial_isometry = lattice.reflection(root)

    stabilizer_default: LatticeOrthogonalSubgroup = lattice.orthogonal_set_stabilizer(vectors)
    stabilizer_stable: LatticeOrthogonalSubgroup = lattice.orthogonal_set_stabilizer(vectors, subgroup=stable_group)

    assert_equal(
        stabilizer_default.contains(nontrivial_isometry),
        True,
        "Default set stabilizer should contain nontrivial reflection in contract model",
    )
    assert_equal(
        stabilizer_stable.contains(nontrivial_isometry),
        True,
        "Subgroup-restricted set stabilizer should contain nontrivial reflection in contract model",
    )


def test_orthogonal_group_set_stabilizer_accessor_with_typed_vectors():
    """
    method: stabilizer_of_set

    Stabilizer contract:
    group-level set stabilizer accepts typed vector collections and returns a subgroup object.
    """
    lattice: Lattice = Lattice.hyperbolic(rank=3)
    group: OrthogonalGroup = lattice.orthogonal_group()
    vectors: list[LatticeElement] = [lattice.element((1, 0, 0)), lattice.element((0, 1, 0))]
    root = lattice.vinberg().simple_roots()[1]
    nontrivial_isometry = lattice.reflection(root)

    stabilizer: LatticeOrthogonalSubgroup = group.stabilizer_of_set(vectors)
    assert_equal(
        stabilizer.contains(nontrivial_isometry),
        True,
        "OrthogonalGroup.stabilizer_of_set should contain nontrivial reflection in contract model",
    )

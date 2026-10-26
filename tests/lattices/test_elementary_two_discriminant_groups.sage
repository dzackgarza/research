r"""Orthogonal groups of the split quadratic form on F_2^(2m).

For each nonzero singular x, there are 2^(2m-2) singular y with b(x,y)=1.
There are (2^m-1)(2^(m-1)+1) choices of x. Removing the hyperbolic pair
therefore gives the order recurrence, with |O(0)|=1. For m=1,2,5 the
orders are 2, 72 and 46998591897600. The discriminant form of U(2)^m is
this split quadratic form, with values read in Q/2Z.
"""

import pytest

from dzack_research.preamble.all import Lattices, ZZ


@pytest.mark.parametrize("planes, expected", [(1, 2), (2, 72), (5, 46998591897600)])
def test_split_elementary_two_discriminant_orthogonal_group(planes, expected) -> None:
    lattice = Lattices(ZZ)([[0, 2], [2, 0]]) ** int(planes)
    form = lattice.discriminant_group()
    group = form.orthogonal_group()

    assert group.cardinality() == expected
    basis = tuple(form.module_generators())
    for generator in group.group_generators():
        for i, left in enumerate(basis):
            assert form.q(generator(left)) == form.q(left)
            for right in basis[i + 1:]:
                assert form.q(generator(left + right)) == form.q(left + right)


def test_hyperbolic_discriminant_form_of_exponent_four() -> None:
    r"""The isometries of xy/2 mod 2 on (Z/4)^2 are +/-1 and +/-swap."""
    form = Lattices(ZZ)([[0, 4], [4, 0]]).discriminant_group()
    group = form.orthogonal_group()

    assert group.cardinality() == 4
    for generator in group.group_generators():
        assert all(form.q(generator(point)) == form.q(point) for point in form.elements())


def test_split_four_dimensional_form_cosets_are_its_nonzero_singular_vectors() -> None:
    r"""O^+(4,2) acts transitively on its nine nonzero singular vectors.

    The stabilizer has order 72/9=8. The coset section must send its
    distinguished vector to the corresponding orbit point, and its
    Schreier images must generate that stabilizer.
    """
    form = (Lattices(ZZ)([[0, 2], [2, 0]]) ** 2).discriminant_group()
    group = form.orthogonal_group()
    vector = next(iter(form.module_generators()))
    vector_stabilizer = group.stabilizer_of_element(vector)
    stabilizer = group.subgroup_on(tuple(vector_stabilizer.group_generators()))
    cosets = group.left_cosets(stabilizer)
    section = cosets.representative_map()

    assert stabilizer.cardinality() == 8
    assert cosets.cardinality() == 9
    assert len({section(point)(vector) for point in cosets}) == 9
    for point in cosets:
        assert cosets.coset_of(section(point)) == point
        for generator in group.group_generators():
            assert section(cosets.act(generator, point))(vector) == generator(section(point)(vector))
    augmentation = cosets.schreier_generating_morphism()
    images = tuple(augmentation(generator) for generator in augmentation.domain().group_generators())
    assert group.subgroup_on(images).cardinality() == 8

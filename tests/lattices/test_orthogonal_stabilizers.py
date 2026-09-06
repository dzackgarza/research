r"""Stabilizer subgroups of \(O(L)\).

A stabilizer is cut out of \(O(L)\) by its defining condition, so it is an
object for indefinite \(L\) as well, where \(O(L)\) is infinite and cannot be
enumerated.  The specimens below separate the three conditions from one
another: fixing a vector, fixing a sublattice pointwise, and carrying a
sublattice onto itself.
"""

from dzack_research.preamble.all import ZZ, Lattices


def test_a_reflection_fixes_the_vectors_orthogonal_to_its_root() -> None:
    r"""\(s_r\) fixes \(r^\perp\) pointwise and negates \(r\)."""
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic, partner, root, _second_root = lattice.module_generators()
    reflection = lattice.reflection(root)

    assert reflection in lattice.O().stabilizer(isotropic)
    assert reflection in lattice.O().stabilizer(partner)
    assert reflection not in lattice.O().stabilizer(root)
    assert reflection(root) == -root


def test_the_setwise_stabilizer_of_an_isotropic_line_holds_maps_the_pointwise_one_does_not() -> None:
    r"""\(-\mathrm{id}\) carries \(\mathbb Ze\) onto itself without fixing \(e\).

    That separates \(\operatorname{Stab}(I)\) from the pointwise stabilizer,
    so a test that confused the two would fail here.
    """
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic = lattice.module_generator(0)
    line = isotropic.sublattice()
    embedding = line.inclusion()
    orthogonal_group = lattice.O()

    negation = orthogonal_group(lambda label: -lattice.module_generator(label))

    assert negation in orthogonal_group.setwise_stabilizer(embedding)
    assert negation not in orthogonal_group.pointwise_stabilizer(embedding)
    assert negation not in orthogonal_group.stabilizer(isotropic)


def test_a_reflection_in_a_root_orthogonal_to_a_line_stabilizes_it_pointwise() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic, _partner, root, _second_root = lattice.module_generators()
    line = isotropic.sublattice()
    embedding = line.inclusion()
    reflection = lattice.reflection(root)
    orthogonal_group = lattice.O()

    assert reflection in orthogonal_group.pointwise_stabilizer(embedding)
    assert reflection in orthogonal_group.setwise_stabilizer(embedding)


def test_a_transvection_moving_a_line_leaves_its_setwise_stabilizer() -> None:
    r"""\(t(e,a)\) fixes \(\mathbb Ze\) but moves \(\mathbb Zf\) off itself."""
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A2")
    isotropic, partner, root, _second_root = lattice.module_generators()
    transvection = lattice.eichler_transvection(isotropic, root)
    orthogonal_group = lattice.O()

    assert transvection in orthogonal_group.setwise_stabilizer(
        isotropic.sublattice().inclusion()
    )
    assert transvection not in orthogonal_group.setwise_stabilizer(
        partner.sublattice().inclusion()
    )


def test_the_orthogonal_group_names_the_lattice_it_acts_on() -> None:
    lattice = Lattices(ZZ)("U")
    assert lattice.O().lattice() is lattice


def test_the_stabilizer_of_a_root_holds_exactly_the_expected_involution() -> None:
    r"""In \(A_2\), \(-s_r\) fixes \(r\) while neither \(-\mathrm{id}\) nor \(s_r\) does.

    \(s_r(r)=-r\) and \(-\mathrm{id}(r)=-r\), so their product is the
    nonidentity element of \(\operatorname{Stab}_{O(A_2)}(r)\); a predicate
    that tested the line \(\mathbb Zr\) instead of the vector \(r\) would
    admit all three.
    """
    root_lattice = Lattices(ZZ)("A2")
    root = root_lattice.module_generator(0)
    orthogonal_group = root_lattice.O()
    stabilizer = orthogonal_group.stabilizer(root)

    reflection = root_lattice.reflection(root)
    negation = orthogonal_group(
        lambda label: -root_lattice.module_generator(label)
    )

    assert reflection not in stabilizer
    assert negation not in stabilizer
    assert negation * reflection in stabilizer
    assert (negation * reflection)(root) == root

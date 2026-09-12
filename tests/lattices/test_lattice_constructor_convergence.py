r"""Structured lattice constructors stay behind the ``Lattices`` owner."""

from dzack_research.preamble.all import Groups, Lattices, ZZ


def test_structured_lattice_specializations_retain_their_defining_data() -> None:
    root = Lattices(ZZ)("A2")
    root_span = root.root_sublattice()

    assert root_span.inclusion().codomain() is root
    assert str(root_span.cartan_type()) == "['A', 2]"

    hyperbolic = Lattices(ZZ)("U") + root
    reduction = hyperbolic.module_generator(0).isotropic_reduction()
    assert reduction.isotropic_embedding().codomain() is hyperbolic
    assert reduction.orthogonal_complement().inclusion().codomain() is hyperbolic
    assert reduction.quotient_lattice() is reduction

    group = Groups.C(2)
    plane = Lattices(ZZ)("U")

    def swap(group_element, vector):
        if group_element == group.one():
            return vector
        left, right = vector.to_tuple()
        return plane((right, left))

    acted = Lattices(ZZ[group])(plane, swap)
    assert acted.action().domain() is group
    assert acted.gram_tensor() == plane.gram_tensor()

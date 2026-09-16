r"""Structured lattice constructors stay behind the ``Lattices`` owner."""

from dzack_research.preamble.all import ZZ, Groups, Lattices


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
    labels = plane.module_generating_set()
    left, right = plane.module_generators()
    swap_isometry = plane.Aut()({labels[0]: right, labels[1]: left})

    def swap(group_element, vector):
        if group_element == group.one():
            return vector
        return swap_isometry(vector)

    acted = Lattices(ZZ[group])(plane, swap)
    assert acted.source_group_module().unacted_module() is plane
    assert acted.action().domain() is group
    assert acted.gram_tensor() == plane.gram_tensor()

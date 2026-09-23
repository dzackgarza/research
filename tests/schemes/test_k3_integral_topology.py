"""A quartic K3 retains its integral middle lattice and divisor inclusion."""

from dzack_research.preamble.all import (
    QQ,
    NamedLattices,
    ProjectiveCompleteIntersections,
    ProjectiveSpaces,
)


def _fermat_quartic():
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    return ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0**4 + x1**4 + x2**4 + x3**4
    )


def test_quartic_k3_middle_integral_cohomology_is_the_k3_lattice() -> None:
    quartic = _fermat_quartic()
    topology = quartic.integral_topology()
    middle = topology.integral_cohomology(2)

    assert middle is NamedLattices.LK3
    assert middle.module_rank() == 22
    signature = middle.signature_pair()
    assert signature.first() == 3
    assert signature.second() == 19
    assert middle.is_even()
    assert middle.is_unimodular()
    assert topology.middle_cohomology_torsion_free_quotient() is middle
    assert topology.integral_cohomology(0).module_rank() == 1
    assert topology.integral_cohomology(1).module_rank() == 0
    assert topology.integral_cohomology(3).module_rank() == 0
    assert topology.integral_cohomology(4).module_rank() == 1


def test_quartic_hyperplane_c1_is_primitive_square_four_and_pairing_is_cup_product() -> None:
    quartic = _fermat_quartic()
    topology = quartic.integral_topology()
    middle = topology.middle_cohomology_lattice()
    hyperplane = topology.hyperplane_first_chern_class()
    embedding = topology.hyperplane_c1_embedding()
    pairing = topology.cup_product_pairing()

    assert middle.q(hyperplane) == 4
    assert hyperplane.is_primitive()
    assert embedding.codomain() is middle
    assert embedding.is_primitive()
    assert pairing(hyperplane, hyperplane) == 4
    assert topology.first_chern_class(quartic.O(2)) == 2 * hyperplane


def test_quartic_k3_cup_product_is_graded_and_uses_the_middle_intersection_form() -> None:
    quartic = _fermat_quartic()
    topology = quartic.integral_topology()
    middle = topology.integral_cohomology(2)
    top = topology.integral_cohomology(4)
    h = topology.hyperplane_first_chern_class()
    top_generator = next(iter(top.module_generators()))

    middle_product = topology.cup_product(2, 2)
    assert middle_product(h, h) == 4 * top_generator

    unit = topology.integral_cohomology(0)
    unit_generator = next(iter(unit.module_generators()))
    assert topology.cup_product(0, 2)(unit_generator, h) == h
    assert topology.cup_product(2, 4)(h, top_generator).parent().module_rank() == 0

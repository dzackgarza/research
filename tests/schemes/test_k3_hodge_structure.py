"""The quartic K3 Hodge structure is attached to adjunction and the K3 lattice."""

from dzack_research.preamble.all import NN, QQ, ProjectiveCompleteIntersections, ProjectiveSpaces


def _quartic():
    space = ProjectiveSpaces(QQ)(3)
    x0, x1, x2, x3 = space.homogeneous_coordinate_generators()
    return ProjectiveCompleteIntersections(space.scheme_base_ring())(
        space, x0**4 + x1**4 + x2**4 + x3**4
    )


def test_quartic_k3_hodge_numbers_have_off_diagonal_holomorphic_two_forms() -> None:
    quartic = _quartic()
    hodge = quartic.hodge_structure()

    assert hodge.scheme() is quartic
    assert hodge.is_pure()
    assert hodge.holomorphic_two_form_space().dimension() == 1
    assert hodge.hodge_number(2, 0) == 1
    assert hodge.hodge_number(0, 2) == 1
    assert hodge.hodge_number(1, 1) == 20
    assert hodge.middle_betti_number() == 22

    degree_two = hodge.degree_hodge_numbers(2)
    assert degree_two.cardinality() == 3
    bidegrees = tuple(degree_two.index_set())
    assert tuple(tuple(int(component) for component in bidegree) for bidegree in bidegrees) == (
        (0, 2),
        (1, 1),
        (2, 0),
    )
    assert tuple(degree_two) == (NN(1), NN(20), NN(1))
    assert all(value in NN for value in degree_two)
    assert sum(int(value) for value in degree_two) == int(hodge.integral_cohomology(2).module_rank())


def test_quartic_hodge_polarization_is_the_integral_hyperplane_class() -> None:
    quartic = _quartic()
    hodge = quartic.hodge_structure()
    topology = quartic.integral_topology()

    assert hodge.integral_cohomology(2) is topology.middle_cohomology_lattice()
    assert hodge.polarization_class() == topology.hyperplane_first_chern_class()
    assert topology.cup_product_pairing()(hodge.polarization_class(), hodge.polarization_class()) == 4

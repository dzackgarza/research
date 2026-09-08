from dzack_research.preamble.all import PolynomialRing, QQ
from dzack_research.preamble.categories.schemes.singularities import (
    IsolatedHypersurfaceSingularity,
)


def test_cusp_milnor_tjurina_and_completion_share_the_hypersurface_equation() -> None:
    plane = PolynomialRing(QQ, ("x", "y"))
    x, y = plane.algebra_generators()
    cusp = IsolatedHypersurfaceSingularity(plane, y**2 - x**3)

    assert cusp.milnor_number() == 2
    assert cusp.tjurina_number() == 2
    assert cusp.milnor_algebra().relations().cardinality() == 2
    assert cusp.tjurina_algebra().relations().cardinality() == 3
    completion = cusp.completed_local_ring(precision=6)
    assert completion.computation_precision() == 6
    assert len(completion.maximal_ideal().ideal_generators()) == 2


def test_a_two_node_has_one_dimensional_milnor_and_tjurina_algebras() -> None:
    plane = PolynomialRing(QQ, ("x", "y"))
    x, y = plane.algebra_generators()
    node = IsolatedHypersurfaceSingularity(plane, x**2 + y**2)

    assert node.milnor_number() == 1
    assert node.tjurina_number() == 1

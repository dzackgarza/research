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
    assert node.zariski_tangent_space().module_rank() == 2
    assert node.is_singular_at_origin()


def test_a_smooth_hypersurface_origin_has_the_jacobian_tangent_hyperplane() -> None:
    plane = PolynomialRing(QQ, ("x", "y"))
    x, y = plane.algebra_generators()
    smooth = IsolatedHypersurfaceSingularity(plane, x + y**2)

    tangent = smooth.zariski_tangent_space()
    embedding = smooth.zariski_tangent_embedding()

    assert tangent.module_rank() == 1
    assert smooth.is_regular_at_origin()
    assert not smooth.is_singular_at_origin()
    assert embedding.domain() is tangent
    assert embedding.codomain() is smooth.ambient_tangent_space()


def test_cusp_delta_branch_and_conductor_are_local_normalization_invariants() -> None:
    plane = PolynomialRing(QQ, ("x", "y"))
    x, y = plane.algebra_generators()
    cusp = IsolatedHypersurfaceSingularity(plane, y**2 - x**3)

    assert cusp.delta_invariant() == 1
    assert cusp.local_tjurina_number() == 2
    assert cusp.number_of_branches_at_origin() == 1

    conductor = cusp.conductor_ideal_at_origin()
    local_ring = conductor.ring()
    localization = local_ring.localization_map()
    assert localization(x) in conductor
    assert localization(y) in conductor

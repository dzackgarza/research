from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.schemes.singularities import (
    IsolatedHypersurfaceSingularity,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_curves_and_singularities.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/singularities.py",
    "disposition": "reconciled-live-owner",
}


def test_cusp_milnor_tjurina_and_completion_share_the_hypersurface_equation() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x, y = plane.algebra_generators()
    cusp = IsolatedHypersurfaceSingularity(plane, y**2 - x**3)
    jacobian = cusp.jacobian_generators()

    assert tuple(jacobian.index_set()) == tuple(plane.algebra_generating_set())
    assert jacobian["x"] == -3 * x**2
    assert jacobian["y"] == 2 * y
    assert cusp.milnor_number() == 2
    assert cusp.tjurina_number() == 2
    assert cusp.milnor_algebra().relations().cardinality() == 2
    assert cusp.tjurina_algebra().relations().cardinality() == 3
    completion = cusp.completed_local_ring(precision=6)
    assert completion.computation_precision() == 6
    assert len(completion.maximal_ideal().ideal_generators()) == 2


def test_a_two_node_has_one_dimensional_milnor_and_tjurina_algebras() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
    x, y = plane.algebra_generators()
    node = IsolatedHypersurfaceSingularity(plane, x**2 + y**2)

    assert node.milnor_number() == 1
    assert node.tjurina_number() == 1
    assert node.zariski_tangent_space().module_rank() == 2
    assert node.is_singular_at_origin()




def test_cusp_delta_branch_and_conductor_are_local_normalization_invariants() -> None:
    plane = QQ.polynomial_ring(("x", "y"))
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


def test_archived_a1_and_a3_curve_germs_keep_their_ade_invariants() -> None:
    for label, milnor in (("A1", 1), ("A3", 3)):
        singularity = IsolatedHypersurfaceSingularity.from_ade_type(QQ, label)
        assert singularity.ade_normal_form_type() == ("A", milnor)
        assert singularity.milnor_number() == milnor
        assert singularity.tjurina_number() == milnor
        assert singularity.is_singular_at_origin()


def test_selected_ade_plane_curve_normal_forms_retain_their_exact_type() -> None:
    for label, milnor in (("A4", 4), ("D5", 5), ("E6", 6), ("E7", 7), ("E8", 8)):
        singularity = IsolatedHypersurfaceSingularity.from_ade_type(QQ, label)
        assert singularity.ade_normal_form_type() == (label[0], int(label[1:]))
        assert singularity.milnor_number() == milnor



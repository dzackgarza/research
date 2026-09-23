"""Non-toric pointed fundamental groups retain base points and induced maps."""

from dzack_research.preamble.all import (
    GeometricFundamentalGroups,
    NodalCubicIntegralTopology,
    PGL2IntegralTopology,
)


def test_pgl2_has_nontrivial_pointed_fundamental_group_at_the_identity() -> None:
    topology = PGL2IntegralTopology()
    point = topology.base_point()
    group = topology.fundamental_group()

    assert point.codomain() is topology.scheme()
    assert tuple(point.point_coordinates()) == (point.codomain().scheme_base_ring()(1), point.codomain().scheme_base_ring()(0), point.codomain().scheme_base_ring()(0), point.codomain().scheme_base_ring()(1))
    assert group in GeometricFundamentalGroups()
    assert group.topological_scheme() is topology.scheme()
    assert group.base_point() is point
    assert "_preamble_topological_scheme" not in group.__dict__
    assert "_preamble_topological_base_point" not in group.__dict__
    assert "_preamble_topological_realization_description" not in group.__dict__
    assert int(group.order()) == 2


def test_nodal_normalization_is_pointed_and_induces_trivial_to_infinite_cyclic_pi1_map() -> None:
    topology = NodalCubicIntegralTopology()
    normalization = topology.normalization_morphism()
    source_point = topology.normalization_base_point()
    target_point = topology.base_point()
    induced = topology.normalization_fundamental_group_map()

    assert normalization.domain() is source_point.codomain()
    assert normalization.codomain() is target_point.codomain()
    assert tuple(normalization.image_of_point(source_point).point_coordinates()) == tuple(target_point.point_coordinates())
    assert induced.domain() is topology.normalization_fundamental_group()
    assert induced.codomain() is topology.fundamental_group()
    assert induced.domain().number_of_group_generators() == 0
    assert induced.codomain().number_of_group_generators() == 1
    assert induced.is_injective()
    assert not induced.is_surjective()

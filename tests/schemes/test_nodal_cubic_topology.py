"""A singular curve distinguishes ordinary from normalization-resolution cohomology."""

from dzack_research.preamble.all import (
    ZZ,
    IntegralSingularCohomologyGroups,
    NodalCubic,
    NodalCubicIntegralTopology,
    NodalCubicNormalization,
    ResolutionIntegralCohomologyGroups,
)


def test_nodal_cubic_normalization_is_an_actual_projective_scheme_morphism() -> None:
    curve = NodalCubic()
    normalization = NodalCubicNormalization()

    assert normalization.codomain() is curve
    assert normalization.domain().relative_dimension() == 1
    assert tuple(normalization.homogeneous_coordinates())


def test_nodal_cubic_ordinary_and_resolution_cohomology_are_distinct_selected_theories() -> None:
    topology = NodalCubicIntegralTopology()
    ordinary_h1 = topology.ordinary_cohomology(1)
    resolution_h1 = topology.resolution_cohomology(1)

    assert ordinary_h1 in IntegralSingularCohomologyGroups(ZZ)
    assert resolution_h1 in ResolutionIntegralCohomologyGroups(ZZ)
    assert ordinary_h1.module_rank() == 1
    assert resolution_h1.module_rank() == 0
    assert ordinary_h1.cohomology_topology() == "ordinary singular cohomology"
    assert resolution_h1.cohomology_topology() == "resolution cohomology via normalization"
    assert ordinary_h1.topological_scheme() is topology.scheme()
    assert resolution_h1.topological_scheme() is topology.scheme()


def test_normalization_pullback_is_the_actual_induced_map_and_kills_the_node_loop() -> None:
    topology = NodalCubicIntegralTopology()
    pullback_h1 = topology.normalization_pullback(1)
    source_generator = next(iter(pullback_h1.domain().module_generators()))

    assert pullback_h1(source_generator) == pullback_h1.codomain().zero()
    pullback_h2 = topology.normalization_pullback(2)
    top_generator = next(iter(pullback_h2.domain().module_generators()))
    assert pullback_h2(top_generator) != pullback_h2.codomain().zero()
    assert topology.normalization_morphism().codomain() is topology.scheme()

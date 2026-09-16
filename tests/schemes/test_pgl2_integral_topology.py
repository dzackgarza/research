"""PGL2 ordinary integral cohomology retains the torsion lost rationally."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    IntegralSingularCohomologyGroups,
    PGL2IntegralTopology,
    ProjectiveGeneralLinearGroup2,
)


def test_pgl2_is_the_projective_determinant_complement_with_zmod2_cohomology() -> None:
    scheme = ProjectiveGeneralLinearGroup2()
    topology = PGL2IntegralTopology(scheme)
    torsion = topology.integral_cohomology(2)

    assert topology.scheme() is scheme
    assert torsion in IntegralSingularCohomologyGroups(ZZ)
    assert torsion.topological_scheme() is scheme
    assert torsion.integral_topological_cohomology_construction().scheme() is scheme
    assert torsion.cohomological_degree() == 2
    assert torsion.cardinality() == 2
    assert topology.integral_cohomology(0).module_rank() == 1
    assert topology.integral_cohomology(1).module_rank() == 0
    assert topology.integral_cohomology(3).module_rank() == 1
    assert topology.integral_cohomology(4).module_rank() == 0


def test_rational_coefficient_change_kills_pgl2_torsion_by_an_actual_unit_map() -> None:
    topology = PGL2IntegralTopology()
    integral = topology.integral_cohomology(2)
    rational = topology.rational_cohomology(2)
    comparison = topology.coefficient_change_to_rationals(2)

    assert rational.base_ring() is QQ
    assert rational.is_zero()
    assert comparison.domain() is integral
    assert comparison(comparison.domain().module_generator(0)) == comparison.codomain().zero()

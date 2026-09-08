r"""H1 geometric complexes for supported toric line-bundle cohomology."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    BasedFreeModule,
    RationalPolyhedralFans,
    ToricGeometricLineBundleCohomologySpaces,
    ToricLineBundleCohomology,
    ToricWeightCohomology,
    ToricWeightCohomologyComplex,
    ToricWeightCohomologyComplexes,
)


def _projective_plane():
    fans = RationalPolyhedralFans(BasedFreeModule(ZZ, 2))
    return fans.projective_space_fan().toric_variety(QQ)


def test_hyperplane_weight_zero_is_computed_by_an_actual_geometric_complex() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    weight = plane.character_lattice().zero()
    complex_ = ToricWeightCohomologyComplex(plane, divisor, weight)
    cohomology = ToricWeightCohomology(plane, divisor, weight, 0)

    assert complex_ in ToricWeightCohomologyComplexes(QQ)
    assert complex_.cohomology_scheme() is plane
    assert complex_.cohomology_divisor() == divisor
    assert complex_.cohomology_weight() == weight
    assert cohomology.cochain_complex().cohomology_scheme() is plane
    assert cohomology.dimension() == 1


def test_a_weight_outside_the_hyperplane_polytope_has_zero_degree_zero_cohomology() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    characters = plane.character_lattice()
    first = next(iter(characters.module_generating_set()))
    outside = ZZ(3) * characters.module_generator(first)

    assert ToricWeightCohomology(plane, divisor, outside, 0).dimension() == 0


def test_total_hyperplane_cohomology_is_the_direct_sum_of_its_three_live_weight_pieces() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    cohomology = ToricLineBundleCohomology(plane, divisor, 0)

    assert cohomology in ToricGeometricLineBundleCohomologySpaces(QQ)
    assert cohomology.dimension() == 3
    assert cohomology.cohomology_weight_support().cardinality() == 3
    for weight in cohomology.cohomology_weight_support():
        piece = cohomology.cohomology_weight_piece(weight)
        inclusion = cohomology.cohomology_weight_inclusion(weight)
        assert piece.dimension() == 1
        assert inclusion.domain() is piece
        assert inclusion.codomain() is cohomology


def test_toric_scheme_cohomology_uses_the_geometric_weight_complex_route() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    cohomology = plane.line_bundle_cohomology(divisor, 0)

    assert cohomology in ToricGeometricLineBundleCohomologySpaces(QQ)
    assert cohomology.dimension() == 3

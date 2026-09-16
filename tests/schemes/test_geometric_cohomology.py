r"""H1 geometric complexes for supported toric line-bundle cohomology."""

from dzack_research.preamble.all import (
    NN,
    QQ,
    ZZ,
    Cat,
    RationalPolyhedralFans,
    ToricFundamentalGroups,
    ToricGeometricLineBundleCohomologySpaces,
    ToricIntegralSingularCohomologyGroups,
    ToricWeightCohomologyComplexes,
)


def _projective_plane():
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    return fans.projective_space_fan().toric_variety(QQ)


def test_hyperplane_weight_zero_is_computed_by_an_actual_geometric_complex() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    weight = plane.character_lattice().zero()
    complex_ = plane.weight_cohomology_complex(divisor, weight)
    cohomology = plane.weight_cohomology(divisor, weight, 0)

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

    assert plane.weight_cohomology(divisor, outside, 0).dimension() == 0


def test_total_hyperplane_cohomology_is_the_direct_sum_of_its_three_live_weight_pieces() -> None:
    plane = _projective_plane()
    divisor = plane.hyperplane_divisor()
    cohomology = plane.line_bundle_cohomology(divisor, 0)

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


def test_projective_plane_integral_singular_cohomology_is_even_and_cycle_generated() -> None:
    plane = _projective_plane()
    groups = tuple(plane.integral_singular_cohomology(degree) for degree in range(5))

    assert all(group in ToricIntegralSingularCohomologyGroups(ZZ) for group in groups)
    assert tuple(group.module_rank() for group in groups) == (1, 0, 1, 0, 1)
    assert groups[2].cohomology_topology() == "singular cohomology of the complex analytic realization"
    assert groups[2].integral_topological_cohomology_construction().scheme() is plane
    assert "_preamble_topological_scheme" not in groups[2].__dict__
    assert "_preamble_topological_cohomological_degree" not in groups[2].__dict__
    assert "_preamble_topological_cohomology_theory" not in groups[2].__dict__
    assert "_preamble_topological_realization_description" not in groups[2].__dict__


def test_projective_plane_cycle_class_is_an_explicit_integral_isomorphism() -> None:
    plane = _projective_plane()
    cycle_class = plane.cycle_class_isomorphism(1)
    chow = plane.chow_group(1)
    cohomology = plane.integral_singular_cohomology(2)
    generator = chow.module_generator(next(iter(chow.module_generating_set())))

    assert cycle_class.forward().domain() is chow
    assert cycle_class.forward().codomain() is cohomology
    assert cycle_class.inverse()(cycle_class.forward()(generator)) == generator


def test_projective_plane_middle_cohomology_form_has_square_one() -> None:
    plane = _projective_plane()
    formed = plane.middle_cohomology_form()
    generator = formed.module_generator(next(iter(formed.module_generating_set())))

    assert formed.b(generator, generator) == ZZ.one()


def test_hirzebruch_zero_middle_cohomology_form_is_unimodular_hyperbolic() -> None:
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    surface = fans.hirzebruch_surface_fan(0).toric_variety(QQ)
    formed = surface.middle_cohomology_form()

    assert formed.module_rank() == 2
    assert formed.is_unimodular()
    assert formed.determinant() == ZZ(-1)


def test_projective_plane_has_a_pointed_trivial_fundamental_group() -> None:
    plane = _projective_plane()
    cone = next(iter(plane.fan().maximal_cones()))
    fundamental = plane.fundamental_group(cone)

    assert fundamental in ToricFundamentalGroups()
    assert ToricFundamentalGroups() in Cat()
    assert ToricFundamentalGroups().category() is Cat()
    assert fundamental.topological_scheme() is plane
    assert fundamental.base_point_cone() is cone
    assert fundamental.group_generators().cardinality() == 0


def test_projective_plane_hodge_numbers_are_diagonal_and_connected_to_integral_cohomology() -> None:
    plane = _projective_plane()
    hodge = plane.hodge_structure()

    assert hodge.is_pure()
    assert hodge.hodge_number(0, 0) == 1
    assert hodge.hodge_number(1, 1) == 1
    assert hodge.hodge_number(2, 2) == 1
    assert hodge.hodge_number(2, 0) == 0
    assert hodge.integral_cohomology(2) is plane.integral_singular_cohomology(2)


def test_hirzebruch_zero_has_hodge_number_h11_two() -> None:
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    surface = fans.hirzebruch_surface_fan(0).toric_variety(QQ)

    assert surface.hodge_structure().hodge_number(1, 1) == 2


def test_toric_hodge_degree_family_has_owned_bidegrees_and_values() -> None:
    plane = _projective_plane()
    hodge = plane.hodge_structure()
    degree_two = hodge.degree_hodge_numbers(2)

    assert degree_two.cardinality() == 3
    assert all(value in NN for value in degree_two)
    assert tuple(
        tuple(int(component) for component in bidegree)
        for bidegree in degree_two.index_set()
    ) == ((0, 2), (1, 1), (2, 0))
    assert tuple(degree_two) == (NN(0), NN(1), NN(0))
    assert degree_two[degree_two.index_set()[1]] == NN(1)

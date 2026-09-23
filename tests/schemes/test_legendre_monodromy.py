"""The Legendre family carries its higher direct image, local system and monodromy."""

from dzack_research.preamble.categories.schemes.monodromy import (
    LegendreMonodromyFamily,
)


def test_legendre_family_retains_singular_fiber_and_smooth_punctured_stratum() -> None:
    data = LegendreMonodromyFamily()
    family = data.family_scheme()
    singular = data.singular_fiber()
    smooth = data.smooth_reference_fiber()

    assert family.family_morphism() is data.family_morphism()
    assert singular.base_change_source_complete_intersection() is family
    assert smooth.base_change_source_complete_intersection() is family
    assert data.smooth_stratum().disc_radius() == 0.75
    assert data.base_point().manifold() is data.smooth_stratum()
    assert tuple(data.base_point().coordinates()) == (0.5,)
    assert data.base_point().coordinates()[0].parent() is data.base_point().chart().coordinate(0).parent()

    singular_ring = singular.complete_intersection_ambient().O(3).global_sections().homogeneous_coordinate_ring()
    singular_equation = tuple(singular.homogeneous_defining_equations(singular_ring))[0]
    x = singular_ring.algebra_generator("x")
    y = singular_ring.algebra_generator("y")
    z = singular_ring.algebra_generator("z")
    assert singular_equation == y**2 * z - x**2 * (x - z)


def test_R1_is_a_local_system_with_actual_stalk_to_fiber_comparison() -> None:
    data = LegendreMonodromyFamily()
    local_system = data.higher_direct_image()
    point = data.base_point()
    comparison = data.stalk_to_fiber_comparison()

    assert data.cohomological_degree() == 1
    representation = local_system.functor()
    assert local_system in representation.functor_category()
    assert representation(representation.domain().an_object()) is data.fiber_cohomology(point)
    assert comparison.domain() is data.fiber_cohomology(point)
    assert comparison.codomain() is data.fiber_cohomology(point)


def test_positive_loop_has_nonidentity_picard_lefschetz_monodromy_preserving_pairing() -> None:
    data = LegendreMonodromyFamily()
    cohomology = data.fiber_cohomology(data.base_point())
    alpha_dual, beta_dual = tuple(cohomology.module_generators())
    pi_one = data.pointed_fundamental_group()
    generator = pi_one.positive_loop_generator()
    representation = data.monodromy_representation()
    point = representation.domain().an_object()
    action = representation(representation.domain().Mor(point, point)(generator))

    assert action(alpha_dual) == alpha_dual
    assert action(beta_dual) == 2 * alpha_dual + beta_dual
    assert action != cohomology.Mor(cohomology).identity()
    assert data.monodromy_preserves_pairing()
    assert cohomology.pairing(alpha_dual, beta_dual) == 1
    assert cohomology.pairing(action(alpha_dual), action(beta_dual)) == 1


def test_singular_specialization_is_not_claimed_by_the_smooth_local_system() -> None:
    data = LegendreMonodromyFamily()

    assert not hasattr(data.higher_direct_image(), "singular_fiber_specialization")
    assert not hasattr(data, "nearby_cycles")

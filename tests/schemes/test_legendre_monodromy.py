"""The Legendre family carries its higher direct image, local system and monodromy."""

from dzack_research.preamble.categories.schemes.monodromy import (
    LegendreMonodromyFamily,
)






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



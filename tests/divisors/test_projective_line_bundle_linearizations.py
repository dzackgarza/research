"""Character twists change projective section actions without changing the line bundle."""

from dzack_research.preamble.all import (
    QQ,
    ProjectiveSpaces,
)
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.schemes.ringed_spaces import QuasiCoherentSheaves
from dzack_research.preamble.categories.schemes.schemes import ClosedSubschemes


def _linearizations():
    line = ProjectiveSpaces(QQ)(1, names=("x", "y"))
    bundle = line.O(1)
    trivial = bundle.c2_coordinate_swap_linearization(1)
    sign = bundle.c2_coordinate_swap_linearization(-1)
    return line, bundle, trivial, sign


def test_two_character_twists_keep_same_bundle_but_swap_section_eigenspaces() -> None:
    _line, bundle, trivial, sign = _linearizations()
    group = trivial.acting_group()
    generator = next(iter(group.group_generators()))
    sections = bundle.global_sections()
    ring = sections.homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    symmetric = sections.section_from_homogeneous_polynomial(x + y)
    alternating = sections.section_from_homogeneous_polynomial(x - y)

    assert trivial.line_bundle() is bundle
    assert sign.line_bundle() is bundle
    assert trivial in GObjects(group, QuasiCoherentSheaves(bundle.scheme()))
    assert sign in GObjects(group, QuasiCoherentSheaves(bundle.scheme()))
    assert trivial.scheme_action_functor() is sign.scheme_action_functor()
    assert trivial.character_value(generator) == 1
    assert sign.character_value(generator) == -1
    assert trivial.section_action_of(generator)(symmetric) == symmetric
    assert trivial.section_action_of(generator)(alternating) == -alternating
    assert sign.section_action_of(generator)(symmetric) == -symmetric
    assert sign.section_action_of(generator)(alternating) == alternating
    assert trivial.cocycle_holds(generator, generator)
    assert sign.cocycle_holds(generator, generator)


def test_fixed_point_fiber_evaluation_is_equivariant_and_detects_character_twist() -> None:
    line, _bundle, trivial, sign = _linearizations()
    point = line.point_morphism((1, 1))
    group = trivial.acting_group()
    generator = next(iter(group.group_generators()))
    trivial_evaluation = trivial.fixed_point_fiber_evaluation(point)
    sign_evaluation = sign.fixed_point_fiber_evaluation(point)
    trivial_fiber = trivial_evaluation.codomain()
    sign_fiber = sign_evaluation.codomain()
    trivial_label = next(iter(trivial_fiber.module_generating_set()))
    sign_label = next(iter(sign_fiber.module_generating_set()))
    trivial_generator = trivial_fiber.module_generator(trivial_label)
    sign_generator = sign_fiber.module_generator(sign_label)

    assert trivial.point_is_fixed(point)
    assert sign.point_is_fixed(point)
    assert trivial_fiber.act(generator, trivial_generator) == trivial_generator
    assert sign_fiber.act(generator, sign_generator) == -sign_generator
    assert trivial_evaluation.parent().is_equivariant(trivial_evaluation) is True
    assert sign_evaluation.parent().is_equivariant(sign_evaluation) is True


def test_sign_eigensection_has_invariant_zero_divisor_and_isotypic_piece() -> None:
    _line, bundle, trivial, _sign = _linearizations()
    group = trivial.acting_group()
    generator = next(iter(group.group_generators()))
    sections = bundle.global_sections()
    ring = sections.homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    alternating = sections.section_from_homogeneous_polynomial(x - y)
    sign_character = lambda element: QQ.one() if element == group.one() else -QQ.one()
    divisor = trivial.eigensection_divisor(alternating, sign_character)
    decomposition = trivial.isotypic_decomposition()
    construction = trivial.eigensection_divisor_construction(divisor)
    lift = trivial.linearization_isomorphism(generator)

    assert divisor.inclusion().codomain() is trivial.projective_space()
    assert divisor in ClosedSubschemes(QQ)
    assert trivial.is_eigensection_divisor(divisor)
    assert construction is divisor
    assert construction.linearization() is trivial
    assert construction.section() == alternating
    assert construction.character() is sign_character
    assert lift in QuasiCoherentSheaves(bundle.scheme()).Core().Mor(bundle, bundle)
    assert trivial.is_eigensection(alternating, sign_character)
    assert decomposition.nontrivial_components()
    assert trivial.section_group_module().act(
        generator,
        trivial.section_group_module().equip_action_morphism()(alternating),
    ) != trivial.section_group_module().equip_action_morphism()(alternating)


def test_nonnegative_projective_line_cohomology_inherits_the_linearized_action() -> None:
    _line, _bundle, trivial, _sign = _linearizations()
    h0 = trivial.coherent_cohomology_group_module(0)
    h1 = trivial.coherent_cohomology_group_module(1)

    assert h0 is trivial.section_group_module()
    assert h0.coefficient_module_rank() == 2
    assert h1.coefficient_module_rank() == 0
    assert h1.is_trivial_action()


def test_restriction_to_an_eigensection_divisor_is_an_equivariant_h0_map() -> None:
    _line, bundle, trivial, _sign = _linearizations()
    group = trivial.acting_group()
    sections = bundle.global_sections()
    ring = sections.homogeneous_coordinate_ring()
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    alternating = sections.section_from_homogeneous_polynomial(x - y)
    sign_character = lambda element: QQ.one() if element == group.one() else -QQ.one()
    divisor = trivial.eigensection_divisor(alternating, sign_character)
    restriction = trivial.equivariant_section_restriction(divisor)

    assert restriction.domain() is trivial.coherent_cohomology_group_module(0)
    assert restriction.codomain().coefficient_module_rank() == 1
    assert restriction.parent().is_equivariant(restriction) is True


def test_line_bundle_linearize_routes_to_the_projective_space_owner() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x", "y"))
    bundle = line.O(1)
    action = line.coordinate_swap_action()
    linearized = bundle.linearize(action, lambda _element: QQ.one())

    assert linearized.line_bundle() is bundle
    assert linearized.section_scheme() is line


def test_product_line_bundle_linearize_routes_to_the_multiprojective_owner() -> None:
    line = ProjectiveSpaces(QQ)(1)
    product = line.scheme_category().product((line, line))
    bundle = product.O(1, 1)
    action = product.c2_diagonal_sign_action()
    linearized = bundle.linearize(action, lambda _element: QQ.one())
    construction = linearized.coordinate_action_construction()

    assert linearized.line_bundle() is bundle
    assert linearized.section_scheme() is product
    assert construction.coordinate_weights() is linearized.coordinate_weights()
    assert construction.local_automorphisms().index_set() is product.standard_affine_atlas().chart_index_set()

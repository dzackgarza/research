r"""Selected projective linear systems retain base loci and rational-map domains."""

from dzack_research.preamble.all import QQ, OpenImmersions, ProjectiveSpaces

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_linear_systems_restrictions.sage",
    "live_owner": "tests/divisors/test_projective_linear_systems.py",
    "owner_overrides": {
        "test_restriction_map_has_expected_rank_and_cokernel": "tests/divisors/test_projective_section_restrictions.py",
    },
    "disposition": "reconciled-live-owner",
}


def _coordinate_sections(bundle):
    sections = bundle.global_sections()
    labels = tuple(sections.module_generating_set())
    return tuple(sections.module_generator(label) for label in labels)


def test_selected_linear_system_with_base_point_retains_actual_open_domain() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(1)
    x0, x1, _x2 = _coordinate_sections(bundle)

    system = bundle.linear_system((x0, x1))
    base_locus = system.base_locus()
    domain = system.domain_of_definition()
    morphism = system.associated_morphism()

    assert system.line_bundle() is bundle
    assert system.selected_section_space().dimension() == 2
    assert system.selected_section_space() is system.section_embedding().domain()
    for old_name in (
        "_preamble_linear_system_line_bundle",
        "_preamble_selected_section_space",
        "_preamble_section_embedding",
        "_preamble_base_locus",
    ):
        assert old_name not in system.__dict__
    assert system.projective_dimension() == 1
    assert system.variable_names() == ProjectiveSpaces(QQ)(1).variable_names()
    assert base_locus.inclusion().codomain() is plane
    assert not base_locus.is_empty()
    assert not system.is_basepoint_free()
    assert domain in OpenImmersions(plane)
    assert domain is not plane
    assert morphism.domain() is domain
    assert morphism.codomain() is system


def test_complete_hyperplane_system_has_empty_base_locus_and_everywhere_defined_map() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(1)
    system = bundle.linear_system()

    assert system.is_basepoint_free()
    assert system.base_locus().is_empty()
    assert system.domain_of_definition() is plane
    assert system.associated_morphism().domain() is plane
    assert system.associated_morphism().codomain() is system


def test_complete_quadrics_and_restriction_to_a_line_keep_expected_dimensions() -> None:
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    bundle = plane.O(2)
    system = bundle.linear_system()
    ring = bundle.global_sections().homogeneous_coordinate_ring()
    line = plane.closed_subscheme(ring.algebra_generator("x"))
    restriction = bundle.restriction_map(line)

    assert system.is_basepoint_free()
    assert system.projective_dimension() == 5
    assert system.associated_morphism().domain() is plane
    assert restriction.domain() is bundle.global_sections()
    assert restriction.domain().dimension() == 6
    assert restriction.codomain().dimension() == 3
    assert restriction.kernel().dimension() == 3

r"""All conic sections of P^2 form a five-dimensional projective linear system."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_complete_conic_sections_as_a_projective_linear_system() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    bundle = plane.O(2)
    system = bundle.linear_system()

    assert system in ProjectiveLinearSystems(QQ)
    assert system.line_bundle() is bundle
    assert system.ambient_section_space().dimension() == 6
    assert system.selected_section_space().dimension() == 6
    assert system.section_embedding().domain() is system.selected_section_space()
    assert system.section_embedding().codomain() is system.ambient_section_space()
    assert system.selected_sections().cardinality() == cardinal(6)
    assert system.projective_dimension() == 5
    assert system.is_basepoint_free()
    assert system.base_locus().is_empty()
    assert system.domain_of_definition() is plane
    assert system.associated_morphism().domain() is plane
    assert system.associated_morphism().codomain() is system


def test_quadrics_restrict_to_a_projective_line() -> None:
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    bundle = plane.O(2)
    system = bundle.linear_system()
    line = plane.closed_subscheme(plane.homogeneous_coordinate_ring()("x"))
    restriction = system.restriction_map(line)

    assert restriction.domain() is system.selected_section_space()
    assert restriction.domain().dimension() == 6
    assert restriction.codomain().dimension() == 3
    assert restriction.kernel().dimension() == 3

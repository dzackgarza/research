r"""Selected projective linear systems retain base loci and rational-map domains."""

from dzack_research.preamble.all import OpenImmersions, ProjectiveSpace, QQ


def _coordinate_sections(bundle):
    sections = bundle.global_sections()
    labels = tuple(sections.module_generating_set())
    return tuple(sections.module_generator(label) for label in labels)


def test_selected_linear_system_with_base_point_retains_actual_open_domain() -> None:
    plane = ProjectiveSpace(2, QQ)
    bundle = plane.O(1)
    x0, x1, _x2 = _coordinate_sections(bundle)

    system = bundle.linear_system((x0, x1))
    base_locus = system.base_locus()
    domain = system.domain_of_definition()
    morphism = system.associated_morphism()

    assert system.line_bundle() is bundle
    assert system.selected_section_space().dimension() == 2
    assert system.projective_dimension() == 1
    assert base_locus.inclusion().codomain() is plane
    assert not base_locus.is_empty()
    assert not system.is_basepoint_free()
    assert domain in OpenImmersions(plane)
    assert domain is not plane
    assert morphism.domain() is domain
    assert morphism.codomain() is system


def test_complete_hyperplane_system_has_empty_base_locus_and_everywhere_defined_map() -> None:
    plane = ProjectiveSpace(2, QQ)
    bundle = plane.O(1)
    system = bundle.linear_system()

    assert system.is_basepoint_free()
    assert system.base_locus().is_empty()
    assert system.domain_of_definition() is plane
    assert system.associated_morphism().domain() is plane
    assert system.associated_morphism().codomain() is system

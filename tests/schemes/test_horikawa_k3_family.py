r"""The Horikawa ``(4,4)`` family is built from the shared equivariant cover owners."""

from dzack_research.preamble.all import QQ, QuadraticField
from dzack_research.preamble.categories.schemes.k3_families import HorikawaK3Family

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/framework/test_group_actions_and_isotypics.sage",
        "live_owner": "tests/schemes/test_horikawa_k3_family.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/framework/test_composite_certificates.sage",
        "live_owner": "tests/schemes/test_horikawa_k3_family.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_branch_section_action_computes_the_source_specified_13_plus_12_split() -> None:
    family = HorikawaK3Family()
    sections = family.branch_section_space()
    decomposition = family.branch_isotypic_decomposition()
    invariant = family.invariant_branch_sections()
    anti_invariant = family.anti_invariant_branch_sections()

    assert sections.module_rank() == 25
    assert decomposition.trivial_component() is invariant
    assert invariant.module_rank() == 13
    assert anti_invariant.module_rank() == 12
    assert invariant.inclusion().codomain() is sections
    assert anti_invariant.inclusion().codomain() is sections

    group = family.branch_linearization().acting_group()
    generator = next(iter(group.group_generators()))
    invariant_label = next(iter(invariant.module_generating_set()))
    anti_invariant_label = next(iter(anti_invariant.module_generating_set()))
    invariant_section = invariant.inclusion()(invariant.module_generator(invariant_label))
    anti_invariant_section = anti_invariant.inclusion()(
        anti_invariant.module_generator(anti_invariant_label)
    )
    section_action = family.branch_linearization().section_action_of(generator)
    assert section_action(invariant_section) == invariant_section
    assert section_action(anti_invariant_section) == -anti_invariant_section

    branch = family.default_branch_section()
    trivial = lambda _element: QQ.one()
    assert family.branch_linearization().is_eigensection(branch, trivial)


def test_selected_invariant_branch_builds_a_smooth_anticanonical_double_cover() -> None:
    member = HorikawaK3Family().member()
    cyclic = member.cyclic_algebra()
    cover = member.scheme()
    projection = member.cover_morphism()

    assert cyclic.degree() == 2
    assert cyclic.line_bundle() is member.family().cover_line_bundle()
    assert projection.domain() is cover
    assert projection.codomain() is member.base_surface()
    assert member.branch_is_smooth()
    assert member.branch_avoids_tau_fixed_corners()
    assert member.cover_line_bundle_is_anticanonical()
    assert member.k3_theorem_hypotheses_hold()
    assert member.is_k3()

    # The canonical deck group scheme remains mu_2; the constant C2 map is an
    # additional choice available over QQ rather than a replacement for it.
    first_chart = next(iter(cyclic.chart_index_set()))
    mu_two_action = cyclic.local_deck_group_scheme_action(first_chart)
    mu_two_algebra = mu_two_action.group_scheme().scheme().coordinate_algebra()
    u = mu_two_algebra.algebra_generator("u")
    assert u**2 == mu_two_algebra.one()
    assert cyclic.constant_deck_transformation().domain() is cover


def test_two_tau_lifts_are_involutions_with_actual_fixed_subschemes_and_top_form_actions() -> None:
    member = HorikawaK3Family().member()
    enriques = member.enriques_lift()
    nikulin = member.nikulin_lift()
    enriques_fixed, nikulin_fixed = member.fixed_subschemes()

    assert member.both_lifts_have_order_two()
    assert enriques.automorphism().domain() is member.scheme()
    assert nikulin.automorphism().domain() is member.scheme()
    assert enriques.base_automorphism() is nikulin.base_automorphism()
    assert enriques_fixed.inclusion().codomain() is member.scheme()
    assert nikulin_fixed.inclusion().codomain() is member.scheme()
    assert member.enriques_lift_is_fixed_point_free()
    assert all(
        not nikulin.local_automorphism(index).fixed_subscheme().is_empty()
        for index in member.cyclic_algebra().chart_index_set()
    )

    assert member.deck_top_form_scalar() == -QQ.one()
    assert enriques.top_form_scalar() == -QQ.one()
    assert nikulin.top_form_scalar() == QQ.one()


def test_cover_and_all_three_involutions_commute_with_nontrivial_scalar_base_change() -> None:
    member = HorikawaK3Family().member()
    field = QuadraticField(2, "s")
    extension = QQ.Mor(field)(lambda element: field(element))
    comparison = member.base_change(extension)

    assert comparison.cover_projection().domain() is comparison.changed_scheme()
    assert comparison.cover_projection().codomain() is member.scheme()
    assert comparison.base_projection().codomain() is member.base_surface()
    assert comparison.cover_square_commutes()
    assert comparison.involutions_commute_with_base_change()
    assert comparison.changed_nikulin_lift().top_form_scalar() == field.one()
    assert comparison.changed_enriques_lift().top_form_scalar() == -field.one()


def test_branch_linear_system_and_double_cover_form_one_composite_construction() -> None:
    family = HorikawaK3Family()
    member = family.member()
    branch_bundle = family.branch_line_bundle()
    sections = branch_bundle.global_sections()
    system = branch_bundle.linear_system()
    cover = member.cover_morphism()

    assert sections.module_rank() == 25
    assert system.line_bundle() is branch_bundle
    assert system.is_basepoint_free()
    assert system.associated_morphism().domain() is family.base_surface()
    assert member.cyclic_algebra().degree() == 2
    assert member.cyclic_algebra().branch_power() is branch_bundle
    branch_local = member.cyclic_algebra().branch_section().parent()
    assert branch_local.gluing_datum().line_bundle() is branch_bundle
    assert "_preamble_line_bundle" not in branch_local.__dict__
    assert cover.domain() is member.scheme()
    assert cover.codomain() is family.base_surface()
    assert member.scheme().relative_dimension() == family.base_surface().relative_dimension()

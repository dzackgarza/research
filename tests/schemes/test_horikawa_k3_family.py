r"""The Horikawa ``(4,4)`` family is built from the shared equivariant cover owners."""

from dzack_research.preamble.all import QQ, QuadraticField, Schemes
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
    assert member.scheme() is member
    assert member in Schemes(QQ)
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
    assert enriques.automorphism() is enriques.left()
    assert enriques.base_automorphism() is enriques.right()
    assert enriques.domain() is enriques.codomain()
    assert enriques.domain().arrow() is member.cover_morphism()
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
    cyclic_square = comparison.cyclic_cover_comparison()

    assert cyclic_square.projection() is cyclic_square.left()
    assert cyclic_square.base_projection() is cyclic_square.right()
    assert cyclic_square.domain().arrow() is cyclic_square.changed_cyclic_algebra().relative_spectrum().arrow()
    assert cyclic_square.codomain().arrow() is member.cyclic_algebra().relative_spectrum().arrow()
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


def test_cyclic_cover_base_change_uses_the_section_after_addition() -> None:
    from dzack_research.preamble.categories.algebras.cyclic_cover_algebras import CyclicCoverAlgebra

    family = HorikawaK3Family()
    power = family.branch_line_bundle()
    local_branch = power.compatible_section(family.default_branch_section())
    # Addition used to discard the hidden homogeneous-source attribute and
    # make scalar change refuse this very same mathematical section.
    branch = local_branch + local_branch.parent().zero()
    cyclic = CyclicCoverAlgebra(family.cover_line_bundle(), branch, 2)
    field = QuadraticField(2, "s")
    extension = QQ.Mor(field)(field)
    comparison = cyclic.base_change(extension)
    changed = comparison.changed_cyclic_algebra()
    assert comparison.cover_square_commutes()
    assert comparison.projection().codomain() is cyclic.relative_spectrum().arrow().domain()
    for index in cyclic.chart_index_set():
        local_projection = comparison.local_projection(index)
        pullback = local_projection.coordinate_algebra_morphism()
        source_algebra = cyclic.local_algebra(index)
        target_algebra = changed.local_algebra(index)
        source_branch = source_algebra.algebra_structure_morphism()(
            cyclic.local_branch_coefficient(index)
        )
        target_branch = target_algebra.algebra_structure_morphism()(
            changed.local_branch_coefficient(index)
        )
        assert pullback(source_branch) == target_branch

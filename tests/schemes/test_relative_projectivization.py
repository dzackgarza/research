r"""Relative projectivization uses Sym(F), not a locally-free rank shortcut."""

from dzack_research.preamble.all import (
    NN,
    ProjectiveSpaces,
    QQ,
    RelativeProjectivizations,
)
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasModuleGluingData,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    QuasiCoherentSheaves,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_nonfree_affine_sheaf_projectivization_retains_the_linear_relation() -> None:
    base = QQ.polynomial_ring("x")
    x = base.algebra_generator("x")
    scheme = base.affine_spectrum()
    relations = base.free_module(finite_ordered_set(("r",)))
    generators = base.free_module(finite_ordered_set(("u", "v")))
    module = relations.module_category().Mor(relations, generators)(
        {"r": generators.scalar_multiple(x, generators.module_generator("u"))}
    ).cokernel()
    sheaf = scheme.associated_module_sheaf(module)

    projectivization = sheaf.projectivization()
    total = projectivization.arrow().domain()
    atlas = total.finite_affine_atlas()

    assert projectivization.arrow().codomain() is scheme
    assert total in RelativeProjectivizations(total.scheme_base_ring())
    assert total.projectivization_source_sheaf() is sheaf
    assert total.symmetric_algebra() is module.symmetric_algebra()
    assert atlas.chart_index_set() == module.module_generating_set()

    u_chart = atlas.chart("u").coordinate_algebra()
    v_chart = atlas.chart("v").coordinate_algebra()
    assert u_chart.algebra_structure_morphism()(x) == u_chart.zero()
    assert v_chart.algebra_structure_morphism()(x) * v_chart.algebra_generator(
        "p0_over_p1"
    ) == v_chart.zero()

    line = total.tautological_line_bundle()
    pulled = total.pulled_source_sheaf()
    quotient = total.universal_quotient()
    assert line.scheme() is total
    assert quotient.domain() is pulled
    assert quotient.codomain() is line.module_sheaf()

    u_source = pulled.gluing_datum().local_module("u")
    u_target = line.module_sheaf().gluing_datum().local_module("u")
    u_basis = u_target.module_generator(next(iter(u_target.module_generating_set())))
    assert quotient.local_map("u")(u_source.module_generator("u")) == u_basis
    assert quotient.local_map("u").is_surjective()

    closed_fiber = base.quotient_ring(base.ideal(x))
    closed_comparison = sheaf.projectivization_base_change(
        closed_fiber.quotient_map()
    )
    closed_total = closed_comparison.changed_projectivization().arrow().domain()
    closed_atlas = closed_total.finite_affine_atlas()
    assert closed_comparison.projection_to_original().domain() is closed_total
    assert closed_comparison.projection_to_original().codomain() is total
    assert closed_comparison.projection_to_changed_base().codomain() is (
        closed_comparison.changed_source_sheaf().scheme()
    )
    assert closed_atlas.chart("u").coordinate_algebra().algebra_generating_set().cardinality() == 1
    assert closed_atlas.chart("v").coordinate_algebra().algebra_generating_set().cardinality() == 1

    away_from_x = base.localization(x)
    open_comparison = sheaf.projectivization_base_change(
        away_from_x.localization_map()
    )
    open_total = open_comparison.changed_projectivization().arrow().domain()
    open_atlas = open_total.finite_affine_atlas()
    assert open_comparison.projection_to_original().domain() is open_total
    assert open_atlas.chart("u").coordinate_algebra().one() == open_atlas.chart(
        "u"
    ).coordinate_algebra().zero()
    assert open_atlas.chart("v").coordinate_algebra().algebra_generator(
        "p0_over_p1"
    ) == open_atlas.chart("v").coordinate_algebra().zero()
    assert open_comparison.universal_quotient().codomain().scheme() is open_total


def test_free_rank_two_projectivization_has_the_standard_ratio_charts() -> None:
    module = QQ.free_module(finite_ordered_set(("s", "t")))
    scheme = QQ.affine_spectrum()
    sheaf = scheme.associated_module_sheaf(module)
    total = sheaf.projectivization().arrow().domain()
    atlas = total.finite_affine_atlas()

    assert "p1_over_p0" in tuple(
        str(label) for label in atlas.chart("s").coordinate_algebra().algebra_generating_set()
    )
    assert "p0_over_p1" in tuple(
        str(label) for label in atlas.chart("t").coordinate_algebra().algebra_generating_set()
    )
    transition = atlas.transition_between("s", "t").forward()
    source_ratio = atlas.overlap("s", "t").inclusion().coordinate_algebra_morphism()(
        atlas.chart("s").coordinate_algebra().algebra_generator("p1_over_p0")
    )
    target_ratio = atlas.overlap("t", "s").inclusion().coordinate_algebra_morphism()(
        atlas.chart("t").coordinate_algebra().algebra_generator("p0_over_p1")
    )
    assert transition.coordinate_algebra_morphism()(target_ratio) == source_ratio.inverse_of_unit()

    standard = ProjectiveSpaces(QQ)(1)
    comparison = total.projective_space_comparison(standard)
    assert comparison.forward().domain() is total
    assert comparison.forward().codomain() is standard
    assert comparison.inverse().domain() is standard
    assert comparison.inverse().codomain() is total


def test_zero_module_projectivization_is_empty_over_the_same_base() -> None:
    scheme = QQ.affine_spectrum()
    module = QQ.free_module(finite_ordered_set(()))
    total = scheme.associated_module_sheaf(module).projectivization().arrow().domain()
    atlas = total.finite_affine_atlas()

    assert atlas.number_of_charts() == 1
    assert atlas.chart("empty").coordinate_algebra().one() == atlas.chart(
        "empty"
    ).coordinate_algebra().zero()


def test_countable_free_sheaf_projectivization_retains_the_exact_unmaterialized_object() -> None:
    scheme = QQ.affine_spectrum()
    module = QQ.free_module(NN)
    sheaf = scheme.associated_module_sheaf(module)
    projectivization = sheaf.projectivization()
    total = projectivization.arrow().domain()
    quotient = total.universal_quotient()

    assert total in RelativeProjectivizations(QQ)
    assert projectivization.arrow() is total.projectivization_projection()
    assert projectivization.arrow().codomain() is scheme
    assert total.projectivization_source_sheaf() is sheaf
    assert total.symmetric_algebra() is module.symmetric_algebra()
    assert quotient.domain() is total.pulled_source_sheaf()
    assert quotient.codomain() is total.tautological_line_bundle().module_sheaf()
    assert quotient.is_surjective()

    extension = QQ.polynomial_ring("t")
    comparison = sheaf.projectivization_base_change(
        extension.algebra_structure_morphism()
    )
    changed_total = comparison.changed_projectivization().arrow().domain()
    assert comparison.changed_source_sheaf().pullback_morphism() is (
        comparison.underlying_base_projection()
    )
    assert comparison.total_projection().domain() is changed_total
    assert comparison.total_projection().codomain() is total
    assert comparison.base_projection().codomain() is conic
    assert comparison.universal_quotient().codomain().scheme() is changed_total

    extension = QQ.polynomial_ring("t")
    comparison = sheaf.projectivization_base_change(
        extension.algebra_structure_morphism()
    )
    changed_total = comparison.changed_projectivization().arrow().domain()
    assert changed_total in RelativeProjectivizations(QQ)
    assert comparison.projection_to_original().domain() is changed_total
    assert comparison.projection_to_original().codomain() is total
    assert comparison.base_morphism().codomain() is scheme
    assert comparison.universal_quotient().is_surjective()


def test_countable_free_sheaf_map_retains_its_exact_projectivization_domain() -> None:
    scheme = QQ.affine_spectrum()
    module = QQ.free_module(NN)
    sheaf = scheme.associated_module_sheaf(module)
    module_map = module.module_category().Mor(module, module).identity()
    sheaf_map = QuasiCoherentSheaves(scheme).Mor(sheaf, sheaf)(module_map)
    total = sheaf.projectivization().arrow().domain()
    projectivized = sheaf_map.projectivization_map()

    assert total in RelativeProjectivizations(QQ)
    assert projectivized.open_immersion().codomain() is total
    assert projectivized.morphism().domain() is projectivized.domain_of_definition()
    assert projectivized.morphism().codomain() is total


def test_nonaffine_represented_sheaf_without_selected_atlas_keeps_exact_projectivization() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    x, y, z = plane.homogeneous_coordinate_generators()
    conic = plane.closed_subscheme(x * z - y**2)
    sheaf = plane.O(1).restrict_to(conic)
    projectivization = sheaf.projectivization()
    total = projectivization.arrow().domain()
    quotient = total.universal_quotient()

    assert total in RelativeProjectivizations(QQ)
    assert not total.has_selected_finite_affine_atlas()
    try:
        total.selected_finite_affine_atlas()
    except TypeError:
        pass
    else:
        raise AssertionError("this exact projectivization must not acquire an unrelated finite atlas")
    assert projectivization.arrow().codomain() is conic
    assert total.projectivization_source_sheaf() is sheaf
    assert quotient.domain() is total.pulled_source_sheaf()
    assert quotient.codomain() is total.tautological_line_bundle().module_sheaf()
    assert quotient.is_surjective()


def test_projectivization_map_is_available_on_finite_atlas_line_bundle_morphisms() -> None:
    line = ProjectiveSpaces(QQ)(1)
    bundle = line.O(1)
    morphism = QuasiCoherentSheaves(line).Mor(bundle, bundle).identity()
    projectivized = morphism.projectivization_map()

    assert projectivized.source_projectivization().has_selected_finite_affine_atlas()
    assert projectivized.target_projectivization().has_selected_finite_affine_atlas()
    assert projectivized.source_projectivization() is bundle.projectivization().arrow().domain()
    assert projectivized.target_projectivization() is bundle.projectivization().arrow().domain()
    assert projectivized.open_immersion().codomain() is projectivized.target_projectivization()
    assert projectivized.morphism().codomain() is projectivized.source_projectivization()


def test_projectivization_map_is_available_on_exact_pullback_line_bundle_morphisms() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    x, y, z = plane.homogeneous_coordinate_generators()
    conic = plane.closed_subscheme(x * z - y**2)
    left = plane.O(1).restrict_to(conic)
    right = plane.O(1).restrict_to(conic)
    morphism = left.canonical_isomorphism_to(right).forward()
    projectivized = morphism.projectivization_map()

    assert projectivized.source_projectivization() is left.projectivization().arrow().domain()
    assert projectivized.target_projectivization() is right.projectivization().arrow().domain()
    assert projectivized.open_immersion().codomain() is projectivized.target_projectivization()
    assert projectivized.morphism().codomain() is projectivized.source_projectivization()


def test_rank_two_bundle_projectivization_uses_the_nonconstant_module_transition() -> None:
    line = ProjectiveSpaces(QQ)(1)
    atlas = line.standard_affine_atlas()
    local_modules = {
        index: atlas.chart(index).coordinate_algebra().free_module(
            finite_ordered_set(("e0", "e1"))
        )
        for index in atlas.chart_indices()
    }
    source_overlap = atlas.overlap(0, 1)
    target_overlap = atlas.overlap(1, 0)
    source_coordinate = atlas.chart(0).coordinate_algebra().algebra_generator(
        "x1_over_x0"
    )
    unit = source_overlap.inclusion().coordinate_algebra_morphism()(source_coordinate)
    reverse_scalar = atlas.transition_between(0, 1).inverse().coordinate_algebra_morphism()
    reverse_unit = reverse_scalar(unit.inverse_of_unit())

    def forward(label, _domain, codomain):
        scalar = unit if label == "e0" else codomain.base_ring().one()
        return codomain.scalar_multiple(scalar, codomain.module_generator(label))

    def inverse(label, _domain, codomain):
        scalar = reverse_unit if label == "e0" else codomain.base_ring().one()
        return codomain.scalar_multiple(scalar, codomain.module_generator(label))

    descent = FiniteAtlasModuleGluingData(atlas)(
        local_modules,
        {(0, 1): (forward, inverse)},
    )
    sheaf = descent.sheaf()
    total = sheaf.projectivization().arrow().domain()
    projective_atlas = total.finite_affine_atlas()
    source_key = (0, "e0")
    target_key = (1, "e0")
    transition = projective_atlas.transition_between(source_key, target_key).forward()
    projective_source_overlap = projective_atlas.overlap(source_key, target_key)
    projective_target_overlap = projective_atlas.overlap(target_key, source_key)
    source_chart = projective_atlas.chart(source_key)
    target_chart = projective_atlas.chart(target_key)
    source_ratio = projective_source_overlap.inclusion().coordinate_algebra_morphism()(
        source_chart.coordinate_algebra().algebra_generator("p1_over_p0")
    )
    target_ratio = projective_target_overlap.inclusion().coordinate_algebra_morphism()(
        target_chart.coordinate_algebra().algebra_generator("p1_over_p0")
    )
    pair_to_projective = descent.pair_module(0, 1).base_ring().induced_morphism(
        projective_source_overlap.inclusion().coordinate_algebra_morphism()
        * source_chart.coordinate_algebra().algebra_structure_morphism()
    )

    assert sheaf.projectivization().arrow().codomain() is line
    assert total in RelativeProjectivizations(QQ)
    assert transition.coordinate_algebra_morphism()(target_ratio) == (
        source_ratio * pair_to_projective(unit).inverse_of_unit()
    )

    symmetric = total.symmetric_algebra()
    symmetric_transition = symmetric.transition(0, 1).pullback()
    target_symmetric = symmetric.pair_algebra(1, 0)
    source_symmetric = symmetric.pair_algebra(0, 1)
    assert symmetric_transition(target_symmetric.algebra_generator("e0")) == (
        source_symmetric.scalar_multiple(
            unit,
            source_symmetric.algebra_generator("e0"),
        )
    )

    tautological = total.tautological_line_bundle()
    assert tautological.transition_unit(source_key, target_key) == pair_to_projective(unit)
    quotient = total.universal_quotient()
    assert quotient.local_map(source_key).is_surjective()


def test_trivial_rank_two_bundle_projectivization_is_the_relative_projective_line() -> None:
    line = ProjectiveSpaces(QQ)(1)
    atlas = line.standard_affine_atlas()
    local_modules = {
        index: atlas.chart(index).coordinate_algebra().free_module(
            finite_ordered_set(("e0", "e1"))
        )
        for index in atlas.chart_indices()
    }

    def identity_transition(label, _domain, codomain):
        return codomain.module_generator(label)

    descent = FiniteAtlasModuleGluingData(atlas)(
        local_modules,
        {(0, 1): (identity_transition, identity_transition)},
    )
    total = descent.sheaf().projectivization().arrow().domain()
    comparison = total.relative_projective_space_comparison()
    relative_space = comparison.forward().codomain()

    assert comparison.forward().domain() is total
    assert comparison.inverse().domain() is relative_space
    assert comparison.inverse().codomain() is total
    assert relative_space.factors()[0] is line
    assert relative_space.factors()[1] in ProjectiveSpaces(QQ)
    assert relative_space.factors()[1].relative_dimension() == 1
    assert relative_space.projection(0) * comparison.forward() == (
        total.projectivization_projection()
    )


def test_finite_atlas_projectivization_retains_scalar_base_change_and_universal_quotient() -> None:
    line = ProjectiveSpaces(QQ)(1)
    atlas = line.standard_affine_atlas()
    local_modules = {
        index: atlas.chart(index).coordinate_algebra().free_module(
            finite_ordered_set(("e0", "e1"))
        )
        for index in atlas.chart_indices()
    }

    def identity_transition(label, _domain, codomain):
        return codomain.module_generator(label)

    descent = FiniteAtlasModuleGluingData(atlas)(
        local_modules,
        {(0, 1): (identity_transition, identity_transition)},
    )
    sheaf = descent.sheaf()
    total = sheaf.projectivization().arrow().domain()
    extension = QQ.polynomial_ring("t")
    comparison = sheaf.projectivization_base_change(
        extension.algebra_structure_morphism()
    )
    changed = comparison.changed_projectivization().arrow().domain()

    assert comparison.total_projection().domain() is changed
    assert comparison.total_projection().codomain() is total
    assert comparison.base_projection().domain() is comparison.changed_base_scheme()
    assert comparison.projection_to_changed_base().domain() is changed
    assert comparison.universal_quotient().codomain().scheme() is changed
    assert comparison.changed_module_datum().gluing_datum() is comparison.changed_atlas()


def test_finite_atlas_projectivization_base_change_accepts_a_glued_base_scheme() -> None:
    projective_line = ProjectiveSpaces(QQ)(1)
    glued_line = projective_line.glued_from_standard_charts()
    atlas = glued_line.finite_affine_atlas()
    local_modules = {
        index: atlas.chart(index).coordinate_algebra().free_module(
            finite_ordered_set(("e0", "e1"))
        )
        for index in atlas.chart_indices()
    }

    def identity_transition(label, _domain, codomain):
        return codomain.module_generator(label)

    descent = FiniteAtlasModuleGluingData(atlas)(
        local_modules,
        {(0, 1): (identity_transition, identity_transition)},
    )
    sheaf = descent.sheaf()
    extension = QQ.polynomial_ring("t")
    comparison = sheaf.projectivization_base_change(
        extension.algebra_structure_morphism()
    )
    changed_base = comparison.changed_base_scheme()

    assert changed_base._is_glued_from_affine_atlas()
    assert changed_base.left_projection().codomain() is glued_line
    assert changed_base.right_projection().codomain() is changed_base.base_scheme()
    assert comparison.changed_atlas().scheme() is changed_base
    assert comparison.base_projection() == changed_base.left_projection()
    assert comparison.total_projection().codomain() is (
        sheaf.projectivization().arrow().domain()
    )


def test_sheaf_map_projectivization_is_defined_exactly_on_the_surjective_quotient_locus() -> None:
    base = QQ.polynomial_ring("x")
    x = base.algebra_generator("x")
    scheme = base.affine_spectrum()
    source_module = base.free_module(finite_ordered_set(("s",)))
    target_module = base.free_module(finite_ordered_set(("g",)))
    source = scheme.associated_module_sheaf(source_module)
    target = scheme.associated_module_sheaf(target_module)
    module_map = source_module.module_category().Mor(source_module, target_module)(
        {
            "s": target_module.scalar_multiple(
                x,
                target_module.module_generator("g"),
            )
        }
    )
    sheaf_map = QuasiCoherentSheaves(scheme).Mor(source, target)(module_map)
    projectivized = sheaf_map.projectivization_map()
    locus = projectivized.domain_of_definition()
    target_total = target.projectivization().arrow().domain()
    source_total = source.projectivization().arrow().domain()
    fine_index = ("g", "s")
    local_open = locus.gluing_datum().chart(fine_index)
    restricted_x = local_open.inclusion().coordinate_algebra_morphism()(
        local_open.inclusion().codomain().coordinate_algebra().algebra_structure_morphism()(x)
    )

    assert projectivized.open_immersion().codomain() is target_total
    assert projectivized.morphism().domain() is locus
    assert projectivized.morphism().codomain() is source_total
    assert restricted_x.is_unit()


def test_zero_source_sheaf_projectivization_map_has_empty_surjectivity_locus() -> None:
    scheme = QQ.affine_spectrum()
    source_module = QQ.free_module(finite_ordered_set(()))
    target_module = QQ.free_module(finite_ordered_set(("g",)))
    source = scheme.associated_module_sheaf(source_module)
    target = scheme.associated_module_sheaf(target_module)
    module_map = source_module.module_category().Mor(source_module, target_module)({})
    sheaf_map = QuasiCoherentSheaves(scheme).Mor(source, target)(module_map)
    projectivized = sheaf_map.projectivization_map()
    locus = projectivized.domain_of_definition()
    local_empty = locus.gluing_datum().chart("g")

    assert projectivized.open_immersion().codomain() is (
        target.projectivization().arrow().domain()
    )
    assert projectivized.morphism().codomain() is (
        source.projectivization().arrow().domain()
    )
    assert local_empty.coordinate_algebra().one() == local_empty.coordinate_algebra().zero()


def test_zero_target_sheaf_projectivization_map_is_the_unique_map_from_the_empty_domain() -> None:
    scheme = QQ.affine_spectrum()
    source_module = QQ.free_module(finite_ordered_set(("s",)))
    target_module = QQ.free_module(finite_ordered_set(()))
    source = scheme.associated_module_sheaf(source_module)
    target = scheme.associated_module_sheaf(target_module)
    module_map = source_module.module_category().Mor(source_module, target_module)(
        {"s": target_module.zero()}
    )
    sheaf_map = QuasiCoherentSheaves(scheme).Mor(source, target)(module_map)
    projectivized = sheaf_map.projectivization_map()
    locus = projectivized.domain_of_definition()
    local_empty = next(iter(locus.gluing_datum().charts()))

    assert projectivized.open_immersion().codomain() is (
        target.projectivization().arrow().domain()
    )
    assert projectivized.morphism().codomain() is (
        source.projectivization().arrow().domain()
    )
    assert local_empty.coordinate_algebra().one() == local_empty.coordinate_algebra().zero()

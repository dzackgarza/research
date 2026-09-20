r"""Relative projectivization uses Sym(F), not a locally-free rank shortcut."""

from dzack_research.preamble.all import QQ
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


def test_zero_module_projectivization_is_empty_over_the_same_base() -> None:
    scheme = QQ.affine_spectrum()
    module = QQ.free_module(finite_ordered_set(()))
    total = scheme.associated_module_sheaf(module).projectivization().arrow().domain()
    atlas = total.finite_affine_atlas()

    assert atlas.number_of_charts() == 1
    assert atlas.chart("empty").coordinate_algebra().one() == atlas.chart(
        "empty"
    ).coordinate_algebra().zero()

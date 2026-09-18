from dzack_research.preamble.all import QQ, ProjectiveSpaces, Schemes
from dzack_research.preamble.categories.divisors.invertible_sheaves import (
    FiniteAtlasInvertibleSheaf,
)
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasModuleGluingDatum,
    FiniteAtlasRefinement,
)


def _projective_line_refinement():
    line = ProjectiveSpaces(QQ)(1)
    coarse = line.glued_from_standard_charts().gluing_datum()
    left = coarse.chart(0)
    right = coarse.chart(1)
    overlap = coarse.overlap(0, 1)
    whole_overlap = overlap.distinguished_open(overlap.coordinate_algebra().one())
    left_forward = whole_overlap.corestriction(overlap.categorical_identity_morphism())
    left_inverse = whole_overlap.inclusion()
    left_to_overlap = Schemes(QQ).Core().Mor(
        left_forward.domain(), left_forward.codomain()
    )(left_forward, left_inverse)
    right_forward = whole_overlap.corestriction(
        coarse.transition_between(1, 0).forward()
    )
    right_inverse = coarse.transition_between(0, 1).forward() * whole_overlap.inclusion()
    right_to_overlap = Schemes(QQ).Core().Mor(
        right_forward.domain(), right_forward.codomain()
    )(right_forward, right_inverse)
    fine = Schemes(QQ).glue_affine_atlas(
        (left, right, overlap),
        (
            coarse.transition_between(0, 1),
            left_to_overlap,
            right_to_overlap,
        ),
    ).gluing_datum()
    refinement = FiniteAtlasRefinement(
        coarse,
        fine,
        (0, 1, 0),
        (
            left.categorical_identity_morphism(),
            right.categorical_identity_morphism(),
            overlap.inclusion(),
        ),
    )
    return coarse, fine, refinement


def _identity_transition(label, domain, codomain):
    position = int(domain.module_generating_set().ranking_map()(label))
    target_label = codomain.module_generating_set()[position]
    return codomain.module_generator(target_label)


def _rank_one_sheaf(datum):
    local_modules = {
        index: datum.chart(index).coordinate_algebra().free_module(1)
        for index in datum.chart_indices()
    }
    transitions = {
        pair: (_identity_transition, _identity_transition)
        for pair in datum.transition_index_set()
    }
    return FiniteAtlasModuleGluingDatum(datum, local_modules, transitions).sheaf()


def _scalar_morphism(source, target, scalar):
    local_maps = {}
    datum = source.atlas_datum()
    for index in datum.chart_indices():
        domain = source.sections_on_chart(index)
        codomain = target.sections_on_chart(index)
        source_label = domain.module_generating_set()[0]
        target_label = codomain.module_generating_set()[0]
        local_maps[index] = domain.module_category().Mor(domain, codomain)(
            {
                source_label: codomain.scalar_multiple(
                    codomain.base_ring()(scalar),
                    codomain.module_generator(target_label),
                )
            }
        )
    return source.morphism_to(target, local_maps)


def test_inverse_image_and_module_pullback_keep_the_structural_map_distinct() -> None:
    coarse, fine, refinement = _projective_line_refinement()
    source = _rank_one_sheaf(coarse)
    inverse_image_functor = refinement.inverse_image_functor()
    scalar_extension = refinement.inverse_image_scalar_extension_functor()
    pullback = refinement.module_pullback_functor()
    inverse_image = inverse_image_functor(source)
    pulled = inverse_image.module_pullback()

    assert pullback.factors() == (inverse_image_functor, scalar_extension)
    assert inverse_image.category() is inverse_image_functor.codomain()
    assert pulled is scalar_extension(inverse_image)
    assert pulled is pullback(source)
    assert inverse_image.scheme_morphism() is refinement.comparison_morphism()
    assert inverse_image.scheme() is fine.scheme()
    for fine_index in fine.chart_indices():
        coarse_index = refinement.coarse_index(fine_index)
        assert inverse_image.source_local_module(fine_index) is source.sections_on_chart(
            coarse_index
        )
        assert inverse_image.structural_ring_map(fine_index) == refinement.chart_map(
            fine_index
        ).coordinate_algebra_morphism()
        assert pulled.sections_on_chart(fine_index).base_ring() is fine.chart(
            fine_index
        ).coordinate_algebra()
        assert pulled.sections_on_chart(fine_index) is not inverse_image.source_local_module(
            fine_index
        )


def test_module_pullback_preserves_nonidentity_maps_identity_and_composition() -> None:
    coarse, fine, refinement = _projective_line_refinement()
    source = _rank_one_sheaf(coarse)
    middle = _rank_one_sheaf(coarse)
    target = _rank_one_sheaf(coarse)
    times_two = _scalar_morphism(source, middle, 2)
    times_three = _scalar_morphism(middle, target, 3)
    composite = times_three * times_two
    pullback = refinement.module_pullback_functor()

    pulled_two = pullback.on_morphism(times_two)
    pulled_three = pullback.on_morphism(times_three)
    pulled_composite = pullback.on_morphism(composite)
    assert pulled_three * pulled_two == pulled_composite

    identity = source.gluing_datum().identity_morphism()
    pulled_identity = pullback.on_morphism(identity)
    assert pulled_identity == pullback.on_object(source).gluing_datum().identity_morphism()

    for fine_index in fine.chart_indices():
        module = pulled_composite.domain().gluing_datum().local_module(fine_index)
        label = module.module_generating_set()[0]
        image = pulled_composite.local_map(fine_index)(module.module_generator(label))
        codomain = pulled_composite.codomain().gluing_datum().local_module(fine_index)
        target_label = codomain.module_generating_set()[0]
        assert image == codomain.scalar_multiple(
            codomain.base_ring()(6), codomain.module_generator(target_label)
        )


def test_inverse_image_functor_preserves_composition_before_scalar_extension() -> None:
    coarse, _fine, refinement = _projective_line_refinement()
    source = _rank_one_sheaf(coarse)
    middle = _rank_one_sheaf(coarse)
    target = _rank_one_sheaf(coarse)
    times_two = _scalar_morphism(source, middle, 2)
    times_three = _scalar_morphism(middle, target, 3)
    inverse_image = refinement.inverse_image_functor()

    inverse_two = inverse_image(times_two)
    inverse_three = inverse_image(times_three)
    inverse_composite = inverse_image(times_three * times_two)
    composed = inverse_three * inverse_two

    assert inverse_two.parent() is inverse_image.codomain().Mor(
        inverse_two.domain(),
        inverse_two.codomain(),
    )
    for fine_index in refinement.fine_datum().chart_indices():
        assert composed.local_map(fine_index) == inverse_composite.local_map(fine_index)


def test_generic_module_pullback_agrees_with_transition_unit_line_bundle_pullback() -> None:
    coarse, fine, refinement = _projective_line_refinement()
    source_overlap = coarse.overlap(0, 1)
    ratio = source_overlap.inclusion().coordinate_algebra_morphism()(
        coarse.chart(0).coordinate_algebra().algebra_generator("x1_over_x0")
    )
    bundle = FiniteAtlasInvertibleSheaf(coarse, {(0, 1): ratio})
    comparison = refinement.compare_line_bundle_pullback(bundle)
    generic = comparison.generic_pullback().gluing_datum()
    specialized = comparison.specialized_module_sheaf().gluing_datum()

    assert comparison.line_bundle() is bundle
    assert comparison.line_bundle_refinement().refined_bundle().gluing_datum() is fine
    assert comparison.inverse() * comparison.forward() == generic.identity_morphism()
    assert comparison.forward() * comparison.inverse() == specialized.identity_morphism()

    for fine_index in fine.chart_indices():
        forward = comparison.forward().local_map(fine_index)
        assert forward.domain() is generic.local_module(fine_index)
        assert forward.codomain() is specialized.local_module(fine_index)

    refined_bundle = comparison.line_bundle_refinement().refined_bundle()
    assert refined_bundle.transition_unit(0, 1) == refinement.overlap_map(
        0, 1
    ).coordinate_algebra_morphism()(bundle.transition_unit(0, 1))


def _cusp_parametrization():
    from dzack_research.preamble.all import AffineSpaces, Algebras

    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    algebra = plane.coordinate_ring()
    algebra.algebra_generator("x")
    algebra.algebra_generator("y")
    line_ring = QQ.polynomial_ring("t")
    t = line_ring.algebra_generator("t")
    morphism = Algebras(QQ).Associative().Unital().Commutative().spectrum()(
        algebra.Mor(line_ring)({"x": t**2, "y": t**3})
    )
    return plane, morphism.domain(), morphism


def test_affine_quasi_coherent_pullback_and_direct_image_are_functorial() -> None:
    plane, line, morphism = _cusp_parametrization()
    pullback = morphism.module_pullback_functor()
    direct = morphism.direct_image_functor()

    assert pullback.functor_category().domain_category() is pullback.domain()
    assert pullback.functor_category().codomain_category() is pullback.codomain()
    assert direct.functor_category().domain_category() is direct.domain()
    assert direct.functor_category().codomain_category() is direct.codomain()

    target_module = plane.coordinate_algebra().free_module(1)
    target_sheaf = plane.associated_module_sheaf(target_module)
    target_label = target_module.module_generating_set()[0]
    times_two = target_module.module_category().Mor(target_module, target_module)(
        {
            target_label: target_module.scalar_multiple(
                plane.coordinate_algebra()(2),
                target_module.module_generator(target_label),
            )
        }
    )
    target_identity = target_module.module_category().Mor(target_module, target_module).identity()

    pulled = pullback.on_object(target_sheaf)
    assert pullback(target_sheaf) is pulled
    assert morphism.module_pullback(target_sheaf) is pulled
    pulled_two = pullback.on_morphism(times_two)
    pulled_identity = pullback.on_morphism(target_identity)
    assert pulled_two * pulled_identity == pulled_two
    assert pulled_identity * pulled_two == pulled_two

    source_module = line.coordinate_algebra().free_module(1)
    source_sheaf = line.associated_module_sheaf(source_module)
    source_label = source_module.module_generating_set()[0]
    times_three = source_module.module_category().Mor(source_module, source_module)(
        {
            source_label: source_module.scalar_multiple(
                line.coordinate_algebra()(3),
                source_module.module_generator(source_label),
            )
        }
    )
    source_identity = source_module.module_category().Mor(source_module, source_module).identity()

    pushed = direct.on_object(source_sheaf)
    assert morphism.direct_image(source_sheaf) is pushed
    pushed_three = direct.on_morphism(times_three)
    pushed_identity = direct.on_morphism(source_identity)
    assert pushed_three * pushed_identity == pushed_three
    assert pushed_identity * pushed_three == pushed_three


def test_affine_quasi_coherent_pullback_is_left_adjoint_to_direct_image() -> None:
    plane, line, morphism = _cusp_parametrization()
    adjunction = morphism.quasi_coherent_adjunction()

    target_module = plane.coordinate_algebra().free_module(1)
    target_sheaf = plane.associated_module_sheaf(target_module)
    pulled = adjunction.left_adjoint().on_object(target_sheaf)
    pushed_back = adjunction.right_adjoint().on_object(pulled)
    unit = adjunction.unit(target_sheaf)
    assert unit.domain() is target_module
    assert unit.codomain() is pushed_back.module()

    source_module = line.coordinate_algebra().free_module(1)
    source_sheaf = line.associated_module_sheaf(source_module)
    pushed = adjunction.right_adjoint().on_object(source_sheaf)
    pulled_back = adjunction.left_adjoint().on_object(pushed)
    counit = adjunction.counit(source_sheaf)
    assert counit.domain() is pulled_back.module()
    assert counit.codomain() is source_module

    source_label = source_module.module_generating_set()[0]
    source_generator = source_module.module_generator(source_label)
    assert counit(
        pulled_back.module_generator(
            pulled_back.module_generating_set()[0]
        )
    ) == source_generator

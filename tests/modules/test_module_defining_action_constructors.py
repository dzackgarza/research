r"""M0 constructor contracts for module actions and selected presentations.

These examples are committed unverified under the standing preamble policy.
They distinguish the chosen presentation from the underlying module while
requiring every constructor route to expose and use the same scalar-action
morphism ``R -> End_Ab(U(M))``.
"""

from dzack_research.preamble.all import (
    NN,
    QQ,
    ZZ,
    AdditiveGroups,
    FramedModules,
    GeneralModules,
    Modules,
    ModulesWithChosenFinitePresentation,
    Set,
)
from dzack_research.preamble.categories.modules.powers import (
    AlternatingPowerModules,
    DividedPowerModules,
    SymmetricPowerModules,
    TensorPowerModules,
)

from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic_six_from_presentation():
    target = ZZ.free_module(finite_ordered_set(("x",)))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    presentation = relations.module_category().Mor(relations, target)(
        {"r": target.scalar_multiple(ZZ(6), target.module_generator("x"))}
    )
    return presentation.cokernel()


def _cyclic_six_from_action():
    return GeneralModules(ZZ).from_operations(
        Set(list(range(6))),
        addition=lambda left, right: (left + right) % 6,
        zero=0,
        negation=lambda value: (-value) % 6,
        scalar_action=lambda scalar, value: (int(scalar) * value) % 6,
    )


def test_presented_and_direct_action_zmod6_have_an_explicit_intertwining_isomorphism() -> None:
    presented = _cyclic_six_from_presentation()
    acted = _cyclic_six_from_action()
    generator = presented.module_generator("x")

    forward = presented.module_category().Mor(presented, acted)(
        {"x": acted(1)}
    )
    inverse = acted.module_category().Mor(acted, presented).elementwise(
        lambda element: presented.scalar_multiple(
            ZZ(element.underlying_element()), generator
        ),
    )
    comparison = Modules(ZZ).Core().Mor(presented, acted)(forward, inverse)

    assert comparison.domain() is presented
    assert comparison.codomain() is acted
    for scalar in (ZZ(-2), ZZ(0), ZZ(5)):
        assert comparison(
            presented.scalar_multiple(scalar, generator)
        ) == acted.scalar_multiple(scalar, comparison(generator))
    assert presented.scalar_action()(ZZ(5))(generator) == presented.scalar_multiple(
        ZZ(5), generator
    )
    assert acted.scalar_action()(ZZ(5))(acted(1)) == acted.scalar_multiple(
        ZZ(5), acted(1)
    )


def test_free_plus_torsion_presentation_uses_its_exposed_scalar_action() -> None:
    target = ZZ.free_module(finite_ordered_set(("free", "torsion")))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    module = relations.module_category().Mor(relations, target)(
        {
            "r": target.scalar_multiple(
                ZZ(6), target.module_generator("torsion")
            )
        }
    ).cokernel()

    for label in module.module_generating_set():
        element = module.module_generator(label)
        assert module.scalar_action()(ZZ(3))(element) == module.scalar_multiple(
            ZZ(3), element
        )


def test_infinite_free_module_keeps_finite_support_and_the_same_action_morphism() -> None:
    module = ZZ.free_module(NN)
    element = module({NN(2): ZZ(3), NN(100): ZZ(-1)})

    assert module.scalar_action()(ZZ(4))(element) == module.scalar_multiple(
        ZZ(4), element
    )
    assert module.scalar_multiple(ZZ(4), element).monomial_coefficients() == {
        NN(2): ZZ(12),
        NN(100): ZZ(-4),
    }


def test_restriction_of_scalars_exposes_the_composed_action() -> None:
    extension = QQ.free_module(finite_ordered_set(("e",)))
    inclusion = ZZ.Mor(QQ)(QQ)
    restricted = extension.restrict_scalars(inclusion)
    element = restricted.wrap(extension.module_generator("e"))

    assert restricted.underlying_additive_group() is extension.underlying_additive_group()
    assert restricted.scalar_action().domain() is ZZ
    assert restricted.scalar_action().codomain() is extension.scalar_action().codomain()
    underlying = restricted._underlying_additive_element(element)
    assert restricted.scalar_action()(ZZ(7))(underlying) == (
        restricted.scalar_multiple(ZZ(7), element).underlying_element()
    )
    assert restricted.scalar_multiple(ZZ(7), element).underlying_element() == (
        extension.scalar_multiple(QQ(7), extension.module_generator("e"))
    )


def test_selected_presentations_are_arrow_objects_and_contractible_summands_remain_distinct() -> None:
    cyclic = _cyclic_six_from_presentation()
    category = ModulesWithChosenFinitePresentation(ZZ).presentation_category()
    selected = cyclic.presentation_object()

    assert selected in category
    assert selected.arrow() is cyclic.presentation()

    target = ZZ.free_module(finite_ordered_set(("x", "contractible")))
    relations = ZZ.free_module(finite_ordered_set(("r", "s")))
    stabilized = relations.module_category().Mor(relations, target)(
        {
            "r": target.scalar_multiple(ZZ(6), target.module_generator("x")),
            "s": target.module_generator("contractible"),
        }
    ).cokernel()

    assert stabilized.presentation_object() in category
    assert stabilized.presentation_object() is not selected
    assert stabilized.presentation().domain().module_generating_set().cardinality() == 2
    assert cyclic.presentation().domain().module_generating_set().cardinality() == 1

    normalization = stabilized.invariant_factor_presentation()
    assert normalization.forward() in category.Mor(
        stabilized.presentation_object(), normalization.codomain()
    )


def test_selected_framings_are_arrow_objects_with_commuting_square_morphisms() -> None:
    source = ZZ.free_module(finite_ordered_set(("x", "y")))
    target = ZZ.free_module(finite_ordered_set(("u", "v")))
    category = FramedModules(ZZ).framing_category()

    source_framing = source.framing_object()
    target_framing = target.framing_object()
    source_free = source_framing.arrow().domain()
    target_free = target_framing.arrow().domain()
    source_change = source_free.module_category().Mor(source_free, target_free)(
        {
            "x": target_framing.arrow().domain().module_generator("u"),
            "y": target_framing.arrow().domain().module_generator("v"),
        }
    )
    target_change = source.module_category().Mor(source, target)(
        {
            "x": target.module_generator("u"),
            "y": target.module_generator("v"),
        }
    )
    square = category.Mor(source_framing, target_framing)(
        source_change, target_change
    )

    assert square.left() is source_change
    assert square.right() is target_change
    assert square.right() * source_framing.arrow() == (
        target_framing.arrow() * square.left()
    )


def test_module_morphism_lifts_to_the_selected_presentation_diagrams() -> None:
    source_target = ZZ.free_module(finite_ordered_set(("x", "y")))
    source_relations = ZZ.free_module(finite_ordered_set(("r",)))
    source = source_relations.module_category().Mor(source_relations, source_target)(
        {"r": source_target.scalar_multiple(ZZ(6), source_target.module_generator("y"))}
    ).cokernel()

    target_target = ZZ.free_module(finite_ordered_set(("u", "v")))
    target_relations = ZZ.free_module(finite_ordered_set(("s",)))
    target = target_relations.module_category().Mor(target_relations, target_target)(
        {"s": target_target.scalar_multiple(ZZ(3), target_target.module_generator("v"))}
    ).cokernel()

    morphism = source.module_category().Mor(source, target)(
        {
            "x": target.module_generator("u"),
            "y": target.module_generator("v"),
        }
    )
    square = morphism.selected_presentation_morphism()

    assert square.domain() is source.presentation_object()
    assert square.codomain() is target.presentation_object()
    assert square.right() * source.presentation() == target.presentation() * square.left()
    source.presentation_projection()
    target_projection = target.presentation_projection()
    for label in source.module_generating_set():
        lifted = square.right()(source.presentation().codomain().module_generator(label))
        assert target_projection(lifted) == morphism(source.module_generator(label))


def test_derived_module_constructors_retain_selected_data_and_scalar_actions() -> None:
    cyclic = _cyclic_six_from_presentation()
    free = ZZ.free_module(finite_ordered_set(("e",)))
    modules = Modules(ZZ)
    constructions = (
        modules.biproduct((cyclic, free)),
        modules.tensor_product((cyclic, free)),
        cyclic.module_category().Mor(cyclic, cyclic),
        cyclic.tensor_power(2),
        cyclic.symmetric_power(2),
        cyclic.exterior_power(2),
        cyclic.divided_power_module(2),
    )

    for module in constructions:
        assert module in ModulesWithChosenFinitePresentation(ZZ)
        assert module.presentation_object().arrow() is module.presentation()
        assert module.framing_object().arrow().codomain() is module
        labels = module.module_generating_set()
        element = (
            module.zero()
            if labels.cardinality() == 0
            else module.module_generator(next(iter(labels)))
        )
        assert module.scalar_action()(ZZ(4))(element) == module.scalar_multiple(
            ZZ(4), element
        )

    powers = (
        (cyclic.tensor_power(2), TensorPowerModules(ZZ)),
        (cyclic.symmetric_power(2), SymmetricPowerModules(ZZ)),
        (cyclic.exterior_power(2), AlternatingPowerModules(ZZ)),
        (cyclic.divided_power_module(2), DividedPowerModules(ZZ)),
    )
    for power, category in powers:
        assert power in category
        assert power.power_source() is cyclic
        assert power.power_degree() == 2


def test_free_duality_retains_the_selected_framing_and_action() -> None:
    module = ZZ.free_module(NN)
    dual = module.dual_module()

    assert dual.module_generating_set() is module.module_generating_set()
    assert dual.framing_object().arrow().codomain() is dual
    displayed = repr(dual.module_generators())
    assert displayed.startswith("Module generators over ")
    assert "Indexed family" not in displayed
    label = NN(3)
    element = dual.module_generator(label)
    assert dual.scalar_action()(ZZ(-2))(element) == dual.scalar_multiple(
        ZZ(-2), element
    )


def test_presented_duality_is_the_internal_mor_into_the_regular_module() -> None:
    module = _cyclic_six_from_presentation()
    dual = module.dual_module()

    assert dual is module.module_category().Mor(module, ZZ.regular_module())
    assert dual.source_module() is module
    assert dual.target_module() is ZZ.regular_module()
    assert dual in ModulesWithChosenFinitePresentation(ZZ)
    assert dual.presentation_object().arrow() is dual.presentation()


def test_mor_over_a_noncommutative_ring_is_enriched_over_its_center() -> None:
    ring = QQ.matrix_space(2)
    additive = AdditiveGroups().AdditiveCommutative()
    endomorphisms = additive.End(ring)
    action = ring.Mor(endomorphisms)(
        lambda scalar: endomorphisms.elementwise(
            lambda element: scalar * element,
        ),
    )
    regular = Modules(ring)(action)
    linear_endomorphisms = Modules(ring).End(regular)
    center = ring.ring_center()

    assert linear_endomorphisms.base_ring() is center
    identity = linear_endomorphisms.identity()
    central_scalar = center(ring.one())
    scaled = linear_endomorphisms.scalar_multiple(central_scalar, identity)
    element = regular(ring.one())
    assert scaled(element) == regular.scalar_multiple(central_scalar, element)


def test_localization_is_scalar_extension_of_the_selected_presentation_and_action() -> None:
    ring = QQ.polynomial_ring("x")
    x = ring.algebra_generator("x")
    target = ring.free_module(finite_ordered_set(("g",)))
    relations = ring.free_module(finite_ordered_set(("r",)))
    module = relations.module_category().Mor(relations, target)(
        {"r": target.scalar_multiple(x, target.module_generator("g"))}
    ).cokernel()
    localized = module.localize(x - ring.one())

    localization_ring = localized.base_ring()
    assert localized.localization_functor().ring_map() is localization_ring.localization_map()
    assert localized in ModulesWithChosenFinitePresentation(localization_ring)
    assert localized.presentation_object().arrow() is localized.presentation()
    generator = localized.module_generator("g")
    scalar = localization_ring.localization_map()(x)
    acted = localized.scalar_action()(scalar)(generator)
    multiplied = localized.scalar_multiple(scalar, generator)

    assert generator.parent() is localized
    assert scalar.parent() is localization_ring
    assert acted.parent() is localized
    assert multiplied.parent() is localized
    assert acted == multiplied
    assert acted.numerator().parent() is module
    assert acted.denominator().parent() is ring

    inverse = localization_ring.fraction(ring.one(), x - ring.one())
    fraction = localized.fraction(module.module_generator("g"), x - ring.one())
    acted_fraction = localized.scalar_action()(inverse)(fraction)

    assert inverse.parent() is localization_ring
    assert fraction.parent() is localized
    assert acted_fraction.parent() is localized
    assert acted_fraction.numerator().parent() is module
    assert acted_fraction.denominator().parent() is ring

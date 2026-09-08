r"""M0 constructor contracts for module actions and selected presentations.

These examples are committed unverified under the standing preamble policy.
They distinguish the chosen presentation from the underlying module while
requiring every constructor route to expose and use the same scalar-action
morphism ``R -> End_Ab(U(M))``.
"""

from dzack_research.preamble.all import (
    AdditiveGroups,
    BasedFreeModule,
    FreeModuleOn,
    FramedModules,
    GeneralModule,
    MatrixSpace,
    ModulesWithChosenFinitePresentation,
    NN,
    QQ,
    Set,
    ZZ,
    module_homset,
)
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.abstract_categories.constructions import (
    Biproduct,
    TensorProduct,
)
from dzack_research.preamble.categories.modules.internal_hom import InternalHom
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    ring_as_module,
)
from dzack_research.preamble.categories.modules.powers import (
    AlternatingPower,
    AlternatingPowerModules,
    DividedPower,
    DividedPowerModules,
    SymmetricPower,
    SymmetricPowerModules,
    TensorPower,
    TensorPowerModules,
)
from dzack_research.preamble.categories.modules.pure.modules import restrict_scalars
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism
from dzack_research.preamble.categories.sets import finite_ordered_set


def _cyclic_six_from_presentation():
    target = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    presentation = module_homset(relations, target)(
        {"r": target.scalar_multiple(ZZ(6), target.module_generator("x"))}
    )
    return presentation.cokernel()


def _cyclic_six_from_action():
    return GeneralModule(
        ZZ,
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

    forward = module_homset(presented, acted)(
        {"x": acted(1)}
    )
    inverse = module_homset(acted, presented).elementwise(
        lambda element: presented.scalar_multiple(
            ZZ(element.underlying_element()), generator
        ),
        verify_linearity=False,
    )
    comparison = Isomorphism(forward, inverse)

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
    target = BasedFreeModule(ZZ, finite_ordered_set(("free", "torsion")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    module = module_homset(relations, target)(
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
    module = FreeModuleOn(ZZ, NN)
    element = module({NN(2): ZZ(3), NN(100): ZZ(-1)})

    assert module.scalar_action()(ZZ(4))(element) == module.scalar_multiple(
        ZZ(4), element
    )
    assert module.scalar_multiple(ZZ(4), element).monomial_coefficients() == {
        NN(2): ZZ(12),
        NN(100): ZZ(-4),
    }


def test_restriction_of_scalars_exposes_the_composed_action() -> None:
    extension = BasedFreeModule(QQ, finite_ordered_set(("e",)))
    inclusion = ring_morphism(ZZ, QQ, QQ)
    restricted = restrict_scalars(extension, inclusion)
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

    target = BasedFreeModule(ZZ, finite_ordered_set(("x", "contractible")))
    relations = BasedFreeModule(ZZ, finite_ordered_set(("r", "s")))
    stabilized = module_homset(relations, target)(
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
    source = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    category = FramedModules(ZZ).framing_category()

    source_framing = source.framing_object()
    target_framing = target.framing_object()
    source_change = module_homset(
        source_framing.arrow().domain(), target_framing.arrow().domain()
    )(
        {
            "x": target_framing.arrow().domain().module_generator("u"),
            "y": target_framing.arrow().domain().module_generator("v"),
        }
    )
    target_change = module_homset(source, target)(
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
    source_target = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    source_relations = BasedFreeModule(ZZ, finite_ordered_set(("r",)))
    source = module_homset(source_relations, source_target)(
        {"r": source_target.scalar_multiple(ZZ(6), source_target.module_generator("y"))}
    ).cokernel()

    target_target = BasedFreeModule(ZZ, finite_ordered_set(("u", "v")))
    target_relations = BasedFreeModule(ZZ, finite_ordered_set(("s",)))
    target = module_homset(target_relations, target_target)(
        {"s": target_target.scalar_multiple(ZZ(3), target_target.module_generator("v"))}
    ).cokernel()

    morphism = module_homset(source, target)(
        {
            "x": target.module_generator("u"),
            "y": target.module_generator("v"),
        }
    )
    square = morphism.selected_presentation_morphism()

    assert square.domain() is source.presentation_object()
    assert square.codomain() is target.presentation_object()
    assert square.right() * source.presentation() == target.presentation() * square.left()
    source_projection = source.presentation_projection()
    target_projection = target.presentation_projection()
    for label in source.module_generating_set():
        lifted = square.right()(source.presentation().codomain().module_generator(label))
        assert target_projection(lifted) == morphism(source.module_generator(label))


def test_derived_module_constructors_retain_selected_data_and_scalar_actions() -> None:
    cyclic = _cyclic_six_from_presentation()
    free = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    constructions = (
        Biproduct(cyclic, free),
        TensorProduct(cyclic, free),
        InternalHom(cyclic, cyclic),
        TensorPower(cyclic, 2),
        SymmetricPower(cyclic, 2),
        AlternatingPower(cyclic, 2),
        DividedPower(cyclic, 2),
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
        (TensorPower(cyclic, 2), TensorPowerModules(ZZ)),
        (SymmetricPower(cyclic, 2), SymmetricPowerModules(ZZ)),
        (AlternatingPower(cyclic, 2), AlternatingPowerModules(ZZ)),
        (DividedPower(cyclic, 2), DividedPowerModules(ZZ)),
    )
    for power, category in powers:
        assert power in category
        assert power.power_source() is cyclic
        assert power.power_degree() == 2


def test_free_duality_retains_the_selected_framing_and_action() -> None:
    module = FreeModuleOn(ZZ, NN)
    dual = module.dual_module()

    assert dual.module_generating_set() is module.module_generating_set()
    assert dual.framing_object().arrow().codomain() is dual
    label = NN(3)
    element = dual.module_generator(label)
    assert dual.scalar_action()(ZZ(-2))(element) == dual.scalar_multiple(
        ZZ(-2), element
    )


def test_presented_duality_is_the_internal_hom_into_the_regular_module() -> None:
    module = _cyclic_six_from_presentation()
    dual = module.dual_module()

    assert dual is InternalHom(module, ring_as_module(ZZ))
    assert dual.source_module() is module
    assert dual.target_module() is ring_as_module(ZZ)
    assert dual in ModulesWithChosenFinitePresentation(ZZ)
    assert dual.presentation_object().arrow() is dual.presentation()


def test_hom_over_a_noncommutative_ring_is_enriched_over_its_center() -> None:
    ring = MatrixSpace(QQ, 2)
    additive = AdditiveGroups().AdditiveCommutative()
    endomorphisms = additive.End(ring)
    action = ring_morphism(
        ring,
        endomorphisms,
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

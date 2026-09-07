r"""Classifying categories and categorical group actions ``BG -> C``."""

from dzack_research.preamble.all import (
    QQ,
    FreeModule,
    GObjects,
    Groups,
    Modules,
    Sets,
    finite_g_set,
)
from dzack_research.preamble.categories.group.classifying_categories import ClassifyingFunctor


def test_classifying_category_and_the_quotient_from_c4_to_c2() -> None:
    group = Groups.C(4)
    quotient = Groups.C(2)
    generator = next(iter(group.group_generators()))
    quotient_generator = next(iter(quotient.group_generators()))
    phi = group.Mor(quotient)({generator: quotient_generator})
    category = group.classifying_category()
    point = category.an_object()
    arrows = category.Mor(point, point)
    arrow = arrows(generator)

    assert (arrow * arrow).group_element() == generator * generator
    assert (arrow * arrow).group_element().order() == 2
    assert arrows.identity().group_element() == group.one()
    assert arrow * arrow.inverse() == arrows.identity()
    assert arrows.identity() * arrow == arrow

    functor = ClassifyingFunctor(phi)
    target = quotient.classifying_category()
    target_point = target.an_object()
    assert functor.domain() is category
    assert functor.codomain() is target
    assert functor(point) is target_point
    assert functor(arrow).group_element() == quotient_generator
    assert functor(arrow * arrow) == target.Mor(target_point, target_point).identity()
    assert functor(arrow * arrow) == functor(arrow) * functor(arrow)
    assert functor(arrows.identity()) == target.Mor(target_point, target_point).identity()


def _swap_action():
    group = Groups.C(2)
    points = Sets.Δ[1]
    generator = group.group_generators()[0]

    def action(group_element, point):
        if group_element == group.one():
            return point
        return points(1 - int(point))

    acted = finite_g_set(points, group, action)
    return group, generator, acted


def test_generic_g_object_is_an_actual_functor_and_equivariant_maps_are_natural() -> None:
    group, generator, represented = _swap_action()
    category = GObjects(group, Sets())
    action = represented.action_functor()
    acted = category(action)

    assert acted in category
    assert acted.arrow().functor() is action
    assert category.forgetful_functor()(acted) is represented

    component = represented.action_of(generator)
    equivariant = category.Mor(acted, acted)(lambda _point: component)
    classifying = group.classifying_category()
    generator_arrow = classifying.Mor(
        classifying.an_object(), classifying.an_object()
    )(generator)
    left, right = equivariant.naturality_square(generator_arrow)
    assert left == right
    assert category.forgetful_functor()(equivariant) == component


def test_restriction_is_precomposition_by_the_classifying_functor() -> None:
    quotient, quotient_generator, represented = _swap_action()
    group = Groups.C(4)
    generator = group.group_generators()[0]
    phi = group.Mor(quotient)({generator: quotient_generator})
    acted = GObjects(quotient, Sets())(represented.action_functor())

    restricted = GObjects(quotient, Sets()).restriction(phi)(acted)
    action = restricted.arrow().functor()
    classifying = group.classifying_category()
    arrow = classifying.Mor(classifying.an_object(), classifying.an_object())(generator)

    assert action.domain() is classifying
    assert action(arrow)(Sets.Δ[1](0)) == Sets.Δ[1](1)
    assert action.factors()[0].group_morphism() is phi


def test_transport_is_postcomposition_on_objects_and_nonidentity_arrows() -> None:
    group, generator, represented = _swap_action()
    acted = GObjects(group, Sets())(represented.action_functor())
    component = represented.action_of(generator)
    equivariant = GObjects(group, Sets()).Mor(acted, acted)(lambda _point: component)

    free_module = Sets().free_module(QQ)
    transport = GObjects(group, Sets()).transport(free_module)
    transported = transport(acted)
    transported_arrow = transport(equivariant)
    module = GObjects(group, free_module.codomain()).forgetful_functor()(transported)
    classifying = group.classifying_category()

    assert transported.arrow().functor().factors()[-1] is free_module
    assert transported_arrow.component(classifying.an_object())(
        module.module_generator(Sets.Δ[1](0))
    ) == module.module_generator(Sets.Δ[1](1))


def test_sign_module_uses_the_same_action_functor_and_equivariant_map_semantics() -> None:
    group = Groups.C(2)
    generator = group.group_generators()[0]
    line = FreeModule(QQ, ("e",))

    def sign_action(group_element, vector):
        return vector if group_element == group.one() else -vector

    representation = Modules(QQ[group])(line, sign_action)
    category = GObjects(group, Modules(QQ))
    equivariant = category.Mor(representation, representation)
    doubling = equivariant(
        {"e": 2 * representation.module_generator("e")}
    )
    transformation = doubling.natural_transformation()
    classifying = group.classifying_category()
    arrow = classifying.Mor(classifying.an_object(), classifying.an_object())(generator)

    assert representation in Modules(QQ[group])
    assert representation.unacted_module() is line
    assert representation.action_functor().domain() is classifying
    assert representation.action_functor()(arrow) == representation.action_of(generator)
    assert transformation.naturality_square(arrow)[0] == transformation.naturality_square(arrow)[1]

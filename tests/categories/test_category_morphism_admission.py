r"""Unverified specimens distinguishing arrow admission from object placement.

``Cat().Mor(C, D)`` is the category of functors and natural transformations,
not the parent of the arrows of ``Cat``. These constructions must accept the
actual functor arrows without making them placed functor objects implicitly.
"""

import pytest

from dzack_research.preamble.categories.abstract_categories.cat import (
    Cat,
    CategoryFunctorMorphism,
)
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.functors.core import IdentityFunctor, NaturalTransformation
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


@pytest.fixture
def discrete_arrow() -> CategoryFunctorMorphism:
    source = DiscreteCategory(finite_ordered_set((0, 1)))
    target = DiscreteCategory(finite_ordered_set(("a", "b")))
    functor = Cat().Mor(source, target).from_object_map(
        lambda point: "b" if point == 0 else "a",
    )
    return Cat().arrow(functor)


def test_a_functor_arrow_is_admitted_without_becoming_a_functor_object(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    functors = Cat().Mor(arrow.domain(), arrow.codomain())
    assert arrow not in functors
    stated = functors.object(arrow)
    assert stated in functors
    assert stated.arrow() is arrow
    assert IdentityFunctor(Cat())(arrow) is arrow
    assert arrow not in functors

    with pytest.raises(ValueError, match="wrong functor-category endpoints"):
        Cat().Mor(arrow.codomain(), arrow.domain()).object(arrow)


def test_products_admit_functor_components_and_reject_wrong_endpoints(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    product = Cat().product((Cat(), Cat()))
    source = product(arrow.domain(), arrow.domain())
    target = product(arrow.codomain(), arrow.codomain())
    maps = product.Mor(source, target)
    pair = maps(arrow, arrow)
    assert pair.first() is arrow
    assert pair.second() is arrow
    assert pair * product.identity(source) == pair
    assert product.identity(target) * pair == pair

    with pytest.raises(ValueError, match="first map"):
        maps(Cat().identity(arrow.domain()), arrow)


def test_opposites_admit_functor_arrows_with_reversed_endpoints(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    opposite = Cat().opposite()
    source = opposite(arrow.codomain())
    target = opposite(arrow.domain())
    maps = opposite.Mor(source, target)
    reversed_arrow = maps(arrow)
    assert reversed_arrow.domain() is source
    assert reversed_arrow.codomain() is target
    assert reversed_arrow.underlying_arrow() is arrow
    assert (reversed_arrow * opposite.identity(source)).underlying_arrow() == arrow

    with pytest.raises(ValueError, match="reversed arrow"):
        maps(Cat().identity(arrow.domain()))


def test_a_square_in_cat_retains_its_actual_functor_edges(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    arrows = Cat().ArrowCategory()
    stated = arrows(arrow)
    square = arrows.Mor(stated, stated).identity()
    assert square.left() is Cat().identity(arrow.domain())
    assert square.right() is Cat().identity(arrow.codomain())
    assert square * square == square


def test_presented_images_in_cat_retain_functor_arrows_and_identities(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    images = IdentityFunctor(Cat()).Image()
    source = images(arrow.domain())
    target = images(arrow.codomain())
    maps = images.Mor(source, target)
    represented = maps(arrow)
    assert represented.underlying_arrow() is arrow
    assert images.inclusion()(represented) is arrow
    identity = images.identity(source)
    assert identity.underlying_arrow() is Cat().identity(arrow.domain())
    assert (represented * identity).underlying_arrow() == arrow

    with pytest.raises(ValueError, match="underlying functor images"):
        maps(Cat().identity(arrow.domain()))


def test_natural_transformation_components_in_cat_are_actual_functor_arrows(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    identity = IdentityFunctor(Cat())
    transformation = NaturalTransformation(identity, identity, Cat().identity)
    component = transformation.component(arrow.domain())
    assert component is Cat().identity(arrow.domain())
    assert transformation.naturality_target_composite(arrow) == arrow
    assert transformation.naturality_source_composite(arrow) == arrow


def test_wide_and_core_constructions_retain_the_exact_base_objects() -> None:
    r"""Changing only the arrows neither adds object data nor changes placement."""
    base = Sets()
    points = finite_ordered_set(("a", "b"))
    placement = points.category()
    core = base.Core()
    injections = base.WideSubcategory(base.MonomorphismArrowCategory())

    for category in (core, injections, injections.Core()):
        assert points in category
        assert category.object(points) is points
        assert category(points) is points
        assert category.ObjectType is base.ObjectType
        assert category.ElementType is base.ElementType
        assert IdentityFunctor(category)(points) is points

        maps = category.MorCategory().Of(points, points)
        assert category.Mor(points, points) is maps
        assert category.MorCategory().Between(points, points) is maps
        assert points.Mor(points, category=category) is maps
        assert category.End(points) is maps
        identity = category.identity(points)
        assert maps.accepts(identity)
        assert IdentityFunctor(category)(identity) is identity
        assert points.category() is placement


def test_shared_objects_do_not_remove_the_selected_arrow_restriction() -> None:
    base = Sets()
    points = finite_ordered_set(("a", "b"))
    maps = base.Mor(points, points)
    swap = maps(lambda point: {"a": "b", "b": "a"}[point])
    collapse = maps(lambda _point: "a")
    injections = base.WideSubcategory(base.MonomorphismArrowCategory())
    selected = injections.MorCategory().Of(points, points)

    assert selected.arrow_set() is maps
    assert selected.accepts(swap)
    assert not selected.accepts(collapse)
    assert selected.object(swap).arrow() is swap
    assert injections.compose(swap, swap) == injections.identity(points)
    with pytest.raises(ValueError):
        selected.object(collapse)
    with pytest.raises(ValueError):
        injections.compose(swap, collapse)
    with pytest.raises(TypeError):
        IdentityFunctor(injections)(collapse)

    core = base.Core()
    isomorphisms = core.MorCategory().Of(points, points)
    isomorphism = isomorphisms(swap, swap)
    assert isomorphism in isomorphisms
    assert not isomorphisms.accepts(collapse)
    assert isomorphisms.object(isomorphism) in isomorphisms
    assert IdentityFunctor(core)(isomorphism) is isomorphism
    with pytest.raises(ValueError):
        isomorphisms(swap, collapse)


def test_core_and_wide_mors_refuse_objects_over_a_different_base_ring() -> None:
    from dzack_research.preamble.all import Modules, QQ, ZZ

    base = Modules(QQ)
    rational = QQ.free_module(1)
    integral = ZZ.free_module(1)
    categories = (base.Core(), base.WideSubcategory(base.MonomorphismArrowCategory()))
    for category in categories:
        assert rational in category
        assert integral not in category
        with pytest.raises(TypeError):
            category.object(integral)
        with pytest.raises(TypeError):
            category.Mor(integral, rational)
        with pytest.raises(TypeError):
            category.Mor(rational, integral)
        with pytest.raises(TypeError):
            category.MorCategory().Of(integral, rational)
        with pytest.raises(TypeError):
            category.End(integral)
        with pytest.raises(TypeError):
            IdentityFunctor(category).object_image(integral)

    with pytest.raises(ValueError):
        base.WideSubcategory(Modules(ZZ).MonomorphismArrowCategory())


def test_core_of_a_fixed_mor_retains_its_object_and_endpoint_representation() -> None:
    left = finite_ordered_set(("a", "b"))
    right = finite_ordered_set(("a", "b"))
    assert left == right and left is not right
    first = Sets().Mor(left, left)
    second = Sets().Mor(right, right)
    first_core = first.Core()
    second_core = second.Core()
    assert first_core is not second_core
    assert first_core.base_category() is first
    assert second_core.base_category() is second
    assert first_core.arrow_category().base_category() is first
    assert second_core.arrow_category().base_category() is second

    arrow = first.identity()
    stated = first.object(arrow)
    assert first_core.object(stated) is stated
    assert stated in first_core
    assert stated not in second_core
    maps = first_core.MorCategory().Of(arrow, stated)
    assert maps is first_core.Mor(stated, arrow)
    assert maps.domain() is stated and maps.codomain() is stated
    assert IdentityFunctor(first_core)(stated) is stated
    with pytest.raises((TypeError, ValueError)):
        second_core.MorCategory().Of(stated, stated)


def test_core_of_cat_uses_the_same_category_endpoint_on_every_mor_entry() -> None:
    base = Cat()
    core = base.Core()
    category = Sets()
    stated = base.object(category)
    maps = core.MorCategory().Of(category, stated)
    assert maps is core.Mor(stated, category)
    assert maps is core.MorCategory().Between(category, category)
    assert maps.domain() is stated and maps.codomain() is stated
    assert core.object(category) is category
    assert core.object(stated) is stated
    assert IdentityFunctor(core)(stated) is stated
    assert maps.identity().domain() is stated


def test_native_functor_mor_retains_placed_natural_transformation_endpoints(
    discrete_arrow: CategoryFunctorMorphism,
) -> None:
    arrow = discrete_arrow
    functor = arrow.functor()
    functors = Cat().Mor(arrow.domain(), arrow.codomain())
    native = functors.arrow_set()
    stated = native.object(functor)
    assert stated is functors.object(arrow)
    assert stated in native
    assert stated in functors
    assert arrow in native
    assert arrow not in functors
    assert functor not in native
    assert functor not in functors

    transformations = functors.Mor(stated, stated)
    assert native.Mor(stated, stated) is transformations
    assert native.MorCategory().Of(functor, arrow) is transformations
    assert native.MorCategory().Between(stated, functor) is transformations
    identity = transformations.identity()
    assert identity.domain() is stated and identity.codomain() is stated
    assert identity * identity == identity
    assert IdentityFunctor(native)(stated) is stated
    assert IdentityFunctor(native)(identity) is identity

    wrong_functor = IdentityFunctor(functor.domain())
    wrong_object = wrong_functor.object()
    assert wrong_object not in native
    assert wrong_object not in functors
    with pytest.raises(TypeError):
        native.MorCategory().Of(wrong_object, stated)
    with pytest.raises(ValueError):
        native.MorCategory().Of(wrong_functor, functor)


def test_functor_construction_does_not_identify_equal_but_distinct_mor_domains() -> None:
    left = finite_ordered_set(("a", "b"))
    right = finite_ordered_set(("a", "b"))
    assert left == right and left is not right
    first = Sets().Mor(left, left)
    second = Sets().Mor(right, right)
    assert first is not second
    selected = Cat().Mor(first, first)
    other = Cat().Mor(second, second)
    identity = IdentityFunctor(first)
    wrong_identity = IdentityFunctor(second)
    stated = selected.object(identity)
    wrong_object = other.object(wrong_identity)
    assert stated in selected
    assert wrong_object not in selected
    assert wrong_object not in selected.arrow_set()
    assert selected.domain_category() is first
    assert other.domain_category() is second

    with pytest.raises(ValueError):
        selected.object(wrong_identity)
    with pytest.raises(ValueError):
        selected.arrow_set()(wrong_identity)
    with pytest.raises(ValueError):
        selected.MorCategory().Of(wrong_identity, identity)
    with pytest.raises(TypeError):
        selected.MorCategory().Of(wrong_object, stated)


def test_module_automorphism_groups_retain_their_categorical_arrow_objects() -> None:
    from dzack_research.preamble.all import QQ, ZZ

    for ring in (ZZ, QQ):
        module = ring.free_module(finite_ordered_set(("a", "b")))
        maps = module.module_category().Mor(module, module)
        automorphisms = module.module_category().Aut(module)
        swap = automorphisms(maps({
            "a": module.module_generator("b"),
            "b": module.module_generator("a"),
        }))
        stated = automorphisms.object(swap)
        ordinary = maps.object(swap)

        assert swap in automorphisms
        assert stated in automorphisms
        assert ordinary in maps
        assert ordinary not in automorphisms
        assert stated.arrow() is ordinary.arrow() is swap
        assert automorphisms.object(ordinary) is stated
        assert automorphisms.object(stated) is stated
        assert swap * swap == automorphisms.one()

        two_mor = automorphisms.MorCategory().Of(swap, stated)
        assert automorphisms.Mor(stated, swap) is two_mor
        assert automorphisms.MorCategory().Between(stated, stated) is two_mor
        assert two_mor.domain() is stated and two_mor.codomain() is stated
        identity = two_mor.identity()
        assert identity * identity == identity
        assert IdentityFunctor(automorphisms)(stated) is stated
        assert IdentityFunctor(automorphisms)(identity) is identity

        other = ring.free_module(finite_ordered_set(("c",)))
        other_group = other.module_category().Aut(other)
        wrong_object = other_group.object(other_group.one())
        assert wrong_object not in automorphisms
        with pytest.raises((TypeError, ValueError)):
            automorphisms.MorCategory().Of(wrong_object, stated)


def test_finite_form_group_predicates_do_not_replace_category_placement() -> None:
    from dzack_research.preamble.all import (
        QQ, ZZ, FractionFieldQuotients,
        TorsionBilinearFormModules, TorsionQuadraticFormModules,
    )
    from dzack_research.preamble.categories.group.groups import (
        GeneratedSubgroups, OwnedGroups, Subgroups,
    )

    for category, modulus in (
        (TorsionBilinearFormModules(ZZ), 1),
        (TorsionQuadraticFormModules(ZZ), 2),
    ):
        values = FractionFieldQuotients(ZZ)(modulus)
        form = category.from_relations_and_gram([[3]], [[QQ(2) / 3]], values)
        group = form.orthogonal_group()
        generator = next(iter(form.module_generators()))
        negative = next(arrow for arrow in group if arrow(generator) == -generator)
        stated = group.object(negative)
        ordinary = category.Mor(form, form).object(negative)

        assert negative in group
        assert group.accepts(negative)
        assert negative * negative == group.one()
        assert stated in group
        assert stated.arrow() is ordinary.arrow() is negative
        assert ordinary not in group
        assert group.object(ordinary) is stated
        assert group.object(stated) is stated

        two_mor = group.MorCategory().Of(negative, stated)
        assert group.Mor(stated, negative) is two_mor
        assert group.MorCategory().Between(stated, stated) is two_mor
        assert two_mor.domain() is stated and two_mor.codomain() is stated
        identity = two_mor.identity()
        assert identity * identity == identity
        assert IdentityFunctor(group)(stated) is stated
        assert IdentityFunctor(group)(identity) is identity

        trivial = group.subgroup_on(())
        assert trivial in Subgroups(group)
        assert trivial in GeneratedSubgroups(group)
        assert trivial in OwnedGroups().Framed()
        assert trivial not in Cat()
        assert group.one() in trivial
        assert negative not in trivial
        assert stated not in trivial
        assert trivial.cardinality() == 1
        assert tuple(trivial.group_generators()) == ()
        with pytest.raises(ValueError):
            trivial(negative)

        generated = group.subgroup_on((negative,))
        assert generated is not group
        assert generated in Subgroups(group)
        assert generated not in Cat()
        assert generated.cardinality() == 2
        assert tuple(generated.group_generators()) == (negative,)
        assert generated.group_generators()[0] is negative
        inclusion = generated.inclusion()
        assert inclusion.domain() is generated and inclusion.codomain() is group
        assert inclusion(negative) is negative
        assert all(arrow.parent() is group for arrow in generated)
        assert category.Iso(form, form) is group
        assert category.Aut(form) is group

        restricted = group.element_action().restrict_action(inclusion)
        assert restricted.acting_group() is generated
        assert restricted.act(negative, generator) == -generator

        nested = generated.subgroup((negative,))
        assert nested in Subgroups(generated)
        assert nested.supergroup() is generated
        assert nested.inclusion()(negative) is negative
        assert all(arrow.parent() is group for arrow in nested)

        other_form = category.from_relations_and_gram([[3]], [[QQ(2) / 3]], values)
        assert other_form is not form
        other_group = other_form.orthogonal_group()
        wrong_arrow = other_group.one()
        wrong_object = other_group.object(wrong_arrow)
        assert wrong_arrow not in group
        assert wrong_object not in group
        assert not group.accepts(wrong_arrow)
        with pytest.raises(ValueError):
            group(wrong_arrow)
        with pytest.raises(ValueError):
            group.subgroup((wrong_arrow,))
        with pytest.raises((TypeError, ValueError)):
            group.MorCategory().Of(wrong_object, stated)


def test_generated_subgroups_keep_the_selected_generator_framing() -> None:
    from dzack_research.preamble.categories.group.groups import (
        GeneratedSubgroups, OwnedGroups,
    )

    group = OwnedGroups().S(3)
    generator = group.group_generators()[0]
    subgroup = group.subgroup((generator,))
    assert subgroup in GeneratedSubgroups(group)
    assert subgroup in OwnedGroups().Framed()
    assert subgroup.selected_subgroup_generators()[0] is generator
    assert subgroup.group_generators()[0] is generator
    assert subgroup.inclusion()(generator) is generator

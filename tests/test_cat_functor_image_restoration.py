from dzack_research.preamble.all import (
    Cat,
    DiscreteCategory,
    DiscreteFunctor,
    ImageOfFunctor,
    ObjectSetFunctor,
    Sets,
    free_forgetful_adjunction,
    set_injection,
)


def test_cat_reifies_live_functors_and_functor_categories_have_natural_transformations() -> None:
    source = DiscreteCategory(Sets.Δ[1])
    target = DiscreteCategory(Sets.Δ[2])
    object_map = set_injection(
        source.object_set(), target.object_set(), lambda value: target.object_set()(value + 1)
    )
    functor = DiscreteFunctor(source, target, object_map)

    cat = Cat()
    cat_arrow = cat.arrow(functor)
    assert cat_arrow.domain() is cat.object(source)
    assert cat_arrow.codomain() is cat.object(target)

    functor_category = cat.Hom(source, target)
    functor_object = functor_category(functor)
    identity_transformation = functor_category.identity(functor_object)
    for index in source.objects():
        component = identity_transformation.component(index)
        image = functor(index)
        assert component.domain() is image
        assert component.codomain() is image

    object_sets = ObjectSetFunctor()
    carried = object_sets(cat_arrow)
    assert carried.domain() is source.object_set()
    assert carried.codomain() is target.object_set()
    assert carried(source.object_set()(0)) == target.object_set()(1)


def test_functor_image_objects_keep_chosen_preimages_without_reverse_lookup() -> None:
    free = free_forgetful_adjunction(__import__(
        "dzack_research.preamble.all", fromlist=["ZZ"]
    ).ZZ).left_adjoint()
    first = Sets.Δ[0]
    second = __import__(
        "dzack_research.preamble.categories.sets", fromlist=["finite_ordered_set"]
    ).finite_ordered_set((first(0),))
    image = ImageOfFunctor(free)
    presented_first = image(first)
    presented_second = image(second)

    assert presented_first.preimage() is first
    assert presented_second.preimage() is second
    inclusion = image.inclusion()
    assert inclusion(presented_first) is free(first)
    assert inclusion(presented_second) is free(second)

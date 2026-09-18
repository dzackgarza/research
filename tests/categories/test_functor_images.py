from dzack_research.preamble.all import (
    Cat,
    DiscreteCategory,
    ObjectSetFunctor,
    Sets,
)


def test_cat_reifies_live_functors_and_functor_categories_have_natural_transformations() -> None:
    source = DiscreteCategory(Sets.Δ[1])
    target = DiscreteCategory(Sets.Δ[2])
    object_map = Sets().Mono(source.object_set(), target.object_set())(
        lambda value: target.object_set()(value + 1)
    )
    functor = Cat().Mor(source, target).from_object_map(object_map)

    cat = Cat()
    cat_arrow = cat.arrow(functor)
    assert cat_arrow.domain() is cat.object(source)
    assert cat_arrow.codomain() is cat.object(target)

    functor_category = cat.Mor(source, target)
    functor_object = functor_category(functor)
    identity_transformation = functor_category.identity(functor_object)
    assert functor_category in cat
    assert functor_object in functor_category
    assert functor_object not in cat
    assert source.objects().index_set() is source.object_set()
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


def test_functor_forward_cache_and_chosen_image_presentations_are_distinct_data() -> None:
    ring = __import__("dzack_research.preamble.all", fromlist=["ZZ"]).ZZ
    free = Sets().free_module_adjunction(ring).left_adjoint()
    source = Sets.Δ[0]

    image = free(source)
    assert free(source) is image

    identity = Sets().Mor(source, source).identity()
    image_identity = free(identity)
    assert free(identity) is image_identity

    presented = free.Image()(source)
    assert free.Image() in Cat()
    assert presented in free.Image()
    assert presented not in Cat()
    assert presented.preimage() is source
    assert presented.underlying_image() is image
    assert presented.constructing_functor() is free

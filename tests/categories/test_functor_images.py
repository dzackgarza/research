import pytest

from dzack_research.preamble.all import (
    Cat,
    DiscreteCategory,
    DiscreteFunctor,
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

    functor_category = cat.Mor(source, target)
    functor_object = functor_category(functor)
    identity_transformation = functor_category.identity(functor_object)
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


def test_functor_provenance_records_objects_and_morphisms_in_one_store() -> None:
    free = free_forgetful_adjunction(__import__(
        "dzack_research.preamble.all", fromlist=["ZZ"]
    ).ZZ).left_adjoint()
    source = Sets.Δ[0]

    image = free(source)
    assert free(source) is image
    assert free.chosen_preimage(image) is source

    identity = Sets().Mor(source, source).identity()
    image_identity = free(identity)
    assert free(identity) is image_identity
    assert free.chosen_preimage(image_identity) is identity

    second_source = Sets.Δ[1]
    free.adopt_object_image(second_source, image)
    with pytest.raises(ValueError, match="multiple chosen preimages"):
        free.chosen_preimage(image)

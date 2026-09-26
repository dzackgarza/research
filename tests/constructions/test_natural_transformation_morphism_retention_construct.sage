r"""A natural-transformation morphism retains the exact selected transformation."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_natural_transformation_morphism_retains_its_transformation() -> None:
    identity = Sets().identity_functor()
    functor_category = Cat().Mor(Sets(), Sets())
    identity_object = functor_category.object(identity)
    parent = identity_object.Mor(identity_object)
    transformation = parent.identity().transformation()
    morphism = NaturalTransformationMorphism(parent, transformation)

    assert morphism.transformation() is transformation

r"""The twist of a finite form is a functor, so it acts on isometries.

Rescaling a form leaves the underlying module alone, so the twist of a
morphism is that same morphism read between the twisted parents.  These rows
assert the two statements that makes falsifiable: the arrow action lands in
the twisted orthogonal setting with an unchanged action on elements, and it
respects composition.
"""

from dzack_research.preamble.all import (
    Lattices,
    TorsionQuadraticFormModules,
    ZZ,
)


def _underlying_images(source, morphism):
    r"""Return the generator images of ``morphism``, read in the underlying module.

    A twisted form and its untwisted original share one underlying module and
    one generating set, so this is where two morphisms with different formed
    endpoints become comparable.
    """
    target = morphism.codomain()
    return tuple(
        target.forget_form_morphism()(morphism(source.module_generator(label)))
        for label in source.module_generating_set()
    )


def test_twist_carries_a_discriminant_automorphism_to_the_twisted_form() -> None:
    form = Lattices(ZZ)("A2").discriminant_group()
    twist = TorsionQuadraticFormModules(ZZ).twist_functor(-1)
    twisted = twist(form)

    assert form.twist(-1) is twisted

    group = form.automorphism_group()
    assert group.order() > 1

    for automorphism in group:
        image = twist(automorphism)
        assert image.domain() is twisted
        assert image.codomain() is twisted
        assert _underlying_images(twisted, image) == _underlying_images(form, automorphism)


def test_twist_of_a_composite_is_the_composite_of_the_twists() -> None:
    form = Lattices(ZZ)("A2").discriminant_group()
    twist = TorsionQuadraticFormModules(ZZ).twist_functor(-1)
    twisted = twist(form)

    group = form.automorphism_group()
    for left in group.group_generators():
        for right in group.group_generators():
            assert _underlying_images(twisted, twist(left * right)) == _underlying_images(
                twisted, twist(left) * twist(right)
            )

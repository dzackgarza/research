r"""One category of ``G``-objects in ``C``; ``G``-sets and ``R[G]``-modules specialize it.

A ``G``-action on ``X`` in ``C`` is a group morphism ``G -> Aut_C(X)``; an
equivariant morphism is a morphism of ``C`` commuting with the actions.  The
specimens are the swap of two of three points and the regular representation
of ``S_3``.
"""

import pytest

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FiniteGSets,
    FreeModule,
    GObjects,
    Groups,
    Modules,
    Sets,
    finite_g_set,
)


def _swap_two_of_three():
    group = Groups.C(2)
    points = (ZZ(0), ZZ(1), ZZ(2))
    swapped = {ZZ(0): ZZ(1), ZZ(1): ZZ(0), ZZ(2): ZZ(2)}

    def action(group_element, point):
        return point if group_element == group.one() else swapped[point]

    return group, finite_g_set(points, group, action)


def _regular_representation(ring):
    r"""The free module on the elements of ``S_3``, acted on by left translation."""
    group = Groups.S(3)
    module = FreeModule(ring, tuple(group))

    def act(group_element, vector):
        return module.Mor(module)(
            {label: module.module_generator(group_element * label) for label in group}
        )(vector)

    return group, Modules(ring[group])(module, act)


def test_a_finite_g_set_on_an_owned_finite_ordered_set_is_a_g_object_in_sets() -> None:
    group, g_set = _swap_two_of_three()
    generator = group.group_generators().unrank(0)
    assert g_set in GObjects(group, Sets())
    assert g_set in FiniteGSets(group)
    assert g_set.acting_group() is group
    assert g_set.underlying_category() is Sets()
    swap = g_set.action_of(generator)
    assert swap in Sets().Mor(g_set, g_set)
    assert swap(ZZ(0)) == ZZ(1)
    assert g_set.act(generator, ZZ(2)) == ZZ(2)
    assert swap * swap == Sets().Mor(g_set, g_set).identity()
    assert g_set.is_invariant(ZZ(2))
    assert not g_set.is_invariant(ZZ(0))


def test_equivariant_maps_of_g_sets_are_the_set_maps_commuting_with_the_actions() -> None:
    group, g_set = _swap_two_of_three()
    equivariant = GObjects(group, Sets()).Mor(g_set, g_set)
    assert equivariant.identity() in equivariant
    collapse = equivariant(lambda point: ZZ(2))
    assert collapse(ZZ(0)) == ZZ(2)
    assert collapse * collapse == collapse
    with pytest.raises(ValueError):
        equivariant(lambda point: ZZ(0))


def test_the_regular_representation_is_a_g_object_in_modules() -> None:
    group, representation = _regular_representation(QQ)
    assert representation in GObjects(group, Modules(QQ))
    assert representation in Modules(QQ[group])
    assert representation.acting_group() is group
    endomorphisms = Modules(QQ).Mor(representation, representation)
    # Left translation is a left action: ``rho(gh) = rho(g) rho(h)``.
    for left in group.group_generators():
        for right in group.group_generators():
            assert representation.action_of(left * right) == (
                representation.action_of(left) * representation.action_of(right)
            )
            assert representation.action_of(left) in endomorphisms
    unit = representation.module_generator(group.one())
    total = sum(representation.module_generator(label) for label in group)
    assert representation.is_invariant(total)
    assert not representation.is_invariant(unit)
    assert representation.act(group.one(), unit) == unit


def test_equivariant_module_maps_commute_with_the_actions() -> None:
    group, representation = _regular_representation(QQ)
    equivariant = GObjects(group, Modules(QQ)).Mor(representation, representation)
    unit = representation.module_generator(group.one())
    total = sum(representation.module_generator(label) for label in group)
    averaging = equivariant({label: total for label in group})
    translate = representation.action_of(group.group_generators().unrank(0))
    assert averaging(unit - translate(unit)) == representation.zero()
    assert averaging * averaging == 6 * averaging.underlying_arrow()
    with pytest.raises(ValueError):
        equivariant(
            {
                label: (2 if label == group.one() else 1) * representation.module_generator(label)
                for label in group
            }
        )
    assert representation.Mor(representation).identity() in equivariant

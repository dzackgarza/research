"""Internal group objects are distinct from external BG-actions."""

import pytest

from dzack_research.preamble.all import (
    GObjects,
    Grp,
    Modules,
    OwnedGroups,
    QQ,
    Sets,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def _c2_internal_group():
    points = finite_ordered_set((0, 1))
    square = Sets().product((points, points))
    multiplication = Sets().Mor(square, points)(
        lambda pair: points((int(pair[0]) + int(pair[1])) % 2)
    )
    terminal = Sets().product(())
    unit = Sets().Mor(terminal, points)(lambda _point: points(0))
    inverse = Sets().Mor(points, points).identity()
    return Grp(Sets())(points, multiplication, unit, inverse)


def test_grp_of_sets_retains_the_group_structure_maps() -> None:
    group = _c2_internal_group()

    assert group in Grp(Sets())
    assert group.underlying_object() in Sets()
    assert group.multiplication().domain() is Sets().product(
        (group.underlying_object(), group.underlying_object())
    )
    assert group.unit_morphism().domain() is Sets().product(())
    assert group.inverse_morphism().domain() is group.underlying_object()


def test_grp_rejects_an_invalid_inverse() -> None:
    points = finite_ordered_set((0, 1))
    square = Sets().product((points, points))
    multiplication = Sets().Mor(square, points)(
        lambda pair: points((int(pair[0]) + int(pair[1])) % 2)
    )
    unit = Sets().Mor(Sets().product(()), points)(lambda _point: points(0))
    bad_inverse = Sets().Mor(points, points)(lambda _point: points(0))

    with pytest.raises(ValueError, match="inverse"):
        Grp(Sets())(points, multiplication, unit, bad_inverse)


def test_internal_action_checks_associativity_and_unit() -> None:
    group = _c2_internal_group()
    points = group.underlying_object()
    action_product = Sets().product((points, points))
    action = Sets().Mor(action_product, points)(
        lambda pair: points((int(pair[0]) + int(pair[1])) % 2)
    )
    acted = group.actions()(points, action)

    assert acted.group_object() is group
    assert acted.action_morphism() is action

    bad_action = Sets().Mor(action_product, points)(lambda _pair: points(0))
    with pytest.raises(ValueError, match="unit"):
        group.actions()(points, bad_action)


def test_external_group_actions_compare_to_internal_actions_only_when_constant_group_exists() -> None:
    abstract_group = OwnedGroups().C(2)
    external = GObjects(abstract_group, Sets())
    acted = external.an_object()
    comparison = external.internal_action_comparison(acted)

    assert external is not Grp(Sets())
    assert comparison.external_object() is acted
    assert comparison.internal_group_object() in Grp(Sets())
    assert comparison.internal_action().group_object() is comparison.internal_group_object()

    module_actions = GObjects(abstract_group, Modules(QQ))
    module_acted = module_actions.an_object()
    with pytest.raises(TypeError, match="constant internal group object"):
        module_actions.internal_action_comparison(module_acted)

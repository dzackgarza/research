import pytest
from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedTorsionModules,
    GF,
    GroupModule,
    Groups,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_ordinary_character_is_the_trace_class_function_of_the_stored_action() -> None:
    group = Groups.S(3)
    module = BasedFreeModule(ZZ, finite_ordered_set(("sign", "trivial")))
    sign_generator = module.module_generator("sign")
    trivial_generator = module.module_generator("trivial")
    positive = module.Hom(module)(
        {"sign": sign_generator, "trivial": trivial_generator}
    )
    negative = module.Hom(module)(
        {"sign": -sign_generator, "trivial": trivial_generator}
    )

    def action(group_element, vector):
        return (positive if group_element.sign() == 1 else negative)(vector)

    acted = GroupModule(module, group, action)
    character = acted.character()

    assert character.domain() is group
    for group_element in group:
        assert character(group_element) == acted.action_of(group_element).matrix().trace()

    transposition = next(element for element in group if element.order() == 2)
    three_cycle = next(element for element in group if element.order() == 3)
    assert character(group.one()) == 2
    assert character(transposition) == 0
    assert character(three_cycle) == 2


def test_brauer_character_uses_teichmuller_lifts_not_modular_traces() -> None:
    base_ring = GF(2)
    group = Groups.C(6)
    module = BasedFreeModule(base_ring, finite_ordered_set(("x", "y")))
    x = module.module_generator("x")
    y = module.module_generator("y")
    order_three = module.Hom(module)({"x": y, "y": x + y})
    generator = next(iter(group.group_generators()))

    def action(group_element, vector):
        exponent = next(
            exponent for exponent in range(6) if group_element == generator**exponent
        )
        moved = vector
        for _ in range(exponent % 3):
            moved = order_three(moved)
        return moved

    acted = GroupModule(module, group, action)
    brauer_character = acted.brauer_character()
    representatives = group.conjugacy_classes_representatives()
    regular_representatives = tuple(
        representative for representative in representatives if representative.order() % 2
    )

    assert tuple(brauer_character) == tuple(
        2 if representative == group.one() else -1
        for representative in regular_representatives
    )
    assert len(brauer_character) == 3 < len(representatives)
    order_three_element = generator**2
    assert acted.action_of(order_three_element).matrix().trace() == GF(2).one()
    order_three_index = regular_representatives.index(order_three_element)
    assert brauer_character[order_three_index] == -1


def test_nonfree_finitely_presented_group_module_has_no_ordinary_matrix_character() -> None:
    group = Groups.C(2)
    module = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    generator = next(iter(group.group_generators()))

    def action(group_element, vector):
        return vector if group_element == group.one() else -vector

    acted = GroupModule(module, group, action)
    assert acted.act(generator, acted.module_generator(0)) == -acted.module_generator(0)
    with pytest.raises(NotImplementedError, match="finite free group module"):
        acted.character()

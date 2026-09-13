from dzack_research.preamble.all import Groups, Modules, QQ
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreshFreeModuleOn
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_zero_module_accepts_the_trivial_group_action_without_fake_enumeration() -> None:
    group = Groups.C(2)
    zero = FreshFreeModuleOn(QQ, finite_ordered_set(()))

    acted = Modules(QQ).trivial_action(group)(zero)

    assert acted.unacted_module() is zero
    assert acted.coefficient_module_rank() == 0
    assert acted.is_trivial_action()
    assert acted.zero() == acted.act(group.group_generators()[0], acted.zero())

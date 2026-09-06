r"""Meet and join on ``Cat`` are the inclusion order the owned graph speaks in.

A subcategory is below its supercategories, so the greatest lower bound of a
family is the category of the objects lying in all of them, and the least
upper bound is the smallest category holding all of them.  The backend orders
categories by their axioms instead, which is the opposite order, so its two
names arrive inverted; these are the owned ones.
"""

from dzack_research.preamble.all import (
    Cat,
    FiniteSets,
    Modules,
    ZZ,
)


def test_the_meet_is_below_every_member() -> None:
    modules = Modules(ZZ)
    finite = FiniteSets()

    met = Cat().meet((modules, finite))

    assert met.is_subcategory(modules)
    assert met.is_subcategory(finite)


def test_the_join_is_above_every_member() -> None:
    modules = Modules(ZZ)
    finite = FiniteSets()

    joined = Cat().join((modules, finite))

    assert modules.is_subcategory(joined)
    assert finite.is_subcategory(joined)


def test_the_meet_of_one_family_sits_under_its_join() -> None:
    family = (Modules(ZZ), FiniteSets())

    assert Cat().meet(family).is_subcategory(Cat().join(family))

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
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.semigroup_algebras import (
    AffineSemigroupAlgebras,
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


def test_meet_drops_strict_supercategories_before_building_the_dynamic_class() -> None:
    affine = AffineSemigroupAlgebras(ZZ)
    commutative = CommutativeAlgebras(ZZ)
    presented = AlgebrasWithChosenFinitePresentation(ZZ)

    met = Cat().meet((affine, commutative, presented))

    assert met is affine

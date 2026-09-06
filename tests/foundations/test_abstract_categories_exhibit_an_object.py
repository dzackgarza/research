r"""The abstract layer's categories exhibit an inhabitant.

``an_object()`` is the contract every owned category carries, and it is what
lets anything reach a category's objects without knowing how they are built.
The four categories here sit at the top of the graph, where a missing witness
leaves nothing below reachable either.
"""

from dzack_research.preamble.all import (
    Cat,
    DiscreteCategories,
    DiscreteCategory,
    Sets,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets.set_categories import Homsets


def test_the_root_of_the_graph_exhibits_an_object() -> None:
    witness = Objects().an_object()

    assert witness in Objects()
    assert witness in Sets()


def test_the_category_of_categories_exhibits_a_category() -> None:
    witness = Cat().an_object()

    assert witness in Cat()
    assert witness.an_object() in witness


def test_the_category_of_discrete_categories_exhibits_one() -> None:
    witness = DiscreteCategories().an_object()

    assert witness in DiscreteCategories()
    assert witness.object_set() in Sets()
    assert witness.an_object() in witness


def test_the_category_of_hom_objects_exhibits_one() -> None:
    witness = Homsets().an_object()

    assert witness in Sets()
    assert witness.domain() is witness.codomain()
    assert witness.identity().domain() is witness.domain()


def test_a_discrete_category_exhibits_an_object_of_its_own() -> None:
    category = DiscreteCategory(Sets.Δ[1])

    assert category.an_object() in category

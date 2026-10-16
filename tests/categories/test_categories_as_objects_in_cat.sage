r"""A category is an object of Cat, with functors as its arrows."""

from dzack_research.preamble.all import *


def test_a_category_answers_its_own_endomorphisms_as_an_object_of_cat():
    category = Sets()
    endomorphisms = category.End()
    identity = endomorphisms.identity()

    assert endomorphisms is Cat().Mor(category, category)
    assert identity.domain() is category
    assert identity.codomain() is category
    assert endomorphisms(identity) is identity


def test_cat_keeps_the_object_and_category_readings_of_mor():
    categories = Cat()
    target = Sets()

    assert categories.Mor(target) is Cat().Mor(categories, target)

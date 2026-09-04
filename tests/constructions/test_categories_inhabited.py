r"""Every owned category exhibits an object, over every ring it can be taken over.

``OwnedCategory.an_object`` is the contract that a category is inhabited.  A
category over a base ring is inhabited over every ring in the catalogue, not
only over the integers: modules over a principal ideal domain must exist over
every named principal ideal domain, and a category that answers only over
$\mathbb Z$ has not stated what its parameter is.

The category list is read from the live session surface: every exported
subclass of ``OwnedCategory``.  Nullary ones are built bare; ones over a base
ring are built over each ring in the catalogue.
"""

import inspect

import pytest

import dzack_research.preamble.all as session
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing


def _exported_categories():
    r"""Every exported category class, split by how it is constructed."""
    nullary, over_ring = [], []
    for name in sorted(dir(session)):
        candidate = getattr(session, name)
        if not (inspect.isclass(candidate) and issubclass(candidate, OwnedCategory)):
            continue
        if candidate in (OwnedCategory, OwnedParameterizedCategory, OwnedCategoryOverBaseRing):
            continue
        if issubclass(candidate, OwnedCategoryOverBaseRing):
            over_ring.append(name)
        elif not issubclass(candidate, OwnedParameterizedCategory) and _is_nullary(candidate):
            nullary.append(name)
    return nullary, over_ring


def _is_nullary(category_class) -> bool:
    parameters = [
        parameter
        for parameter in inspect.signature(category_class.__init__).parameters.values()
        if parameter.name != "self"
        and parameter.kind not in (parameter.VAR_POSITIONAL, parameter.VAR_KEYWORD)
        and parameter.default is parameter.empty
    ]
    return not parameters


NULLARY, OVER_RING = _exported_categories()


@pytest.mark.parametrize("name", NULLARY)
def test_a_nullary_category_is_inhabited(name) -> None:
    category = getattr(session, name)()
    witness = category.an_object()
    assert witness in category, f"{name}.an_object() is not in {name}"


@pytest.mark.parametrize("name", OVER_RING)
def test_a_category_over_a_ring_is_inhabited_over_every_ring(name, commutative_ring) -> None:
    category = getattr(session, name)(commutative_ring)
    witness = category.an_object()
    assert witness in category, f"{name}({commutative_ring}).an_object() is not in it"
    assert witness.base_ring() is commutative_ring


@pytest.mark.parametrize("name", OVER_RING)
def test_a_category_over_a_ring_remembers_its_ring(name, field) -> None:
    category = getattr(session, name)(field)
    assert category.base_ring() is field
    assert category is getattr(session, name)(field)

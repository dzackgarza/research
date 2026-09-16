import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules import (
    ModulesWithConnection,
    ModulesWithFlatConnection,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_connection_categories_range_over_the_commutative_algebras_of_their_parameter() -> None:
    integers = _own_ring(SageZZ)
    commutative = Algebras(integers).Associative().Unital().Commutative()
    algebra = commutative.an_object()

    assert ModulesWithConnection(algebra).parameter_category() is commutative
    assert ModulesWithFlatConnection(algebra).parameter_category() is commutative


def test_connection_categories_reject_an_unstructured_parameter() -> None:
    unrelated = finite_ordered_set((0, 1))

    with pytest.raises((AssertionError, AttributeError)):
        ModulesWithConnection(unrelated)

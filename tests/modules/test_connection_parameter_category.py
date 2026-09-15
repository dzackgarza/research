import pytest
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.modules import (
    CommutativeAlgebraParameters,
    ModulesWithConnection,
    ModulesWithFlatConnection,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def test_connection_categories_state_their_commutative_algebra_parameter_domain() -> None:
    integers = _own_ring(SageZZ)
    algebra = Algebras(integers).Associative().Unital().Commutative().an_object()

    assert algebra in CommutativeAlgebraParameters()
    assert (
        ModulesWithConnection(algebra).parameter_category()
        is CommutativeAlgebraParameters()
    )
    assert (
        ModulesWithFlatConnection(algebra).parameter_category()
        is CommutativeAlgebraParameters()
    )


def test_connection_categories_reject_an_unstructured_parameter() -> None:
    unrelated = finite_ordered_set((0, 1))

    assert unrelated not in CommutativeAlgebraParameters()
    with pytest.raises(AssertionError, match="parameterized by"):
        ModulesWithConnection(unrelated)

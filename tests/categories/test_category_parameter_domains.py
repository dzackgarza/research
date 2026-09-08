from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings, _own_ring


def test_every_category_over_a_base_ring_states_the_ring_parameter_domain() -> None:
    integers = _own_ring(SageZZ)
    algebras = Algebras(integers)

    assert algebras.parameter_category() is OwnedRings()
    witness = algebras.parameter_category().an_object()
    assert witness in OwnedRings()
    assert Algebras(witness).base_ring() is witness


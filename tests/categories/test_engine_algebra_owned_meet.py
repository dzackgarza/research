r"""Engine-backed algebra views use the owned algebra category graph."""

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
)
from dzack_research.preamble.rings import session_ring_objects


def test_base_ring_as_algebra_has_owned_mathematical_placement() -> None:
    integers = session_ring_objects()["ZZ"]
    algebra = integers.Mor(integers).identity().as_algebra()

    assert algebra in Algebras(integers).Associative().Unital()
    assert algebra.unformed_module() is algebra
    assert algebra in Algebras(integers).Associative().Unital().Commutative()
    assert algebra not in FramedAlgebras(integers)
    assert algebra.base_ring() is integers

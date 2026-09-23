from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories import lattice_engines
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_oscar_supplies_an_actual_indefinite_integral_isometry() -> None:
    integers = _own_ring(SageZZ)
    source = Lattices(integers)(
        (
            (0, 1, 0),
            (1, 0, 0),
            (0, 0, -2),
        )
    )
    target = Lattices(integers)(
        (
            (0, 1, 0),
            (1, 2, 0),
            (0, 0, -2),
        )
    )

    assert not source.is_definite()
    assert not target.is_definite()
    witness_rows = lattice_engines._integral_isometry_witness(
        source.gram_tensor(),
        target.gram_tensor(),
    )
    assert witness_rows is not None
    isometry = source.Isom(target)._from_backend_row_action(witness_rows)
    assert isometry.domain() is source
    assert isometry.codomain() is target
    assert (~isometry) * isometry == source.Isom(source).identity()
    assert source.Isom(target).is_empty() is False



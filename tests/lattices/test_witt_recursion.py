r"""Exact rank-decreasing data for the represented higher-Witt recursion."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.eichler_criterion import (
    EichlerRecursiveStabilizerDatum,
    two_u_eichler_model,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_covering_stabilizers_restrict_to_rank_one_smaller_orthogonal_complements() -> None:
    integers = _own_ring(SageZZ)
    model = two_u_eichler_model(Lattices(integers)("A2"))
    lattice = model.lattice()
    recursive = model.recursive_stabilizer_data(integers(-2))

    assert recursive.cardinality() > 0
    for discriminant_class in recursive.index_set():
        datum = recursive[discriminant_class]
        assert isinstance(datum, EichlerRecursiveStabilizerDatum)
        vector = datum.vector()
        perpendicular = datum.perpendicular_lattice()
        inclusion = perpendicular.inclusion()
        assert vector.parent() is lattice
        assert vector.q() == -2
        assert int(perpendicular.module_rank()) + 1 == int(lattice.module_rank())
        assert datum.rank_drop() == 1
        assert datum.restricted_generators().index_set() is datum.stabilizer_generators()
        for generator in datum.stabilizer_generators():
            restricted = datum.restricted_generators()[generator]
            assert generator(vector) == vector
            assert restricted in perpendicular.O()
            for label in perpendicular.module_generating_set():
                element = perpendicular.module_generator(label)
                assert inclusion(restricted(element)) == generator(inclusion(element))

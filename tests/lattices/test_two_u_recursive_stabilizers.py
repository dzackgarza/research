r"""Recursive stabilizer and transporter data in a represented ``2U`` model."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.eichler_criterion import (
    EichlerCoveringOrbitDatum,
    two_u_eichler_model,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_covering_classes_retain_stabilizers_and_actual_full_orbit_transporters() -> None:
    integers = _own_ring(SageZZ)
    model = two_u_eichler_model(Lattices(integers)("A2"))
    lattice = model.lattice()
    data = model.covering_orbit_data(integers(-2))

    assert data.cardinality() > 0
    for discriminant_class in data.index_set():
        orbit = data[discriminant_class]
        assert isinstance(orbit, EichlerCoveringOrbitDatum)
        assert orbit.discriminant_class() == discriminant_class
        assert orbit.representative().parent() is lattice
        assert orbit.representative().q() == -2
        assert all(
            generator(orbit.representative()) == orbit.representative()
            for generator in orbit.stabilizer_generators()
        )
        transporter = orbit.transporter_to_full_orbit()
        assert transporter in lattice.O()
        assert transporter(orbit.representative()) == orbit.full_orbit_representative()


def test_covering_data_does_not_assert_distinct_full_orbits() -> None:
    integers = _own_ring(SageZZ)
    model = two_u_eichler_model(Lattices(integers)("A2"))
    data = model.covering_orbit_data(integers(-2))

    full_orbit_targets = tuple(
        tuple(data[index].full_orbit_representative().to_tuple())
        for index in data.index_set()
    )
    assert len(full_orbit_targets) == int(data.cardinality())

r"""Lattice refinements, subobjects, and biproducts use owned category meets."""

from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import (
    DirectSumObjects,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.modules.pure.modules import ModuleSubobjects
from dzack_research.preamble.rings import session_ring_objects


def test_lattice_subobject_retains_owned_module_subobject_placement() -> None:
    integers = session_ring_objects()["ZZ"]
    lattice = Lattices(integers)("A2")
    first = lattice.module_generators()[0]
    sublattice = lattice.subobject_on((first,))

    assert sublattice in Lattices(integers)
    assert sublattice in ModuleSubobjects(integers)
    assert sublattice.inclusion().codomain() is lattice


def test_lattice_biproduct_retains_owned_direct_sum_placement() -> None:
    integers = session_ring_objects()["ZZ"]
    plane = Lattices(integers)("U")
    biproduct = plane + plane

    assert biproduct in Lattices(integers)
    assert biproduct in DirectSumObjects(Lattices(integers))
    assert biproduct.summands().cardinality() == 2

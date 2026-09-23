r"""Exact half-space ownership for hyperbolic reflection chambers."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring








def test_hyperbolic_containment_uses_rays_and_lineality_not_the_origin() -> None:
    integers = _own_ring(SageZZ)
    lattice = HyperbolicLattices(integers)(Lattices(integers)([[2, 0], [0, -2]]))
    dual = lattice.dual_module()
    first, second = dual.module_generators()

    future = lattice.rational_polyhedral_cone((first - second, first + second))
    timelike = lattice.basis_vector(0)
    assert future.is_pointed()
    assert future.lies_in_closed_positive_cone(timelike)
    assert future.ideal_rays().cardinality() == 2
    assert future.timelike_rays().cardinality() == 0



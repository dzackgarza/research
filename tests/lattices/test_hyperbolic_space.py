r"""Owned positive-cone components and their projectivized hyperbolic geometry."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.polyhedral_cones import rational_polyhedral_cone
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def _lorentz_plane():
    integers = _own_ring(SageZZ)
    return HyperbolicLattices(integers)(Lattices(integers)([[2, 0], [0, -2]]))


def test_selected_positive_component_distinguishes_the_two_sheets() -> None:
    lattice = _lorentz_plane()
    timelike, spacelike = tuple(lattice.module_generators())
    component = lattice.positive_cone_component(timelike)

    assert timelike in component
    assert -timelike not in component
    assert spacelike not in component
    assert -timelike in component.opposite()


def test_hyperbolic_projectivization_identifies_positive_integral_multiples() -> None:
    lattice = _lorentz_plane()
    timelike = lattice.module_generator(0)
    space = lattice.hyperbolic_space(timelike)

    assert space.rational_point(timelike) == space.rational_point(3 * timelike)


def test_projectivized_light_cone_has_ideal_vertices() -> None:
    lattice = _lorentz_plane()
    timelike = lattice.module_generator(0)
    dual = lattice.dual_module()
    first, second = tuple(dual.module_generators())
    cone = rational_polyhedral_cone(lattice, (first - second, first + second), complete=True)

    polyhedron = lattice.hyperbolic_space(timelike).projectivize_cone(cone)
    assert polyhedron.ordinary_vertices().cardinality() == 0
    assert polyhedron.ideal_vertices().cardinality() == 2
    assert not polyhedron.is_compact()

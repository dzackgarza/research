r"""Owned positive-cone components and their projectivized hyperbolic geometry."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.hyperbolic_geometry import (
    HyperbolicPolyhedra,
    HyperbolicSpaces,
    PositiveConeComponents,
)
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces


def _lorentz_plane():
    integers = _own_ring(SageZZ)
    return HyperbolicLattices(integers)(Lattices(integers)([[2, 0], [0, -2]]))


def test_selected_positive_component_distinguishes_the_two_sheets() -> None:
    lattice = _lorentz_plane()
    timelike, spacelike = lattice.module_generators()
    component = lattice.positive_cone_component(timelike)

    assert component in PositiveConeComponents(lattice)
    assert component in Sets().Subobjects(component.ambient_space())
    assert component.contains(timelike)
    assert not component.contains(-timelike)
    assert not component.contains(spacelike)
    assert component.opposite().contains(-timelike)


def test_hyperbolic_projectivization_identifies_positive_integral_multiples() -> None:
    lattice = _lorentz_plane()
    timelike = lattice.module_generator(0)
    space = lattice.hyperbolic_space(timelike)

    assert space in HyperbolicSpaces(space.positive_cone_component())
    assert space in TopologicalSpaces()
    assert space.rational_point(timelike) == space.rational_point(3 * timelike)


def test_projectivized_light_cone_has_ideal_vertices() -> None:
    lattice = _lorentz_plane()
    timelike = lattice.module_generator(0)
    dual = lattice.dual_module()
    first, second = dual.module_generators()
    cone = lattice.rational_polyhedral_cone((first - second, first + second), complete=True)

    assert cone in Sets().Subobjects(cone.ambient_space())
    polyhedron = lattice.hyperbolic_space(timelike).projectivize_cone(cone)
    assert polyhedron in HyperbolicPolyhedra(polyhedron.hyperbolic_space())
    assert polyhedron in Sets().Subobjects(polyhedron.hyperbolic_space())
    assert polyhedron.ordinary_vertices().cardinality() == 0
    assert polyhedron.ideal_vertices().cardinality() == 2
    assert not polyhedron.is_compact()

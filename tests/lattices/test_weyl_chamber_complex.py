r"""Weyl chambers retain exact wall crossings and transporters."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.chamber_systems import ChamberSystems
from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def _one_wall_chamber():
    integers = _own_ring(SageZZ)
    lattice = HyperbolicLattices(integers)(Lattices(integers)([[2, 0], [0, -2]]))
    root = lattice.module_generator(1)
    covector = lattice.algebraic_correlation_morphism()(root)
    chamber = lattice.rational_polyhedral_cone(
        (covector,),
        wall_roots=(root,),
        complete=True,
    )
    return lattice, root, chamber


def test_simple_reflection_crosses_the_retained_wall() -> None:
    lattice, root, chamber = _one_wall_chamber()
    complex_ = chamber.chamber_complex()
    adjacency = complex_.fundamental_adjacencies()[root]

    assert complex_ in ChamberSystems()
    reflection = lattice.reflection(root)
    assert adjacency.source() is chamber
    assert adjacency.transporter() == reflection
    assert adjacency.target().wall_roots()[0] == -root
    assert adjacency.shared_wall_covector() == lattice.algebraic_correlation_morphism()(root)
    face = adjacency.shared_face()
    assert face.dimension() == chamber.dimension() - 1
    timelike = lattice.module_generator(0)
    assert face.contains(timelike)
    assert adjacency.transporter()(timelike) == timelike


def test_a_double_wall_word_returns_to_the_original_root_orientation() -> None:
    _lattice, root, chamber = _one_wall_chamber()
    complex_ = chamber.chamber_complex()
    transporter = complex_.transporter_from_word((root, root))

    assert transporter == complex_.lattice().O().one()
    returned = complex_.chamber_from_word((0, 0))
    assert returned.wall_roots() == chamber.wall_roots()

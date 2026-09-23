r"""Exact half-space ownership for hyperbolic reflection chambers."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.hyperbolic_lattices import HyperbolicLattices
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_root_halfspaces_retain_the_bilinear_covectors(monkeypatch) -> None:
    integers = _own_ring(SageZZ)
    lattice = HyperbolicLattices(integers)(Lattices(integers)([[2, 0], [0, -2]]))
    positive, negative = lattice.module_generators()
    root = negative
    monkeypatch.setattr(lattice, "_vinberg_search", lambda *_args, **_kw: (True, (root,)))

    chamber = lattice.fundamental_chamber()
    covector = chamber.halfspace_covectors()[0]
    assert chamber.wall_roots()[0] == root
    assert chamber.evaluate_covector(covector, positive) == lattice.b(root, positive)
    assert chamber.evaluate_covector(covector, negative) == lattice.b(root, negative)
    assert chamber.is_complete_wall_set() is True


def test_unbounded_cone_retains_rays_facets_and_lineality() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)([[1, 0], [0, 1]])
    dual = lattice.dual_module()
    first, second = dual.module_generators()

    cone = lattice.rational_polyhedral_cone((first, second))
    assert cone.is_pointed()
    assert cone.primitive_rays().cardinality() == 2
    assert cone.facet_covectors().cardinality() == 2
    assert cone.hilbert_basis().cardinality() == 2
    assert cone.lineality_generators().cardinality() == 0


def test_exact_engine_faces_cross_back_as_owned_cones() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)([[1, 0], [0, 1]])
    dual = lattice.dual_module()
    first, second = dual.module_generators()

    cone = lattice.rational_polyhedral_cone((first, second))
    assert cone.faces(0).cardinality() == 1
    assert cone.faces(1).cardinality() == 2
    assert cone.faces(2).cardinality() == 1
    assert cone.nonempty_faces().cardinality() == 4
    assert cone.faces(0)[0].primitive_rays().cardinality() == 0
    assert all(face.primitive_rays().cardinality() == 1 for face in cone.faces(1))


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


def test_root_defined_chamber_owns_its_reflection_group_and_diagram(monkeypatch) -> None:
    integers = _own_ring(SageZZ)
    lattice = HyperbolicLattices(integers)(Lattices(integers)([[2, 0], [0, -2]]))
    root = lattice.basis_vector(1)
    monkeypatch.setattr(lattice, "_vinberg_search", lambda *_args, **_kw: (True, (root,)))

    chamber = lattice.fundamental_chamber()
    group = chamber.weyl_group()
    reflection = lattice.reflection(root)
    assert reflection in group
    assert group.supergroup() is lattice.O()
    diagram = chamber.coxeter_diagram()
    assert diagram.roots().cardinality() == 1
    assert diagram.roots()[0] == root

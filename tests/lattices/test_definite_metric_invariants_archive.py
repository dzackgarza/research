r"""Archived definite-lattice metric invariants on the live lattice owner.

The archived ``DefiniteLattices`` category exposed closest vectors, successive
minima, theta series, kissing number, packing/covering radii, contact
polytopes, Hermite invariant, Hadamard ratio, and center/packing densities.
These are geometric invariants of the represented lattice, not cached table
entries; the specimens below retain their exact relations on both the square
lattice and the nonorthogonal root lattice ``A2``.
"""

from sage.symbolic.constants import pi

from dzack_research.preamble.all import QQ, RR, ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/definite_lattices.sage",
    "live_owner": "src/dzack_research/preamble/categories/definite_lattices.py",
    "owner_overrides": {
        "DefiniteSubobjectParent.embedding": "src/dzack_research/preamble/categories/lattices.py",
        "DefiniteLattices.Subobjects.ParentMethods.sum": "src/dzack_research/preamble/categories/lattices.py",
        "DefiniteLattices.Subobjects.ParentMethods.intersection": "src/dzack_research/preamble/categories/lattices.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_square_lattice_metric_invariants_are_exact() -> None:
    lattice = Lattices(ZZ)(2)
    e1, _e2 = lattice.module_generators()
    target = (QQ(3) / 4, QQ(1) / 4)

    assert lattice.closest_vector(target) == e1
    minima = lattice.successive_minima()
    assert minima.cardinality() == 2
    assert minima[0] == 1
    assert minima[1] == 1

    theta = lattice.theta_series(5)
    assert theta[0] == 1
    assert theta[1] == 4
    assert lattice.kissing_number() == 4

    assert lattice.packing_radius() == QQ(1) / 2
    assert lattice.covering_radius() ** 2 == QQ(1) / 2
    assert lattice.hadamard_ratio() == 1
    assert lattice.hermite_invariant() == 1
    assert lattice.center_density() == QQ(1) / 4
    assert lattice.packing_density() == RR(pi / 4)
    assert lattice.contact_polytope().n_vertices() == 4


def test_archived_a2_invariants_see_the_nonorthogonal_hexagonal_geometry() -> None:
    lattice = Lattices(ZZ)("A2")

    assert lattice.minimum() == -2
    assert lattice.kissing_number() == 6
    assert lattice.contact_polytope().n_vertices() == 6
    assert lattice.voronoi_relevant_vectors().cardinality() == 6

    minima = lattice.successive_minima()
    assert minima.cardinality() == 2
    assert minima[0] ** 2 == 2
    assert minima[1] ** 2 == 2

    # det(-G_A2)=3 and the minimal squared length is 2.
    assert lattice.hermite_invariant() ** 2 == QQ(4) / 3
    assert lattice.packing_radius() ** 2 == QQ(1) / 2

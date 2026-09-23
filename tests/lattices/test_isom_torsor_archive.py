r"""Archived ``Isom(L,M)`` torsor semantics on the live lattice Mor owner.

The archived lattice-homomorphism layer made ``Isom(L,M)`` a torsor under
``O(M)`` by postcomposition and required a transporter between any two
represented isometries.  The live Mor keeps those operations directly; the
specimens below retain the actual equation defining the torsor action.
"""

from dzack_research.preamble.all import ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattice_morphisms.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_isom_mor_is_acted_on_by_the_codomain_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("A2")
    mor = lattice.Isom(lattice)
    identity = mor.identity()
    root = lattice.module_generators()[0]
    reflection = lattice.reflection(root)

    assert mor.acting_group() is lattice.Aut()
    assert mor.act(lattice.Aut().one(), identity) == identity
    assert mor.act(reflection, identity) == reflection

    for generator in lattice.module_generators():
        assert mor.act(reflection, identity)(generator) == reflection(generator)


def test_archived_isom_transporter_is_the_postcomposition_torsor_difference() -> None:
    lattice = Lattices(ZZ)("A2")
    mor = lattice.Isom(lattice)
    mor.identity()
    first_root, second_root = lattice.module_generators()
    first = lattice.reflection(first_root)
    second = lattice.reflection(second_root) * first

    transporter = mor.transporter(first, second)

    assert transporter.parent() is mor.acting_group()
    assert mor.act(transporter, first) == second
    for generator in lattice.module_generators():
        assert transporter(first(generator)) == second(generator)

    back = mor.transporter(second, first)
    assert mor.act(back, second) == first
    assert back == ~transporter


def test_archived_identity_to_isometry_transporter_recovers_that_isometry() -> None:
    lattice = Lattices(ZZ)("A2")
    mor = lattice.Isom(lattice)
    identity = mor.identity()
    reflection = lattice.reflection(lattice.module_generators()[0])

    assert mor.transporter(identity, reflection) == reflection
    assert mor.transporter(reflection, identity) == ~reflection

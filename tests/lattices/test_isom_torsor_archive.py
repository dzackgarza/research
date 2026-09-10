r"""Archived ``Isom(L,M)`` torsor semantics on the live lattice Hom owner.

The archived lattice-homomorphism layer made ``Isom(L,M)`` a torsor under
``O(M)`` by postcomposition and required a transporter between any two
represented isometries.  The live homset keeps those operations directly; the
specimens below retain the actual equation defining the torsor action.
"""

from dzack_research.preamble.all import Lattices, ZZ


def test_archived_isom_homset_is_acted_on_by_the_codomain_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("A2")
    homset = lattice.Isom(lattice)
    identity = homset.identity()
    root = lattice.module_generators()[0]
    reflection = lattice.reflection(root)

    assert homset.acting_group() is lattice.Aut()
    assert homset.act(lattice.Aut().one(), identity) == identity
    assert homset.act(reflection, identity) == reflection

    for generator in lattice.module_generators():
        assert homset.act(reflection, identity)(generator) == reflection(generator)


def test_archived_isom_transporter_is_the_postcomposition_torsor_difference() -> None:
    lattice = Lattices(ZZ)("A2")
    homset = lattice.Isom(lattice)
    identity = homset.identity()
    first_root, second_root = lattice.module_generators()
    first = lattice.reflection(first_root)
    second = lattice.reflection(second_root) * first

    transporter = homset.transporter(first, second)

    assert transporter.parent() is homset.acting_group()
    assert homset.act(transporter, first) == second
    for generator in lattice.module_generators():
        assert transporter(first(generator)) == second(generator)

    back = homset.transporter(second, first)
    assert homset.act(back, second) == first
    assert back == ~transporter


def test_archived_identity_to_isometry_transporter_recovers_that_isometry() -> None:
    lattice = Lattices(ZZ)("A2")
    homset = lattice.Isom(lattice)
    identity = homset.identity()
    reflection = lattice.reflection(lattice.module_generators()[0])

    assert homset.transporter(identity, reflection) == reflection
    assert homset.transporter(reflection, identity) == ~reflection

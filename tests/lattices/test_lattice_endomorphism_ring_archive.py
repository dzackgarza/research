r"""Archive reconciliation for the endomorphism ring of a lattice.

A lattice is, in particular, a ``ZZ``-module.  Its endomorphism ring here is
therefore the module endomorphism ring; the orthogonal group is the separate
group of form-preserving automorphisms.  The archived audit requires that the
lattice reaches this ring through its ordinary ``End`` vocabulary.
"""

from dzack_research.preamble.all import ZZ, Lattices, Modules, module_homset


def test_lattice_end_is_the_underlying_module_endomorphism_ring() -> None:
    lattice = Lattices.A2
    endomorphisms = lattice.End()

    assert endomorphisms is Modules(ZZ).End(lattice)
    assert endomorphisms is lattice.module_category().Mor(lattice, lattice)


def test_lattice_endomorphism_ring_contains_nonisometric_module_maps() -> None:
    lattice = Lattices.A2
    endomorphisms = lattice.End()
    doubling = endomorphisms(
        lambda label: 2 * lattice.module_generator(label)
    )
    identity = endomorphisms.one()

    assert doubling.parent() is endomorphisms
    assert doubling != identity
    for generator in lattice.module_generators():
        assert doubling(generator) == 2 * generator
        assert (identity * doubling)(generator) == doubling(generator)
        assert (doubling * identity)(generator) == doubling(generator)

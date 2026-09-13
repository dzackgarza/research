r"""Nikulin genus-existence distinctions retained from the archive suite.

For the discriminant form of the negative-definite ``A2`` lattice, Milgram's
congruence separates the supported signatures used here.  The positive rows
are also realized by adjoining unimodular hyperbolic planes, which leaves the
discriminant form unchanged.
"""

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.lattices import Genus


def test_a2_discriminant_genus_exists_exactly_on_the_selected_nikulin_rows() -> None:
    discriminant = Lattices(ZZ)("A2").discriminant_group()
    expected = {
        (0, 2): True,
        (2, 0): False,
        (1, 3): True,
        (3, 1): False,
        (2, 4): True,
        (0, 6): False,
    }

    assert discriminant.brown_invariant() == 6
    for signature, exists in expected.items():
        genus = Genus(signature, discriminant)
        assert genus.exists() is exists
        assert ((signature[0] - signature[1]) % 8 == 6) is exists


def test_adjoining_hyperbolic_planes_realizes_the_positive_rows() -> None:
    discriminant = Lattices(ZZ)("A2").discriminant_group()

    assert Genus((1, 3), discriminant) == (Lattices(ZZ)("A2") + Lattices(ZZ)("U")).genus()
    assert Genus((2, 4), discriminant) == (
        Lattices(ZZ)("A2") + Lattices(ZZ)("U") + Lattices(ZZ)("U")
    ).genus()

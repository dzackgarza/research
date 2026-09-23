r"""Archive reconciliation for the torsor cardinality of ``Isom(L,M)``."""

from sage.misc.unknown import Unknown

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.sets.cardinals import cardinal


def test_empty_isometry_mor_has_cardinality_zero() -> None:
    even = Lattices(ZZ)("U")
    odd = Lattices(ZZ)([[1, 0], [0, -1]])

    isometries = even.Isom(odd)
    assert isometries.is_empty() is True
    assert isometries.cardinality() == cardinal(0)


def test_nonempty_isometry_mor_has_orthogonal_group_cardinality() -> None:
    lattice = Lattices(ZZ)("A2")
    isometries = lattice.Isom(lattice)

    assert isometries.is_empty() is False
    assert isometries.cardinality() == lattice.O().cardinality()


def test_unknown_isometry_mor_keeps_unknown_cardinality() -> None:
    source = Lattices(ZZ)([[1, 0], [0, -1]])
    change = ZZ.matrix_space(2, 2).from_rows([[1, 2], [0, 1]])
    target = Lattices(ZZ)(source.gram_tensor().pullback(change))
    isometries = source.Isom(target)

    assert isometries.is_empty() is Unknown
    assert isometries.cardinality() is Unknown

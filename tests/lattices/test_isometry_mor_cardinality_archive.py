r"""Archive reconciliation for the torsor cardinality of ``Isom(L,M)``."""


from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.sets.cardinals import cardinal


def test_empty_isometry_mor_has_cardinality_zero() -> None:
    even = Lattices(ZZ)("U")
    odd = Lattices(ZZ)([[1, 0], [0, -1]])

    isometries = even.Isom(odd)
    assert isometries.is_empty() is True
    assert isometries.cardinality() == cardinal(0)





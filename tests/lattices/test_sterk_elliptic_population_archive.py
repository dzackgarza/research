r"""Sterk connected elliptic-subdiagram populations retained from the archive.

The committed Sterk artifact directories contain one image for every connected
elliptic induced subdiagram, with the empty ``A_0`` diagram included as a
separate rank-zero convention.  The live Coxeter owner follows the ordinary
graph convention instead: ``elliptic_subdiagrams(connected=True)`` contains
only nonempty connected diagrams.  Thus the archived totals are one plus the
live connected counts.
"""

from dzack_research.preamble.all import Sterk


_ARCHIVED_TOTALS = {
    "Sterk_1": 121,
    "Sterk_2": 65,
    "Sterk_3": 67,
    "Sterk_4": 78,
    "Sterk_5": 119,
}


def test_sterk_connected_elliptic_populations_match_the_committed_archive() -> None:
    diagrams = Sterk.diagrams()
    assert set(diagrams) == set(_ARCHIVED_TOTALS)

    for name, expected_total in _ARCHIVED_TOTALS.items():
        diagram = diagrams[name]
        empty = diagram.induced_subdiagram(())
        connected = diagram.elliptic_subdiagrams(connected=True)

        assert empty.is_elliptic()
        assert not empty.is_connected()
        assert connected.cardinality() + 1 == expected_total
        assert all(subdiagram.is_elliptic() for subdiagram in connected)
        assert all(subdiagram.is_connected() for subdiagram in connected)

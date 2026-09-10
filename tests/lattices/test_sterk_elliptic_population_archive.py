r"""Sterk connected elliptic-subdiagram populations retained from the archive.

The committed Sterk artifact directories contain one image for every connected
elliptic induced subdiagram, with the empty ``A_0`` diagram included as a
separate rank-zero convention.  The live Coxeter owner follows the ordinary
graph convention instead: ``elliptic_subdiagrams(connected=True)`` contains
only nonempty connected diagrams.  Thus the archived totals are one plus the
live connected counts.
"""

import re
from collections import Counter
from pathlib import Path

import dzack_research

from dzack_research.preamble.all import Sterk


_ARTIFACTS = (
    Path(dzack_research.__file__).resolve().parent.parent.parent
    / "computations"
    / "enriques-paper-artifacts"
    / "Sterk"
)

_FILENAME = re.compile(
    r"elliptic_subdiagram_number_\d+_rank_(?P<rank>\d+)"
    r"_type_(?P<label>.+)_index_\d+\.png"
)


def _legacy_label(subdiagram) -> str:
    if subdiagram.cardinality() == 0:
        return "A_{0}"
    cartan, scale = subdiagram.scaled_cartan_type()
    letter = cartan.type()
    rank = cartan.rank()
    if letter in ("A", "D", "E"):
        if scale not in (1, 2):
            raise ArithmeticError(
                f"the archived Sterk labels have no {letter}_{rank} scale {scale}"
            )
        if scale == 1:
            return f"{letter}_{rank}"
        return f"{letter}_{rank}(2)"
    if scale != 1:
        raise ArithmeticError(
            f"the archived Sterk labels have no {letter}_{rank} scale {scale}"
        )
    if letter == "B":
        return f"B_{rank}(2)"
    if letter == "C" and rank == 2:
        return "G_2"
    if letter == "C":
        return f"C_{rank}(2)"
    raise ArithmeticError(f"the archived Sterk labels have no Cartan type {letter}_{rank}")


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


def test_sterk_artifact_rank_type_multisets_match_live_diagrams() -> None:
    diagrams = Sterk.diagrams()
    for name, expected_total in _ARCHIVED_TOTALS.items():
        parsed = []
        for path in sorted((_ARTIFACTS / name).iterdir()):
            match = _FILENAME.fullmatch(path.name)
            assert match is not None
            parsed.append((int(match.group("rank")), match.group("label")))
        archived = Counter(parsed)
        assert sum(archived.values()) == expected_total

        diagram = diagrams[name]
        empty = diagram.induced_subdiagram(())
        connected = diagram.elliptic_subdiagrams(connected=True)
        live = Counter(
            [(0, _legacy_label(empty))]
            + [
                (int(subdiagram.cardinality()), _legacy_label(subdiagram))
                for subdiagram in connected
            ]
        )
        assert sum(live.values()) == expected_total
        assert live == archived

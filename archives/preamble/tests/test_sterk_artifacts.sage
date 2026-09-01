r"""Sterk's elliptic-subdiagram artifacts are regenerated from the diagrams.

The five directories ``computations/enriques-paper-artifacts/Sterk/Sterk_k``
hold one committed PNG per connected elliptic induced subdiagram of Sterk's
five rooted Coxeter diagrams -- the fundamental-domain diagrams at the five
$0$-cusps of the Baily--Borel compactification of the degree-$2$ Enriques
moduli space, after Sterk's classification of those cusps, in the coordinates
the AEGS paper trail fixed (provenance of the root data, not a computed
input).  Each filename records the subdiagram's vertex count and the legacy
generator's type label::

    elliptic_subdiagram_number_N_rank_{r}_type_{T}_index_N.png

``number`` and ``index`` are a bookkeeping counter and carry no assertion.

The test enumerates the connected elliptic induced subdiagrams of each
diagram, the empty subdiagram included, labels each through the owned
recognition :meth:`scaled_cartan_type`, and asserts that the multiset of
``(vertex count, legacy label)`` pairs equals the multiset parsed from the
committed filenames.  The population totals are asserted against fixed
counts as an independent guard: an emptied or moved artifact directory
cannot pass vacuously.
"""

import re
from collections import Counter
from pathlib import Path

import pytest

import dzack_research

from dzack_research.preamble.install import install_preamble
install_preamble(globals())

# ``dzack_research`` is editable-installed from ``src/``, so the repo root is
# stable under QC's preparse tempdir where ``__file__`` is not.
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

# The committed artifact populations, one PNG per connected elliptic induced
# subdiagram, the empty subdiagram's rank-0 file included in each directory.
_EXPECTED_TOTALS = {
    "Sterk_1": 121,
    "Sterk_2": 65,
    "Sterk_3": 67,
    "Sterk_4": 78,
    "Sterk_5": 119,
}


def _legacy_label(subdiagram) -> str:
    r"""Return the label the legacy artifact generator wrote for a diagram.

    The fixed map from the owned ``(Cartan type, scale)`` recognition to the
    legacy filename vocabulary: ``(X_n, 1)`` is ``X_n`` and ``(X_n, 2)`` is
    ``X_n(2)`` for the simply-laced ``X``; ``(B_n, 1)`` is ``B_n(2)`` and
    ``(C_n, 1)`` is ``C_n(2)`` -- at scale 1 those types already contain
    square ``-4`` roots, which is what the legacy ``(2)`` recorded; the
    rank-two double-bond pair, ``(C_2, 1)`` in the owned spelling, was
    labeled ``G_2`` by the legacy generator; the empty diagram is ``A_{0}``.
    """
    if subdiagram.cardinality() == 0:
        return "A_{0}"
    cartan, scale = subdiagram.scaled_cartan_type()
    letter = cartan.type()
    rank = cartan.rank()
    if letter in ("A", "D", "E"):
        assert scale in (1, 2), (
            f"the legacy labels cover simply-laced scales 1 and 2 only; "
            f"found {letter}_{rank} at scale {scale}"
        )
        return f"{letter}_{rank}" if scale == 1 else f"{letter}_{rank}(2)"
    assert scale == 1, (
        f"the legacy labels cover B and C at scale 1 only; "
        f"found {letter}_{rank} at scale {scale}"
    )
    if letter == "B":
        return f"B_{rank}(2)"
    assert letter == "C", f"no legacy label exists for Cartan type {letter}_{rank}"
    if rank == 2:
        return "G_2"
    return f"C_{rank}(2)"


def _connected_elliptic_subdiagrams(diagram) -> list:
    r"""Return the connected elliptic induced subdiagrams, empty included.

    Connected candidates come from Sage's ``connected_subgraph_iterator`` on
    the diagram's Coxeter graph -- an induced subdiagram is connected exactly
    when its vertex set induces a connected subgraph there -- and ellipticity
    is then asked of each induced subdiagram itself.  The iterator yields
    nonempty vertex sets, so the empty subdiagram is adjoined directly.
    """
    subdiagrams = [diagram.subdiagram(())]
    for vertices in diagram.graph().connected_subgraph_iterator(vertices_only=True):
        subdiagram = diagram.subdiagram(tuple(sorted(vertices)))
        if subdiagram.is_elliptic():
            subdiagrams.append(subdiagram)
    return subdiagrams


def test_the_empty_subdiagram_is_connected_elliptic_and_labeled_a0() -> None:
    r"""The empty subdiagram is the ``A_{0}`` member of every enumeration.

    The conventions the population count leans on, asserted once: the empty
    induced subdiagram of a rooted Sterk diagram is connected (Sage's
    empty-graph convention), elliptic (the trivial Coxeter group is finite),
    not parabolic, realizes no Cartan type, and carries the legacy label
    ``A_{0}``.
    """
    empty = SterkDiagrams.Sterk_1.subdiagram(())

    assert empty.cardinality() == 0
    assert empty.is_connected()
    assert empty.is_elliptic()
    assert not empty.is_parabolic()
    assert empty.scaled_cartan_type() is None
    assert _legacy_label(empty) == "A_{0}"


@pytest.mark.parametrize("name", sorted(_EXPECTED_TOTALS))
def test_connected_elliptic_subdiagrams_reproduce_the_committed_artifacts(
    name: str,
) -> None:
    r"""Enumeration and recognition reproduce the committed PNG population."""
    parsed = []
    for path in sorted((_ARTIFACTS / name).iterdir()):
        match = _FILENAME.fullmatch(path.name)
        assert match is not None, f"unrecognized artifact filename {path.name!r}"
        parsed.append((Integer(match.group("rank")), match.group("label")))
    artifact_population = Counter(parsed)
    assert sum(artifact_population.values()) == _EXPECTED_TOTALS[name]

    subdiagrams = _connected_elliptic_subdiagrams(getattr(SterkDiagrams, name))
    # ``finite_value()`` keys the multiset on the same ``Integer`` type the
    # filename parse produces.
    enumerated_population = Counter(
        (subdiagram.cardinality().finite_value(), _legacy_label(subdiagram))
        for subdiagram in subdiagrams
    )
    assert sum(enumerated_population.values()) == _EXPECTED_TOTALS[name]
    assert enumerated_population == artifact_population

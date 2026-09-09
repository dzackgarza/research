r"""Recorded ``(r,a,delta)`` invariants from the archived Oscar verification notebook.

The notebook computed these rows from the discriminant quadratic form of the
six period lattices.  The live owner already implements Nikulin's invariant;
this archive specimen preserves the recorded mathematical table rather than
porting the notebook's temporary Oscar helper.
"""

from dzack_research.preamble.all import NamedLattices, nikulin_invariants


def test_archived_period_lattices_retain_the_recorded_two_elementary_rows() -> None:
    expected = {
        "Sdp": (2, 2, 0),
        "SEn": (10, 10, 0),
        "LpNik": (14, 8, 0),
        "TdP": (20, 2, 0),
        "TEn": (12, 10, 0),
        "LmNik": (8, 8, 0),
    }

    for name, (rank, length, delta) in expected.items():
        lattice = getattr(NamedLattices, name)
        assert lattice.two_elementary_invariants() == nikulin_invariants(
            rank,
            length,
            delta,
        )


def test_all_six_archived_period_rows_are_coeven() -> None:
    for name in ("Sdp", "SEn", "LpNik", "TdP", "TEn", "LmNik"):
        invariants = getattr(NamedLattices, name).two_elementary_invariants()
        assert invariants.delta() == 0

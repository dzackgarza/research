r"""Archive reconciliation for the named lattice catalogue.

These are identity and invariant assertions from the historical session
surface.  They remain mathematical facts of the current catalogue; no legacy
constructor wrapper is needed to state them.
"""

from dzack_research.preamble.catalogue import NamedLattices


def test_named_period_lattices_retain_their_defining_rank_and_signature() -> None:
    expected = {
        "U": (2, (1, 1)),
        "U_2": (2, (1, 1)),
        "E8": (8, (0, 8)),
        "E8_2": (8, (0, 8)),
        "E10": (10, (1, 9)),
        "E10_2": (10, (1, 9)),
        "LK3": (22, (3, 19)),
        "SEn": (10, (1, 9)),
        "TEn": (12, (2, 10)),
        "LpNik": (14, (3, 11)),
        "LmNik": (8, (0, 8)),
        "TdP": (20, (2, 18)),
        "L_20_2_0": (20, (2, 18)),
    }

    for name, (rank, signature) in expected.items():
        lattice = getattr(NamedLattices, name)
        actual_signature = lattice.signature_pair()
        assert int(lattice.module_rank()) == rank
        assert actual_signature.first() == signature[0]
        assert actual_signature.second() == signature[1]





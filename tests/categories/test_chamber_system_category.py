r"""Chamber-system owners retain typed equivalence relations."""

import pytest

from dzack_research.preamble.categories.chamber_systems import ChamberSystems


def test_finite_chamber_system_retains_typed_adjacency() -> None:
    system = ChamberSystems().from_adjacencies(
        (0, 1),
        ("s",),
        {"s": ((0, 0), (0, 1), (1, 0), (1, 1))},
    )

    assert system in ChamberSystems()
    assert system.is_adjacent(0, "s", 1)


def test_typed_adjacency_must_be_an_equivalence_relation() -> None:
    with pytest.raises(ValueError, match="symmetric"):
        ChamberSystems().from_adjacencies(
            (0, 1),
            ("s",),
            {"s": ((0, 0), (1, 1), (0, 1))},
        )

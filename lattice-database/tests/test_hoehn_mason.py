"""The coinvariant records are the coinvariant lattices of Höhn and Mason, their groups have the orders of Table 10.2 of Hashimoto, and the morphism files hold their maps; a false entry is refused."""

from pathlib import Path

import pytest
from latticedb import corpus, hashimoto, hoehn_mason

REPOSITORY = Path(__file__).resolve().parent.parent
LOADED = corpus.load(REPOSITORY)
LATTICES = {entry.lattice.tag: entry.lattice for entry in LOADED.entries}
HELD = corpus.held(LOADED)
GROUPS, _ = hashimoto.stored(REPOSITORY / "sources" / "hashimoto")
LEECH, ENTRIES = hoehn_mason.stored(REPOSITORY / "sources" / "hoehn_mason")


def test_the_stored_entries_agree_with_the_records_table_10_2_and_the_morphism_files() -> None:
    assert len(ENTRIES) == 40
    assert hoehn_mason.check(LEECH, ENTRIES, GROUPS, LATTICES, HELD) == []


def test_the_group_order_is_the_order_of_the_closure() -> None:
    # The rotation by a quarter turn generates the cyclic group of order 4.
    assert hoehn_mason.group_order([((0, -1), (1, 0))]) == 4


Change = dict[str, int | tuple[corpus.Matrix, ...]]


def _replace(index: int, change: Change) -> tuple[hoehn_mason.Entry, ...]:
    return tuple(entry.model_copy(update=change) if k == index else entry for k, entry in enumerate(ENTRIES))


def test_a_generator_that_does_not_fix_the_fixed_point_lattice_is_refused() -> None:
    # The negation of the Leech lattice is an isometry that moves every vector of B.
    index, entry = next((k, entry) for k, entry in enumerate(ENTRIES) if entry.record == "02AQ")
    negation = tuple(tuple(-int(r == c) for c in range(24)) for r in range(24))
    entries = _replace(index, {"stabilizer_generators": (*entry.stabilizer_generators, negation)})
    assert any("not an isometry of leech[1] that fixes B" in problem for problem in hoehn_mason.check(LEECH, entries, GROUPS, LATTICES, HELD))


def test_a_group_of_the_wrong_order_is_refused() -> None:
    # Row 81 of Table 10.2 states |G| = 960; the first generator alone generates a proper subgroup.
    index, entry = next((k, entry) for k, entry in enumerate(ENTRIES) if entry.row == 81)
    entries = _replace(index, {"stabilizer_generators": entry.stabilizer_generators[:1]})
    problems = hoehn_mason.check(LEECH, entries, GROUPS, LATTICES, HELD)
    assert any("Table 10.2 row 81 states |G| = 960" in problem for problem in problems)


@pytest.mark.parametrize("twist", [2, -1])
def test_a_basis_that_is_not_an_isometry_is_refused(twist: int) -> None:
    index, _ = next((k, entry) for k, entry in enumerate(ENTRIES) if entry.record == "02AQ")
    entries = _replace(index, {"twist": twist})
    assert any("is not an isometry from 02AQ" in problem for problem in hoehn_mason.check(LEECH, entries, GROUPS, LATTICES, HELD))

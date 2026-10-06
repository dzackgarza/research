"""Stored transcription of the Höhn--Mason Leech-lattice ancillary file.

G. Höhn and G. Mason, "The 290 fixed-point sublattices of the Leech lattice",
arXiv:1505.06420.  This module parses the archived source and its card/tag
locators only. Coordinate changes, isometries, stabilizer actions and group
orders are mathematical computations owned by the research preamble.
"""

from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter

from latticedb.corpus import Matrix
from latticedb.model import Tag


class Leech(BaseModel):
    """The stored ``leech[1]`` source datum and its card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    basis: Matrix
    inner_product: tuple[tuple[str, ...], ...]
    record: Tag
    record_basis: Matrix


class Entry(BaseModel):
    """One stored ``lattices[i,j]`` source datum and its card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    i: int
    j: int
    coinvariant_basis: Matrix
    fixed_basis: Matrix
    stabilizer_generators: tuple[Matrix, ...]
    row: int
    record: Tag
    twist: int
    record_basis: Matrix


def stored(directory: Path) -> tuple[Leech, tuple[Entry, ...]]:
    """Return the archived Leech datum and all ancillary entries."""
    leech = Leech.model_validate_json((directory / "leech.json").read_text())
    entries = tuple(
        TypeAdapter(Entry).validate_json(path.read_text())
        for path in sorted(directory.glob("lattices_*.json"))
    )
    return leech, entries

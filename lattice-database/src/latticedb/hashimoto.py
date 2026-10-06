"""Stored transcription of Tables 10.2 and 10.3 of Hashimoto.

K. Hashimoto, "Finite symplectic actions on the K3 lattice", arXiv:1012.2682.
This module is source intake only: it parses the archived transcription and its
card/tag locators.  Mathematical verification of the stated lattices, forms,
embeddings and complements belongs to the research preamble, not to latticedb.
"""

import re
from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter

from latticedb.model import Tag

_SYMBOL = re.compile(r"(\d+)(?:_(?:II|\d))?\^\{([+-])(\d+)\}")


class Twist(BaseModel):
    """A record ``R`` and nonzero integer ``t`` naming the source lattice ``R(t)``."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    record: Tag
    twist: int


class GroupRow(BaseModel):
    """One stored row of Table 10.2."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    n: int
    order: int
    small_group: int
    group: str
    discriminant_order: int
    discriminant_form: str | None
    shares: int | None
    rank: int
    coinvariant: Twist | None = None


class InvariantLattice(BaseModel):
    """One printed Gram tensor of Table 10.3 and its stored card locator."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    gram_tensor: tuple[tuple[int, ...], ...]
    record: Tag
    twist: int
    basis: tuple[tuple[int, ...], ...]


class InvariantRow(BaseModel):
    """One stored row of Table 10.3."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    n: int
    lattices: tuple[InvariantLattice, ...]


def stored(directory: Path) -> tuple[tuple[GroupRow, ...], tuple[InvariantRow, ...]]:
    """Return Tables 10.2 and 10.3 exactly as stored under ``directory``."""
    groups = TypeAdapter(tuple[GroupRow, ...]).validate_json(
        (directory / "table_10_2.json").read_text()
    )
    invariants = TypeAdapter(tuple[InvariantRow, ...]).validate_json(
        (directory / "table_10_3.json").read_text()
    )
    return groups, invariants


def symbol_group(symbol: str) -> list[int]:
    """Parse the prime-power cyclic-factor orders printed in a genus symbol."""
    terms = [term.strip() for term in symbol.split(",")]
    found = [_SYMBOL.fullmatch(term) for term in terms]
    if not all(found):
        raise ValueError(f"{symbol!r} is not a stored Hashimoto genus symbol")
    return sorted(
        int(match[1])
        for match in found
        if match is not None
        for _ in range(int(match[3]))
    )

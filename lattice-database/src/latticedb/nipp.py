"""Exact form presentations in Gordon Nipp's quaternary and quinary tables."""

import re
from dataclasses import dataclass
from fractions import Fraction
from html import unescape
from pathlib import Path

from latticedb.bulk_sources import NIPP_QUATERNARY, NIPP_QUINARY

QUATERNARY_PAIRS = ((0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3))
QUINARY_PAIRS = (*QUATERNARY_PAIRS, (0, 4), (1, 4), (2, 4), (3, 4))
_PRE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.IGNORECASE | re.DOTALL)
_INTEGER = re.compile(r"-?\d+")
_HEADER = re.compile(r"D=\s*(\d+);\s*GENUS#\s*(\d+);\s*MASS=\s*(\d+)/\s*(\d+);\s*HASSE SYMBOLS ARE\s*(.*)")


@dataclass(frozen=True)
class NippEntry:
    source_file: str
    source_line: int
    rank: int
    discriminant: int
    genus: int
    coefficients: tuple[int, ...]
    hasse_symbols: tuple[int, ...]
    level: int | None
    automorphism_group_order: int
    mass: Fraction

    @property
    def gram_tensor(self) -> tuple[tuple[int, ...], ...]:
        """The integral bilinear form associated with the source's quadratic polynomial."""
        matrix = [[2 * self.coefficients[i] if i == j else 0 for j in range(self.rank)] for i in range(self.rank)]
        pairs = QUATERNARY_PAIRS if self.rank == 4 else QUINARY_PAIRS
        for (i, j), coefficient in zip(pairs, self.coefficients[self.rank :], strict=True):
            matrix[i][j] = matrix[j][i] = coefficient
        return tuple(tuple(row) for row in matrix)


def _lines(path: Path) -> list[str]:
    page = path.read_text(encoding="latin-1")
    blocks = _PRE.findall(page)
    assert len(blocks) == 1, f"{path}: expected one table"
    return unescape(blocks[0]).splitlines()


def quaternary(path: Path) -> list[NippEntry]:
    """Read one table of primitive positive-definite quaternary forms."""
    entries: list[NippEntry] = []
    for line_number, line in enumerate(_lines(path), start=1):
        if not re.match(r"^\s*\d+\s+\d+\s+\d+", line):
            continue
        values = tuple(int(token) for token in _INTEGER.findall(line))
        assert len(values) >= 16, f"{path}:{line_number}: incomplete form row"
        discriminant, genus = values[:2]
        coefficients = values[2:12]
        hasse_symbols = values[12:-4]
        level, order, mass_numerator, mass_denominator = values[-4:]
        assert all(symbol in (-1, 1) for symbol in hasse_symbols), f"{path}:{line_number}: invalid Hasse symbol"
        entries.append(NippEntry(path.name, line_number, 4, discriminant, genus, coefficients, hasse_symbols, level, order, Fraction(mass_numerator, mass_denominator)))
    return entries


def quinary(path: Path) -> list[NippEntry]:
    """Read one table of primitive positive-definite quinary forms."""
    entries: list[NippEntry] = []
    discriminant = genus = 0
    mass = Fraction(0)
    hasse_symbols: tuple[int, ...] = ()
    for line_number, line in enumerate(_lines(path), start=1):
        if line.startswith("D="):
            header = _HEADER.fullmatch(line.strip())
            assert header is not None, f"{path}:{line_number}: invalid genus header"
            discriminant, genus, numerator, denominator = (int(header.group(i)) for i in range(1, 5))
            mass = Fraction(numerator, denominator)
            hasse_symbols = tuple(int(token) for token in _INTEGER.findall(header.group(5)))
            assert all(symbol in (-1, 1) for symbol in hasse_symbols)
            continue
        if not re.match(r"^\s*\d+\s+\d+\s+\d+", line):
            continue
        coefficients, separator, order = line.partition(";")
        assert separator and discriminant > 0, f"{path}:{line_number}: form without genus"
        values = tuple(int(token) for token in _INTEGER.findall(coefficients))
        assert len(values) == 15, f"{path}:{line_number}: expected 15 coefficients"
        entries.append(NippEntry(path.name, line_number, 5, discriminant, genus, values, hasse_symbols, None, int(order), mass))
    return entries


def stored(directory: Path) -> list[NippEntry]:
    """Read the complete stored Nipp source tables."""
    return [entry for name in NIPP_QUATERNARY for entry in quaternary(directory / name)] + [entry for name in NIPP_QUINARY for entry in quinary(directory / name)]

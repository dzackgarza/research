"""Representatives of primitive single-class genera in Watson's source table."""

import re
from dataclasses import dataclass
from pathlib import Path

_DIMENSION = re.compile(r"// dimension (\d+): (\d+) lattices")


@dataclass(frozen=True)
class WatsonEntry:
    source_line: int
    dimension: int
    ordinal: int
    lower_triangle: tuple[int, ...]

    @property
    def gram_tensor(self) -> tuple[tuple[int, ...], ...]:
        """The symmetric tensor printed by its lower-triangular components."""
        lower = [self.lower_triangle[i * (i + 1) // 2 : (i + 1) * (i + 2) // 2] for i in range(self.dimension)]
        return tuple(tuple(lower[max(i, j)][min(i, j)] for j in range(self.dimension)) for i in range(self.dimension))


def stored(path: Path) -> list[WatsonEntry]:
    """Read every dimension block and check its stated row count."""
    entries: list[WatsonEntry] = []
    dimension = expected = ordinal = 0
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if match := _DIMENSION.fullmatch(line):
            if dimension:
                assert ordinal == expected, f"dimension {dimension}: found {ordinal} rows, expected {expected}"
            dimension, expected = int(match.group(1)), int(match.group(2))
            ordinal = 0
            continue
        if line.startswith("//") or not line.strip():
            continue
        assert dimension > 0, f"{path}:{line_number}: form without dimension"
        values = tuple(int(token) for token in line.split())
        assert len(values) == dimension * (dimension + 1) // 2, f"{path}:{line_number}: incorrect row length"
        ordinal += 1
        entries.append(WatsonEntry(line_number, dimension, ordinal, values))
    assert ordinal == expected, f"dimension {dimension}: found {ordinal} rows, expected {expected}"
    return entries

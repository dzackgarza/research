"""The odd and even ternary forms in the Brandt–Intrau–Schiemann tables."""

import re
from dataclasses import dataclass
from html import unescape
from pathlib import Path

from latticedb.model import Yaml

_PRE = re.compile(r"<pre[^>]*>(.*?)</pre>", re.IGNORECASE | re.DOTALL)
_DISCRIMINANT = re.compile(r"B\.-I\.discr\s*=\s*(-\d+)")
_FORM = re.compile(r"\s*(\d+):\s*(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s*")


@dataclass(frozen=True)
class BrandtIntrauEntry:
    source_file: str
    source_line: int
    source_number: int
    discriminant: int
    coefficients: tuple[int, int, int, int, int, int]
    odd_form: bool

    @property
    def gram_tensor(self) -> tuple[tuple[int, ...], ...]:
        """The lattice Gram tensor under the source's odd/even convention."""
        a1, a2, a3, a4, a5, a6 = self.coefficients
        if self.odd_form:
            assert a4 % 2 == a5 % 2 == a6 % 2 == 0
            return ((a1, a6 // 2, a5 // 2), (a6 // 2, a2, a4 // 2), (a5 // 2, a4 // 2, a3))
        return ((2 * a1, a6, a5), (a6, 2 * a2, a4), (a5, a4, 2 * a3))


def table(path: Path, *, odd_form: bool) -> list[BrandtIntrauEntry]:
    """Read each numbered ternary form and its stated discriminant."""
    page = path.read_text(encoding="latin-1")
    blocks = _PRE.findall(page)
    assert len(blocks) == 1, f"{path}: expected one table"
    discriminant = 0
    entries: list[BrandtIntrauEntry] = []
    for line_number, line in enumerate(unescape(blocks[0]).splitlines(), start=1):
        if match := _DISCRIMINANT.search(line):
            discriminant = int(match.group(1))
            continue
        match = _FORM.fullmatch(line)
        if match is None:
            continue
        assert discriminant < 0, f"{path}:{line_number}: form without discriminant"
        number, *coefficients = (int(value) for value in match.groups())
        entries.append(BrandtIntrauEntry(path.name, line_number, number, discriminant, tuple(coefficients), odd_form))
    return entries


def stored(directory: Path) -> list[BrandtIntrauEntry]:
    """Read both parity tables from the stored source pages."""
    return table(directory / "Brandt_1.html", odd_form=True) + table(directory / "Brandt_2.html", odd_form=False)


def record(entry: BrandtIntrauEntry) -> tuple[dict[str, Yaml], str]:
    """State one numbered ternary form as a lattice record's declared fields."""
    locator = f"{entry.source_file}:{entry.source_number}"
    name = f"Brandt–Intrau–Schiemann form {locator}"
    declared: dict[str, Yaml] = {
        "name": name,
        "latex": name,
        "aliases": [],
        "gram_tensor": [list(row) for row in entry.gram_tensor],
        "families": [],
        "related": [],
        "references": [{"citation": f"Brandt–Intrau–Schiemann ternary form table, {locator}.", "url": f"https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES/{entry.source_file}"}],
    }
    prose = f"The Gram tensor is the integral bilinear form of form {entry.source_number} in `{entry.source_file}`."
    return declared, prose

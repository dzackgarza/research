"""Entries of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane) as records.

Each entry page lists sections `NAME`, `DIMENSION`, `DET`, `MINIMAL_NORM`,
`KISSING_NUMBER`, `REFERENCES` and `GRAM`. The `GRAM` section gives the rank
and then the components `b(e_i, e_j)`, row by row, for all `j` or for `j <= i`.
`fetch` reads an entry page into an `Entry`; `sources/nebe_sloane/<NAME>.json`
stores it. `record` writes the entry as the declared fields of a record, and
`records.derive` computes the rest; `check` compares the invariants that the
catalogue states with the computed ones.
"""

import re
from decimal import Decimal
from fractions import Fraction
from html import unescape
from pathlib import Path
from urllib.request import urlopen

from pydantic import BaseModel, ConfigDict

from latticedb.model import Yaml

CATALOGUE = "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES"
FAMILY = "nebe-sloane-catalogue"
_SECTION = re.compile(r'<a NAME="([^"]+)"><STRONG>[^<]*</STRONG></a><br>\n(.*?)(?=<p><li>|</ul>)', re.DOTALL)


class Entry(BaseModel):
    """What an entry page of the catalogue states."""

    model_config = ConfigDict(strict=True, extra="forbid", frozen=True)

    name: str
    title: str
    url: str
    dimension: int
    determinant: int
    minimal_norm: int
    kissing_number: int
    references: tuple[str, ...]
    gram_tensor: tuple[tuple[int, ...], ...]


def sections(page: str) -> dict[str, list[str]]:
    """Section name -> its lines, without markup."""
    return {name: [unescape(re.sub(r"<[^>]+>", "", line)).strip() for line in body.split("<br>") if line.strip()] for name, body in _SECTION.findall(page)}


def integer(token: str) -> int:
    """Read `4` or `.400000000000E+01`: some entries print their integers in scientific notation."""
    value = Fraction(Decimal(token))
    assert value.denominator == 1, f"{token} is not an integer"
    return value.numerator


def components(lines: list[str]) -> tuple[tuple[int, ...], ...]:
    """The full symmetric array of components from the `GRAM` section."""
    rank = int(lines[0].split()[0])
    values = [integer(token) for line in lines[1:] for token in line.split()]
    if len(values) == rank * rank:
        full = [tuple(values[i * rank : (i + 1) * rank]) for i in range(rank)]
        assert all(full[i][j] == full[j][i] for i in range(rank) for j in range(i)), "the full array is not symmetric"
        return tuple(full)
    assert len(values) == rank * (rank + 1) // 2, f"expected {rank} rows, full or lower triangular, found {len(values)} values"
    lower = [values[i * (i + 1) // 2 : (i + 1) * (i + 2) // 2] for i in range(rank)]
    return tuple(tuple(lower[max(i, j)][min(i, j)] for j in range(rank)) for i in range(rank))


def fetch(name: str) -> Entry:
    """Read the entry page of the catalogue."""
    url = f"{CATALOGUE}/{name}.html"
    with urlopen(url) as response:
        found = sections(response.read().decode("latin-1"))
    return Entry(
        name=name,
        title=" ".join(found["NAME"]),
        url=url,
        dimension=int(found["DIMENSION"][0]),
        determinant=integer(found["DET"][0]),
        minimal_norm=integer(found["MINIMAL_NORM"][0]),
        kissing_number=integer(found["KISSING_NUMBER"][0]),
        references=tuple(found.get("REFERENCES", [])),
        gram_tensor=components(found["GRAM"]),
    )


def stored(directory: Path, name: str) -> Entry:
    """The entry from `directory/<name>.json`, fetched and stored there first when the file does not exist."""
    path = directory / f"{name}.json"
    if not path.exists():
        directory.mkdir(parents=True, exist_ok=True)
        path.write_text(fetch(name).model_dump_json(indent=1) + "\n")
    return Entry.model_validate_json(path.read_text())


def record(entry: Entry, name: str, latex: str, aliases: tuple[str, ...], families: tuple[str, ...]) -> tuple[dict[str, Yaml], str]:
    """The declared fields of the record of an entry, without a tag, and its prose. `records.derive` computes the other fields."""
    fields: dict[str, Yaml] = {
        "name": name,
        "latex": latex,
        "aliases": [entry.name, *(alias for alias in aliases if alias != entry.name)],
        "gram_tensor": [list(row) for row in entry.gram_tensor],
        "families": [FAMILY, *(family for family in families if family != FAMILY)],
        "related": [],
        "references": [{"citation": f"G. Nebe and N. J. A. Sloane, Catalogue of Lattices, entry {entry.name}.", "url": entry.url}],
    }
    prose = f"The components $b(e_i, e_j)$ are those of the section `GRAM` of the entry `{entry.name}` of the Catalogue of Lattices."
    if entry.references:
        prose += "\n\nThe catalogue entry gives this reference text: " + " ".join(entry.references)
    return fields, prose


def check(entry: Entry, derived: dict[str, Yaml]) -> None:
    """Assert that the invariants the catalogue states are the computed ones."""
    definite = derived["definite"]
    match definite:
        case dict():
            pass
        case _:
            raise AssertionError(f"the entry {entry.name} is not definite")
    stated = {"rank": entry.dimension, "determinant": entry.determinant, "minimum": entry.minimal_norm, "kissing_number": entry.kissing_number}
    computed = {"rank": derived["rank"], "determinant": derived["determinant"], "minimum": definite["minimum"], "kissing_number": definite["kissing_number"]}
    assert stated == computed, f"the entry {entry.name} states {stated}, the Gram tensor gives {computed}"

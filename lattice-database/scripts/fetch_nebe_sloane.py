# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///
"""Fetch entries of the Catalogue of Lattices (G. Nebe, N. J. A. Sloane) into `scripts/nebe_sloane/<NAME>.json`.

Usage: uv run scripts/fetch_nebe_sloane.py

Each entry page lists sections `NAME`, `DIMENSION`, `DET`, `MINIMAL_NORM`,
`KISSING_NUMBER`, `REFERENCES` and `GRAM`. The `GRAM` section gives the rank
and then the components `b(e_i, e_j)`, row by row, for all `j` or for `j <= i`. The seed
script reads these files and checks every stated invariant again.
"""

import json
import re
from decimal import Decimal
from fractions import Fraction
from html import unescape
from pathlib import Path
from urllib.request import urlopen

CATALOGUE = "https://www.math.rwth-aachen.de/~Gabriele.Nebe/LATTICES"
ENTRIES = ("K12", "BW16", *(f"LAMBDA{n}" for n in range(9, 21)), *(f"KAPPA{n}" for n in (7, 8, 9)))
SECTION = re.compile(r'<a NAME="([^"]+)"><STRONG>[^<]*</STRONG></a><br>\n(.*?)(?=<p><li>|</ul>)', re.DOTALL)


def sections(page: str) -> dict[str, list[str]]:
    """Section name -> its lines, without markup."""
    return {name: [unescape(re.sub(r"<[^>]+>", "", line)).strip() for line in body.split("<br>") if line.strip()] for name, body in SECTION.findall(page)}


def integer(token: str) -> int:
    """Read `4` or `.400000000000E+01`: some entries print their integers in scientific notation."""
    value = Fraction(Decimal(token))
    assert value.denominator == 1, f"{token} is not an integer"
    return value.numerator


def components(lines: list[str]) -> list[list[int]]:
    """The full symmetric array of components from the `GRAM` section."""
    rank = int(lines[0].split()[0])
    values = [integer(token) for line in lines[1:] for token in line.split()]
    if len(values) == rank * rank:
        full = [values[i * rank : (i + 1) * rank] for i in range(rank)]
        assert all(full[i][j] == full[j][i] for i in range(rank) for j in range(i)), "the full array is not symmetric"
        return full
    assert len(values) == rank * (rank + 1) // 2, f"expected {rank} rows, full or lower triangular, found {len(values)} values"
    lower = [values[i * (i + 1) // 2 : (i + 1) * (i + 2) // 2] for i in range(rank)]
    return [[lower[max(i, j)][min(i, j)] for j in range(rank)] for i in range(rank)]


def entry(name: str) -> dict[str, str | int | list[str] | list[list[int]]]:
    url = f"{CATALOGUE}/{name}.html"
    with urlopen(url) as response:
        found = sections(response.read().decode("latin-1"))
    return {
        "name": name,
        "title": " ".join(found["NAME"]),
        "url": url,
        "dimension": int(found["DIMENSION"][0]),
        "determinant": integer(found["DET"][0]),
        "minimal_norm": integer(found["MINIMAL_NORM"][0]),
        "kissing_number": integer(found["KISSING_NUMBER"][0]),
        "references": found.get("REFERENCES", []),
        "gram_tensor": components(found["GRAM"]),
    }


def main() -> None:
    target = Path(__file__).parent / "nebe_sloane"
    target.mkdir(exist_ok=True)
    for name in ENTRIES:
        (target / f"{name}.json").write_text(json.dumps(entry(name), indent=1) + "\n")
        print(name)


if __name__ == "__main__":
    main()

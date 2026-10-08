"""The tables of regular and spinor regular positive ternary forms, with what each row's source proves."""

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from latticedb.model import Yaml

SOURCES = Path(__file__).resolve().parents[2] / "sources"
REGULAR = SOURCES / "jagy_kaplansky_schiemann" / "regular_ternaries.txt"
SPINOR_REGULAR = SOURCES / "earnest_haensch" / "spinor_regular_ternaries.txt"

_JKS97 = "W. C. Jagy, I. Kaplansky and A. Schiemann, There are 913 regular ternary forms, Mathematika 44 (1997), 332-341"
_DMPW19 = (
    "A. G. Doyle, B. Muskat, K. Pehlivan and K. S. Williams, Positive integers represented by regular primitive "
    "positive-definite integral ternary quadratic forms, Integers 19 (2019), #A45, Tables 1 and 2"
)
_EH18 = "A. G. Earnest and A. Haensch, Completeness of the list of spinor regular ternary quadratic forms, arXiv:1711.05811v2 (2018)"
_PROOFS = {
    "JKS97": f"regular by {_JKS97}",
    "Oh11": "regular by B.-K. Oh, Regular positive ternary quadratic forms, Acta Arith. 147 (2011), 233-243",
    "LO14": (
        "regular under the generalized Riemann hypothesis by R. J. Lemke Oliver, Representations by ternary quadratic forms, "
        "Bull. London Math. Soc. 46 (2014), 1237-1247, Theorem 1.1"
    ),
    "one-class": "its spinor genus has one class",
    "BEHH90": "spinor regular by J. W. Benham, A. G. Earnest, J. S. Hsia and D. C. Hung, Spinor regular positive ternary quadratic forms, J. London Math. Soc. 42 (1990), 1-10",
}
_URLS = {REGULAR: "https://math.colgate.edu/~integers/t45/t45.pdf", SPINOR_REGULAR: "https://arxiv.org/abs/1711.05811v2"}


@dataclass(frozen=True)
class TernaryEntry:
    """One row: the form ax^2 + by^2 + cz^2 + dyz + ezx + fxy and the source that proves its property."""

    table: Path
    row: int
    coefficients: tuple[int, int, int, int, int, int]
    proof: str

    @property
    def gram_tensor(self) -> list[list[int]]:
        """The Gram tensor of the even lattice with b(x, x) = 2Q(x), as the source's coefficients print it."""
        a, b, c, d, e, f = self.coefficients
        return [[2 * a, f, e], [f, 2 * b, d], [e, d, 2 * c]]

    @property
    def proved(self) -> Literal[True, "true under GRH"]:
        """The table's property of the form: regular, or spinor regular, unconditionally or under GRH."""
        match self.proof:
            case "LO14":
                return "true under GRH"
            case _:
                return True

    @property
    def field(self) -> Literal["regular", "spinor_regular"]:
        """The card field whose value the table proves."""
        return "regular" if self.table == REGULAR else "spinor_regular"

    @property
    def reference(self) -> dict[str, str]:
        """The citation of this row, with its locator and the proof of its property."""
        listing = f"{_JKS97}, form {self.row}, as tabulated in {_DMPW19}" if self.table == REGULAR else f"{_EH18}, Table 1, row {self.row}"
        return {"citation": f"{listing}; {_PROOFS[self.proof]}.", "url": _URLS[self.table]}


def stored(table: Path) -> list[TernaryEntry]:
    """Read every row of one stored table."""
    entries: list[TernaryEntry] = []
    for line_number, line in enumerate(table.read_text().splitlines(), start=1):
        if line.startswith("//") or not line.strip():
            continue
        row, a, b, c, d, e, f, proof = line.split()
        assert proof in _PROOFS, f"{table}:{line_number}: unknown proof {proof}"
        entries.append(TernaryEntry(table, int(row), (int(a), int(b), int(c), int(d), int(e), int(f)), proof))
    assert [entry.row for entry in entries] == list(range(1, len(entries) + 1)), f"{table}: rows are not numbered 1 to {len(entries)}"
    return entries


def requested() -> list[dict[str, Yaml]]:
    """Every row of both tables, as `latticedb certify` sends it to the preamble adapter."""
    return [
        {"field": entry.field, "gram": entry.gram_tensor, "proved": entry.proved, "reference": entry.reference, "locator": f"{entry.table.parent.name} row {entry.row}"}
        for table in (REGULAR, SPINOR_REGULAR)
        for entry in stored(table)
    ]

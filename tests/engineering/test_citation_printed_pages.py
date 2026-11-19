"""Citations that name a numbered statement must also name its printed page.

The repository's standard, quoted verbatim in every issue brief: "Every mathematical statement you
write cites a published source by authors, numbered statement and printed page, or a lattice-database
card or Lean declaration; a page proof certifies nothing by itself."  Nothing checked it until now,
and the gap it names is open at exactly one place.

The open one, decided blocked rather than repaired:

    writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md
    cites [@Gur99, Theorem D] -- Guralnick, *Small representations are completely reducible*,
    J. Algebra 220 (1999) 531--541, doi 10.1006/jabr.1999.7963 -- with no printed page.

The page cannot be supplied from here: the article is in no `tmp/sources` tree, it has no arXiv
version (`export.arxiv.org` title query: 0 results), and Crossref's registered record gives the
article's pages, 531--541, but not the page a theorem letter falls on.  The entry itself exists
(`writing/coble/coble_supplement.bib`, `Gur99`), so this is a citation needing one number, not a
missing reference.

So the two tests below are a sentinel pair rather than a red suite: the first pins the gap as it
stands, and the second fails the moment the gap becomes stale -- when a page number appears, or when
another page starts citing `Gur99`.  A suite that is red on main is not a record of anything; a
suite that goes red on the change that resolves or duplicates the gap is.

Run: python3 tests/engineering/test_citation_printed_pages.py     (or pytest)
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
SUPPLEMENT = ROOT / "writing/coble/coble_supplement.bib"

# The one citation whose printed page is owed, and the source that would supply it.
MISSING_SOURCE = (
    "Guralnick, R. M., Small Representations Are Completely Reducible, "
    "Journal of Algebra 220 (1999) 531-541, doi 10.1006/jabr.1999.7963"
)
OWED = "Gur99"

# Any `@key, ...Theorem D...` citation, with whatever follows it, up to the closing bracket.
CITATION = re.compile(r"@([A-Za-z0-9]{2,}),([^\]]{0,200})")


def citations_naming_a_statement(key: str) -> list[tuple[pathlib.Path, int, str]]:
    """Every place a page cites `key` together with a numbered statement, and the citation's text."""
    out = []
    statement = re.compile(r"(Theorem|Lemma|Proposition|Corollary|Thm\.|Lem\.|Prop\.|Cor\.)\s"
                           r"([A-Z0-9][0-9.]*)")
    for path in sorted((ROOT / "writing").rglob("*.md")):
        if ".book" in path.parts or ".assets" in path.parts:
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in CITATION.finditer(line):
                if m.group(1) != key:
                    continue
                if statement.search(m.group(2)):
                    out.append((path, number, m.group(0)))
    return out


def test_the_bibliography_entry_for_the_owed_page_exists():
    text = SUPPLEMENT.read_text(encoding="utf-8")
    assert re.search(r"^@article\{" + OWED + r",", text, re.M), f"{OWED} is not in the supplement"
    assert "10.1006/jabr.1999.7963" in text, "the entry lost its DOI"


def test_the_owed_page_is_still_owed_at_exactly_one_place():
    """The gap is open at one citation and nowhere else; a second site is a new defect."""
    sites = citations_naming_a_statement(OWED)
    assert len(sites) == 1, [
        (p.relative_to(ROOT).as_posix(), n, t[:80]) for p, n, t in sites
    ]
    path, number, citation = sites[0]
    assert path == PAGE, path.relative_to(ROOT).as_posix()
    # no printed page in the citation: that is precisely the gap
    assert "printed p" not in citation and not re.search(r"\bp\.\s?\d", citation), citation


def test_the_gap_is_resolved_once_a_page_appears():
    """Fails when the citation gains a page, so the record above gets updated in the same change.

    This asserts the negative: as long as the page is owed, the citation carries none.  Whoever
    supplies it -- from a copy of the article -- must delete this test and the MISSING_SOURCE note
    with the commit that adds the number, and this failure is what says so.
    """
    sites = citations_naming_a_statement(OWED)
    assert sites, f"no @{OWED} statement citation left; delete this file and MISSING_SOURCE"
    _, _, citation = sites[0]
    assert "printed p" not in citation, (
        f"@{OWED} now names a printed page ({citation[:80]!r}): delete "
        f"test_the_gap_is_resolved_once_a_page_appears and MISSING_SOURCE, which say the page is "
        f"owed"
    )
    assert MISSING_SOURCE, "MISSING_SOURCE names the source that supplies the page"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)

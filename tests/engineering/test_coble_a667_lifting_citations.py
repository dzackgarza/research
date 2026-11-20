"""Acceptance gate for research#667, the dependent-page item.

The acceptance sentence is "Every dependent page must use the proved subgroup and fibre
hypotheses".  The proved statement is ``thm:coble-integral-lifting-fibre`` on the Heegner page:
for a subgroup $\\Gamma\\leq\\Orth(T_\\Co)$ containing $\\widetilde\\Orth^+(T_\\Co)$, the datum map
$x\\mapsto D(x)$ is a bijection from $\\Gamma$-orbits of primitive isotropic lines, planes and
flags onto the $H=\\rho(\\Gamma)$-orbits of the finite data, and the fibre over one datum is a
single orbit because $\\rho(\\Stab(x))=\\Stab_Q(D(x))$; the finite double quotient is therefore one
point per datum.

  item 1  the two pages that applied the $527$-cusp count of the stable quotient without that
          statement now cite it at the count itself.  The reviewer's witness is
          ``coble/coble-moduli/cusp-correspondence-morphism-chain.md:32``, a live book chapter
          (``writing/.book/_quarto.yml``), and the same shape stood at
          ``coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md:346``.
  item 2  no book chapter applies a count of cusps of a stable quotient without citing the
          statement that count comes from.  This is the shape a sweep keyed on the existing
          labels cannot see, and it is not a sentence with no reference at all: the reviewer's
          sentence cited the equivariance, injectivity and non-surjectivity of its map and
          omitted only the source of the number.  So the check is that a sentence applying
          such a count carries ``thm:coble-zero-cusp-count`` or
          ``thm:coble-integral-lifting-fibre``.

Both checks read the markdown sources; neither needs the Sage runtime or a render.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
WRITING = ROOT / "writing"
QUARTO = WRITING / ".book" / "_quarto.yml"
OWNER_PAGE = "coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
MORPHISM_CHAIN = WRITING / "coble/coble-moduli/cusp-correspondence-morphism-chain.md"
COMPARISON = WRITING / "coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"

THEOREM = "@thm:coble-integral-lifting-fibre"

# The stable quotient's cusp counts, in each spelling the corpus uses for them.
COUNT = re.compile(r"527|189\\,720|569\\,160|23\\,715|189720|569160|23715")
STABLE_CUSPS = re.compile(r"cusps? of the stable quotient|stable quotient[^.]{0,40}cusps?")
# The statements a stable-quotient cusp count may come from: the count itself, or the theorem
# that carries the subgroup and fibre hypotheses under which it is a count of lattice orbits.
COUNT_OWNERS = ("thm:coble-zero-cusp-count", "thm:coble-integral-lifting-fibre")


def chapters() -> list[str]:
    """The book's chapters, as paths relative to ``writing/``, in reading order."""
    text = QUARTO.read_text(encoding="utf-8")
    return [
        line.strip()[2:].strip()
        for line in text.splitlines()
        if re.match(r"\s*- \S+\.md\s*$", line)
    ]


def sentences(text: str):
    """Line number and sentence, splitting prose on sentence-final punctuation."""
    for number, line in enumerate(text.splitlines(), start=1):
        for sentence in re.split(r"(?<=[.!?])\s+", line):
            yield number, sentence


# ------------------------------------------------------- item 1: the two pages, at the count
def test_item1_the_morphism_chain_page_cites_the_theorem_at_the_count():
    """The reviewer's witness: the 527-cusp count is not applied bare."""
    text = MORPHISM_CHAIN.read_text(encoding="utf-8")
    hits = [
        line
        for line in text.splitlines()
        if "527" in line and "cusps of the stable quotient" in line
    ]
    assert hits, "the 527-cusp sentence of the morphism chain is gone; re-anchor this test"
    for line in hits:
        assert THEOREM in line, "the stable-quotient 527 count is applied without the theorem"
        assert "orbit" in line, "the fibre hypothesis -- one orbit per class -- is not stated"


def test_item1_the_comparison_page_cites_the_theorem_at_its_count():
    """The same shape on the Enriques--Coble comparison page."""
    text = COMPARISON.read_text(encoding="utf-8")
    hits = [
        line
        for line in text.splitlines()
        if "527" in line and "cusps of the stable quotient" in line
    ]
    assert hits, "the 527-cusp sentence of the comparison page is gone; re-anchor this test"
    for line in hits:
        assert THEOREM in line, "the stable-quotient 527 count is applied without the theorem"
        assert "orbit" in line, "the fibre hypothesis -- one orbit per class -- is not stated"


# ------------------------------------------ item 2: no book chapter applies such a count bare
def test_item2_no_book_chapter_applies_a_stable_quotient_count_without_a_reference():
    """A count of cusps of a stable quotient names the statement it comes from.

    Two things are checked per sentence: it applies such a count (a stable-quotient cusp
    phrase and one of the numbers), and it cites the count's owner -- ``thm:coble-zero-cusp-count``
    for the number or ``thm:coble-integral-lifting-fibre`` for the hypotheses.  A sentence that
    cites only *other* facts about the same map is exactly the defect the reviewer found, so
    the check is not "carries no reference".  The owning page is exempt: it proves the counts,
    and the other pages are the ones that must cite it.
    """
    offenders = []
    for chapter in chapters():
        if chapter == OWNER_PAGE:
            continue
        path = WRITING / chapter
        if not path.exists():
            continue
        for number, sentence in sentences(path.read_text(encoding="utf-8")):
            if not COUNT.search(sentence) or not STABLE_CUSPS.search(sentence):
                continue
            if any(owner in sentence for owner in COUNT_OWNERS):
                continue
            offenders.append(f"{chapter}:{number}: {sentence.strip()[:140]}")
    assert not offenders, "counts of a stable quotient whose source is not cited:\n" + "\n".join(
        offenders
    )


def test_item2_the_check_rejects_the_sentence_the_reviewer_found():
    """The guard is exercised on the defect itself, so a green run means something."""
    defect = (
        "On $0$-cusps, $\\eta$ induces an injective map from the $527$ $0$-cusps of the stable "
        "quotient to the divisibility-$2$ cusps: the orbit map is defined because the embedding "
        "is equivariant (@thm:coble-strong-lifting); it is injective (@prop:cusp-map-injective)."
    )
    assert COUNT.search(defect) and STABLE_CUSPS.search(defect)
    assert not any(owner in defect for owner in COUNT_OWNERS), "the guard would not have fired"
    repaired = defect.replace(
        "$527$ $0$-cusps of the stable quotient",
        "$527$ $0$-cusps of the stable quotient (@thm:coble-zero-cusp-count(2), one $0$-cusp per "
        "class by @thm:coble-integral-lifting-fibre(1), (2))",
    )
    assert any(owner in repaired for owner in COUNT_OWNERS)

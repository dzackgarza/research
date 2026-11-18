"""Acceptance gate for research#672 (A29): which Sterk cusp carries the Coble 0-cusp.

The acceptance is a single sentence: "Done when the question is settled in ``writing/`` with a
proof, a disproof, or a computation record, and every page that cites the open form is updated."

  item 1   the question is settled on the page as a theorem with its proof, or as a disproof.
           Here the settlement is both: the identification with cusp 2 alone is false as a
           statement about the boundary lattice, and what is true is the chamber statement.
  item 2   every page that cites the open form is updated -- the page itself, the research
           statement, and the open-question register row that pointed at the section.
  item 1b  the record builds its lattices from the cited formulas by library construction and
           not from typed Gram matrices, and its invariants are the library's, not hand-written
           linear algebra (research#672 review, finding 1).

The tests below do three kinds of check.  The structural ones read the record's source.  The
transcript ones read what the library returned.  ``test_a1b_the_chamber_half_recomputed`` is a
genuine re-derivation: it recomputes the labelled graph of the restricted chamber at each of the
four cusps from the committed figure transcript, in the standard library, with no Sage, and
compares it with `thm:coble-cusp-chamber`'s adjacency table.  Nothing here needs the Sage runtime;
the quarter of the record that does is the transcript's, and the test says which lines it trusts.
"""

from __future__ import annotations

import pathlib
import re
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/coble-moduli/cusp-correspondence-morphism-chain.md"
DIAGRAM_PAGE = ROOT / "writing/coble/cusp-correspondence/cusp-diagrams-by-moduli-space.md"
OPEN_QUESTIONS = ROOT / "writing/open-questions.md"
RECORD = ROOT / "computations/reports/coble_672-zero-cusp-sterk-two-run.txt"
SCRIPT = ROOT / "computations/reports/coble_672-zero-cusp-sterk-two.py"
WHITE = ROOT / "computations/reports/coble_enriques-white-root-facets-run.txt"
PAIR = ROOT / "computations/reports/coble_pair-semifan-cusps-run.txt"


def page() -> str:
    return PAGE.read_text(encoding="utf-8")


def record() -> str:
    return RECORD.read_text(encoding="utf-8")


def script() -> str:
    return SCRIPT.read_text(encoding="utf-8")


# ------------------------------------------------------------------ item 1: the settlement

def test_a1_the_conjecture_is_gone_and_a_theorem_stands_in_its_place():
    text = page()
    assert "conj:coble-zero-cusp-sterk-two" not in text, "the open form is still on the page"
    assert re.search(r"::: \{\.theorem #thm:coble-zero-cusp-sterk-two", text)
    assert "::: {.proof}" in text


def test_a1_the_page_states_both_halves_of_the_settlement():
    text = page()
    assert "boundary lattice" in text and "(9,9,1)_1" in text
    assert "singles out no cusp" in text
    assert "singles out cusp $2$" in text


def test_a1_the_cusp_map_lemma_the_argument_rests_on_is_stated_and_proved():
    assert re.search(r"::: \{\.lemma #lem:cusp-map-of-a-period-lattice-embedding", page())


# ------------------------------------- item 1b: library construction, no typed matrices

FORBIDDEN = ("det_bareiss", "smith_normal_form", "quotient_gram", "reduce_row", "inverse_unimodular",
             "CartanMatrix", "IntegralLattice(", "np.linalg", "import numpy")


def test_a1b_the_record_builds_its_lattices_from_the_library():
    text = script()
    for name in ("NamedLattices.Tco", "NamedLattices.TEn", "NamedLattices.TdP",
                 "Sterk.selected_isotropic_vectors()", "Embeddings.TEn_into_TdP"):
        assert name in text, name


def test_a1b_the_record_writes_no_linear_algebra_and_types_no_gram_matrix():
    text = script()
    for token in FORBIDDEN:
        assert token not in text, f"{token} is hand-written linear algebra in the record"
    # no three-line nested list literal, which is how a typed Gram matrix would appear
    assert not re.search(r"\[\s*\[[^\]]*\d[^\]]*\]\s*,", text), "a matrix literal is typed"


def test_a1b_the_record_uses_the_library_operations_the_page_names():
    text = script()
    for op in ("primitive_sublattice_from", "orthogonal_complement", "radical_quotient",
               "primitive_isotropic_subobject", "isotropic_reduction", "divisibility_ideal",
               "two_elementary_invariants", "is_isometric"):
        assert op in text, op


def test_a1b_the_transcript_is_the_library_speaking():
    text = record()
    # every cusp 2..5 reduces to <2> + E8(2) by the library's own isometry verdict
    assert text.count("is <2> + E8(2) = (9,9,1)_1: True") == 4
    # the period lattices and the two 2-elementary boundary types, as the library prints them
    assert "T_Co = NamedLattices.Tco rank 11  det -2048  signature (2, 9)  even True" in text
    assert "delta^perp is T_Co                : True" in text
    assert "invariants (18, 0, 0)" in text and "invariants (18, 2, 0)" in text
    # the cusp-1 exclusion is the library's pairing, not a transcription
    assert "not a vector of T_Co = delta^perp" in text


def test_a1b_no_line_of_the_transcript_reports_a_contradictory_rank():
    text = record()
    for line in text.splitlines():
        if "delta^perp in T_En" in line:
            assert "rank 11" in line, line


# ----------------------- item 1b: the chamber half, recomputed from the committed figure data

def wall_gram(cusp: int) -> list[list[int]]:
    lines = WHITE.read_text(encoding="utf-8").splitlines()
    start = next(i for i, ln in enumerate(lines) if re.match(r"=== cusp %d; eta" % cusp, ln))
    j = start
    while not lines[j].startswith("wall Gram matrix"):
        j += 1
    j += 1
    M = []
    while j < len(lines) and lines[j].strip().startswith("["):
        M.append([int(x) for x in lines[j].strip().strip("[]").split()])
        j += 1
    return M


def figure_data(cusp: int):
    """The white node and the printed (r_i, delta) pairings of one cusp, from the transcript."""
    white, pairs = None, {}
    current = None
    for ln in PAIR.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-- the 0-cusp over Sterk cusp (\d+)", ln)
        if m:
            current = int(m.group(1))
            continue
        if current != cusp:
            continue
        m = re.search(r"the white node is figure node (\d+)", ln)
        if m:
            white = int(m.group(1))
        m = re.match(r"\s+pairings \(r_i,delta\) nonzero only for \[([^\]]*)\], with values \[([^\]]*)\]", ln)
        if m and m.group(1).strip():
            pairs = dict(zip([int(x) for x in m.group(1).split(",")],
                             [int(x) for x in m.group(2).split(",")]))
    return white, pairs


def restricted_chamber(cusp: int):
    """The walls C cap delta^perp: project each root other than delta, then label the graph."""
    G = wall_gram(cusp)
    white, pairs = figure_data(cusp)
    pd = {i: 0 for i in range(1, len(G) + 1)}
    pd.update(pairs)
    keep = [i for i in range(1, len(G) + 1) if i != white]
    n = len(keep)
    # alpha_bar^2 = alpha^2 + (alpha,delta)^2 / 2, because delta^2 = -2
    square = {a: F(G[a - 1][a - 1]) + F(pd[a] * pd[a], 2) for a in keep}
    edges, labels = [], {}
    for i, a in enumerate(keep):
        for b in keep[i + 1:]:
            # (alpha_bar, beta_bar) = g_ab + g_ad g_bd / 2
            val2 = 2 * G[a - 1][b - 1] + pd[a] * pd[b]
            if val2 == 0:
                continue
            edges.append((a, b))
            cos2 = F(val2 * val2, 4) / (F(square[a]) * F(square[b]))
            labels[(a, b)] = 3 if cos2 == F(1, 4) else 4 if cos2 == F(1, 2) else (
                "parallel" if cos2 == 1 else "other")
    return keep, square, edges, labels


def arm_signature(keep, square, edges, labels):
    """(arm lengths from the single branch vertex, label of each arm's last edge, square at its end)."""
    deg = {a: 0 for a in keep}
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    branch = [a for a in keep if deg[a] >= 3]
    if len(branch) != 1:
        return None
    b0 = branch[0]
    arms = []
    for a, b in edges:
        if b0 not in (a, b):
            continue
        prev, cur = b0, (b if a == b0 else a)
        length, last = 1, (min(prev, cur), max(prev, cur))
        while deg[cur] == 2:
            nxt = [z for (x, y) in edges for z in ((y,) if x == cur else (x,) if y == cur else ()) if z != prev]
            prev, cur = cur, nxt[0]
            length += 1
            last = (min(prev, cur), max(prev, cur))
        arms.append((length, labels[last], square[cur]))
    return tuple(sorted(arms))


COBLE_ARMS = ((1, 3, -4), (2, 3, -4), (5, 4, -2))   # thm:coble-cusp-chamber, AN06 Table 1, N = 10


def test_a1b_the_chamber_half_recomputed():
    keep, square, edges, labels = restricted_chamber(2)
    assert len(keep) == 9 and len(edges) == 8
    assert sorted(square.values()) == [-4] * 8 + [-2]
    assert arm_signature(keep, square, edges, labels) == COBLE_ARMS


def test_a1b_the_other_three_cusps_have_more_walls():
    counts = {}
    for cusp in (3, 4, 5):
        keep, square, edges, labels = restricted_chamber(cusp)
        parallel = sum(1 for lab in labels.values() if lab == "parallel")
        counts[cusp] = len(keep) - parallel
    assert counts == {3: 10, 4: 10, 5: 11}, counts


def test_a1b_the_transcript_reports_those_same_counts():
    text = record()
    for line in ("cusp 2: white node figure 10; 9 projected roots, 0 induced parallel pair(s), 9 distinct walls",
                 "cusp 3: white node figure 5; 11 projected roots, 1 induced parallel pair(s), 10 distinct walls",
                 "cusp 4: white node figure 9; 10 projected roots, 0 induced parallel pair(s), 10 distinct walls",
                 "cusp 5: white node figure 11; 13 projected roots, 2 induced parallel pair(s), 11 distinct walls"):
        assert line in text, line


# ------------------------------------------------------------------ item 2: the other pages

def test_a2_the_open_question_register_no_longer_asks_it():
    text = OPEN_QUESTIONS.read_text(encoding="utf-8")
    assert "The Coble cusps in the morphism chain" not in text
    assert "@sec-cusp-correspondence-morphism-chain" not in text


def pages():
    """Every authored page under writing/, excluding the book's symlinked mirror."""
    out = []
    for path in sorted((ROOT / "writing").rglob("*.md")):
        parts = path.parts
        if ".book" in parts or ".assets" in parts:
            continue
        out.append(path)
    assert len(out) > 100, f"only {len(out)} pages found: the sweep is not sweeping"
    return out


FORBIDDEN_CLAIMS = (
    "the identification of Sterk cusp 2",
    "Coble 0-cusp corresponds with cusp 2",
    "Coble 0-cusp corresponds to cusp 2",
    "the Coble cusps correspond to",
    "conj:coble-zero-cusp-sterk-two",
)


def test_a2_no_page_anywhere_still_asserts_the_unique_correspondence():
    hits = []
    for path in pages():
        text = path.read_text(encoding="utf-8")
        for claim in FORBIDDEN_CLAIMS:
            if claim in text:
                hits.append((path.relative_to(ROOT).as_posix(), claim))
    assert not hits, hits


def test_a2_the_bibliography_note_on_sterk_cites_the_theorem():
    text = (ROOT / "writing/coble/extracted-references/extracted-references.md").read_text(encoding="utf-8")
    entry = text[text.index("## Ste91"):]
    entry = entry[: entry.index("\n## ", 10)] if "\n## " in entry[10:] else entry
    assert "@thm:coble-zero-cusp-sterk-two" in entry
    assert "the identification of Sterk cusp 2" not in entry


def test_a2_the_restricted_semifan_page_says_cusp_2_is_where_the_chamber_occurs():
    text = (ROOT / "writing/coble/heegner-report/coble-heegner-research-report.md").read_text(encoding="utf-8")
    assert "Cusp $2$ is the one cusp of $\\fentwo$ at which this chamber occurs" in text
    assert "carry Coble $0$-cusps with boundary lattice $(9,9,1)_1$" in text


def test_a2_the_research_statement_no_longer_asserts_the_unique_correspondence():
    text = (ROOT / "writing/research-statement/ResearchStatement.md").read_text(encoding="utf-8")
    assert "I have computed that the Coble 0-cusp corresponds with cusp 2" not in text
    assert "does not sit over a single one of Sterk's cusps" in text


def test_a2_every_computed_number_names_its_record():
    text = page()
    assert "computations/reports/coble_672-zero-cusp-sterk-two-run.txt" in text
    assert "computations/reports/coble_pair-semifan-cusps-run.txt" in text


def test_a2_the_source_citations_carry_printed_pages():
    text = page()
    for cite in ("printed p. 589", "printed p. 590", "printed pp. 594--595", "printed p. 144",
                 "printed p. 16"):
        assert cite in text, cite


def test_a2_the_cusp_vectors_printed_on_the_diagram_page_are_the_library_ones():
    text = DIAGRAM_PAGE.read_text(encoding="utf-8")
    assert "\\overline{\\alpha}_8$ | 2 | 1" not in text
    assert "y_3 = -(2\\alpha_1+3\\alpha_2+4\\alpha_3+6\\alpha_4" in text
    assert "Sterk.selected_isotropic_vectors()" in text




# ------------------------------------ item 2, render layer: no undefined macro on these pages
#
# The book defines no macros of its own (justfile `docs-assets`): the corpus is
# ~/.pandoc/templates/css/mathjax-macros.html, copied to writing/.assets.  An undefined macro is
# left raw in the html and renders as a MathJax error box, so a markdown parse and the source
# layer both pass while the page is broken.  This is the check the render layer would make.

MACRO_CORPUS = ROOT / "writing/.assets/mathjax-macros.html"

STANDARD_MACROS = set("""
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi
omicron pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
frac dfrac tfrac sqrt sum prod int oint iint lim inf sup max min bigcup bigcap
left right big Big bigg Bigg bigl bigr Bigl Bigr middle
langle rangle lfloor rfloor lceil rceil vert Vert backslash lvert rvert
cdot cdots ldots dots vdots ddots times oplus ominus otimes odot bigoplus wedge vee neg
le ge leq geq neq ne lt gt equiv sim simeq approx cong propto perp parallel asymp doteq
subset subseteq supset supseteq subsetneq supsetneq nsubseteq nsupseteq in notin ni not
cup cap setminus emptyset varnothing sqcup sqcap uplus
to mapsto rightarrow leftarrow Rightarrow Leftarrow leftrightarrow Leftrightarrow
longleftrightarrow implies iff hookrightarrow longrightarrow longleftarrow
infty partial nabla forall exists nexists aleph hbar ell wp Re Im
mathbb mathbf mathcal mathfrak mathrm mathit mathsf mathtt operatorname mathop mathbin mathrel
rm bf it sf tt cal em
text textbf textit overline underline widehat widetilde hat bar vec dot ddot tilde acute grave
breve check over stackrel overset underset binom choose atop
quad qquad enspace thinspace hspace hfill mkern
pm mp ast star circ bullet div mid nmid dashv vdash models vDash
zmod limits nolimits pmod pod bmod mod
begin end boldsymbol bm dots colon
ker dim deg arg hom det coker rank gcd arccos log ln exp sin cos tan
veebar barwedge curlyvee curlywedge lhd rhd unlhd unrhd
triangleleft triangleright trianglelefteq trianglerighteq
square blacksquare Box boxtimes ltimes rtimes
ll gg sharp flat natural
hline arrow cline multicolumn
input include pic usepackage newtheorem theoremstyle set
newcommand renewcommand DeclareMathOperator
""".split())


def undefined_macros(page: pathlib.Path) -> set[str]:
    """The macros a page uses that neither the book's corpus nor standard LaTeX defines."""
    text = MACRO_CORPUS.read_text(encoding="utf-8")
    defined = set(re.findall(r"\\(?:newcommand|renewcommand)\s*\{?\\?([A-Za-z]+)", text))
    defined |= set(re.findall(r"\\DeclareMathOperator\s*\{?\\?([A-Za-z]+)", text))
    body = page.read_text(encoding="utf-8")
    used = set(re.findall(r"\\([A-Za-z]+)", body))
    return {m for m in used if m not in defined and m not in STANDARD_MACROS}


PAGES_THIS_ISSUE_OWNS = (
    "writing/coble/coble-moduli/cusp-correspondence-morphism-chain.md",
    "writing/coble/cusp-correspondence/cusp-diagrams-by-moduli-space.md",
    "writing/coble/extracted-references/extracted-references.md",
    "writing/research-statement/ResearchStatement.md",
    "writing/open-questions.md",
)


def test_a2_the_pages_this_issue_owns_and_the_research_report_use_only_defined_macros():
    if not MACRO_CORPUS.exists():
        return  # a bare checkout has no generated corpus; `just docs-assets` writes it
    offenders = {rel: sorted(undefined_macros(ROOT / rel))
                 for rel in PAGES_THIS_ISSUE_OWNS + (
                     "writing/coble/heegner-report/coble-heegner-research-report.md",)}
    offenders = {k: v for k, v in offenders.items() if v}
    assert not offenders, offenders


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)

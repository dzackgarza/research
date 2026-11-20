"""Acceptance gate for research#645 (A2): the Coble plane/flag application.

The issue's acceptance is the "Ready work" paragraph of its body plus the
constraints stated around it:

  A1  the chapter's plane/flag application using the actual group constructions,
      public entry points, counted objects and records;
  A2  the group bookkeeping --- ``Gamma_Co = Otilde^+(T_Co)`` conjectural, neither
      inclusion asserted, ``F^un_Co`` the ``Orth(T_Co)`` row, ``R_gent`` the
      restricted stabilizer image and ``Gamma_{Co,2}`` the monodromy group, related
      to it by the containment of thm:coble-monodromy-versus-enriques(4) and by
      qst:coble-monodromy-equality, with no inclusion against ``Gamma_Co``;
  A3  the exact subgroup and fibre hypotheses connected to the public rows,
      never finite containment read as arithmetic flag transitivity;
  A4  the page's stale claim that every plane row is still uncomputed reconciled;
  A5  endpoint incidence kept apart from flag-orbit multiplicity;
  A6  the proved stable flag theorem preserved with the kernel-incidence
      computation visibly separate;
  A7  sage-extensions#381 asynchronous (no result claimed) and lattice-database#7
      the card owner.

Each test states the smallest input that decides its item: the discriminant
module for the counted objects, the page's own orders for the fibre index, the
committed records for the numbers the prose quotes, and a two-dimensional model
for the endpoint-versus-flag inequality.  No Sage and no provider call: these
are checks on arithmetic and on committed records, not new computations, and
they replace nothing that sage-extensions owes (#381) or that the card owns.

Run standalone (``python3 tests/engineering/test_coble_a2_acceptance.py``) or
under pytest; the module imports nothing outside the standard library.
"""

from __future__ import annotations

import itertools
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"
CONVENTIONS = ROOT / "writing/coble/reference-tables/lattice-and-diagram-conventions.md"


def parens_normalised(text):
    r"""The text with \left( ... \right) spelled as \pqty{ ... }.

    The prose must not use \pqty: scripts/docs_check.py's check 8 refuses it as a macro the
    corpus does not define, so the pages write the same delimiter as \left( ... \right).  The
    assertions below are written once, in the \pqty spelling, and read either.
    """
    return text.replace("\\left(", "\\pqty{").replace("\\right)", "}")

DESCENT = ROOT / "writing/coble/computations/discriminant-form-descent.md"
LOG_391 = ROOT / "computations/reports/coble_gco_public_incidence_source-run.log"
QUOTIENT_RUN = ROOT / "computations/reports/coble_integral_flag_quotient-run.txt"

def _nums(text: str) -> list[int]:
    """Integers written with LaTeX thin spaces (``189\\,720``) or plain."""
    return [int(t.replace("\\,", "").replace(",", "")) for t in re.findall(r"\d[\d\\,]*", text)]


# ---------------------------------------------------------------------------
# A1: the counted objects, from the discriminant module itself.
# ---------------------------------------------------------------------------

def test_a1_counted_objects_of_the_discriminant_module():
    """B = I_{2,9}, T_Co = B(2), A = B/2B, q([x/2]) = (x,x)_B/2.

    Decides: 527 nonzero isotropic classes, 23 715 isotropic 2-planes, 135 of
    them through one fixed class -- the three numbers the page counts and the
    rows return.
    """
    n = 11
    gram = [1, 1] + [-1] * 9

    def square(x):
        return sum(gram[i] * x[i] for i in range(n))

    vectors = list(itertools.product((0, 1), repeat=n))
    nonzero = [x for x in vectors if any(x)]
    isotropic = [x for x in nonzero if square(x) % 4 == 0]
    assert len(nonzero) == 2047
    assert len(isotropic) == 527, len(isotropic)

    isoset = set(isotropic)
    planes = set()
    for i, u in enumerate(isotropic):
        for v in isotropic[i + 1:]:
            w = tuple((u[k] + v[k]) % 2 for k in range(n))
            if w in isoset:
                planes.add(frozenset((u, v, w)))
    assert len(planes) == 23715, len(planes)

    c = isotropic[0]
    through = sum(1 for plane in planes if c in plane)
    assert through == 135, through
    # the decorated count the page uses: eight stars over each isotropic plane
    assert 8 * len(planes) == 189720
    assert 3 * len(planes) == 71145  # flags over undecorated planes, for contrast


def test_a1_fibre_identity_and_the_plane_cusps():
    """The four orders the page divides, and the identities that reconcile them."""
    order_q = 46998591897600  # |Orth(q_{T_Co})|
    stab_plane = 1981808640  # |Stab_{Orth(q)}(J)|
    image_s = 247726080  # |rho(Stab_{Orth(B)}(P))|
    assert order_q // stab_plane == 23715
    assert order_q // image_s == 189720
    assert stab_plane // image_s == 8
    assert 30240 * 2 ** 13 == image_s  # thm:coble-plane-stabilizer-image(3)
    assert 8 * 23715 == 189720
    # 1-cusps: full group 1, stable 189 720, Gamma_{Co,2} 7 (the row's)
    page = PAGE.read_text()
    assert "has one $1$-cusp" in page and "189\\,720$ $1$-cusps" in page
    assert "seven $1$-cusps" in page


def test_a1_the_plane_rows_report_the_two_kernel_groups():
    """The paragraph that identifies the row's groups names both and their count."""
    text = PAGE.read_text()
    para = next(p for p in text.split("\n\n") if p.startswith("*The two plane rows.*"))
    assert "isotropic_orbit_representatives(2)" in para
    assert "Tco.stable_orthogonal_group()" in para and "Tco.O_plus()" in para
    for group in ("\\ker\\rho", "\\widetilde\\Orth^+(T_\\Co)"):
        assert re.search(r"189\\,720\$ (planes )?for \$" + re.escape(group), para), group
    assert "897e7f7fd45e4d4f4cfcb29b266672e9232d25ab" in para
    assert "primitive" in para and "zero Gram tensor" in para
    assert "double cosets" in para


def test_a1_the_plane_rows_record_is_archived():
    """The record of run 43798731423 is in this repository, and the page names it.

    The run's log archive needs admin rights on sage-extensions (the API answers
    403), so the record archived here is the issue's closing comment, retrieved
    verbatim from the public API.  It must carry the run, the revision, both
    counts and both durations, and the page must point at it.
    """
    rec = (ROOT / "computations/reports/coble_kernel_plane_rows-issue390-run-record.txt").read_text()
    assert "43798731423" in rec and "897e7f7fd4" in rec
    assert rec.count("189720") >= 2
    assert "4013.4" in rec and "1821.2" in rec
    assert "double-coset count" in rec
    para = next(p for p in PAGE.read_text().split("\n\n") if p.startswith("*The two plane rows.*"))
    assert "coble_kernel_plane_rows-issue390-run-record.txt" in para
    assert "4013.4" in para and "1821.2" in para


# ---------------------------------------------------------------------------
# A2: the group bookkeeping the issue fixes.
# ---------------------------------------------------------------------------

def test_a2_every_gamma_co_equality_is_named_with_its_base():
    """The equality Gamma_Co = Otilde^+(T_Co) holds on the labelled base and is proved there;
    elsewhere it may appear only in the conjecture remark, in a conditional, or alongside its
    own reference."""
    offenders = []
    for path in (ROOT / "writing").rglob("*.md"):
        text = path.read_text(errors="replace")
        if not re.search(r"\\Gamma_\\Co\s*=\s*\\widetilde\\Orth", text):
            continue
        # allow the display inside the theorem div or the conjecture div, and lines naming them
        inside = False
        for lineno, line in enumerate(text.splitlines(), 1):
            if re.search(r"#(conj:gamma-co-stable|thm:gamma-co-is-stable)", line):
                inside = True
            elif line.strip() == ":::":
                inside = False
            if re.search(r"\\Gamma_\\Co\s*=\s*\\widetilde\\Orth", line):
                if ("conj:gamma-co-stable" in line or "thm:gamma-co-is-stable" in line
                        or "gamma-co-status" in line or inside):
                    continue
                # An occurrence that is the CONDITION of an equivalence is not an assertion of
                # the equality: "Ext(Gamma) = Ext(Otilde) holds exactly when Gamma = Otilde"
                # states the equivalence, not the equality.
                if re.search(r"exactly when|holds if and only if|if and only if", line):
                    continue
                offenders.append(f"{path.relative_to(ROOT)}:{lineno}")
    assert offenders == [], offenders
    # the equality is proved on the labelled base, and the page says so
    lattices = LATTICES.read_text()
    assert "#thm:gamma-co-is-stable" in lattices
    assert "\\Gamma_\\Co=\\widetilde\\Orth^+(T_\\Co)" in lattices
    # no inclusion between Gamma_{Co,2} and Gamma_Co is asserted
    assert "no inclusion between it and $\\Gamma_\\Co$ is asserted" in PAGE.read_text()


def test_a2_the_four_groups_are_named_with_their_rows():
    text = PAGE.read_text()
    # F^un_Co is the Orth(T_Co) row; F_{Co,2} the Gamma_{Co,2} row; F_Co the stable row
    assert "F^{\\mathrm{un}}_\\Co = \\bD(T_\\Co)/\\Orth(T_\\Co)" in text
    assert "$189\\,720$ is the number of $1$-cusps of $\\fco$" in text
    for key in ("def:gamma-co-groups", "rmk:gamma-co-status", "conj:gamma-co-stable"):
        assert key in text, key


# ---------------------------------------------------------------------------
# A3: the subgroup and fibre hypotheses, connected to the two rows.
# ---------------------------------------------------------------------------

def test_a3_subgroup_hypothesis_is_the_row_s_group():
    text = parens_normalised(PAGE.read_text())
    section = text[text.index("{#sec-plane-flag-rows}"):]
    # the subgroup hypothesis: rho^{-1}(P) = Gamma^{cong}_{Co,2} = R_{gent}, the entry point's
    # group.  The row builds this arithmetic group; the monodromy group Gamma_{Co,2} is related
    # to it by the containment of thm:coble-monodromy-versus-enriques(4) and by
    # qst:coble-monodromy-equality, never by an unconditional equality, which item (3) refutes.
    assert "\\rho_{T_\\Co}^{-1}\\pqty{\\Stab_{\\Orth(q_{T_\\Co})}\\bigl(A_{U(2)}\\bigr)} = \\rho_{T_\\Co}^{-1}(P) = \\Gamma^{\\mathrm{cong}}_{\\Co,2} = R_{\\gent}" in text
    assert "discriminant_point_stabilizer(point)" in section
    assert "\\Gamma_{\\Co,2} = R_{\\gent}\\intersect\\Orth^+(T_\\Co)" in section
    assert "@qst:coble-monodromy-equality" in section
    # the fibre hypothesis: [F:S] = 8, the index the plane count is built from
    assert "[F:S] = 8" in section or "[F:S]=8" in section or "index is $8$" in section


def test_a3_no_unconditional_identity_of_the_monodromy_and_arithmetic_groups():
    """The equality Gamma_{Co,2} = R_{gent} is refuted; only the containment is asserted.

    thm:coble-monodromy-versus-enriques(3) refutes the equality, and (4) proves the
    containment.  A page that writes the equality says something false about the monodromy
    group; the one place the string may occur is inside the conditional of
    qst:coble-monodromy-equality, which names R_{gent} cap O^+, not R_{gent}.
    """
    text = PAGE.read_text()
    unconditional = re.compile(r"\\Gamma_\{\\Co,2\}\s*=\s*R_\{\\gent\}(?!\\intersect)")
    hits = [f"{n}: {line.strip()[:120]}"
            for n, line in enumerate(text.splitlines(), 1)
            if unconditional.search(line)]
    assert not hits, hits


def test_a3_no_integral_orbit_count_from_a_finite_containment():
    """Every transitivity used in the section is integral, or counts classes.

    The failure mode the issue names is reading finite containment (a subgroup of
    Orth(q)) as arithmetic flag transitivity.  The section's two uses of a finite
    action are the class action of GL(J_0)<=S_3, which counts H_0-orbits on a
    three-element set, and the class-orbit reduction, whose integral step is
    thm:cusp-lifting(1), (4).  Both must be present with their integral support.
    """
    text = PAGE.read_text()
    section = text[text.index("{#sec-plane-flag-rows}"):]
    assert "GL(J_0)\\cong S_3" in section  # the finite part
    assert "@thm:cusp-lifting(1), (4)" in section  # the integral step that licenses it
    assert "proves the existence of its subgroup transporter" in section


def test_a3_the_fibre_hypothesis_is_the_row_s_double_coset_count():
    """The fibre index is the number the row divides by, in the row's own wording.

    ``thm:plane-fibre(1)`` computes the fibre over one ``J`` as ``[F:S] = 8``;
    the row's expected count is the double-coset quotient over one
    ``Orth(T_Co)``-class of planes.  The page must display that quotient and its
    value, or the two hypotheses are not connected to the row.
    """
    text = parens_normalised(PAGE.read_text())
    section = text[text.index("{#sec-plane-flag-rows}"):]
    assert "\\frac{\\abs{\\rho(\\Orth(T_\\Co))}}{\\abs{\\rho\\pqty{\\Stab_{\\Orth(B)}(P)}}}" in section
    assert "\\frac{46\\,998\\,591\\,897\\,600}{247\\,726\\,080} = 189\\,720 = 8\\cdot 23\\,715" in section
    assert "\\abs{\\Orth(q)}/\\abs{S} = \\pqty{\\abs{\\Orth(q)}/\\abs{F}}\\pqty{\\abs{F}/\\abs{S}}" in section
    assert "with $F = \\Stab_{\\Orth(q)}(J)$ and $S = \\rho\\pqty{\\Stab_{\\Orth(B)}(P)}$ of @thm:plane-fibre(1)" in section


# ---------------------------------------------------------------------------
# A4: no stale "uncomputed plane row" survives.
# ---------------------------------------------------------------------------

def test_a4_no_plane_row_is_described_as_uncomputed():
    pattern = re.compile(
        r"(plane\s+(row|orbit|fibre)|1-cusp)[^.]{0,140}(uncomputed|not computed|no page proof|never computed)",
        re.IGNORECASE,
    )
    hits = []
    for path in (ROOT / "writing").rglob("*.md"):
        for lineno, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
            if pattern.search(line):
                hits.append(f"{path.relative_to(ROOT)}:{lineno}")
    assert hits == [], hits


# ---------------------------------------------------------------------------
# A5: endpoint incidence versus flag-orbit multiplicity.
# ---------------------------------------------------------------------------

def _gamma_co_2_edges_from_log() -> dict[tuple[str, str], int]:
    edges = {}
    for line in LOG_391.read_text(errors="replace").splitlines():
        m = re.search(r"\[Gamma_\{Co,2\}\] edge \d+: (L_?\d) < (P_?\d); line=\(\((.+?)\),\); plane=\(\((.+?)\), \(", line)
        if m:
            assert m.group(3) and m.group(4), "edge without both witnesses"
            edges[(m.group(1).replace("_", ""), m.group(2).replace("_", ""))] = 0
    return edges


def _prose_edge_table() -> dict[tuple[str, str], int]:
    table = {}
    for line in PAGE.read_text().splitlines():
        for m in re.finditer(r"\$(L_?\d)<(P_?\d)\$\s*\|\s*\$(\d+)\$", line):
            table[(m.group(1).replace("_", ""), m.group(2).replace("_", ""))] = int(m.group(3))
    return table


def test_a5_public_incidence_matches_the_prose_table():
    """The archived #391 log's edges are exactly the page's thirteen labels."""
    log = LOG_391.read_text(errors="replace")
    lines = re.findall(r"\[Gamma_\{Co,2\}\] line cusp \d+:", log)
    planes = re.findall(r"\[Gamma_\{Co,2\}\] plane cusp \d+:", log)
    assert (len(lines), len(planes)) == (4, 7), (len(lines), len(planes))
    assert "[O(T_Co)] 1 edges over 1 line cusps and 1 plane cusps" in log
    assert "[Gamma_{Co,2}] 13 edges over 4 line cusps and 7 plane cusps" in log
    assert set(_gamma_co_2_edges_from_log()) == set(_prose_edge_table())


def test_a5_the_two_number_sets_are_the_parameter_and_the_measure():
    """13 edges, 13 flag orbits, but 569 160 integral flags: different objects.

    The edge table's weights are counts of integral flags over each endpoint
    pair; their sum must be the kernel's flag total, and their multiset must be
    the thirteen G_Co flag-orbit sizes from the committed transcript.  The
    *number* of edges (13) equals the number of flag orbits here only because
    the forgetful map happens to be injective for this group, which the page
    states as a computed special case and which prop:coble-flag-orbits-and-edges(3)
    does not assert in general.
    """
    table = _prose_edge_table()
    assert len(table) == 13
    assert sum(table.values()) == 569160
    run = QUOTIENT_RUN.read_text()
    sizes = _nums(re.search(r"star-decorated flag orbits: 13 \[(.*?)\]", run).group(1))
    assert len(sizes) == 13 and sum(sizes) == 569160
    assert sorted(table.values()) == sorted(sizes)
    # the general inequality, on the smallest input that decides it
    j0 = [1, 2, 3]
    ident = lambda x: x
    trans = lambda x: x if x == 3 else {1: 2, 2: 1}[x]
    cyc = lambda x: {1: 2, 2: 3, 3: 1}[x]
    def orbit(p, group):
        seen, stack = {p}, [p]
        while stack:
            q = stack.pop()
            for g in group:
                r = g(q)
                if r not in seen:
                    seen.add(r)
                    stack.append(r)
        return seen
    def orbits(group):
        seen, out = set(), 0
        for p in j0:
            if p in seen:
                continue
            out += 1
            seen |= orbit(p, group)
        return out
    s2, s3 = [ident, trans], [ident, trans, cyc]
    assert orbits([ident]) == 3  # H_0 trivial: three flag orbits over one edge
    assert orbits(s2) == 2  # H_0 = S_2: the two-element summand
    assert orbits(s3) == 1  # H_0 = H = S_3: equality, one flag orbit and one edge


def test_a5_the_seven_and_thirteen_are_reproduced_from_the_module():
    """The two orbit counts recomputed here, not only transcribed from a record.

    ``coble_a2-plane-flag-orbit-reproduction.py`` builds ``A_{S_En} = C/2C`` for
    ``C = U + E8(-1)``, the nine G_Co transvections, the eight stars of every
    isotropic plane and the flags, and counts the orbits with no Sage and no
    provider call.  Its transcript must carry the same seven and thirteen.
    """
    run = (ROOT / "computations/reports/coble_a2-plane-flag-orbit-reproduction-run.txt").read_text()
    assert "nonzero isotropic classes of A: 527" in run
    assert "isotropic 2-planes: 23715" in run
    assert "stars of each J: 8" in run
    assert "G_Co-orbits of decorated planes: 7" in run
    assert "G_Co-orbits of flags: 13" in run
    assert "151200" in run and "2160" in run


# ---------------------------------------------------------------------------
# A6: the proved stable flag theorem, and the kernel computation kept apart.
# ---------------------------------------------------------------------------

def test_a6_stable_flag_count_is_a_page_proof():
    text = PAGE.read_text()
    cor = text[text.index("#cor:coble-flag-counts-per-group"):]
    cor = cor[: cor.index(":::")]
    assert "3\\cdot 23\\,715\\cdot 8 = 569\\,160" in cor
    assert "for the stable group it is both the flag count and the edge count" in cor
    # the kernel incidence is a theorem-derived count, not a returned row
    eight = text[text.index("#cor:coble-eight-standard-line-counts"):]
    eight = eight[: eight.index("::: {.proposition")]
    assert "569\\,160" in eight and "189\\,720" in eight and "527" in eight
    assert "527\\cdot1080=189\\,720\\cdot3=569\\,160" in eight


def test_a6_kernel_incidence_row_is_not_claimed_returned():
    text = PAGE.read_text()
    assert "sage-extensions#381" in text
    para = next(p for p in text.split("\n\n") if p.startswith("*What the rows do not establish.*"))
    assert "without printing either incidence row" in para
    assert "did not return either public kernel incidence row" in para
    # The sentence that stood here said the pending public computation had not returned.  It
    # has: the endpoint relation returned both kernel rows with these counts (job 44392429173),
    # and the paragraph now says so while keeping the edge certificates separate.  The guard is
    # that the theorem-derived values are not read off a returned edge list, and that the
    # row's own failure is still recorded.
    assert ("theorem-derived values are not a claim that the pending public computation has returned" in para
            or "The theorem-derived values are not read off a returned edge list" in para)
    forbidden = re.compile(r"kernel[- ]incidence (row|relation) (has )?returned", re.IGNORECASE)
    for path in (ROOT / "writing").rglob("*.md"):
        assert not forbidden.search(path.read_text(errors="replace")), path


# ---------------------------------------------------------------------------
# A7: records are not cards; the card has an owner.
# ---------------------------------------------------------------------------

def test_a7_rows_are_records_and_the_card_is_owned():
    text = PAGE.read_text()
    assert "These plane and incidence rows are computation records in sage-extensions, not lattice-database card fields." in text
    assert "lattice-database#7" in text
    assert "#7 therefore remains open against its original acceptance" in text
    # the two rows' numbers are not attributed to a card
    para = next(p for p in text.split("\n\n") if p.startswith("*The cusp rows and the incidence row.*"))
    assert "they enter no card" in para or "No count in this remark is read off a card" in para


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items()) if name.startswith("test_")]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

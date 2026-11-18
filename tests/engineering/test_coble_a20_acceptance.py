"""Acceptance gate for research#663 (A20): the four arithmetic groups.

The acceptance is the third comment on the issue, item by item:

  item 1   the Heegner description against the congruence description.  The
           condition is gamma(A_{U(2)}) = A_{U(2)}, and whether it is a
           condition at all depends on the U(2)/E8(2) decomposition of
           A_{S_En} (order 1024) and of A_{S_Co} (order 2048): (a) whether it
           is O(q)-invariant, (b) whether the gluing the provider builds is
           block-compatible.  If the decomposition is invariant, the Heegner
           description is the congruence one and item 1 closes; otherwise the
           item stays with #664 and the record states which condition remains.
           Every page citing the open form is updated.
  item 2   Gamma^dir: the reduction recorded as its own step, not claimed.
  item 3   Gamma^geom: a direct period theorem, recorded as having no lattice
           statement.
  #720     the six absorbed entries, one line each on what each would need,
           so the issue can be split: (D1), (RI), (REL), (INV), and the pair
           no page formulates.

Each test names the smallest input that decides its item.  For (a) and (b) that
is the committed transcript of computations/reports/coble_a20-enriques-gluing-block.py
and, for the Coble side, of coble_gluing_discriminants.py: the orbit partition,
the block test, and the two elementary sums that say the partitions cover the
module.  For the prose items it is the statement on the page that carries them,
never a re-derivation.  No Sage and no provider call: these are checks on
committed records and on arithmetic, and they decide nothing that a provider
owes.

The witness pair is checked in both directions -- transcript against page --
because the two runs of the record pick different representatives of one orbit,
and the page quotes what the transcript prints or it quotes nothing.

Run standalone (``python3 tests/engineering/test_coble_a20_acceptance.py``) or
under pytest; the module imports nothing outside the standard library.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "computations/reports"

PAGE = ROOT / "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
OPEN_PROBLEMS = ROOT / "writing/coble/open-problems/open-problems.md"
OPEN_QUESTIONS = ROOT / "writing/open-questions.md"
REPORT = ROOT / "writing/coble/heegner-report/coble-heegner-research-report.md"

RECORD_EN = REPORTS / "coble_a20-enriques-gluing-block.py"
RUN_EN = REPORTS / "coble_a20-enriques-gluing-block-run.txt"
RECORD_CO = REPORTS / "coble_gluing_discriminants.py"
RUN_CO = REPORTS / "coble_gluing_discriminants-run.txt"
RECORD_EN_OLD = REPORTS / "coble_a20-block-invariance.py"
RUN_EN_OLD = REPORTS / "coble_a20-block-invariance-run.txt"
RUN_CAPS = REPORTS / "coble_a20-owner-capabilities-run.txt"
RECORD_CAPS = REPORTS / "coble_a20-owner-capabilities.py"


def _text(path: Path) -> str:
    assert path.is_file(), f"missing {path.relative_to(ROOT)}"
    return path.read_text()


def _block(text: str, start: str) -> str:
    """The fenced unit beginning at the line containing ``start``, up to its closing ``:::``."""
    i = text.index(start)
    j = text.index("\n:::\n", i)
    return text[i:j]


# ---------------------------------------------------------------------------
# item 1(a): the U(2)/E8(2) decompositions are not O(q)-invariant.
# ---------------------------------------------------------------------------

def test_item1a_enriques_partition_is_three_orbits_covering_the_module():
    """A_{S_En} has 1024 classes; the record's three orbits must cover it.

    Decides: whether the recorded orbit partition is a partition of the whole
    module -- 1 + 496 + 527 = 1024 -- and that the U(2) block meets all three
    orbits without being one of them.
    """
    run = _text(RUN_EN)
    m = re.search(r"orbits of O\(q_\{S_En\}\) on the (\d+) classes: (\d+), sizes \[([\d, ]+)\]", run)
    assert m, "the transcript does not print the orbit partition of O(q_{S_En})"
    cardinality, count, sizes = int(m.group(1)), int(m.group(2)), [int(s) for s in m.group(3).split(",")]
    assert cardinality == 1024
    assert count == len(sizes) == 3
    assert sizes == [1, 496, 527]
    assert sum(sizes) == cardinality
    assert "the decomposition is O(q_{S_En})-invariant: False" in run
    # the block meets three orbits, in 1, 1 and 2 classes
    inside = re.findall(r"orbit of size\s+(\d+): (\d+) of its classes inside the U\(2\) block", run)
    assert [(int(a), int(b)) for a, b in inside] == [(1, 1), (496, 1), (527, 2)]
    assert sorted(int(b) for _, b in inside) and sum(int(b) for _, b in inside) == 4


def test_item1a_coble_partition_is_six_orbits_covering_the_module():
    """A_{S_Co} has 2048 classes; the six recorded orbits must cover it.

    Decides the same question for the Coble side, which is where the cycle
    in @prop:gamma-cong-eq-heegner(4) lives.
    """
    run = _text(RUN_CO)
    m = re.search(r"orbits on the (\d+) classes: (\d+), sizes \[([\d, ]+)\]", run)
    assert m, "the transcript does not print the orbit partition of O(q_{S_Co})"
    cardinality, count, sizes = int(m.group(1)), int(m.group(2)), [int(s) for s in m.group(3).split(",")]
    assert cardinality == 2048
    assert count == len(sizes) == 6
    assert sizes == [1, 1, 496, 496, 527, 527]
    assert sum(sizes) == cardinality
    assert "orbits meeting the U(2) block but not contained in it: 2" in run


def test_item1a_the_page_proves_what_the_record_computes():
    """The page's orbit counts and the record's must be the same counts.

    Decides: that the non-invariance is not carried by the record alone.  The
    lemma states it as a theorem (Witt plus a count), and its numbers are the
    record's numbers.
    """
    page = _text(PAGE)
    lemma = _block(page, '{.lemma #lem:coble-discriminant-blocks')
    assert "the $527$ nonzero classes with $q = 0$" in lemma
    assert "the $496$ classes with $q = 1$" in lemma
    assert "some $g\\in\\Orth(q_A)$ has $g(A_{U(2)})\\neq A_{U(2)}$" in lemma
    # 3*136 + 1*120 = 528 isotropic classes and 3*120 + 1*136 = 496 of value 1, on A^0
    assert 3 * 136 + 1 * 120 == 528
    assert 3 * 120 + 1 * 136 == 496
    assert 1 + 527 + 496 == 1024


# ---------------------------------------------------------------------------
# item 1(b): the gluing the provider builds is not block-compatible.
# ---------------------------------------------------------------------------

def test_item1b_enriques_block_test_and_its_scope():
    """gamma = A_{S_En}.isometry_to(A_{T_En}(-1)): anti-isometry, block test False.

    Decides the Heegner half of item 1.  The anti-isometry identity must hold on
    every class of the two blocks -- 4 + 256 less the shared zero class is 259 --
    and the image of the U(2) block must lie in neither block.
    """
    run = _text(RUN_EN)
    assert "isometry-to-the-twist check q_{T_En(-1)}(gamma z) = q_{S_En}(z) on all 259 classes" in run
    assert "block-compatible on this gamma: False" in run
    assert "gamma(U(2))  == A_{U(2)} of T_En : False" in run
    assert "inside the U(2) block: False   inside the E8(2) block: False" in run
    # the scope the acceptance demands: the record says what it does not decide
    assert "not about the gluing of the marked embedding" in run
    assert "prob:coble-rigidity" in run


def test_item1b_coble_block_test_covers_three_blocks():
    """gamma_Co on A_{S_Co}: all three block checks False on 2048 classes.

    Decides the theta half of item 1, as @prop:gamma-cong-eq-heegner(4) needs it.
    """
    run = _text(RUN_CO)
    assert "isometry-to-the-twist check q_{T(-1)}(gamma x) = q_S(x) on all 260 classes" in run
    assert "block-compatible on this gamma: False" in run
    for block in ("order-2 block  gamma(<K>) == <1> : False",
                  "U(2) block     gamma(U)   == U   : False",
                  "E8(2) block    gamma(E8)  == E8  : False"):
        assert block in run
    assert 2 * 4 * 256 == 2048


def test_item1b_page_quotes_the_witness_the_transcript_prints():
    """The page's witness pair is the transcript's, both classes and both values.

    Decides: that the remark and the record agree on the object they quote.  The
    two runs of the record choose different representatives of one orbit, so the
    page must quote the committed one.
    """
    run = _text(RUN_EN)
    x = re.search(r"x = (\[.*?\])\s+\(inside the U\(2\) block, q = (\d+)\)", run)
    y = re.search(r"y = (\[.*?\])\s+\(outside the U\(2\) block, q = (\d+)\)", run)
    assert x and y, "the transcript does not print the witness pair"
    xs = x.group(1).replace(" ", "")
    ys = y.group(1).replace(" ", "")
    assert x.group(2) == y.group(2) == "1"
    remark = _block(_text(PAGE), '{.remark title="The block condition is satisfiable')
    assert f"${xs}$" in remark.replace(" ", "").replace("$[0]+[1]$", "$[0]+[1]$")
    assert f"${ys}$" in remark
    assert "orbit of size $496$" in remark


def test_item1b_block_compatibility_is_neither_vacuous_nor_automatic():
    """The lemma states both an anti-isometry that preserves the block and one that does not.

    Decides: that the hypothesis of @prop:gamma-cong-eq-heegner(2) is satisfiable
    and not automatic -- item (5) together with item (4).  Without (5), (4)'s
    "if gamma is block-compatible then gamma o g is not" has no antecedent.
    """
    page = _text(PAGE)
    lemma = _block(page, '{.lemma #lem:coble-discriminant-blocks')
    assert "if $A'$ is a second form of the shapes above with the same two summands" in lemma
    assert "then there is an anti-isometry $A\\too A'$ with $\\gamma(A_{U(2)}) = A_{U(2)}$, and one without that property." in lemma
    proof = _block(page, "::: {.proof}\n\nWrite $H = A_{U(2)}$")
    assert "(5) The map that is the identity on each of the two summands" in proof
    assert "where $q = -q$" in proof


def test_item1b_the_body_s_explicit_isometry_constructor_exists_at_this_runtime():
    """The body records the twisted explicit isometry as unavailable; both transcripts have one.

    Decides the capability half of item 1's body at the runtime the records were made on: the
    object returned is a typed isometry of torsion forms, it is built against the TWISTED target
    (``A(...).twist(-1)``), the untwisted answer is True, and the anti-isometry identity holds on
    every class of the blocks.  What stays open next to it is not this operation but the marking.
    """
    for run_name, target in ((RUN_EN, "A_{T_En}(-1)"), (RUN_CO, "A_{T_Co}(-1)")):
        run = _text(run_name)
        assert f"isometry_to({target})" in run
        assert "is_anti_isometric(A_{T_" in run and "= True" in run
        assert "built: OwnedTorsionFormIsometryMor" in run
        assert "isometry-to-the-twist check q_" in run and ": True" in run
    assert "A_{S_En}.is_anti_isometric(A_{T_En}) = True" in _text(RUN_EN)
    assert "A_{S_Co}.is_anti_isometric(A_{T_Co}) = True" in _text(RUN_CO)


def test_item1a_body_surjectivity_call_returns_true_at_this_runtime():
    """#663 item 1(a) of the body: T_Co.discriminant_representation_is_surjective().

    Decides: the operation the body records as raising at the pinned provider returns True at the
    runtime the checkouts carry, with its three controls, and the record names the method's line.
    It decides the capability, not the mathematics behind it (@thm:two-elementary-surjectivity).
    """
    run = _text(RUN_CAPS)
    assert "lattices.py:4226" in run
    assert "T_Co.discriminant_representation_is_surjective() = True" in run
    for control in ("S_Co  -> True", "T_En  -> True", "S_En  -> True"):
        assert control in run
    assert "prob:coble-rigidity" in run          # the scope the record declares


def test_item1b_body_twisted_isometry_holds_on_every_class():
    """#663 item 1(b) of the body: the explicit twisted anti-isometry on all 1024 classes.

    Decides: the object exists, is typed, is built against the TWISTED target, satisfies
    q_T o gamma = -q_S on every class and is injective there.
    """
    run = _text(RUN_CAPS)
    assert "A_{S_En}.isometry_to(A_{T_En}(-1))   = OwnedTorsionFormIsometryMor" in run
    assert "q_{T_En(-1)}(gamma x) = q_{S_En}(x) on all 1024 classes: True" in run
    assert "distinct images: 1024" in run
    assert "A_{S_En}.is_anti_isometric(A_{T_En}) = True" in run


# ---------------------------------------------------------------------------
# item 1, the pages the acceptance names.
# ---------------------------------------------------------------------------

def test_item1_pages_citing_the_open_form_are_updated():
    """@prop:gamma-cong-eq-heegner is followed by the computed remark, and the register agrees.

    Decides the last clause of item 1's acceptance.  The two remarks the
    acceptance names were folded into one by the house-style pass; what the
    check enforces is that a remark carrying the computation sits with the
    proposition, and that both registers state the condition that remains.
    """
    page = _text(PAGE)
    prop_at = page.index("{.proposition #prop:gamma-cong-eq-heegner")
    remark_at = page.index('{.remark title="The block condition is satisfiable')
    next_header = page.index("\n## ", prop_at)
    assert prop_at < remark_at < next_header, "the remark is not attached to the proposition"
    remark = _block(page, '{.remark title="The block condition is satisfiable')
    assert "coble_a20-enriques-gluing-block.py" in remark
    assert "@qst:gamma-co-generators(2)" in remark
    assert "@prob:coble-rigidity" in remark

    q = _text(OPEN_PROBLEMS)
    item2 = next(line for line in q.splitlines() if line.startswith("2. Are the subgroups"))
    assert "@def:congruence-group" in item2 and "@prop:gamma-cong-eq-heegner" in item2
    assert "\\gamma_\\Co(A_{U(2)})" in item2

    row = next(line for line in _text(OPEN_QUESTIONS).splitlines()
               if line.startswith("| **Equality of the four arithmetic groups**"))
    assert "@prob:group-identification" in row
    assert "@qst:gamma-co-generators" in row
    assert "@prob:coble-rigidity" in row and "@prob:B24" in row and "@prob:B25" in row


# ---------------------------------------------------------------------------
# item 2: Gamma^dir, a reduction and not a claim.
# ---------------------------------------------------------------------------

def test_item2_the_unlabelled_comparison_is_a_page_proposition():
    """The settled half of item 2: one isometry of L_K3 carries the Coble datum to the Enriques one.

    Decides: that the body's "the unlabelled comparison of the two polarizations is settled in the
    affirmative" is carried by a statement, not by prose -- Phi(S_Co) = M, Phi(T_Co) =
    delta^perp, Phi(H) = h -- while the labels stay with A21.
    """
    page = _text(PAGE)
    prop = _block(page, "{.proposition #prop:coble-enriques-polarized-match")
    assert "\\Phi(S_\\Co) = M" in prop
    assert "\\Phi(T_\\Co) = \\delta^{\\perp\\ten}" in prop
    assert "\\Phi(H) = h" in prop
    assert "@prob:coble-rigidity" not in prop  # the labels are not claimed here


def test_item2_the_two_half_fibres_have_the_numbers_the_proposition_uses():
    """The arithmetic of item 2's settled half, on the page's own displayed classes.

    Decides: F_1 = 3H - sum_{i<=9}E_i and F_2 = 3H - sum_{i<=8}E_i - E_10 on the plane model
    (H^2 = 1, H.E_i = 0, E_i^2 = -1) have F_i^2 = 0, F_1.F_2 = 1 and (F_1+F_2)^2 = 2, which is
    what @prop:coble-enriques-polarized-match transports to h = e+f in U(2).
    """
    page = _text(PAGE)
    assert "F_1 = 3H_{\\PP^2}-\\Sum_{i\\le9}E_i" in page
    assert "F_2 = 3H_{\\PP^2}-\\Sum_{i\\le8}E_i-E_{10}" in page
    assert "F_i^2 = 0$, $F_1\\cdot F_2 = 1" in page

    def dot(a, b):                      # (H, E_1..E_10) in diag(1, -1, ..., -1)
        return a[0] * b[0] - sum(x * y for x, y in zip(a[1:], b[1:]))

    F1 = (3,) + (-1,) * 9 + (0,)
    F2 = (3,) + (-1,) * 8 + (0, -1)
    assert dot(F1, F1) == 0
    assert dot(F2, F2) == 0
    assert dot(F1, F2) == 1
    assert dot(tuple(x + y for x, y in zip(F1, F2)), tuple(x + y for x, y in zip(F1, F2))) == 2


def test_item2_direct_group_is_defined_and_its_comparison_handed_on():
    """Decides: Gamma^dir is a named group whose comparison is the labeled embedding.

    The report must define it, tie it to labeled rigidity, and say which equality
    needs which argument; nothing may assert the equality.
    """
    report = _text(REPORT)
    direct = _block(report, "{.definition #def:direct-group")
    assert "Z_{O(L_{K3})}(I_{\\Co},I_{\\mathrm{dP}})_{H,\\alpha,\\mcc}" in direct
    assert "provided the labeled rigidity theorem holds" in report
    groups = _block(report, "{.problem #prob:group-identification")
    assert "\\Gamma_{\\Co,2}^{\\mathrm{geom}}\n =\\Gamma_{\\Co,2}^{\\mathrm{dir}}" in groups
    assert "labeled embedding comparison for the second" in groups
    assert "no relation between $\\Gamma_{\\Co}^{\\mathrm{dir}}$ and $\\Gamma_\\Co$ is established" in report


# ---------------------------------------------------------------------------
# item 3: Gamma^geom, a period theorem with no lattice statement.
# ---------------------------------------------------------------------------

def test_item3_geometric_entry_is_a_period_theorem():
    """Decides: Gamma^geom is monodromy of the direct stack, named to B24 and B25."""
    report = _text(REPORT)
    geom = _block(report, "{.definition #def:geometric-monodromy")
    assert "orbifold monodromy representation" in geom
    assert "{.problem #prob:B24 title=\"B2.4. Direct global Torelli theorem\"}" in report
    assert "{.problem #prob:B25 title=\"B2.5. Direct monodromy theorem\"}" in report
    assert "global Torelli and parallel transport for the first" in report


# ---------------------------------------------------------------------------
# the absorbed #720 entries.
# ---------------------------------------------------------------------------

def test_absorbed_d1_is_b25_with_the_unpolarized_definition():
    """(D1) monodromy maximality: the monodromy equals the labeled centralizer, off-lattice."""
    report = _text(REPORT)
    assert "geometric monodromy group equal the labeled centralizer group" in report
    unpolarized = _block(report, "{.definition #def:unpolarized-direct-group")
    assert "remains a geometric monodromy statement until the direct period theorem is proved" in unpolarized


def test_absorbed_ri_is_the_index_of_the_reflection_group():
    """(RI) ker rho_T = W, in decidable form: the index of W(T_Co)."""
    q = _text(OPEN_PROBLEMS)
    item3 = next(line for line in q.splitlines() if line.startswith("3. Let $W(T_\\Co)$"))
    assert "[\\widetilde\\Orth^+(T_\\Co) : W(T_\\Co)]" in item3
    assert "@prop:gamma-co-reflective-set" in item3


def test_absorbed_ri_names_the_input_that_would_settle_it():
    """(RI) as an entry the issue can be split on: the statement, and what it needs.

    Decides: the index question names the missing input -- a finite presentation of W(T_Co) with
    its chamber -- in the owning question, and the register points at that question instead of
    restating it.  Without this the entry states a question and no way to attack it.
    """
    page = _text(PAGE)
    qst = _block(page, "{.question #qst:gamma-co-reflection-index")
    assert "What would settle it is a finite set of reflections generating $W(T_\\Co)$" in qst
    assert "a Coxeter presentation of $W(T_\\Co)$" in qst
    assert "exactly when that chamber has finite volume" in qst
    assert "@prop:gamma-co-reflective-set" in qst
    item3 = next(line for line in _text(OPEN_PROBLEMS).splitlines()
                 if line.startswith("3. Let $W(T_\\Co)$"))
    assert "@qst:gamma-co-reflection-index" in item3


def test_absorbed_inv_names_the_input_that_would_settle_it():
    """(INV): the question, and the input it needs, at the statement that asks it.

    Decides: the root-arrangement question names what would settle it -- an effective-Torelli or
    lift-to-automorphism input, of which @prob:B24 is the direct statement -- and says why no
    computation on the lattice decides it.  Without that line the entry is a question with no
    attack, which is what #663's acceptance asks each absorbed entry not to be.
    """
    page = _text(PAGE)
    qst = _block(page, "{.question #qst:kernel-and-root-arrangement")
    assert "preserve the $(-2)$-root arrangement of the tuple" in qst
    assert "What would settle it is an effective-Torelli or lift-to-automorphism input" in qst
    assert "@prob:B24" in qst
    assert "effectivity is a property of a member and its Kähler cone" in qst


def test_absorbed_rel_is_the_splitting_question():
    """(REL): a section of rho_T normalizing W(T_Co) and a homomorphism modulo it."""
    q = _text(OPEN_PROBLEMS)
    item4 = next(line for line in q.splitlines() if line.startswith("4. Does $\\rho_{T_\\Co}$"))
    assert "\\sigma(p)w\\sigma(p)^{-1}\\in W(T_\\Co)" in item4
    assert "\\sigma(p)\\sigma(q)\\sigma(pq)^{-1}\\in W(T_\\Co)" in item4
    assert "W(T_\\Co)\\rtimes P" in item4


def test_absorbed_inv_is_asked_as_a_question_on_the_page():
    """(INV): the (-2)-root arrangement of the tuple."""
    page = _text(PAGE)
    qst = _block(page, "{.question #qst:kernel-and-root-arrangement")
    assert "preserve the $(-2)$-root arrangement of the tuple" in qst
    assert "Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha}" in qst


def test_absorbed_pair_without_a_page_formulation_is_reported_not_invented():
    """The two remaining absorbed entries have no statement under writing/ to attach to.

    Decides the finding rather than a gap: a pair no page formulates cannot be
    recorded against a page.  The check pins the fact, so that a later
    formulation of either one fails here and gets its one line.
    """
    book = ROOT / "writing"
    hits = []
    for path in book.rglob("*.md"):
        if ".book" in path.parts:
            continue
        text = path.read_text(errors="ignore")
        for name in ("G_3", "G_4"):
            if re.search(r"(?<![\\A-Za-z])" + re.escape(name) + r"(?![0-9A-Za-z])", text):
                hits.append(f"{path.relative_to(ROOT)}:{name}")
    assert hits == [], f"a page now formulates one of the absorbed pair: {hits}"


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

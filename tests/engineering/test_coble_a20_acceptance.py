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
    proposition, and that both registers state where the block question stands.
    Updated when the block condition was decided: the remark now points at the
    decision instead of naming it as the remaining condition, the register row
    carries the resulting equality, and the open problem no longer lists the
    answered item.
    """
    page = _text(PAGE)
    prop_at = page.index("{.proposition #prop:gamma-cong-eq-heegner")
    remark_at = page.index('{.remark title="The block condition is satisfiable')
    next_header = page.index("\n## ", prop_at)
    assert prop_at < remark_at < next_header, "the remark is not attached to the proposition"
    remark = _block(page, '{.remark title="The block condition is satisfiable')
    assert "coble_a20-enriques-gluing-block.py" in remark
    assert "@prob:coble-rigidity" in remark
    # the condition is now decided, and the remark says where
    assert "@prop:coble-block-compatibility" in remark
    assert "@prop:coble-enriques-ambient-isometry" in remark

    q = _text(OPEN_PROBLEMS)
    # the answered item has left the question; the two that remain keep their order
    assert "2. Are the subgroups" not in q
    assert "3. Let $W(T_\\Co)$" not in q
    assert "2. Let $W(T_\\Co)$" in q
    assert "3. Does $\\rho_{T_\\Co}$ admit a section" in q
    assert "with item 2 it would make the congruence group" in q
    # and the question says where its block half was decided
    assert "@prop:coble-block-compatibility" in _block(
        q, "{.question #qst:gamma-co-generators")

    # the four-group question is settled, so its register row has left the table
    table = _text(OPEN_QUESTIONS)
    assert "| **Equality of the four arithmetic groups**" not in table
    groups = _block(_text(REPORT), "{.problem #prob:group-identification")
    assert "@cor:four-groups-decided" in groups
    assert "@prob:B25" in groups


def test_item1c_the_block_test_is_in_the_record_and_the_transcript_decides_it():
    """The block condition of @def:congruence-group is decided on the marked gluings.

    Decides: that the answer on the page is backed by a run, that the run tests
    both gluings, that the search over each target block is exhaustive (4 and
    256 candidates, one image per class), and that both answers are affirmative.
    """
    page = _text(PAGE)
    prop = _block(page, "{.proposition #prop:coble-block-compatibility")
    assert "\\gamma_\\Co(A_{U(2)}) = A_{U(2)}" in _block(
        page, "{.proof}\n\nThe test is `computations/reports/coble_a21-ambient-extension.py`")
    assert "not block-compatible" not in prop

    cor = _block(page, "{.corollary #cor:gamma-hdg-is-congruence")
    assert "\\Gamma^{\\mathrm{Hdg}}_\\Co = \\Gamma^\\theta_\\Co" in cor

    run = _text(REPORTS / "coble_a21-ambient-extension-run.txt")
    script = _text(REPORTS / "coble_a21-ambient-extension.py")
    assert "6. the block test of @def:congruence-group" in script
    lines = run.splitlines()
    start = next(i for i, line in enumerate(lines)
                 if line.startswith("6. the block test of @def:congruence-group"))
    block = "\n".join(lines[start:])
    assert "Coble: gamma_Co is block-compatible" in block
    assert "Enriques: gamma_En is block-compatible" in block
    assert "NOT block-compatible" not in block
    # exhaustive on both blocks, on both sides
    assert block.count("the whole block: 255 of the 255 nonzero classes have exactly one image"
                       " inside it") == 2
    assert block.count("the blocks, as class sets: source U(2) 4, source E8(2) 256,"
                       " target U(2) 4, target E8(2) 256") == 2
    assert block.count("gamma carries the U(2) block to the U(2) block: True") == 2
    # the third block too, on the Coble side
    assert "the remaining square-2 direction: [alpha/2] lands on [0]" in block


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


def test_item2b_the_direct_group_equals_the_heegner_one():
    """The second equality of the four, for the centralizer without the chamber subscript.

    Decides: that @prop:direct-eq-heegner states the equality, that its proof names the two
    computed inputs (alpha^perp cap S_Co = S_En, and the action of I_dP on the pieces), that
    it rests on block-compatibility and on the surjectivity facts already on record, and that
    the record's part 7 prints both inputs as checked.
    """
    page = _text(PAGE)
    prop = _block(page, "{.proposition #prop:direct-eq-heegner")
    assert "\\Gamma^{\\mathrm{dir}}_{\\Co,2} = \\Gamma^{\\mathrm{Hdg}}_{\\Co,2}" in prop
    assert "@thm:chamber-pinned-by-labels" in prop  # the chamber is in the datum, and redundant

    proof = _block(page, "{.proof}\n\n*The $S$-side of the centralizer.*")
    assert "part 7 of `computations/reports/coble_a21-ambient-extension.py`" in proof
    assert "\\alpha^{\\perp}\\cap S_\\Co = S_\\En" in proof
    assert "@prop:gamma-co-heegner-strict" in proof
    assert "@prop:coble-block-compatibility" in proof

    run = _text(REPORTS / "coble_a21-ambient-extension-run.txt")
    lines = run.splitlines()
    start = next(i for i, line in enumerate(lines)
                 if line.startswith("7. the direct labelled group against the Heegner one"))
    block = "\n".join(lines[start:])
    assert "equal True" in block            # alpha^perp cap S_Co = S_En
    assert "rank 10, det -1024, sig (1, 9)" in block
    assert "+1 on the slot: I_dP(e) = e True, I_dP(f) = f True" in block
    assert "-1 on Delta(E8): True over the eight generators" in block
    assert "-1 on ZZ alpha: I_dP(alpha) = -alpha True" in block
    assert "-1 on T_Co: True over a basis of T_Co" in block


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

def test_item2b_the_chamber_subscript_stands_and_is_preserved():
    """A20 item 2 as the issue states it: the object carries the chamber mcc.

    Decides: the equality is stated for the centralizer WITH the chamber in its datum, and the
    chamber is not dropped but proved redundant -- every element of the centralizer preserves it
    (@thm:chamber-pinned-by-labels).  Both the page and the definition of the issue's group say
    so, and no page leaves the preservation open.  A page that proves the equality for a
    subscript-free variant is what the review rejected.
    """
    page = _text(PAGE)
    proof = page[page.index("::: {.proof}", page.index("{.proposition #prop:direct-eq-heegner")):]
    chamber = proof[proof.index("*The chamber.*"):]
    assert "carries the subscript $\\mcc$" in chamber
    assert "every element of the centralizer preserves it" in chamber
    assert "Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha,\\mcc} = Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha}" in chamber
    assert "@thm:chamber-pinned-by-labels" in chamber
    definition = _block(_text(REPORT), "{.definition #def:direct-group")
    assert "The chamber $\\mcc$ is part of this datum" in definition
    assert "@thm:chamber-pinned-by-labels" in definition
    assert "@qst:kernel-and-root-arrangement" not in _text(REPORT)
    assert "@qst:kernel-and-root-arrangement" not in page


def test_item2b_the_theorem_has_its_three_parts_and_its_scope():
    """The input of the preservation: the (-2)-classes, the chamber, the action, and the scope.

    Decides: the theorem's three clauses are the proof's content, the two inputs it uses are
    named -- Riemann-Roch plus the nefness of H, and @lem:face-at-H part 2 -- and the scope, a
    member whose Picard lattice is the invariant lattice, is stated together with the mechanism
    that makes it a scope rather than an ornament.
    """
    page = _text(PAGE)
    thm = _block(page, "{.theorem #thm:chamber-pinned-by-labels")
    assert "\\Delta_b = \\set{\\delta\\in S_{\\Co,b} : \\delta^2 = -2,\\ H_b\\cdot\\delta>0}\\cup\\set{\\alpha_b}" in thm
    assert "x\\cdot\\delta>0 \\ \\text{for every}\\ \\delta\\in\\Delta_b" in thm
    assert "\\psi(\\Delta_b) = \\Delta_b" in thm and "\\psi(\\mcc_b) = \\mcc_b" in thm
    assert "Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha,\\mcc} = Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha}" in thm
    proof = _block(page, "{.proof}\n\n*The classes of square $-2$.*")
    assert "Riemann–Roch" in proof
    assert "h^0(\\delta)+h^0(-\\delta) = 1+h^1(\\delta)\\ge1" in proof
    assert "@lem:face-at-H, part 2" in proof
    scope = _block(page, "{.remark #rmk:chamber-pinned-scope")
    assert "\\Pic(\\widehat X_b) = S_{\\Co,b}" in scope
    assert "s_\\delta$ fixes $H_b$ and $\\alpha_b$" in scope
    assert "@thm:automorphism-lifting-criterion" in scope


def test_item3_geometric_entry_is_decided_by_the_direct_period_theorems():
    """A20 item 3: Gamma^geom, by the two period theorems that were its named input.

    Decides: the entry is no longer a period theorem owed but a monodromy group identified.
    @prob:B24 is decided with its arrangement-complement form refuted -- the image is a
    complement of a proper, nonempty set of Heegner divisors -- and @prob:B25 is proved by
    taking the marked moduli to be the complement of that subarrangement: a connected,
    Gamma_lab-saturated set, so the marking cover is a regular covering with deck group
    Gamma_lab and the monodromy is its deck group.
    """
    report = _text(REPORT)
    geom = _block(report, "{.definition #def:geometric-monodromy")
    assert "orbifold monodromy representation" in geom

    b24 = _block(report, "{.theorem #prob:B24")
    assert "the period image, decided" in b24
    assert "no period of the construction lies on a wall" in b24
    assert "the reading of B2.4 that identifies it with the complement of the whole divisorial locus" in b24
    assert "is **false**" in b24
    b24_proof = _block(report, "{.proof}\n\n*The image.*")
    assert "smwo_direct-period.md" in b24_proof
    assert "decided member by member rather than by a dominance argument" in b24_proof
    assert "121" in b24_proof

    b25 = _block(report, "{.theorem #prob:B25")
    assert "geometric monodromy group coincide" in b25
    assert "if the $\\{\\pm1\\}$-cover of the period image is nontrivial" in b25
    assert "if it splits" in b25
    b25_proof = _block(report, "{.proof}\n\n*The two groups.*")
    assert "\\Gamma_{\\mathrm{lab}} = \\Gamma^{\\mathrm{dir}}_{\\Co,2}" in b25_proof
    assert "@lem:chamber-from-marked-period the marked moduli injects" in b25_proof
    assert "the complement of a locally finite union of proper closed analytic subsets" in b25_proof
    assert "and not $\\Gamma_{\\mathrm{lab}}$" in b25_proof

    cor = _block(report, "{.corollary #cor:four-groups-decided")
    assert "\\Gamma^{\\mathrm{dir}}_{\\Co,2} = \\Gamma^{\\mathrm{Hdg}}_{\\Co,2} = \\Gamma^\\theta_\\Co" in cor
    assert "or $\\Gamma^{\\mathrm{dir}}_{\\Co,2}/\\{\\pm1\\}$" in cor
    assert "s_\\zeta" in cor


# ---------------------------------------------------------------------------
# the absorbed #720 entries.
# ---------------------------------------------------------------------------

def test_absorbed_d1_monodromy_maximality_is_b25_proved():
    """(D1) monodromy maximality: the monodromy is the labeled centralizer group.

    Decides: the entry that awaited the direct period theorem is discharged by it -- the deck
    group and the monodromy are both Gamma^dir -- while the *unpolarized* statement, which is a
    different moduli problem, keeps its own status.
    """
    report = _text(REPORT)
    b25 = _block(report, "{.theorem #prob:B25")
    assert "geometric monodromy group coincide" in b25
    assert "if the $\\{\\pm1\\}$-cover of the period image is nontrivial" in b25
    assert "if it splits" in b25
    assert "in either case" in b25
    unpolarized = _block(report, "{.definition #def:unpolarized-direct-group")
    assert "remains a geometric monodromy statement until the direct period theorem is proved" in unpolarized


def test_absorbed_ri_is_the_index_of_the_reflection_group():
    """(RI) ker rho_T = W, in decidable form: the index of W(T_Co)."""
    q = _text(OPEN_PROBLEMS)
    item2 = next(line for line in q.splitlines() if line.startswith("2. Let $W(T_\\Co)$"))
    assert "[\\widetilde\\Orth^+(T_\\Co) : W(T_\\Co)]" in item2
    assert "@prop:gamma-co-reflective-set" in item2


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
    item2 = next(line for line in _text(OPEN_PROBLEMS).splitlines()
                 if line.startswith("2. Let $W(T_\\Co)$"))
    assert "@qst:gamma-co-reflection-index" in item2


def test_absorbed_inv_is_answered_by_the_theorem():
    """(INV): every g in Z(O(lkt))(I_Co,I_dP)_{H,alpha} preserves the tuple's (-2)-root arrangement.

    Decides: the page answers the entry rather than asking it -- the arrangement is read off from
    the two labels at a member whose Picard lattice is the invariant lattice -- and records why
    the earlier formulation expected an effective-Torelli input: effectivity is decided by the
    nef class H together with Riemann-Roch, and the centralizer's infinity does not put the
    question beyond a lattice argument.
    """
    page = _text(PAGE)
    rmk = _block(page, "{.remark #rmk:root-arrangement-answered")
    assert "preserves the $(-2)$-root arrangement $\\Delta_b$ of the tuple" in rmk
    assert "exactly one of $\\pm\\delta$ is effective for a class of square $-2$" in rmk
    assert "Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha}" in rmk
    assert "@rmk:chamber-pinned-scope" in rmk
    assert "{.question #qst:kernel-and-root-arrangement" not in page


def test_absorbed_rel_is_the_splitting_question():
    """(REL): a section of rho_T normalizing W(T_Co) and a homomorphism modulo it."""
    q = _text(OPEN_PROBLEMS)
    item3 = next(line for line in q.splitlines() if line.startswith("3. Does $\\rho_{T_\\Co}$ admit a section"))
    assert "\\sigma(p)w\\sigma(p)^{-1}\\in W(T_\\Co)" in item3
    assert "\\sigma(p)\\sigma(q)\\sigma(pq)^{-1}\\in W(T_\\Co)" in item3
    assert "W(T_\\Co)\\rtimes P" in item3


def test_absorbed_inv_names_the_member_where_it_holds():
    """(INV): the scope, at the statement that answers it.

    Decides: the answer is not left unscoped -- the member whose Picard lattice is the invariant
    lattice is named, the larger-Picard-lattice case is named as the one the argument does not
    reach, and the mechanism there is the reflection in an effective class of square -2 outside
    the invariant lattice.
    """
    page = _text(PAGE)
    rmk = _block(page, "{.remark #rmk:root-arrangement-answered")
    assert "at a member whose Picard lattice is the invariant lattice" in rmk
    scope = _block(page, "{.remark #rmk:chamber-pinned-scope")
    assert "the member with a larger Picard lattice" in rmk
    assert "does not reach" in rmk
    assert "negates the effective class $\\delta$" in scope


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



def test_absorbed_ri_unrestricted_form_is_false():
    """(RI) as the issue states it: ker rho_T = W.  Decided, negatively.

    Decides: the reflection in the square-2 summand lies in the congruence kernel -- every
    pairing in T_Co is even, so it is trivial modulo 2T -- and outside O^+(T_Co), where every
    reflection in a square-(-2) vector lies; so the kernel is strictly larger than the
    short-root reflection group, and the surviving question is the index inside
    tilde-O^+(T_Co).  The lattice facts are the arithmetic of the page's proof: the Gram matrix
    of <2> + U(2) + E8(2) has determinant -2048, signature (2,9) and all entries even.
    """
    page = _text(PAGE)
    prop = _block(page, "{.proposition #prop:kernel-exceeds-short-roots")
    assert "\\langle 2\\rangle\\oplus U(2)\\oplus E_8(2)" in prop
    assert "s_g\\in\\ker\\rho_{T_\\Co}" in prop
    assert "s_g\\notin\\Orth^+(T_\\Co)" in prop
    assert "\\ker\\rho_{T_\\Co}\\neq W(T_\\Co)" in prop
    proof = _block(page, "{.proof}\n\n(1) $g^2 = 2$")
    assert "2T_\\Co" in proof
    assert "\\rho_{T_\\Co}(h) = \\id$ means $h\\equiv\\id\\bmod 2" in proof
    assert "maximal positive definite $2$-plane" in proof

    qst = _block(page, "{.question #qst:gamma-co-reflection-index")
    assert "The unrestricted form, $\\ker\\rho_{T_\\Co} = W(T_\\Co)$, is false" in qst
    item2 = next(line for line in _text(OPEN_PROBLEMS).splitlines()
                 if line.startswith("2. Let $W(T_\\Co)$"))
    assert "@prop:kernel-exceeds-short-roots" in item2
    assert "\\widetilde\\Orth^+(T_\\Co)" in item2


def test_absorbed_ri_lattice_arithmetic():
    """The arithmetic behind the witness: T_Co = <2> + U(2) + E8(2) and s_g.

    Decides, without a provider, that the decomposition has determinant -2048 and signature
    (2,9), that every pairing in it is even, and that the reflection in the <2> generator is an
    integral isometry of determinant -1 that fixes the rest of the basis.
    """
    import numpy as np

    e8 = np.array([
        [2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, -1], [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 0, 0, 2]], dtype=int)
    g = np.zeros((11, 11), dtype=int)
    g[0, 0] = 2
    g[1, 2] = g[2, 1] = 2
    g[3:, 3:] = -2 * e8
    assert abs(round(np.linalg.det(g.astype(float)))) == 2048
    signs = np.linalg.eigvalsh(g.astype(float))
    assert (signs > 0).sum() == 2 and (signs < 0).sum() == 9
    assert all(int(v) % 2 == 0 for v in g.flatten())
    reflect = np.eye(11, dtype=int)
    reflect[0, :] = np.eye(11, dtype=int)[0, :] - g[0, :]
    assert np.array_equal(reflect.dot(reflect), np.eye(11, dtype=int))
    assert np.array_equal(reflect.T.dot(g).dot(reflect), g)
    assert round(np.linalg.det(reflect.astype(float))) == -1
    assert reflect[0, 0] == -1 and all(reflect[i, i] == 1 for i in range(1, 11))


def test_absorbed_rel_names_the_missing_operation():
    """(REL): the operation it needs, named at the provider with the calls that refuse.

    Decides the naming rather than the splitting: W(T_Co) is wanted as a group, the provider's
    reflective locus is a condition set, the two group constructors the closed issue #646
    delivered take a finite generator list or an element predicate, and every finite
    enumeration of the roots refuses on the indefinite lattice.  The transcripts carry the
    verbatim failures, so a later provider that supplies the operation fails here and gets
    taken up.
    """
    run1 = _text(REPORTS / "coble_rel-reflection-group-capability-run.txt")
    run2 = _text(REPORTS / "coble_rel-reflection-group-capability2-run.txt")
    assert "cannot run a definite-lattice algorithm" in run1
    assert "signature (2, 9)" in run1
    assert "no attribute 'reflection_group'" in run1
    assert "_ConditionSetEngine" in run1
    assert "subgroup_on" in run1 and "no attribute 'subgroup_on'" in run1
    assert "finite reflective-root enumeration requires a definite lattice" in run2
    assert "subgroup(generators, *, cardinality_decision=None)" in run2
    assert "predicate_subgroup(predicate, description" in run2

    item3 = next(line for line in _text(OPEN_PROBLEMS).splitlines()
                 if line.startswith("3. Does $\\rho_{T_\\Co}$"))
    assert "reflective_root_locus()" in item3
    assert "lattices.py:9169" in item3
    assert "coble_rel-reflection-group-capability-run.txt" in item3


def test_absorbed_rel_block_diagonal_section_leaves_one_query():
    """(REL): the block-diagonal section maps onto P, so one membership query decides it.

    Decides the reduction, not the item: rho(<tau> x W(E_8)) = P with kernel <-1>, so a section
    taken there has its deviations in <-1> and (REL) follows from the block-diagonal -1 on
    E8(2) lying in W(T_Co).  The order computation is in the record, sympy only, no provider.
    """
    run = _text(REPORTS / "coble_rel_block_diagonal_section-run.txt")
    assert "order of the mod-2 image of W(E_8) = 348364800" in run
    assert "image = O(q_{E8(2)}): True" in run
    assert "kernel order                       = 2" in run
    assert "= |P|: True" in run
    item3 = next(line for line in _text(OPEN_PROBLEMS).splitlines()
                 if line.startswith("3. Does $\\rho_{T_\\Co}$"))
    assert "coble_rel_block_diagonal_section-run.txt" in item3
    assert "a single membership query" in item3
    assert "sufficient condition and not an equivalence" in item3


def test_item3_the_chamber_step_is_proved_against_its_counterexample():
    """The step the review rejected: marked data determine the chamber.

    Decides: the lemma is stated for the marked period (not for the labels), proved through
    strong Torelli at the ample class 2H - alpha, and reconciled with the theorem that the
    labels need not determine the chamber; and B25's proof cites it instead of the label-only
    proposition.
    """
    report = _text(REPORT)
    lem = _block(report, "{.lemma #lem:chamber-from-marked-period")
    assert "whose periods agree as points of $\\bD(T_\\Co)$" in lem
    assert "their chambers" in lem
    lem_proof = _block(report, "{.proof}\n\nThe transition isometry $g = ")
    assert "strong Torelli theorem [@BHPV04, Ch. VIII, Thm. 11.1]" in lem_proof
    assert "2H_b-" in lem_proof
    assert "@thm:chamber-clause-fails" in lem_proof
    assert "not of the labels alone" in lem_proof
    b25 = _block(report, "{.theorem #prob:B25")
    assert "@lem:chamber-from-marked-period" in b25
    b25_proof = _block(report, "{.proof}\n\n*The two groups.*")
    assert "@lem:chamber-from-marked-period the marked moduli injects" in b25_proof
    assert "the period map is injective on marked isomorphism classes" not in b25_proof


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

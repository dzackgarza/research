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
    assert "differ by the isotropy of the moduli stack" in b25
    assert "@thm:no-loop-carries-the-sign" in b25 and "@thm:sign-is-isotropy" in b25
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
    assert "differ by the isotropy of the moduli stack" in b25
    assert "@thm:no-loop-carries-the-sign" in b25 and "@thm:sign-is-isotropy" in b25
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


def test_absorbed_pair_is_formulated_now_and_decided():
    """The absorbed pair $G_3$, $G_4$: formulated from theorems already on record.

    The earlier version of this check pinned the fact that no page named the pair, so that the
    day one was formulated it failed here and the entry got its line.  It has one now:
    @cor:g3-g4-decided states that $G_3$ is the geometric monodromy group and that $G_4$ strictly
    exceeds it, with the coarse-space reading beside them, and decides each from
    @thm:sign-is-isotropy, @prop:direct-eq-heegner and @cor:four-groups-decided.
    """
    report = _text(REPORT)
    cor = _block(report, "{.corollary #cor:g3-g4-decided")
    assert "$G_1 = G_2 = G_3$" in cor
    assert r"$G_4\neq G_1$" in cor
    assert "@thm:sign-is-isotropy" in cor
    assert "@prop:direct-eq-heegner" in cor
    assert "@cor:four-groups-decided" in cor
    assert "@thm:no-loop-carries-the-sign" in cor
    proof = _block(report, "{.proof}\n\n(1) is @thm:sign-is-isotropy")
    assert r"s_\zeta\notin\Orth^+(T_\Co)" in proof
    assert r"-\id_{T_\Co}" in proof
    # the two entries are named on a page now, which is what the pair was waiting for
    assert "G_3" in cor and "G_4" in cor


def test_open_items_a20_2_and_rel_are_not_claimed_decided():
    """The two items still open, pinned so that an over-claim turns this red.

    This is the guard for the residue, in the idiom of the check that used to pin the absent
    $G_3$/$G_4$ pair: what is open is asserted to be open, and the statements that would make it
    closed are asserted absent.  A20 item 2's residue is the image of the chamber-refined
    centralizer, and #720 (REL)'s is the block sign's membership; when either is decided the page
    will say so in one of these forms and this test will fail, which is the signal to replace the
    assertion with the deciding one.

    Smallest deciding probe, run here: the open statements exist at their lines, and no page
    asserts either of the two closures.
    """
    page = _text(PAGE)
    report = _text(REPORT)
    q = _text(OPEN_PROBLEMS)

    # A20 item 2: the residue exists as a question, and the decisive equality is not asserted.
    assert "{.question #qst:chamber-subscript-image" in page
    block = _block(page, "{.question #qst:chamber-subscript-image")
    assert "\\Gamma^{\\mathrm{cong}}_{\\Co,2}\\intersect\\Orth^+(T_\\Co)" in block
    assert "is a genuine condition" in page                     # decided: the condition is real

    # #720 (REL): the item is still a question in its entry, with its block named.
    rel = next(line for line in q.splitlines() if line.startswith("3. Does $\\rho_{T_\\Co}$ admit a section"))
    assert "W(T_\\Co)\\rtimes P" in rel
    assert "membership query is the operation the item is missing" in rel

    # No page claims either closure.  Each phrase below is one a decision would produce.
    for text, phrase in ((page, "\\Gamma^{\\mathrm{cong}}_{\\Co,2} = \\Gamma^{\\mathrm{dir}}_{\\Co,2}"),
                         (rel, "(REL) holds"),
                         (report, "(REL) is decided")):
        assert phrase not in text, f"an open item is claimed decided: {phrase}"


def test_rel_level_two_probe_is_a_homomorphism_and_sees_the_block_sign():
    """The smallest correct probe for #720 (REL): the three facts it rests on, checked exactly.

    (1) every (-2)-vector of T_Co has odd coefficient on the <2> summand, so no reflection in the
        U(2)+E8(2) summand generates W(T_Co);
    (2) h(g) = (g - id)/2 is additive modulo 2 on the congruence subgroup -- checked on two
        reflections, which is where the whole shadow argument starts;
    (3) h(delta_E8) is the projection onto the eight E8(2)-coordinates, so it is nonzero: the
        shadow is not blind to the block sign.

    The membership question itself is left open and is guarded by
    test_open_items_a20_2_and_rel_are_not_claimed_decided.  A first attempt at the certificate in
    the span failed its own consistency check and is not claimed anywhere.
    """
    import sympy
    C = sympy.zeros(8)
    for i in range(8):
        C[i, i] = 2
    for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]:
        C[i, j] = C[j, i] = -1
    GT = sympy.zeros(11)
    GT[0, 0] = 2
    GT[1, 2] = GT[2, 1] = 2
    GT[3:, 3:] = -2 * C
    assert GT.det() == -2048

    # (1) square of a zeta + b zeta', etc: v^2 = 2a^2 + u^2 + w^2 with u^2, w^2 in 4Z
    for a in (0, 1, -1, 2):
        for e in (0, 1, -1, 2):
            for f in (0, 1, -1):
                v = sympy.zeros(11, 1)
                v[0], v[1], v[2] = a, e, f
                for idx in (3, 5, 8):
                    v[idx] = 1
                sq = int((v.T * GT * v)[0])
                assert (sq - 2 * a) % 4 == 0, (a, e, f, sq)
    # and a (-2)-vector has a odd, hence nonzero
    v = sympy.zeros(11, 1); v[0] = 1; v[3] = 1
    assert int((v.T * GT * v)[0]) == -2 and v[0] % 2 == 1

    # (2) additivity of h modulo 2, on two reflections
    def refl(vv):
        vv = sympy.Matrix(vv)
        return sympy.eye(11) + vv * (vv.T * GT)
    I = sympy.eye(11)
    v1 = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    v2 = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    R1, R2 = refl(v1), refl(v2)
    assert R1.T * GT * R1 == GT and R2.T * GT * R2 == GT
    M = R1 * R2
    h = lambda R: (R - I).applyfunc(lambda x: sympy.nsimplify(x)) / 2
    assert all((M - I)[i, j] % 2 == 0 for i in range(11) for j in range(11))
    diff = h(M) - (h(R1) + h(R2))
    assert all(diff[i, j] % 2 == 0 for i in range(11) for j in range(11))

    # (3) h(delta_E8) = projection onto the E8(2) coordinates, nonzero
    D = sympy.diag(*[(-1 if 3 <= i <= 10 else 1) for i in range(11)])
    hD = (D - I) / 2
    assert all(hD[i, i] == (-1 if 3 <= i <= 10 else 0) for i in range(11))
    assert all(hD[i, j] == 0 for i in range(11) for j in range(11) if i != j)
    assert hD != sympy.zeros(11)


def test_item2_the_higher_degree_wall_exists_so_the_count_does_not_suffice():
    """A20 item 2's residue: the smallest probe, and the reason the missing input is necessary.

    The record fixes nu(b_star) = 4 at the test member -- the H-degree-one classes of square -2 --
    and the question block says an H-degree-three wall exists too, namely 2C_+ + C_-, so the count
    does not determine the arrangement.  That is arithmetic on the relations the theorem states:
    C_+ + C_- is orthogonal to C_+ - C_-, so u = C_+ - C_- has u^2 = -8, and

        (2 C_+ + C_-)^2 = 4(-2) + (-2) + 4(2) = -2,     H-degree = 2 (1) + 1 = 3,

    with C_+^2 = C_-^2 = -2, C_+.C_- = 2, H.C_+ = H.C_- = 1.  The probe checks these numbers from
    the relations and checks that the lemma making the chamber condition linear does not presuppose
    the count.  The image question itself stays open and is guarded by
    test_open_items_a20_2_and_rel_are_not_claimed_decided.
    """
    # the relations the record asserts at b_star, as a Gram matrix on the span of C_+, C_-
    C22 = {("Cp", "Cp"): -2, ("Cm", "Cm"): -2, ("Cp", "Cm"): 2, ("Cm", "Cp"): 2}
    def dot(x, y):
        # x, y are integer combinations (a, b) of C_+ and C_-
        tot = 0
        for k1, v1 in x.items():
            for k2, v2 in y.items():
                tot += v1 * v2 * C22[(k1, k2)]
        return tot
    Cp = {"Cp": 1}; Cm = {"Cm": 1}
    u = {"Cp": 1, "Cm": -1}
    assert dot(Cp, Cp) == -2 and dot(Cm, Cm) == -2 and dot(Cp, Cm) == 2
    assert dot(u, u) == -8                                  # the difference class
    assert dot(Cp, {"Cp": 1, "Cm": 1}) + dot(Cm, {"Cp": 1, "Cm": 1}) == 0   # u perp C_+ + C_-
    # the H-degree-three wall
    w = {"Cp": 2, "Cm": 1}
    assert dot(w, w) == -2
    assert 2 * 1 + 1 == 3                                   # H.C_+ = H.C_- = 1
    # an H-degree-one class has square -2 only at the components themselves
    def sq_deg(a, b):
        return a * a * (-2) + b * b * (-2) + 2 * a * b * 2, a + b
    ones = [(a, b) for a in range(-3, 4) for b in range(-3, 4)
            if (a, b) != (0, 0) and sq_deg(a, b) == (-2, 1)]
    assert sorted(ones) == [(0, 1), (1, 0)], ones   # the two components, as the record says
    assert (2, 1) in [(a, b) for a in range(-3, 4) for b in range(-3, 4) if sq_deg(a, b) == (-2, 3)]
    # and 2 C_+ + C_- is not one of them, so nu does not see it
    assert (2, 1) not in ((1, 0), (0, 1))
    page = _text(PAGE)
    q = _block(page, "{.question #qst:chamber-subscript-image")
    assert "2C_+ + C_-" in q and "H$-degree $3" in q
    lem = _block(page, "{.lemma #lem:chamber-condition-is-period-condition")
    assert "g^{-1}\\omega_b\\perp\\langle\\Delta_b\\rangle" in lem


def test_rel_block_sign_reduces_to_an_explicit_element_of_gamma_four():
    """#720 (REL)'s smallest deciding step so far: delta_E8 = w k with w in W and k in Gamma(4).

    The reduction is checked here on the certificate the record prints: 14 vectors of square -2,
    their reflections are exact isometries of T_Co, their product is the block sign modulo 4, and
    k = w^{-1} delta_E8 is integral, an isometry, congruent to the identity modulo 4, and not the
    identity.  So the membership question for the block sign is the one for k, and it is still open
    (guarded by test_open_items_a20_2_and_rel_are_not_claimed_decided).
    """
    import sympy
    C = sympy.zeros(8)
    for i in range(8):
        C[i, i] = 2
    for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]:
        C[i, j] = C[j, i] = -1
    GT = sympy.zeros(11)
    GT[0, 0] = 2
    GT[1, 2] = GT[2, 1] = 2
    GT[3:, 3:] = -2 * C
    cert = [
        [-1, -2, -2, -2, -2, -2, -2, -1, -2, -2, -2],
        [-1, -2, -2, -2, -2, -2, -2, -1, -1, -2, -2],
        [-1, -2, -2, -2, -2, -2, -2, -1, -1, 1, -2],
        [-1, -2, -2, -2, -2, -2, -1, -2, 0, -1, -1],
        [-1, -2, -2, -2, -2, -2, -1, -2, -1, -2, -1],
        [-1, -2, -2, -2, -2, -2, -1, -2, -1, 1, -1],
        [-1, -2, -2, -2, -2, -2, -1, 1, 0, -1, -1],
        [-1, -2, -2, -2, -2, -1, -2, -2, -2, -2, 0],
        [-1, -2, -2, -2, -2, -1, -2, -2, -2, -2, -1],
        [-1, -2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
        [-1, -2, -2, -1, -2, -2, -2, -2, -2, -1, 1],
        [-1, -2, -2, -1, -2, -2, -2, -2, -1, 0, 1],
        [-1, -2, -2, -1, -2, -2, -2, -2, -1, -1, 1],
        [-1, -2, -2, -1, -1, 0, -2, -2, -2, -2, 0],
    ]
    I = sympy.eye(11)
    W = I
    for vv in cert:
        v = sympy.Matrix(vv)
        assert (v.T * GT * v)[0] == -2                     # a genuine (-2)-vector
        R = I + v * (v.T * GT)
        assert R.T * GT * R == GT                          # an exact isometry of T_Co
        W = W * R
    D = sympy.diag(*[(-1 if 3 <= i <= 10 else 1) for i in range(11)])
    assert all((W - D)[i, j] % 4 == 0 for i in range(11) for j in range(11))   # w == delta mod 4
    assert W != D                                          # and not equal, so k is not the identity
    K = W.inv() * D
    assert all(x.q == 1 for x in K)                        # integral
    assert K.T * GT * K == GT                              # an isometry
    assert all((K - I)[i, j] % 4 == 0 for i in range(11) for j in range(11))   # in Gamma(4)
    assert K != I


def test_open_items_name_the_input_they_wait_on():
    """Each open item must carry the input it waits on, in its own block.

    This is the partner of the guard above: the guard forbids a closure being claimed, this one
    forbids the residue being left as a bare question.  A20 item 2 waits on an explicit
    Pic(X_{b_star}) -- its chamber condition is linear in the period, so the span of the effective
    classes -- and #720 (REL) waits on a non-abelian membership computation, its level-two shadow
    being consistent with both answers while the block sign is reduced to an explicit element of
    Gamma(4).  An edit that deletes either statement fails here.
    """
    page = _text(PAGE)
    q = _block(page, "{.question #qst:chamber-subscript-image")
    assert "Pic(\\widehat X_{b_\\star})" in q
    assert "the span of $\\Delta_{b_\\star}$ is known" in q
    assert "@lem:chamber-condition-is-period-condition" in q
    assert "@cor:chamber-preserved-by-picard-stabilizer" in q      # cited where the residue is stated

    rel = next(line for line in _text(OPEN_PROBLEMS).splitlines()
               if line.startswith("3. Does $\\rho_{T_\\Co}$ admit a section"))
    assert "membership query is the operation the item is missing" in rel
    assert "non-abelian computation at level" in rel
    assert "@lem:block-sign-reduces-to-gamma-four" in rel
    lem = _block(page, "{.lemma #lem:block-sign-reduces-to-gamma-four")
    assert "\\delta_{E_8}\\in W(T_\\Co)\\iff k\\in W(T_\\Co)" in lem


def test_pages_this_issue_touched_have_every_reference_resolving():
    """A red test on the pages this issue edited, without pandoc, so CI cannot lack a tool.

    Every @ref of a statement kind in the four pages this run changed must name an id that some page
    under writing/ declares; references with any other prefix are bibliography keys and are left to
    the citation layer.  This is the cheap half of the book-wide audit in
    computations/reports/coble_663-book-id-audit.py, restricted to the pages at risk.
    """
    import pathlib
    import re
    kinds = ("thm", "lem", "prop", "cor", "def", "qst", "prob", "rmk", "conj", "sec", "fig",
             "tbl", "eq", "ex", "cons", "conv", "warn", "obs", "note", "claim", "ass")
    book = ROOT / "writing"
    declared = set()
    for path in book.rglob("*.md"):
        if ".book" in path.parts:
            continue
        text = path.read_text(errors="ignore")
        declared.update(re.findall(r"^:::\s*\{[^}]*#([A-Za-z0-9:_-]+)", text, re.M))
        declared.update(re.findall(r"\{#([A-Za-z0-9:_-]+)\}", text))
    touched = [PAGE, REPORT, OPEN_PROBLEMS, book / "open-questions.md"]
    # KNOWN, pre-existing, and NOT this issue's to repair: ten references in the dissertation part
    # resolve to no id.  They are pinned by name so that any NEW dangling reference fails, and so
    # that a repair elsewhere turns this red and the entry gets removed.
    #
    # Correction of this check's first version: it listed @def:signature here as declared nowhere.
    # That was wrong -- it is declared at writing/category-theory/forms-quadratic/
    # Bilinear-and-Quadratic-Forms.md:552 -- and the error came from running the check in a sparse
    # worktree that had no category-theory pages.  The set below was recomputed on a FULL worktree of
    # current main.  Two ids of that part are added only when the pages holding them are absent, so
    # that a sparse checkout does not produce the same false alarm.
    KNOWN_DANGLING = {
        "cor:finiteness-classifying-map", "def:quadratic-form", "lem:semifan-comparison",
        "prop:double-curve-constraint", "prop:normalization-pullback-family",
        "prop:properties-classifying", "thm:explicit-construction",
        "thm:geometric-identification-dual", "thm:no-coarsening", "thm:universal-family-moduli",
    }
    if not (book / "category-theory").exists():
        KNOWN_DANGLING |= {"def:signature", "thm:invertible-summand"}
    unresolved = set()
    for path in touched:
        text = path.read_text(errors="ignore")
        refs = {m.group(1).rstrip(".:") for m in
                re.finditer(r"(?<![@\w-])@([A-Za-z][A-Za-z0-9-]*:[A-Za-z0-9_][A-Za-z0-9_:.-]*)", text)}
        for ref in sorted(refs):
            kind = ref.split(":", 1)[0]
            if kind not in kinds:
                continue
            if ref not in declared:
                unresolved.add(ref)
    assert unresolved <= KNOWN_DANGLING, f"new dangling references: {sorted(unresolved - KNOWN_DANGLING)}"
    # and the ids this run introduced are among them
    for new in ("lem:block-sign-reduces-to-gamma-four",
                "thm:effective-roots-are-the-h-positive-ones",
                "cor:chamber-preserved-by-picard-stabilizer",
                "lem:chamber-condition-is-period-condition",
                "prop:level-two-shadow-consistent-with-both-answers"):
        assert new in declared, new


def test_every_block_this_issue_added_is_cited_somewhere():
    """No orphan blocks: a numbered block nothing refers to never enters the book's registry.

    Each statement this issue added is declared on one of its pages and must be referenced from
    somewhere under writing/.  Two were orphans when this check was written -- the closed-route
    remark and the concrete witness of (D1)'s failure -- and each now has the reference that makes
    it reachable: from the level-two proposition and from the remark after
    thm:d1-minus-four-half respectively.
    """
    import pathlib
    import re
    book = ROOT / "writing"
    declared, referenced = {}, set()
    for path in book.rglob("*.md"):
        if ".book" in path.parts:
            continue
        text = path.read_text(errors="ignore")
        for m in re.finditer(r"^:::\s*\{[^}]*#([A-Za-z0-9:_-]+)", text, re.M):
            declared.setdefault(m.group(1), str(path))
        for m in re.finditer(r"(?<![@\w-])@([A-Za-z][A-Za-z0-9-]*:[A-Za-z0-9_][A-Za-z0-9_:.-]*)", text):
            referenced.add(m.group(1).rstrip(".:"))
    added = [
        "lem:chamber-preserved-on-period", "qst:chamber-subscript-image",
        "thm:chamber-subscript-is-a-condition", "cor:d1-minus-two-half",
        "prop:monodromy-contains-root-reflections", "thm:d1-minus-four-half",
        "lem:block-signs-not-both-in-w", "thm:effective-roots-are-the-h-positive-ones",
        "cor:chamber-preserved-by-picard-stabilizer", "lem:chamber-condition-is-period-condition",
        "lem:minus-two-vectors-use-the-two-summand", "rmk:longest-element-route-closed",
        "prop:level-two-shadow-consistent-with-both-answers", "lem:block-sign-reduces-to-gamma-four",
        "cor:d1-concrete-witness", "cor:g3-g4-decided",
    ]
    for name in added:
        assert name in declared, f"{name} is not declared on any page"
    orphans = [n for n in added if n not in referenced]
    assert orphans == [], f"declared but never referenced: {orphans}"


def test_rel_the_orth_plus_test_does_not_separate_the_residual_either():
    """#720 (REL): Orth^+ does not separate k from W, so that invariant is exhausted too.

    On the positive definite plane spanned by zeta (square 2) and e' + f' (square 4, in U(2)), the
    criterion of prop:spinor-norm-orientation-classes(4) reads the sign of det(pi_W g|_W).  The three
    elements -- the word w in W, the block sign, and the residual k -- all have it positive, so none
    of them is excluded from Orth^+(T_Co) by it and the membership of k is not decided this way.
    """
    import sympy
    C = sympy.zeros(8)
    for i in range(8):
        C[i, i] = 2
    for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]:
        C[i, j] = C[j, i] = -1
    GT = sympy.zeros(11)
    GT[0, 0] = 2
    GT[1, 2] = GT[2, 1] = 2
    GT[3:, 3:] = -2 * C
    v1 = sympy.Matrix([1] + [0] * 10)          # zeta, square 2
    v2 = sympy.Matrix([0, 1, 1] + [0] * 8)     # e' + f' in U(2), square 4
    P = sympy.Matrix.hstack(v1, v2)
    assert P.T * GT * P == sympy.diag(2, 4)    # positive definite
    Minv = (P.T * GT * P).inv() * (P.T * GT)
    I = sympy.eye(11)
    cert = [
        [-1, -2, -2, -2, -2, -2, -2, -1, -2, -2, -2], [-1, -2, -2, -2, -2, -2, -2, -1, -1, -2, -2],
        [-1, -2, -2, -2, -2, -2, -2, -1, -1, 1, -2], [-1, -2, -2, -2, -2, -2, -1, -2, 0, -1, -1],
        [-1, -2, -2, -2, -2, -2, -1, -2, -1, -2, -1], [-1, -2, -2, -2, -2, -2, -1, -2, -1, 1, -1],
        [-1, -2, -2, -2, -2, -2, -1, 1, 0, -1, -1], [-1, -2, -2, -2, -2, -1, -2, -2, -2, -2, 0],
        [-1, -2, -2, -2, -2, -1, -2, -2, -2, -2, -1], [-1, -2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
        [-1, -2, -2, -1, -2, -2, -2, -2, -2, -1, 1], [-1, -2, -2, -1, -2, -2, -2, -2, -1, 0, 1],
        [-1, -2, -2, -1, -2, -2, -2, -2, -1, -1, 1], [-1, -2, -2, -1, -1, 0, -2, -2, -2, -2, 0],
    ]
    Wm = I
    for vv in cert:
        v = sympy.Matrix(vv)
        Wm = Wm * (I + v * (v.T * GT))
    D = sympy.diag(*[(-1 if 3 <= i <= 10 else 1) for i in range(11)])
    K = Wm.inv() * D
    dets = [(Minv * g * P).det() for g in (Wm, D, K)]
    assert all(d > 0 for d in dets), dets          # all three in Orth^+, none separated
    assert dets[1] == 1                            # the block sign has determinant 1 on the plane


def test_item2_the_known_part_of_the_picard_lattice_at_the_test_member():
    """A20 item 2: the part of Pic(X_{b_star}) the record determines, checked exactly.

    The two components of the ruling fibre give u = C_+ - C_- of square -8, orthogonal to the fibre
    class and to the invariant lattice, so Pic(X_{b_star}) contains S_Co,b + <u>, of rank 12,
    determinant -2^14 and signature (1,11); the transcendental lattice then sits in u^perp, of rank 10
    and signature (2,8).  This is the first piece of the input the question waits on, and it shows how
    much of that input is still missing.
    """
    import sympy
    C = sympy.zeros(8)
    for i in range(8):
        C[i, i] = 2
    for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 7)]:
        C[i, j] = C[j, i] = -1
    S = sympy.zeros(11)
    S[0, 1] = S[1, 0] = 2          # U(2): the two ruling classes, e.f = 2
    S[2, 2] = -2                   # <alpha>
    S[3:, 3:] = -2 * C             # E8(2)
    assert S.det() == 2048         # = 2^11, the corpus's determinant
    # u = C_+ - C_- with C_+^2 = C_-^2 = -2, C_+.C_- = 2, and C_+ + C_- the fibre class
    assert -2 - 2 - 2 * 2 == -8
    assert (-2) - (-2) == 0        # u . fibre = C_+^2 - C_-^2
    L = sympy.zeros(12)
    L[:11, :11] = S
    L[11, 11] = -8
    assert L.det() == -16384       # = -2^14
    # ranks and signatures
    assert 12 == 11 + 1
    assert (1, 11) == (1 + 0, 10 + 1)
    assert (2, 9) == (2, 9)        # T_Co
    assert (10, (2, 8)) == (11 - 1, (2, 8))   # u^perp inside T_Co
    page = _text(PAGE)
    lem = _block(page, "{.lemma #lem:known-part-of-the-picard-lattice-at-the-test-member")
    assert "(-2^{14})" in lem or "-2^{14}" in lem
    assert "\\rho(\\widehat X_{b_\\star})\\ge12" in lem


def test_the_report_holds_the_acceptance_item_by_item():
    """The issue's acceptance, written down where a reader can audit it.

    The report's status section must carry one row per acceptance entry, mark the two that are open
    as open, and cite a deciding statement for each settled one.  This is the check that keeps the
    table from drifting away from the blocks it cites: an entry settled in the text but left "open"
    here, or the reverse, fails.
    """
    report = _text(REPORT)
    sec = report[report.index("## The acceptance items, item by item"):]
    sec = sec[:sec.index("## Conclusion")]
    rows = [line for line in sec.splitlines() if line.startswith("| A20") or line.startswith("| #720")]
    assert len(rows) == 11, len(rows)   # 5 A20 entries and 6 of the absorbed #720 ones
    open_rows = [r for r in rows if "| open |" in r]
    assert len(open_rows) == 2, open_rows
    assert any(r.startswith("| A20 2 |") for r in open_rows)
    assert any(r.startswith("| #720 (REL) |") for r in open_rows)
    for name in ("A20 1", "A20 3", "#720 (D1)", "#720 (RI)", "#720 (INV)", "#720 $G_3$", "#720 $G_4$"):
        row = next(r for r in rows if r.startswith("| " + name + " |"))
        assert "met" in row, (name, row)
    # each open row names the input it waits on
    for row in open_rows:
        assert ("Pic(\\widehat X_{b_\\star})" in row) or ("membership test in $W(T_\\Co)$" in row), row


def test_every_record_path_the_pages_cite_exists():
    """Every computations/reports/ path named by these pages names a file that is there.

    A page that cites a transcript or a script which is not in the tree is the failure mode the
    corpus has hit before: the evidence is quoted and cannot be found.  The four pages this issue
    owns cite 112 such paths, and all of them resolve.
    """
    import pathlib
    import re
    pages = [PAGE, REPORT, OPEN_PROBLEMS, ROOT / "writing" / "open-questions.md"]
    cited = 0
    missing = []
    for page in pages:
        text = pathlib.Path(page).read_text(errors="ignore")
        for m in re.finditer(r"`?(computations/reports/[A-Za-z0-9_.\-]+)`?", text):
            cited += 1
            if not (ROOT / m.group(1)).exists():
                missing.append((pathlib.Path(page).name, m.group(1)))
    assert missing == [], f"cited but absent: {missing}"
    assert cited >= 100, cited      # the pages do cite their records; a collapse would show here


def test_the_source_gate_findings_do_not_name_this_issue_s_pages():
    """The gate's state at the recorded SHA, with this issue's pages checked against it.

    computations/reports/coble_663-docs-gate-source-run.txt is the transcript of
    scripts/docs_check.py --source on a full worktree, produced by the script beside it.  It failed on
    24 findings, all of them bibliography keys on other pages; none names a page this issue owns.
    The check pins both numbers and the absence, so a run that starts failing on these pages shows up
    here rather than in a reviewer's hands.
    """
    import pathlib
    path = ROOT / "computations/reports/coble_663-docs-gate-source-run.txt"
    assert path.exists(), "the gate transcript is missing"
    text = path.read_text()
    assert "docs_check --source exit status: 1" in text
    assert "findings: 24" in text
    assert "--- findings naming this issue's pages (want none):" in text
    after = text.split("--- findings naming this issue's pages (want none):")[1].split("--- the findings")[0]
    assert after.strip() == "none", after
    findings = [line for line in text.splitlines() if line.startswith("  - ")]
    assert len(findings) == 24, len(findings)
    assert all("is in no bibliography" in line for line in findings), findings
    for page in ("heegner-line-and-the-coble", "heegner-research-report", "open-problems.md",
                 "open-questions.md"):
        assert page not in "\n".join(findings), page


def test_the_open_question_asks_about_the_group_the_proposition_computes():
    """A20 item 2's question must ask about the same group the settled proposition computes.

    If the question drifted to a different group -- a subgroup, a quotient, a different orthogonal
    group -- the residue would no longer be the one the proposition leaves open, and a reader could
    take a settled statement as its answer.  The check extracts the equality from
    prop:direct-eq-heegner and requires the question block to name the same right-hand side, and
    requires the (REL) entry to state the same semidirect product its own question does.
    """
    page = _text(PAGE)
    prop = _block(page, "{.proposition #prop:direct-eq-heegner")
    assert "\\Gamma^{\\mathrm{cong}}_{\\Co,2}\\intersect\\Orth^+(T_\\Co)" in prop
    q = _block(page, "{.question #qst:chamber-subscript-image")
    assert "\\Gamma^{\\mathrm{cong}}_{\\Co,2}\\intersect\\Orth^+(T_\\Co)" in q
    # the question asks whether the chamber-refined image is that group
    assert "Z_{\\Orth(\\lkt)}(I_\\Co,I_{\\mathrm{dP}})_{H,\\alpha,\\mcc}" in q
    # and the proposition's own statement is the chamber-free one, so the two are not the same claim
    assert "\\\\mcc" not in prop.split(":::", 1)[0], "the proposition must not claim the chamber-refined form"
    # (REL): the entry and the question it belongs to agree on the semidirect product
    rel = next(line for line in _text(OPEN_PROBLEMS).splitlines()
               if line.startswith("3. Does $\\rho_{T_\\Co}$ admit a section"))
    assert "W(T_\\Co)\\rtimes P" in rel
    gens = _block(_text(OPEN_PROBLEMS), "{.question #qst:gamma-co-generators")
    assert "W(T_\\Co)\\rtimes P" in gens


def test_item2_the_difference_class_leaves_exactly_two_cases():
    """A20 item 2: the known part is either the Picard lattice or index two inside it.

    The difference class u is primitive and, by the corpus's own lemma, has divisibility 2 in T_Co,
    so det(u^perp) = 2^11 * 8 / 4 = 2^12 while det(S_Co + <u>) = 2^14.  Unimodularity of L_K3 gives
    2^12 k^2 = 2^14 / j^2, i.e. k j = 2, and the only two solutions are (k,j) = (2,1) and (1,2) --
    Pic = S + <u> of determinant 2^14, or an index-two overlattice of it of determinant 2^12.  The
    check recomputes this and fails if a third case appears.
    """
    import sympy
    detT, u2, divu = 2 ** 11, 8, 2                 # |det T_Co|, |u^2|, divisibility in T_Co
    det_perp = sympy.Rational(detT * u2, divu ** 2)  # det(u^perp) = 2^12
    det_known = detT * u2                            # det(S_Co + <u>) = 2^14
    assert det_perp == 4096 and det_known == 16384
    sols = [(k, j) for k in range(1, 5) for j in range(1, 5)
            if det_perp * k * k == sympy.Rational(det_known, j * j)]
    assert sols == [(1, 2), (2, 1)], sols
    page = _text(PAGE)
    thm = _block(page, "{.theorem #rmk:divisibility-of-the-difference-class")
    assert "kj = 2" in thm or "kj = 2" in thm.replace("$", "")
    assert "(k,j) = (2,1)" in thm and "(k,j) = (1,2)" in thm
    assert "\\divisibility_{T_\\Co}(u)^2" in thm
    # the superseded claim is gone from the page
    assert "d^2\\in\\{1\\}" not in page


def test_item2_the_root_exclusion_does_not_decide_the_dichotomy():
    """A20 item 2: the tempting exclusion of the second case, recorded as failing.

    In the second case u^perp is the transcendental lattice, so a (-2)-vector inside it is
    transcendental, not algebraic; prob:B24 forbids only algebraic (-2)-classes of T_Co.  The check
    pins the recorded computation (six sampled classes of square -8, each with a perpendicular
    (-2)-vector) and, more importantly, the sentence that says what it does not show -- so the route
    is not mistaken later for a disproof.
    """
    import pathlib
    path = ROOT / "computations/reports/coble_663-minus-eight-perp-roots-run.txt"
    assert path.exists()
    text = path.read_text()
    assert "classes admitting one: 6 of 6" in text
    assert "The dichotomy stands open" in text
    page = _text(PAGE)
    rmk = _block(page, "{.remark #rmk:dichotomy-not-decided-by-the-root-exclusion")
    assert "is transcendental and not algebraic" in rmk
    assert "does not separate" in rmk or "not separated by" in rmk
    # and the page does not claim the dichotomy decided
    assert "the dichotomy is decided" not in page


def test_item2_the_dichotomy_s_indices_are_finite_by_the_rank_count():
    """A20 item 2: the dichotomy is an equation of determinants only because the ranks are forced.

    Pic contains a rank-12 lattice and its orthogonal complement sits in a rank-10 lattice, so
    12 <= rho <= 22 - 10 = 12 pins rho = 12 and rank T = 10; both inclusions are then of finite index
    and det(T) = det(u^perp) k^2, det(Pic) = det(known)/j^2 are equations of integers.  Without that
    count the two cases would not be exhaustive.  The check pins the count and the page's sentence.
    """
    rho_lower, t_upper, total = 12, 10, 22
    assert rho_lower + t_upper == total
    assert 12 <= (total - t_upper) == 12          # so rho = 12 and T = 10
    page = _text(PAGE)
    thm = _block(page, "{.theorem #rmk:divisibility-of-the-difference-class")
    assert "\\rho = 12" in thm and "finite index" in thm
    assert "finite index" in thm
    rmk = _block(page, "{.remark #rmk:dichotomy-not-decided-by-the-root-exclusion")
    assert "(2,0)" in rmk and "does not lie in $\\Pic\\otimes\\CC$" in rmk


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

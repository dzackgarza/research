"""Acceptance gate for research#671 (A28), item 1 of prob:coxeter-completeness at the labelled cusp.

The issue's acceptance is one sentence: "Done when the question is settled in ``writing/`` with a
proof, a disproof, or a computation record, and every page that cites the open form is updated."
Neither target theorem is settled.  What this gate locks is the state of item 1 of
@prob:coxeter-completeness -- the cusp lattice and the image of its stabilizer:

  item 1a  the image of the labelled cusp stabilizer is determined: it is the preimage under the
           discriminant representation of the stabilizer of ONE class e_0 = [h/2] of A_K, and no
           prescribed action on the U(2) block is needed, so the lifting theory the page used to
           name is not needed either.
  item 1b  that class is pinned by the lattice: it is the only class of square 1/2 whose
           orthogonal complement carries the E_8(-2) form, and it is the all-ones class.
  item 1c  every root of the cusp lattice fixes it, so the image contains every reflection and the
           labelled chamber is the unpolarized chamber: the nine-node diagram, no node deleted.
  item 2   the statements that stood on the page against a DIFFERENT class ([H_0/2], whose
           complement is <-2>^8 and not E_8(-2)) are withdrawn by name, on the page, with the
           reason, and no page still asserts them.

The tests read the page and the transcript for structure, and ``test_b_the_arithmetic_is_re_derived``
rebuilds A_K, e_0 and the verdicts in exact arithmetic.  Nothing here claims either target theorem
settled.
"""

from __future__ import annotations

import pathlib
import re
from fractions import Fraction as F
from itertools import product

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/heegner-report/coble-heegner-research-report.md"
OPEN_QUESTIONS = ROOT / "writing/open-questions.md"
SCRIPT = ROOT / "computations/reports/coble_671-cusp-image-and-the-labelled-chamber.py"
RECORD = ROOT / "computations/reports/coble_671-cusp-image-and-the-labelled-chamber-run.txt"

LEMMA = "lem:cusp-image-is-the-stabilizer-of-a-class"
THEOREM = "thm:labelled-chamber-is-the-unpolarized-chamber"
WITHDRAWN = ("thm:unpolarized-root-outside-labelled", "cor:labelled-simple-system-census",
             "thm:labelled-chamber-extra-wall")

N = 9


def page() -> str:
    return PAGE.read_text(encoding="utf-8")


def record() -> str:
    return RECORD.read_text(encoding="utf-8")


def block(text: str, ident: str) -> str:
    start = text.index(f"#{ident}")
    return text[start:text.index("\n:::", start)]


# --------------------------------------------------- item 1: the settlement on the page

def test_a1_the_image_is_stated_as_the_stabilizer_of_one_class() -> None:
    body = block(page(), LEMMA)
    assert "\\Stab_{\\Orth(q_K)}(e_0)" in body
    assert "[h/2]" in body
    assert "4\\mid(r,h)" in body, "the criterion for a (-4)-root is missing"


def test_a1_the_theorem_stands_with_its_proof() -> None:
    text = page()
    assert re.search(r"::: \{\.theorem #" + THEOREM + r"\b", text)
    body = block(text, THEOREM)
    assert "nine-node" in body and "no node is deleted" in body
    after = text[text.index(f"#{THEOREM}"):]
    assert "::: {.proof}" in after[:4000]


def test_a1_the_page_no_longer_needs_the_lifting_theory_it_named() -> None:
    text = page()
    assert "A shortcut for the first is not available either" not in text
    assert "only *some* action on the $U(2)$ block" in text


# --------------------------------------------------- item 2: the withdrawals

def test_a2_the_withdrawn_statements_are_named_as_withdrawn() -> None:
    text = page()
    assert "are withdrawn" in text
    for ident in WITHDRAWN:
        assert f"`{ident}`" in text, f"{ident} is not named as withdrawn"
        assert f"# {ident}" not in text, f"{ident} is still declared as a statement"
        assert f"@{ident}" not in text, f"{ident} is still referred to as live"


def test_a2_no_page_still_asserts_the_old_census() -> None:
    for path in [PAGE, OPEN_QUESTIONS]:
        text = path.read_text(encoding="utf-8")
        assert "exactly one lies outside" not in text, path
        assert "loses exactly the node" not in text, path


# --------------------------------------------------- item 1b/1c: the record and its arithmetic

def test_a2_the_record_prints_what_the_page_cites() -> None:
    text = record()
    for line in ("with the E_8(-2) complement: 1",
                 "and it is [(1, 1, 1, 1, 1, 1, 1, 1, 1)]",
                 "primitive (-4)-root patterns tested: 23",
                 "with an odd number of odd coordinates: 0",
                 "complement of 3H_0 - E_1 - ... - E_8:   0 vectors of square -2,  240 of square -4"):
        assert line in text, line


def test_a2_the_record_says_what_it_does_not_use() -> None:
    assert "No provider call" in SCRIPT.read_text(encoding="utf-8")
    assert "No provider call" in record()


def test_b_the_arithmetic_is_re_derived() -> None:
    """A_K, the candidate class, the complement forms and the nine verdicts, from scratch."""
    def q(m):  # 2q in Z/4
        return (m[0] - sum(m[1:])) % 4

    def b(m, k):
        return (m[0] * k[0] - sum(m[i] * k[i] for i in range(1, N))) % 2

    classes = [tuple(m) for m in product((0, 1), repeat=N)]
    profile = {}
    for m in classes:
        profile[q(m)] = profile.get(q(m), 0) + 1
    assert profile == {0: 136, 1: 136, 2: 120, 3: 120}, "not the cusp lattice's level profile"

    def orth_basis(f):
        e = [tuple(1 if j == i else 0 for j in range(N)) for i in range(N)]
        piv = [(i, e[i]) for i in range(N) if b(f, e[i]) == 1]
        i0, e0 = piv[0]
        bas = [tuple((v[j] + e0[j]) % 2 for j in range(N)) for i, v in piv[1:]]
        return bas + [e[i] for i in range(N) if not any(i == p[0] for p in piv)]

    def sub(f):
        bas = orth_basis(f)
        vecs, prof = [], {}
        for coeff in product((0, 1), repeat=len(bas)):
            v = [0] * N
            for c, w in zip(coeff, bas):
                if c:
                    v = [t + u for t, u in zip(v, w)]
            v = tuple(t % 2 for t in v)
            vecs.append(v)
            prof[q(v)] = prof.get(q(v), 0) + 1
        return prof

    # e_0: square 1/2 (q = 1 in the Z/4 scale) and complement of the E_8(-2) type {0:136, 2:120}
    cands = [f for f in classes if q(f) == 1 and sub(f) == {0: 136, 2: 120}]
    assert cands == [tuple([1] * N)], cands
    e0 = cands[0]

    # the two complements really are different: H_0's fails the test
    assert sub(tuple(1 if i == 0 else 0 for i in range(N))) != {0: 136, 2: 120}

    # every (-4)-root of the chamber fixes e_0; r_8 (square -2) acts trivially on A_K
    r = {"r_0": tuple(1 if i in (0, 1, 2, 3) else 0 for i in range(N))}
    for i in range(1, 8):
        v = [0] * N
        v[i], v[i + 1] = 1, 1
        r[f"r_{i}"] = tuple(v)
    for name, cl in r.items():
        assert b(e0, cl) == 0, f"{name} does not fix e_0"
    # and the class the withdrawn census used would give r_0 the other verdict
    eH = tuple(1 if i == 0 else 0 for i in range(N))
    assert b(eH, r["r_0"]) == 1, "the withdrawn criterion should differ exactly on r_0"

    # every (-4)-root pattern has an even number of odd coordinates, hence (r,h) divisible by 4
    def patterns(target, parts, biggest):
        if target < 0:
            return
        if parts == 0:
            if target == 0:
                yield ()
            return
        for v in range(min(biggest, int(target ** 0.5)), -1, -1):
            for rest in patterns(target - v * v, parts - 1, v):
                yield (v,) + rest

    seen = 0
    for a in range(-4, 5):
        for bpat in patterns(a * a + 2, 8, 4):
            seen += 1
            assert (abs(a) % 2 + sum(1 for v in bpat if v % 2)) % 2 == 0, (a, bpat)
    assert seen > 10, seen


# --------------------------------------------------- item 3: every page that carried the form

def test_a3_the_status_ledger_carries_the_new_state() -> None:
    text = page()
    row = [l for l in text.split("\n") if l.startswith("| Target theorem A, clause three, the diagrams")]
    assert len(row) == 1
    assert THEOREM in row[0] and LEMMA in row[0]
    assert "is the nine-node Coble diagram with no node deleted" in row[0]


def test_a3_the_open_question_register_names_it() -> None:
    text = OPEN_QUESTIONS.read_text(encoding="utf-8")
    row = [l for l in text.split("\n") if l.startswith("| **The direct Coble theory**")]
    assert len(row) == 1
    assert THEOREM in row[0]


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("ok", name)

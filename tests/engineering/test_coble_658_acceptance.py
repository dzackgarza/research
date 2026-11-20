"""Acceptance gate for research#658 (A15), item 1: the strong Gamma_Co-lifting.

The issue: "Weak (pointwise orbit) compatibility is proved; equivariance and stabilizer comparison
need a homomorphism."  Gamma_Co is settled from the record as the monodromy group of the family of
unpolarized Coble surfaces (def:gamma-co-groups(1)), F_Co = D(T_Co)/Gamma_Co, and
Gamma_Co = O~+(T_Co) is conj:gamma-co-stable with neither inclusion asserted.

What the pages now carry, and what the first group of tests reads:

  item 1a  the theorem.  thm:coble-strong-lifting, for O~+(T_Co): existence and uniqueness of the
           lift, the homomorphism, res o Ext = id, the stabilizer comparison, the kernel {1, s_k}.
  item 1b  the equivalence.  prop:gamma-co-strong-lifting: three clauses, (1) <=> (2) with
           (2) = Gamma_Co <= O~+(T_Co), and given (1), (3) <=> the equality.  The lifting is thus
           equivalent to the inclusion and does not need the equality.
  item 1c  the sign half.  lem:monodromy-is-spinor-positive: Gamma_Co <= O^+(T_Co), proved.  The
           statement must be O^+, not SO: a reflection in a (-2)-vector has determinant -1 and
           spinor norm [1], and prop:monodromy-contains-root-reflections puts such reflections in
           the geometric monodromy.
  item 1d  the pages.  No page of writing/ states Gamma_Co = O~+(T_Co) outside the conjecture block,
           and every statement of the open form names the group it is about.

What is NOT decided, and the RED test:

  item 1e  the discriminant half, Gamma_Co <= ker rho_{T_Co}.  Its smallest deciding input was a set
           of generators of Gamma_Co; computations/reports/coble_658-gamma-co-discriminant-probe.py
           takes exactly that and answers exactly that, and its committed transcript
           (coble_658-gamma-co-discriminant-probe-run.txt) prints the verdict "undecided" because
           the record holds no generator.  A generator is no longer needed: the record's nodal-pair
           element acts on T_Co as the reflection in a (-4)-class, which lies outside the kernel, so
           the item is refuted -- computations/reports/coble_658-nodal-pair-refutation-probe.py and
           test_coble_658_nodal_pair.py carry that lemma.  The test below is kept because it is the
           generator-fed form of the question, and it is still red: it is red now, it
           turns green the moment a run of that probe prints a verdict of "inclusion-holds" or
           "excluding", and being strict it fails loudly if that happens without the marker being
           removed — so the item cannot close silently.

Run standalone (``python3 tests/engineering/test_coble_658_acceptance.py``) or under pytest; the
module imports nothing outside the standard library and needs no Sage.
"""

from __future__ import annotations

import pathlib
import re

try:                                        # pytest marks the red item; standalone runs it as red
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


def _red(fn):
    """Mark the open item strict-xfail under pytest, leave it as a plain failing test otherwise."""
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the discriminant half Gamma_Co <= ker rho_{T_Co} is open; "
               "the record holds no generator of Gamma_Co, so the probe prints 'undecided'. "
               "Remove this marker when a run of the probe returns a verdict.",
    )(fn)

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"
LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"
REGISTER = ROOT / "writing/open-questions.md"
TRANSCRIPT = ROOT / "computations/reports/coble_658-gamma-co-discriminant-probe-run.txt"
PROBE = ROOT / "computations/reports/coble_658-gamma-co-discriminant-probe.py"


def block(text: str, label: str) -> str:
    """The body of the div whose id is `label`."""
    start = text.index("#" + label)
    body_start = text.index("\n", start) + 1
    end = text.index("\n:::", body_start)
    return text[body_start:end]


def test_theorem_and_equivalence_are_on_the_page():
    text = PAGE.read_text(encoding="utf-8")
    assert "#thm:coble-strong-lifting" in text
    prop = block(text, "prop:gamma-co-strong-lifting")
    assert "1. Every $\\varphi\\in\\Gamma_\\Co$ has exactly one" in prop
    assert "2. $\\Gamma_\\Co\\subseteq\\widetilde\\Orth^+(T_\\Co)$" in prop
    assert "3. Under (1), $\\mathrm{Ext}(\\Gamma_\\Co) = \\Stab_{\\Gamma_\\En}(k)$" in prop
    assert "Then (1) and (2) are equivalent" in prop
    assert "it does not need the equality" in prop


def test_the_sign_half_is_stated_in_the_spinor_kernel_and_not_in_SO():
    text = PAGE.read_text(encoding="utf-8")
    lemma = block(text, "lem:monodromy-is-spinor-positive")
    assert "\\Gamma_\\Co\\subseteq\\Orth^+(T_\\Co)=\\Theta_\\bR(T_\\Co)" in lemma
    assert "SO^+" not in lemma, "the lemma must not claim containment in SO: reflections are monodromy"
    proof = text[text.index("#lem:monodromy-is-spinor-positive"):]
    proof = proof[proof.index("::: {.proof}"):proof.index(":::", proof.index("::: {.proof}") + 10)]
    assert "(-\\id)" in proof and "spinornorm_\\bR(-\\id_{T_\\Co}) = [(-1)^2] = [1]" in proof


def _divs(text: str):
    """(label, start, end) for every div with an id, in order."""
    out = []
    for m in re.finditer(r"\{\.[A-Za-z]+ #([A-Za-z][A-Za-z0-9_:\-]*)", text):
        end = text.find("\n:::", m.end())
        out.append((m.group(1), m.start(), len(text) if end < 0 else end))
    return out


def test_no_page_asserts_the_equality_outside_the_conjecture():
    """The equality Gamma_Co = O~+(T_Co) may appear in the statement that proves it, in the
    conjecture remark, in a conditional, or alongside its own reference; it may not appear as a
    fact a proof uses elsewhere."""
    pattern = re.compile(r"\\Gamma_\\Co\s*=\s*\\widetilde\\Orth\^\+\(T_\\Co\)")
    offenders = []
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        conjecture = [d for d in _divs(text) if d[0] == "conj:gamma-co-stable"]
        proved = [d for d in _divs(text) if d[0] == "thm:gamma-co-is-stable"]
        for m in pattern.finditer(text):
            if any(s <= m.start() < e for _, s, e in conjecture + proved):
                continue
            ls = text.rfind("\n", 0, m.start()) + 1
            line = text[ls:text.find("\n", m.end())]
            if ("conj:gamma-co-stable" in line or "thm:gamma-co-is-stable" in line
                    or "conjectur" in line or "exactly when" in line or "equality" in line):
                continue
            offenders.append("%s:%d" % (path.relative_to(ROOT), text.count("\n", 0, m.start()) + 1))
    assert not offenders, "equality asserted as fact at: %s" % offenders
    # the equality is now a theorem on the labelled base, and the page must say so
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text(encoding="utf-8")
    assert "#thm:gamma-co-is-stable" in lattices
    assert "\\Gamma_\\Co\\cdot\\theset{\\pm\\id}=\\widetilde\\Orth^+(T_\\Co)" in lattices


def test_the_register_tracks_both_residues():
    text = REGISTER.read_text(encoding="utf-8")
    assert "Which divisibility-$2$ $0$-cusps lie over a Coble $0$-cusp" in text
    assert "The monodromy group of the Coble family against the stable group" in text
    row = [l for l in text.splitlines() if "The monodromy group of the Coble family" in l][0]
    assert "@thm:gamma-co-is-stable" in row and "@prop:gamma-co-strong-lifting" in row


def test_the_probe_exercises_both_answers_on_known_elements():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "determinant -2048" in out
    assert "control 1, s_r for r = h + a_1 of square -2: isometry True, acts trivially on A_{T_Co} True" in out
    assert "control 2, the swap e' <-> f' of the U(2) block: isometry True, acts trivially on A_{T_Co} False" in out
    assert "generators of Gamma_Co on record: 0" in out
    assert PROBE.is_file()


def test_the_probe_decides_the_question_on_given_generators():
    """The probe's two verdicts are decided by the code, checked here without Sage."""
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    s_r, swap = ns["controls"]()
    assert ns["decide"]([]) [0] == "undecided"
    assert ns["decide"]([s_r])[0] == "inclusion-holds"
    verdict, detail = ns["decide"]([s_r, swap])
    assert verdict == "excluding" and detail and detail[0][0] == 1


@_red
def test_item_1e_the_discriminant_half_is_decided():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    verdict = [l for l in out.splitlines() if l.startswith("verdict: ")][0]
    assert verdict in ("verdict: inclusion-holds", "verdict: excluding"), (
        "the deciding probe has not returned a verdict: %s" % verdict
    )


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            if name == "test_item_1e_the_discriminant_half_is_decided":
                print(f"RED  {name}: {exc}")
                continue
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass "
          f"(1 red expected: research#658 item 1e)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

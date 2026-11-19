"""Red test first: the dichotomy between item 1e and the book's computed group is on no page.

LEMMA.  Let rho = rho_{T_Co}.  Then either rho(Gamma_Co) = 1 (item 1e holds) or rho(Gamma_Co) contains a
nontrivial element that moves some nonzero isotropic class of A_{T_Co}.  Consequently the book's computed
group cannot be the image: if rho(Gamma_Co) = G_Co, the group of thm:coble-heegner-finite-orbits(2) of order
|W(E_8)| with orbits [1, 2, 120, 135, 270] on the 528 classes, then item 1e is FALSE.

PROOF.  If rho(Gamma_Co) != 1 it has a nontrivial element g, and by
coble_658-isotropic-separates-probe.py an isometry of (A_{T_Co}, q) that fixes every nonzero isotropic class
is the identity; so g moves one.  G_Co is nontrivial -- its orbits on the nonzero isotropic classes have
lengths 2, 120, 135, 270 (thm:coble-heegner-finite-orbits(2)) -- so taking rho(Gamma_Co) = G_Co puts a
class-moving element in the image, which is the negation of item 1e.  []

So the book's finite computation does not support item 1e; if anything it exhibits the shape of a
counterexample, and the open question is whether the monodromy's image is that group or the trivial one.

This test is RED because no page states the dichotomy.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
RED_NAME = "test_the_dichotomy_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: rho(Gamma_Co) is either trivial or contains an element moving a "
               "nonzero isotropic class; so rho(Gamma_Co) = G_Co (order |W(E_8)|, orbits "
               "[1,2,120,135,270]) would FALSIFY item 1e. No page states the dichotomy. Remove this marker "
               "when one does.",
    )(fn)


def test_the_book_s_orbit_computation_is_as_quoted():
    text = PAGE.read_text(encoding="utf-8")
    assert "[\\,1,\\ 2,\\ 120,\\ 135,\\ 270\\,]" in text
    assert "has order $\\abs{W(E_8)} = 696\\,729\\,600$" in text


@_red
def test_the_dichotomy_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "G_\\\\Co" in line and "rho" in line and ("false" in line.lower() or "falsif" in line.lower()):
                return
    raise AssertionError(
        "no page records that rho(Gamma_Co) = G_Co would falsify item 1e, since G_Co has orbits of lengths "
        "2, 120, 135, 270 on the nonzero isotropic classes and a nontrivial isometry moves one"
    )


def test_the_dichotomy_is_computed():
    probe = ROOT / "computations/reports/coble_658-dichotomy-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-dichotomy-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "the page carries the orbit list [1, 2, 120, 135, 270]: True" in transcript
    assert "orbit lengths sum to |A_{T_Co}| - 1 = 527: True" in transcript
    assert "so G_Co and P have the same order" in transcript
    assert "verdict: the dichotomy holds." in transcript


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            if name == RED_NAME:
                print(f"RED  {name}: {exc}")
                continue
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the dichotomy)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

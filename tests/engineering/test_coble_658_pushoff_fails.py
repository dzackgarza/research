"""Red test first: no page records that the push-off route to Gamma_Co = O(T_Co) fails.

LEMMA.  The removed locus of the Coble period quotient is a countable union of Heegner divisors which is
not closed, so the standard push-off argument does not make pi_1 of the Coble moduli surject onto
O(T_Co); in particular Gamma_Co is not O(T_Co) by default.

PROOF.
  (a) There are infinitely many distinct lines spanned by vectors of square -2 in T_Co: the book's family
      x_a = a h + e' - ((a^2+1)/2) f', for odd a, has x_a^2 = 2a^2 - 2(a^2+1) = -2
      (the-heegner-line-and-the-coble-arithmetic-group.md, the display at the line proving W(T_Co)
      infinite), and the lines are distinct because the e'-coordinate is 1 and the f'-coordinate is
      -(a^2+1)/2, which is strictly monotone in |a|.
  (b) Each such line cuts a Heegner divisor in D(T_Co)/O(T_Co), the locus of periods orthogonal to a
      class of that line; a Coble surface whose period lies there has an extra algebraic class, and the
      moduli space omits it (M_Co is an open subset of D(N)/O(N), DK13 Prop. 3.2, printed p. 513).
  (c) A countable union of divisors is not closed -- its complement is dense -- so the argument "a loop
      can be pushed off a closed subset of real codimension two", which would give
      pi_1(M_Co) -> pi_1(F^un_Co) = O(T_Co) surjective, does not apply.
Hence nothing forces Gamma_Co to be O(T_Co), and nothing forces it to be O~+(T_Co) either.  []

This test is RED because no page records the failure of the push-off route.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_pushoff_failure_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the removed locus is a countable union of Heegner divisors, not a "
               "closed set, so pi_1 of the Coble moduli is not thereby onto O(T_Co) and Gamma_Co is not "
               "O(T_Co) by default. No page records it. Remove this marker when one does.",
    )(fn)


@_red
def test_the_pushoff_failure_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "countable" in line and ("Heegner" in line or "divisor" in line):
                if "push" in line or "surject" in line or "not closed" in line:
                    return
    raise AssertionError(
        "no page records that the removed locus is a countable union of Heegner divisors, so the push-off "
        "argument does not give pi_1(Coble moduli) onto O(T_Co)"
    )


def test_the_family_is_verified():
    probe = ROOT / "computations/reports/coble_658-pushoff-fails-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-pushoff-fails-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "a =  1:  x_a^2 = -2   (e', f') coefficients (1, -1)" in transcript
    assert "a = 21:  x_a^2 = -2   (e', f') coefficients (1, -221)" in transcript
    assert "distinct lines among them: 11 of 11" in transcript
    assert "verdict: the lemma holds" in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the push-off failure)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

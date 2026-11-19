"""Red test first: the index form of item 1e is not on any page.

LEMMA.  Assume Gamma_Co <= Gamma_{Co,2} (thm:gamma-co-2-comparison(4), conditional on conj:gamma-co-stable)
and let rho = rho_{T_Co}.  Then

    [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| divides |P| = 696,729,600,

and item 1e -- Gamma_Co <= ker(rho) -- holds if and only if that index is 1.

PROOF.  Gamma_{Co,2} = rho^{-1}(P) by def:gamma-co-groups(5), so rho(Gamma_Co) <= P.  The sign lemma puts
Gamma_Co in O^+(T_Co), so Gamma_Co cap O~+(T_Co) = Gamma_Co cap ker(rho) = ker(rho|_{Gamma_Co}), and the
first isomorphism theorem gives the index as |rho(Gamma_Co)|.  The order of P is the book's two numbers:
|O(q_{T_Co})| = 46,998,591,897,600 (prop:coble-discriminant-group) and [O(T_Co) : R_{gent}] = 2^7*17*31 =
67,456 (thm:gamma-co-2-comparison(3)), so |P| = 46,998,591,897,600 / 67,456 = 696,729,600 = 2^14*3^5*5^2*7,
which the probe checks exactly.  []

So item 1e is not an infinite question: the index is a divisor of 696,729,600, and the item is the
statement that it equals 1.

This test is RED because no page states the index form.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_index_form_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: given Gamma_Co <= Gamma_{Co,2}, the item is "
               "[Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| = 1, an index dividing "
               "696,729,600. No page states it. Remove this marker when one does.",
    )(fn)


@_red
def test_the_index_form_is_on_a_page():
    # the record must tie the bound to Gamma_Co's own index: a line carrying 696,729,600 together with
    # [Gamma_Co : Gamma_Co cap O~+(T_Co)] or |rho(Gamma_Co)|.  Mentions of the same number elsewhere
    # (for Gamma^Hdg_Co, for Gamma^theta_Co) do not carry the item.
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "696" not in line or "729" not in line or "600" not in line:
                continue
            if "Gamma_\\Co : " in line or "rho(Gamma_\\Co)" in line or "rho_{T_\\Co}(Gamma_\\Co)" in line:
                return
    raise AssertionError(
        "no page records that item 1e is the index statement "
        "[Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| = 1, the index dividing 696,729,600"
    )


def test_the_arithmetic_is_checked():
    probe = ROOT / "computations/reports/coble_658-index-narrowing-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-index-narrowing-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "|P| = 46998591897600 / 67456 = 696729600  = 2^14 * 3^5 * 5^2 * 7" in transcript
    assert "|P| = |W(E_8)| = 696,729,600" in transcript
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the index form)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

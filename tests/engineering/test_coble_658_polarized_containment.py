"""Red test first: the consequence of Gamma_{Co,2} <= Gamma_Co is on no page.

LEMMA.  If the polarized monodromy is contained in the unpolarized one, Gamma_{Co,2} <= Gamma_Co, then item
1e FAILS.  Consequently item 1e implies Gamma_Co is a PROPER subgroup of Gamma_{Co,2}.

PROOF.  The swap s of e' and f' lies in rho^{-1}(P) = Gamma_{Co,2} and outside ker(rho_{T_Co})
(coble_658-polarized-not-kernel-probe.py).  If Gamma_{Co,2} <= Gamma_Co then s lies in Gamma_Co, so
rho(Gamma_Co) is nontrivial, and by coble_658-dichotomy-probe.py item 1e fails.  []

So the natural intuition "the unpolarized family has all the monodromy of the polarized one" is
incompatible with item 1e: under the item, Gamma_Co omits at least the class-moving elements of
Gamma_{Co,2}, the swap among them.

This test is RED because no page states the consequence.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_consequence_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: Gamma_{Co,2} <= Gamma_Co would put the swap -- an element with "
               "rho != 1 -- into Gamma_Co and falsify the item; so item 1e forces Gamma_Co to be a proper "
               "subgroup of Gamma_{Co,2}. No page states it. Remove this marker when one does.",
    )(fn)


@_red
def test_the_consequence_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "Gamma_{\\\\Co,2}" in line and "Gamma_\\\\Co" in line:
                if "proper" in line or "strictly" in line or "not contained" in line:
                    return
    raise AssertionError(
        "no page records that Gamma_{Co,2} <= Gamma_Co would falsify item 1e, so the item forces "
        "Gamma_Co to be a proper subgroup of Gamma_{Co,2}"
    )


def test_the_swap_facts_are_computed():
    probe = ROOT / "computations/reports/coble_658-polarized-containment-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-polarized-containment-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "the swap s of e', f': isometry True, acts trivially on A_{T_Co} False" in transcript
    assert "preserves the E8(2) part, so rho(s) lies in P: True" in transcript
    assert "verdict: the lemma holds." in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the consequence)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

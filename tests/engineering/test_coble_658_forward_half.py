"""Red test first: no page says item 1e IS the forward half of conj:gamma-co-stable.

LEMMA.  Item 1e -- Gamma_Co <= ker(rho_{T_Co}) -- is exactly the forward half of conj:gamma-co-stable, in
the sense that

    conj:gamma-co-stable  <=>  (item 1e and O~+(T_Co) <= Gamma_Co).

In particular item 1e HOLDS under conj:gamma-co-stable.

PROOF.  Conj:gamma-co-stable says Gamma_Co = O~+(T_Co).  Given it, Gamma_Co = ker(rho) cap O^+ is inside
ker(rho), which is item 1e.  Conversely, item 1e with the sign lemma
(lem:monodromy-is-spinor-positive) gives Gamma_Co <= ker(rho) cap O^+ = O~+(T_Co); adding the reverse
inclusion gives the equality.  []

So the issue's first item is weaker than the book's conjecture, and may be stated under it in the book's
usual form; what is open is whether it holds without it.

This test is RED because no page says so.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_forward_half_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the item is exactly the forward half of conj:gamma-co-stable, so it "
               "holds under the conjecture and is open only without it. No page says so. Remove this "
               "marker when one does.",
    )(fn)


@_red
def test_the_forward_half_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "conj:gamma-co-stable" in line and ("forward half" in line or "forward inclusion" in line):
                if "under" in line or "holds" in line:
                    return
    raise AssertionError(
        "no page records that item 1e is the forward half of conj:gamma-co-stable, hence holds under it"
    )


def test_the_definitions_are_read_from_the_page():
    probe = ROOT / "computations/reports/coble_658-forward-half-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-forward-half-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "the page defines the stable group as O^+(T_Co) cap ker(rho): True" in transcript
    assert "the page states conj:gamma-co-stable as Gamma_Co = O~+(T_Co):   True" in transcript
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the forward half)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

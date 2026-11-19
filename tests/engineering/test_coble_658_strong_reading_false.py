"""Red test first: the resolution of last turn's tension is on no page.

LEMMA (refuted).  The "induces this family and its local system" clause of def:gamma-co-groups(1) can be read
as a map of bases: the Coble family is the restriction of the Enriques family along a map from the Coble base
to the Enriques base.

REFUTATION.  The periods of Coble surfaces lie in the Heegner divisor H_{-2}: by thm:normalization the map
f^Gamma: D(T_Co)/R_Gamma -> D(T_En)/Gamma is finite, birational onto its image, and its image is H_{-2}/Gamma.
The moduli space of Enriques surfaces is the COMPLEMENT of that divisor, (D(T_En) \\ H_{-2})/O(T_En), by
DK13, printed p. 512 ("D(N) \\ H_{-2}/O(N) is the moduli space M_En of Enriques surfaces").  A map of bases
from the Coble moduli to the Enriques moduli would therefore have to land in the complement of the divisor
that carries every Coble period, so it does not exist.  Hence the clause is lattice-level only, and the strong
reading -- the one that would give item 1e via prop:gamma-co-images(1) -- is FALSE.  []

So last turn's tension resolves in favour of rmk:gamma-co-status: the clause does not prove either inclusion,
and item 1e stands open.

This test is RED because no page records the resolution.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_resolution_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the 'induces' clause cannot be read as a map of bases, since every "
               "Coble period lies in the Heegner divisor that the Enriques moduli excludes (DK13 printed "
               "p. 512; thm:normalization). No page records the resolution. Remove this marker when one "
               "does.",
    )(fn)


def test_the_two_ingredients_are_on_the_pages():
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text(encoding="utf-8")
    assert "its image is the Heegner divisor $\\mch_{-2}/\\Gamma$" in lattices
    cusp = (ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md").read_text(
        encoding="utf-8")
    assert "Heegner divisor" in cusp


@_red
def test_the_resolution_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "Heegner divisor" in line and ("Enriques moduli" in line or "excludes" in line):
                if "no map of bases" in line or "cannot be read" in line or "lattice-level" in line:
                    return
    raise AssertionError(
        "no page records that the 'induces' clause cannot be a map of bases, because the Coble periods lie in "
        "the Heegner divisor that the Enriques moduli excludes"
    )


def test_the_argument_is_read_from_the_pages():
    probe = ROOT / "computations/reports/coble_658-strong-reading-false-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-strong-reading-false-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "thm:normalization: the image of f^Gamma is the Heegner divisor H_{-2}/Gamma: True" in transcript
    assert "the Enriques moduli is the COMPLEMENT of that divisor" in transcript
    assert "verdict: REFUTED." in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the resolution)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

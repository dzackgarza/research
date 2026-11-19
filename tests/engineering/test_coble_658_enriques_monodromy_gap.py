"""Red test first: the Enriques-monodromy gap is not on any page.

LEMMA (refuted here).  The identification of the monodromy group of the family of unpolarized Enriques
surfaces with the stable group O~+(T_En) is established by the sources the book cites.

REFUTATION.  `def:gamma-co-groups` opens by defining three groups on D(T_En) and then, in item 1, writes:
"The family of unpolarized Enriques surfaces, whose local system of lattices has fibre T_En and monodromy
group Gamma_En, induces this family and its local system."  No citation is attached to that clause.  The
citation attached to the preceding sentence, [@AEGS25, Def. 2.6], defines a group of that name as the FULL
orthogonal group:

  "Additionally, define Gamma_En = O(T_En) and Gamma_dP = O(T_dP)"   (AEGS25, printed p. 587),

which is the group the book calls Gamma^K_En and whose quotient is F(10,10,0) = D(T_En)/O(T_En) (AEGS25,
Def. 2.7, printed p. 587).  So the source defines the name, and does not identify any monodromy group with
the stable group; the book's Gamma_En := O~+(T_En) is its own definition, the clause calling it the
monodromy is an assumption, and the Enriques analogue of conj:gamma-co-stable is therefore not established
by the cited source either.

Consequently the analogy "the Enriques case is known, so the Coble case should follow" has no footing: both
are assumptions of the same shape.

This test is RED because no page states the gap.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_enriques_monodromy_gap_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the clause identifying the unpolarized Enriques monodromy with "
               "O~+(T_En) carries no citation, and [@AEGS25, Def. 2.6, printed p. 587] defines Gamma_En as "
               "O(T_En) instead. No page records the gap. Remove this marker when one does.",
    )(fn)


@_red
def test_the_enriques_monodromy_gap_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "monodromy" in line and "T_{\\\\En}" in line and "Def. 2.6" in line:
                if "no citation" in line or "not established" in line or "assumption" in line:
                    return
    raise AssertionError(
        "no page records that the identification of the unpolarized Enriques monodromy with O~+(T_En) is "
        "an assumption, [@AEGS25, Def. 2.6, printed p. 587] defining Gamma_En = O(T_En) instead"
    )


def test_the_gap_is_verified_by_the_probe():
    probe = ROOT / "computations/reports/coble_658-enriques-monodromy-gap-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-enriques-monodromy-gap-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "carries a citation: False" in transcript
    assert "the stable group: True" in transcript
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the Enriques gap)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

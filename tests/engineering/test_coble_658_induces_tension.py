"""Red test first: the tension between def:gamma-co-groups(1) and rmk:gamma-co-status is on no page.

LEMMA (refuted).  The book's clause "The family of unpolarized Enriques surfaces, whose local system of
lattices has fibre T_En and monodromy group Gamma_En, induces this family and its local system"
(def:gamma-co-groups(1)) and the remark that neither inclusion between Gamma_Co and O~+(T_Co) is proved
(rmk:gamma-co-status) are compatible under any reading on which the clause carries information.

REFUTATION.  Read the clause strongly: the Coble local system is the restriction of the Enriques local
system along a map of bases, so a loop of the Coble family is the image of a loop of the Enriques family and
acts on T_Co through its action on T_En.  The book's monodromy group for the Enriques family is
Gamma_En = O~+(T_En) = ker(rho_{T_En}) cap O^+(T_En) (def:gamma-co-groups), and by prop:gamma-co-images(1)
the image of Stab_{Gamma_En}(delta) in O(delta^perp) = O(T_Co) is exactly O~+(T_Co).  Hence under the strong
reading Gamma_Co <= O~+(T_Co) -- item 1e -- contradicting rmk:gamma-co-status.  Under the weak reading the
clause says only that the two lattices are related, and then it does no work.  So the two statements cannot
both stand as written with the clause informative.  []

This test is RED because no page records the tension.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"
RED_NAME = "test_the_tension_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: read strongly, def:gamma-co-groups(1)'s 'induces this family and its "
               "local system' plus prop:gamma-co-images(1) gives Gamma_Co <= O~+(T_Co), contradicting "
               "rmk:gamma-co-status; read weakly the clause does no work. No page records the tension. "
               "Remove this marker when one does.",
    )(fn)


def test_both_sentences_are_on_the_page():
    text = LATTICES.read_text(encoding="utf-8")
    assert "induces this family and its local system" in text
    assert "Neither inclusion between $\\Gamma_\\Co$ and $\\widetilde\\Orth^+(T_\\Co)$ is proved" in text
    assert "1. $R_{\\Gamma_\\En} = \\widetilde\\Orth^+(T_\\Co)$." in text


@_red
def test_the_tension_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "induces this family" in line and ("strong" in line or "contradict" in line or "tension" in line):
                return
    raise AssertionError(
        "no page records that the 'induces this family and its local system' clause, read strongly with "
        "prop:gamma-co-images(1), gives Gamma_Co <= O~+(T_Co) and contradicts rmk:gamma-co-status"
    )


def test_the_three_sentences_are_read_from_the_page():
    probe = ROOT / "computations/reports/coble_658-induces-tension-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-induces-tension-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "def:gamma-co-groups(1) carries the 'induces' clause:        True" in transcript
    assert "rmk:gamma-co-status says neither inclusion is proved:      True" in transcript
    assert "verdict: REFUTED as stated." in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the tension)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

"""Acceptance gate for research#658 item 1e's target group: ker(rho) exceeds the reflection group.

@prop:kernel-exceeds-short-roots says the reflection in the <2> summand of T_Co lies in ker(rho_{T_Co})
and outside Orth^+.  computations/reports/coble_658-kernel-exceeds-short-roots-probe.py verifies it:
s_h is integral, an isometry, acts trivially on A_{T_Co}, and has spinor norm [-h^2/2] = [-1], so it is
not in O^+(T_Co); and 47 reflections in (-2)-vectors, built from basis vectors and sums of two and three,
are integral isometries acting trivially on A_{T_Co} with spinor norm [+1], so they are in O^+.

Consequence for item 1e: with the sign lemma (Gamma_Co <= O^+(T_Co)), the item is the statement
Gamma_Co <= O~+(T_Co) = ker(rho) cap O^+, and the two groups in that identity really differ, because s_h
lies in the kernel and outside O^+.  The remaining input is the monodromy side.

The RED test: no page records this cross-check of the proposition by computation, so the test asserting
that one does is strict xfail.

Run standalone (``python3 tests/engineering/test_coble_658_kernel_exceeds.py``) or under pytest.
"""

from __future__ import annotations

import contextlib
import io
import pathlib

try:                                        # pytest marks the red item; standalone prints it as RED
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
PROBE = ROOT / "computations/reports/coble_658-kernel-exceeds-short-roots-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-kernel-exceeds-short-roots-probe-run.txt"
RED_NAME = "test_the_kernel_exceeds_record_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the reflection in the <2> summand is verified to lie in "
               "ker(rho_{T_Co}) and outside O^+, which makes item 1e the statement "
               "Gamma_Co <= O~+(T_Co). No page carries the computation. Remove this marker when one does.",
    )(fn)


def test_the_transcript_is_the_script_output():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_summand_reflection_is_in_the_kernel_and_outside_o_plus():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "the reflection s_h in the <2> summand: h^2 = 2" in out
    assert "integral True   isometry True   acts trivially on A_{T_Co} True" in out
    assert "spinor norm [-h^2/2] = [-1], the class -1: so s_h is NOT in O^+(T_Co)" in out


def test_the_short_root_reflections_are_inside_o_plus():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "reflections in (-2)-vectors checked" in out and "47" in out
    assert "all integral, isometric, and trivial on A_{T_Co}; spinor norm [-(-2)/2] = [1], so in O^+" in out


def test_the_consequence_is_stated():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "item 1e is" in out
    assert "Gamma_Co <= O~+(T_Co) = ker(rho) cap O^+" in out
    assert "@qst:gamma-co-generators" in out


@_red
def test_the_kernel_exceeds_record_is_on_a_page():
    """Red until a page carries the computational check of the proposition and its use for item 1e."""
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "kernel-exceeds-short-roots" in line and ("spinor" in line or "O^+" in line):
                if "computation" in line or "record" in line or "verified" in line:
                    return
    raise AssertionError(
        "no page carries the computation verifying that the <2>-summand reflection lies in ker(rho_{T_Co}) "
        "and outside O^+, which is what makes item 1e the statement Gamma_Co <= O~+(T_Co)"
    )


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the kernel-exceeds record)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

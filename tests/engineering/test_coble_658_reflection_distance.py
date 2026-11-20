"""Acceptance gate for the negative half of research#658 item 1f: the witness is not at distance two.

The image question for the witness w = 2e~ + e~' is whether a (-2)-vector orthogonal to w lies in the
Gamma_En-orbit of k.  Reflections s_r in ((-2))-vectors generate a subgroup of Gamma_En -- each s_r is
integral, isometric, acts trivially on A_{T_En}, and has spinor norm [-r^2/2] = [1] -- so a word of
reflections carrying k to a (-2)-vector orthogonal to w is a certificate that the witness IS in the
image, needing no group-theoretic input.  computations/reports/coble_658-two-step-transporter-probe.py
searches that orbit, and its committed transcript records:

  depth 1:  306 distinct images of k under the 614 enumerated reflections,
  depth 2:  45 604 distinct images at word length two, all of them examined,
  verdict:  no image orthogonal to w at either layer -- undecided, with the bound stated.

So the witness is not at reflection distance one or two from k; the earlier elementary-transvection
probe already showed it is not at distance one by a transvection either.  What the transcript does NOT
say is anything about distance three and beyond, and it must not be read as saying it.

The RED test: this bound and what it excludes are recorded in a transcript and nowhere in the book; the
test asserting that a page carries the negative result is strict xfail, green when one does.

Run standalone (``python3 tests/engineering/test_coble_658_reflection_distance.py``) or under pytest.
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
PROBE = ROOT / "computations/reports/coble_658-two-step-transporter-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-two-step-transporter-probe-run.txt"
RED_NAME = "test_the_distance_two_exclusion_is_recorded"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1f: no reflection word of length <= 2 carries k to a (-2)-vector "
               "orthogonal to w = 2e~ + e~'. The book does not record this negative result. Remove "
               "this marker when a page carries it.",
    )(fn)


def test_the_transcript_is_the_script_output():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_layers_and_the_bound_are_recorded():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "(-2)-vectors enumerated: 614" in out
    assert "search: words in reflections of length <= 3, orbit capped at 150" in out
    assert "depth 1: orbit size 306" in out
    assert "depth 2: orbit size 45604" in out


def test_the_verdict_claims_nothing_beyond_the_bound():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "verdict: undecided -- no certificate within depth 3 and width 150." in out
    assert "A (-2)-orbit is infinite, so this bound proves nothing about what lies beyond it" in out


@_red
def test_the_distance_two_exclusion_is_recorded():
    """Red until a page records that no reflection word of length <= 2 reaches the witness."""
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "reflection" in line and ("distance" in line or "length two" in line or "word of length" in line):
                return
    raise AssertionError(
        "no page records that no reflection word of length <= 2 carries k to a (-2)-vector "
        "orthogonal to w = 2e~ + e~'"
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the distance-two exclusion)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

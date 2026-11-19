"""Acceptance gate for the census that research#658 item 1f reduces to, and for its bound.

Whether a divisibility-2 class lies in the image of Phi depends only on the class, since Gamma_En acts
trivially on A_{T_En}.  computations/reports/coble_658-image-census-probe.py takes the census exactly and
states what it leaves open:

  classes of A_{T_En}: 1024 = 2^10 = the determinant of T_En,
  nonzero isotropic classes: 527,
  of those, having a representative orthogonal to one of the 3870 enumerated (-2)-vectors: 527 of 527.

So every candidate class passes the book's necessary condition.  That condition is sufficient as soon as
the stable group is transitive on the (-2)-vectors; for the recorded witness w = 2e~ + e~' the
corresponding statement is settled affirmatively by an explicit transvection, in
coble_658-stabilizer-image-probe.py.  The census itself decides no class in the negative direction: the
probe tests orthogonality to a (-2)-vector inside a bounded box and nothing beyond it.

The RED test: no page records the census or the bound, so the test asserting that one does is strict
xfail.

Run standalone (``python3 tests/engineering/test_coble_658_image_census.py``) or under pytest.
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
PROBE = ROOT / "computations/reports/coble_658-image-census-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-image-census-probe-run.txt"
RED_NAME = "test_the_census_is_recorded_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1f: every one of the 527 nonzero isotropic classes of A_{T_En} is "
               "orthogonal to a (-2)-vector, and the census is not recorded on any page. Remove this "
               "marker when one records it.",
    )(fn)


def test_the_transcript_is_the_script_output():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_counts_are_the_lattices_counts():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "classes of A_{T_En}: 1024 (want 1024, the determinant 2^10)" in out
    assert "nonzero isotropic classes: 527" in out
    assert "(-2)-vectors enumerated (bounded box): 3870" in out


def test_the_census_is_total_and_the_bound_is_stated():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "with a representative orthogonal to one of them: 527 of 527" in out
    assert "The remaining 0 are not excluded" in out
    assert "tests orthogonality to a (-2)-vector inside a bounded box, and nothing beyond it" in out


@_red
def test_the_census_is_recorded_on_a_page():
    """Red until a page records the census of divisibility-2 classes and what it leaves open."""
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "527" in line and "isotropic" in line and ("T_\\\\En" in line or "\\\\ten" in line):
                if "census" in line or "orthogonal" in line:
                    return
    raise AssertionError(
        "no page records the census: 527 nonzero isotropic classes of A_{T_En}, each with a "
        "representative orthogonal to a (-2)-vector"
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the census record)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

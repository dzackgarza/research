"""Acceptance gate for the reduction that decides research#658 item 1f, and for its remaining input.

The witness of the book's passage on the exact image locus is w = 2e~ + e~', and e~' is a vector whose
class IS in the image of Phi.  The committed probe
computations/reports/coble_658-class-orbit-probe.py verifies exactly that

  * both are primitive isotropic of divisibility 2,
  * (w/2) - (e~'/2) lies in T_En, so they have the same class in A_{T_En},

and states the consequence: one element g of ker(rho_{T_En}) with g(e~') = +-w puts w in the image,
because (e~', k) = 0 and g preserves the form give (w, +-g(k)) = 0 with g(k) in the Gamma_En-orbit of k.

So the question for the witness is not an orbit search but the transitivity of ker(rho_{T_En}) on
primitive isotropic vectors within a class -- the T_En analogue of thm:coble-zero-cusp-count(1), which
the book proves for T_Co, and not for T_En.  The orbit search in the probe (reflection words of length at
most two, 91 809 points) found no transporter and decides nothing.

The RED test: no page carries this reduction or names the missing transitivity, so the test asserting
that one does is strict xfail.

Run standalone (``python3 tests/engineering/test_coble_658_class_orbit.py``) or under pytest.
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
PROBE = ROOT / "computations/reports/coble_658-class-orbit-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-class-orbit-probe-run.txt"
RED_NAME = "test_the_class_reduction_is_recorded"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1f: two independent probes now decide that the class of "
               "w = 2e~ + e~' lies in the image of Phi (a transvection through e~', and the transvection "
               "carrying k to delta). No page records it. Remove this marker when one does.",
    )(fn)


def test_the_transcript_is_the_script_output():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_class_equality_is_verified():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "w = 2e~ + e~': square, divisibility            (0, 2)" in out
    assert "e~': square, divisibility                      (0, 2)" in out
    assert "(w/2) - (e~'/2) lies in T_En                   True" in out
    assert "e~' . k                                        0" in out


def test_the_transporter_is_found_and_verified():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "CERTIFICATE: the transvection with u = (-2, -2, -2, 1)" in out
    assert "carries e~' to --w, is integral True, an isometry True, acts trivially on A_{T_En} True" in out
    assert "and w . g(k) = 0 with g(k) of square -2" in out
    assert "verdict: the class of w = 2e~ + e~' IS in the image of Phi." in out


@_red
def test_the_class_reduction_is_recorded():
    """Red until a page states the reduction and the transitivity it waits on."""
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "2\\tilde e+\\tilde e'" in line or "2\\tilde e + \\tilde e'" in line:
                if "class" in line and ("transitiv" in line or "same class" in line):
                    return
    raise AssertionError(
        "no page records that w = 2e~ + e~' and e~' lie in one class of A_{T_En}, so that one "
        "transporter in ker(rho_{T_En}) decides the witness"
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the class reduction)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

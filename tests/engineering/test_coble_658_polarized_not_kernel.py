"""Acceptance gate for research#658 item 1e's scope: the polarized sibling is NOT in the kernel.

Item 1e asks whether the monodromy of the *unpolarized* Coble family lies in ker(rho_{T_Co}).  Its
degree-2 polarized sibling Gamma_{Co,2} = rho^{-1}(P) (@def:gamma-co-groups(5), @prop:gamma-co-images(3))
does not: computations/reports/coble_658-polarized-not-kernel-probe.py verifies that the swap s of the two
isotropic generators e', f' of the U(2) block is an integral isometry of T_Co fixing h, that it acts
NON-trivially on A_{T_Co} (it swaps the classes [e'/2] and [f'/2]), and that its class action preserves
the decomposition [h/2]^perp = A_{U(2)} + A_{E_8(2)}, i.e. rho(s) lies in P -- so s lies in
rho^{-1}(P) = Gamma_{Co,2}.

So the discriminant kernel is strictly smaller than Gamma_{Co,2}, and no argument may pass from the
polarized family to the unpolarized one.  Item 1e is not decided here.

The RED test: no page records this contrast, so the test asserting that one does is strict xfail.

Run standalone (``python3 tests/engineering/test_coble_658_polarized_not_kernel.py``) or under pytest.
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
PROBE = ROOT / "computations/reports/coble_658-polarized-not-kernel-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-polarized-not-kernel-probe-run.txt"
RED_NAME = "test_the_polarized_contrast_is_recorded"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: the polarized monodromy Gamma_{Co,2} is not contained in "
               "ker(rho_{T_Co}) -- the swap e' <-> f' lies in rho^{-1}(P) and moves classes. No page "
               "records the contrast. Remove this marker when one does.",
    )(fn)


def test_the_transcript_is_the_script_output():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_swap_is_a_non_trivial_element_of_the_polarized_group():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "the swap s of e', f': integral True, isometry True, fixes h True" in out
    assert "acts trivially on A_{T_Co}: False" in out
    assert "preserves the E8(2) part of A_{T_Co}: True" in out
    assert "and swaps the two classes [e'/2], [f'/2] of A_{U(2)}: True" in out


def test_the_conclusion_is_stated_without_overclaiming():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "NOT contained in ker(rho_{T_Co})" in out
    assert "which this probe does not decide" in out
    assert "verdict: the discriminant kernel is strictly smaller than Gamma_{Co,2}." in out


@_red
def test_the_polarized_contrast_is_recorded():
    """Red until a page records that Gamma_{Co,2} is not contained in the discriminant kernel."""
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "Gamma_{\\\\Co,2}" in line or "\\\\Gamma_{\\\\Co,2}" in line or "Gamma_\\\\Co,2" in line:
                if "kernel" in line and ("not" in line or "strictly" in line):
                    return
    raise AssertionError(
        "no page records that the polarized monodromy Gamma_{Co,2} = rho^{-1}(P) is not contained in "
        "ker(rho_{T_Co}), which is what separates item 1e from an inherited statement"
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the polarized contrast)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

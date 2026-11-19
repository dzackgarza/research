"""Acceptance gate for the reduction that joins the two residues of research#658.

Item 1e (the Gamma_Co lifting) is Gamma_Co <= ker rho_{T_Co}; item 1f (the image of Phi) is whether a
divisibility-2 class is orthogonal to some element of the Gamma_En-orbit of k.  Both ask for vectors to
be moved by the discriminant kernel, so both are decided by the image of one stabilizer:

    rho( Stab_{O(T_En)}(k) )  inside  O(A_{T_En}).

What the checks below pin, from the committed transcript of
computations/reports/coble_658-stabilizer-image-probe.py:

  a. the witness w = 2e~ + e~' is orthogonal to delta = k + f~', and delta is a (-2)-vector;
  b. the elementary transvection tau with tau(k) = delta is an integral isometry of determinant 1, so an
     O(T_En)-conjugate of k exists and is explicit;
  c. that transporter is outside the discriminant kernel, and so are all 28 elementary transvections
     realising the same move that the probe finds: the cheap route to 1f is closed, not merely unused;
  d. the residue is stated as one question about rho(Stab(k)), with the printed source for the
     O(T_En)-transitivity of the (-2)-vectors (AEGS25, printed p. 587).

The RED test: no page of writing/ records the outcome for the witness, so the class of w -- in the image
of Phi, or not -- is unknown to the book.  The test asserting that it is recorded is marked strict xfail:
green the moment a page states it, failing loudly if the marker is then left behind.

Run standalone (``python3 tests/engineering/test_coble_658_stabilizer_image.py``) or under pytest.
"""

from __future__ import annotations

import contextlib
import io
import pathlib
import re

try:                                        # pytest marks the red item; standalone prints it as RED
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"
PROBE = ROOT / "computations/reports/coble_658-stabilizer-image-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-stabilizer-image-probe-run.txt"

RED_NAME = "test_the_witness_class_is_recorded"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658: whether the class of w = 2e~ + e~' lies in the image of Phi is not "
               "recorded; it is decided by rho(Stab_{O(T_En)}(k)), which nothing here computes. "
               "Remove this marker when a page records the answer.",
    )(fn)


def test_the_transcript_is_the_script_output():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_witness_and_the_transporter():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "k = e~ - f~      square -2   delta = k + f~'   square -2   w = 2e~ + e~'   square 0" in out
    assert "w . delta = 0   (the witness's cheap test)" in out
    assert "integral True   isometry True   determinant 1   tau(k) = delta True" in out
    assert "discriminant action trivial: False" in out


def test_the_cheap_route_is_closed_for_every_elementary_transporter():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "elementary transvections realising k |-> delta found: 28" in out
    assert "of those with trivial discriminant action: 0" in out


def test_the_reduction_and_its_printed_source_are_stated():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "AEGS25, printed p. 587" in out
    assert "Namikawa, Math. Ann. 270 (1985), Thm. 2.13" in out
    assert "does rho(Stab_{O(T_En)}(k)) meet the coset of rho(tau)" in out
    assert "verdict: undecided" in out


def test_the_page_asks_the_question_in_the_same_terms():
    text = PAGE.read_text(encoding="utf-8")
    assert "\\beta_\\ten\\bigl(\\tilde w,\\ \\gamma^{-1}k\\bigr) = 0" in text
    assert "orthogonal to a $(-2)$-vector in the $\\Gamma_\\En$-orbit of $k$" in text


@_red
def test_the_witness_class_is_recorded():
    """Red until some page says whether the class of w = 2e~ + e~' lies in the image of Phi."""
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "2\\tilde e+\\tilde e'" in line or "2\\tilde e + \\tilde e'" in line:
                if re.search(r"image of \$\\Phi\$|in the image|lies over a Coble", line):
                    return
    raise AssertionError(
        "no page records whether the class of w = 2e~ + e~' lies in the image of Phi"
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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the witness class)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

"""Acceptance gate for the second residue research#658 leaves open: the image of Phi.

The register row (writing/open-questions.md, "Which divisibility-2 0-cusps lie over a Coble 0-cusp")
asks for the image of the orbit map Phi of sec-enriques-coble-correspondence.  prop:cusp-map-not-onto
excludes the divisibility-1 cusps; assertiveness aside, what is not recorded is which divisibility-2
classes are in the image.

What is settled, and what the checks below pin:

  a. the criterion is on the page: a class is in the image exactly when its vector is orthogonal to an
     element of the Gamma_En-orbit of k, i.e. to a (-2)-vector in that orbit;
  b. the witness that the necessary condition "orthogonal to some (-2)-vector" is not by itself the
     criterion -- w = 2e~ + e~', orthogonal to delta = e~ - f~ + f~' -- is verified exactly by
     computations/reports/coble_658-image-witness-probe.py, whose transcript is committed beside it;
  c. the shape of what remains: AEGS25 printed p. 587 (after Namikawa, Math. Ann. 270 (1985),
     Thm. 2.13) gives a single (-2)-vector of T_En modulo O(T_En), so no O(T_En)-invariant can refine
     the cheap test and the residue is exactly the transitivity of the stable group O~+(T_En) on the
     (-2)-vectors.

The RED test: the image is not recorded, so a test that asserts it is on the page must fail.  It is
marked strict xfail, so the suite stays green while the item is open, it turns green when the page
records the image, and it fails loudly if the marker is left behind after that.

Run standalone (``python3 tests/engineering/test_coble_658_image_residue.py``) or under pytest.
"""

from __future__ import annotations

import pathlib
import re

try:                                        # pytest marks the red item; standalone prints it as RED
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"
REGISTER = ROOT / "writing/open-questions.md"
PROBE = ROOT / "computations/reports/coble_658-image-witness-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-image-witness-probe-run.txt"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658, the image of Phi: the page records the criterion and the witness but "
               "not the image; the deciding input is a generating set of Gamma_En shown to move k to a "
               "chosen (-2)-vector. Remove this marker when the image is recorded.",
    )(fn)


def test_the_criterion_is_on_the_page():
    text = PAGE.read_text(encoding="utf-8")
    assert "\\beta_\\ten\\bigl(\\tilde w,\\ \\gamma^{-1}k\\bigr) = 0" in text
    assert "orthogonal to a $(-2)$-vector in the $\\Gamma_\\En$-orbit of $k$" in text


def test_the_witness_is_verified_exactly():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "k = e~ - f~                  square  -2  divisibility 1  primitive True" in out
    assert "delta = e~ - f~ + f~'        square  -2  divisibility 1  primitive True" in out
    assert "w = 2e~ + e~'                square   0  divisibility 2  primitive True" in out
    assert "w . delta = 0   (the cheap test: orthogonal to a (-2)-vector)" in out
    assert "e~' . k = 0   (orthogonal to k itself, so its class is in the image)" in out
    assert PROBE.is_file()


def test_the_probe_reproduces_its_transcript():
    """The committed transcript is the committed script's output, not a hand-written record."""
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")


def test_the_printed_statement_is_cited_where_the_residue_is_stated():
    out = TRANSCRIPT.read_text(encoding="utf-8")
    assert "AEGS25, printed p. 587" in out
    assert "Namikawa, Math. Ann. 270 (1985), Thm. 2.13" in out
    assert "unique (-2)-vector of T_En modulo O(T_En)" in out


def test_the_register_row_states_the_criterion_and_not_a_claim():
    text = REGISTER.read_text(encoding="utf-8")
    row = [l for l in text.splitlines() if "Which divisibility-$2$ $0$-cusps lie over a Coble" in l][0]
    assert "@thm:coble-strong-lifting" in row and "@prop:cusp-map-injective" in row
    assert "is open" in row


@_red
def test_the_image_of_phi_is_recorded():
    """Red until the page states which divisibility-2 classes are in the image."""
    text = PAGE.read_text(encoding="utf-8")
    statements = re.findall(r"[^\n]*image of \$\\Phi\$[^\n]*", text)
    assert any("exactly" in s and "all" in s for s in statements), (
        "the page states the complement of the image and its criterion, but not the image"
    )


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            if name == "test_the_image_of_phi_is_recorded":
                print(f"RED  {name}: {exc}")
                continue
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass "
          f"(1 red expected: the image of Phi)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

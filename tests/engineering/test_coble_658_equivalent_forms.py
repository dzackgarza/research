"""Red test first: the four equivalent forms of item 1e are not collected on any page.

LEMMA.  The following are equivalent, for Gamma_Co acting on T_Co with the sign lemma
(lem:monodromy-is-spinor-positive) in force:
  (a) rho(Gamma_Co) = 1, i.e. Gamma_Co <= ker(rho_{T_Co})                     -- item 1e;
  (b) Gamma_Co fixes each of the 527 nonzero isotropic classes of A_{T_Co};
  (c) every Gamma_Co-orbit on the 527 0-cusps of D(T_Co)/O~+(T_Co) is a singleton;
  (d) the index [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| is 1.

PROOF.
  (a) <=> (b): coble_658-isotropic-separates-probe.py -- the isotropic classes generate ker(2q) of index
      two, and an isometry fixing ker(2q) pointwise is the identity.
  (b) <=> (c): thm:coble-zero-cusp-count(1) puts the 527 nonzero isotropic classes of A_{T_Co} in bijection
      with the 527 orbits of the discriminant kernel on primitive isotropic lines, and (2) with the 527
      0-cusps of the stable quotient; the class of v/2 is Gamma_Co-invariant because rho is the action.
  (a) <=> (d): coble_658-index-narrowing-probe.py -- Gamma_Co <= O^+(T_Co) makes
      Gamma_Co cap O^+(T_Co) the kernel of rho on Gamma_Co, so the first isomorphism theorem gives
      the index as |rho(Gamma_Co)|.
So the four forms stand or fall together, and the item may be attacked in whichever is convenient.  []

This test is RED because no page collects the four forms.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_four_forms_are_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e has four equivalent forms -- rho(Gamma_Co) = 1, the 527 isotropic "
               "classes fixed, the 527 0-cusps fixed, the index equal to 1 -- and no page collects them. "
               "Remove this marker when one does.",
    )(fn)


@_red
def test_the_four_forms_are_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "527" in line and "isotropic" in line and "0-cusp" in line:
                if "equivalent" in line or "if and only if" in line or "index" in line:
                    return
    raise AssertionError(
        "no page collects the four equivalent forms of item 1e: rho(Gamma_Co) = 1, the 527 isotropic "
        "classes fixed, the 527 0-cusps fixed, the index [Gamma_Co : Gamma_Co cap O~+] equal to 1"
    )


def test_the_numbers_the_equivalences_rest_on():
    probe = ROOT / "computations/reports/coble_658-equivalent-forms-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-equivalent-forms-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "A_{T_Co}: |A| = 2048, nonzero isotropic classes = 527" in transcript
    assert "= 46998591897600 / 67456 = 696729600" in transcript
    assert "(d) [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| = 1  (a divisor of 696729600)" in transcript
    assert "verdict: the lemma holds" in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the four forms)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

"""Red test first: the conditional corollary is on no page.

COROLLARY.  Under conj:gamma-co-stable, the conclusion of thm:coble-strong-lifting holds with Gamma_Co in
place of O~+(T_Co): every phi in Gamma_Co has exactly one lift gamma in Gamma_En with
gamma o eta = eta o phi and gamma(k) = k, the assignment is a homomorphism of which res is a left inverse,
and eta is equivariant.

PROOF.  conj:gamma-co-stable gives Gamma_Co = O~+(T_Co) (coble_658-forward-half-probe.py shows the item's
forward half is what is needed), and prop:gamma-co-strong-lifting says the conclusion holds with Gamma_Co in
place of O~+ exactly when Gamma_Co <= O~+(T_Co).  Under the conjecture that containment is an equality.  []

So research#658's first item is a THEOREM of the book modulo the book's own conjecture, and only its
unconditional form is open.

This test is RED because no page states the corollary.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_conditional_corollary_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1: under conj:gamma-co-stable the Gamma_Co form of "
               "thm:coble-strong-lifting follows from prop:gamma-co-strong-lifting, since the conjecture "
               "gives the inclusion it needs. No page states the corollary. Remove this marker when one "
               "does.",
    )(fn)


@_red
def test_the_conditional_corollary_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "conj:gamma-co-stable" in line and "thm:coble-strong-lifting" in line:
                if "corollary" in line or "follows" in line or "gives" in line:
                    return
    raise AssertionError(
        "no page records that the Gamma_Co form of thm:coble-strong-lifting follows from "
        "conj:gamma-co-stable via prop:gamma-co-strong-lifting"
    )


def test_the_chain_is_read_from_the_pages():
    probe = ROOT / "computations/reports/coble_658-conditional-corollary-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-conditional-corollary-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "the page states conj:gamma-co-stable (Gamma_Co = O~+(T_Co)):      True" in transcript
    assert "prop:gamma-co-strong-lifting says (1) and (2) are equivalent:     True" in transcript
    assert "verdict: the corollary holds." in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the conditional corollary)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

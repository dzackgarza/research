"""Red test first: the pointwise-fixing criterion for item 1e is on no page.

LEMMA.  Let g be an isometry of the K3 lattice L = II_{3,19} preserving S_Co and T_Co and fixing S_Co
pointwise.  Then its restriction to T_Co acts trivially on A_{T_Co}.  Consequently the monodromy of any family
whose local system has S_Co fixed pointwise lies in ker(rho_{T_Co}) -- item 1e for such a family.

PROOF.  By cor:lifting-unimodular the two restrictions of a gluing-preserving isometry satisfy
bar-phi o gamma = gamma o bar-psi, gamma: A_{S_Co} -> A_{T_Co}(-1) being the gluing isometry.  With
psi = id, bar-psi = 1, so bar-phi = gamma o 1 o gamma^{-1} = 1.  Equivalently, and by the same identity as
lem:coble-discriminant-actions-conjugate: an element with trivial S_Co-side action is in the kernel.  []

So the obstruction in item 1e is exactly the S_Co-side action: it is not the fixing of a class or two (H and
alpha) but the pointwise fixing of the whole summand that forces the discriminant action to vanish.  A family
whose monodromy fixes only H and alpha is not covered -- which is why cor:construction-monodromy, a
containment in the stabilizer of the quadruple (S_Co, S_dP, H, alpha), does not give the item.

This test is RED because no page states the criterion.
"""

from __future__ import annotations

import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_pointwise_criterion_is_on_a_page"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e: an isometry fixing S_Co pointwise acts trivially on A_{T_Co} "
               "(bar-phi = gamma bar-psi gamma^{-1} at bar-psi = 1), so the item holds for any family whose "
               "local system fixes S_Co pointwise. No page states the criterion. Remove this marker when "
               "one does.",
    )(fn)


def test_the_ingredients_are_on_the_pages():
    lifting = (ROOT / "writing/lattice-theory/automorphism-lifting-through-a-gluing.md").read_text(
        encoding="utf-8")
    assert "bar{\\varphi}_N\\circ\\gamma=\\gamma\\circ\\bar{\\varphi}_M" in lifting
    cusp = (ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md").read_text(
        encoding="utf-8")
    assert "\\bar\\varphi = \\gamma\\,\\bar\\psi\\,\\gamma^{-1}" in cusp


@_red
def test_the_pointwise_criterion_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "pointwise" in line and "S_{\\\\Co}" in line and "ker" in line:
                return
    raise AssertionError(
        "no page records that an isometry fixing S_Co pointwise acts trivially on A_{T_Co}, so item 1e holds "
        "for any family whose local system fixes S_Co pointwise"
    )


def test_the_substitution_is_printed():
    probe = ROOT / "computations/reports/coble_658-pointwise-criterion-probe.py"
    transcript = (ROOT / "computations/reports/coble_658-pointwise-criterion-probe-run.txt").read_text(
        encoding="utf-8")
    import contextlib
    import io
    ns = {}
    exec(compile(probe.read_text(encoding="utf-8"), str(probe), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == transcript
    assert "cor:lifting-unimodular: bar-phi o gamma = gamma o bar-psi     True" in transcript
    assert "substituting bar-psi = 1 (S_Co fixed pointwise): bar-phi = gamma o gamma^{-1} = 1." in transcript
    assert "verdict: the lemma holds." in transcript


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the pointwise criterion)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

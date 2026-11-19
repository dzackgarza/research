"""Item 1f's transitivity shortcut is not available: T_En is 2-elementary, not unimodular.

A draft route to item 1f was to prove Gamma_En transitive on the primitive isotropic vectors of
T_En and then read surjectivity of Phi off it.  That route transplants the proof of
lem:I29-plus-line-transitivity, which splits the lattice at a primitive isotropic vector by
cor:hyperbolic-splitting -- a corollary that requires the lattice to be unimodular.

T_En is not unimodular: it is U + U(2) + E8(2), rank 12, signature (2,10), determinant 2^10,
2-elementary with A_{T_En} = (Z/2)^10 [@AEGS25, Def. 2.3, printed p. 586].  The unimodular lattice
of the same shape is the Enriques lattice U + E8(-1), rank 10, signature (1,9) -- a different
object.  This module holds that computation, which refutes the shortcut, and checks the probe's
transcript against a fresh run.

Run standalone (``python3 tests/engineering/test_coble_658_ten_transitivity.py``) or under pytest.
"""

from __future__ import annotations

import contextlib
import io
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROBE = ROOT / "computations/reports/coble_658-ten-transitivity-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-ten-transitivity-probe-run.txt"


def test_the_invariants_are_computed_as_stated():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    out = buf.getvalue()
    assert out == TRANSCRIPT.read_text(encoding="utf-8")
    assert "T_En = U+U(2)+E8(2) rank 12   even True   det +1024   signature (2,10)" in out
    assert "U + E8(-1) (Enriques) rank 10   even True   det -1   signature (1,9)" in out
    assert "verdict: the transitivity shortcut for item 1f is REFUTED." in out


def test_the_shortcut_needs_unimodularity():
    """Both splitting results the transitivity proofs use require unimodularity of the lattice."""
    page = (ROOT / "writing/lattice-theory/embeddings-and-overlattices.md").read_text(encoding="utf-8")
    cor = page[page.index("#cor:hyperbolic-splitting"):]
    cor = cor[:cor.index("\n:::")]
    assert "unimodular" in cor
    odd = page[page.index("#lem:odd-unimodular-isotropic-splitting"):]
    odd = odd[:odd.index("\n:::")]
    assert "odd unimodular" in odd
    tail = page[page.index("#lem:I29-plus-line-transitivity"):]
    assert "odd-unimodular-isotropic-splitting" in tail[:tail.index("#thm:plane-transitivity-tco")]


def test_the_page_states_one_f_at_the_strength_of_its_proof():
    """The proposition is about classes; the orbit question is stated as open, not as a theorem."""
    page = (ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md").read_text(
        encoding="utf-8")
    start = page.index("#prop:cusp-map-surjective-on-classes")
    block = page[start:page.index("\n:::", page.index("\n", start))]
    assert "The divisibility-$2$ classes are exactly the classes of the image" in block
    assert "is a question about the orbits of $\\Gamma_\\En$" in block
    assert "open" in block


def _run_all() -> int:
    items = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in items:
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {name}: {exc}")
        else:
            print(f"ok   {name}")
    print(f"\n{len(items) - failures}/{len(items)} checks pass")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

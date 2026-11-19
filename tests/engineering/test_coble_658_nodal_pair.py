"""Red test first: the nodal-pair reading that decides item 1e is on no page.

LEMMA.  The record of the one-node construction (computations/reports/smwo_direct-period.md,
Theorem E) states that the monodromy image G1 contains the nodal-pair transformations with
s = delta + delta', e = delta - delta', s^2 = e^2 = -4, and that "the nodal-pair products ...
act on T_Co as the reflection in a class e of square -4".  The parenthesised (w_s, w_e) of that
item is the block decomposition of the single element w_delta w_delta', not a pair of monodromy
elements: w_delta alone does not preserve the summands S_Co, T_Co.

That element acts on T_Co as the reflection w_e in a (-4)-class.  By the page's own
@prop:gamma-co-reflective-set(3), s_v for v^2 = -4 lies in O^+(T_Co) and NOT in ker rho_{T_Co},
so Gamma_Co is not contained in the discriminant kernel: item 1e is FALSE, and with it the
Gamma_Co form of the strong lifting (@prop:gamma-co-strong-lifting, (1) <=> (2)) and the forward
half Gamma_Co <= O~^+(T_Co) of @conj:gamma-co-stable.

The probe computes the block identity from scratch, the integrality and spinor sign of w_e, and
its non-trivial action on A_{T_Co}.  This test is RED because no page records the consequence.

Run standalone (``python3 tests/engineering/test_coble_658_nodal_pair.py``) or under pytest.
"""

from __future__ import annotations

import contextlib
import io
import pathlib

try:
    import pytest
except ImportError:                         # pragma: no cover
    pytest = None


ROOT = pathlib.Path(__file__).resolve().parents[2]
RED_NAME = "test_the_nodal_pair_monodromy_is_on_a_page"
PROBE = ROOT / "computations/reports/coble_658-nodal-pair-refutation-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-nodal-pair-refutation-probe-run.txt"


def _red(fn):
    if pytest is None:
        return fn
    return pytest.mark.xfail(
        strict=True,
        reason="research#658 item 1e is refuted: the nodal-pair monodromy acts on T_Co as the "
               "reflection in a (-4)-class, which lies outside the discriminant kernel. No page "
               "records it. Remove this marker when one does.",
    )(fn)


def test_the_record_is_as_quoted():
    text = (ROOT / "computations/reports/smwo_direct-period.md").read_text(encoding="utf-8")
    assert "nodal-pair transformations" in text
    assert "`G1` contains `W_node" in text
    assert "nodal-pair products, which act on `T_Co` as the reflection in a class `e` of square `-4`" in text


def test_the_block_identity_is_computed():
    ns = {}
    exec(compile(PROBE.read_text(encoding="utf-8"), str(PROBE), "exec"), ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ns["main"]()
    assert buf.getvalue() == TRANSCRIPT.read_text(encoding="utf-8")
    out = buf.getvalue()
    assert "w_delta w_delta' acts on T_Co exactly as the reflection w_e in the (-4)-class e: True" in out
    assert "the reflection w_e is integral on T_Co: True" in out
    assert "w_e acts trivially on A_{T_Co}: False" in out
    assert "verdict: item 1e is FALSE." in out


@_red
def test_the_nodal_pair_monodromy_is_on_a_page():
    for path in sorted((ROOT / "writing").rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if "nodal-pair" in line and ("(-4)" in line or "square $-4$" in line) and "monodromy" in line:
                return
    raise AssertionError(
        "no page records that the nodal-pair monodromy acts on T_Co as the reflection in a "
        "(-4)-class, hence lies outside the discriminant kernel and refutes item 1e"
    )


def test_the_argument_is_a_proposal_that_names_its_missing_inputs():
    """The reviewer's condition on main: the (-4)-reflection stays, as a proposal with named gaps."""
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text(encoding="utf-8")

    def block(label):
        start = lattices.index("#" + label)
        body = lattices.index("\n", start) + 1
        return lattices[body:lattices.index("\n:::", body)]

    conj = block("conj:gamma-co-stable")
    assert "is false" not in conj, "the conjecture is open; it may not be marked refuted"

    proposal = block("rmk:gamma-co-nodal-pair-proposal")
    assert "smw0o7jbf/m5" in proposal, "the off-main derivation must be named as missing"
    assert "restrict ourselves to these classical examples" in proposal, "DK13's scope must be named"
    assert "contained in $\\Gamma_\\Co$" in proposal, "the containment step must be named"
    assert "proposal, not a theorem" in proposal


def test_the_classical_model_cannot_host_the_witness():
    """The proposal's gap 2 has a reason: in DK13's model the node classes lie in M_X, orthogonal to T_Co."""
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text(encoding="utf-8")
    start = lattices.index("#rmk:gamma-co-nodal-pair-proposal")
    body = lattices[start:lattices.index("\n:::", lattices.index("\n", start))]
    assert "M_X\\cong\\generators{2}\\oplus\\generators{-2}" in body
    assert "acts as the identity on $T_\\Co$" in body
    assert "they are not vanishing classes" in body
    assert "neither produced nor excluded by it" in body
    assert "(-4)$-Heegner divisor" in body
    assert "the meridians to generate" in body
    assert "an input, not a result of this book" in body
    assert "cons:lefschetz-periods" in body


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
    print(f"\n{len(items) - failures}/{len(items)} checks pass (1 red expected: the nodal-pair monodromy)")
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if _run_all() else 0)

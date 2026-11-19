"""The nodal-pair reading that decides item 1e, and its statement on the page.

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

ROOT = pathlib.Path(__file__).resolve().parents[2]
PROBE = ROOT / "computations/reports/coble_658-nodal-pair-refutation-probe.py"
TRANSCRIPT = ROOT / "computations/reports/coble_658-nodal-pair-refutation-probe-run.txt"


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


def test_the_refutation_is_stated_on_the_page():
    lattices = (ROOT / "writing/coble/lattices-and-moduli/lattices.md").read_text(encoding="utf-8")

    def block(label):
        start = lattices.index("#" + label)
        body = lattices.index("\n", start) + 1
        return lattices[body:lattices.index("\n:::", body)]

    thm = block("thm:gamma-co-not-stable")
    assert "\\Gamma_\\Co\\not\\subseteq\\widetilde\\Orth^+(T_\\Co)" in thm
    assert "@prop:gamma-co-reflective-set(3)" in thm

    conj = block("conj:gamma-co-stable")
    assert "This statement is false" in conj and "@thm:gamma-co-not-stable" in conj
    assert "@conj:gamma-co-full" in conj

    assert "\\Gamma_\\Co = \\Orth^+(T_\\Co)" in block("conj:gamma-co-full")

    status = block("rmk:gamma-co-status")
    assert "Neither inclusion" not in status
    assert "is false (@thm:gamma-co-not-stable)" in status

    counts = block("rmk:gamma-co-counts")
    assert "are not those of the stable quotient" in counts


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

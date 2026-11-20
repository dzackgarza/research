"""Red test first: the sextic base's group and the two indices are on no page.

LEMMA (to be proved).  For T = 10A_1, P = <H> + L with L = A_1^10, Q = P^perp = T_Co,
the monodromy group Gamma_T of Yu--Zheng--Zhong (Theorem 3.4, Proposition 6.5(ii)) is

    Gamma_{10A_1} = O^+(T_Co) cap rho-bar^{-1}(Theta),

with Theta = gamma * rho-bar_M(S_10) * gamma^{-1}, |Theta| = 10!, and

    [Gamma_{10A_1} : Otilde^+(T_Co)] = 10!,   [O^+(T_Co) : Gamma_{10A_1}] = |O(q)|/10! = 12951552,

so Otilde^+(T_Co) is properly contained in Gamma_{10A_1}, which is properly contained in O^+(T_Co).

The page carried the identification only as a citation to YZZ25 and the index only as an
inequality (dividing 10!).  This test is RED until both are proved statements on the page.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

OQ = 46998591897600              # |O(q_{T_Co})| = 2^21 3^5 5^2 7 17 31
TEN_FACTORIAL = 3628800
INDEX_SEXTIC = 12951552          # 2^13 3 17 31


def test_the_arithmetic_of_the_two_indices():
    assert TEN_FACTORIAL * INDEX_SEXTIC == OQ
    assert OQ // TEN_FACTORIAL == INDEX_SEXTIC
    assert 2**13 * 3 * 17 * 31 == INDEX_SEXTIC


def _blocks(text: str) -> dict[str, str]:
    out = {}
    for m in re.finditer(r"^:{3,}\s*\{[^}\n]*#([\w:.-]+)", text, re.M):
        start = m.end()
        end = text.find("\n:::", start)
        out[m.group(1)] = text[start:end]
    return out


def test_the_sextic_identification_is_a_proved_statement():
    text = LATTICES.read_text(encoding="utf-8")
    blocks = _blocks(text)
    assert "thm:gamma-co-sextic-group" in blocks, sorted(k for k in blocks if "sextic" in k)
    body = blocks["thm:gamma-co-sextic-group"]
    assert "\\Gamma_{10A_1}" in body
    assert "\\bar\\rho^{-1}(\\Theta)" in body
    assert "\\widetilde\\Orth^+(T_\\Co)" in body
    # the two indices, as displays
    assert "10!" in body
    assert "12\\,951\\,552" in body or "12951552" in body
    # strictness in both directions
    assert "\\subsetneq" in body
    # the proof cites the numbered statements of the two sources
    proof_start = text.index("#thm:gamma-co-sextic-group")
    proof = text[proof_start:proof_start + 9000]
    for key in ("YZZ25, Prop. 6.5", "YZZ25, Lemma 6.7",
                "YZZ25, Thm. 3.4", "Nik80, Cor. 1.5.2"):
        assert key in proof, key


def test_the_corollary_points_at_the_proved_identification():
    text = LATTICES.read_text(encoding="utf-8")
    start = text.index("#cor:gamma-co-inclusions")
    body = text[start:text.index("\n:::", start)]
    assert "@thm:gamma-co-sextic-group" in body
    assert "\\subsetneq" in body


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
    raise SystemExit(_run_all())

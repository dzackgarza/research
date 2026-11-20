"""The two statements of research#797, items 3 and 4, and the guard on their form.

Item 3 asks for the quotient presentation of the S_Co-polarized moduli stack with its
hypotheses checked; item 4 for the monodromy exact sequence with the covering it
defines.  Both pins below are on the statements themselves, not on the implementation
of any computation, together with one guard for the failure mode that bit this page:
a doubled control sequence inside math, which pandoc keeps verbatim and TeX then
fails to convert.
"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
MC = ROOT / "writing/coble/lattices-and-moduli/moduli-construction.md"

QUOTIENT = "prop:coble-quotient-presentation"
MONODROMY = "thm:monodromy-exact-sequence"


def _block(text: str, label: str) -> str:
    assert "#" + label in text, f"#{label} is not on the page"
    start = text.index("#" + label)
    body = text.index("\n", start) + 1
    return text[body:text.index("\n:::", body)]


def test_the_quotient_presentation_is_stated_with_its_hypotheses():
    body = _block(MC.read_text(encoding="utf-8"), QUOTIENT)
    # condition (U) is by [@Dol96, Prop. 5.1], and its disjunct at t = 10 is the one used
    assert "@Dol96, Prop. 5.1" in body
    assert "or** $t\\leq10$" in body or "**or** $t\\leq10$" in body
    assert "U(2)" in body
    # the presentation itself, and the group it is by
    assert "\\widetilde\\Orth^+(T_\\Co)" in body
    # the non-emptiness is NOT claimed from the proposition whose t <= 9 fails
    assert "@Dol96, Cor. 5.2" in body


def test_the_monodromy_sequence_is_stated_with_its_cover():
    body = _block(MC.read_text(encoding="utf-8"), MONODROMY)
    assert "K_\\bL" in body and "\\operatorname{Mon}(\\bL)" in body
    assert "1\\too K_\\bL\\too\\pi_1(X,x)\\too\\operatorname{Mon}(\\bL)\\too1" in body
    assert "Theorem 18.19" in body and "Corollary 18.20" in body
    assert "Definition 18.10" in body
    assert "deck transformations" in body


def test_no_doubled_control_sequence_in_either_block():
    text = MC.read_text(encoding="utf-8")
    for label in (QUOTIENT, MONODROMY):
        body = _block(text, label)
        assert not re.search(r"\\\\+[A-Za-z]+", body), label

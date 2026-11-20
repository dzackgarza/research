"""research#658 item 1e: the "induces" clause, read strongly, would prove the item -- a tension refuted.

LEMMA (refuted).  def:gamma-co-groups(1)'s clause "The family of unpolarized Enriques surfaces, whose local
system of lattices has fibre T_En and monodromy group Gamma_En, induces this family and its local system" and
rmk:gamma-co-status's "Neither inclusion between Gamma_Co and O~+(T_Co) is proved" are compatible under any
reading on which the clause carries information.

REFUTATION.  Strong reading: the Coble local system is the restriction of the Enriques one along a map of
bases; a loop of the Coble family is then the image of a loop of the Enriques family, acting on T_Co through
its action on T_En.  The Enriques monodromy group in the book is Gamma_En = O~+(T_En) = ker(rho_{T_En}) cap
O^+(T_En) (@def:gamma-co-groups), and @prop:gamma-co-images(1) says the image of Stab_{Gamma_En}(delta) in
O(delta^perp) = O(T_Co) is exactly O~+(T_Co).  Under the strong reading, then, Gamma_Co <= O~+(T_Co) -- item
1e -- contradicting rmk:gamma-co-status.  Weak reading: the clause relates the lattices only, and does no
work.  []

The probe reads the three sentences from the page -- the clause, the remark, and prop:gamma-co-images(1) --
and prints the two readings and the consequence of each.  It decides nothing about Gamma_Co; it shows that
the page cannot be read as giving item 1e for free, and that the book owes a statement of which reading it
intends.

Usage: python3 computations/reports/coble_658-induces-tension-probe.py
"""

from __future__ import annotations

import pathlib

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"


def main():
    text = LATTICES.read_text(encoding="utf-8")
    clause = "induces this family and its local system" in text
    remark = "Neither inclusion between $\\Gamma_\\Co$ and $\\widetilde\\Orth^+(T_\\Co)$ is proved" in text
    prop1 = "1. $R_{\\Gamma_\\En} = \\widetilde\\Orth^+(T_\\Co)$." in text
    print("def:gamma-co-groups(1) carries the 'induces' clause:        %s" % clause)
    print("rmk:gamma-co-status says neither inclusion is proved:      %s" % remark)
    print("prop:gamma-co-images(1) gives R_{Gamma_En} = O~+(T_Co):    %s" % prop1)
    assert clause and remark and prop1
    print()
    print("strong reading: Gamma_Co <= R_{Gamma_En} = O~+(T_Co) = item 1e -- contradicting the remark.")
    print("weak reading:   the clause relates the two lattices only, and yields no inclusion.")
    print()
    print("verdict: REFUTED as stated.  The three sentences cannot stand together with the clause")
    print("  informative: either the book's Enriques monodromy identification and its 'induces' clause")
    print("  give item 1e (and rmk:gamma-co-status is wrong), or the clause is weaker than it reads and")
    print("  the book owes the weaker statement in writing.  Item 1e is not thereby decided.")


if __name__ == "__main__":
    main()

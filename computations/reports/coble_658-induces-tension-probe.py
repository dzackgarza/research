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
    remark = "The inclusion $\\Gamma_\\Co\\subseteq\\widetilde\\Orth^+(T_\\Co)$ is false" in text
    prop1 = "1. $R_{\\Gamma_\\En} = \\widetilde\\Orth^+(T_\\Co)$." in text
    print("def:gamma-co-groups(1) carries the 'induces' clause:        %s" % clause)
    print("rmk:gamma-co-status says the inclusion is false:           %s" % remark)
    print("prop:gamma-co-images(1) gives R_{Gamma_En} = O~+(T_Co):    %s" % prop1)
    assert clause and remark and prop1
    print()
    print("The tension the earlier version of this probe recorded is gone, and it is resolved against")
    print("the strong reading: a loop of the Coble family need not come from the Enriques base -- the")
    print("period of a Coble surface lies in the Heegner divisor mch_{-2}, which the Enriques moduli")
    print("excludes -- and the monodromy itself is now known to leave the stable group:")
    print("Gamma_Co is not contained in O~+(T_Co) (thm:gamma-co-not-stable).  So the 'induces' clause")
    print("is the weak one, and the book states it as a relation of local systems, not of bases.")
    print()
    print("verdict: RESOLVED.  The strong reading is refuted by thm:gamma-co-not-stable, and")
    print("  rmk:gamma-co-status now records the failure instead of an open inclusion.")


if __name__ == "__main__":
    main()

"""research#658 item 1e: the book's computed group would falsify the item -- the dichotomy.

LEMMA.  Let rho = rho_{T_Co}.  Either rho(Gamma_Co) = 1 (item 1e holds) or rho(Gamma_Co) contains a
nontrivial element moving some nonzero isotropic class of A_{T_Co}.  Consequently, if rho(Gamma_Co) equals
the group G_Co of thm:coble-heegner-finite-orbits(2) -- order |W(E_8)| = 696,729,600, orbits
[1, 2, 120, 135, 270] on the 528 isotropic classes -- then item 1e is FALSE.

PROOF.  If rho(Gamma_Co) != 1 pick g != 1 in it; by coble_658-isotropic-separates-probe.py an isometry of
(A_{T_Co}, q) that fixes every nonzero isotropic class is the identity, so g moves one.  The group G_Co is
nontrivial: the orbit of 0 is {0}, and the other orbits have lengths 2, 120, 135 and 270
(thm:coble-heegner-finite-orbits(2), printed on that page).  So rho(Gamma_Co) = G_Co puts a class-moving
element in the image, which is the negation of item 1e.  []

What the probe checks: that the page really carries the orbit list and the order (read from the source), the
arithmetic |W(E_8)| = 696,729,600 = |P| = |O(q_{T_Co})| / [O(T_Co) : R_{gent}], and the sum 1+2+120+135+270
= 528.  It draws no conclusion about which alternative holds.

Usage: python3 computations/reports/coble_658-dichotomy-probe.py
"""

from __future__ import annotations

import pathlib
import re

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

PAGE = ROOT / "writing/coble/lattices-and-moduli/the-heegner-line-and-the-coble-arithmetic-group.md"
ORDER_W_E8 = 696_729_600
ORBITS = [1, 2, 120, 135, 270]
ORDER_OQ = 46_998_591_897_600
INDEX_R = 67_456


def main():
    text = PAGE.read_text(encoding="utf-8")
    has_orbits = any("120," in ln and "135," in ln and "270" in ln
                     for ln in text.splitlines())
    has_order = "has order $\\abs{W(E_8)} = 696\\,729\\,600$" in text
    print("the page carries the orbit list [1, 2, 120, 135, 270]: %s" % has_orbits)
    print("the page carries the order |W(E_8)| = 696,729,600:      %s" % has_order)
    assert has_orbits and has_order

    print("orbit lengths sum to |A_{T_Co}| - 1 = 527: %s" % (sum(ORBITS) - 1 == 527))
    assert sum(ORBITS) - 1 == 527
    assert ORDER_OQ // INDEX_R == ORDER_W_E8
    print("and |O(q_{T_Co})| / [O(T_Co) : R_{gent}] = %d = |W(E_8)|, so G_Co and P have the same order"
          % (ORDER_OQ // INDEX_R))
    print()
    print("verdict: the dichotomy holds.  rho(Gamma_Co) is either trivial -- item 1e -- or contains an")
    print("  element moving a nonzero isotropic class, in which case the item fails.  The book's computed")
    print("  group G_Co has nontrivial orbits (2, 120, 135, 270 on the nonzero classes), so if the")
    print("  monodromy's image were G_Co the item would be FALSE.  Which alternative holds is not decided")
    print("  here.")


if __name__ == "__main__":
    main()

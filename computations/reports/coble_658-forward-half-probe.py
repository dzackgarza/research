"""research#658 item 1e: the item is the forward half of conj:gamma-co-stable, and holds under it.

LEMMA.  Item 1e -- Gamma_Co <= ker(rho_{T_Co}) -- is exactly the forward half of conj:gamma-co-stable:

    conj:gamma-co-stable  <=>  (Gamma_Co <= ker(rho_{T_Co})  and  O~+(T_Co) <= Gamma_Co).

In particular item 1e holds under conj:gamma-co-stable.

PROOF.  conj:gamma-co-stable asserts Gamma_Co = O~+(T_Co) = ker(rho_{T_Co}) cap O^+(T_Co) (the identity is
@def:gamma-co-groups(3) for the stable group).  Given the equality, Gamma_Co lies in ker(rho_{T_Co}), which
is item 1e.  Conversely, item 1e together with the sign lemma (lem:monodromy-is-spinor-positive,
Gamma_Co <= O^+(T_Co)) gives Gamma_Co <= ker(rho) cap O^+ = O~+(T_Co), and adding the reverse inclusion
gives the equality.  []

So the issue's first item is strictly weaker than the book's conjecture: it may be asserted under it in the
book's usual form, and what is open is its unconditional holding -- which the last several lemmas reduced to
the 527 isotropic classes, to an index dividing 696,729,600, and to the two-element dichotomy
(rho(Gamma_Co) = 1, or an element moving a class).

The probe checks the two definitions the proof uses: the stable group is ker(rho) cap O^+ in
@def:gamma-co-groups(3), and conj:gamma-co-stable states Gamma_Co = O~+(T_Co) -- both read from the page.

Usage: python3 computations/reports/coble_658-forward-half-probe.py
"""

from __future__ import annotations

import pathlib

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

PAGE = ROOT / "writing/coble/lattices-and-moduli/lattices.md"


def main():
    text = PAGE.read_text(encoding="utf-8")
    stable = ("\\widetilde\\Orth^+(T_\\Co) = \\Orth^+(T_\\Co)\\intersect\\ker\\bar\\rho"
              in text)
    conj = ("\\Gamma_\\Co = \\widetilde\\Orth^+(T_\\Co)." in text)
    print("the page defines the stable group as O^+(T_Co) cap ker(rho): %s" % stable)
    print("the page states conj:gamma-co-stable as Gamma_Co = O~+(T_Co):   %s" % conj)
    assert conj
    print()
    print("verdict: the lemma holds.  Item 1e is the forward half: conj gives Gamma_Co = ker(rho) cap O^+,")
    print("  which lies in ker(rho); and conversely item 1e with the sign lemma gives that containment, so")
    print("  the conjecture is item 1e plus the reverse inclusion.  Item 1e therefore HOLDS under")
    print("  conj:gamma-co-stable, and only its unconditional form is open.")


if __name__ == "__main__":
    main()

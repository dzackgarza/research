"""research#658 item 1: the Gamma_Co lifting is a theorem of the book modulo its own conjecture.

COROLLARY.  Under conj:gamma-co-stable, the conclusion of thm:coble-strong-lifting holds with Gamma_Co in
place of O~+(T_Co).

PROOF.  conj:gamma-co-stable states Gamma_Co = O~+(T_Co); prop:gamma-co-strong-lifting says the conclusion
with Gamma_Co in place of O~+ holds exactly when Gamma_Co <= O~+(T_Co).  Under the conjecture the inclusion
is an equality, so the conclusion holds.  []

The probe reads the three statements it chains from the pages -- the conjecture, the proposition's clause
(2) and the theorem's clause (1) -- and prints the chain.  It decides nothing unconditionally: the
unconditional form is item 1e, reduced on the record to the 527 isotropic classes, to an index dividing
696,729,600 and to the dichotomy of coble_658-dichotomy-probe.py.

Usage: python3 computations/reports/coble_658-conditional-corollary-probe.py
"""

from __future__ import annotations

import pathlib

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"
CUSP = ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"


def main():
    lattices = LATTICES.read_text(encoding="utf-8")
    cusp = CUSP.read_text(encoding="utf-8")

    has_conj = "\\Gamma_\\Co = \\widetilde\\Orth^+(T_\\Co)." in lattices
    has_prop = "2. $\\Gamma_\\Co\\subseteq\\widetilde\\Orth^+(T_\\Co)$" in cusp
    has_thm = "#thm:coble-strong-lifting" in cusp
    has_equiv = "Then (1) and (2) are equivalent" in cusp
    print("the page states conj:gamma-co-stable (Gamma_Co = O~+(T_Co)):      %s" % has_conj)
    print("prop:gamma-co-strong-lifting carries clause (2), the inclusion:   %s" % has_prop)
    print("prop:gamma-co-strong-lifting says (1) and (2) are equivalent:     %s" % has_equiv)
    print("thm:coble-strong-lifting is on the page:                          %s" % has_thm)
    assert has_conj and has_prop and has_equiv and has_thm
    print()
    print("verdict: the corollary holds.  Under conj:gamma-co-stable the inclusion needed by")
    print("  prop:gamma-co-strong-lifting is an equality, so the Gamma_Co form of thm:coble-strong-lifting")
    print("  follows -- the issue's first item is a theorem of the book modulo the book's own conjecture.")
    print("  Unconditionally it remains item 1e, reduced on the record to the 527 isotropic classes, to an")
    print("  index dividing 696,729,600 and to the dichotomy of coble_658-dichotomy-probe.py.")


if __name__ == "__main__":
    main()

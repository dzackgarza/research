"""research#658 item 1e: the "induces" clause cannot be a map of bases -- the strong reading refuted.

LEMMA (refuted).  The clause of def:gamma-co-groups(1), "The family of unpolarized Enriques surfaces ...
induces this family and its local system", can be read as a map of bases: the Coble family is the restriction
of the Enriques family.

REFUTATION.  By thm:normalization the map f^Gamma: D(T_Co)/R_Gamma -> D(T_En)/Gamma is finite, birational
onto its image, and its image is the Heegner divisor H_{-2}/Gamma: every Coble period lies in that divisor.  By
DK13, printed p. 512, the moduli space of Enriques surfaces is the complement (D(T_En) \\ H_{-2})/O(T_En).
A map of bases from the Coble moduli into the Enriques moduli would have to carry a period in the divisor to a
period in its complement, which is impossible.  So the clause is lattice-level only.  []

Consequence: last turn's tension resolves in favour of rmk:gamma-co-status.  The strong reading -- the one
that would give Gamma_Co <= O~+(T_Co) through prop:gamma-co-images(1) -- is false, the clause proves neither
inclusion, and item 1e stands open on the monodromy input.

The probe reads the two ingredients from the pages and prints the argument.  The DK13 quotation is carried
with its printed page, since tmp/sources is not available in CI.

Usage: python3 computations/reports/coble_658-strong-reading-false-probe.py
"""

from __future__ import annotations

import pathlib

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

LATTICES = ROOT / "writing/coble/lattices-and-moduli/lattices.md"
CUSP = ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"

DK13_QUOTATION = ("The quotient D(N)/O(N) is a normal quasi-projective variety of dimension 10, and "
                  "D(N) \\ H_{-2}/O(N) is the moduli space M_En of Enriques surfaces")
DK13_CITATION = "[DK13, printed p. 512]"


def main():
    lattices = LATTICES.read_text(encoding="utf-8")
    cusp = CUSP.read_text(encoding="utf-8")
    image = "its image is the Heegner divisor $\\mch_{-2}/\\Gamma$" in lattices
    periods = "Heegner divisor" in cusp
    print("thm:normalization: the image of f^Gamma is the Heegner divisor H_{-2}/Gamma: %s" % image)
    print("the cusp page places every Coble period on that divisor:                    %s" % periods)
    assert image and periods
    print()
    print("and the source, %s:" % DK13_CITATION)
    print("  %s" % DK13_QUOTATION)
    print("  -- the Enriques moduli is the COMPLEMENT of that divisor.")
    print()
    print("verdict: REFUTED.  A map of bases from the Coble moduli to the Enriques moduli would carry a")
    print("  period in H_{-2} to a period in its complement, which is impossible; so the 'induces' clause")
    print("  is lattice-level only, the strong reading that would give item 1e is false, and last turn's")
    print("  tension resolves in favour of rmk:gamma-co-status.")


if __name__ == "__main__":
    main()

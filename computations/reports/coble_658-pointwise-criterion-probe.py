"""research#658 item 1e: fixing S_Co pointwise forces the discriminant action to vanish.

LEMMA.  Let g be an isometry of the K3 lattice L = II_{3,19} preserving S_Co and T_Co and fixing S_Co
pointwise.  Then its restriction to T_Co acts trivially on A_{T_Co}.  Consequently the monodromy of any family
whose local system has S_Co fixed pointwise lies in ker(rho_{T_Co}) -- item 1e for such a family.

PROOF.  The gluing of S_Co + T_Co in L is unimodular, so A_{S_Co} and A_{T_Co} are glued by an anti-isometry
gamma (cor:lifting-unimodular), and by that corollary -- equivalently by
lem:coble-discriminant-actions-conjugate -- the two restrictions of a gluing-preserving isometry satisfy
    bar-phi o gamma = gamma o bar-psi .
With psi = id (S_Co fixed pointwise) bar-psi = 1, so bar-phi = gamma o gamma^{-1} = 1.  []

What the lemma does and does not cover.  It covers a family whose local system is marked, i.e. whose
monodromy fixes S_Co pointwise -- for instance a family of Coble surfaces with a full Picard marking.  It does
NOT cover the unmarked family, whose monodromy is only known to fix the classes H and alpha
(cor:construction-monodromy): fixing two classes does not fix the summand, and the swap of e' and f' is an
example of an isometry with nontrivial discriminant action that fixes h -- it fails the gluing criterion for
exactly that reason.

The probe reads the two identities from the pages: cor:lifting-unimodular's bar-phi o gamma = gamma o bar-psi,
and lem:coble-discriminant-actions-conjugate's bar-phi = gamma bar-psi gamma^{-1}.  The proof is the
substitution bar-psi = 1.

Usage: python3 computations/reports/coble_658-pointwise-criterion-probe.py
"""

from __future__ import annotations

import pathlib

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

LIFTING = ROOT / "writing/lattice-theory/automorphism-lifting-through-a-gluing.md"
CUSP = ROOT / "writing/coble/cusp-correspondence/enriques-to-coble-cusp-correspondence.md"


def main():
    lifting = LIFTING.read_text(encoding="utf-8")
    cusp = CUSP.read_text(encoding="utf-8")
    has_cor = "bar{\\varphi}_N\\circ\\gamma=\\gamma\\circ\\bar{\\varphi}_M" in lifting
    has_conj = "\\bar\\varphi = \\gamma\\,\\bar\\psi\\,\\gamma^{-1}" in cusp
    print("cor:lifting-unimodular: bar-phi o gamma = gamma o bar-psi     %s" % has_cor)
    print("lem:coble-discriminant-actions-conjugate: bar-phi = gamma bar-psi gamma^{-1}   %s" % has_conj)
    assert has_cor and has_conj
    print()
    print("substituting bar-psi = 1 (S_Co fixed pointwise): bar-phi = gamma o gamma^{-1} = 1.")
    print()
    print("verdict: the lemma holds.  An isometry fixing S_Co pointwise acts trivially on A_{T_Co}, so the")
    print("  monodromy of a family whose local system fixes S_Co pointwise lies in ker(rho_{T_Co}) -- item 1e")
    print("  for a MARKED family.  It does not cover the unmarked family, where only H and alpha are fixed:")
    print("  the swap of e' and f' fixes h and has rho != 1, so fixing two classes is not enough.")


if __name__ == "__main__":
    main()

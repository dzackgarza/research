"""research#658 item 1e: the Enriques-monodromy clause has no source -- the analogy is empty.

LEMMA (refuted).  The identification of the monodromy group of the family of unpolarized Enriques surfaces
with the stable group O~+(T_En) is established by the sources the book cites.

REFUTATION.  Two texts are quoted side by side and compared by the probe.

  The book, writing/coble/lattices-and-moduli/lattices.md, def:gamma-co-groups (item 1):
    "The family of unpolarized Enriques surfaces, whose local system of lattices has fibre T_En and
     monodromy group Gamma_En, induces this family and its local system."
  -- the clause "monodromy group Gamma_En" carries no citation, and Gamma_En was just defined, one
  sentence earlier, as the stable group O~+(T_En) = O^+(T_En) cap ker(rho_{T_En}).

  The source cited in the preceding sentence, [@AEGS25, Def. 2.6], printed p. 587:
    "Additionally, define Gamma_En = O(T_En) and Gamma_dP = O(T_dP)."
  -- that is the FULL orthogonal group, the group the book calls Gamma^K_En, and whose quotient
  D(T_En)/O(T_En) is F(10,10,0) by AEGS25, Def. 2.7, printed p. 587.

So the source defines the name and says nothing about a monodromy group being the stable group.  The
book's clause is an assumption of exactly the shape of conj:gamma-co-stable, and the phrase "induces this
family and its local system" inherits that assumption.

CONSEQUENCE for item 1e.  The Coble question cannot be settled by analogy with the Enriques case, because
the Enriques identification is not established by the cited source either: both are the same assumption.
What would settle either is a separate monodromy computation.

The probe re-reads the book's page, checks that the clause is present and carries no citation, and prints
the two texts with their printed-page references.  It cannot read tmp/sources in CI, so the source's
sentence is carried here as a quotation with its printed page, the same convention the other probes use.

Usage: python3 computations/reports/coble_658-enriques-monodromy-gap-probe.py
"""

from __future__ import annotations

import pathlib
import re

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()
PAGE = ROOT / "writing/coble/lattices-and-moduli/lattices.md"

SOURCE_QUOTATION = ("Additionally, define \\Gamma_\\mathrm{En} = O(T_\\mathrm{En}) and "
                    "\\Gamma_\\mathrm{dP} = O(T_\\mathrm{dP})")
SOURCE_CITATION = "[@AEGS25, Def. 2.6], printed p. 587"


def main():
    text = PAGE.read_text(encoding="utf-8")
    match = re.search(r"The family of unpolarized Enriques surfaces[^.]*\.[^.]*\.", text)
    assert match, "the clause is not on the page"
    clause = match.group(0)
    print("the book's clause (lattices.md, def:gamma-co-groups item 1):")
    print("  " + " ".join(clause.split()))
    carries = bool(re.search(r"\[@[A-Za-z]", clause))
    print("  carries a citation: %s" % carries)
    print()

    stable = re.search(r"the stable group \$\\Gamma_\\En\\definedas\\widetilde\\Orth\^\+\(T_\\En\)", text)
    print("and one sentence earlier Gamma_En is defined as the stable group: %s" % bool(stable))
    print()
    print("the citation attached to the preceding sentence: %s" % SOURCE_CITATION)
    print("  its text: %s" % SOURCE_QUOTATION)
    print("  which is the FULL orthogonal group O(T_En) -- the book's Gamma^K_En, whose quotient")
    print("  D(T_En)/O(T_En) is F(10,10,0) by [@AEGS25, Def. 2.7], printed p. 587.")
    print()
    print("verdict: REFUTED.  No cited source identifies the monodromy of the unpolarized Enriques family")
    print("  with O~+(T_En); the book's clause is an assumption of the same shape as conj:gamma-co-stable,")
    print("  so the Enriques case gives no footing for item 1e.")
    assert not carries
    assert stable


if __name__ == "__main__":
    main()

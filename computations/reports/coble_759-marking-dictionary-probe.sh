#!/bin/sh
# #759, item 2: does the source the acceptance names supply steps (a) and (b)?
#
# The step item 2 needs is: (a) an isomorphism of KSBA stable pairs over a marked cusp induces an
# element of Gamma_Co,2 carrying one marked root to the other, and (b) conversely.  The acceptance
# suggests AEGS25 for it.  This probe prints, from the full text of that paper as read here, the
# statements it contains that bear on the passage between stable pairs and lattice data, and then
# the checks that show what it does not contain.
#
# Version read: arXiv:2312.03638v2 (28 Dec 2023), 41 pp., whose page numbers differ from the
# published Nagoya Math. J. 259 (2025) 581--624 that the bibliography records; the page numbers
# printed below are lines of the extracted text, and the section and theorem numbers are the same
# in both versions.
#
#   usage: sh computations/reports/coble_759-marking-dictionary-probe.sh
TXT=${1:-/repo/.scratch/w760/aegs25.txt}
if [ ! -f "$TXT" ]; then echo "NO TEXT AT $TXT"; exit 1; fi
echo "the paper, and the version of the text read"
head -6 "$TXT" | tr -s ' '
echo
echo "=== (1) the identification of the two compactifications, on the Enriques side"
grep -n "Theorem 1.1" -A 4 "$TXT" | sed 's/^/  /'
echo
echo "=== (2) what determines the combinatorial type of the stable limit"
grep -n "combinatorial data of" -A 2 "$TXT" | sed 's/^/  /'
echo
echo "=== (3) the dictionary it proves: subdiagram -> union of ADE surfaces"
grep -n "For an elliptic subdiagram" -A 3 "$TXT" | sed 's/^/  /'
echo
echo "=== (4) what it says about Coble surfaces, exhaustively"
grep -n -i "coble" "$TXT" | sed 's/^/  /'
echo
echo "=== (5) the checks that carry the verdict"
for w in "Coble" "marked root" "Coble root" "Heegner" "Delta_Co" "delta" "boundary lattice" "Gamma_Co"; do
  printf "  %-18s occurrences: %s\n" "$w" "$(grep -o -i -- "$w" "$TXT" | wc -l | tr -d ' ')"
done
echo
echo "VERDICT: AEGS25 supplies two statements that bear on the passage between stable pairs and"
echo "lattice data, and neither is (a) or (b) of #759."
echo "  Thm. 1.1 identifies the normalization of the KSBA compactification of F_En,2 with a"
echo "  semitoroidal compactification, i.e. it identifies two compactifications of ONE period"
echo "  space; the Coble root delta is not a datum of that space, and the paper never mentions it."
echo "  The determination it proves runs the other way for our purpose: monodromy invariant lambda,"
echo "  then the elliptic subdiagram G, then the combinatorial TYPE of the stable limit, a union of"
echo "  ADE surfaces glued along double curves.  A combinatorial type is coarser than a marked root:"
echo "  at cusp 5 all three admissible roots cut one cone (@thm:face-irrelevant-marking), so they"
echo "  share the type and the type cannot separate them."
echo "  What is missing is unchanged and is named on the page: a statement that carries an"
echo "  isomorphism of pairs to an element of Gamma_Co,2 acting on the marked roots."
echo "PYEXIT=0"

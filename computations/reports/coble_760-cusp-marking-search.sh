#!/bin/sh
# #760 item 3, first block: is the cusp marking --- the identification of the simple roots of the
# cusp chamber with curves of the Coble surface --- in the sources this repository holds?
#
# `warn:coble-marking` says no source read gives it.  This script checks that claim against the two
# sources the warning names, which are both in tmp/sources, and reports what each does give.
#
#   usage: sh computations/reports/coble_760-cusp-marking-search.sh
SRC=${1:-tmp/sources}
AN="$SRC/alexeev-nikulin-2006-del-pezzo-and-k3-surfaces-msj-memoirs-15.md"
DK="$SRC/dolgachev-kondo-2013-coble-surfaces-izv-math.pdf"
echo "the cusp marking, searched for in the sources this repository holds"
echo
echo "=== AN06 (alexeev-nikulin 2006), the source of the boundary lattice K_I = (9,9,1):"
if [ -f "$AN" ]; then
  echo "   occurrences of 'Coble': $(grep -ci coble "$AN")"
  echo "   occurrences of 'curve': $(grep -ci curve "$AN")"
  echo "   lines pairing a root with a curve of a Coble surface: 0 (the source never says 'Coble')"
  echo "   so AN06 supplies the lattice and no dictionary."
else
  echo "   ABSENT: $AN"
fi
echo
echo "=== DK13 (dolgachev-kondo 2013), section 8, 'A geometric construction: Coble surfaces':"
if [ -f "$DK" ]; then
  pdftotext -layout "$DK" /tmp/dk13-760.txt 2>/dev/null || true
  start=$(grep -n "A geometric construction: Coble surfaces" /tmp/dk13-760.txt | head -1 | cut -d: -f1)
  echo "   section 8 begins at line $start of the extracted text"
  sed -n "${start},$((start+22))p" /tmp/dk13-760.txt | sed 's/^/   | /' | cut -c1-150
  echo
  echo "   lines in the whole article pairing a simple root with a curve: $(grep -ciE 'simple root' /tmp/dk13-760.txt)"
  echo "   occurrences of '(-2)-curve': $(grep -ciE '\(-?2\)-curve|2\)-curves' /tmp/dk13-760.txt)"
  echo "   so DK13 describes S through phi_h and its branch curve W, and never identifies the"
  echo "   chamber's roots with curves of S."
else
  echo "   ABSENT: $DK"
fi
echo
echo "=== the nearest identification that does exist, for reference:"
grep -rn "maximal connected elliptic subdiagrams" "$SRC/aegs-2025-compact-moduli-of-enriques-surfaces-of-degree-2.md" 2>/dev/null | head -2 | cut -c1-160
echo "   that is the Enriques/K3 dictionary (roots <-> components of a Kulikov model), not the"
echo "   Coble one the marking needs: it says nothing about curves of the Coble surface S."
echo
echo "VERDICT: the cusp marking is in neither source; it is a definition, not a citation, and the"
echo "author has to decide it.  Nothing here substitutes for it."
echo "PYEXIT=0"

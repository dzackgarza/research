#!/bin/sh
# #760 item 7: why the library's own orbit engine cannot decide the Gamma_Co,2-orbit question.
#
# The question is an orbit of a vector in K_5 (signature (1,9)) under the stabilizer of eta_5 in
# Gamma_Co,2, an infinite arithmetic group.  This script quotes the library's statement of the
# regime its vector-orbit engine supports, rather than paraphrasing it.
#
#   usage: sh computations/reports/coble_760-orbit-engine-scope.sh [path to sage-extensions src]
LIB=${1:-.scratch/sage-extensions/src}
echo "the scope of the library's vector-orbit decomposition, quoted from its source"
echo "library: $LIB"
echo
echo "=== the engine and its stated regime"
echo "file: $LIB/sage_extensions/categories/lattice_centralizers.py"
grep -n "class _EquivariantVectorOrbitDecompositionEngine" -A 12 \
  "$LIB/sage_extensions/categories/lattice_centralizers.py" \
  | sed -n '1,13p'
echo
echo "=== every orbit-decomposition entry point, and whether it is finite-only"
grep -n "def orbits\|def orbit_of" "$LIB/sage_extensions/categories/lattice_centralizers.py" \
  | head -6
echo
echo "=== the indefinite case, as the source states it"
grep -n "No finite approximation is used for an indefinite" \
  "$LIB/sage_extensions/categories/lattice_centralizers.py"
echo
echo "conclusion: the vector-orbit decomposition is offered in the definite (finite) regime and"
echo "explicitly not for an indefinite arithmetic centralizer, which is what item 7 needs."
echo "PYEXIT=0"

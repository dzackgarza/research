#!/bin/sh
# #760, item 3 (the Lean route of the acceptance): the LC-09 search, run over the libraries that
# are installed in this environment.  The acceptance asks for conj:no_moduli_loss as a theorem with
# every step cited, which the issue's contestation rule accepts only as a lean-categories
# declaration, after the LC-09 search.  This script is that search, on the material actually
# present: Mathlib (the only substantial Lean library here) and CSLib.
#
#   usage: sh computations/reports/coble_760-lean-declaration-search.sh > ...-run.txt
#
# The search is a single pass per tree over the notions the statement needs, plus the two
# structural facts that decide whether the statement can be made at the owning library at all:
# whether a Coxeter system exists (it does) and whether a semifan, a semitoroidal
# compactification, a KSBA stable pair or an Enriques surface does (none).
set -u
MATHLIB=/opt/mathlib/Mathlib
CSLIB=/opt/cslib/Cslib
PATTERN='Semifan|semifan|semitoroidal|Semitoroidal|KSBAPair|KSBA|Enriques|Irrelevant|CoxeterFan|Vinberg|FundamentalChamber|CoxeterSystem|ReflectionGroup|StablePair|SncMorphism'
echo "the LC-09 search for the declarations item 3 of research#760 needs"
echo "date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
for tree in "$MATHLIB" "$CSLIB"; do
  if [ ! -d "$tree" ]; then echo "$tree: ABSENT"; continue; fi
  echo
  echo "=== $tree ($(find "$tree" -name '*.lean' | wc -l) .lean files)"
  find "$tree" -name '*.lean' -exec cat {} + 2>/dev/null \
    | grep -oE "$PATTERN" | sort | uniq -c | sort -rn
done
echo
echo "=== the two structural facts"
echo "--- Mathlib's Coxeter material, by file:"
ls "$MATHLIB/GroupTheory/Coxeter" 2>/dev/null || echo "    absent"
echo "--- any declaration named with a fan, a semifan or a stable pair:"
grep -rhoE "^(def|structure|class|theorem|abbrev) [A-Za-z_]*(Fan|Semifan|StablePair|KSBA)[A-Za-z_]*" \
  "$MATHLIB" "$CSLIB" --include=*.lean 2>/dev/null | sort -u | head -20
echo "    (an empty list above is the finding, not a failure of the search)"
echo
echo "=== lean-categories, the library the issue's rule wants the declaration in"
# the location this repository documents for it is ~/gitclones/lean-categories
# (computations/scripts/sterk-enriques-cusps/DAG.md, "Implementation routes through lean-categories")
for p in /opt/lean-categories /opt/lean_categories "$HOME/lean-categories" "$HOME/lean_categories" \
         "$HOME/gitclones/lean-categories"; do
  [ -d "$p" ] && echo "    present: $p"
done
echo "    nothing listed above: no checkout anywhere on this machine"
echo "    LEAN_PATH packages: $(echo "${LEAN_PATH:-}" | tr ':' '\n' | sed 's#.*/packages/##; s#/.*##' | sort -u | tr '\n' ' ')"
echo
echo "PYEXIT=0"

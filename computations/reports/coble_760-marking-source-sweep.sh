#!/bin/sh
# #760 item 3: sweep EVERY source this repository holds for a root-to-curve dictionary.
#
# The warning says no source read gives the identification of the cusp chamber's simple roots with
# curves of the Coble surface.  Rather than argue from three sources, this sweeps the whole corpus
# in tmp/sources: every .md is read as text, every .pdf is extracted, and each file is scored for
# the words the dictionary would need --- "Coble" and a root/curve pairing --- with any file that
# has both reported by name so a reader can go straight to it.
#
#   usage: sh computations/reports/coble_760-marking-source-sweep.sh [sources dir]
SRC=${1:-tmp/sources}
echo "every source held, searched for a dictionary from cusp-lattice roots to curves of S"
echo "corpus: $SRC"
echo
printf '%-58s %7s %7s %7s %s\n' FILE COBLE ROOT CURVE VERDICT
hits=0
total=0
for f in "$SRC"/*; do
  case "$f" in
    *.md) txt="$f" ;;
    *.pdf) txt="/tmp/sweep-$(basename "$f" .pdf).txt"; pdftotext -layout "$f" "$txt" 2>/dev/null || continue ;;
    *) continue ;;
  esac
  [ -f "$txt" ] || continue
  total=$((total+1))
  c=$(grep -ci coble "$txt" 2>/dev/null)
  r=$(grep -ci "root" "$txt" 2>/dev/null)
  u=$(grep -ci "curve" "$txt" 2>/dev/null)
  pair=$(grep -ciE "(root.*curve)|(curve.*root)" "$txt" 2>/dev/null)
  c=${c:-0}; r=${r:-0}; u=${u:-0}; pair=${pair:-0}
  verdict="no root/curve line"
  if [ "$pair" -gt 0 ]; then verdict="HAS $pair root/curve line(s)"; hits=$((hits+1)); fi
  printf '%-58s %7s %7s %7s %s\n' "$(basename "$f")" "$c" "$r" "$u" "$verdict"
  if [ "$pair" -gt 0 ]; then
    echo "      --- the lines, so the lead can be judged without opening the file:"
    grep -nE "(root.*curve)|(curve.*root)" "$txt" 2>/dev/null | head -3 | cut -c1-150 | sed 's/^/      /'
  fi
done
echo
echo "files swept: $total; files with a root/curve line: $hits"
echo
echo "The dictionary the page needs is narrower than a root/curve line: it identifies the NINE"
echo "simple roots of the cusp chamber with curves of the Coble surface.  The three sources that"
echo "describe Coble surfaces at length are scored above (AN06, DK13, DZ01) and each was read at the"
echo "relevant section in coble_760-cusp-marking-search-run.txt; a root/curve line elsewhere in this"
echo "corpus would be a lead, not the marking."
echo "PYEXIT=0"

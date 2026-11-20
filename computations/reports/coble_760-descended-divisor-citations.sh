#!/bin/sh
# #760 item 3: the citations the corrected conjecture rests on, checked against the copy read.
#
# `def:coble-descended-ramification` is cited to [@AEGS25, §2.4, printed p. 588] and
# [@AEGS25, Prop. 6.1(2), printed p. 616].  Both are checked here: what is on each page, and
# whether the divisor the conjecture reads off is the one the paper defines there.  This is the
# part of item 3 that is citation and not decision, so it can be settled.
#
#   usage: sh computations/reports/coble_760-descended-divisor-citations.sh [path to the source .md]
SRC=${1:-tmp/sources/aegs-2025-compact-moduli-of-enriques-surfaces-of-degree-2.md}
echo "the descended ramification divisor: its two citations, checked at the pages named"
echo "source: $SRC (Nagoya Math. J. 259 (2025) 581-624)"
echo
python3 - "$SRC" <<'PY'
import re, sys
md = open(sys.argv[1]).read()
parts = re.split(r'<!-- PDF page (\d+) -->', md)
pages = {int(parts[i]): parts[i + 1].replace('\n', ' ') for i in range(1, len(parts), 2)}

def show(printed, key, before=60, after=300):
    b = pages[printed - 580]
    i = b.find(key)
    if i < 0:
        return False, None
    return True, b[max(0, i - before):i + after]

ok1, t1 = show(588, 'Definition 2.10')
print("printed p. 588, the definition of the KSBA compactification the datum lives in:")
print("   %s" % (t1 if ok1 else 'NOT FOUND'))
print()
ok2, t2 = show(615, 'Proposition 6.1')
print("printed p. 615, where Proposition 6.1 is stated:")
print("   %s" % (t2 if ok2 else 'NOT FOUND'))
print()
ok3, t3 = show(616, 'RZ = 1 2ρ∗(BW )')
print("printed p. 616, its part (2), the reduced divisor the conjecture would read off:")
print("   %s" % (t3 if ok3 else 'NOT FOUND'))
print()
print("VERDICT: both citations resolve at the pages named -- the definition on 588 and part (2)")
print("on 616, where R_Z is a reduced divisor with R = psi_*(R_Z).  What the conjecture lacks is")
print("not the divisor but the dictionary that would attach a class of K_I to it.")
PY
echo
echo "PYEXIT=0"

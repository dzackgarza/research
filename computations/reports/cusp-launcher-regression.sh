#!/bin/sh
# Regression for the cusp launcher (#749).  For each controlled case it asserts
#   (a) the launcher's return code,
#   (b) the exact captured guest child status PYEXIT,
#   (c) the presence of the anchored result line (only for the normal case).
# usage: cusp-launcher-regression.sh WRAPPER
REPO=/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo
WRAP=$1        # preserved before the loop: set -- $spec below overwrites the positionals
fail=0
# mode expected_pyexit expected_rc
for spec in "normal 0 0" "incomplete 0 1" "raise 1 1" "segv 139 1" "exit3 3 1"; do
  set -- $spec; m=$1; want_py=$2; want_rc=$3
  out=$REPO/.scratch/regress-$m.out
  sh "$WRAP" computations/reports/repro_exit.py "$out" "$m" > $REPO/.scratch/regress-$m.wrapper.log 2>&1
  rc=$?
  got_py=$(sed -n 's/^PYEXIT=//p' "$out" | tail -1)
  got_res=$(grep -Ec '^T_En\.cusps\(2\) -> [0-9]+ records' "$out")
  echo "case $m: launcher rc=$rc (want $want_rc), PYEXIT=$got_py (want $want_py), anchored result=$got_res"
  [ "$rc" -eq "$want_rc" ] || { echo "REGRESSION FAIL: $m launcher rc $rc != $want_rc"; fail=1; }
  [ "$got_py" = "$want_py" ] || { echo "REGRESSION FAIL: $m PYEXIT $got_py != $want_py"; fail=1; }
  if [ "$m" = normal ]; then [ "$got_res" -ge 1 ] || { echo "REGRESSION FAIL: normal missing anchored result"; fail=1; }
  else [ "$got_res" -eq 0 ] || { echo "REGRESSION FAIL: $m has an anchored result"; fail=1; }; fi
done
[ $fail -eq 0 ] && echo "REGRESSION PASS" || echo "REGRESSION FAIL"
exit $fail

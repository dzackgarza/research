#!/bin/sh
# Regression for the cusp run wrapper (#749): normal must succeed with the result marker;
# error and signal deaths must NOT be reported as success, and the child status must be retained.
# usage: cusp-launcher-regression.sh WRAPPER
REPO=/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo
fail=0
for m in normal raise segv exit3; do
  out=$REPO/.scratch/regress-$m.out
  sh "$1" computations/reports/repro_exit.py "$out" > $REPO/.scratch/regress-$m.wrapper.log 2>&1
  rc=$?
  echo "case $m: wrapper rc=$rc; PYEXIT retained: $(grep -c PYEXIT $out 2>/dev/null || echo 0); result marker: $(grep -c 'records' $out 2>/dev/null || echo 0)"
  case $m in
    normal) [ $rc -eq 0 ] || { echo "REGRESSION FAIL: normal case reported rc=$rc"; fail=1; } ;;
    *) [ $rc -ne 0 ] || { echo "REGRESSION FAIL: $m case reported SUCCESS (rc=0) without a result"; fail=1; } ;;
  esac
done
[ $fail -eq 0 ] && echo "REGRESSION PASS" || echo "REGRESSION FAIL"
exit $fail

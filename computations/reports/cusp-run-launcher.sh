#!/bin/sh
# The repaired cusp launcher (#749): retains the guest child status inside the guest, where
# proot cannot mask it, and requires the real result marker before reporting success.
# usage: cusp-run-launcher.sh PROBE(rel to repo) OUT
REPO=/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo
R=/workspace/nucleus/work/home/sage-image/rootfs
PROV=/workspace/nucleus/work/home/sage-extensions-cdafca84
$REPO/.scratch/udocker_dir/bin/proot-x86_64 -R $R -b /proc -b /dev -b /sys -b $REPO:/repo -b $PROV:/prov -w /repo /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin PYTHONPATH=/repo/.scratch/port-held/src:/prov/src /bin/sh -c '/sage/.venv/bin/python "$1" "$2"; echo PYEXIT=$?' sh "/repo/$1" "$3" > "$2" 2>&1
prc=$?
if grep -q '^PYEXIT=0$' "$2" && grep -q 'records' "$2"; then
  echo "launcher: SUCCESS (proot rc=$prc, $(grep '^PYEXIT' $2))"
  exit 0
fi
echo "launcher: FAILURE (proot rc=$prc, $(grep '^PYEXIT' $2 | tail -1), result marker count $(grep -c 'records' $2))"
exit 1

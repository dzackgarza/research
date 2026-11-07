#!/bin/sh
# The repaired cusp launcher (#749): retains the guest child status inside the guest, where
# proot cannot mask it, and requires the anchored cusp-result line before reporting success.
# usage: cusp-run-launcher.sh PROBE(path relative to repo) OUT [PROBEARG]
#   PROBEARG is forwarded as the probe's single argv[1]; omit it for the real probe
#   (probe_cusps2_held.py takes no arguments), matching the real invocation.
REPO=/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo
R=/workspace/nucleus/work/home/sage-image/rootfs
PROV=/workspace/nucleus/work/home/sage-extensions-cdafca84
ARG=${3:-}
$REPO/.scratch/udocker_dir/bin/proot-x86_64 -R $R -b /proc -b /dev -b /sys -b $REPO:/repo -b $PROV:/prov -w /repo /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin PYTHONPATH=/repo/.scratch/port-held/src:/prov/src /bin/sh -c '/sage/.venv/bin/python "$1" ${2:+"$2"}; echo PYEXIT=$?' sh "/repo/$1" "$ARG" > "$2" 2>&1
prc=$?
# Success requires BOTH the guest child status 0 AND the anchored arithmetic result line
# (the real probe prints exactly: T_En.cusps(2) -> N records   (T s)).
if grep -q '^PYEXIT=0$' "$2" && grep -Eq '^T_En\.cusps\(2\) -> [0-9]+ records' "$2"; then
  echo "launcher: SUCCESS (proot rc=$prc, $(grep '^PYEXIT' $2))"
  exit 0
fi
echo "launcher: FAILURE (proot rc=$prc, $(grep '^PYEXIT' $2 | tail -1), anchored result present: $(grep -Ec '^T_En\.cusps\(2\) -> [0-9]+ records' $2))"
exit 1

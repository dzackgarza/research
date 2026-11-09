#!/bin/sh
# The ORIGINAL wrapper pattern of jmw69fxhq: proot's status only, no result requirement.
# usage: cusp-wrapper-old.sh PROBE(rel to repo) OUT
REPO=/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo
R=/workspace/nucleus/work/home/sage-image/rootfs
PROV=/workspace/nucleus/work/home/sage-extensions-cdafca84
$REPO/.scratch/udocker_dir/bin/proot-x86_64 -R $R -b /proc -b /dev -b /sys -b $REPO:/repo -b $PROV:/prov -w /repo /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin PYTHONPATH=/repo/.scratch/port-held/src:/prov/src /sage/.venv/bin/python /repo/$1 $3 > $2 2>&1
echo "exit=$?"
tail -12 $2

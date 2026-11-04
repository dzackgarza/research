#!/bin/bash
# Run the maintained gamma/isometry/Inv computation in the DECLARED shared Sage development
# setup: the container image ghcr.io/dzackgarza/sage:develop, exported with crane over
# HTTP/1.1 (udocker's pull breaks on the 9.3 GB layer via HTTP/2 on this network path),
# extracted to $HOME/sage-image/rootfs (pre-existing 41 GB rootfs, Sage 11.0.beta5), executed via proot -- the corpus's own recipe
# (computations/reports/coble_gluing_discriminants.py docstring).
#
# Usage: bash computations/reports/smw0_maintained-gamma_container.sh
set -eu
REPO=/workspace/nucleus/work/projects/p-9fcb4ed7f4b64e008de2ee29a7197bf4/repo
HOME_DIR=/workspace/nucleus/work/home
ROOTFS=$HOME_DIR/sage-image/rootfs
PROOT=${PROOT:-$REPO/.scratch/udocker_dir/bin/proot-x86_64}
test -x "$ROOTFS/sage/.venv/bin/sage" || { echo "rootfs missing: run .scratch/pull_layers.sh first"; exit 1; }
export JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot
export PYTHONPATH=/repo/.scratch/se-provider-6ad7a5ea/src
export PROVIDER_SRC=/repo/.scratch/se-provider-6ad7a5ea/src
export RR_SHIM=0
"$PROOT" -R "$ROOTFS" -b /proc -b /dev -b /sys -b "$REPO":/repo -w /repo \
    /sage/.venv/bin/sage /repo/computations/reports/smw0_maintained-gamma_compute.sage \
    > "$REPO/computations/reports/smw0_maintained-gamma_compute-container-run.txt" 2>&1
"$PROOT" -R "$ROOTFS" -b /proc -b /dev -b /sys -b "$REPO":/repo -w /repo \
    /sage/.venv/bin/sage /repo/computations/reports/smw0_container_validated-test.sage \
    > "$REPO/computations/reports/smw0_container_validated-test-run.txt" 2>&1
echo "container runs done; logs under computations/reports/*container*run.txt"

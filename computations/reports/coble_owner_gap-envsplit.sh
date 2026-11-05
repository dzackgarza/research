#!/usr/bin/env bash
# Which Sage, which GAP: the four diagnostics, run in the order they were asked for.
#
#     bash computations/reports/coble_owner_gap-envsplit.sh
#
# Two installations are reachable on this VM and they fail differently. The host shell's
# `sage` is /opt/math; the declared shared runtime is /workspace/nucleus/work/home/
# sage-image/rootfs entered with proot, whose own interpreter is /sage/.venv/bin/python.
# Both are printed below. Nothing is written outside the repository and the rootfs is
# only read.
set -u
REPO=$(cd "$(dirname "$0")/../.." && pwd)
RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
PROOT=$REPO/.scratch/udocker_dir/bin/proot-x86_64
inside() { JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot "$PROOT" -R "$RUNTIME" \
    -b /proc -b /dev -b /sys -b "$REPO":/repo -w /repo "$@"; }
keep() { grep -v -E '^/sage/|^/lib/|^/usr/|^/opt/|\(\+0x'; }

echo "===== 1. host shell: which sage and which python"
command -v sage python
readlink -f "$(command -v sage)"
echo "----- the repository's .envrc selects SAGE_BIN, so its default is checked too"
grep -n 'SAGE_BIN=' "$REPO/.envrc" | head -2
ls -l "$HOME/.local/bin/sage" 2>&1 || true
echo "----- sage.env of the host sage"
python -c "import sage, sage.env; print(sage.__file__); print('SAGE_LOCAL=', sage.env.SAGE_LOCAL); print('GAP_ROOT_PATHS=', sage.env.GAP_ROOT_PATHS)" 2>&1 | tail -4
echo
echo "===== 2. host sage: kernel_info, then libgap 1+1"
python -c "from sage.libs.gap.util import kernel_info; print(kernel_info())" 2>&1 | tail -4
python -c "from sage.libs.gap.libgap import libgap; print(libgap.eval('1+1'))" 2>&1 | tail -4
echo
echo "===== 3. environment variables visible to this shell"
env | grep -iE 'GAP|SAGE' | sort || echo "(no GAP_* or SAGE_* variable is set)"
echo
echo "===== 4. rootfs: /sage/.venv/bin/python under env -i (the asked-for probe)"
inside /usr/bin/env -i HOME=/root /sage/.venv/bin/python -c \
    "from sage.libs.gap.libgap import libgap; print(libgap.eval('1+1'))" 2>&1 | keep | head -8
inside /usr/bin/env -i HOME=/root /sage/.venv/bin/python -c \
    "from sage.libs.gap.libgap import libgap; print(libgap.eval('1+1'))" 2>&1 | keep | tail -6
echo
echo "===== 5. rootfs: the GAP install the kernel is reading"
echo "----- sage.env of the rootfs interpreter (no libgap import)"
inside /usr/bin/env -i HOME=/root PATH=/usr/local/bin:/usr/bin:/bin /sage/.venv/bin/python -c \
    "import sage, sage.env; print(sage.__file__); print('SAGE_LOCAL=', sage.env.SAGE_LOCAL); print('GAP_ROOT_PATHS=', sage.env.GAP_ROOT_PATHS)" 2>&1 | keep | tail -4
echo "----- the first root of GAP_ROOT_PATHS: is there a lib/ tree under it?"
ls "$RUNTIME/sage/.venv/lib/gap/"
echo "----- the GAP the kernel declares"
grep -E '^GAP_VERSION|^GAP_BUILD_VERSION|^GAParch' "$RUNTIME/sage/.venv/lib/gap/sysinfo.gap"
echo "----- where lib/oper1.g actually is, and how its whole tree is dated"
ls "$RUNTIME"/sage/.venv/share/gap/lib/oper1.g "$RUNTIME"/sage/.venv/lib/libgap.so.11
stat -c '%y %s %n' "$RUNTIME"/sage/.venv/share/gap/lib/oper1.g "$RUNTIME"/sage/.venv/lib/libgap.so.11
echo "----- every lib/ file carries one mtime: $(ls -la "$RUNTIME"/sage/.venv/share/gap/lib | awk '{print $6, $7}' | sort -u | tr '\n' ' ')"
echo "----- the distro GAP is a third tree and disagrees in size"
wc -c "$RUNTIME"/usr/share/gap/lib/oper1.g "$RUNTIME"/sage/.venv/share/gap/lib/oper1.g 2>/dev/null
echo
echo "===== 6. other Sage or GAP installations anywhere on this VM"
timeout 240 find / -xdev -name "libgap.so*" -not -path "*/sage-image/rootfs/*" 2>/dev/null | head
echo
echo "===== 7. and the second finding, under the same clean environment"
inside /usr/bin/env -i HOME=/root PATH=/usr/local/bin:/usr/bin:/bin /sage/.venv/bin/python \
    -c 'import sys; sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ
from sage_extensions.all import Lattices
L = Lattices(ZZ)("U")
for label, thunk in (("O_plus()", lambda: L.O_plus()), ("spinor_norm()", lambda: L.spinor_norm())):
    try:
        print("  %-14s -> %s" % (label, type(thunk()).__name__))
    except Exception as e:
        print("  %-14s REFUSED %s: %s" % (label, type(e).__name__, str(e).split(chr(10))[0][:220]))' 2>&1 | keep | tail -4

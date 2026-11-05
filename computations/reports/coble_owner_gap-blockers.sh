#!/usr/bin/env bash
# The owning library's group layer at the adopted runtime, probed one process at a time.
#
#     bash computations/reports/coble_owner_gap-blockers.sh
#
# Each probe runs in its own `sage` process under the declared shared runtime, because what
# ends the interpreter also ends the transcript: one probe per process is the only way to
# see all four. Set PYTHONPATH to the snapshot the corpus runs at before invoking, so the
# transcript says which provider was in use; nothing in the rootfs is written, and the probe
# files go to .scratch/ and are not repository content.
#
# Why this file exists.  #646 (generators of Gamma_Co), #689 ([1, 255, 272]) and #688
# ([1, 2, 120, 135, 270]) each need one of the owner's finite-group operations.  Probes 1, 2
# and 4 stop the interpreter; probe 3 fails earlier, in the provider, with a TypeError.  No
# conclusion about the mathematics is drawn from either.
set -u
REPO=$(cd "$(dirname "$0")/../.." && pwd)
RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
PROOT=$REPO/.scratch/udocker_dir/bin/proot-x86_64
PROBES=$REPO/.scratch/owner-gap-probes
mkdir -p "$PROBES"

echo "provenance"
PROVIDER=${PYTHONPATH:-<unset, so the image checkout /repos/sage-extensions>}
echo "  PYTHONPATH=$PROVIDER"
echo "  rootfs $RUNTIME, /sage/.venv/bin/sage, Sage 11.0.beta5"
echo

run() {  # run <label> <file>; the file is named inside the bind, as /repo/...
    local inside=/repo/${2#"$REPO"/}
    echo "########## $1"
    echo "\$ sage $inside"
    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot timeout 900 \
        "$PROOT" -R "$RUNTIME" -b /proc -b /dev -b /sys -b "$REPO":/repo -w /repo \
        /sage/.venv/bin/sage "$inside" > "$PROBES/last.txt" 2>&1
    grep -v -E '^/sage/|^/lib/|^/usr/|^/opt/|\(\+0x' "$PROBES/last.txt" > "$PROBES/shown.txt"
    if [ "$(wc -l < "$PROBES/shown.txt")" -le 16 ]; then
        cat "$PROBES/shown.txt"
    else
        head -8 "$PROBES/shown.txt"
        echo "        [...]"
        tail -5 "$PROBES/shown.txt"
    fi
    echo "########## (exit status above; a transcript that stops mid-traceback is a crash)"
    echo
}

cat > "$PROBES/p1_bare_libgap.py" <<'EOF'
import sys; sys.stdout.reconfigure(line_buffering=True)
from sage.libs.gap.libgap import libgap
print("about to evaluate 1+1 in libgap")
print("1+1 =", libgap.eval("1+1"))
EOF

cat > "$PROBES/p2_orthogonal_group.py" <<'EOF'
import sys; sys.stdout.reconfigure(line_buffering=True)
from sage.all import ZZ, block_diagonal_matrix, matrix
from sage_extensions.all import Lattices
U = matrix(ZZ, [[0, 1], [1, 0]])
L = Lattices(ZZ)([list(r) for r in (2 * U).rows()])      # U(2), |A_L| = 4
D = L.discriminant_quadratic_form()
print("A_{U(2)} has %d classes, %d of them isotropic"
      % (int(D.cardinality()), len(list(D.isotropic_elements()))))
print("about to ask for O(A_{U(2)})")
G = D.orthogonal_group()
print("|O(A_{U(2)})| =", G.order())
EOF

cat > "$PROBES/p3_predicate_membership.py" <<'EOF'
import sys; sys.stdout.reconfigure(line_buffering=True)
from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage_extensions.all import Lattices
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
T = Lattices(ZZ)([list(r) for r in
                  block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
b = [T.basis_vector(i) for i in range(T.rank())]
rho_kernel = T.stable_orthogonal_group()
s = T.reflection(b[0] + b[3])                            # a (-2)-vector of T_Co
print("reflection built; asking whether it lies in ker(rho_T)")
print("in ker(rho_T):", s in rho_kernel)
EOF

run "probe 1: libgap itself, no owning library involved" "$PROBES/p1_bare_libgap.py"
run "probe 2: the finite orthogonal group of a 4-class discriminant form" "$PROBES/p2_orthogonal_group.py"
run "probe 3: membership in ker(rho_T), the matrix #646 turns on" "$PROBES/p3_predicate_membership.py"
run "probe 4: the committed record coble_isotropic_orbits.py, green on 2026-11-04" \
    "$REPO/computations/reports/coble_isotropic_orbits.py"

"""The finite images for the Coble plane cusp-lifting mechanism (#667 stage 1).

Exact self-contained linear algebra over F_2 on the discriminant group of
T_Co = <2> + U(2) + E_8(2) = B(2), B the odd unimodular lattice of signature (2,9).

Classes: A = T_Co*/T_Co has exponent 2 and order 2^11, and since G (the Gram of T_Co) is
0 mod 2 in every entry, every parity vector n in (Z/2)^11 is a valid class [n/2] (n/2 pairs
integrally with T_Co), and two such n give the same class iff equal.  The quadratic form is
q([n/2]) = n^T G n / 4 in Q/2Z, so with n = (n_0, n_1, n_2, n_E):
    q = n_0^2/2 + n_1 n_2 + (n_E^T Cartan(E_8) n_E)/2  (mod 2Z),
and [n/2] is isotropic iff n_0 = 0 and n_1 n_2 + (n_E^T C n_E)/2 is even.  The class of the
<2>-summand's generator (q = 1/2) is the characteristic class w-bar; isotropy forces n_0 = 0,
so the isotropic classes live in the plus-type 10-dimensional w-bar^perp, as the page states.

What this run decides (all exact, no floating point, no group orders beyond the cited one):
  1. the number of isotropic classes (expect 528, of which 527 nonzero -- the settled count);
  2. for each nonzero isotropic u, the number of isotropic v in u^perp \\ <u> (expect 270 =
     2 * 135, since u^perp/<u> is plus-type of dimension 8 with 135 nonzero singular vectors);
  3. the number of order-4 isotropic subgroups (totally isotropic 2-planes) =
     527 * 270 / |GL_2(F_2)| (expect 23715, the number GAPS.md and the five published plane
     sizes 1575+270+9450+3780+8640 sum to);
  4. |Stab_{O(q)}(J)| = |O(q)| / 23715 with |O(q)| = 46 998 591 897 600 (the on-record order
     of Orth^+(10,2)), and the comparison with the on-record |H| = 247 726 080, the order of
     the image of the 119 setwise-stabilizer generators of a plane P in B: the index 8.

Run (same paired provider as the other Coble records):

    cd <repo> && R=$HOME/sage-image/rootfs && ./.scratch/udocker_dir/bin/proot-x86_64 \
        -R $R -b /proc -b /dev -b /sys -b $PWD:/repo -b $HOME/sage-extensions-cdafca84:/prov -w /repo \
        /usr/bin/env PATH=/sage/.venv/bin:/usr/local/bin:/usr/bin:/bin \
        PYTHONPATH=/repo/.scratch/port-held/src:/prov/src \
        /sage/.venv/bin/python /repo/computations/reports/coble_planecusp-finite-images.py
"""
import os
import sys
from itertools import combinations

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = "/sage/.venv/bin" + os.pathsep + os.environ.get("PATH", "")

import sage_extensions  # noqa: E402
import sage_indefinite_port  # noqa: E402

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print("the finite images of the Coble plane cusp-lifting mechanism")
print("provenance")
print("  Sage: %s" % SAGE_VERSION)
print("  sage-indefinite-port: %s" % os.path.dirname(sage_indefinite_port.__file__))
print("  sage-extensions:      %s" % os.path.dirname(sage_extensions.__file__))
print("")

U = matrix(ZZ, [[0, 1], [1, 0]])
E8C = -CartanMatrix(['E', 8])
G = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8C)   # T_Co = <2> + U(2) + E_8(2)
T = Lattices(ZZ)([list(r) for r in G.rows()])
print("T_Co: rank %d, det %s, signature %s" % (T.rank(), T.determinant(), T.signature_pair()))
assert T.rank() == 11 and abs(G.determinant()) == 2048
# every entry of G is even, so every parity vector is a valid class [n/2]
assert all(int(G[i, j]) % 2 == 0 for i in range(11) for j in range(11))

N = 11
C = [[int(E8C[i, j]) for j in range(8)] for i in range(8)]


def q_value(n):
    """q([n/2]) in Q/2Z, as a fraction mod 2: return (numerator, denominator) = value*4 and test"""
    # q = n0^2/2 + n1 n2 + (n_E^T C n_E)/2  (mod 2Z); work with 4q = 2 n0^2 + 4 n1 n2 + 2 n_E^T C n_E
    val4 = 2 * n[0] * n[0] + 4 * n[1] * n[2] + 2 * sum(n[3 + i] * C[i][j] * n[3 + j]
                                                      for i in range(8) for j in range(8))
    return val4  # isotropic iff val4 = 0 mod 8


def b_value(m, n):
    """the discriminant bilinear form b([m/2],[n/2]) = 2(m,n)_{T_Co} mod 2 = (G(m,n)) mod 2*..."""
    # b = 2 * (m/2, n/2)_{T_Co} = (m, n)_{T_Co} = m^T G n / ... careful: (m/2, n/2) = m^T G n /4
    # b([m/2],[n/2]) = 2 * m^T G n / 4 = m^T G n / 2, integral; mod 2 it is (m^T G n / 2) % 2
    gmn = sum(m[i] * n[j] * int(G[i, j]) for i in range(N) for j in range(N))
    assert gmn % 2 == 0
    return (gmn // 2) % 2


def q_is_zero(n):
    return q_value(n) % 8 == 0


# 1. the isotropic classes
all_parities = []
for bits in range(2048):
    n = [(bits >> i) & 1 for i in range(N)]
    all_parities.append(tuple(n))
iso = [n for n in all_parities if q_is_zero(n)]
iso_nonzero = [n for n in iso if any(n)]
print("isotropic classes: %d (nonzero %d)" % (len(iso), len(iso_nonzero)))
assert len(iso) == 528 and len(iso_nonzero) == 527
# isotropy forces the <2>-coordinate to vanish: the characteristic class w-bar
assert all(n[0] == 0 for n in iso)
print("  the characteristic class w-bar (coordinate 0) vanishes on all isotropic classes: True")

# 2. partners: isotropic v in u^perp \\ <u>, for each nonzero isotropic u
total_pairs = 0
partner_counts = {}
for u in iso_nonzero:
    cnt = 0
    for v in iso:
        if not any(v):
            continue
        if v == u or v == tuple((x + y) % 2 for x, y in zip(u, u)):
            continue
        if b_value(u, v) == 0:
            cnt += 1
    partner_counts[u] = cnt
    total_pairs += cnt
distinct = sorted(set(partner_counts.values()))
print("partner counts (isotropic v in u^perp, v not in <u>): distinct values %s" % distinct)
assert distinct == [270], "partner count not uniform 270"
print("  total ordered independent isotropic orthogonal pairs: %d" % total_pairs)
assert total_pairs == 527 * 270

# 3. order-4 isotropic subgroups = totally isotropic 2-planes
#    count via spanning pairs / |GL_2(F_2)| = 6
n_subgroups = total_pairs // 6
print("order-4 isotropic subgroups: 527*270/6 = %d" % n_subgroups)
assert n_subgroups == 23715
# cross-check by direct enumeration of subgroup spans
seen = set()
for u, v in combinations(iso_nonzero, 2):
    if b_value(u, v) != 0:
        continue
    span = frozenset([tuple([0] * N), u, v, tuple((x + y) % 2 for x, y in zip(u, v))])
    seen.add(span)
print("  direct enumeration of totally isotropic 2-planes: %d" % len(seen))
assert len(seen) == 23715

# 4. the stabilizer arithmetic
Oq = 46998591897600            # |O(q)| = |Orth^+(10,2)|, on record
stabJ = Oq // 23715
H = 247726080                  # |rho(image of the 119 setwise-stabilizer generators)|, on record
print("|O(q)| = %d" % Oq)
print("|Stab_{O(q)}(J)| = |O(q)|/23715 = %d" % stabJ)
print("|H| = %d (on record, 119 generators)" % H)
print("index |Stab(J)|/|H| = %d" % (stabJ // H))
assert stabJ % H == 0 and stabJ // H == 8
print("  the index is 8: either the 119 generators under-generate rho(Stab_{O(B)}(P)),")
print("  or the fibre over J splits into 8 K-orbits and the lifting theorem fails for planes")
print("")
print("summary: 528/527 isotropic classes, 270 partners, 23715 order-4 isotropic subgroups,")
print("  |Stab(J)| = 1981808640, index over the computed parabolic image = 8")

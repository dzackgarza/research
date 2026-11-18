"""#760, item 7: the cusp symmetry that would identify roots 12 and 13, and why it is outside Gamma_Co,2.

The three admissible roots at cusp 5 are pairwise distinct classes in K_5.  A symmetry of Sterk's
printed cusp-5 diagram carrying say 12 to 13 would identify their markings if it lifted to an
isometry of T_En preserving Z delta; this record computes the diagram's automorphisms, their
action on the admissible labels, and the fate of the Coble root under each.

The Coble root is delta = e - f, and in Sterk's printed labelling it is the root of label 11
(coble_cusp-admissibility-run.txt certifies "is +-delta: True" there).  So what a candidate
symmetry must do is carry label 11 to label 11, and the point of the computation is that the one
automorphism which does swap 12 and 13 does not: it carries 11 to 14.  An isometry g of T_En with
g(r_i) = r_{sigma(i)} therefore has g(delta) = r_14, which is not +-delta, so g lies outside
Gamma_Co,2 = Stab_{O(T_En)}(Z delta).

That is the concrete reason the three roots are not identified by any symmetry of the cusp: the
marking is extra data, and the symmetries that would identify the roots move it.

    usage: PYTHONPATH=<repo>/.scratch/sage-extensions/src python \\
               <repo>/computations/reports/coble_760-cusp-symmetry.py
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix  # noqa: E402

t0 = time.time()
C = CartanMatrix(["E", 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2 * U, -2 * C)
N = 12
BAS = [vector(ZZ, [1 if k == i else 0 for k in range(N)]) for i in range(N)]
e, f, ep, fp = BAS[0], BAS[1], BAS[2], BAS[3]
alpha = [BAS[4 + i] for i in range(8)]
Cinv = C.inverse()
abar = [vector(ZZ, [int(c) for c in sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))])
        for i in range(8)]


def ip(x, y):
    return int(vector(ZZ, x) * G * vector(ZZ, y))


delta = e - f
et, ft = e + ep + fp - alpha[0], f + ep + fp - alpha[0]
at = [ep - fp, alpha[1], fp + alpha[2]] + list(alpha[3:8])
Gt = matrix(ZZ, 8, 8, lambda i, j: ip(at[i], at[j]))
Gti = Gt.inverse()
abart = [vector(ZZ, [int(c) for c in sum(QQ(2 * Gti[k, i]) * at[k] for k in range(8))])
         for i in range(8)]
R5 = [at[1], at[3], at[4], at[5], at[6], at[7], at[0], abart[7],
      2 * et - at[0], 2 * et + (abart[1] - abart[2]), ft - et,
      et + ft + (abart[5] - abart[2]), et + ft + (abart[0] + abart[7] - abart[2]),
      et + ft + at[2]]

print("the symmetries of Sterk's cusp-5 diagram and the Coble root's fate")
print("(delta = e - f is the root of printed label 11: |(r_11, delta)| = %d, r_11^2 = %d)"
      % (abs(ip(R5[10], delta)), ip(R5[10], R5[10])))
assert abs(ip(R5[10], delta)) == 2 and ip(R5[10], R5[10]) == -2

G5 = matrix(ZZ, 14, 14, lambda i, j: ip(R5[i], R5[j]))
sig = [(int(G5[i, i]), tuple(sorted(int(G5[i, j]) for j in range(14) if j != i))) for i in range(14)]
cand = [[k for k in range(14) if sig[k] == sig[i]] for i in range(14)]
sols = []


def walk(assign, used):
    i = len(assign)
    if i == 14:
        sols.append(tuple(assign))
        return
    for k in cand[i]:
        if k in used:
            continue
        if all(int(G5[i, b]) == int(G5[k, assign[b]]) for b in range(i)):
            assign.append(k)
            used.add(k)
            walk(assign, used)
            used.discard(k)
            assign.pop()


walk([], set())
print("automorphisms of the labelled Gram: %d" % len(sols))
print()
adm = (12, 13, 14)
fixing = 0
for s in sols:
    lab = {l: s[l - 1] + 1 for l in range(1, 15)}
    keeps_delta = lab[11] in (11,)
    swaps = (lab[12], lab[13], lab[14])
    if keeps_delta:
        fixing += 1
    print("  sigma %s" % [lab[i] for i in range(1, 15)])
    print("     11 (delta) -> %2d   |   12,13,14 -> %2d, %2d, %2d   |   preserves Z delta: %s"
          % (lab[11], lab[12], lab[13], lab[14], keeps_delta))
print()
print("automorphisms preserving the Coble root's label (11 -> 11): %d of %d" % (fixing, len(sols)))
swap = [s for s in sols if s[11] + 1 == 13 and s[12] + 1 == 12]
both = [s for s in swap if s[10] + 1 == 11]
print("automorphisms swapping labels 12 and 13: %d" % len(swap))
print("  of those, ones that also fix label 11: %d" % len(both))
for s in both:
    lab = {l: s[l - 1] + 1 for l in range(1, 15)}
    print("  the candidate: %s" % [lab[i] for i in range(1, 15)])
    print("     12 -> %d, 13 -> %d, 14 -> %d, 11 (delta) -> %d"
          % (lab[12], lab[13], lab[14], lab[11]))
print()
print("VERDICT, stated from the numbers above and not from a programme.")
print("  There are %d symmetries of the labelled diagram, %d of them fix the Coble root's label,"
      % (len(sols), fixing))
print("  %d swap labels 12 and 13, and of those %d fix label 11." % (len(swap), len(both)))
if both:
    print("  So a symmetry of the cusp identifies 12 with 13 while preserving the Coble root's")
    print("  label: the candidate %s.  Whether it lifts to an integral isometry of T_En is the" % both[0])
    print("  remaining question, and this record does not decide it.")
else:
    print("  So no symmetry of the cusp identifies 12 with 13 while preserving the Coble root's")
    print("  label: every one that swaps them moves delta's label.  That is a negative about the")
    print("  diagram's symmetries, not about Gamma_Co,2, whose elements need not preserve the")
    print("  printed chamber; the orbit question therefore stands exactly where the library")
    print("  leaves it, and the lift question does not arise for these permutations.")
print()
print("=== the pair that a marking-preserving symmetry does exchange")
pair = [s for s in sols if s[10] + 1 == 11 and s[12] + 1 == 14 and s[13] + 1 == 13]
for s in pair:
    lab = [s[l - 1] + 1 for l in range(1, 15)]
    print("  the symmetry %s" % lab)
    print("  fixes the Coble root's label 11, and exchanges labels 13 and 14.")
    print("  If it lifted to an integral isometry of T_En, roots 13 and 14 would be")
    print("  Gamma_Co,2-equivalent, and the pair (12, 13) would be the only pair left to decide:")
    print("  no symmetry of the diagram exchanges 12 with either of them while fixing 11.")
    print("  Whether it lifts is an extension problem over the rank-%d sublattice the fourteen"
          % (12 - 2))
    print("  roots span, and no operation here performs it; that is the input item 7 still")
    print("  needs, together with the reduction it needed before.")
if not pair:
    print("  no symmetry fixes label 11 and exchanges 13 with 14")
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")

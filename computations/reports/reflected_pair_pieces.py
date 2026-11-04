"""Joint eigenspaces of the reflected pair on the model K3 lattice at the AEGS marking.
L = U^3 + E8(-1)^2. I_dP: v -> -v, u <-> u', e -> -e (both E8 blocks).
I_En: v -> -v, u <-> u', e-block1 <-> e-block2. alpha = e - f in the v-axis (coords 0,1).
J_Co = w_alpha . I_En, J_dP = w_alpha . I_dP. Integer arithmetic via maintained Sage
(kernel, Hermite form, determinants, characteristic polynomial for signatures)."""
from sage.all import ZZ, matrix, vector, block_matrix, identity_matrix
import numpy as np

DU = matrix(ZZ, [[0, 1], [1, 0]])
E8 = matrix(ZZ, [[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],
 [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],
 [0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
Em8 = -E8
G = DU.block_sum(DU).block_sum(DU).block_sum(Em8).block_sum(Em8)
n = 22
Id = identity_matrix(ZZ, n)

def op(swaps, signs):
    M = matrix(ZZ, n, n)
    claimed = set()
    for i in range(n):
        j = swaps.get(i, i)
        s = -1 if i in signs else 1
        M[j, i] = s
        claimed.add(j)
    return M

swapU = {2: 4, 4: 2, 3: 5, 5: 3}
swapE = dict(swapU)
for i in range(6, 14):
    swapE[i] = i + 8
    swapE[i + 8] = i
Idp = op(dict(swapU), set({0, 1}) | set(range(6, 22)))
Ien = op(swapE, {0, 1})

alpha = vector(ZZ, [1, -1] + [0] * 20)
assert alpha * G * alpha == -2
Ga = G * alpha
w = Id + matrix(ZZ, n, n, lambda i, j: alpha[i] * Ga[j])
J_Co = w * Ien
J_dP = w * Idp

def eigpiece(sC, sD):
    M = block_matrix(2, 1, [J_Co - sC * Id, J_dP - sD * Id])
    return M.transpose().kernel().basis_matrix()

def report(nm, K):
    r = K.dimensions()[0]
    Gs = K * G * K.transpose()
    if r:
        d = int(Gs.determinant())
        ev = np.linalg.eigvalsh(np.array(Gs, dtype=float))
        sig = (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()))
    else:
        d, sig = 0, (0, 0)
    print(nm, "rank", r, "det", d, "sig", sig)
    return d

tot = 1
for nm, sC, sD in [("(++)", 1, 1), ("(+-)", 1, -1), ("(-+)", -1, 1), ("(--)", -1, -1)]:
    tot *= report(nm, eigpiece(sC, sD))
Kco = eigpiece(1, 0) if False else (J_Co - Id).transpose().kernel().basis_matrix()
print("J_Co-invariant rank", Kco.dimensions()[0], "det", int((Kco * G * Kco.transpose()).determinant()))
He = vector(ZZ, [(1 if k in (2, 4) else 0) for k in range(22)])
Hf = vector(ZZ, [(1 if k in (3, 5) else 0) for k in range(22)])
alphaH = He + Hf
print("H = Delta(e)+Delta(f) =", alphaH, " H^2 =", alphaH * G * alphaH, " H.alpha =", alphaH * G * alpha)

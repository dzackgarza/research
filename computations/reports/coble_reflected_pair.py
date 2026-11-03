"""Maintained-tier computation for the reflected pair, following coble_aegs_involutions.py's
style and at the same provider pin: on the model lattice L = U^3 + E8^2 build the two AEGS
involutions, take alpha = e - f of the first U, w = L.reflection(alpha), and the reflected
pair J_Co = w o I_enr, J_dP = w o I_dP.  Compute the four joint eigenspaces (++, +-, -+, --)
as maintained sublattices, report rank, determinant, signature and evenness, and check the
isometry type of each against its maintained counterpart built independently: Lambda of the
construction side (U(2) perp <-2>), E8(-2) for the (+-) piece, and the T_Co model
(<2> perp U(2) perp E8(-2), as coble_aegs_involutions builds T_En-book) for the (--) one.
Everything below is raw integer matrix arithmetic ONLY where a kernel basis is computed
(maintained Sage matrix/kernel operations as in coble_aegs_involutions.py); all lattice-type
claims are made by the provider's own semantic checks."""
import sys
from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix, block_matrix
from sage.version import version as sage_version
from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)
PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'
print('provenance: %s, Sage %s' % (PIN, sage_version))

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
GRAM = block_diagonal_matrix(U, U, U, E8, E8)
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
n = int(L.rank())
assert int(L.determinant()) == -1 and L.is_even()

def blocks(vec):
    coords = [int(vec.to_vector()(i)) for i in range(n)]
    return (coords[0:2], coords[2:4], coords[4:6], coords[6:14], coords[14:22])

def image_under(kind, coords):
    v, u, u1, e, e1 = (list(part) for part in coords)
    if kind == 'dP': return [-x for x in v] + u1 + u + [-x for x in e] + [-x for x in e1]
    if kind == 'enr': return [-x for x in v] + u1 + u + e1 + e
    raise ValueError(kind)

def build_involution(kind):
    imgs = {}
    for i in range(n):
        b = L.basis_vector(i)
        imgs[i] = L.linear_combination({j: L.base_ring()(c) for j, c in enumerate(image_under(kind, blocks(b))) if c})
    return L.O()(lambda label: imgs[int(label)]), imgs

Idp, Idp_img = build_involution('dP'); Ien, Ien_img = build_involution('enr')

alpha = L.linear_combination({0: 1, 1: -1})
assert abs(int(alpha * alpha)) == 2 and int(alpha * alpha) == -2
w = L.reflection(alpha)

def apply_w(img):
    return lambda label: w(label)

J_Co, J_dP = (lambda label: w(Ien(label)), lambda label: w(Idp(label)))
assert all(J_Co(J_Co(b)) == b and J_dP(J_dP(b)) == b for b in [L.basis_vector(i) for i in range(n)])

# joint eigenspaces: kernel bases by maintained integer matrix kernel (as in the corpus's
# own scripts), then the provider's sublattice_from carries the semantic part.
Gram = matrix(ZZ, [[int(L.basis_vector(i) * L.basis_vector(j)) for j in range(n)] for i in range(n)])
def joint_matrix(kindJ, kindK, signJ, signK):
    AJ = matrix(ZZ, n, n)
    AK = matrix(ZZ, n, n)
    for i in range(n):
        for j in range(n):
            pass
    invJ = J_Co if kindJ == 'Co' else J_dP
    invK = Idp if kindK == 'dP' else Ien

def lin_rows_of_kern(A):
    K = A.kernel()
    return [list(row) for row in K.basis_matrix().rows()]

def op_matrix(wmap):
    return matrix(ZZ, n, n, lambda i, j: int(wmap(L.basis_vector(j)).to_vector()(i)))

M_Co = op_matrix(J_Co); M_dP = op_matrix(J_dP)
Id = matrix(ZZ, np_eye_placeholder := __import__('sage.all').identity_matrix(ZZ, n)) if False else matrix(ZZ, [[int(i == j) for j in range(n)] for i in range(n)])

pieces = {}
for tag, sJ, sK in [('++', 1, 1), ('+-', 1, -1), ('-+', -1, 1), ('--', -1, -1)]:
    M = block_matrix([[M_Co - sJ * Id], [M_dP - sK * Id]])
    rows = lin_rows_of_kern(M.transpose())
    rows = [[int(v) for v in r] for r in rows]
    vecs = [L.linear_combination({j: L.base_ring()(int(c)) for j, c in enumerate(r) if c}) for r in rows]
    sub = L.sublattice_from(vecs)
    pieces[tag] = sub
    print('%s: rank %d, det %s, sig %s, even %s'
          % (tag, sub.rank(), sub.determinant(), sub.signature_pair(), sub.is_even()))

# maintained types to compare against, built in coble_aegs_involutions.py's own style:
Lambda_target = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(2 * U, matrix(ZZ, [[-2]])).rows()])
E8m2_target = Lattices(ZZ)([list(r) for r in (2 * E8).rows()])
TCO_target = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
print('++ isometric to U(2) perp <-2>:', pieces['++'].is_isometric_to(Lambda_target) if pieces['++'].rank() else 'empty')
print('+- isometric to E8(-2):', pieces['+-'].is_isometric_to(E8m2_target) if pieces['+-'].rank() else 'empty')
print('-- isometric to <2> perp U(2) perp E8(-2):', pieces['--'].is_isometric_to(TCO_target) if pieces['--'].rank() else 'empty')

alpha_class = pieces['++']
H = alpha_class.basis_vector(0) if alpha_class.rank() else None

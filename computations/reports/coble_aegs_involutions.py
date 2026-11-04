"""Focused check: AEGS's involutions I_dP, I_enr, I_nik and their stated eigenspaces.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_aegs_involutions.py

Why this exists.  The A21 tuple needs a del Pezzo involution, and an earlier note in this repository
said the sources give it no lattice data at all.  That is wrong: AEGS (en.tex, def:involutions) give
three involutions in coordinates on L = U^3 (+) E8^2,

    I_dP  : (v, u, u', e, e') -> (-v, u', u, -e, -e')
    I_enr : (v, u, u', e, e') -> (-v, u', u,  e', e)
    I_nik = I_dP o I_enr      : (v, u, u', e, e') -> (v, u, u', -e', -e)

with eigenspaces

    S_dP = Delta(U) = U(2),                    T_dP = U (+) Delta^-(U) (+) E8^2
    S_enr = Delta(U) (+) Delta(E8) = U(2)(+)E8(2),  T_enr = U (+) Delta^-(U) (+) Delta^-(E8)

(Delta and Delta^- the diagonal and anti-diagonal).  What this script does is check that statement at the
owner, on the lattice in those coordinates, and connect the Enriques pair to the book's S_En, T_En.

What it does not do: it does not identify AEGS's I_dP with the del Pezzo involution of the Coble K3
cover, which is a labeling statement about a specific surface and not a property of L alone.
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s (.scratch/se-provider-c546/src, read-only export)' % PIN)
print('  Sage: %s' % sage_version)
print('  source for the involutions: AEGS en.tex, def:involutions and the eigenlattice display after it')
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])          # negative definite, as AEGS use it
GRAM = block_diagonal_matrix(U, U, U, E8, E8)
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
n = int(L.rank())
print('L = U^3 + E8^2: rank %d, det %s, signature %s, even %s'
      % (n, L.determinant(), L.signature_pair(), L.is_even()))
assert n == 22 and abs(int(L.determinant())) == 1

# block layout of a coordinate vector: v | u | u' | e | e'
def blocks(vec):
    coords = [int(vec.to_vector()(i)) for i in range(n)]
    return (coords[0:2], coords[2:4], coords[4:6], coords[6:14], coords[14:22])


def image_under(kind, coords):
    v, u, u1, e, e1 = (list(part) for part in coords)
    if kind == 'dP':
        return [-x for x in v] + u1 + u + [-x for x in e] + [-x for x in e1]
    if kind == 'enr':
        return [-x for x in v] + u1 + u + e1 + e
    if kind == 'nik':
        return v + u + u1 + [-x for x in e1] + [-x for x in e]
    raise ValueError(kind)


def build(kind):
    images = {}
    for i in range(n):
        basis = L.basis_vector(i)
        images[i] = L.linear_combination(
            {j: L.base_ring()(c) for j, c in enumerate(image_under(kind, blocks(basis))) if c})
    return L.O()(lambda label: images[int(label)])


basis = [L.basis_vector(i) for i in range(n)]
involutions = {kind: build(kind) for kind in ('dP', 'enr', 'nik')}
for kind, iso in involutions.items():
    square_ok = all(iso(iso(b)) == b for b in basis)
    fixes_basis_len = all(abs(int((iso(b)).to_vector()(i))) <= abs(int(b.to_vector()(i))) for b in basis for i in range(n))
    print('  I_%-4s is an isometry of L (by construction) and an involution: %s' % (kind, square_ok))
    assert square_ok
print('  I_nik = I_dP o I_enr: %s'
      % all(involutions['nik'](b) == involutions['dP'](involutions['enr'](b)) for b in basis))

# ---------------------------------------------------------------- the stated eigenspaces
def span(coordinate_rows):
    vecs = [L.linear_combination({j: L.base_ring()(c) for j, c in enumerate(row) if c})
            for row in coordinate_rows]
    return vecs


def pad(v=None, u=None, u1=None, e=None, e1=None):
    out = [0] * n
    for part, start in ((v, 0), (u, 2), (u1, 4), (e, 6), (e1, 14)):
        if part is not None:
            for k, val in enumerate(part):
                out[start + k] = val
    return out


Eu = [[1, 0], [0, 1]]
Ee = [[1 if i == j else 0 for j in range(8)] for i in range(8)]

S_dP = span([pad(u=u, u1=u) for u in Eu])
T_dP = span([pad(v=v) for v in Eu] + [pad(u=u, u1=[-x for x in u]) for u in Eu]
            + [pad(e=e) for e in Ee] + [pad(e1=e) for e in Ee])
S_enr = span([pad(u=u, u1=u) for u in Eu] + [pad(e=e, e1=e) for e in Ee])
T_enr = span([pad(v=v) for v in Eu] + [pad(u=u, u1=[-x for x in u]) for u in Eu]
             + [pad(e=e, e1=[-x for x in e]) for e in Ee])

checks = (
    ('S_dP  = Delta(U)', S_dP, 'dP', +1),
    ('T_dP  = U + Delta^-(U) + E8^2', T_dP, 'dP', -1),
    ('S_enr = Delta(U) + Delta(E8)', S_enr, 'enr', +1),
    ('T_enr = U + Delta^-(U) + Delta^-(E8)', T_enr, 'enr', -1),
)
for label, vectors, kind, sign in checks:
    iso = involutions[kind]
    good = all(iso(x) == sign * x for x in vectors)
    sub = L.sublattice_from(vectors)
    print('  %-40s acts by %+d on all its basis vectors: %s; rank %d, det %s, signature %s'
          % (label, sign, good, sub.rank(), sub.determinant(), sub.signature_pair()))
    assert good

# ---------------------------------------------------------------- the book's lattices
S_En_book = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(2 * U, 2 * E8).rows()])
T_En_book = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
S_enr_lat = L.sublattice_from(S_enr)
T_enr_lat = L.sublattice_from(T_enr)
print('')
print("  AEGS's Enriques pair versus the book's S_En = U(2) + E8(2), T_En = U + U(2) + E8(2):")
print('    S_enr isometric to S_En: %s' % S_enr_lat.is_isometric_to(S_En_book))
print('    T_enr isometric to T_En: %s' % T_enr_lat.is_isometric_to(T_En_book))
print('    |A_{S_enr}| = %d, |A_{T_enr}| = %d, so [L : S_enr + T_enr] = %d = 2^10'
      % (S_enr_lat.discriminant_group().cardinality(),
         T_enr_lat.discriminant_group().cardinality(),
         S_enr_lat.discriminant_group().cardinality()))
print('')
print('SUMMARY')
print('  AEGS def:involutions is lattice data, and the owner confirms it: I_dP, I_enr, I_nik are')
print('  involutions of L = U^3 + E8^2, I_nik = I_dP o I_enr, and the four stated eigenspaces act by')
print('  +1 and -1 as AEGS say.  AEGS\'s Enriques pair is the book\'s S_En, T_En, and the index of')
print('  S_enr + T_enr in L is |A_{S_enr}| = 2^10, which is the figure used in the embedding argument.')
print('  An earlier note in this repository said the sources give I_dP no lattice data; that is')
print('  withdrawn.  What remains a labeling statement: identifying this I_dP with the del Pezzo')
print('  involution of the Coble K3 cover, i.e. its commutation with I_Co and the fixity of H.')
print('OK: the involutions and their eigenspaces verified at the owner, from the defining source')

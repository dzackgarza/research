# Container-only validation (DECLARED shared setup):
# 1) execute the provider's own validated test verbatim;
# 2) cross-check the hand-built discriminant forms against the LATTICE route
#    (Lattices(ZZ)(gram).discriminant_group()), the maintained semantic lattice API.
# Requires: PYTHONPATH=<provider checkout>/src, run under the container (Sage 11.0.beta5).
from sage.version import version as sage_version
print('container validated-test, Sage:', sage_version)

# 1) the validated test, verbatim
ns = {}
path = '/repo/.scratch/se-provider-6ad7a5ea/tests/forms/test_the_coble_anti_isometry.sage'
exec(compile(open(path).read(), path, 'exec'), ns)
ns['test_the_two_coble_discriminant_forms_are_anti_isometric']()
print('validated test 1 (decision): PASS')
ns['test_the_witness_is_a_typed_isometry_realizing_the_anti_isometry']()
print('validated test 2 (typed witness): PASS')

# 2) lattice-route cross-check of the two models' forms
from sage.all import ZZ as SageZZ, CartanMatrix, matrix, block_diagonal_matrix, diagonal_matrix
from sage_extensions.all import Lattices
C8 = -CartanMatrix(['E', int(8)])
U2 = matrix(SageZZ, [[0, 2], [2, 0]])
gram_T = block_diagonal_matrix(matrix(SageZZ, [[2]]), U2, 2 * C8)
gram_S = block_diagonal_matrix(matrix(SageZZ, [[-2]]), U2, 2 * C8)
gram_Sdg = diagonal_matrix(SageZZ, [2] + [-2] * 10)
LT = Lattices(ZZ)([list(r) for r in gram_T.rows()])
LS = Lattices(ZZ)([list(r) for r in gram_S.rows()])
LSdg = Lattices(ZZ)([list(r) for r in gram_Sdg.rows()])
DT, DS, DSdg = LT.discriminant_group(), LS.discriminant_group(), LSdg.discriminant_group()
print('|A_T|, |A_S|, |A_Sdiag| =', DT.cardinality(), DS.cardinality(), DSdg.cardinality())
print('lattice route: DS.is_anti_isometric(DT) =', DS.is_anti_isometric(DT))
print('lattice route: DSdiag.is_isomorphic(DS) =', DSdg.is_isomorphic(DS))
w_lat = DS.isometry_to(DT.twist(-1))
print('lattice route: DS.isometry_to(DT(-1)) =', type(w_lat).__name__)
gs = tuple(DS.module_generators())
gt = tuple(DT.module_generators())
im0 = w_lat.forward()(gs[0])
DTm = DT.twist(-1)
gtm = tuple(DTm.module_generators())   # the twisted parent the image lives in
coords0 = None
import itertools as _it
for bits in _it.product((0, 1), repeat=11):
    if sum(int(b) * gtm[i] for i, b in enumerate(bits)) == im0:
        coords0 = bits
        break
print('lattice-route witness on [generator 0 of S]:', coords0)
print('  equals eta_0 = [g/2] = (1,0,...,0)?', coords0 == (1,) + (0,) * 10)
ok = all(DT.twist(-1).q(w_lat.forward()(x)) == DS.q(x) for x in gs)
print('lattice-route witness isometry on generators (q):', ok)

import pathlib
import sys

from sage.all import QQ, ZZ, identity_matrix, matrix
from pytest import raises

ROOT = pathlib.Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
    IntegralLattice,
    IntegralLatticeGluing,
)
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

from src.lattices.category import (
    ConsolidatedLattice,
    DiscriminantGroups,
    Lattice,
    LatticeHomset,
    RationalLattices,
    from_sage,
)


U = Lattice("U")
assert isinstance(U, ConsolidatedLattice)
assert isinstance(U.sage_object(), FreeQuadraticModule_integer_symmetric)
assert U in RationalLattices(ZZ).Integral()
assert U.signature_pair() == (1, 1)

U_QQ = U.rational_span()
assert U_QQ.base_ring() == QQ
assert U_QQ.gram_matrix() == U.gram_matrix()
assert U_QQ in RationalLattices(QQ)

A2 = Lattice("A2")
A2_dual = A2.dual()
assert A2.sage_object().is_submodule(A2_dual.sage_object())
assert A2_dual in RationalLattices(ZZ)
assert A2_dual not in RationalLattices(ZZ).Integral()
assert A2_dual.gram_matrix().base_ring() == QQ
assert A2_dual.dual() == A2

H = A2.hom(A2)
assert isinstance(H, LatticeHomset)
assert isinstance(H.sage_homset(), FreeModuleHomspace)
identity = H(identity_matrix(2))
assert isinstance(identity, FreeModuleMorphism)
assert identity.matrix() == identity_matrix(2)

with raises(ValueError, match="lattice morphisms must preserve the bilinear form"):
    H(2 * identity_matrix(2))

H5 = matrix(ZZ, 2, 2, [2, 1, 1, -2])
L = Lattice(2 * H5)
A = L.discriminant_group()
assert A in DiscriminantGroups()
assert A.invariants() == (2, 10)
assert A.primary_part(2).invariants() == (2, 2)
assert A.primary_part(5).invariants() == (5,)
assert A.cover() == A.V()
assert A.relations() == A.W()

D = TorsionQuadraticForm(identity_matrix(3) / 2)
assert D in DiscriminantGroups()
assert D.orthogonal_group().order() == 6

L1_sage = IntegralLattice(matrix([[4]]))
g = L1_sage.discriminant_group().gens()[0]
glued = from_sage(IntegralLatticeGluing([L1_sage], [[2 * g]]))
assert glued.gram_matrix() == matrix([[1]])

# NOTE: this is NOT a "stale" API. Do not delete or overwrite any specs
from pathlib import Path
import sys

sys.path.insert(0, str(Path(".").resolve()))

from src.lattices.lattices import FreeBilinearModule, Lattice

U2 = Lattice.U().twist(2)
assert U2.is_even()

O_U2 = U2.orthogonal_group()
swap = matrix(ZZ, [[0, 1], [1, 0]])
minus_I2 = -identity_matrix(ZZ, 2)
assert swap not in O_U2 # A matrix is not a hom
assert O_U2.from_matrix(swap) in O_U2 # Checks isometry condition
assert minus_I2 not in O_U2 # A matrix is not a hom
assert O_U2(minus_I2) in O_U2 # __call__ is a thin dispatcher

swap = O_U2(swap)
minus_I2 = O_U2(minus_I2) # Proper constructions, don't work with raw matrices: work with semantic homs that have matrix REPRESENTATIONS

centralizer = O_U2.centralizer(minus_I2)
assert minus_I2 in centralizer
assert identity_matrix(ZZ, 2) not in centralizer.kernel_of_discriminant_action() # A matrix is not a hom
assert O_U2.identity() in centralizer.kernel_of_discriminant_action() # Semantic identity.
# TODO: I have no idea what this is
# There is a map O(L) -> O(A_L), say p_L := L.O().morphism_to_discriminant()
# Then any subgroup G in O(L) has G.inclusion() mapping G -> O(L)
# And O^+(L) := ker(p_L) is L.O_plus()
# Which has a map p_L_plus: O^+(L) -> O(L) where (p_L_plus * p_L).image() == 0 in O(A_L)
# So if G is the centralizer in O(L) of f, what does G.kernel_of_discriminant_action() even mean...? There is no map G -> O^+(L), only a map G -> O(L) -> O(A_L)

U = Lattice.U()
e, f = tuple(U.gens())
assert e.span() == U.span([e])
assert e.is_isotropic() and e^2 == 0
assert e.perp() == e.span()
assert e.span().perp() == e.span()

ambient = U + Lattice.Z()
e1, f1, g1 = tuple(ambient.gens())
assert e1.perp() == ambient.span((e1, g1))
assert f1.perp() == ambient.span((f1, g1))

ambient_sum = U + U2
iota_U, iota_U2 = ambient_sum.embeddings
assert iota_U.image().perp() == iota_U2.image()
assert iota_U2.image().perp() == iota_U.image()
assert ambient_sum.quotient_by(iota_U.image()).is_isometric_to(U2)

swap_morphism = U.O().from_dict({e: f, f: e})
assert swap_morphism.to_matrix() == swap
# assert minus_I2 in U.orthogonal_group().stabilizer_of_isotropic_line(e)
# assert swap not in U.orthogonal_group().stabilizer_of_isotropic_line(e)
assert minus_I2 in U.O().stabilizer(e.span()) # Dispatch for isotropic lines
assert swap not in U.O().stabilizer(e.span())
assert minus_I2 not in U.orthogonal_group().stabilizer(e) # Stabilizes <e> but not e, because it sends e -> -e

dual = U2.dual()
dual_line = dual.span((next(iter(dual.gens())),))
dual_quotient = dual.quotient_by(dual_line)
assert isinstance(dual_line, FreeBilinearModule)
assert isinstance(dual_quotient, FreeBilinearModule)
assert dual_line.base_ring() is ZZ
assert dual_quotient.base_ring() is ZZ
assert dual_line.value_ring() is QQ
assert dual_quotient.value_ring() is QQ


# TODO: assert saturation of a finite-index sublattice is the full lattice.
# TODO: assert on L.maximal_even_overlattice() isometry class
# TODO: assert on L.overlattice_from_glue(...{glue data}...)
# TODO: does L.overlattice_from_gens([ (1/2)*(e+f) ]), e.g.
# TODO: assert not hasattr(L, "signature_pair")
# TODO: assert L.signature() = (p,q) when L is nondegenerate, and (p,q,n) when L is degenerate, where n := L.radical().rank()

Z2 = ZZ / (2*ZZ)
Z4 = ZZ / (4*ZZ)
R = 2*ZZ
assert Z2^2 == Z2.direct_product(Z2)
assert not Z2^2.is_isomorphic_to(Z4)
assert ZZ in Modules(ZZ)
assert R in Modules(ZZ)
assert Z2 in Modules(ZZ)
assert Z2 in Modules(Z2)
assert Z2 == ZZ/2 # Syntax sugar
assert Z4 == ZZ/4
assert Z2.is_field() and not Z4.is_field() # Identify Z/p with F_p

M = ZZ^3
assert M.base_ring() == ZZ
assert M in Modules(ZZ)
assert M.is_free() and M.is_torsionfree()
assert not M.is_torsion()
assert M.rank() == 3 # Validates M is free before computing
assert M == ZZ + ZZ + ZZ # Direct sum
assert M.dual() == M.Hom(ZZ)
assert M.dual() in Modules(ZZ) # R-Mod is enriched over itself
assert M * M == M.tensor(M) # Always tensors over common base ring
assert M.tensor(Z2) in Modules(Z2) 
assert M/(2*M) == M.tensor(Z2) # Canonical isomorphisms are equalities
assert M.base_change(Z2) == M.tensor(Z2) # Base change to S := \otimes_ZZ S

F1, F2 = ZZ^2, ZZ^3
T1, T2 = ZZ/5, ZZ/7 
M1 = F1 + T1
M2 = F2 + T2
assert M1.free_part() == F1 and M1.torsion_part() == T1
assert M2.free_part() == F2 and M2.torsion_part() == T2

# General tensor product formula
assert M1 + M2 == (F1 * F2) + (F1 * T2) + (T1 * F2) + (T1 * T2)

assert (M1 + M2).free_part() == F1 * F2

assert (ZZ^2 * ZZ^3).rank() == 2*3
assert (ZZ^2 + ZZ^3).rank() == 2+3

M.<x,y,z> = ZZ^3
Md = M.dual()
assert Md == M.Hom(ZZ)

f = M.Hom(ZZ).from_dict({
	x: 1,
	y: 3,
	z: 5
}) # Convenience: interpret n as n*g where g is a positive generator
assert f == M.Hom(ZZ).from_images([1,3,5])
assert f == M.Hom(ZZ).from_matrix(matrix(ZZ, 1, [1,3,5]))
assert f.to_matrix() == matrix(ZZ, [1,3,5])
assert f.to_dict().values() == [1,3,5]

R = QQ/ZZ
assert R in Modules(ZZ) # Need a working model of this ZZ-module
assert R(1/2) == R(3/2) # Coerce QQ elements to quotient
assert R(3/2).lift() == QQ(1/2) # Canonical representatives in [0, 1)

# Need compatible p-adic theory for base ring
S = ZZ.complete(5) # I-adic completion of a ring R
assert S == Zp(5) # Set reasonable defaults
assert (ZZ^3).base_change(S) == S^3
assert ZZ.fraction_field() == QQ # Need rings of integers to know their fraction fields
assert Zp(5).fraction_field() == Qp(5) # Need Qp to exist as a field for "local" lattice theory

ZZ_L5 = ZZ.localize(5)
assert ZZ_L5 == Localization(ZZ, [5])
assert ZZ_L5 == ZZ.adjoin(1/5)
assert ZZ_L5 == ZZ.invert(5)
assert 1/5 in ZZ_L5 and 1/3 not in ZZ_L5




# Basic homological algebra in ZZ-Mod
M = ZZ^3 + ZZ/2 + ZZ/3 + ZZ/5
# Tor_0(Z/p, M) = M/pM
# Tor_1(Z/p, M) = {m in M | p*M = 0}
# Tor_n(Z/p, M) = 0 for n >= 2
assert Tor(Z/11, M) == [M/11*M, M.p_torsion(11)]
# M.p_torsion(p) is a condition set defining a ZZ-submodule
# Use Tor_n(F + T, B) = \oplus_i Tor_n(T_i, B) to reduce to cyclic case
assert Tor(QQ/ZZ, M) == M.torsion_part()
assert Tor(ZZ^2, M) == 0 # Tor(F, M) = 0 when F is free.

assert Ext(Z/11, M) == [M.p_torsioN(11), M/11*M] 
assert Ext(ZZ, M) == 0 # Ext(F, B) = 0 when F is free.
# TODO: assert tables of Tor(A, B), Ext(A, B) when A, B = Z/p, ZZ

M = ZZ^4
assert M in Modules(ZZ)
assert M.complete(2) in Modules(ZZ.complete(2))

M1.<g1,g2> = ZZ^2
M2.<h1, h2> = ZZ^2
H = M1.Hom(M2) 
assert H in Modules(ZZ) 
f = H.from_matrix(matrix(ZZ, 2, [0,1,1,0]))
# f is the "swap" morphism
assert f in H and not f in M1.Hom(ZZ^3)
assert f in (ZZ^2).Hom(ZZ^2) # Domain and codomain are canonically ZZ^2,
# f in Hom(A, B) and Hom(C, D) when A == C and B == D
assert f(g1) == h2 and f(g2) == h1
assert f.apply_to([g1,g2]) == [h2, h1] # Apply to sequences
assert f.to_matrix() == matrix(ZZ, 2, [0,1,1,0])
assert f.is_injective() and f.kernel() == Modules(ZZ).zero() # Kernel is an explicit module
assert ZZ^0 == Modules(ZZ).zero() # Convenience
assert f.kernel() == 0 # Convenience: coerce to ZZ-module
assert f.is_surjective() and f.cokernel() == Modules(ZZ).zero() # Cokernel is an explicit module
assert f.is_bijective() and f.is_isomorphism() and not f.is_identity()
assert f.image() == M2 # Image is a module
assert f.lift(h1) == g2 and f.lift(h2) == g1 # Find some preimage

# Real kernels and cokernel support
g = H.from_images([2*h1, 3*h2])
assert g.to_matrix() == diagonal_matrix(ZZ, [2,3])
assert g.cokernel() == ZZ/2 + ZZ/3
assert g.cokernel() in Modules(ZZ)
h1_bar, h2_bar = g.cokernel().gens()
pi = g.cokernel().projection() # For f: A->B, the morphism pi: B->coker(f)
assert pi(h1) == h1_bar and pi(h2) == h2_bar # Generators are images of generators
assert h1_bar.lift() == h1 and h2_bar.lift() == h2
assert pi.is_surjective()
assert pi.kernel() == M2.span([2*h1, 3*h2]) # coker(f) = (<h1> + <h2>) / (<2h_1> + <3h_2>)

assert g.cokernel().invariants() == [2,3]

assert f.base_change(Zp(3)) in (Zp(3)^2).Hom(Zp(3))
assert f.base_change(Zp(3)).to_matrix() == matrix(Zp(3), f.to_matrix())

assert M1.End() == M1.Hom(M1)
assert M1.End().identity() in M1.Aut()
assert M1.End() in Monoids
assert M1.Aut() in Groups

assert (ZZ^3).Hom(ZZ^2).natural_map().to_matrix() == matrix(ZZ, 2*3, [[1,0,0],[0,1,0],[0,0,0]]) # Natural maps are always [1 | 0] or [1 | 0]^t, matches first n generators of each module. Only makes sense for free modules as stated

f = ZZ.Hom(ZZ/2).element_from_function(lambda x: x % 2) # Any callable allowed, apply to generators to ensure it is a morphism
assert f.kernel() == 2*ZZ

g = ZZ.End().element_from_function(lambda x: 2*x) # End has all Hom methods
assert g.kernel() == 0 and g.cokernel() == ZZ/2

M = ZZ/4
h = M.End().element_from_function(lambda x: 2*x)
assert M.as_set() == {M(0), M(1), M(2), M(3)}
assert M.as_set() == {M(4), M(5), M(6), M(7)}
assert {h(x) for x in M} == {M(0), M(2)}
assert h.image() == M.span([M(0), M(2)])
assert h.kernel() == M.span([M(0)])
assert M.span([M(0)]) == Modules(ZZ).zero()
assert h.cokernel() == ZZ/2 
assert list(map(lambda x: x.lift(), h.cokernel())) == [M(0), M(1)]
pi = h.cokernel().projection()
assert pi(M(0)) == pi(M(2)) and pi(M(1)) == pi(M(3))
# Coker(f) = {[0] + im(f), [1] + im(f)} as cosets

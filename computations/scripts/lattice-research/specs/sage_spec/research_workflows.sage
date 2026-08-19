
U = Lattices.U()
E8 = Lattices.E8()
L_K3 = Lattices.K3()

assert L_K3 == U^3 + E8^2
assert L_K3.summands() == [U, U, U, E8, E8]
#e,f,ep,fp,epp,fpp,r1,...,r8,r1p,...r8p = L_K3.gens() # Need to hack preparser to learn ellipses patterns
u1,u2,u3,e1,e2 = L_K3.block_variables()
H = L_K3.End()

# del Pezzo
I_dp = H.from_block_dict({
	u1: -u1,
	u2: u3,
	u3: u2,
	e1: -e1,
	e3: -e3,
})
assert I_dp == -1 * U.O().identity() + (U + U).O().permute_factors((1,2)) - (E8 + E8).O().identity()
# If L = \bigoplus_i^n L_i is an n-fold sum, permutations sigma in S_n define self-isometries. Here (1,2) is cycle notation.
assert I_dp.is_involution() and I_dp.order() == 2
assert I_dp in L_K3.O()
assert L_K3.O() == L_K3.Aut()

S_dp, T_dp = I_dp.invariant_coinvariant_pair() # +1/-1 eigenlattice in this case

assert S_dp.is_isometric_to( Lattices.Nikulin((2,2,0), 1) )
assert S_dp.is_isometric_to( U.twist(2) )
assert S_dp.is_isometric_to( U.diagonal_sublattice() )

assert T_dp.is_isometric_to( Lattices.Nikulin((20,2,0), 2) )
assert T_dp.is_isometric_to( U + U.twist(2) + E8^2 )
assert T_dp.is_isometric_to( U + U.antidiagonal_sublattice() + E8^2 )


assert S_dp.embedding().is_primitive() # Subobjects have embedding data attached.
assert T_dp.embedding().is_primitive() 

# Enriques

I_en = H.from_block_dict({
	u1: -u1,
	u2: u3,
	u3: u2,
	e1: e3,
	e3: e1,

})

assert I_en == -U.O().id() + (U+U).O().swap() + (E8+E8).O().swap() # Convenienve/sugar
assert I_en.is_involution() and I_en.order() == 2 and I_en in L_K3.O()

S_en, T_en = I_en.invariant_coinvariant_pair() 

assert S_en.is_isometric_to( Lattices.Nikulin((10,10,0),1) )
assert S_en.is_isometric_to( U.twist(2) + E8.twist(2) )
assert S_en.is_isometric_to( U.diagonal() + E8.diagonal() )

assert T_en.is_isometric_to( Lattices.Nikulin((12,10,0),2) )
assert T_en.is_isometric_to( U + U.antidiagonal() + E8.antidiagonal() )
assert T_en.is_isometric_to( U + U.twist(2) + E8.twist(2) )


assert S_en.embedding().is_primitive() # Subobjects have embedding data attached.
assert T_en.embedding().is_primitive() 

# Nikulin


I_nik = H.from_block_dict({
	u1: u1,
	u2: u2,
	u3: u3,
	e1: -e2,
	e2: -e1,
})

assert I_nik == (U^3).O().identity() - (E8^2).O().swap()
assert I_nik.is_involution() and I_nik.order() == 2 and I_nik in L_K3.O()

S_nik, T_nik = I_nik.invariant_coinvariant_pair()

assert S_nik.is_isometric_to( Lattices.Nikulin( (14,8,0), 3) )
assert S_nik.is_isometric_to( U^3 + E8.antidiagonal() )
assert S_nik.is_isometric_to( U^3 +  E8.twist(2) )

assert T_nik.is_isometric_to( Lattices.Nikulin( (8,8,0), 0) )
assert T_nik.is_isometric_to( E8.diagonal() )
assert T_nik.is_isometric_to( E8.twist(2) )

assert S_nik.embedding().is_primitive() # Subobjects have embedding data attached.
assert T_nik.embedding().is_primitive() 

assert I_nik == I_dp * I_en

assert L_K3.subgroup([I_nik, I_dp, I_en]).is_isomorphic_to(ZZ/2 + ZZ/2)

# Moduli spaces
G = L_K3.O()

# The following 3 are only conjectures, but maybe can be proved with computations.
assert G.stabilizer(S_en) == G.stabilizer(T_en) == G.centralizer(I_en)
assert G.stabilizer(S_dp) == G.stabilizer(T_dp) == G.centralizer(I_dp)
assert G.stabilizer(S_nik) == G.stabilizer(T_nik) == G.centralizer(I_nik)

# But this is what we actually use in the paper
ep, fp = S_dp.gens() # U(2)
h = ep + fp
assert h^2 == 4

Stab_h = G.stabilizer(h)
Cent_inv = G.centralizer(I_en)


# There is always a morphism from Z_{O(L)} -> O(T) and O(S) in this case

p_sen = Cent_inv.invariant_sublattice_projection()
p_ten = Cent_inv.coinvaraint_sublattice_projection()

assert p_sen.is_surjective() and p_ten.is_surjective() # Should follow from Nikulin 79 1.5.2 and 3.6.3

pre_Gamma_En2 = Stab_h & Cent_inv # {g in O(L_K3) | g*I_En = I_En*g, g(h) = h}

p_ten_res = pre_Gamma_En2.coinvariant_sublattice_projection() # Restrict the domain of p_ten
assert p_ten_res.domain() == pre_Gamma_En2 and p_ten_res.codomain() == T_en.O()

Gamma_En2 = p_ten_res.image() # In O(T_En)
iota_en2 = Gamma_En2.inclusion()
assert iota_en2 in Gamma_En2.Hom(T_en.O()) # Group morphism
assert iota_en2.index().is_finite()

assert len(T_en.isotropic_vectors() / T_en.O()) == 2 # Computes orbits
assert len(T_en.isotropic_vectors() / Gamma_En2) == 5 # Similarly, orbits

assert len(T_en.norm_n_vectors(-2) / Gamma_En2) == 1 # Unique by Nam85 2.13
alpha = (T_en.norm_n_vectors(-2) / Gamma_En2).representative() # Cache the computation!

S_co = Lattices.Z(-2) + U().twist(2) + E8.twist(2)
T_co = Lattices.Z(2) + U.twist(2) + E8.twist(2)
assert S_co.is_isometric_to( Lattices.Nikulin( (11,11,1), 1) )
assert T_co.is_isometric_to( Lattices.Nikulin( (11,11,1), 2) )
assert S_co.is_isometric_to( Lattices.I(1, 10).twist(2) )
assert T_co == S_co.perp() and S_co == T_co.perp()

assert alpha.perp().is_isometric_to(S_co) or alpha.perp().is_isometric_to(T_co)


assert len(T_en.norm_n_vectors(-4) / Gamma_En2) == 2
orb_1, orb_2 = (T_en.norm_n_vectors(-4) / Gamma_En2)
b1, b2 = orb_1.representative(), orb_2.representative()

one_perp = Lattices.Z(4) + U + E8.twist(2)
betas = [x for x in [b1,b2] if x.perp().is_isometric_to(one_perp)]
assert len(betas) == 1 # By Nam85 2.15
beta = betas[0]


S_nod = ... # Nodal Enriques surfaces
T_nod = ... 

assert beta.perp().is_isometric_to(S_nod) or beta.perp().is_isometric_to(T_nod) # Unsure which




# Uniqueness of embeddings
H = T_en.Hom(L_K3)
t_emb = U.O().id() + U.twist(2).O().id() + E8.twist(2).O().diagonal()
assert E8.twist(2).diagonal() in E8.twist(2).Hom(E8^2) # v -> (v,v)
assert t_emb.is_essentially_unique() # By Nik79 Thm 1.14.4

Lp = U + E8
Hp = U.Hom(Lp)
u = U.block_variables()
up, ep = Lp.block_variables()
iota_p = Hp.from_block_dict({u: up}) # U -> U+E8 by inclusion in the first factor
assert iota_p.is_essentially_unique() # Why: Lp = U + U.perp() and both are unimodular

Gamma_en = T_en.O()
Gamma_dp = T_dp.O()
assert Gamma_en & Gamma_dp == Gamma_En2 # True, but likely hard to check...

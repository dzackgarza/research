r"""
Finitely presented modules over a PID.
TODO: owns most module constructions in Modules(R), should delegate here.
Every object in this category is represented by an ordered list of ring elements, which can include zero, representing a preferred decomposition of M as follows:
if the list is [0_1, 0_2, ..., 0_n, r_1, ..., r_m], it represents
M := R_1 \oplus ... \oplus R_n \oplus R/r_1 \oplus ... \oplus R/r_m
This is not EQUAL to its SNF representation, just isomorphic!
This means that if you want to compute coker(f: M->N), you first have to
compute D = SNF(A_f), as well as U*A_f*V = D. Then define Q as the module
abstractly determined by D, say with generators q_i -- then the morphism
\pi: N->Q which sends the generators n_i of N to q_i is defined by 
the matrix of U, with various coordinates interpretted mod d_i.

All objects:
    - order := generator of Ann_R(M)
    - invariant_factors: [0,...,0,r_1,...,r_n] with n zeros for R^n 
    - free_part
    - torsion_part
    - free_rank
    - element_from_vector
All elements:
    - to_vector
    - order := generator of Ann_R(m) = Ann_R(<m>)
All homsets:
    - from_dict
    - from_matrix
    - from_images(self, Sequence[RModuleElement]) -> RModuleMorphism
All morphisms:
    - to_dict
    - to_matrix
    - to_list
    - to_tuple
    - to_function
Torsion subcategory:
    p_part := the factor of (R/p)^n in T in M = F + T
    is_p_elementary := M == M.p_part()
Lattices:
    - determinant
    - discriminant_group
    - orthogonal_group := O(L)
    - special_orthogonal_group := SO(L)
    - stable_orthogonal_group := O^+(L)
    - stable_special_orthogonal_group := SO^+(L)
"""

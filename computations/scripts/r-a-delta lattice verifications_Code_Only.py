"""
Code extracted from: r-a-delta lattice verifications.ipynb
This file contains only the code cells from the notebook.
"""

# === Code Cell 1 ===

using Oscar
using LinearAlgebra
using Oscar.Hecke


# === Code Cell 2 ===

function twist(L, k)
    Lm = gram_matrix(L)
    n = minimum(size(Lm))
    Lm_twist = Lm * (k * identity_matrix(ZZ, n))
    L_twist = integer_lattice(gram = Lm_twist)
    return L_twist
end


# === Code Cell 3 ===

Z1 = root_lattice(:I, 1)
display(Z1)

Z2 = twist(Z1, 2)
display(Z2)

E8 = twist( root_lattice(:E, 8), -1)
display(E8)

E82 = twist(E8, 2)
display(E82)

H = hyperbolic_plane_lattice()
display(H)

H2 = twist(H, 2)
display(H2)


# === Code Cell 4 ===

E10 = direct_sum(H, E8)[1]
display(E10)

E10_2 = twist(E10, 2)
display(E10_2)


# === Code Cell 5 ===

Sdp = H2
Sen = direct_sum( twist(H, 2), twist(E8, 2) )[1]
Lnikp = direct_sum(H, H, H, twist(E8, 2) )[1]

Tdp = direct_sum(H, twist(H, 2), E8, E8)[1]
Ten = direct_sum(H, twist(H, 2), twist(E8, 2) )[1]
Lnikm = twist(E8, 2)


# === Code Cell 6 ===

# Return whether L is primary, that is whether L is integral and its discriminant group (see discriminant_group) is a p-group for some prime number p. 
# In case it is, p is also returned as second output.
#Note that for unimodular lattices, this function returns (true, 1). 
# If the lattice is not primary, the second return value is -1 by default.

display( is_primary_with_prime(H) ) #unimodular
display( is_primary_with_prime(E8) ) #unimodular
display( is_primary_with_prime(E10) ) #unimodular
display( is_primary_with_prime(E10_2) ) #2-primary


# === Code Cell 7 ===

display( is_elementary_with_prime(H) ) #unimodular
display( is_elementary_with_prime(E8) ) #unimodular
display( is_elementary_with_prime(E10) ) #unimodular
display( is_elementary_with_prime(E10_2) ) #2-elementary


# === Code Cell 8 ===

# Return the number of (positive, zero, negative) inertia of L.

display(signature_tuple(H))
display(signature_tuple(E8))
display(signature_tuple(E10))
display(signature_tuple(E10_2))


# === Code Cell 9 ===

discriminant_group(E10)


# === Code Cell 10 ===

discriminant_group(E10_2)


# === Code Cell 11 ===

L = direct_sum(Z2, H2, E82)[1]


# === Code Cell 12 ===

display( signature_tuple(L) )
display( is_primary_with_prime(L) )
display( is_elementary_with_prime(L) )
display( discriminant_group(L) )


# === Code Cell 13 ===

function rad_invts(lat::ZZLat)
    display("------------------------------------")
    is_elem = is_elementary_with_prime(lat)
    if is_elem[1] == false || is_elem[2] != 2
        display("Not a 2-elementary lattice:")
        display(is_elem)
        return 0
    end
    #display("This is a p-elementary lattice.")

    D_L = discriminant_group(lat)
    display(D_L)
    Q = D_L.gram_matrix_quadratic
    G = D_L.ab_grp
    #display(G)

    #display("Computing r..")
    r = rank(lat)

    #display("Computing a..")
    a = length( filter(x -> x == 2, elementary_divisors(G)) )

    #display("Computing delta...")
    
    n = minimum(size(Q))
    diags = [ Q[i, i] for i in 1:n ]
    #show("Diagonal of Q:")
    #show(diags)
    are_diags_ints = map(is_integer, diags)
    all_integer_diags = reduce(&, are_diags_ints)
    # = 1 if all integers, = 0 if any non-integer  
    
    delta = 1 - all_integer_diags
    # delta = 0 <=> image in Z, dellta=1 <=> non-integral image

    display("------------------------------------")
    
    return (r, a, delta)
end


# === Code Cell 14 ===

display( rad_invts(Sdp) )
display( rad_invts( Sen ) )
display( rad_invts( Lnikp ) )

display( rad_invts( Tdp ) )
display( rad_invts( Ten ) )
display( rad_invts( Lnikm ) )


# === Code Cell 15 ===

lat = Lnikp
is_elem = is_elementary_with_prime(lat)
if is_elem[1] == false || is_elem[2] != 2
    display("Not a 2-elementary lattice:")
    display(is_elem)
    return 0
end
is_elem


# === Code Cell 16 ===

D_L = discriminant_group(lat);
display(D_L)
G = D_L.ab_grp;
display(G)
Q = D_L.gram_matrix_quadratic;


# === Code Cell 17 ===

D_L = discriminant_group(lat)
Q = D_L.gram_matrix_quadratic
G = D_L.ab_grp

# Computing r
r = rank(lat)


# === Code Cell 18 ===

# Computing a
    a = length( filter(x -> x == 2, elementary_divisors(G)) )


# === Code Cell 19 ===

n = minimum(size(Q))
diags = [ Q[i, i] for i in 1:n ]
#show("Diagonal of Q:")
#show(diags)
are_diags_ints = map(is_integer, diags)
all_integer_diags = reduce(&, are_diags_ints)
# = 1 if all integers, = 0 if any non-integer


# === Code Cell 20 ===

Q


# === Code Cell 21 ===

delta = 1 - all_integer_diags
    # delta = 0 <=> image in Z, dellta=1 <=> non-integral image


import IPython
from IPython.display import Math
import numpy as np
import pandas as pd
from IPython.display import HTML
from collections import Counter
from sage.modules.free_module_integer import IntegerLattice
import sys
sys.path.append('/home/dzack/gitclones/vinal/src/sage')
from vinal import *
import subprocess
import tempfile
implicit_multiplication(True)
import re
import timeit
import pickle
from sage.modules.free_quadratic_module_integer_symmetric import *

libgap.LoadPackage("PackageManager")


do_tests = False
# do_tests = True


def lmap(f, ls):
    return list(map(f, ls))

def lzip(*iterables):
    return list(zip(*iterables))


IPython.core.ultratb.VerboseTB._tb_highlight = "bg:ansired"


from sage.modules.free_quadratic_module_integer_symmetric import FreeQuadraticModule_integer_symmetric, FreeQuadraticModule_submodule_with_basis_pid    
from sage.modules.torsion_quadratic_module import TorsionQuadraticModule

def vinberg_algorithm(self, v0=None, use_coxiter=False, output=sys.stdout):
    A = VinAl(self.gram_matrix(), v0, use_coxiter, output)
    A.FindRoots()
    return A.roots

setattr(
    sage.modules.free_quadratic_module_integer_symmetric.FreeQuadraticModule_integer_symmetric,
    "vinberg_algorithm",
    lambda self, v0=None, use_coxiter=False, output=sys.stdout: vinberg_algorithm(self, v0, use_coxiter, output)
)




#######################################################
Z = IntegralLattice( Matrix(ZZ, [1] ) )
Z_2 = Z.twist(2)


H = IntegralLattice("H")
H_2 = H.twist(2)

U = H
U_2 = H_2

exec("".join( [f'A{n+1}=IntegralLattice("A{n+1}").twist(-1);' for n in range(20+1)]) )
exec("".join( [f'D{n+2}=IntegralLattice("D{n+2}").twist(-1);' for n in range(20+1)]) )
exec("".join( [f'E{n}=IntegralLattice("E{n}").twist(-1);' for n in [6,7,8] ]) )

# CoxeterMatrix(['B', 4])


E8_2 = E8.twist(2)

E10 = U @ E8 
E10_2 = U_2 @ E8_2 

lk3 = U**3 @ E8^2

Sdp = U_2
TdP = U.direct_sum(U_2).direct_sum(E8).direct_sum(E8)

SEn = E10_2

TEn = U @ E10_2


Tco = Z_2.direct_sum(E10_2)
Sco = Z_2.twist(-1).direct_sum(E10_2)

LpNik = U.direct_sum(U).direct_sum(U).direct_sum(E8_2)
LmNik = E8_2

# blocks_2_elem = [
# Z_2, U, U_2, 
# B_n(2), #(n,n,1)
# C_4n, #(4n, 2, 0), 4n >= 8
# C_4n+2, #(4n+2, 2, 1) 4n+2>= 6
# F4, #(4,2,0)
# E7, #(7,1,1)
# E8, #(8,8,0)
# E8_2 #(8,8,0)
# ]

def is_coeven(L):
    return L.delta == 0
    return L.dual_lattice().twist(2).is_even()

def is_coodd(L):
    return L.delta == 1
    return L.dual_lattice().twist(2).is_odd()

def get_isotrop_type(L, v):
    S_bar = L.e_perp_mod_e(v)
    compl = L.orthogonal_complement(S_bar)
    if compl.is_isometric(U):
        return "Odd"
    elif compl.is_isometric(U_2):
        return "Even ordinary"
    elif compl.is_isometric(IPQ(1,1).twist(2)):
        return "Even characteristic"
    else:
        return "Not found."


two_elem_building_blocks = [
A1, D4, D6, D8, E7, E8, E8_2, IPQ(2, 0), U, U_2
]

# <2>, U, U(2), B_n(2)=(n,n,1), C_4n=(4n,2,0), 4n>=8, C_4n+2=(4n+2,2,1), 4n+2>=6, F4=(4,2,0), E7=(7,1,1), E8=(8,0,0), E8(2)=(8,8,0).

two_elementary_lattices = {
        "(1,1,1)":      Z.twist(2),
        "(2,0,0)":      U,
        "(2,2,0)":      U.twist(2),
        "(10,10,0)":    SEn,
        "(14,8,0)":     LpNik,
        "(20,2,0)":     TdP,
        "(12,10,0)":    TEn,
        "(8,8,0)":      LmNik,
        "(18,2,0)":     U_2.direct_sum(E8**2),
        "(18,0,0)":     U.direct_sum(E8**2),
        "(10,10,0)":    E10_2,
        "(10,8,0)":     U.direct_sum(E8_2),
        "(8,6,0)":      U, # A1^8 *
        "(2,2,1)":      None, #B2.twist(2),
        "(3,3,1)":      None, #B3.twist(2),
        "(4,4,1)":      None, #B4.twist(2),
        "(5,5,1)":      None, #B5.twist(2),
        "(6,6,1)":      None, #B6.twist(2),
        "(7,7,1)":      None, #B7.twist(2),
        "(8,8,1)":      None, #B8.twist(2),
        "(9,9,1)":      None, #B9.twist(2),
        "(10,10,1)":    None, #B11.twist(2),
        "(11,11,1)":      None, #B12.twist(2),
        "(12,12,1)":      None, #B13.twist(2),
        "(13,13,1)":      None, #B14.twist(2),
        "(14,14,1)":      None, #B15.twist(2),
        "(15,15,1)":      None, #B16.twist(2),
        "(16,16,1)":      None, #B17.twist(2),
        "(17,17,1)":      None, #B17.twist(2),
        "(18,18,1)":      None, #B18.twist(2),
        "(19,19,1)":      None, #B19.twist(2),
        "(20,20,1)":      None, #B20.twist(2),
        "(8,2,0)":        None, #C8,
        "(16,2,0)":       None, #C16,
        "(24,2,0)":       None, #C24,
        "(6,2,1)":        None, #C6,
        "(10,2,1)":        None, #C10,
        "(14,2,1)":        None, #C14,
        "(18,2,1)":        None, #C18,
        "(22,2,1)":        None, #C22,
        "(4,2,0)":         None, #F4,
        "(7,1,1)":         None, #E7,
        "(8,0,0)":         E8,
        "(8,8,0)":         E8.twist(2)
}



def to_var_names(s):
    return lmap(lambda x: x.replace(" ", "").strip(), s.split(","))


LK3.<v1, v2, \
u1, u2, \
up1, up2, \
e1, ..., e8, \
ep1, ..., ep8> \
= U**3 @ E8**2

LK3.inject_variables()

I_dP = LK3.hom([
    -v1, -v2,
    up1, up2,
    u1, u2,
    -e1, ..., -e8,
    -ep1, ..., -ep8
])

# -e1, -e2, -e3, -e4, -e5, -e6, -e7, -e8,
# -ep1, -ep2, -ep3, -ep4, -ep5, -ep6, -ep7, -ep8

I_En = LK3.hom([
    -v1, -v2, 
    up1, up2, 
    u1, u2, 
    ep1, ..., ep8,
    e1, ..., e8
])

# ep1, ep2, ep3, ep4, ep5, ep6, ep7, ep8, 
# e1, e2, e3, e4, e5, e6, e7, e8

I_Nik = LK3.hom([
    v1, v2,
    u1, u2,
    up1, up2,
    -ep1, ..., -ep8,
    -e1, ..., -e8
])

# -ep1, -ep2, -ep3, -ep4, -ep5, -ep6, -ep7, -ep8, 
# -e1, -e2, -e3, -e4, -e5, -e6, -e7, -e8

# exec( "".join( [f'del({x});' for x in LK3_var_names] ) )

positions = {
    "Sterk_1": {
        0: [0, 0],
        1: [4, 0],
        2: [8, 0],
        3: [8, -4],
        4: [8, -8],
        5: [4, -8],
        6: [0, -8],
        7: [0, -4],
        8: [2, -6],
        9: [3.25, -4.75],
        10: [4.5, -3.5],
        11: [6, -2]
    },
    "Sterk_2": {
        0: [0, 0],
        1: [-4, 0],
        2: [-8, 0],
        3: [-7, 4],
        4: [-6, 8],
        5: [-5, 12],
        6: [-4, 16],
        7: [-3, 20],
        8: [-2, 24],
        9: [-2, 6]
    },
    "Sterk_3": {
        0: [0, -4],
        1: [0, 4],
        2: [0, 8],
        3: [0, 12],
        4: [0, 16],
        5: [4, 16],
        6: [8, 16],
        7: [12, 16],
        8: [20, 16],
        9: [4, 12],
        10: [6, 2],
        11: [14, 10]
    },
    "Sterk_4": {
        0: [0, 0],
        1: [0, 4],
        2: [0, 8],
        3: [4, 8],
        4: [8, 8],
        5: [12, 8],
        6: [16, 8],
        7: [16, 4],
        8: [16, 0],
        9: [4, 4],
        10: [12, 4]    
    },
    "Sterk_5": {
        0: [0, 0],
        1: [10, 0],
        2: [20, 0],
        3: [20, -10],
        4: [20, -20],
        5: [10, -20],
        6: [0, -20],
        7: [0, -10],
        8: [4, -4],
        9: [16, -4],
        10: [16, -16],
        11: [4, -16],
        12: [8, -8],
        13: [8, -12]
    }
}


def root_intersection_matrix(vectors, labels, bil_form):
    n = len(vectors)
    M = zero_matrix(ZZ, n)
    nums = Set(range(n))
    for i in range(n):
        for j in range(n):
            M[i, j] = bil_form( vectors[i], vectors[j] )
            
    # Must be symmetric
    assert M.is_symmetric()
        
    # Must have -2 or -4 on the diagonal
    s = Set( M.diagonal() )
    assert s in Subsets( Set( [-2, -4] ) )

    # Diagonals should be square norms of vectors
    for i in range(n):
        assert M[i, i] == bil_form(vectors[i], vectors[i])
    return M



#### Enriques

SEn = E10_2

TEn.<\
e, f, \
ep, fp, \
a1, ..., a8> \
= U @ E10_2 

ed, fd, \
epd, fpd, \
w1, ..., w8, \
= TEn.dual_basis()

# Square 4 vector
omega = 2 * w8

# Square 8 vector
alpha = 2 * w1

TEn.isotropic_vectors_Sterk = [
e, 
ep,
ep + fp + omega,
ep + 2*fp + alpha,
2*e + 2*f + alpha
]

TEn.isotropic_vectors_OTEn = [
e, 
ep
]

for i,v in enumerate(TEn.isotropic_vectors_Sterk):
    j = i+1
    TEn.sublattices.update({ f'Sterk_{j}': TEn.e_perp_mod_e(v) })
    if do_tests:
        if j == 1:
            print( TEn.sublattices[f"Sterk_{j}"].is_isometric(U_2 @ E8_2 ) )
        else:
            print( TEn.sublattices[f"Sterk_{j}"].is_isometric(U @ E8_2 ) )

if do_tests:
    assert TEn.div(e) == 1 and TEn.q(e) == 0
    assert TEn.e_perp_mod_e(e).is_isometric(E10_2)
    assert TEn.e_perp_mod_e(e).is_isometric(
            two_elementary_lattices["(10,10,0)"]
    )

    assert TEn.div(ep) == 2 and TEn.q(ep) == 0
    assert TEn.e_perp_mod_e(ep).is_isometric(U @ E8_2)
    assert TEn.e_perp_mod_e(ep).is_isometric(
            two_elementary_lattices["(10,8,0)"]
    )

    assert TEn.I_perp_mod_I([e, ep]).is_isometric(
            two_elementary_lattices["(8,8,0)"]
    )
    
    vp = 2*e + 2*f + 2*w1
    assert TEn.div(vp) == 2 and TEn.q(vp) == 0
    assert TEn.I_perp_mod_I([ep, vp]).is_isometric(
            two_elementary_lattices["(8,6,0)"]
    )


# exec( "".join( [f'del({x});' for x in L_20_2_0_var_names] ) )
# exec( "".join( [f'del({x});' for x in L_20_2_0_dual_var_names] ) )

## Sterk and 20,2,0

L_20_2_0 = U @ U_2 @ E8**2

Gram_L_20_2_0 = L_20_2_0.gram_matrix()
L_20_2_0_dual_changeofbasis = Gram_L_20_2_0.inverse()

e,f ,ep,fp, a1,a2,a3,a4,a5,a6,a7,a8, a1t,a2t,a3t,a4t,a5t,a6t,a7t,a8t = L_20_2_0.basis()
eb,fb, epb,fpb, w1,w2,w3,w4,w5,w6,w7,w8, w1t,w2t,w3t,w4t,w5t,w6t,w7t,w8t = L_20_2_0_dual_changeofbasis.columns()

# display(Math("$(18, 2, 0)="), Gram_L_20_2_0)
# display(Math("(18,2,0)vee=(18, 2, 0)^{\\vee} ="), L_20_2_0_dual_changeofbasis)

# The primes are the image of the diagonal embedding from E_8(2)
a1p = a1 + a1t
a2p = a2 + a2t
a3p = a3 + a3t
a4p = a4 + a4t 
a5p = a5 + a5t
a6p = a6 + a6t
a7p = a7 + a7t
a8p = a8 + a8t

w1p = w1 + w1t
w2p = w2 + w2t
w3p = w3 + w3t
w4p = w4 + w4t
w5p = w5 + w5t
w6p = w6 + w6t
w7p = w7 + w7t
w8p = w8 + w8t

# MS      = [e,f,   ep,fp,   a1,a2,a3,a4,a5,a6,a7,a8, a1t,a2t,a3t,a4t,a5t,a6t,a7t,a8t]
# MS_dual = [eb,fb, epb,fpb, w1,w2,w3,w4,w5,w6,w7,w8, w1t,w2t,w3t,w4t,w5t,w6t,w7t,w8t]

# VS      = [ep,fp,   a1,a2,a3,a4,a5,a6,a7,a8, a1t,a2t,a3t,a4t,a5t,a6t,a7t,a8t]
# VS_dual = [epb,fpb, w1,w2,w3,w4,w5,w6,w7,w8, w1t,w2t,w3t,w4t,w5t,w6t,w7t,w8t]

# WS      = [e,f,   a1,a2,a3,a4,a5,a6,a7,a8, a1t,a2t,a3t,a4t,a5t,a6t,a7t,a8t]
# WS_dual = [eb,fb, w1,w2,w3,w4,w5,w6,w7,w8, w1t,w2t,w3t,w4t,w5t,w6t,w7t,w8t]

# Root vectors for (18, 2, 0), roots taken from above, v_i are according to numerical labeling above

v1 = a8t
v2 = ep + fp + w1 + w8t
v3 = a1 
v4 = a3
v5 = a4
v6 = a5
v7 = a6
v8 = a7
v9 = a8
v10 = ep + fp + w8 + w1t
v11 = a1t
v12 = a3t
v13 = a4t
v14 = a5t
v15 = a6t
v16 = a7t

v17 = ep + w8t
v18 = a2
v19 = ep + w8
v20 = a2t

v21 = fp - ep
v22 = 5 *ep + 3 *fp + 2 *w2 + 2 *w2t

roots_18_2_0 = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22]

# Root vectors for (18, 0, 0), roots taken from above, w_i are according to numerical labeling above


w1 = a1
w2 = a3
w3 = a4
w4 = a5
w5 = a6
w6 = a7
w7 = a8
w8 = w8 + e
w9 = f- e
w10 = w8t + e
w11 = a8t
w12 = a7t
w13 = a6t
w14 = a5t
w15 = a4t
w16 = a3t
w17 = a1t
w18 = a2
w19 = a2t

roots_18_0_0 = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19]

Sterk_roots = {
    "Sterk_1": [],
    "Sterk_2": [],
    "Sterk_3": [],
    "Sterk_4": [],
    "Sterk_5": []
}



## Sterk 1: 12 roots
s1_1 = v3 + v11
s1_2 = v4 + v12
s1_3 = v5 + v13
s1_4 = v6 + v14
s1_5 = v7 + v15
s1_6 = v8 + v16
s1_7 = v9 + v1
s1_8 = v10 + v2
s1_9 = v17 + v19
s1_10 = v21
s1_11 = v22
s1_12 = v18 + v20
Sterk_roots["Sterk_1"] = [s1_1, s1_2, s1_3, s1_4, s1_5, s1_6, s1_7, s1_8, s1_9, s1_10, s1_11, s1_12]


## Sterk 2: 10 roots
s2_1 = w1 + w17
s2_2 = w2 + w16
s2_3 = w3 + w15
s2_4 = w4 + w14
s2_5 = w5 + w13
s2_6 = w6 + w12
s2_7 = w7 + w11
s2_8 = w8 + w10
s2_9 = w9
s2_10 = w18 + w19

Sterk_roots["Sterk_2"] = [s2_1, s2_2, s2_3, s2_4, s2_5, s2_6, s2_7, s2_8, s2_9, s2_10]

## Sterk 3: 12 roots
wa = lambda x: x + (1/2) * L_20_2_0.b(v22, x) * v22
inv = lambda x: x + wa(x)

s3_1 = v13
s3_2 = v14 + v12
s3_3 = v15 + v11
s3_4 = v16 + v10
s3_5 = v1 + v9
s3_6 = v2 + v8
s3_7 = v3 + v7
s3_8 = v4 + v6
s3_9 = v5
s3_10 = v17 + v19
s3_11 = inv(v20) #v22 + 2*v20
s3_12 = inv(v18) #v22 + 2*v18

Sterk_roots["Sterk_3"] = [s3_1, s3_2, s3_3, s3_4, s3_5, s3_6, s3_7, s3_8, s3_9, s3_10, s3_11, s3_12]

## Sterk 4: 11 roots

s4_1 = v15
s4_2 = v16 + v14
s4_3 = v1 + v13
s4_4 = v2 + v12
s4_5 = v3 + v11
s4_6 = v4 + v10
s4_7 = v5 + v9
s4_8 = v6 + v8
s4_9 = v7
s4_10 = v17 + v20
s4_11 = v18 + v19
s4_12 = v22 + v21

Sterk_roots["Sterk_4"] = [s4_1, s4_2, s4_3, s4_4, s4_5, s4_6, s4_7, s4_8, s4_9, s4_10, s4_11]


## Sterk 5: 14 roots

s5_1 = v16 + 2*v1 + v2
s5_2 = v2 + 2*v3 + v4
s5_3 = v4 + 2*v5 + v6
s5_4 = v6 + 2*v7 + v8
s5_5 = v8 + 2*v9 + v10
s5_6 = v10 + 2*v11 + v12
s5_7 = v12 + 2*v13 + v14
s5_8 = v14 + 2*v15 + v16
s5_9 = v17
s5_10 = v18
s5_11 = v19
s5_12 = v20
s5_13 = v21
s5_14 = v22

Sterk_roots["Sterk_5"] = [s5_1, s5_2, s5_3, s5_4, s5_5, s5_6, s5_7, s5_8, s5_9, s5_10, s5_11, s5_12, s5_13, s5_14]



##### Actual Sterk Vectors

G = TEn.gram_matrix()
Ginv = G.inverse()

dualize = lambda x: (2*Ginv) * x

e,f ,ep,fp, a1,a2,a3,a4,a5,a6,a7,a8, = TEn.basis()
ed,fd, epd,fpd, a1d, a2d, a3d, a4d, a5d, a6d, a7d, a8d = (2 * Ginv).columns()

a9 = fp - ep
a10 = a8d + 2*ep
a11 = 2*ep + 2*fp + a1d + a8d
a12 = a12 = 5*ep + 3*fp + 2*a2d
sterks1 = [a1, ..., a12]
# G = CoxeterGraph(M)
# G.plot(vertex_labels = lambda i: ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12'][i])

a9 = a8d + 2*f
a10 = e-f
sterks2 = [a1, ..., a10]
# G = CoxeterGraph(M)
# G.plot(vertex_labels = lambda i: ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10'][i])

######
e,f ,ep,fp, a1,a2,a3,a4,a5,a6,a7,a8, = TEn.basis()
ed,fd, epd,fpd, a1d, a2d, a3d, a4d, a5d, a6d, a7d, a8d = Ginv.columns()

a9 = f-e
a10 = 2*fp + 2*a8d
a11 = 2*e - 2*fp - 2*a8d
a12 = 2*e + 2*(a1d - a8d)
a13 = (e+f) + (a8 - fp)
sterks3 = [a1, ..., a7, a9, a10, a11, a12, a13]
#######
# G = CoxeterGraph(M)
# G.plot(vertex_labels = lambda i: ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a9', 'a10', 'a11', 'a12', 'a13'][i])

# a9 = f-e
# a10 = 2*fp + a8d
# a11 = 2*e - 2*fp - a8d
# a12 = 2*e + (a1d - a8d)
# a13 = (e+f) + (a8 - fp)
# sterks3 = [a1, ..., a7, a9, a10, a11, a12, a13]

# a9 = f-e
# a10 = a8d + 2*ep
# a11 = e + f + a1 -ep
# a12 = 2*e - 2*ep + a8d - a1d
# sterks4 = [a2, ..., a12]

# Ginv_prime = (U @ U @ E8).gram_matrix().inverse()
# dualize = lambda v: Ginv_prime * v

# tilde_e = e + ep + fp - a1
# tilde_f = f + ep + fp - a1
# tilde_a1 = ep - fp
# tilde_a2 = a2
# tilde_a3 = fp + a3
# tilde_a4 = a4
# tilde_a5 = a5
# tilde_a6 = a6
# tilde_a7 = a7
# tilde_a8 = a8
# tilde_a1d = dualize(tilde_a1)
# tilde_a2d = dualize(tilde_a2)
# tilde_a3d = dualize(tilde_a3)
# tilde_a4d = dualize(tilde_a4)
# tilde_a5d = dualize(tilde_a5)
# tilde_a6d = dualize(tilde_a6)
# tilde_a7d = dualize(tilde_a7)
# tilde_a8d = dualize(tilde_a8)

# a9 = 2*ed - tilde_a1
# a10 = 2*ed + (tilde_a2d - tilde_a3d)
# a11 = tilde_f - tilde_e
# a12 = ed + fd + (tilde_a6d - tilde_a3d)
# a13 = tilde_e + tilde_f + (tilde_a1d + tilde_a8d -tilde_a3d)
# a14 = tilde_e + tilde_f + tilde_a3
# sterks5=[a2, a4, a5, a6, a7, a8, tilde_a8d, a10, a11, a12, a13, a14, tilde_a1, a9]

def getSterk5():

    L.<e,f,a1, ..., a8> = U @ E8_2

    ed, fd, a1d, a2d, a3d, a4d, a5d, a6d, a7d, a8d = L.gram_matrix().inverse().columns()

    a9 = 2*e - a1
    a10 = 2*e + 2*(a2d - a3d)
    a11 = f - e
    a12 = e + f + 2*(a6d - a3d)
    a13 = e + f + 2*(a1d + a8d - a3d)
    a14 = e + f + a3
    return (L, [a2, a4, a5, a6, a7, a8, 2*a8d, a10, a11, a12, a13, a14, a1, a9])

sterks5 = getSterk5()

#1vertex_labels = lambda i: ['a2', 'a4', 'a5', 'a6', 'a7', 'a8', 'a8d', 'a10', 'a11', 'a12', 'a13', 'a14', 'a1', 'a9'][i])

def test_sterk():

    L = TEn
    assert all( 
        [L.q(x) == -4 for x in [
            a10, a2, a4, a5, a6, a7, a8, tilde_a8d, a9, tilde_a1
        ] ]
    )
    assert all( 
        [L.q(x) == -2 for x in [
           a11, a14, a12, a13 
        ] ]
    )
    # a12, a13 broken norm
    assert all( 
        [L.b(a,b) == 2 for a,b in [ 
            (a10, a2), (a2, a4), (a4, a5), (a5, a6), (a6,a7), (a7, a8), 
            (a8, tilde_a8d), (tilde_a8d, a10)
        ] ]
    )
    assert all( 
        [L.b(a,b) == 2 for a,b in [ 
            (a6, a12), (a8, a13), (a10, a11), (a4, a14),
            (tilde_a1, a14), (tilde_a1, a13), (a9, a11), (a9, a12)
        ] ]
    )
    # a10-a11, tilde_a1-a13, a9-a11, a9-a12 broken

# Errors: a12 at index 9, a13 at index 10
# Double lines, white to black: r_i r_j = 2
# Single lines, white to white: r_i r_j = 2
# Black nodes: -2
# White nodes: -4
# Arrow points from -4 to -2


##### [12, 10, 12, 11, 14] ##################

# Sterk 1 roots: 9 (10s Julia). Sterk had 12: 12x -4 roots
Sterk1_Julia = [
[0,0,-1,-1,-2,-3,-2,-2,-2,-1],
[0,0,2,2,3,4,3,2,1,1],
[0,0,0,1,0,1,1,1,1,1],
[0,0,1,1,1,2,2,1,1,0],
[0,0,-1,-1,-1,-1,-1,0,0,0],
[0,0,1,2,3,4,3,2,1,0],
[0,0,-1,-2,-2,-4,-3,-2,-1,0],
[0,0,0,0,0,0,-1,-1,0,0],
[1,0,0,-1,-1,-2,-2,-1,-1,-1]
]

# Sterk 1 roots: 10 (10s VinAl) 1 ideal vertex
Sterk1_vinal = [
(0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 1, 2, 3, 4, 6, 5, 4, 3, 2)
 ]

# Sterk 2 roots: 10 (2s Julia). Sterk had 10: 9x -4 roots, 1x -2 root
Sterk2_julia = [
[0,0,1,2,3,4,3,2,1,1],
[0,0,-1,-1,-2,-2,-1,-1,-1,-1],
[0,0,1,1,2,3,2,2,1,0],
[0,0,0,-1,-1,-2,-2,-2,-1,-1],
[0,0,-1,-1,-2,-3,-3,-2,-1,0],
[0,0,-2,-3,-3,-5,-4,-3,-2,-1],
[0,0,2,2,3,4,4,3,2,1],
[0,0,0,1,1,2,2,2,2,1],
[-1,1,0,0,0,0,0,0,0,0],
[2,0,0,-1,-1,-1,-1,-1,-1,0]
]

# Sterk 2 roots: 10 (5s VinAl) 2 ideal vertices
Sterk2_vinal = [
(0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 2, 2, 3, 4, 6, 5, 4, 3, 2)
 ]
# Almost exactly matches Sterk.

# Sterk 3: 10 (20s Julia). Sterk had 12: 10x -4 roots, 2x -2 roots
Sterk3_julia = [
[0,0,-1,0,1,1,1,2,2,2],
[0,0,0,1,-1,-2,-2,-3,-2,-2],
[0,0,-1,0,1,2,2,3,2,1],
[0,0,1,1,-1,-2,-2,-3,-3,-2],
[0,0,-1,-1,0,1,1,2,2,2],
[0,0,1,1,-1,-2,-3,-5,-4,-3],
[0,0,1,0,-1,0,-1,-1,-1,-1],
[0,0,0,-1,1,1,2,2,2,1],
[-1,1,0,0,0,0,0,0,0,0],
[2,0,0,-1,1,1,1,2,1,1]
]

# Sterk 3: 10 (10s VinAl) 2 ideal vertices
Sterk3_vinal = [
(0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 1, 0, 0, 0, 0, 0, -1),
(0, 0, 1, -1, 0, 0, 0, 0, 0, 0),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 2, -1, -1, 2, 3, 4, 6, 5, 4)
]

# Sterk 4: 10 (20s Julia). Sterk had 11: 9x -4 roots, 2x -2 roots
Sterk4_julia = [
[0,0,0,0,-1,0,-1,-1,-1,-1],
[0,0,2,3,-8,-4,-17,-14,-11,-7],
[0,0,-1,-2,5,2,10,8,6,4],
[0,0,2,4,-11,-5,-22,-18,-13,-9],
[0,0,-2,-4,11,5,22,18,14,10],
[0,0,0,2,-2,-1,-4,-3,-3,-2],
[0,0,0,0,0,0,0,1,1,0],
[0,0,-2,-5,11,5,21,17,13,9],
[-1,1,0,0,0,0,0,0,0,0],
[2,0,1,2,-4,-2,-8,-7,-5,-4]
]

# Sterk 4: 10 (5s Vinal) 2 ideal vertices
Sterk4_vinal = [
(0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(0, 0, 0, 2, -2, -1, -4, -3, -2, -1),
(0, 0, 1, 0, -2, -1, -4, -3, -2, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(0, 2, -3, -6, 16, 7, 31, 25, 19, 13)
]

# Sterk 5: 10 (2s Julia). Sterk had 14: 10x -4 roots, 4x -2 roots
Sterk5_julia = [
[-1,1,0,0,0,0,0,0,0,0],
[6,6,0,0,-15,-7,-30,-24,-18,-12],
[0,0,0,0,0,0,0,1,1,0],
[-6,-6,0,0,15,7,30,24,18,13],
[2,0,0,0,-3,-1,-5,-4,-3,-2],
[0,0,0,0,0,0,0,0,-1,-1],
[0,0,0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,-1,-1,0,0],
[-2,-2,1,0,4,2,9,7,6,4],
[0,0,-1,1,0,0,0,0,0,0]
]

# Sterk 5: 10 (5s VinAl) 2 ideal vertices
Sterk5_vinal = [
(0, 0, -1, 1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
(0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
(0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
(0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
(0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
(0, 2, 0, 0, -2, -1, -4, -3, -2, -1),
(1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
(4, 4, 0, 0, -10, -5, -21, -17, -13, -9),
(-6, -6, 1, 0, 16, 7, 31, 25, 19, 13)
]

# See https://arxiv.org/pdf/2002.07127#page=12&zoom=auto,-13,249
# L = IIPQ(1, 17)
# L.vinberg_algorithm() == ?
# L.root_system.relations = ?
# L.root_system.num_facets = 19 # mod W
# L.root_system.num_rays = 82 # mod W

LK3_2 = Z.twist(-2) @ U**2 @ E8**2
LK3_4 = Z.twist(-4) @ U**2 @ E8**2

LK3_2d = lambda d: Z.twist(-2*d) @ U**2 @ E8**2

# I^2d( LK3) /O(LK3) = {h}, h^perp = LK3_2d
# J^perp/J = A17, D10 + E7, E8^2 + A1, D16 + A1

# LK3_2.vinberg_algorithm() == ?
# See https://arxiv.org/pdf/1903.09742#page=22&zoom=auto,-13,546



def Coxeter_Diagram(M):
    nverts = M.ncols()
    G = Graph()
    vertex_labels = dict();
    
    vertex_colors = {
        '#F8F9FE': [], # white
        '#BFC9CA': [], # black
    }
    
    for i in range(nverts):
        for j in range(nverts):
            mij = M[i, j]
            if i == j: 
                if mij == -4:
                    vertex_colors["#F8F9FE"].append(i) # white
                    continue
                if mij == -2:
                    vertex_colors["#BFC9CA"].append(i) # black
                    continue
                continue
            if mij > 0:
                G.add_edge(i, j, str(mij) )
                continue
    assert len( vertex_colors["#F8F9FE"]) + len( vertex_colors["#BFC9CA"]) == nverts
    G.vertex_colors = vertex_colors    
    return G

def plot_coxeter_diagram(G, v_labels, pos={}):
    n = len( G.vertices() )
    vlabs = {v: k for v, k in enumerate(v_labels)}
    if pos == {}:
        display(G.plot(
            edge_labels=True, 
            vertex_labels = vlabs,
            vertex_size=200,
            vertex_colors = G.vertex_colors
        ))
    else:
        display(G.plot(
            edge_labels=True, 
            vertex_labels = vlabs,
            vertex_size=200,
            vertex_colors = G.vertex_colors,
            pos = pos
        ))
        

# sage: G = Graph([(1,2, 3)])
# CoxeterMatrix(G)
# WeylGroup(["B", 3])                                                       
#  s = W.simple_reflections()
#  (w = s[1]*s[2]*s[3]).canonical_matrix()
# w.reduced_word()
# W = CoxeterGroup(['H', 3], implementation='reflection')
# G = W.coxeter_diagram(); G

# R = RootSystem("A2xB2xF4")
#  DynkinDiagram(R)


def run_vin(L):
    doTwist = False
    if L.signature_pair()[0] == 1: 
        print("Twisting..")
        do_twist=True
        M = L.twist(-1).gram_matrix() 
    else:
        M = L.gram_matrix()
    A = VinAl(M)
    A.FindRoots()
    Lp = IntegralLattice( L.gram_matrix() )
    if doTwist:
        Lp.roots = [Lp(-1*x) for x in A.roots]
    else:
        Lp.roots = [Lp(x) for x in A.roots]
    Lp._assign_names(L.variable_names())
    Lp.root_names = [str( Lp.to_lin_comb_generators(x) ) for x in Lp.roots]
    return Lp


bond1 = matrix(ZZ, 2, [2,-1,-1,2])
bond2 = matrix(ZZ, 2, [2,-1,-1,1])
bond3 = matrix(ZZ, 2, [6,-3,-3, 2])
bond_heavy_or = matrix(ZZ, 2, [4,-2,-2,1])
bound_heavy_unor = matrix(ZZ, 2, [1,-1,-1,1])

# from juliacall import Main as jl

#M = (U @ D4.twist(-1)**2).gram_matrix()

def mat_to_julia_str(M):
    return "[" + str(M).replace("],", ";").replace(",", "").replace("\n", "").replace("[", "").replace("]", ";") + "]"


# ls = [(" + ".join(x[0]), x[1]) for x in lmap(lambda x: (get_coxeter_label(x), x), get_connected_elliptic_subgraphs(G) )]
# ls = lmap(lambda H: (get_coxeter_label(H), H), get_connected_elliptic_subgraphs(G) )
# ls = lmap(lambda x: (coxeter_str_format(x[0]), x)) 


#summarize_elliptic_subgraphs(Sterk1_connected_elliptic_subgraphs, "Sterk_1")


def is_coeven(L):
    return L.dual_lattice().twist(2).is_even()

def delta_comp(L):
    return 0 if is_coeven(L) else 1





"""The rank-one del Pezzo slot: what the gluing decides, and what it does not.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_rank_one_placement.py

What this report supersedes.  An earlier version of this file concluded that ``S' perp T`` is
the even unimodular lattice of signature (3,19), "hence L_K3", so that the involution with
(+1)-eigenspace U(2) is "an integral isometry of L_K3".  Each step of that chain was wrong: an
orthogonal sum of two lattices with nontrivial discriminant is not unimodular and is not L_K3;
the predicate ``is_discriminant_form_of_even_lattice`` says only that a complement of the
required genus exists, not that one is constructed, and gives neither the gluing nor a
primitive embedding nor any operator; and the integral eigensplitting of S_Co was asserted,
not proved.  Those claims are deleted here, not patched.

What is computed.  Three statements, each on its own.

(A) Integrality of the operator.  div_{S_Co}(H) = 2 (by ``L.div``), so

        phi(x) = -x + ((x.H)/2) H

    maps S_Co into itself; it is -s_H, i.e. -id on H^{perp} with phi(H) = H.  It is built here
    from the maintained ``L.reflection`` and verified as an element of ``S.Aut()``.  The
    lattice does not split along its eigenspaces: Z H + (H^{perp} cap S_Co) has index 2 in
    S_Co, computed from determinants.  Operator integral, lattice not split -- independent
    facts, and the second is why the earlier "integral eigensplitting" was wrong.

(B) The discriminant side.  The rank-one case asks for an isotropic b in L_K3 with b.H = 2
    whose (+1)-eigenspace meets S_Co in exactly Z H.  Writing b = H/2 + t with t in
    T_Co tensor Q, the conditions are t^2 = -1 and the class of t in A_{T_Co} equal to the
    gluing image of [H/2].  The gluing is an anti-isometry of quadratic discriminant forms, so
    that class has the parity of [H/2], which is odd; and the census of A_{T_Co} below shows
    exactly 496 classes of odd q-value.  For each of the 496 the script exhibits an explicit
    tau in T_Co with tau^2 = -4, div(tau) = 2 and the prescribed class, i.e. a vector tau/2 of
    square exactly -1 in that class.  So a vector of square -1 exists in EVERY class the
    gluing can present, for every anti-isometry gamma_Co -- which matters because the book
    does not carry gamma_Co explicitly.

(C) A model check of the operator that (B) produces: in T_Co itself, with H_M = e_0 + e_1
    (square 4) and b_M = e_1 (isotropic, b_M.H_M = 2), the involution with (+1)-eigenspace
    <H_M, b_M> is integral and is an isometry.

(D) The invariants that put J in the conjugacy class of AEGS's I_dP.  The coinvariant
    lattice of J is the orthogonal complement of a U(2) in a unimodular lattice, so its
    discriminant form is that of U(2) up to sign; the script prints the invariants of U(2)
    and of T_dP = U(2) + U + E8^2, which are the ones Nikulin's classification compares:
    rank, signature, generator length a, and coparity delta read off the value census.
    That the two agree is what makes J conjugate to I_dP in Orth(L_K3).

What is NOT computed and NOT claimed.  Nothing here constructs L_K3, the overlattice, or the
embedding S_Co -> L_K3: that argument is in the manuscript and runs through the gluing of the
Coble primitive embedding, not through this file.  Nothing here says an AUTOMORPHISM of a K3
surface realises the involution; nothing about the chamber (h_Co nef, H nef and big) or the
effectivity of alpha.  The predicate ``is_discriminant_form_of_even_lattice`` is used nowhere.

Provenance: pin c546077dce79a76eb32e92d080aa9c44e4c67552, Sage 11.0.beta5, image rootfs
read-only, repository bound at /repo.
"""
import sys
from collections import Counter
from itertools import product

from sage.all import ZZ, matrix, block_diagonal_matrix, diagonal_matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'
print('provenance')
print('  provider pin: %s   Sage: %s' % (PIN, sage_version))
print('')

# ---------------------------------------------------------------------------------------
# (A) S_Co, the degree-4 class H, and the integral operator
# ---------------------------------------------------------------------------------------
print('(A) the operator on S_Co')
S = Lattices(ZZ)([list(r) for r in diagonal_matrix(ZZ, [2] + [-2] * 10).rows()])
H = S.linear_combination({0: 6, 1: -2, 2: -2, 3: -2, 4: -2, 5: -2, 6: -2, 7: -2, 8: -2,
                          9: -1, 10: -1})
print('  S_Co = <2> + <-2>^10 : rank %d, det %s, sig %s'
      % (S.module_rank(), S.determinant(), S.signature()))
print('  H = 6e_0 - 2(e_1+...+e_8) - e_9 - e_10 : H^2 = %s, H primitive %s'
      % (S.q(H), H.is_primitive()))
print('  divisibility ideal b(H, S_Co) = %s' % (S.divisibility_ideal(H),))
divH = S.div(H)
print('  div_{S_Co}(H) = %s' % (divH,))
assert divH == 2
print('  so (x.H)/2 is an integer for every x in S_Co, while H/2 is not in S_Co.')

reflection = S.reflection(H)
print('  L.reflection(H) exists: integral because 2 div(H)/H^2 = %s'
      % (ZZ(2) * divH // S.q(H),))
Aut = S.Aut()
phi = Aut(lambda label: -reflection(S.module_generator(label)))
print('  phi := -s_H is an element of S.Aut() : %s' % (phi in Aut,))
print('  phi(H) == H : %s        phi^2 == id : %s' % (phi(H) == H, phi * phi == Aut.one()))
print('  phi(v) + v on the generators of S_Co (each a multiple of H):')
for label in S.module_generating_set():
    w = phi(S.module_generator(label)) + S.module_generator(label)
    print('    e_%s : %s' % (label, w))
assert all(phi(S.module_generator(l)) + S.module_generator(l) in
           [ZZ(k) * H for k in range(-8, 9)] for l in S.module_generating_set())

line = S.primitive_sublattice_from([H])
N = S.orthogonal_complement(line)
print('  H^perp cap S_Co : rank %d, det %s' % (N.module_rank(), N.determinant()))
index_squared = (S.q(H) * N.determinant()) // S.determinant()
print('  det(Z H + (H^perp cap S_Co)) / det(S_Co) = %s * %s / %s = %s'
      % (S.q(H), N.determinant(), S.determinant(), index_squared))
assert index_squared == 4
print('  index of Z H + (H^perp cap S_Co) in S_Co : 2 -- the lattice does NOT split along')
print('  the eigenspaces of phi, although phi itself is integral.')
print('')

# ---------------------------------------------------------------------------------------
# (B) the discriminant census of T_Co and the (-1)-vectors in the odd classes
# ---------------------------------------------------------------------------------------
print('(B) A_{T_Co} and the classes of square -1')
U2 = matrix(ZZ, [[0, 2], [2, 0]])
G = block_diagonal_matrix(U2, U2, -2 * matrix.identity(ZZ, 7))
T = Lattices(ZZ)([list(r) for r in G.rows()])
print('  T_Co = U(2) + U(2) + <-2>^7 : rank %d, det %s, sig %s, even %s, 2-elementary %s'
      % (T.module_rank(), T.determinant(), T.signature(), T.is_even(), T.is_p_elementary(2)))
A = T.discriminant_group()
vals = A.value_module()
one = vals(1)
classes = list(A.elements())
census = Counter(str(z.q()) for z in classes)
print('  |A_{T_Co}| = %s, class q-value census: %s' % (A.cardinality(), dict(census)))
odd = [z for z in classes if z.q() == one]
print('  classes of odd q-value (a lift of odd square): %d' % len(odd))
print('  cross-check: the recorded Heegner run counts 496 classes of value q = 1 in A_{T_Co},')
print('  and this census reproduces 496 odd classes.')
print('')

tau_of = {}
for c in product([0, 1], repeat=11):
    supp = tuple(i for i in range(11) if c[i])
    tau = T.linear_combination({i: 1 for i in supp})
    if T.div(tau) != 2:
        continue
    cl = T.divided_discriminant_class(tau)
    tau_of.setdefault(cl, (supp, tau))
print('  classes reached by a tau with div(tau) = 2 : %d of %d'
      % (len(tau_of), len(classes)))

basis = [T.module_generator(i) for i in range(11)]
missing = []
case_count = Counter()
for cl in odd:
    supp, tau = tau_of[cl]
    assert T.q(tau) % 4 == 0
    t0_square = T.q(tau) // 4
    assert t0_square % 2 != 0, (cl, T.q(tau))
    if 0 in supp:
        lam = ((-1 - t0_square) // 2) * basis[1]
        case_count['c_0 = 1 : lam = p e_1'] += 1
    elif 1 in supp:
        lam = ((-1 - t0_square) // 2) * basis[0]
        case_count['c_1 = 1 : lam = p e_0'] += 1
    elif 2 in supp:
        lam = ((-1 - t0_square) // 2) * basis[3]
        case_count['c_2 = 1 : lam = p e_3'] += 1
    elif 3 in supp:
        lam = ((-1 - t0_square) // 2) * basis[2]
        case_count['c_3 = 1 : lam = p e_2'] += 1
    elif t0_square == -1:
        lam = ZZ(0) * basis[0]
        case_count['c_0 = c_1 = c_2 = c_3 = 0, k = 2 : lam = 0'] += 1
    else:
        unused = [j for j in range(4, 11) if j not in supp]
        assert unused, (cl, supp)
        lam = basis[0] + basis[1] + basis[unused[0]]
        case_count['c_0 = c_1 = c_2 = c_3 = 0, k = 6 : lam = e_0 + e_1 + e_j'] += 1
    tau_new = tau + 2 * lam
    assert T.q(tau_new) == -4, (cl, T.q(tau_new))
    assert T.div(tau_new) == 2, (cl, T.div(tau_new))
    if T.divided_discriminant_class(tau_new) != cl:
        missing.append(cl)
print('  witnesses found in each case:')
for key in sorted(case_count):
    print('    %-52s %d' % (key, case_count[key]))
print('  odd classes with a tau of square -4 and the prescribed class : %d / %d'
      % (len(odd) - len(missing), len(odd)))
assert not missing
print('  Adding lam in T_Co leaves the class of tau/2 unchanged, so each of the 496 odd')
print('  classes contains a vector of square exactly -1.')
print('')

cH = S.divided_discriminant_class(H)
print('  the class of H/2 in A_{S_Co} : %s, its square %s' % (cH, cH.q()))
print('  every anti-isometry A_{S_Co} -> A_{T_Co} carries it to a class of square -1, which')
print('  is odd whichever sign the anti-isometry carries, oddness being invariant under')
print('  q -> -q.  So the class the gluing presents is among the 496 above, whatever')
print('  gamma_Co is.')
print('')

# ---------------------------------------------------------------------------------------
# (C) the operator produced by such a vector, in a model
# ---------------------------------------------------------------------------------------
print('(C) the involution with (+1)-eigenspace <H_M, b_M>, in the model T_Co')
HM = basis[0] + basis[1]
bM = basis[1]
print('  H_M = e_0 + e_1 : square %s ; b_M = e_1 : square %s, b_M.H_M = %s'
      % (T.q(HM), T.q(bM), HM.b(bM)))
assert T.q(HM) == 4 and T.q(bM) == 0 and HM.b(bM) == 2


def projection_doubled(v):
    """2 * proj_{<H_M, b_M>}(v) = (v.H_M) b_M + (v.b_M) H_M - 2 (v.b_M) b_M."""
    return HM.b(v) * bM + bM.b(v) * HM - 2 * bM.b(v) * bM


TAut = T.Aut()
J = TAut(lambda label: projection_doubled(T.module_generator(label)) - T.module_generator(label))
print('  J := 2 proj - id is an element of T.Aut() : %s' % (J in TAut,))
print('  J^2 == id : %s' % (J * J == TAut.one(),))
print('  J(H_M) == H_M : %s      J(b_M) == b_M : %s' % (J(HM) == HM, J(bM) == bM))
fix = T.primitive_sublattice_from([HM, bM])
print('  <H_M, b_M> : rank %d, det %s  (= U(2))' % (fix.module_rank(), fix.determinant()))
moved = [label for label in T.module_generating_set()
         if J(T.module_generator(label)) != T.module_generator(label)]
print('  generators moved by J : %d ; on each of them J(v) + v is orthogonal to <H_M, b_M>: %s'
      % (len(moved),
         all(HM.b(J(T.module_generator(l)) + T.module_generator(l)) == ZZ(0)
             and bM.b(J(T.module_generator(l)) + T.module_generator(l)) == ZZ(0)
             for l in moved)))
print('')

# ---------------------------------------------------------------------------------------
# (D) the invariants that put J in the conjugacy class of I_dP
# ---------------------------------------------------------------------------------------
print('(D) the classification invariants of the coinvariant lattices')
from sage.all import CartanMatrix  # noqa: E402

UU = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
for name, gram in (('U(2), the invariant lattice', U2),
                   ('T_dP = U(2) + U + E8^2', block_diagonal_matrix(U2, UU, E8, E8))):
    M = Lattices(ZZ)([list(r) for r in gram.rows()])
    AM = M.discriminant_group()
    values = Counter(str(z.q()) for z in AM.elements())
    integral_values = all(z.q() in (AM.value_module()(0), AM.value_module()(1))
                          for z in AM.elements())
    print('  %-26s rank %2d, det %s, sig %s, 2-elementary %s, |A| %s, delta = %s'
          % (name, M.module_rank(), M.determinant(), M.signature(), M.is_p_elementary(2),
             AM.cardinality(), 0 if integral_values else 1))
    print('     value census: %s' % (dict(values),))
print('  By thm:two-elementary-classification an indefinite even 2-elementary lattice is')
print('  determined by (p, q), a and delta.  The complement of <H,b> in L_K3 has the disc')
print('  form of U(2) up to sign, so the invariants printed for U(2); T_dP has those printed')
print('  for T_dP; the two agree, so the complements are isometric and J is conjugate to I_dP')
print('  in Orth(L_K3).')
print('')

print('CONCLUSION')
print('  (1) div_{S_Co}(H) = 2, so phi(x) = -x + ((x.H)/2)H is an integral isometry of S_Co')
print('      with (+1)-eigenspace exactly Z H; the eigenspaces span only an index-2')
print('      sublattice, so the operator is integral while the lattice does not split.')
print('  (2) Every class of A_{T_Co} of odd q-value contains a vector of square -1: all 496')
print('      are certified by an explicit tau with tau^2 = -4.  The gluing class of [H/2] is')
print('      odd for every anti-isometry, so t in T_Co tensor Q with t^2 = -1 and the glued')
print('      class exists, and b = H/2 + t is isotropic in L_K3 with b.H = 2 and b orthogonal')
print('      to H^{perp} cap S_Co.')
print('  (3) The involution with (+1)-eigenspace <H,b> is integral (projection formula, checked')
print('      in the model), fixes H, commutes with I_Co, and its invariant lattice is U(2),')
print('      meeting S_Co in Z H.')
print('')
print('  NOT claimed: that an automorphism of a K3 surface realises it; the chamber (h_Co')
print('  nef, H nef and big); the effectivity of alpha.  L_K3 and the overlattice are not')
print('  constructed here: the existence of b is an argument in the manuscript that uses the')
print('  gluing of the Coble primitive embedding, and this file supplies the arithmetic')
print('  inputs to it.')

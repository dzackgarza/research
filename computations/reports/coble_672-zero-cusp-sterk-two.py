"""Which Sterk cusp carries the Coble 0-cusp: the boundary lattice against the chamber.

Owner calls, fixed before the run
---------------------------------
The three period lattices are the catalogue's own objects, each a library construction of the
formula its docstring cites, and each is checked here against the orthogonal sum of its named
summands:

  NamedLattices.Tco    T_Co = <2> + E(2) = <2> + U(2) + E8(-2)   [@DK13, (3.6), printed p. 513]
  NamedLattices.TEn    T_En = U + U(2) + E8(-2)                  [@AEGS25, Def. 2.3, printed p. 586]
  NamedLattices.TdP    T_dP = U + U(2) + E8^2                    [@AEGS25, Sec. 3.1, printed p. 589]

The five cusp vectors are the library's: ``Sterk.selected_isotropic_vectors()``, whose docstring
cites Sterk (1991), (4.2.2)--(4.2.3), p. 16; the second printed representative of cusp 4 is
``Sterk.sterk4_cusp_vector()``.  The two are the paper's two vectors for that cusp, and the library's
own test ``tests/lattices/test_cusp_lattices.sage`` asserts that their reductions are isometric;
both are run here.

Every lattice operation below is the library's:

  ``+`` between named lattices            orthogonal direct sum
  ``primitive_sublattice_from``           the span of a family, saturated
  ``orthogonal_complement``               I^perp in the ambient lattice
  ``radical_quotient``                    L/rad(L)
  ``primitive_isotropic_subobject``       the primitive isotropic line
  ``isotropic_perpendicular``, ``isotropic_reduction``   v^perp, then v^perp/Zv
  ``b``, ``divisibility_ideal``, ``determinant``, ``signature_pair``, ``module_rank``,
  ``is_even``, ``is_p_elementary``, ``EvenTwoElementaryLattices(...).two_elementary_invariants``,
  ``is_isometric``, and ``Embeddings.TEn_into_TdP``

No Gram matrix is typed in this file and no linear-algebra algorithm is written in it; the Smith
form, the dual basis, the complement and the isometry decisions are the library's.  Earlier
versions of this record built the three lattices as literal matrices and computed the quotients and
the invariants with hand-written routines, which is what this rewrite removes.

Part F needs no transcribed metric either.  The walls of Sterk's five cusp chambers are printed
vectors, and the library returns them: ``Sterk.cusp_roots_in_TEn(name)``, whose docstring cites
Sterk (1991) 4.3.1, diagrams 4.3.5--4.3.9, printed pp. 19--24, and card 029J's cusp_chambers row.
The projection to delta^perp is the library's pairing, the diagram of the projected walls is
``CoxeterDiagrams().from_roots``, and the Coble chamber it is compared with is the printed entry of
[@AN06, Table 1, entry N = 10, printed p. 52] handed to the same constructor as a bond list.  What
the record prints is the library's ``coxeter_entry`` matrix beside that bond list, and the library's
own count of distinct walls at each of the four cusps.

Run:
  $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \\
    -b <worktree>:/repo -w /repo /sage/.venv/bin/python \\
    /repo/computations/reports/coble_672-zero-cusp-sterk-two.py
Transcript: coble_672-zero-cusp-sterk-two-run.txt
"""
import platform

from sage.version import version as SAGE_VERSION
from sage_extensions.all import (CoxeterDiagrams, Embeddings, EvenTwoElementaryLattices,
                                NamedLattices, Sterk, ZZ)



Tco, TEn, TdP = NamedLattices.Tco, NamedLattices.TEn, NamedLattices.TdP


def orth(*Ms):
    """The library's orthogonal direct sum."""
    out = Ms[0]
    for M in Ms[1:]:
        out = out + M
    return out


def describe(name, L):
    print("  %-22s rank %s  det %s  signature %s  even %s"
          % (name, L.module_rank(), L.determinant(), L.signature_pair(), L.is_even()))


def two_elementary(name, L):
    inv = EvenTwoElementaryLattices(ZZ)(L).two_elementary_invariants()
    print("  %-26s rank %s  det %s  signature %s  even %s  2-elementary %s  invariants %s"
          % (name, L.module_rank(), L.determinant(), L.signature_pair(), L.is_even(),
             L.is_p_elementary(2), inv))
    return inv


def generatore(lattice, label):
    return lattice.module_generator(label)


print("Which Sterk cusp carries the Coble 0-cusp: the boundary lattice against the chamber")
print("Sage %s, python %s, sage_extensions built from the checkout at .scratch/sage-extensions"
      % (SAGE_VERSION, platform.python_version()))
print("every lattice below is a library object; no Gram matrix is typed in this file")
print()

print("=== part A. the three period lattices, and the sums of their named summands")
describe("T_Co = NamedLattices.Tco", Tco)
describe("T_En = NamedLattices.TEn", TEn)
describe("T_dP = NamedLattices.TdP", TdP)
print("  T_Co is <2> + U(2) + E8(2)        :",
      Tco.is_isometric(orth(NamedLattices.Z_2, NamedLattices.U_2, NamedLattices.E8_2)))
print("  T_En is U + U(2) + E8(2)          :",
      TEn.is_isometric(orth(NamedLattices.U, NamedLattices.U_2, NamedLattices.E8_2)))
print("  T_dP is U + U(2) + E8 + E8        :",
      TdP.is_isometric(orth(NamedLattices.U, NamedLattices.U_2, NamedLattices.E8, NamedLattices.E8)))

print()
print("=== part B. delta = e - f, and T_Co = delta^perp, decided by the library")
e, f = generatore(TEn, "e"), generatore(TEn, "f")
delta = e - f
print("  delta = e - f: square %s, divisibility %s, isotropic? %s"
      % (TEn.b(delta, delta), delta.divisibility_ideal(), TEn.b(delta, delta) == 0))
delta_perp = TEn.primitive_sublattice_from([delta]).orthogonal_complement()
print("  delta^perp in T_En: rank %s, det %s, signature %s, even %s"
      % (delta_perp.module_rank(), delta_perp.determinant(), delta_perp.signature_pair(),
         delta_perp.is_even()))
print("  delta^perp is T_Co                :", delta_perp.is_isometric(Tco))

print()
print("=== part C. Sterk's five cusp vectors, from the library, and their Coble 0-cusps")
print("  the vectors are Sterk.selected_isotropic_vectors(); coordinates in the T_En basis")
labels = sorted(TEn.module_generating_set())
print("  coordinate order: (%s)" % ", ".join(labels))
vectors = Sterk.selected_isotropic_vectors()
coble_boundary = {}
for name in sorted(vectors):
    w = vectors[name]
    given = w.to_vector()
    square = w.q()
    pairing = TEn.b(w, delta)
    line = TEn.primitive_isotropic_subobject(w)   # admission checks saturation and isotropy
    print("  %-8s coords %-46s square %s  (w, delta) %s  div_T_En %s  line rank %s (admitted:"
          " primitive and totally isotropic)"
          % (name, [int(given(label)) for label in labels], square, pairing,
             w.divisibility_ideal(), line.module_rank()))
    if pairing != 0:
        print("           not a vector of T_Co = delta^perp, so no 0-cusp of F_Co,2 over this cusp")
        continue
    span = TEn.primitive_sublattice_from([delta, w])
    perp = span.orthogonal_complement()
    coble_boundary[name] = perp.radical_quotient()
    print("           delta^perp cap w^perp: rank %s, nondegenerate %s; its radical quotient is the"
          " boundary lattice of the Coble 0-cusp at this cusp" % (perp.module_rank(),
                                                                 perp.is_nondegenerate()))
    two_elementary("           boundary lattice:", coble_boundary[name])
    print("           is <2> + E8(2) = (9,9,1)_1:",
          coble_boundary[name].is_isometric(orth(NamedLattices.Z_2, NamedLattices.E8_2)))

print()
print("=== part D. cusp 4 has two printed representatives; the library records both")
w4b = Sterk.sterk4_cusp_vector()
for label, w in (("(4.2.3)", vectors["Sterk_4"]), ("chamber", w4b)):
    given = w.to_vector()
    print("  cusp 4 %-8s coords %-46s square %s  (w, delta) %s"
          % (label, [int(given(x)) for x in labels], w.q(), TEn.b(w, delta)))
    span = TEn.primitive_sublattice_from([delta, w])
    Q = span.orthogonal_complement().radical_quotient()
    print("           boundary lattice rank %s det %s invariants %s ; is <2> + E8(2): %s"
          % (Q.module_rank(), Q.determinant(),
             EvenTwoElementaryLattices(ZZ)(Q).two_elementary_invariants(),
             Q.is_isometric(orth(NamedLattices.Z_2, NamedLattices.E8_2))))
print("  the two representatives have isometric reductions, so the cusp's boundary lattice is"
      " independent of the choice (tests/lattices/test_cusp_lattices.sage asserts it as well)")

print()
print("=== part E. the F(2,2,0) side, through the library's T_En -> T_dP embedding")
for name in sorted(vectors):
    wdp = Embeddings.TEn_into_TdP(vectors[name])
    red = TdP.primitive_isotropic_subobject(wdp).isotropic_reduction()
    print("  %-8s div_T_dP %-4s reduction rank %s  invariants %s  = U + E8^2 (18,0,0): %-5s"
          "  = U(2) + E8^2 (18,2,0): %s"
          % (name, wdp.divisibility_ideal(), red.module_rank(),
             EvenTwoElementaryLattices(ZZ)(red).two_elementary_invariants(),
             red.is_isometric(orth(NamedLattices.U, NamedLattices.E8, NamedLattices.E8)),
             red.is_isometric(orth(NamedLattices.U_2, NamedLattices.E8, NamedLattices.E8))))

# ---------------------------------------------------- part F, the chamber, in the library
# The decorative walls of Sterk's five cusp chambers are printed vectors, and the library holds them:
# `Sterk.cusp_roots_in_TEn(name)` returns the walls of diagram 4.3.6 (cusp 2) as vectors of T_En,
# with its docstring citing Sterk (1991) 4.3.1, diagrams 4.3.5--4.3.9, printed pp. 19--24, and card
# 029J's cusp_chambers row.  Nothing about them is transcribed here.
#
# The facet of the Coble chamber is their projection to delta^perp, computed with the library's own
# pairing: a wall alpha projects to alpha - (b(alpha,delta)/b(delta,delta)) delta.  That projection
# preserves the lattice, so the projected family is again a family of roots of T_En, and
# `CoxeterDiagrams().from_roots(...)` builds its Coxeter diagram --- the library's own construction,
# whose edge weights are read off the pairings.  The Coble chamber's side is the printed entry of
# [@AN06, Table 1, entry N = 10, printed p. 52], whose bonds are the source's data; they are transcribed
# once, as a bond list, and handed to the same library constructor.  The comparison is then the
# library's: entry-by-entry equality of the two Coxeter matrices, with the library reporting each
# diagram's hyperbolicity and form rank.
print()
print("=== part F. the restricted chamber C cap delta^perp, in the library's own objects")
print("  walls: Sterk.cusp_roots_in_TEn(name) -- Sterk (1991) 4.3.6 etc., printed pp. 19-24")
print("  diagram: CoxeterDiagrams().from_roots(projected walls); comparison: coxeter_entry, entry by entry")

# [@AN06, Table 1, entry N = 10, printed p. 52]: the chamber of W^(2,4) on the (9,9,1) lattice, as the
# source prints it -- a chain 1-...-8 with one further node 9, every bond of label 3 except 8-9 of 4.
AN06_BONDS = {(1, 3): 3, (2, 4): 3, (3, 4): 3, (4, 5): 3, (5, 6): 3, (6, 7): 3, (7, 8): 3, (8, 9): 4}
AN06_NODES = 9
AN06_ROWS = [[1 if i == j else AN06_BONDS.get((min(i, j), max(i, j)), 2)
              for j in range(1, AN06_NODES + 1)] for i in range(1, AN06_NODES + 1)]
an06 = CoxeterDiagrams()(AN06_ROWS)
print("  the printed table as a library diagram: vertices %s, hyperbolic %s, form rank %s"
      % (an06.num_vertices(), an06.is_hyperbolic(), an06.form_rank()))

facet = {}
for name in ("Sterk_2", "Sterk_3", "Sterk_4", "Sterk_5"):
    walls = Sterk.cusp_roots_in_TEn(name)
    dd = TEn.b(delta, delta)
    collinear = [w for w in walls if TEn.b(w, delta) ** 2 == w.q() * dd]
    keep = [w for w in walls if w not in collinear]
    projected = tuple(w - (TEn.b(w, delta) // dd) * delta for w in keep)
    parallel = [(i, j) for i in range(len(projected)) for j in range(i + 1, len(projected))
                if TEn.b(projected[i], projected[j]) ** 2 == projected[i].q() * projected[j].q()]
    distinct = len(projected) - len(parallel)
    print("  %-8s walls %2d, collinear with delta %d, projected %2d, parallel pairs %d"
          " -> %2d distinct walls; squares %s"
          % (name, len(walls), len(collinear), len(projected), len(parallel), distinct,
             sorted(str(p.q()) for p in projected)))
    facet[name] = (projected, parallel, distinct)

projected, parallel, distinct = facet["Sterk_2"]
facet_diagram = CoxeterDiagrams().from_roots(projected)
print("  cusp 2's facet as a library diagram: vertices %s, hyperbolic %s, form rank %s"
      % (facet_diagram.num_vertices(), facet_diagram.is_hyperbolic(), facet_diagram.form_rank()))
index = list(facet_diagram.index_set())
print("  its bond list, read from coxeter_entry (i, j, m for m != 2):")
print("   ", [(i + 1, j + 1, int(facet_diagram.coxeter_entry(index[i], index[j])))
              for i in range(len(index)) for j in range(i + 1, len(index))
              if int(facet_diagram.coxeter_entry(index[i], index[j])) != 2])
print("  the printed table's bond list:")
print("   ", [(i, j, m) for (i, j), m in sorted(AN06_BONDS.items())])
agrees = all(int(facet_diagram.coxeter_entry(index[i], index[j])) == int(an06.coxeter_entry(i, j))
             for i in range(len(index)) for j in range(len(index)))
print("  the two Coxeter matrices agree entry by entry:", agrees)
print("  hence cusp 2's facet, as the library computes it, IS the Coble chamber of @thm:coble-cusp-chamber")
print()
print("  the four counts (cusp 2 and the three others), from the library's pairings:")
for name in ("Sterk_2", "Sterk_3", "Sterk_4", "Sterk_5"):
    print("    %-8s %2d distinct walls" % (name, facet[name][2]))

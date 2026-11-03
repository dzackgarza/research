"""Focused semantic check of delta(T_Co) through the maintained discriminant-form API
(provider pin c546077d). Convention: Z/2Z inside Q/2Z is { 0+2Z, 1+2Z }: an element's
order-2 condition is 2x in 2Z, so the canonical subgroup has the order-2 elements 0 and 1;
[1/2] has order 4 and lies outside it. delta = 0 iff Im q stays in that subgroup.
Uses: L.discriminant_group(), A.value_module(), class .q() -- the same operations as
computations/reports/coble_rank_one_placement.py (B)."""
from sage.all import ZZ, matrix, block_diagonal_matrix
from sage_extensions.all import Lattices

E8r = matrix(ZZ, 8, 8, [
    [2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],[0,0,-1,2,-1,0,0,0],
    [0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
U2 = matrix(ZZ, [[0, 2], [2, 0]])

def census(name, G, witness, wi_coords):
    L = Lattices(ZZ)([list(r) for r in G.rows()])
    A = L.discriminant_group()
    classes = list(A.elements())
    vals = sorted({str(z.q()) for z in classes})
    print(f"{name}: det {L.determinant()}, |A_L| {A.cardinality()}, distinct q-values {vals}")
    if witness is not None:
        w = L.linear_combination({i: c for i, c in wi_coords.items()})
        print(f"  witness div({witness}) = {w.div() if hasattr(w, 'div') else L.div(w)}")
        cl = L.divided_discriminant_class(w)
        print(f"  {witness}: q(class) = {cl.q()}")

G_sub = matrix(ZZ, [[2]])
census("<2>", G_sub, "eta", {0: 1})
G_u2 = U2
census("U(2)", G_u2, "e+f", {0: 1, 1: 1})
# T_Co: only the two witness classes' q-values (no full 2048-element enumeration:
# the Heegner census of the full group is the job of coble_rank_one_placement.py).
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(G_sub, U2, -2*E8r).rows()])
for name, coords in [("eta (in <2>)", {0: 1}), ("e+f (in U(2))", {1: 1, 2: 1})]:
    w = T.linear_combination(coords)
    cl = T.divided_discriminant_class(w)
    print(f"T_Co witness {name}: q(class) = {cl.q()}")

"""
Compute generators of Stab_{O(T_En)}(h) where h = e+f in the U(2) block.

T_En = U ⊕ U(2) ⊕ E_8(2),  signature (2,10), rank 12.
h = [0,0,1,1,0,...,0], h^2 = 4.

Uses INDEF_FORM_StabilizerVector from polyhedral_common (Dutour-Sikiric).
"""

import json
import sys

sys.path.insert(0, ".")
from src.coble_geometry_foundation import Lattice
from src.external.py_polyhedral.binaries import indefinite_form_stabilizer_vector


def gram_as_lists(L):
    n = L.rank()
    M = L.inner_product_matrix()
    return [[int(M[i][j]) for j in range(n)] for i in range(n)]


def main():
    U = Lattice.U()
    E8 = Lattice.E(8)
    T_En = U.direct_sum(U.twist(2)).direct_sum(E8.twist(2))
    G = gram_as_lists(T_En)

    assert T_En.rank() == 12
    assert T_En.signature_pair() == (2, 10)

    # h = e+f in the U(2) block (positions 2,3 in 0-indexed basis)
    h = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    h2 = sum(G[i][j] * h[i] * h[j] for i in range(12) for j in range(12))
    assert h2 == 4, f"h^2 = {h2}, expected 4"

    print("Computing Stab_{O(T_En)}(h)...", flush=True)
    gens = indefinite_form_stabilizer_vector(G, h)

    assert len(gens) > 0, "Expected at least one generator"

    # Verify each generator fixes h and preserves the Gram matrix
    # polyhedral_common convention: M G M^T = G (row vectors, right action)
    n = 12
    for idx, M in enumerate(gens):
        # Check M G M^T = G
        MGMt = [
            [
                sum(M[i][k] * G[k][m] * M[j][m] for k in range(n) for m in range(n))
                for j in range(n)
            ]
            for i in range(n)
        ]
        assert MGMt == G, f"Generator {idx} does not preserve Gram matrix"
        # Check M h = h (column action)
        Mh = [sum(M[i][j] * h[j] for j in range(n)) for i in range(n)]
        assert Mh == h, f"Generator {idx} does not fix h: {Mh}"

    print(f"OK: {len(gens)} generators of Stab_{{O(T_En)}}(h) verified.")
    print(json.dumps(gens))


if __name__ == "__main__":
    main()

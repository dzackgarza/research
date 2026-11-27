"""
Verify Sterk's result (Sterk 1991, confirmed in AEGS23 Fig. 3) that
F_{(10,10,0)} = D(T_En) / O(T_En) has exactly two 0-cusps and two 1-cusps.

T_En = U ⊕ U(2) ⊕ E_8(2)   (signature (2,10), rank 12, Nikulin (12,10,0)_2)

0-cusps = O(T_En)-orbits of primitive isotropic lines  (k=1 planes)
1-cusps = O(T_En)-orbits of primitive isotropic planes (k=2 planes)

Both counts should equal 2.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.coble_geometry_foundation import Lattice
from src.external.py_polyhedral.binaries import indefinite_form_isotropic_k_plane


def gram_as_lists(lattice):
    M = lattice.inner_product_matrix()
    return [[int(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]


def main():
    U = Lattice.U()
    E8 = Lattice.E8()

    # T_En = U ⊕ U(2) ⊕ E_8(2)
    T_En = U.direct_sum(U.twist(2)).direct_sum(E8.twist(2))

    sig = T_En.signature_pair()
    assert sig == (2, 10), f"Expected signature (2,10), got {sig}"
    assert T_En.rank() == 12, f"Expected rank 12, got {T_En.rank()}"

    gram = gram_as_lists(T_En)

    # 0-cusps: orbits of primitive isotropic lines (k=1)
    zero_cusps = indefinite_form_isotropic_k_plane(gram, 1)
    n_zero = len(zero_cusps)
    assert n_zero == 2, f"Expected 2 zero-cusps, got {n_zero}: {zero_cusps}"

    # 1-cusps: orbits of primitive isotropic planes (k=2)
    one_cusps = indefinite_form_isotropic_k_plane(gram, 2)
    n_one = len(one_cusps)
    assert n_one == 2, f"Expected 2 one-cusps, got {n_one}: {one_cusps}"

    print(f"OK: T_En has {n_zero} zero-cusps and {n_one} one-cusps under O(T_En).")
    print(f"    Zero-cusps: {zero_cusps}")
    print(f"    One-cusps:  {one_cusps}")


if __name__ == "__main__":
    main()

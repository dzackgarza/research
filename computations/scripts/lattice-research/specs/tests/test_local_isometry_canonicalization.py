from __future__ import annotations

from sage.all import ZZ, matrix


def test_local_isometry_canonicalization_at_prime_two():
    """
    Prove that is_locally_isometric_to correctly identifies isometric lattices
    even when their raw Jordan decomposition (symbol_tuple_list) differs.

    Case: A = [1 0; 0 2], B = [3 0; 0 6].
    A raw: [[0, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    B raw: [[0, 1, 3, 1, 3], [1, 1, 3, 1, 3]]
    They are locally isometric at p=2.

    Proof by Witness:
    Let M = [1 -2; 1 1].
    Then M^T A M = [1 1; -2 1] [1 0; 0 2] [1 -2; 1 1] = [3 0; 0 6] = B.
    det(M) = 3, which is a unit in Z_2.
    """
    A_mat = matrix(ZZ, [[1, 0], [0, 2]])
    B_mat = matrix(ZZ, [[3, 0], [0, 6]])
    M = matrix(ZZ, [[1, -2], [1, 1]])

    # Witness Assertions in Z_2
    from sage.all import Zp

    Z2 = Zp(2, prec=20, type="capped-rel", print_mode="series")
    A_Z2 = matrix(Z2, A_mat)
    B_Z2 = matrix(Z2, B_mat)
    M_Z2 = matrix(Z2, M)

    # 1. Assert M is an isometry: M^T A M = B
    assert M_Z2.transpose() * A_Z2 * M_Z2 == B_Z2

    # 2. Assert M is an element of GL_2(Z_2): det(M) is a unit
    det_M = M_Z2.det()
    assert det_M.is_unit()

    from src.lattices.lattices import Lattice

    L1 = Lattice.from_gram(A_mat)
    L2 = Lattice.from_gram(B_mat)

    # Verify that the library correctly identifies them as isometric
    # This proves that our use of the Genus symbol object's equality handles
    # the canonicalization (fusion of Jordan blocks) correctly.
    assert L1.is_locally_isometric_to(L2, 2) is True


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

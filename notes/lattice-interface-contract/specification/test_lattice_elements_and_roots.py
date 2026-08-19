from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from sage.all import ZZ, matrix

from .conftest import Lattice, assert_equal

H3 = Lattice.hyperbolic(rank=3)


def test_lattice_element_interface_contract():
    """
    method: element

    Element contract:
    `L.element(coords)` yields an element supporting stable coordinates,
    element-level norm, and element-level bilinear product.
    """
    L = Lattice.from_gram(matrix(ZZ, ((2, 0), (0, 2))))
    x = L.element([3, -1])
    y = L.element([1, 2])

    assert_equal(tuple(x.coords()), (3, -1), "Lattice.element coordinate mismatch")
    assert_equal(x.norm(), 20, f"Lattice.element norm mismatch: x={tuple(x.coords())}")
    assert_equal((x * y, y * x), (2, 2), f"Lattice.element bilinear product mismatch: x={tuple(x.coords())}, y={tuple(y.coords())}")


def test_lattice_element_norm_and_pairing_overlap_contract():
    """
    method: norm

    Element/lattice overlap contract:
    lattice-level and element-level norm/pairing APIs agree.
    """
    L = Lattice.from_gram(matrix(ZZ, ((2, 0), (0, 2))))
    x = L.element([1, 2])
    y = L.element([-1, 3])

    assert_equal(L.norm(x), x.norm(), "Lattice/Element norm contract mismatch")
    assert_equal(L.pairing(x, y), x * y, "Lattice/Element pairing contract mismatch")


def test_hyperbolic_root_interface_reflection_and_orthogonal_hyperplane():
    """
    method: orthogonal_hyperplane

    Root contract:
    each simple root yields its reflection and orthogonal hyperplane, consistent
    with lattice-level operations; reflection lies in O(L).
    """
    V = H3.vinberg()
    r = V.simple_roots()[0]
    s_from_root = r.reflection()
    s_from_lattice = H3.reflection(r)
    hyperplane_from_root = r.orthogonal_hyperplane()
    hyperplane_from_lattice = H3.orthogonal_hyperplane(r)

    assert s_from_root == s_from_lattice, (
        "Root/lattice reflection mismatch: "
        f"root_reflection={s_from_root}, lattice_reflection={s_from_lattice}, root={r}"
    )
    assert hyperplane_from_root == hyperplane_from_lattice, (
        "Root/lattice orthogonal-hyperplane mismatch: "
        f"root_hyperplane={hyperplane_from_root}, lattice_hyperplane={hyperplane_from_lattice}, root={r}"
    )

    O = H3.orthogonal_group()
    assert_equal(O.contains(s_from_root), True, f"Reflection should lie in O(L): reflection={s_from_root}")

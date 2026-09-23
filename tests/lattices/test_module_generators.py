import pytest

from dzack_research.preamble.all import (
    ZZ,
    Lattices,
)
from dzack_research.preamble.categories.sets import NN


































def test_infinite_rank_form_predicates_and_finite_support_operations() -> None:
    from sage.rings.infinity import Infinity

    infinite = Lattices(ZZ)(ZZ**NN)
    e0 = infinite.basis_vector(0)
    e3 = infinite.basis_vector(3)
    support = e0 + e3

    assert infinite.is_nondegenerate()
    assert infinite.is_positive_definite()
    assert not infinite.is_negative_definite()
    # The full dual is R^N, not the restricted finite-support dual.
    # Sending every basis vector to 1 is outside the correlation image.
    assert infinite.gram_tensor().is_unimodular() is False
    with pytest.raises(AssertionError, match="cokernel construction"):
        infinite.is_unimodular()
    assert infinite.unformed_module() is ZZ**NN
    assert not infinite.is_even()
    assert e0.div() == 1
    assert support.div() == 1
    assert e0.is_root()
    assert not (2 * e0 + infinite.basis_vector(1)).is_root()
    assert infinite.identity_morphism()(e0) == e0

    doubled = infinite.twist(2)
    assert doubled.module_rank() == Infinity
    assert doubled.is_even()
    assert doubled.gram_tensor().is_unimodular() is False
    with pytest.raises(AssertionError, match="cokernel construction"):
        doubled.is_unimodular()
    assert doubled.basis_vector(0).div() == 2
    assert not (2 * doubled.basis_vector(0) + doubled.basis_vector(1)).is_root()

    plane = Lattices(ZZ)("U")
    assert plane.is_even()
    assert plane.is_unimodular()
    u0 = plane.basis_vector(0)
    assert u0.div() == 1
    assert plane.reflection(u0 + plane.basis_vector(1))(u0) == -plane.basis_vector(1)









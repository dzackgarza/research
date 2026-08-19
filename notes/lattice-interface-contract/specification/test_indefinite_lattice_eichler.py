from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import Lattice, assert_equal


def test_indefinite_lattice_eichler_criterion_equivalent_on_u():
    """
    method: eichler_criterion_equivalent

    Eichler-criterion contract:
    in the unimodular hyperbolic plane U, primitive isotropic vectors e1=(1,0) and e2=(0,1)
    are equivalent under O(U), while (1,0) and (2,0) are not both primitive.
    """
    lattice = Lattice.U()
    e1 = lattice.element((1, 0))
    e2 = lattice.element((0, 1))
    nonprimitive = lattice.element((2, 0))

    assert_equal(
        lattice.eichler_criterion_equivalent(e1, e2),
        True,
        f"Expected Eichler equivalence in U for primitive isotropic vectors e1={e1}, e2={e2}",
    )
    assert_equal(
        lattice.eichler_criterion_equivalent(e1, nonprimitive),
        False,
        "Expected non-equivalence when one vector is non-primitive: "
        f"e1={e1}, nonprimitive={nonprimitive}",
    )

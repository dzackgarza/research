r"""Archive reconciliation for the lattice twist endofunctor.

The archive required Nikulin's ``L -> L(a)`` to act on morphisms as well as
objects.  The live functor delegates object scaling to the lattice owner and
reparents the same coordinate matrix between the twisted endpoints.
"""

import pytest

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.functors.twist import twist_functor


def test_twist_functor_transports_a_nonidentity_isometry_with_the_same_matrix() -> None:
    lattice = Lattices(ZZ)("A2")
    root = lattice.module_generator(0)
    reflection = lattice.reflection(root)
    functor = twist_functor(-2)

    twisted = functor(lattice)
    moved = functor(reflection)

    assert moved.domain() is twisted
    assert moved.codomain() is twisted
    assert moved.matrix() == reflection.matrix()
    assert moved != twisted.Hom(twisted).identity()
    assert moved(twisted.module_generator(0)).q() == twisted.module_generator(0).q()
    assert twisted.module_generator(0).q() == -2 * root.q()


def test_twist_functor_is_cached_and_zero_is_not_a_lattice_twist() -> None:
    assert twist_functor(3) is twist_functor(3)
    assert twist_functor(3).scale() == ZZ(3)
    with pytest.raises(ValueError):
        twist_functor(0)

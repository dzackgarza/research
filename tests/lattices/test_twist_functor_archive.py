r"""Archive reconciliation for the lattice twist endofunctor.

The archived operation was stronger than the surviving object method: it was
an actual faithful endofunctor, acting on morphisms by the same coordinate
matrix.  These specimens retain that mathematical contract without reviving
the archived implementation.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.functors.twist import twist_functor
from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/functors/twist.sage",
    "live_owner": "src/dzack_research/preamble/categories/functors/twist.py",
    "disposition": "reconciled-live-owner",
}


def test_twist_functor_scales_the_form_and_caches_the_selected_image() -> None:
    integers = _own_ring(SageZZ)
    plane = Lattices(integers)("U")
    twist = twist_functor(integers(2))

    image = twist(plane)

    assert twist.domain() == Lattices(integers)
    assert twist.codomain() == Lattices(integers)
    assert twist.is_faithful()
    assert twist(plane) is image
    assert image.gram_matrix() == integers(2) * plane.gram_matrix()


def test_nonidentity_isometry_keeps_its_matrix_after_twisting() -> None:
    integers = _own_ring(SageZZ)
    plane = Lattices(integers)("U")
    labels = tuple(plane.module_generating_set())
    swap = plane.Aut()(
        {
            labels[0]: plane.module_generator(labels[1]),
            labels[1]: plane.module_generator(labels[0]),
        }
    )
    twist = twist_functor(integers(-3))

    carried = twist(swap)
    twisted_plane = twist(plane)

    assert carried.domain() is twisted_plane
    assert carried.codomain() is twisted_plane
    assert carried.matrix() == swap.matrix()
    assert carried(twisted_plane.module_generator(labels[0])) == (
        twisted_plane.module_generator(labels[1])
    )
    assert carried(twisted_plane.module_generator(labels[1])) == (
        twisted_plane.module_generator(labels[0])
    )


def test_zero_scale_is_not_a_lattice_twist() -> None:
    import pytest

    with pytest.raises(ValueError):
        twist_functor(0)

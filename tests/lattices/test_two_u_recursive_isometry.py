from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_recursive_two_u_isometry_is_identity_on_the_hyperbolic_factors() -> None:
    integers = _own_ring(SageZZ)
    lattices = Lattices(integers)
    first_complement = lattices("A2")
    second_complement = lattices([[-2, 1], [1, -2]])
    source = first_complement.two_u_eichler_model()
    target = second_complement.two_u_eichler_model()

    assert source.is_isometric_to(target)
    witness = source.isometry_to(target)
    assert witness is not None
    assert witness.domain() is source.lattice()
    assert witness.codomain() is target.lattice()

    source_hyperbolic = source.hyperbolic_basis()
    target_hyperbolic = target.hyperbolic_basis()
    for left, right in zip(source_hyperbolic, target_hyperbolic, strict=True):
        assert witness(left) == right


def test_recursive_two_u_isometry_rejects_nonisometric_complements() -> None:
    integers = _own_ring(SageZZ)
    lattices = Lattices(integers)
    source = lattices("A2").two_u_eichler_model()
    target = (lattices("A1") + lattices("A1")).two_u_eichler_model()

    assert not source.is_isometric_to(target)
    assert source.isometry_to(target) is None

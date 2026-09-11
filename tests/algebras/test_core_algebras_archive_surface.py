r"""Archive reconciliation for the core algebra categories.

The live algebra owner strengthens the archived framing: an algebra over ``R``
retains its actual scalar structure map, while a framed algebra retains the
chosen algebra-generator family used by finite generator operations.
"""

from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
    OwnedAlgebras,
    finite_algebra_generators,
    own_algebra,
)
from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.rings import ring_homset

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/algebras.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_owned_algebra_retains_the_scalar_structure_map() -> None:
    integers_to_rationals = ring_homset(ZZ, QQ)(lambda scalar: QQ(scalar))
    rationals_identity = ring_homset(QQ, QQ).identity()

    over_integers = own_algebra(integers_to_rationals)
    over_rationals = own_algebra(rationals_identity)

    assert over_integers in OwnedAlgebras(ZZ)
    assert over_rationals in OwnedAlgebras(QQ)
    assert over_integers in Algebras(ZZ).Associative().Unital()
    assert over_rationals in Algebras(QQ).Associative().Unital()
    assert over_integers._ring_morphism_defining_algebra_structure() is integers_to_rationals
    assert over_rationals._ring_morphism_defining_algebra_structure() is rationals_identity
    assert over_integers.base_ring() is ZZ
    assert over_rationals.base_ring() is QQ


def test_archived_framed_algebra_generators_are_the_selected_finite_family() -> None:
    polynomial = PolynomialRing(QQ, ("x", "y"))
    generators = finite_algebra_generators(polynomial)

    assert polynomial in FramedAlgebras(QQ)
    assert tuple(polynomial.algebra_generating_set()) == ("x", "y")
    assert generators == (
        polynomial.algebra_generator("x"),
        polynomial.algebra_generator("y"),
    )
    assert polynomial.product_on_algebra_generators("x", "y") == generators[0] * generators[1]

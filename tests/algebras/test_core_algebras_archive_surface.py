r"""Archive reconciliation for the core algebra categories.

The live algebra owner strengthens the archived framing: an algebra over ``R``
retains its actual scalar structure map, while a framed algebra retains the
chosen algebra-generator family used by finite generator operations.
"""

from dzack_research.preamble.all import QQ, ZZ, finite_ordered_set
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
)


ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/algebras.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_owned_algebra_retains_the_scalar_structure_map() -> None:
    integers_to_rationals = ZZ.Mor(QQ)(lambda scalar: QQ(scalar))
    rationals_identity = QQ.Mor(QQ).identity()

    over_integers = integers_to_rationals.as_algebra()
    over_rationals = rationals_identity.as_algebra()

    assert over_integers.multiplication() is not None
    assert over_rationals.multiplication() is not None
    assert over_integers in Algebras(ZZ).Associative().Unital()
    assert over_rationals in Algebras(QQ).Associative().Unital()
    structure = over_integers.algebra_structure_morphism()
    assert structure is over_integers.algebra_structure_morphism()
    assert structure.domain() is ZZ
    assert structure(ZZ(3)) == over_integers(QQ(3))
    assert over_rationals.algebra_structure_morphism() is over_rationals.Mor(over_rationals).identity()
    assert over_integers.base_ring() is ZZ
    assert over_rationals.base_ring() is QQ


def test_archived_framed_algebra_generators_are_the_selected_finite_family() -> None:
    polynomial = QQ.polynomial_ring(("x", "y"))
    generators = polynomial.finite_algebra_generators()

    assert polynomial in FramedAlgebras(QQ)
    assert polynomial.algebra_generating_set() == finite_ordered_set(("x", "y"))
    assert generators.cardinality() == 2
    assert generators[0] == polynomial.algebra_generator("x")
    assert generators[1] == polynomial.algebra_generator("y")
    assert polynomial.product_on_algebra_generators("x", "y") == generators[0] * generators[1]

r"""Archive reconciliation for the former monolithic algebra-syntax session.

The archived test mixed four mathematical owners in one notebook surface:
free/presented algebras, ring/algebra structure maps, fractional ideals, and
number-field arithmetic.  Those constructions now live at their dedicated
owners; these specimens retain the cross-owner user syntax without restoring a
second algebra object system.
"""

from dzack_research.preamble.all import (
    NN,
    QQ,
    ZZ,
    FinitelyPresentedAlgebra,
    FractionalIdeal,
    FreeAlgebraOn,
    PolynomialRing,
    QuadraticField,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_preamble_algebra_syntax.sage",
    "live_owner": "tests/algebras/test_preamble_algebra_syntax_archive.py",
    "disposition": "reconciled-live-owner",
}


def test_countable_free_algebra_keeps_generator_labels_and_generator_determined_maps() -> None:
    source = FreeAlgebraOn(QQ, NN)
    target = FreeAlgebraOn(QQ, NN)
    shift = source.Mor(target)(lambda label: target.algebra_generator(label + 1))

    assert source.algebra_generating_set() is NN
    assert not source.algebra_generating_set().cardinality().is_finite()
    assert shift(source.algebra_generator(0) * source.algebra_generator(7)) == (
        target.algebra_generator(1) * target.algebra_generator(8)
    )


def test_presented_algebra_retains_relation_and_explicit_scalar_change() -> None:
    presentation = PolynomialRing(QQ, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    quotient = FinitelyPresentedAlgebra(presentation, (x * y,))
    gaussian = QuadraticField(-1, "i")
    extension = QQ.Mor(gaussian)(lambda value: gaussian(value))
    changed = quotient.base_change(extension)

    assert quotient.presentation_ring() is presentation
    assert quotient.algebra_presentation_morphism()(x * y) == quotient.zero()
    assert changed.base_ring() is gaussian
    assert changed.algebra_presentation_morphism()(
        changed.presentation_ring().algebra_generator("x")
        * changed.presentation_ring().algebra_generator("y")
    ) == changed.zero()


def test_fractional_ideal_membership_uses_the_module_span_not_the_input_tuple() -> None:
    ideal = FractionalIdeal(ZZ, (ZZ(2), ZZ(3)))
    half = FractionalIdeal(ZZ, (QQ(1) / 2,))

    assert ZZ(1) in ideal
    assert QQ(1) / 2 not in ideal
    assert half.module_generating_set().cardinality() == 1
    assert half.module_generator(next(iter(half.module_generating_set()))) == QQ(1) / 2


def test_univariate_algorithms_and_number_field_arithmetic_return_owned_values() -> None:
    polynomials = PolynomialRing(QQ, "x")
    x = polynomials.algebra_generator("x")
    cubic = (x - 1) * (x - 2) * (x - 3)
    quotient, remainder = cubic.quo_rem((x - 1) * (x - 2))
    field = QuadraticField(5, "a")
    primitive = field.primitive_element()

    assert quotient.parent() is polynomials
    assert remainder == polynomials.zero()
    assert cubic.factor().reconstruct() == cubic
    assert field.degree() == 2
    assert primitive.norm() == QQ(-5)
    assert primitive.trace() == QQ.zero()
    assert field.ring_of_integers().integral_basis().cardinality() == 2

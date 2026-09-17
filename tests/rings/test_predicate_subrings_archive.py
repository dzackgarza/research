r"""Archive reconciliation for predicate-defined subrings.

The archived object retained an ambient ring, a membership predicate and the
canonical inclusion.  The live owner keeps the same mathematics and additionally
refuses undecided predicate answers instead of coercing them to truth values.
"""

import pytest

from dzack_research.preamble.all import QQ, ZZ, PredicateSubrings

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/rings/predicate_subrings.sage",
    "live_owner": "src/dzack_research/preamble/categories/rings/ring_foundation.py",
    "disposition": "reconciled-live-owner",
}


def test_predicate_subring_retains_ambient_ring_predicate_and_inclusion() -> None:
    integers_in_rationals = QQ.predicate_subring(
        lambda value: value.denominator() == 1,
        "z is integral",
    )

    assert integers_in_rationals in PredicateSubrings()
    assert integers_in_rationals.ambient_ring() is QQ
    assert integers_in_rationals.one() == QQ.one()
    assert integers_in_rationals.zero() == QQ.zero()
    assert QQ(6) in integers_in_rationals
    assert QQ(1) / 2 not in integers_in_rationals

    inclusion = integers_in_rationals.inclusion()
    assert inclusion.domain() is integers_in_rationals
    assert inclusion.codomain() is QQ
    assert inclusion(integers_in_rationals(ZZ(3))) == QQ(3)


def test_predicate_subring_constructor_rejects_elements_outside_the_predicate() -> None:
    integers_in_rationals = QQ.predicate_subring(
        lambda value: value.denominator() == 1,
        "z is integral",
    )

    with pytest.raises(ValueError):
        integers_in_rationals(QQ(1) / 2)


def test_undecided_predicate_membership_is_not_guessed() -> None:
    unresolved = QQ.predicate_subring(
        lambda value: True if value == 0 else None,
        "membership is only decided at zero",
    )

    assert QQ.zero() in unresolved
    with pytest.raises(AssertionError, match="selected predicate"):
        QQ.one() in unresolved


def test_predicate_subring_initializes_its_scalar_action_product_and_unit() -> None:
    subring = QQ.predicate_subring(
        lambda value: value.denominator() == 1,
        "the denominator is one",
    )
    three = subring(3)
    four = subring(4)

    assert subring.base_ring() is subring
    assert subring.unformed_module() is subring
    assert subring.multiplication()(three, four) == subring(12)
    assert subring.scalar_multiple(three, four) == subring(12)
    assert subring.multiplication()(subring.one(), four) == four
    assert subring.algebra_structure_morphism() is subring.Mor(subring).identity()
    assert subring.inclusion()(subring.multiplication()(three, four)) == QQ(12)

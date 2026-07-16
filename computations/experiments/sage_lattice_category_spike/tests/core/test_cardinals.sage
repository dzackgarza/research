r"""Cardinal arithmetic laws (issue #211, CP1).

The owned cardinals are the exact naturals, ``aleph_0``, and the continuum
``2^aleph_0`` — the cardinalities realized by objects of the owned graph.
Arithmetic is standard cardinal arithmetic: exact on naturals, absorption
at infinity, ``0`` annihilates products, and exponentiation follows
``kappa^aleph_0 == 2^aleph_0``; a value beyond the continuum is refused,
never misrepresented. Sage's ``+Infinity`` normalizes to ``aleph_0`` (its
weakest reading), so countable-infinite comparisons against ``oo`` keep
working while the continuum stays strictly larger.
"""

from __future__ import annotations

import pytest

from sage.all import ZZ, oo

from sage_lattice_category_spike.objects.cardinals import Cardinal, aleph0, cardinal, continuum


def test_the_cardinal_tower_is_strictly_ordered():
    five = cardinal(5)
    assert five < aleph0 < continuum
    assert five < continuum
    assert aleph0 != continuum
    assert cardinal(7) > five
    assert cardinal(5) == 5 == ZZ(5)


def test_sage_infinity_reads_as_aleph_naught():
    assert aleph0 == oo
    assert continuum != oo
    assert continuum > oo
    assert cardinal(oo) == aleph0


def test_addition_is_exact_then_absorbs():
    assert cardinal(3) + cardinal(4) == 7
    assert cardinal(5) + aleph0 == aleph0
    assert aleph0 + aleph0 == aleph0
    assert aleph0 + continuum == continuum
    assert continuum + continuum == continuum
    assert 5 + aleph0 == aleph0


def test_multiplication_is_exact_absorbs_and_is_annihilated_by_zero():
    assert cardinal(3) * cardinal(4) == 12
    assert cardinal(5) * aleph0 == aleph0
    assert aleph0 * aleph0 == aleph0
    assert aleph0 * continuum == continuum
    assert continuum * continuum == continuum
    assert cardinal(0) * aleph0 == 0
    assert cardinal(0) * continuum == 0
    assert 0 * aleph0 == 0


def test_exponentiation_follows_cardinal_laws_within_the_representable_range():
    assert cardinal(0) ** cardinal(0) == 1
    assert cardinal(0) ** aleph0 == 0
    assert cardinal(1) ** continuum == 1
    assert cardinal(2) ** cardinal(10) == 1024
    assert cardinal(2) ** aleph0 == continuum
    assert aleph0 ** cardinal(10) == aleph0
    assert aleph0 ** aleph0 == continuum
    assert continuum ** cardinal(10) == continuum
    assert continuum ** aleph0 == continuum


def test_beyond_the_continuum_is_refused_not_misrepresented():
    with pytest.raises(AssertionError):
        cardinal(2) ** continuum
    with pytest.raises(AssertionError):
        aleph0 ** continuum
    with pytest.raises(AssertionError):
        Cardinal(-1)


def test_predicates_and_hashing_are_consistent():
    assert cardinal(5).is_finite() and cardinal(5).is_countable()
    assert aleph0.is_countably_infinite() and not aleph0.is_finite()
    assert continuum.is_uncountably_infinite() and continuum.is_uncountable()
    assert hash(cardinal(5)) == hash(ZZ(5))
    assert hash(aleph0) != hash(continuum)
    assert len({aleph0, continuum, aleph0 + aleph0, continuum * aleph0}) == 2

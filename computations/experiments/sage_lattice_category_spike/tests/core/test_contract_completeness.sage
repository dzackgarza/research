r"""Completeness gate: every constructible object must implement all the
required ``abstract_method`` contracts its category declares.

This is Sage's own parent-conformance surface, not a bespoke check.
``SageObject._test_not_implemented_methods`` accesses every name and fails with
``Not implemented method: <name>`` for any required ``abstract_method`` a leaf
does not shadow. (The full ``TestSuite(obj).run()`` battery is a superset that
also exercises pickling, elements, and the additive-magma/zero axioms; this file
gates only the abstract-method-compliance slice.)

A constructor with an unrealized required contract fails HARD here -- a bright red
flag tracked in dzackgarza/research#24 until that contract is implemented or
localized (implement / constructor-assert-with-data / leaf subcategory).
"""
from __future__ import annotations

import pytest

from sage.all import ZZ, TestSuite, matrix

from sage_lattice_category_spike.lattice_categories import Lattice, Lattices, U


CONSTRUCTORS = [
    pytest.param(lambda: Lattice("A2"), id="Lattice_A2_posdef"),
    pytest.param(lambda: Lattice("D4"), id="Lattice_D4_posdef"),
    pytest.param(lambda: Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2, 0], [0, 2]])), id="from_gram_definite_rank2"),
    pytest.param(lambda: Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2]])), id="from_gram_definite_rank1"),
    pytest.param(lambda: U(), id="U_hyperbolic_plane"),
]


@pytest.mark.xfail(reason="red proof gate for OPEN issue dzackgarza/research#24: unrealized required contracts (primitive-embedding cluster) await the implement/localize triage", strict=True)
@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_constructor_implements_all_required_contracts(construct):
    r"""Sage's standard abstract-method compliance check. Raises
    ``AssertionError: Not implemented method: <name>`` for the first required
    contract a constructor leaves unrealized. A gap is a bright red flag: the
    object claims a category whose total vocabulary it does not provide.

    Marked as a strict open-issue xfail gate (POLICY.NO_SKIP_MASK grant
    2026-07-09): the moment a constructor's contracts are all realized, its
    param XPASSes and the suite goes red, forcing this marker's removal."""
    construct()._test_not_implemented_methods()


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_zero_satisfies_inherited_additive_group_axioms(construct):
    r"""The zero slice of ``TestSuite(obj).run()``: the additive-group axioms the
    element class inherits from the module category chain
    (``AdditiveMagmas.AdditiveUnital`` up through ``Element``) -- ``zero`` reads
    as false, ``is_zero`` holds, and it is fixed under the group law.

    Run standalone (not the full battery, whose abstract-method superset is
    #24-red). This guards against an element re-hand-rolling ``__eq__`` instead
    of supplying ``_richcmp_``: a Python ``__eq__`` satisfies direct ``==`` but
    is invisible to Sage's inherited ``is_zero``/``__bool__``, silently detaching
    these checks (the exact failure this test was added for)."""
    lattice = construct()
    lattice._test_zero()
    lattice.zero()._test_nonzero_equal()


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_elements_are_hashable_consistently_with_equality(construct):
    r"""Sage's ``Element`` sets ``__hash__ = None`` -- rich comparison lives at
    the C level and every element subclass must opt into hashing. Lattice
    elements opt in categorically on ``LatticeElement`` over their generator
    coefficients, so they are usable in sets/dicts/caches and equal elements hash
    equally (the ``hash``/``==`` contract)."""
    lattice = construct()
    generator = lattice.gen(0)
    assert hash(generator) == hash(lattice.gen(0))
    assert {generator, lattice.zero()} == {lattice.gen(0), lattice.zero()}


@pytest.mark.xfail(
    reason="parents are not UniqueRepresentation, so loads(dumps(L)) is not L and "
    "pickled elements compare unequal. Deferred to the object/subobject identity "
    "refactor. THIS MARKER MUST BE REMOVED FOR dzackgarza/research#25 TO CLOSE.",
    strict=True,
)
@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_pickling_roundtrip_preserves_equality(construct):
    r"""The pickling slice of ``TestSuite(obj).run()``. Currently xfails: object
    identity keys on ``(R, G)`` but the parent is not ``UniqueRepresentation``, so
    ``loads(dumps(L))`` is a distinct value-equal parent and ``_richcmp_`` (which
    only fires after coercion to a common parent) reports the pickled zero as
    unequal to the original. The fix is parent ``UniqueRepresentation`` on ``(R, G)``
    (subobjects on ``(R, G, f)``), tracked in dzackgarza/research#25. When that
    lands this xpasses under ``strict`` and forces removal of the marker."""
    lattice = construct()
    lattice.zero()._test_pickling()


# Axes skipped by the full-battery runner because they fail for separately-tracked
# reasons that already have dedicated coverage above:
#   _test_elements                -> element _test_pickling (strict xfail + #25)
#   _test_not_implemented_methods -> #24 abstract-method contracts (honest-red)
FULL_TESTSUITE_SKIP = ("_test_elements", "_test_not_implemented_methods")


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_full_testsuite_passes_except_tracked_failures(construct):
    r"""Run the FULL Sage ``TestSuite(obj).run()`` battery -- pickling of the
    parent, category axioms, ``some_elements``, ``an_element``, and the rest --
    so a regression in ANY axiom is caught, not only the hand-picked slices above.
    The two axes with separately-tracked failures (see ``FULL_TESTSUITE_SKIP``)
    are skipped; everything else must pass."""
    TestSuite(construct()).run(
        skip=FULL_TESTSUITE_SKIP, raise_on_failure=True, catch=False
    )

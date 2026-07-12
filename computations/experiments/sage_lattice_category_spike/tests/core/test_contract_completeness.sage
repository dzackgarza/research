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
from sage.categories.homset import Hom

from sage_lattice_category_spike.lattice_categories import Lattice, Lattices


CONSTRUCTORS = [
    pytest.param(lambda: Lattice("A2"), id="Lattice_A2_posdef"),
    pytest.param(lambda: Lattice("D4"), id="Lattice_D4_posdef"),
    pytest.param(lambda: Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2, 0], [0, 2]])), id="from_gram_definite_rank2"),
    pytest.param(lambda: Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2]])), id="from_gram_definite_rank1"),
    pytest.param(lambda: Lattice("U"), id="U_hyperbolic_plane"),
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


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_pickling_roundtrip_preserves_equality(construct):
    r"""The pickling slice of ``TestSuite(obj).run()``. A deserialized element
    has a fresh parent equal by ``(R, G)``; the equal-parent coercion must make
    Sage compare its coefficient vector in a common parent."""
    lattice = construct()
    lattice.zero()._test_pickling()


def test_fresh_dual_elements_compare_through_equal_parent_coercion():
    r"""Fresh dual parents have equal lattice data, so corresponding elements
    compare through the canonical identity coercion rather than by allocation
    identity."""
    lattice = Lattice("A2")
    first_dual = lattice.dual()
    second_dual = lattice.dual()
    assert first_dual == second_dual
    assert first_dual.gen(0) == second_dual.gen(0)


def test_equal_parent_coercion_maps_elements_to_the_target_parent():
    r"""The public coercion map transports a vector from a fresh equal parent
    into the target parent without changing its coefficient data."""
    lattice = Lattice("A2")
    target = lattice.dual()
    source = lattice.dual()
    coercion = target.coerce_map_from(source)
    assert coercion(source.gen(0)) == target.gen(0)


def test_sourced_discriminant_lifts_compare_across_fresh_dual_parents():
    r"""``lift`` and ``coset_representative`` independently construct the
    dual cover, but represent the same discriminant coset."""
    discriminant_form = Lattice("A2").discriminant_group()
    generator = discriminant_form.gen(0)
    assert discriminant_form.lift(generator) == discriminant_form.coset_representative(generator)


def test_subobjects_compare_by_lattice_and_inclusion_morphism():
    r"""Subobjects retain their slice data: equal inclusions compare equal,
    while equal-Gram inclusions into different generator lines do not."""
    lattice = Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2, 0], [0, 2]]))
    first = lattice.subobject([lattice.gen(0)])
    same = lattice.subobject([lattice.gen(0)])
    different = lattice.subobject([lattice.gen(1)])
    assert first == same
    assert hash(first) == hash(same)
    assert first != different


def test_plain_lattice_and_subobject_compare_false_with_warning():
    r"""A plain lattice and an equal presented subobject are categorically
    distinct; the comparison must be visible rather than silently conflated."""
    lattice = Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2]]))
    subobject = lattice.subobject([lattice.gen(0)])
    with pytest.warns(UserWarning):
        assert not (lattice == subobject)
    with pytest.warns(UserWarning):
        assert not (subobject == lattice)


def test_lattice_hom_factory_accepts_the_explicit_category():
    r"""The Sage ``Hom`` factory and the parent spelling both construct the
    form-preserving homset in the requested lattice category."""
    lattice = Lattice("A2")
    category = lattice.category()
    direct_homset = lattice.Hom(lattice, category=category)
    factory_homset = Hom(lattice, lattice, category=category)
    identity_matrix = lattice.identity_morphism().matrix()
    assert direct_homset(identity_matrix) == lattice.identity_morphism()
    assert factory_homset(identity_matrix) == lattice.identity_morphism()


# Axes skipped by the full-battery runner because they fail for separately-tracked
# reasons that already have dedicated coverage above:
#   _test_not_implemented_methods -> #24 abstract-method contracts (honest-red)
FULL_TESTSUITE_SKIP = ("_test_not_implemented_methods",)


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

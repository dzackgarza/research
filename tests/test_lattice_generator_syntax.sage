r"""Torture tests for the ``L.<e1, ..., en> = IntegralLattice(...)`` generator sugar.

This file is ``.sage`` on purpose: the preparser *is* the subject. Running it as
``.py`` would test nothing.

The goal of the sugar is notation close to ordinary mathematical writing --
"let $L$ have basis $e_1, \ldots, e_n$" -- so the tests below pin down exactly what
the preparser does with each form, including the ones that fail and the one that
fails *silently*.

Findings these tests encode, each verified against this Sage:

1. ``L.<e,f> = IntegralLattice("H")`` preparses to a ``names=`` keyword plus
   ``_first_ngens``.  The ``names=`` keyword is supplied by the category-refinement
   constructor hook (``integral_lattices``), active at module import time.

2. ``L.<a1,...,a8> = ...`` is a **silent trap**. The preparser does not expand the
   range; it emits three names, the middle one the literal string ``'Ellipsis'``.
   This is not specific to lattices -- ``R.<x0,...,x5> = QQ[]`` yields a polynomial
   ring with generators ``(x0, Ellipsis, x5)``. The constructor hook expands the
   ``Ellipsis`` slot.

3. ``@`` and ``**`` are available via ``IntegralLattices.ParentMethods.__matmul__``
   and ``__pow__``, applied through category refinement.
"""

# Activate the IntegralLattice constructor hook at import time (replaces
# IntegralLattice in sage.all so that names=, __matmul__, __pow__ all work).
import dzack_research.preamble.categories.integral_lattices  # noqa: F401


def _lattice_constructor():
    from sage.all import IntegralLattice

    return IntegralLattice


def test_explicit_generator_form_preparses_to_names_keyword():
    """The sugar becomes a ``names=`` kwarg plus ``_first_ngens``."""
    source = preparse('L.<e,f> = IntegralLattice("H")')
    assert "names=('e', 'f',)" in source, source
    assert "_first_ngens(2)" in source, source


def test_ellipsis_form_expands_the_range():
    r"""``L.<a1, ..., a8>`` must give **eight** named generators.

    Sage's preparser emits three names with the middle one the literal string
    ``'Ellipsis'`` and does not expand the range. The constructor hook reads that
    slot and expands it into the full range.
    """
    IntegralLattice = _lattice_constructor()
    L.<a1,...,a8> = IntegralLattice("E8")
    assert L.variable_names() == tuple(f"a{i}" for i in range(1, 9)), L.variable_names()
    assert len(L.gens()) == 8
    # The crux: a8 is the EIGHTH generator, not the third slot of the raw spec.
    assert a1 == L.gens()[0], a1
    assert a8 == L.gens()[7], a8


def test_explicit_generator_form_binds_names():
    """``L.<e,f> = IntegralLattice("H")`` works via the hooked ``names=``."""
    IntegralLattice = _lattice_constructor()
    L.<e,f> = IntegralLattice("H")
    assert L.variable_names() == ("e", "f")
    assert e == L.gens()[0] and f == L.gens()[1]


def test_generator_count_must_match_the_rank():
    """A range whose length disagrees with the rank fails loudly, not silently."""
    try:
        IntegralLattice = _lattice_constructor()
        L.<a1,...,a5> = IntegralLattice("E8")
    except AssertionError as error:
        assert "5" in str(error) and "8" in str(error), str(error)
    else:
        raise AssertionError("a 5-name range on a rank-8 lattice should fail")


def test_assign_names_then_inject_works():
    """The machinery the sugar needs is present on all lattices."""
    lattice = _lattice_constructor()("E8")
    names = tuple(f"a{i}" for i in range(1, 9))
    lattice._assign_names(names)
    assert lattice.variable_names() == names
    assert len(lattice.gens()) == 8
    first_two = lattice._first_ngens(2)
    assert len(first_two) == 2


def test_variable_names_before_assignment_raises():
    """An unnamed lattice reports loudly rather than inventing names."""
    lattice = _lattice_constructor()("H")
    try:
        lattice.variable_names()
    except ValueError as error:
        assert "_assign_names" in str(error), str(error)
    else:
        raise AssertionError("variable_names() unexpectedly succeeded")


def test_matmul_is_direct_sum():
    """``U @ E8`` must be the orthogonal direct sum."""
    combined = _lattice_constructor()("H") @ IntegralLattice("E8")
    assert combined.rank() == 10, combined.rank()
    expected = _lattice_constructor()("H").direct_sum(IntegralLattice("E8"))
    assert combined.gram_matrix() == expected.gram_matrix()


def test_pow_is_repeated_direct_sum():
    """``U**3`` and the full ``U**3 @ E8**2`` from the old init.sage."""
    IntegralLattice = _lattice_constructor()
    assert (IntegralLattice("H") ** 3).rank() == 6

    # Sage's E8 is POSITIVE definite; this repo's convention is negative definite,
    # so the K3 lattice must be built from the twisted E8 to get signature (3,19).
    # Rank alone would not have caught the flipped convention.
    from dzack_research.preamble import catalogue

    k3 = IntegralLattice("H") ** 3 @ catalogue.Lattices.E8 ** 2
    assert k3.rank() == 22, k3.rank()
    assert k3.signature_pair() == (3, 19), k3.signature_pair()

    raw = IntegralLattice("H") ** 3 @ IntegralLattice("E8") ** 2
    assert raw.signature_pair() == (19, 3), raw.signature_pair()


def test_named_lattice_helper_gives_the_intended_sugar():
    """The ``with_names`` method works via category refinement."""
    lattice = _lattice_constructor()("E8")
    named = lattice.with_names("a1..a8")
    assert named.variable_names() == tuple(f"a{i}" for i in range(1, 9))
    assert len(named.gens()) == 8

    explicit = _lattice_constructor()("H").with_names("e, f")
    assert explicit.variable_names() == ("e", "f")


def test_named_lattice_helper_rejects_a_count_mismatch():
    """A range whose length disagrees with the rank fails loudly, not silently."""
    try:
        _lattice_constructor()("E8").with_names("a1..a5")
    except AssertionError as error:
        assert "8" in str(error) and "5" in str(error), str(error)
    else:
        raise AssertionError("a 5-name range on a rank-8 lattice should fail")


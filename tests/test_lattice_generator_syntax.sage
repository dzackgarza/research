r"""Torture tests for the ``L.<e1, ..., en> = IntegralLattice(...)`` generator sugar.

This file is ``.sage`` on purpose: the preparser *is* the subject. Running it as
``.py`` would test nothing.

The goal of the sugar is notation close to ordinary mathematical writing --
"let $L$ have basis $e_1, \ldots, e_n$" -- so the tests below pin down exactly what
the preparser does with each form, including the ones that fail and the one that
fails *silently*.

Findings these tests encode, each verified against this Sage:

1. ``L.<e,f> = IntegralLattice("H")`` preparses to a ``names=`` keyword plus
   ``_first_ngens``. ``IntegralLattice`` rejects ``names=``, so the explicit form
   raises TypeError. This is a loud failure.

2. ``L.<a1,...,a8> = ...`` is a **silent trap**. The preparser does not expand the
   range; it emits three names, the middle one the literal string ``'Ellipsis'``.
   This is not specific to lattices -- ``R.<x0,...,x5> = QQ[]`` yields a polynomial
   ring with generators ``(x0, Ellipsis, x5)``. Any code relying on this form has the
   wrong number of generators and one bogus name, with no error raised.

3. The underlying machinery is all present on lattices: ``_assign_names``,
   ``variable_names``, ``inject_variables``, ``_first_ngens``, ``gens``. Only the
   constructor keyword is missing, which is what ``patches.lattice_methods`` supplies.

4. ``@`` and ``**`` are not direct-sum and power on lattices, though the old
   init.sage used both throughout (``U**3 @ E8**2``).
"""

# NOT imported at module scope on purpose: patches.install() rebinds the name in
# sage.all and in its defining module, so a reference bound before installation would
# never see the patch. Each test resolves it after installing.


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
    ``'Ellipsis'`` and does not expand the range. Nothing in Sage reads that slot, so
    the patch hijacks it. This test asserts the behaviour we want, so it is red
    without the patch and green with it -- never the other way round.
    """
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        IntegralLattice = _lattice_constructor()
        L.<a1,...,a8> = IntegralLattice("E8")
        assert L.variable_names() == tuple(f"a{i}" for i in range(1, 9)), L.variable_names()
        assert len(L.gens()) == 8
        # The crux: a8 is the EIGHTH generator, not the third slot of the raw spec.
        assert a1 == L.gens()[0], a1
        assert a8 == L.gens()[7], a8
    finally:
        patches.uninstall("lattice_methods")


def test_explicit_generator_form_binds_names():
    """``L.<e,f> = IntegralLattice("H")`` must work, via the patched ``names=``."""
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        IntegralLattice = _lattice_constructor()
        L.<e,f> = IntegralLattice("H")
        assert L.variable_names() == ("e", "f")
        assert e == L.gens()[0] and f == L.gens()[1]
    finally:
        patches.uninstall("lattice_methods")


def test_generator_count_must_match_the_rank():
    """A range whose length disagrees with the rank fails loudly, not silently.

    This is the check whose absence makes the unpatched form dangerous: it would
    have produced three generators for a rank-8 lattice with no error at all.
    """
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        try:
            IntegralLattice = _lattice_constructor()
            L.<a1,...,a5> = IntegralLattice("E8")
        except AssertionError as error:
            assert "5" in str(error) and "8" in str(error), str(error)
        else:
            raise AssertionError("a 5-name range on a rank-8 lattice should fail")
    finally:
        patches.uninstall("lattice_methods")


def test_assign_names_then_inject_works():
    """The machinery the sugar needs is present; only the constructor keyword is not."""
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
    """``U @ E8`` must be the orthogonal direct sum, as the old init.sage used it."""
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        combined = _lattice_constructor()("H") @ IntegralLattice("E8")
        assert combined.rank() == 10, combined.rank()
        expected = _lattice_constructor()("H").direct_sum(IntegralLattice("E8"))
        assert combined.gram_matrix() == expected.gram_matrix()
    finally:
        patches.uninstall("lattice_methods")


def test_pow_is_repeated_direct_sum():
    """``U**3`` and the full ``U**3 @ E8**2`` from the old init.sage."""
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        IntegralLattice = _lattice_constructor()
        assert (IntegralLattice("H") ** 3).rank() == 6

        # Sage's E8 is POSITIVE definite; this repo's convention is negative definite,
        # so the K3 lattice must be built from the twisted E8 to get signature (3,19).
        # Rank alone would not have caught the flipped convention.
        from dzack_research.preamble import catalogue

        k3 = IntegralLattice("H") ** 3 @ catalogue.E8 ** 2
        assert k3.rank() == 22, k3.rank()
        assert k3.signature_pair() == (3, 19), k3.signature_pair()

        raw = IntegralLattice("H") ** 3 @ IntegralLattice("E8") ** 2
        assert raw.signature_pair() == (19, 3), raw.signature_pair()
    finally:
        patches.uninstall("lattice_methods")


def test_named_lattice_helper_gives_the_intended_sugar():
    """The supported route to the same notation, via the patch module."""
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        lattice = _lattice_constructor()("E8")
        named = lattice.with_names("a1..a8")
        assert named.variable_names() == tuple(f"a{i}" for i in range(1, 9))
        assert len(named.gens()) == 8

        explicit = _lattice_constructor()("H").with_names("e, f")
        assert explicit.variable_names() == ("e", "f")
    finally:
        patches.uninstall("lattice_methods")


def test_named_lattice_helper_rejects_a_count_mismatch():
    """A range whose length disagrees with the rank fails loudly, not silently."""
    from dzack_research.preamble import patches

    patches.install("lattice_methods")
    try:
        try:
            _lattice_constructor()("E8").with_names("a1..a5")
        except AssertionError as error:
            assert "8" in str(error) and "5" in str(error), str(error)
        else:
            raise AssertionError("a 5-name range on a rank-8 lattice should fail")
    finally:
        patches.uninstall("lattice_methods")

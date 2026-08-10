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

3. ``**`` is available via ``IntegralLattices.ParentMethods.__pow__``, applied
   through category refinement.  ``@`` is deliberately *not* the direct sum --
   the operator is reserved for the tensor product -- so the orthogonal sum is
   spelled ``+`` or ``direct_sum``.
"""

# Category hooks: load mathematical preamble scripts (not notebook init.sage).
from pathlib import Path
from typing import Callable, ParamSpec, cast

import dzack_research

_LatticeConstructorParams = ParamSpec("_LatticeConstructorParams")

_p = Path(dzack_research.__file__).resolve().parent / "preamble"
load(str(_p / "install.sage"))


def test_set_literal_preparser_preserves_sage_generator_declarations() -> None:
    r"""The notebook set extension must compose with Sage's ``R.<x> =`` syntax."""
    import sageparse.preparser.research  # noqa: F401
    from sage.repl import preparse as sage_preparse
    namespace = dict(globals())
    source = (
        'A2.<alpha1, alpha2> = Lattices.root_lattice("A", 2); '
        "simple_roots = {alpha1, alpha2}; "
        "weight = 3alpha1 + 2alpha2"
    )
    exec(sage_preparse.preparse(source), namespace)

    lattice = namespace["A2"]
    assert lattice.rank() == 2
    assert namespace["alpha1"] == lattice.module_generators()[0]
    assert namespace["alpha2"] == lattice.module_generators()[1]
    expected_roots = Set([namespace["alpha1"], namespace["alpha2"]])
    # Two sets are equal when they have the same elements, which is what ``==``
    # asks of them.  A separate ``equal_as_sets`` would be a second name for
    # that one question.
    assert namespace["simple_roots"] == expected_roots
    assert namespace["weight"] == 3 * namespace["alpha1"] + 2 * namespace["alpha2"]


def _lattice_constructor() -> Callable[_LatticeConstructorParams, "Lattice"]:
    r"""Return the preamble's lattice constructor.

    Not ``sage.all``'s function of this name.  The preamble installs its own
    over that name, and only that one takes ``names=`` -- which is what the
    sugar passes -- and builds a parent inside the owned categories, where
    ``module_generators`` and ``with_names`` live.  Sage's returns a submodule
    of a base-changed module over $\mathbb Q$, which answers to none of them.
    """
    return IntegralLattice


def test_explicit_generator_form_preparses_to_names_keyword() -> None:
    """The sugar becomes a ``names=`` kwarg plus ``_first_ngens``."""
    source = preparse('L.<e,f> = IntegralLattice("H")')
    assert "names=('e', 'f',)" in source, source
    assert "_first_ngens(2)" in source, source


def test_ellipsis_form_expands_the_range() -> None:
    r"""``L.<a1, ..., a8>`` must give **eight** named generators.

    Sage's preparser emits three names with the middle one the literal string
    ``'Ellipsis'`` and does not expand the range. The constructor hook reads that
    slot and expands it into the full range.
    """
    IntegralLattice = _lattice_constructor()
    L.<a1,...,a8> = IntegralLattice("E8")
    assert L.variable_names() == tuple(f"a{i}" for i in range(1, 9)), L.variable_names()
    assert len(L.module_generators()) == 8
    # The crux: a8 is the EIGHTH generator, not the third slot of the raw spec.
    assert a1 == L.module_generators()[0], a1
    assert a8 == L.module_generators()[7], a8


def test_explicit_generator_form_binds_names() -> None:
    """``L.<e,f> = IntegralLattice("H")`` works via the hooked ``names=``."""
    IntegralLattice = _lattice_constructor()
    L.<e,f> = IntegralLattice("H")
    assert L.variable_names() == ("e", "f")
    assert e == L.module_generators()[0] and f == L.module_generators()[1]


def test_generator_count_must_match_the_rank() -> None:
    """A range whose length disagrees with the rank fails loudly, not silently."""
    try:
        IntegralLattice = _lattice_constructor()
        L.<a1,...,a5> = IntegralLattice("E8")
    except AssertionError as error:
        assert "5" in str(error) and "8" in str(error), str(error)
    else:
        raise AssertionError("a 5-name range on a rank-8 lattice should fail")


def test_assign_names_then_inject_works() -> None:
    """The machinery the sugar needs is present on all lattices."""
    lattice = _lattice_constructor()("E8")
    names = tuple(f"a{i}" for i in range(1, 9))
    lattice._assign_names(names)
    assert lattice.variable_names() == names
    assert len(lattice.module_generators()) == 8
    first_two = lattice._first_ngens(2)
    assert len(first_two) == 2


def test_variable_names_before_assignment_raises() -> None:
    """An unnamed lattice reports loudly rather than inventing names."""
    lattice = _lattice_constructor()("H")
    try:
        lattice.variable_names()
    except ValueError as error:
        assert "_assign_names" in str(error), str(error)
    else:
        raise AssertionError("variable_names() unexpectedly succeeded")


def test_pow_is_repeated_direct_sum() -> None:
    """``U**3`` and the full ``U**3 + E8**2`` from the old init.sage."""
    IntegralLattice = _lattice_constructor()
    assert (IntegralLattice("H") ** 3).rank() == 6

    # Sage's E8 is POSITIVE definite; this repo's convention is negative definite,
    # so the K3 lattice must be built from the twisted E8 to get signature (3,19).
    # Rank alone would not have caught the flipped convention.
    E8 = IntegralLattice("E8").twist(-1)
    k3 = IntegralLattice("H") ** 3 + E8 ** 2
    assert k3.rank() == 22, k3.rank()
    assert k3.signature_pair() == (3, 19), k3.signature_pair()

    raw = IntegralLattice("H") ** 3 + IntegralLattice("E8") ** 2
    assert raw.signature_pair() == (19, 3), raw.signature_pair()


def test_named_lattice_helper_gives_the_intended_sugar() -> None:
    """The ``with_names`` method works via category refinement."""
    lattice = _lattice_constructor()("E8")
    named = lattice.with_names("a1..a8")
    assert named.variable_names() == tuple(f"a{i}" for i in range(1, 9))
    assert len(named.module_generators()) == 8

    explicit = _lattice_constructor()("H").with_names("e, f")
    assert explicit.variable_names() == ("e", "f")


def test_named_lattice_helper_rejects_a_count_mismatch() -> None:
    """A range whose length disagrees with the rank fails loudly, not silently."""
    try:
        _lattice_constructor()("E8").with_names("a1..a5")
    except AssertionError as error:
        assert "8" in str(error) and "5" in str(error), str(error)
    else:
        raise AssertionError("a 5-name range on a rank-8 lattice should fail")

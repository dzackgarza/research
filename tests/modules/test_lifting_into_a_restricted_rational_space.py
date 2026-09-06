r"""Containment between two lattices inside one rational space read over ``ZZ``.

``Res(V)`` for ``V = QQ^2`` along ``ZZ -> QQ`` is divisible, hence not finitely
generated over ``ZZ`` and carrying no framing of its own.  A lattice in ``V``
is a monomorphism into that one module, two lattices are two subobjects of it,
and ``L <= M`` is the statement that every generator of ``L`` lifts through the
inclusion of ``M``.  The coefficients of such a lift are read in the
``QQ``-framing of ``V``, so what is decided is a rational linear system whose
solution must be integral.

Unverified: written without running the suite.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FinitelyGeneratedModules,
    FreeModule,
    Modules,
    module_embedding,
    restrict_scalars,
)


def _rational_plane():
    r"""``Res(QQ^2)`` over ``ZZ``, with the rational plane it restricts."""
    plane = FreeModule(QQ, 2)
    space = restrict_scalars(plane, ZZ.Mor(QQ)(lambda element: QQ(element)))
    return space, plane


def test_the_rational_plane_over_the_integers_has_no_framing() -> None:
    r"""A divisible module is a ``ZZ``-module and is not finitely generated."""
    space, _ = _rational_plane()

    assert space in Modules(ZZ)
    assert space not in FinitelyGeneratedModules(ZZ)


def test_a_lattice_in_the_rational_plane_contains_a_second_lattice() -> None:
    r"""``2 ZZ^2 <= ZZ^2`` inside ``Res(QQ^2)``, and each lift returns its coefficients."""
    space, plane = _rational_plane()
    e0, e1 = plane.module_generator(0), plane.module_generator(1)

    standard = FreeModule(ZZ, 2)
    into_standard = module_embedding(standard, space, {0: space(e0), 1: space(e1)})
    doubled = FreeModule(ZZ, 2)
    into_doubled = module_embedding(doubled, space, {0: space(2 * e0), 1: space(2 * e1)})

    assert into_standard.is_in_image(into_doubled(doubled.module_generator(0)))
    assert into_standard.lift(space(2 * e0)) == 2 * standard.module_generator(0)
    assert into_standard.lift(space(e0 + 3 * e1)) == standard.module_generator(0) + 3 * standard.module_generator(1)

    factorization = into_doubled.factor_through(into_standard)

    assert factorization.domain() is doubled
    assert factorization.codomain() is standard
    assert factorization(doubled.module_generator(1)) == 2 * standard.module_generator(1)


def test_a_half_integral_vector_of_the_rational_plane_is_not_in_a_lattice() -> None:
    r"""``e0/2`` is in the ``QQ``-span of ``ZZ^2`` and not in its ``ZZ``-span."""
    space, plane = _rational_plane()
    e0, e1 = plane.module_generator(0), plane.module_generator(1)

    standard = FreeModule(ZZ, 2)
    into_standard = module_embedding(standard, space, {0: space(e0), 1: space(e1)})
    half = space(plane.scalar_multiple(QQ(1) / 2, e0))

    assert not into_standard.is_in_image(half)


def test_a_vector_outside_the_rational_span_of_a_line_is_not_in_it() -> None:
    r"""``ZZ e0`` contains its own multiples and no multiple of ``e1``."""
    space, plane = _rational_plane()
    e0, e1 = plane.module_generator(0), plane.module_generator(1)

    line = FreeModule(ZZ, 1)
    into_line = module_embedding(line, space, {0: space(e0)})

    assert into_line.is_in_image(space(-3 * e0))
    assert into_line.lift(space(-3 * e0)) == -3 * line.module_generator(0)
    assert not into_line.is_in_image(space(e1))

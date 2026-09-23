r"""The five functors out of ``Mod_R``, asked for on that category.

A functor is a method of its domain category, so ``Mod_R`` is where the
underlying set, the linear dual, and the three free-algebra constructions are
spelled.  Each is applied here to one specimen: the free ``ZZ``-module of rank
two, and the involution of it that exchanges the two basis vectors.
"""

from dzack_research.preamble.all import (
    ZZ,
    Algebras,
    AlternatingAlgebras,
    Modules,
)


def _plane_with_swap():
    r"""``ZZ^2`` and the involution exchanging its two basis vectors."""
    plane = ZZ.free_module(2)
    swap = Modules(ZZ).End(plane)(
        {0: plane.module_generator(1), 1: plane.module_generator(0)}
    )
    return plane, swap






def test_the_symmetric_algebra_functor_is_asked_of_the_module_category() -> None:
    r"""``Sym_ZZ`` is commutative and ``Sym^2(ZZ^2)`` has rank three."""
    plane, swap = _plane_with_swap()
    symmetric = Modules(ZZ).symmetric_algebra()

    assert symmetric.codomain() == Algebras(Modules(ZZ).base_ring()).Associative().Unital().Commutative()
    algebra = symmetric(plane)
    assert algebra in Algebras(ZZ).Associative().Unital().Commutative()
    assert algebra.graded_piece(1).module_rank() == 2
    assert algebra.graded_piece(2).module_rank() == 3
    x, y = algebra.algebra_generator(0), algebra.algebra_generator(1)
    assert x * y == y * x

    image = symmetric(swap)
    assert image.domain() is algebra
    assert image.codomain() is algebra
    assert image(x) == y


def test_the_tensor_algebra_functor_is_asked_of_the_module_category() -> None:
    r"""``T_ZZ`` is noncommutative and ``T^2(ZZ^2)`` has rank four."""
    plane, swap = _plane_with_swap()
    tensor = Modules(ZZ).tensor_algebra()

    assert tensor.codomain() == Algebras(Modules(ZZ).base_ring())
    algebra = tensor(plane)
    assert algebra in Algebras(ZZ)
    assert algebra.graded_piece(1).module_rank() == 2
    assert algebra.graded_piece(2).module_rank() == 4
    x, y = algebra.algebra_generator(0), algebra.algebra_generator(1)
    assert x * y != y * x

    image = tensor(swap)
    assert image.domain() is algebra
    assert image.codomain() is algebra
    assert image(x) == y


def test_the_exterior_algebra_functor_is_asked_of_the_module_category() -> None:
    r"""``Lambda_ZZ`` is alternating and ``Lambda^2(ZZ^2)`` has rank one."""
    plane, swap = _plane_with_swap()
    exterior = Modules(ZZ).exterior_algebra()

    assert exterior.codomain() == AlternatingAlgebras(Modules(ZZ).base_ring())
    algebra = exterior(plane)
    assert algebra in AlternatingAlgebras(ZZ)
    assert algebra.graded_piece(1).module_rank() == 2
    assert algebra.graded_piece(2).module_rank() == 1
    x, y = algebra.algebra_generator(0), algebra.algebra_generator(1)
    assert x * x == algebra.zero()
    assert x * y == -(y * x)

    image = exterior(swap)
    assert image.domain() is algebra
    assert image.codomain() is algebra
    assert image(x) == y



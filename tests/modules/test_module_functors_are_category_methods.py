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
    CommutativeAlgebras,
    FinitelyGeneratedFreeModules,
    FreeModule,
    Modules,
    Sets,
)


def _plane_with_swap():
    r"""``ZZ^2`` and the involution exchanging its two basis vectors."""
    plane = FreeModule(ZZ, 2)
    swap = Modules(ZZ).End(plane)(
        {0: plane.module_generator(1), 1: plane.module_generator(0)}
    )
    return plane, swap


def test_the_underlying_set_functor_is_asked_of_the_module_category() -> None:
    r"""``U : Mod_ZZ -> Set`` drops the scalar action and keeps every element."""
    plane, swap = _plane_with_swap()
    underlying = Modules(ZZ).underlying_set()

    assert underlying.codomain() == Sets()
    assert underlying(plane) in Sets()
    assert underlying(plane) is plane

    image = underlying(swap)
    assert image.domain() is underlying(plane)
    assert image.codomain() is underlying(plane)
    assert image(plane.module_generator(0)) == swap(plane.module_generator(0))


def test_dualization_is_asked_of_the_module_category() -> None:
    r"""``Hom_ZZ(-, ZZ)`` keeps the rank and sends the swap to its transpose."""
    plane, swap = _plane_with_swap()
    dualize = Modules(ZZ).dualization()

    assert dualize.codomain() == FinitelyGeneratedFreeModules(Modules(ZZ).base_ring())
    dual = dualize(plane)
    assert dual in FinitelyGeneratedFreeModules(ZZ)
    assert dual.rank() == plane.rank()

    transpose = dualize(swap)
    assert transpose.domain() is dual
    assert transpose.codomain() is dual
    assert transpose(dual.module_generator(0)) == dual.module_generator(1)


def test_the_symmetric_algebra_functor_is_asked_of_the_module_category() -> None:
    r"""``Sym_ZZ`` is commutative and ``Sym^2(ZZ^2)`` has rank three."""
    plane, swap = _plane_with_swap()
    symmetric = Modules(ZZ).symmetric_algebra()

    assert symmetric.codomain() == CommutativeAlgebras(Modules(ZZ).base_ring())
    algebra = symmetric(plane)
    assert algebra in CommutativeAlgebras(ZZ)
    assert algebra.graded_piece(1).rank() == 2
    assert algebra.graded_piece(2).rank() == 3
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
    assert algebra.graded_piece(1).rank() == 2
    assert algebra.graded_piece(2).rank() == 4
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
    assert algebra.graded_piece(1).rank() == 2
    assert algebra.graded_piece(2).rank() == 1
    x, y = algebra.algebra_generator(0), algebra.algebra_generator(1)
    assert x * x == algebra.zero()
    assert x * y == -(y * x)

    image = exterior(swap)
    assert image.domain() is algebra
    assert image.codomain() is algebra
    assert image(x) == y


def test_the_free_algebra_adjunctions_are_asked_of_the_module_category() -> None:
    r"""``Sym_ZZ -| U`` and ``T_ZZ -| U`` produce a unit and a counit on ``ZZ^2``.

    The unit is the degree-one inclusion of the module into the underlying
    module of its free algebra, so it is injective; the counit evaluates the
    free algebra on an algebra's own underlying module back onto that algebra.
    """
    plane, _ = _plane_with_swap()
    modules = Modules(ZZ)

    for adjunction, degree_two_rank in (
        (modules.symmetric_algebra_adjunction(), 3),
        (modules.tensor_algebra_adjunction(), 4),
    ):
        algebra = adjunction.left_adjoint()(plane)
        assert algebra.graded_piece(2).rank() == degree_two_rank

        unit = adjunction.unit(plane)
        assert unit.domain() is plane
        assert unit.codomain() == adjunction.right_adjoint()(algebra)
        assert unit.is_injective()

        counit = adjunction.counit(algebra)
        assert counit.codomain() is algebra
        assert counit.domain() is adjunction.left_adjoint()(
            adjunction.right_adjoint()(algebra)
        )

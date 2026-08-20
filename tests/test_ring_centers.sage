r"""The centre of a ring, as the question a session can actually ask.

$Z(R)=\{z\in R:zr=rz\text{ for all }r\}$ is a subring nobody can hand you
generators for: for a free construction on two letters the centre is a
theorem, and for a ring given by a multiplication table it is a computation
that does not finish.  What is always available is *membership* -- deciding
$z\in Z(R)$ -- and deciding it needs only a generating set, because the
centralizer of one element is a subring and so contains everything the
elements it centralizes generate.

So the centre here is a carve-out by predicate, exactly as a subgroup of
$O(L)$ is, and the specimens below are the two halves of that: what the
carve-out answers, and what it refuses to answer.

$Z$ is also a functor, but not on all of $\mathbf{Rings}$: only on the
isomorphisms.  That restriction is the ``core`` of a category, and the
refusal of a non-invertible arrow is the last specimen.
"""

from typing import TYPE_CHECKING

import pytest

from sage.categories.category import Category

if TYPE_CHECKING:
    from dzack_research.preamble.categories.algebras.framed_free_algebras import (
        FramedFreeAlgebras,
        FreeAlgebraParent,
    )


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _wedge_algebra() -> "tuple[FreeAlgebraParent, FramedFreeAlgebras.ElementMethods, FramedFreeAlgebras.ElementMethods]":
    r"""Return $\Lambda(F_\QQ(S))$ on two letters, and its two generators."""
    algebra = AlternatingAlgebraOn(QQ, Sets.Δ[1])
    first, second = algebra.algebra_generators()
    return algebra, first, second


def test_a_commutative_ring_is_its_own_centre() -> None:
    r"""$R$ commutative means $Z(R)=R$, and there is nothing to carve out."""
    _ensure_preamble()

    assert QQ.ring_center() is QQ
    assert QQ.is_central(QQ(3))

    polynomials = FreeAlgebraOn(QQ, Sets.Δ[0])
    assert polynomials.ring_center() is polynomials


def test_the_even_part_of_a_wedge_is_central_and_a_generator_is_not() -> None:
    r"""$e_1\wedge e_2$ commutes with everything; $e_1$ does not commute with $e_2$.

    Both facts are the sign rule: moving a degree-two monomial past a
    generator costs two transpositions and moving a generator past a
    generator costs one.  This is the answer the predicate must give, and it
    gives it without knowing $\Lambda^{\text{even}}\oplus\Lambda^{\text{top}}$.
    """
    _ensure_preamble()
    algebra, first, second = _wedge_algebra()

    assert algebra.is_central(first * second)
    assert not algebra.is_central(first)
    assert algebra.is_central(algebra.one())


def test_the_centre_of_a_wedge_is_a_subring_one_can_ask_about() -> None:
    r"""$Z(\Lambda)$ answers membership, and answers it as a subring."""
    _ensure_preamble()
    algebra, first, second = _wedge_algebra()
    centre = algebra.ring_center()

    assert first * second in centre
    assert first not in centre
    assert centre.one() == algebra.one()
    assert centre.zero() == algebra.zero()
    assert centre(first * second) == first * second
    assert centre.ambient_ring() is algebra

    inclusion = centre.inclusion()
    assert inclusion.domain() is centre
    assert inclusion.codomain() is algebra
    assert inclusion(first * second) == first * second


def test_the_centre_of_a_wedge_is_commutative() -> None:
    r"""$Z(R)$ is commutative, whatever $R$ is: its elements commute with all of $R$."""
    from sage.categories.commutative_rings import CommutativeRings

    _ensure_preamble()
    algebra, _, _ = _wedge_algebra()

    assert algebra not in CommutativeRings(), "or the specimen proves nothing"
    assert algebra.ring_center() in CommutativeRings()


def test_a_ring_that_cannot_name_generators_declines() -> None:
    r"""$Z(M_2(\QQ))$ is the scalars, and this preamble does not know it.

    A predicate that answered here would be answering on trust: $M_2(\QQ)$
    names no generating set to test commutation against.  It is the matrix
    units, and saying so is a construction nobody has made here.
    """
    _ensure_preamble()
    matrices = MatrixSpace(QQ, 2)
    centre = matrices.ring_center()

    with pytest.raises(AssertionError):
        matrices.one() in centre


def test_an_infinite_generating_set_is_not_a_finite_check() -> None:
    r"""$\Lambda$ on infinitely many letters cannot decide centrality by testing.

    The centre is still $\Lambda^{\text{even}}$, and it is still a theorem.
    What fails is the carve-out's method of deciding, and it fails loudly
    rather than testing generators until it runs out.
    """
    _ensure_preamble()
    algebra = AlternatingAlgebraOn(QQ, Sets.Δ[Sets.ℵ[0]])
    first = algebra.algebra_generator(0)

    with pytest.raises(AssertionError):
        algebra.is_central(first)


def test_an_algebra_map_corestricts_to_the_centre_when_the_generators_are_central() -> None:
    r"""$f:\QQ[t]\to\Lambda$, $t\mapsto e_1\wedge e_2$, lands in $Z(\Lambda)$.

    Checked on the one generator, which decides it: the image of $f$ is
    generated as a ring by the scalars -- central because $\Lambda$ is a
    $\QQ$-algebra -- and by the images of the generators.
    """
    _ensure_preamble()
    algebra, first, second = _wedge_algebra()
    polynomials = FreeAlgebraOn(QQ, Sets.Δ[0])
    label = next(iter(polynomials.algebra_generating_set()))
    variable = polynomials.algebra_generator(label)

    to_the_top = polynomials.hom({label: first * second})
    corestricted = corestrict_to_center(to_the_top)

    assert corestricted.domain() is polynomials
    assert corestricted.codomain() is algebra.ring_center()
    assert corestricted(variable) == first * second


def test_a_map_whose_generators_leave_the_centre_does_not_corestrict() -> None:
    r"""$t\mapsto e_1$ is an algebra map, and it does not land in $Z(\Lambda)$."""
    _ensure_preamble()
    algebra, first, _ = _wedge_algebra()
    polynomials = FreeAlgebraOn(QQ, Sets.Δ[0])
    label = next(iter(polynomials.algebra_generating_set()))

    to_a_generator = polynomials.hom({label: first})

    with pytest.raises(AssertionError):
        corestrict_to_center(to_a_generator)


def test_the_core_of_a_category_has_the_same_objects() -> None:
    r"""$\operatorname{core}(\mathbf C)$ drops arrows, not objects."""
    _ensure_preamble()
    algebra, _, _ = _wedge_algebra()
    core = Rings().core()

    assert algebra in core
    assert QQ in core
    assert core.ambient_category() is Rings()


def test_a_category_performs_its_constructions_as_an_object_of_Cat() -> None:
    r"""$\mathbf{Cat}$ holds the categories, and the constructions built out
    of a category are the methods it has there."""
    _ensure_preamble()

    assert Rings() in Cat()
    assert QQ not in Cat()

    over_the_rationals = Rings().SliceOver(QQ)

    assert over_the_rationals is SliceOverCategory(Rings(), QQ)
    assert vars(Category)["SliceOver"] is Cat.ParentMethods.SliceOver


def test_the_centre_functor_transports_an_isomorphism() -> None:
    r"""$Z$ carries an isomorphism $A\to A$ to $Z(A)\to Z(A)$."""
    _ensure_preamble()
    algebra, first, second = _wedge_algebra()
    centre_functor = RingCenterFunctor()

    assert centre_functor(algebra) is algebra.ring_center()

    identity = Hom(algebra, algebra, Rings()).identity()
    transported = centre_functor(identity)

    assert transported.domain() is algebra.ring_center()
    assert transported.codomain() is algebra.ring_center()
    assert transported(first * second) == first * second


def test_the_centre_functor_refuses_an_arrow_that_is_not_invertible() -> None:
    r"""$Z$ is a functor on $\operatorname{core}(\mathbf{Rings})$ and nothing wider.

    The inclusion $\QQ[t]\hookrightarrow\Lambda$, $t\mapsto e_1$, is the
    reason: $t$ is central in $\QQ[t]$ and $e_1$ is not central in $\Lambda$,
    so there is no map $Z(\QQ[t])\to Z(\Lambda)$ to be had.
    """
    _ensure_preamble()
    algebra, first, _ = _wedge_algebra()
    polynomials = FreeAlgebraOn(QQ, Sets.Δ[0])
    label = next(iter(polynomials.algebra_generating_set()))
    centre_functor = RingCenterFunctor()

    not_invertible = polynomials.hom({label: first})

    with pytest.raises(AssertionError):
        centre_functor(not_invertible)

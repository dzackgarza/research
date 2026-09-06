r"""Every owned ring is a ``ZZ``-algebra, and every commutative one an algebra over itself.

The placement is made once, at construction, for every route that builds an
owned ring; what it buys is the algebra homsets into the ring itself, such as
the augmentation ``R[G] -> R`` for a number field ``R``.
"""

from typing import Any, cast

import pytest

from dzack_research.preamble.all import (
    RR,
    Algebras,
    CommutativeAlgebras,
    Fields,
    FinitelyGeneratedFreeModules,
    FreeModule,
    Groups,
    Modules,
    OwnedRings,
    ring_as_module,
)
from dzack_research.preamble.rings import (
    predicate_subring,
    ring_constructor_surface,
    session_ring_objects,
)

_RINGS = session_ring_objects()
_CONSTRUCTORS = ring_constructor_surface()
QQ = cast(Any, _RINGS["QQ"])
ZZ = cast(Any, _RINGS["ZZ"])
GF = cast(Any, _CONSTRUCTORS["GF"])
PolynomialRing = cast(Any, _CONSTRUCTORS["PolynomialRing"])
QuadraticField = cast(Any, _CONSTRUCTORS["QuadraticField"])
Zmod = cast(Any, _CONSTRUCTORS["Zmod"])


def _commutative_rings() -> dict[str, Any]:
    return {
        "QQ": QQ,
        "QQ(i)": QuadraticField(-1, "i"),
        "GF(5)": GF(5),
        "ZZ_(5)": ZZ.localize_at_prime(5),
        "QQ[x]": PolynomialRing(QQ, "x"),
        "Z/12": Zmod(12),
        "ZZ[C2]": ZZ[Groups.C(2)],
    }


@pytest.fixture(params=sorted(_commutative_rings()), ids=str)
def promoted_ring(request: Any) -> Any:
    return _commutative_rings()[request.param]


def test_a_commutative_ring_is_a_commutative_algebra_over_itself_and_over_the_integers(
    promoted_ring: Any,
) -> None:
    ring = promoted_ring
    assert ring in CommutativeAlgebras(ring)
    assert ring in Algebras(ZZ)
    assert ring in Modules(ring)
    identity = Algebras(ring).Mor(ring, ring).identity()
    element = ring.one() + ring.one()
    assert identity(element) == element


def test_a_noncommutative_ring_is_an_algebra_over_the_integers_only() -> None:
    group_algebra = ZZ[Groups.S(3)]
    assert group_algebra in Algebras(ZZ)
    assert group_algebra not in CommutativeAlgebras(group_algebra)
    assert group_algebra.is_commutative() is False


def test_scalar_restriction_is_visible_in_the_module_and_algebra_category_towers() -> None:
    field = QuadraticField(-1, "i")
    group_algebra = field[Groups.C(2)]

    assert Modules(group_algebra).is_subcategory(Modules(field))
    assert Modules(field).is_subcategory(Modules(QQ))
    assert Modules(QQ).is_subcategory(Modules(ZZ))

    assert Algebras(group_algebra).is_subcategory(Algebras(field))
    assert Algebras(field).is_subcategory(Algebras(QQ))
    assert Algebras(QQ).is_subcategory(Algebras(ZZ))

    assert CommutativeAlgebras(group_algebra).is_subcategory(CommutativeAlgebras(field))
    assert CommutativeAlgebras(field).is_subcategory(CommutativeAlgebras(QQ))


def test_the_augmentation_of_a_group_algebra_over_a_number_field_is_an_algebra_morphism() -> None:
    field = QuadraticField(-1, "i")
    group = Groups.S(3)
    group_algebra = field[group]
    augmentation = group_algebra.augmentation()
    assert augmentation in Algebras(field).Mor(group_algebra, field)
    generator = group.group_generators().unrank(0)
    two_elements = group_algebra(generator) + 3 * group_algebra(group.one())
    assert augmentation(two_elements) == field(4)

    permutation = Modules(field[group])(
        FreeModule(field, 2),
        lambda group_element, vector: vector,
    )
    assert permutation.module_invariants().rank() == 2


def test_a_self_algebra_keeps_the_ring_morphism_homset_as_its_default_mor() -> None:
    real_ring = cast(Any, RR)
    assert real_ring.Mor(real_ring) is OwnedRings().Mor(real_ring, real_ring)
    identity = real_ring.Mor(real_ring)(lambda element: real_ring(element))
    assert identity(RR(2)) == RR(2)


def test_the_endomorphism_ring_contains_the_base_ring_as_scalar_endomorphisms() -> None:
    module = FreeModule(QQ, 2)
    endomorphisms = Modules(QQ).End(module)
    generator = module.module_generator(0)
    scalar_two = endomorphisms(2)

    assert scalar_two(generator) == 2 * generator
    assert endomorphisms.algebra_structure_morphism()(QQ(2)) == scalar_two


def test_commutativity_and_localization_remain_coherent_on_non_engine_ring_parents() -> None:
    subring = predicate_subring(
        QQ,
        lambda element: element.denominator() == 1,
        "the denominator is one",
    )
    assert subring.is_commutative() is True
    assert subring in CommutativeAlgebras(subring)

    localization = QQ.localize_at_prime(QQ.ideal(QQ.zero()))
    assert localization.localization_source() is QQ
    assert localization.residue_field() in Fields()


def test_a_ring_over_nothing_smaller_is_its_own_scalar_ring(promoted_ring: Any) -> None:
    r"""A ring states its own scalars when nothing smaller presents it.

    A ring is free of rank one over its own scalars, so it is a rank-one
    algebra over itself whatever else it is.  Where no smaller base was
    chosen, that canonical structure is the answer, not an error and not a
    stand-in for a declaration nobody made.
    """
    ring = promoted_ring
    scalars = ring.algebra_base_ring()
    assert scalars is not None
    assert ring in Algebras(scalars)
    assert ring in Modules(scalars)


def test_the_integers_are_an_algebra_over_themselves() -> None:
    r"""The integers have nothing smaller beneath them, so they are their own base.

    The module membership is not a separate fact: the algebras over a ring
    have the modules over it among their supercategories, so the placement
    made at construction carries it.
    """
    assert ZZ.algebra_base_ring() is ZZ
    assert ZZ.base_ring() is ZZ
    assert ZZ in CommutativeAlgebras(ZZ)
    assert ZZ in Modules(ZZ)


def test_a_ring_is_the_rank_one_free_module_over_itself(promoted_ring: Any) -> None:
    r"""A ring *is* its own regular module, rather than having one beside it.

    One object sits in several categories: a ring is a ring, a rank-one free
    module over itself, and a rank-one algebra over itself.  So the ring
    answers for its own rank, and the canonical free rank-one module over it
    is the ring, not a second object built to stand for it.

    This is expected to fail today, and the failure is the point.  Nothing
    places a ring among the finitely generated free modules over itself, so
    ``ring_as_module`` takes its second branch and returns a separate
    ``BasedFreeModule`` of rank one.  The branch above it already expects the
    identification and is unreachable.  What would supply it is that
    placement, with the framing on the ring's own unit, made where the ring is
    placed as an algebra over itself.
    """
    ring = promoted_ring
    assert ring in FinitelyGeneratedFreeModules(ring)
    assert ring.module_generating_set().cardinality() == 1
    assert ring_as_module(ring) is ring

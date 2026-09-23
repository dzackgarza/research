from dzack_research.preamble.all import *


def factors():
    return Sets.Δ[1], Sets.Δ[2]


def coproduct():
    return Sets().coproduct(factors())


def test_the_category_and_the_object_constructions_agree() -> None:
    two, three = factors()
    assert two.coproduct_with(three) == coproduct()


def test_the_categories_of_the_coproduct() -> None:
    assert coproduct() in Sets()
    assert coproduct() in FiniteSets()


def test_the_coproduct_is_the_disjoint_union() -> None:
    assert coproduct().cardinality() == 5


def test_the_injections() -> None:
    two, three = factors()
    union = coproduct()
    assert union.injection(0).domain() is two
    assert union.injection(1).domain() is three
    assert union.injection(0).is_injective()
    assert union.injection(1).is_injective()
    assert union.injection(0)(two(0)) != union.injection(1)(three(0))


def test_the_coproduct_has_one_endomorphism_category() -> None:
    union = coproduct()
    endomorphisms = union.Mor(union)
    identity = endomorphisms.identity()
    assert endomorphisms in Cat()
    assert union.Mor(union) is endomorphisms
    assert identity * identity == identity

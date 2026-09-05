from dzack_research.preamble.all import *  # noqa: F401,F403


def test_the_group_algebra_functor_extends_a_subgroup_inclusion_linearly() -> None:
    symmetric = Groups.S(3)
    rotation = symmetric.group_generators().unrank(0)
    cyclic = symmetric.subgroup([rotation])
    functor = Groups().group_algebra(QQ)

    inclusion = functor(cyclic.inclusion())

    assert inclusion.domain() is QQ[cyclic]
    assert inclusion.codomain() is QQ[symmetric]
    h = cyclic(rotation)
    assert inclusion(QQ[cyclic](h) + 2 * QQ[cyclic](h * h)) == QQ[symmetric](
        rotation
    ) + 2 * QQ[symmetric](rotation * rotation)


def test_the_group_inclusion_lands_in_the_units() -> None:
    symmetric = Groups.S(3)
    algebra = QQ[symmetric]
    inclusion = algebra.group_inclusion()
    rotation = symmetric.group_generators().unrank(0)
    transposition = symmetric((1, 2))

    assert inclusion(rotation) * inclusion(rotation.inverse()) == algebra.one()
    assert inclusion(rotation * transposition) == inclusion(rotation) * inclusion(transposition)
    assert inclusion(rotation * transposition) != inclusion(transposition) * inclusion(rotation)


def test_the_augmentation_over_the_integers_lands_in_the_session_integers() -> None:
    symmetric = Groups.S(3)
    algebra = ZZ[symmetric]
    augmentation = algebra.augmentation()

    assert augmentation.codomain() is ZZ
    assert augmentation(sum(algebra(g) for g in symmetric)) == 6
    assert augmentation(algebra(symmetric((1, 2))) - algebra.one()) == 0


def test_maschke_decides_semisimplicity_by_the_group_order() -> None:
    symmetric = Groups.S(3)

    assert GF(5)[symmetric].is_semisimple()
    assert not GF(3)[symmetric].is_semisimple()
    assert not ZZ[Groups.C(2)].is_semisimple()


def test_the_centre_of_the_symmetric_group_algebra_counts_partitions() -> None:
    assert QQ[Groups.S(4)].center().dimension() == 5
    assert QQ[Groups.S(4)].center().dimension() == Groups.S(4).conjugacy_classes_representatives().cardinality()

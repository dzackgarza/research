r"""Schreier words are selected free-group augmentations, not bare tuples."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_kernel_of_c4_to_c2_has_a_schreier_epimorphism() -> None:
    four, two = Groups.C(4), Groups.C(2)
    s, t = next(iter(four.group_generators())), next(iter(two.group_generators()))
    reduction = four.Mor(two)({s: t})
    kernel = reduction.kernel()
    augmentation = kernel.schreier_generating_morphism()
    words = kernel.schreier_generators()

    assert augmentation.domain().free_basis() == words.index_set()
    assert augmentation.codomain() is kernel
    assert words.index_set() in FiniteSets()
    assert all(reduction(augmentation(g)) == two.one() for g in augmentation.domain().group_generators())
    assert all(augmentation(augmentation.domain().free_generator(label)) == words.value(label) for label in words.index_set())
    assert four.subgroup(augmentation(g) for g in augmentation.domain().group_generators()).cardinality() == cardinal(2)


def test_preimage_schreier_generators_keep_the_free_basis_index() -> None:
    four = Groups.C(4)
    s = next(iter(four.group_generators()))
    subgroup = four.subgroup((s**2,))
    identity = four.Mor(four).identity()
    preimage = identity.preimage_subgroup(subgroup)
    augmentation = preimage.schreier_generating_morphism()
    words = preimage.schreier_generators()

    assert augmentation.domain().free_basis() == words.index_set()
    assert augmentation.codomain() is preimage
    assert words.index_set() == augmentation.domain().group_generating_set()
    assert all(augmentation(g) in preimage for g in augmentation.domain().group_generators())

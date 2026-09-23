r"""Archived lattice similarities on the live twist/isometry construction.

A similarity of scale ``a`` from ``L`` to ``M`` is an isometry ``L(a) -> M``.
The archived API exposed both the existence predicate and the actual morphism.
The hyperbolic plane and its scale-two twist distinguish this from ordinary
isometry because their determinants differ by a factor of four.
"""

from dzack_research.preamble.all import ZZ, Lattices


def test_archived_scale_two_similarity_is_an_actual_isometry_from_the_twist() -> None:
    source = Lattices(ZZ)("U")
    target = source.twist(2)
    images = target.module_generators()

    similarity = source.similarity(2, images, codomain=target)

    assert similarity.domain().gram_tensor() == source.twist(2).gram_tensor()
    assert similarity.codomain() is target
    for source_generator, target_generator in zip(
        similarity.domain().module_generators(),
        target.module_generators(),
        strict=True,
    ):
        assert similarity(source_generator) == target_generator


def test_archived_similarity_predicate_does_not_conflate_similarity_with_isometry() -> None:
    source = Lattices(ZZ)("U")
    target = source.twist(2)

    assert source.is_similar(target, 2) is True
    assert source.is_isometric(target) is False
    assert abs(source.determinant()) == 1
    assert abs(target.determinant()) == 4


def test_archived_wrong_similarity_scale_is_rejected_by_the_form_mor() -> None:
    source = Lattices(ZZ)("U")
    target = source.twist(2)

    assert source.is_similar(target, 1) is False

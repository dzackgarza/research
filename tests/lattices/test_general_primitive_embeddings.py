r"""Primitive embeddings into specified non-unimodular indefinite targets."""

from dzack_research.preamble.all import Lattices, ZZ


def test_a1_embeds_primitively_into_u_plus_a1_with_an_actual_map() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U") + Lattices(ZZ)("A1")
    embedding = source.Emb(target).an_element()

    assert embedding.domain() is source
    assert embedding.codomain() is target
    assert embedding.is_primitive()
    generator = source.module_generator(0)
    assert target.q(embedding(generator)) == source.q(generator)


def test_target_specific_embedding_decision_is_not_the_even_unimodular_special_case() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U") + Lattices(ZZ)("A1")

    assert not target.is_unimodular()
    assert source.Emb(target).is_empty() is False

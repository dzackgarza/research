r"""Primitive embeddings into specified non-unimodular indefinite targets."""

from dzack_research.preamble.all import ZZ, Lattices


def test_a1_embeds_primitively_into_u_plus_a1_with_an_actual_map() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U") + Lattices(ZZ)("A1")
    embedding = source.Emb(target).an_element()

    assert embedding.domain() is source
    assert embedding.codomain() is target
    assert embedding.is_primitive()
    generator = source.basis_vector(0)
    assert target.q(embedding(generator)) == source.q(generator)


def test_target_specific_embedding_decision_is_not_the_even_unimodular_special_case() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U") + Lattices(ZZ)("A1")

    assert not target.is_unimodular()
    assert source.Emb(target).is_empty() is False


def test_target_specific_primitive_embedding_classes_are_actual_maps() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U") + Lattices(ZZ)("A1")
    homset = source.Emb(target)

    representatives = homset.primitive_embedding_class_representatives("emb")
    assert representatives.cardinality() > 0
    for embedding in representatives:
        assert embedding.parent() is homset
        assert embedding.is_primitive()
        assert embedding.domain() is source
        assert embedding.codomain() is target


def test_embedding_classification_names_the_equivalence_relation() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U") + Lattices(ZZ)("A1")
    homset = source.Emb(target)

    sublattice_classes = homset.primitive_embedding_class_representatives("sub")
    embedding_classes = homset.primitive_embedding_class_representatives("emb")
    assert sublattice_classes.cardinality() > 0
    assert embedding_classes.cardinality() >= sublattice_classes.cardinality()

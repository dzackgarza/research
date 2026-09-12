r"""Archive reconciliation for arithmetic attached to a number field.

The archived number-field category exposed class number, ramified primes,
Galois structure, embeddings and conjugates in addition to the presentation
of the field.  These operations now belong to the live owned number-field
object itself.  The Gaussian field gives a source-standard exact specimen:
its maximal order is ``ZZ[i]``, of class number one and discriminant ``-4``.
"""

from dzack_research.preamble.all import ZZ, QuadraticField


def test_gaussian_field_retains_class_number_ramification_and_galois_group() -> None:
    field = QuadraticField(-1, "i")

    assert field.discriminant() == ZZ(-4)
    assert field.class_number() == ZZ(1)
    assert tuple(field.ramified_primes()) == (ZZ(2),)
    assert field.is_galois() is True
    assert field.galois_group().order() == 2


def test_gaussian_primitive_element_has_two_owned_embedding_images() -> None:
    field = QuadraticField(-1, "i")
    primitive = field.primitive_element()
    embeddings = field.embeddings(field)
    images = field.embedding_images(field)
    conjugates = primitive.conjugates(field)

    assert embeddings.cardinality() == 2
    assert images.cardinality() == 2
    assert set(images) == {primitive, -primitive}
    assert conjugates.index_set() is embeddings
    assert conjugates.cardinality() == 2
    assert {conjugates[embedding] for embedding in embeddings} == {
        primitive,
        -primitive,
    }

from dzack_research.preamble.all import QuadraticField


def test_number_field_element_polynomials_keep_their_distinct_degrees() -> None:
    field = QuadraticField(5, "a")
    one = field.one()

    characteristic = one.characteristic_polynomial()
    minimal = one.minimal_polynomial()

    assert characteristic.degree() == field.degree()
    assert minimal.degree() == 1
    assert characteristic != minimal


def test_number_field_integrality_is_not_membership_in_the_selected_power_order() -> None:
    field = QuadraticField(5, "a")
    a = field.primitive_element()
    integral = (field.one() + a) / 2

    assert integral.is_integral()
    assert not (field.one() / 2).is_integral()


def test_conjugates_are_indexed_by_embeddings_and_retain_multiplicity() -> None:
    field = QuadraticField(5, "a")
    closure = field.normal_closure()
    embeddings = field.embeddings(closure)
    conjugates = field.one().conjugates(closure)

    assert conjugates.index_set() is embeddings
    assert conjugates.cardinality() == embeddings.cardinality()
    assert all(value == closure.one() for value in conjugates)

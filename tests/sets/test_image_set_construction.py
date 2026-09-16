from dzack_research.preamble.all import NN, ZZ, Sets, finite_ordered_set


def test_finite_injective_image_reuses_owned_ordered_image_construction() -> None:
    source = Sets.Δ[2]
    target = finite_ordered_set(("a", "b", "c"))
    values = {0: "a", 1: "b", 2: "c"}
    positions = {value: index for index, value in values.items()}
    morphism = Sets().Mor(source, target)(lambda index: target(values[int(index)]))
    inverse = lambda value: source(positions[str(value)])
    image = Sets().image_set(
        morphism,
        source,
        is_injective=True,
        inverse=inverse,
    )

    assert image.source_set() is source
    assert image.image_map() is morphism
    assert image.inverse_on_image()(target("b")) == source(1)
    assert tuple(image) == ("a", "b", "c")
    assert image[1] == "b"
    assert image.cardinality() == 3
    assert repr(image) == "{'a', 'b', 'c'}"


def test_countable_injective_image_transports_enumeration_without_materializing() -> None:
    doubling = Sets().Mor(NN, ZZ)(lambda index: ZZ(2 * int(index)))
    inverse = lambda value: NN(int(value) // 2)
    image = Sets().image_set(
        doubling,
        NN,
        is_injective=True,
        inverse=inverse,
    )

    assert image.source_set() is NN
    assert image.image_map() is doubling
    assert image.inverse_on_image()(ZZ(8)) == NN(4)
    assert image.cardinality() == NN.cardinality()
    assert image[0] == ZZ(0)
    assert image[3] == ZZ(6)
    assert ZZ(8) in image
    assert ZZ(7) not in image
    assert repr(image).startswith("{0, 2, 4, 6, 8, 10, ...}")


def test_finite_noninjective_image_retains_source_map_and_actual_image() -> None:
    source = Sets.Δ[2]
    target = finite_ordered_set(("a", "b"))
    morphism = Sets().Mor(source, target)(
        lambda index: target("a" if int(index) < 2 else "b")
    )

    image = Sets().image_set(morphism, source)

    assert image.source_set() is source
    assert image.image_map() is morphism
    assert tuple(image) == ("a", "b")
    assert image.cardinality() == 2
    assert "a" in image and "b" in image
    assert repr(image) == "{'a', 'b'}"


def test_infinite_noninjective_image_is_owned_without_inventing_decidability() -> None:
    target = Sets.Δ[1]
    parity = Sets().Mor(NN, target)(lambda index: target(int(index) % 2))
    image = Sets().image_set(parity, NN)

    assert image.source_set() is NN
    assert image.image_map() is parity
    assert repr(image) == f"Image of {NN} under {parity}"
    try:
        image.cardinality()
    except AssertionError as error:
        assert "noninjective image" in str(error)
    else:
        raise AssertionError("noninjective infinite image cardinality was guessed")

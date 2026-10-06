"""CI validation by constructing stored mathematical arrows in the preamble.

There are no lattice equations or independent algorithms here.  A stored map is
mathematically valid exactly when the corresponding preamble constructor accepts
it.  Algorithms and constructor contracts are tested at their preamble owners.
"""

from pathlib import Path

import pytest

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import corpus
from latticedb.model import Lattice

REPOSITORY = Path(__file__).resolve().parent.parent.parent
_RINGS = session_ring_objects()
ZZ = _RINGS["ZZ"]
QQ = _RINGS["QQ"]


@pytest.fixture(scope="module")
def loaded() -> corpus.Corpus:
    return corpus.load(REPOSITORY)


def _owned(lattice: Lattice):
    """Construct the preamble object represented by a lattice card."""
    assert lattice.rank is not None and lattice.gram_tensor is not None
    if lattice.integral is not None:
        return Lattices(ZZ)(lattice.gram_tensor)
    return ZZ.free_module(lattice.rank).equip_bilinear_form(QQ, lattice.gram_tensor)


def test_stored_lattice_morphisms_construct_in_the_preamble(loaded: corpus.Corpus) -> None:
    cards = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    owned = {tag: _owned(lattice) for tag, lattice in cards.items()}

    for source_tag, source_card in cards.items():
        for stored in source_card.morphisms:
            target_card = cards[stored.target]
            source = owned[source_tag].twist(stored.scale)
            target = owned[target_card.tag]
            source.Mor(target)(tuple(target(image) for image in stored.images))


def test_integral_root_span_sum_embeddings_construct_in_the_preamble(
    loaded: corpus.Corpus,
) -> None:
    cards = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    category = Lattices(ZZ)

    for target_card in cards.values():
        span = target_card.root_span
        if (
            span is None
            or span.summands is None
            or span.embedding is None
            or target_card.integral is None
            or not span.summands
            or any(cards[summand.tag].integral is None for summand in span.summands)
        ):
            continue
        target = category(target_card.gram_tensor)
        source = category.biproduct(
            tuple(
                category(cards[summand.tag].gram_tensor).twist(summand.scale)
                for summand in span.summands
            )
        )
        source.Mor(target)(tuple(target(row) for row in span.embedding))


def test_local_system_monodromies_construct_as_preamble_automorphisms(
    loaded: corpus.Corpus,
) -> None:
    cards = {entry.lattice.tag: entry.lattice for entry in loaded.entries}

    for entry in loaded.local_systems:
        system = entry.value
        if system.fiber_lattice is None:
            continue
        fiber_card = cards[system.fiber_lattice]
        fiber = _owned(fiber_card)
        for generator in system.monodromy_generators:
            columns = tuple(
                tuple(row[index] for row in generator.matrix)
                for index in range(system.rank)
            )
            fiber.Aut()(tuple(fiber(column) for column in columns))

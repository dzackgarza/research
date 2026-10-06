"""Serialize preamble-owned coordinate diagonal embeddings onto lattice cards.

The mathematical construction is ``Lattices(ZZ).coordinate_diagonal_embeddings``.
This module only constructs the owned lattice objects represented by integral cards,
matches the returned source/target objects back to those cards, extracts coordinates
of the returned typed embeddings, and writes new morphism records.
"""

from pathlib import Path

import frontmatter
from pydantic import TypeAdapter

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import corpus, records
from latticedb.corpus import Corpus
from latticedb.model import Tag, Yaml

ZZ = session_ring_objects()["ZZ"]


def store(root: Path, loaded: Corpus) -> list[str]:
    """Write preamble-computed coordinate diagonal embeddings on source cards."""
    category = Lattices(ZZ)
    owned = []
    entry_by_object_id = {}
    for entry in loaded.entries:
        lattice = entry.lattice
        if lattice.integral is None:
            continue
        value = category(lattice.gram_tensor)
        owned.append(value)
        entry_by_object_id[id(value)] = entry

    new: dict[Tag, list[dict[str, Yaml]]] = {}
    for source, target, scale, embedding, parts in category.coordinate_diagonal_embeddings(tuple(owned)):
        source_entry = entry_by_object_id[id(source)]
        target_entry = entry_by_object_id[id(target)]
        domain = embedding.domain()
        codomain = embedding.codomain()
        source_labels = tuple(domain.module_generating_set())
        target_labels = tuple(codomain.module_generating_set())
        matrix = [
            [
                int(
                    codomain.framing_morphism().lift(
                        embedding(domain.module_generator(source_label))
                    )(target_label)
                )
                for source_label in source_labels
            ]
            for target_label in target_labels
        ]
        numbered_parts = tuple(tuple(position + 1 for position in part) for part in parts)
        sets = " \\sqcup ".join(
            "\\{" + ", ".join(str(position) for position in part) + "\\}"
            for part in numbered_parts
        )
        morphism: dict[str, Yaml] = {
            "target": target_entry.lattice.tag,
            "name": f"Diagonal into the summands ${sets}$",
            "description": (
                "Summand $j$ of the source maps diagonally into the selected coordinate-orthogonal "
                "summands of the target, counted from 1 in the stored basis."
            ),
            "matrix": matrix,
        }
        if scale != 1:
            morphism["scale"] = scale
        held = source_entry.lattice.morphisms
        parsed_matrix = tuple(tuple(int(entry) for entry in row) for row in matrix)
        if any(
            existing.target == target_entry.lattice.tag
            and existing.matrix == parsed_matrix
            and existing.scale == scale
            for existing in held
        ):
            continue
        new.setdefault(source_entry.lattice.tag, []).append(morphism)

    for source, morphisms in new.items():
        path = root / "lattices" / f"{source}.md"
        document = frontmatter.load(str(path))
        metadata = corpus.front_matter(document)
        stored = TypeAdapter(list[dict[str, Yaml]]).validate_python(
            metadata.get("morphisms", [])
        )
        metadata["morphisms"] = stored + morphisms
        path.write_text(records.record_text(metadata, document.content))
    print(
        f"{sum(len(morphisms) for morphisms in new.values())} preamble-computed embeddings written to {len(new)} source lattice cards"
    )
    return []

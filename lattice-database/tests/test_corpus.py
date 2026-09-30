"""A corpus is valid exactly when the statements of a record about other records agree with those records."""

from pathlib import Path

import pytest
import yaml
from latticedb import corpus
from latticedb.model import Yaml


def rank_one(tag: str, value: int) -> dict[str, Yaml]:
    """The lattice of rank 1 with b(e_1, e_1) = value, for value = 2 or value = -2."""
    return {
        "tag": tag,
        "name": f"<{value}>",
        "latex": rf"\langle {value} \rangle",
        "rank": 1,
        "gram_tensor": [[value]],
        "signature": [1, 0] if value > 0 else [0, 1],
        "determinant": value,
        "definiteness": "positive_definite" if value > 0 else "negative_definite",
        "provenance": {"source": "Test record."},
        "integral": {"parity": "even", "discriminant_group": [2]},
    }


def hyperbolic_plane(summands: list[str]) -> dict[str, Yaml]:
    """U with its roots (1, 1) and (1, -1), which have b(r, r) = 2 and b(r, r) = -2 and are orthogonal."""
    return {
        "tag": "0016",
        "name": "U",
        "latex": "U",
        "rank": 2,
        "gram_tensor": [[0, 1], [1, 0]],
        "signature": [1, 1],
        "determinant": -1,
        "definiteness": "indefinite",
        "provenance": {"source": "Test record."},
        "integral": {"parity": "even", "discriminant_group": []},
        "indefinite": {"isotropic": True},
        "root_span": {"roots": [[1, 1], [1, -1]], "summands": summands, "embedding": [[1, 1], [1, -1]]},
    }


def write(directory: Path, *records: dict[str, Yaml]) -> Path:
    for record in records:
        (directory / f"{record['tag']}.md").write_text("---\n" + yaml.safe_dump(record) + "---\n\nA test record.\n")
    return directory


def test_a_root_span_is_accepted_when_its_embedding_has_the_gram_tensor_of_the_sum_of_its_summands(tmp_path: Path) -> None:
    directory = write(tmp_path, rank_one("0002", 2), rank_one("0008", -2), hyperbolic_plane(["0002", "0008"]))
    assert [entry.lattice.tag for entry in corpus.load(directory)] == ["0002", "0008", "0016"]


def test_a_root_span_is_rejected_when_its_summands_are_not_isometric_to_the_image_of_its_embedding(tmp_path: Path) -> None:
    # <2> + <2> is positive definite, and the sublattice of U that (1, 1) and (1, -1) generate is <2> + <-2>.
    directory = write(tmp_path, rank_one("0002", 2), rank_one("0008", -2), hyperbolic_plane(["0002", "0002"]))
    with pytest.raises(corpus.CorpusInvalid) as raised:
        corpus.load(directory)
    assert len(raised.value.problems) == 1


def test_a_root_span_is_rejected_when_a_summand_is_not_a_record_of_the_corpus(tmp_path: Path) -> None:
    directory = write(tmp_path, rank_one("0002", 2), hyperbolic_plane(["0002", "0008"]))
    with pytest.raises(corpus.CorpusInvalid) as raised:
        corpus.load(directory)
    assert len(raised.value.problems) == 1

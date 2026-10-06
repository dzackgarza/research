"""Validation: SageMath genus computations over the full corpus.

Runs only as `just test-validation` and in CI, never as `just test`.
"""

import shutil
from pathlib import Path

import frontmatter
import pytest

from latticedb import certificates, corpus, genus, records
from latticedb.model import Lattice, Yaml

REPOSITORY = Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="module")
def loaded() -> corpus.Corpus:
    """The full corpus."""
    return corpus.load(REPOSITORY)


@pytest.fixture(scope="module")
def a2(loaded: corpus.Corpus) -> Lattice:
    return next(
        entry.lattice for entry in loaded.entries if entry.lattice.tag == "0012"
    )


def test_sagemath_computes_the_invariants_of_a2(loaded: corpus.Corpus) -> None:
    # A2 (record 0012) has rank 2, so no spinor genera are computed.
    # It is alone in its genus, and O(A2) is the dihedral group of order 12 (Conway and Sloane, SPLAG, Chapter 4, Section 6.1).
    # O(A2) = W(A2) x {1, -1}, and -1 acts on A_L = Z/3 by -1 while W(A2) acts trivially, so O~(A2) = W(A2): it is simply transitive on the 6 roots,
    # its rotations of order 3 have 2 orbits on them, and so do SO~ = O~ n SO. The norms of A2 are 2, 6, 8, ..., so c(1) = c(3) = c(4) = 0.
    one = {"constant": 0, "z": [0, 1, 0, 0], "w": [0, 0, 0, 0]}
    two = {"constant": 0, "z": [0, 2, 0, 0], "w": [0, 0, 0, 0]}
    [values] = genus.computed(
        genus.requests(loaded, {}, ("0012",), seconds=60), seconds=60
    )
    assert {
        field: values[field]
        for field in genus.BLOCKS
        if field in values and field != "discriminant_sequence"
    } == {
        "genus_symbol": "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)",
        "automorphism_group_order": 12,
        "genus_class_count": 1,
        "overlattice_count": 1,
        "hyperbolic_index": 0,
        "primitive_orbits": {
            "O": one,
            "SO": one,
            "Otilde": one,
            "SOtilde": two,
            "O+": one,
            "SO+": one,
            "Otilde+": two,
            "SOtilde+": two,
        },
    }


def test_discriminant_sequence_keeps_the_pointed_coset_quotient(
    tmp_path: Path,
) -> None:
    # For A2, O(L) has order 12 and surjects onto O(q_L) = C2. For <2> + <10>,
    # O(L) consists of the two independent sign changes, while O(q_L) has order 4;
    # the image has order 2, so the pointed coset set has two elements.
    chosen: list[dict[str, Yaml]] = [
        {
            "tag": "A2",
            "gram": [[2, -1], [-1, 2]],
            "sign": 1,
            "fields": ["discriminant_sequence"],
        },
        {
            "tag": "<2>+<10>",
            "gram": [[2, 0], [0, 10]],
            "sign": 1,
            "fields": ["discriminant_sequence"],
        },
    ]
    found = {
        str(result["tag"]): result["discriminant_sequence"]
        for result in genus.computed(chosen, seconds=60)
    }
    assert found["A2"]["lattice_group_order"] == 12
    assert found["A2"]["discriminant_group_order"] == 2
    assert found["A2"]["image_order"] == 2
    assert len(found["A2"]["coset_representatives"]) == 1
    assert found["A2"]["mm_trivial"] is True
    assert found["<2>+<10>"]["discriminant_factors"] == [2, 10]
    assert found["<2>+<10>"]["discriminant_group_order"] == 4
    assert found["<2>+<10>"]["image_order"] == 2
    assert len(found["<2>+<10>"]["coset_representatives"]) == 2
    assert found["<2>+<10>"]["mm_trivial"] is False
    assert found["<2>+<10>"]["quotient_multiplication"] == [[0, 1], [1, 0]]
    (tmp_path / "lattices").mkdir()
    path = tmp_path / "lattices" / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    genus.store(path, {"discriminant_sequence": found["A2"]})
    stored = frontmatter.load(str(path)).metadata["integral"]["discriminant_sequence"]
    assert len(stored["lattice_generator_morphisms"]) == len(
        found["A2"]["lattice_generators"]
    )
    assert "lattice_generators" not in stored
    lattice = Lattice.model_validate(frontmatter.load(str(path)).metadata)
    self_isometries = [morphism for morphism in lattice.morphisms if morphism.target == "0012"]
    assert len(self_isometries) == len(found["A2"]["lattice_generators"])


def test_sagemath_computes_the_hyperbolic_index() -> None:
    # U + U + E8(-1) has hyperbolic index 2; U(2) + <-2> has 0, because its discriminant group (Z/2)^3 needs rank 3;
    # I_{1,1} is odd unimodular and U is even, so it has 0; I_{2,1} is U + <1>.
    plane = [[0, 1], [1, 0]]
    gram_tensor = frontmatter.load(str(REPOSITORY / "lattices" / "0094.md")).metadata[
        "gram_tensor"
    ]
    negative_e8: list[list[int]] = [[-int(x) for x in row] for row in gram_tensor]
    grams: dict[str, list[list[int]]] = {
        "U+U+E8(-1)": block_sum(plane, plane, negative_e8),
        "U(2)+<-2>": block_sum([[0, 2], [2, 0]], [[-2]]),
        "I_{1,1}": block_sum([[1]], [[-1]]),
        "I_{2,1}": block_sum([[1]], [[1]], [[-1]]),
    }
    chosen: list[dict[str, Yaml]] = [
        {"tag": tag, "gram": gram, "sign": 0, "fields": ["hyperbolic_index"]}
        for tag, gram in grams.items()
    ]
    computed = {
        str(values["tag"]): values["hyperbolic_index"]
        for values in genus.computed(chosen, seconds=60)
    }
    assert computed == {"U+U+E8(-1)": 2, "U(2)+<-2>": 0, "I_{1,1}": 0, "I_{2,1}": 1}


def test_sagemath_computes_the_discriminant_orbits_of_an_even_lattice_that_contains_two_hyperbolic_planes() -> (
    None
):
    # U + U + <-2> has A_L = Z/2 with q(a) = -1/2, and O(q_L) = 1. A primitive v has v* + L = 0 when div(v) = 1, which needs b(v, v) even,
    # and v* + L = a when div(v) = 2, which needs b(v, v) / 4 = -1/2 mod 2: of norms in [-4, 4] only -2. So c(-2) = 2 and c(n) = 1 for the other even n.
    plane = [[0, 1], [1, 0]]
    [values] = genus.computed(
        [
            {
                "tag": "U+U+<-2>",
                "gram": block_sum(plane, plane, [[-2]]),
                "sign": 0,
                "fields": ["discriminant_orbits"],
            }
        ],
        seconds=60,
    )
    series = {"constant": 1, "z": [0, 1, 0, 1], "w": [0, 2, 0, 1]}
    assert values["discriminant_orbits"] == dict.fromkeys(
        ("O", "SO", "Otilde", "SOtilde", "O+", "SO+", "Otilde+", "SOtilde+"), series
    )


def test_the_discriminant_orbits_are_computed_only_when_the_lattice_is_even_and_contains_two_hyperbolic_planes(
    loaded: corpus.Corpus, a2: Lattice
) -> None:
    # Record 0036 is U + U(2), even with no stored hyperbolic index; record 0015 is the odd lattice I_{1,1}.
    by_tag = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    assert genus.applies("discriminant_orbits", by_tag["0036"], 2)
    assert not genus.applies("discriminant_orbits", by_tag["0036"], 1)
    assert not genus.applies("discriminant_orbits", by_tag["0015"], 2)
    # F_{L,Gamma} is computed for a definite lattice, and F_{A_L,Gamma} is not.
    assert genus.applies("primitive_orbits", a2, 0)
    assert not genus.applies("discriminant_orbits", a2, 0)


def test_sagemath_computes_the_spinor_genera() -> None:
    # SPLAG, Chapter 15, Section 9.6: the genus of A2 + <18> has two spinor genera, one with the form and one with a second representative.
    # Genus(G).representatives() finds two classes, so each spinor genus holds one.
    # SPLAG, Chapter 15, Section 11: the genus of diag(-1, 64, 2) has two spinor genera and hence two classes.
    chosen: list[dict[str, Yaml]] = [
        {
            "tag": "SPLAG 9.6",
            "gram": [[2, 1, 0], [1, 2, 0], [0, 0, 18]],
            "sign": 1,
            "fields": ["genus_class_count", "spinor_genus_count", "spinor_genera"],
        },
        {
            "tag": "SPLAG 11",
            "gram": [[-1, 0, 0], [0, 64, 0], [0, 0, 2]],
            "sign": 0,
            "fields": ["genus_class_count", "spinor_genus_count", "spinor_genera"],
        },
    ]
    computed = {
        str(values.pop("tag")): values for values in genus.computed(chosen, seconds=60)
    }
    expected = {
        "genus_class_count": 2,
        "spinor_genus_count": 2,
        "spinor_genera": [1, 1],
    }
    assert {
        tag: {field: values[field] for field in expected}
        for tag, values in computed.items()
    } == {"SPLAG 9.6": expected, "SPLAG 11": expected}


def block_sum(*blocks: list[list[int]]) -> list[list[int]]:
    size = sum(len(block) for block in blocks)
    rows: list[list[int]] = []
    offset = 0
    for block in blocks:
        rows.extend(
            [0] * offset + row + [0] * (size - offset - len(row)) for row in block
        )
        offset += len(block)
    return rows


def test_a_certified_value_is_not_requested(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    shutil.copy(REPOSITORY / corpus.FAMILIES_FILE, tmp_path / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).write_text("{}\n")
    source = frontmatter.load(str(REPOSITORY / "lattices" / "0012.md"))
    metadata = corpus.front_matter(source)
    a2 = Lattice.model_validate(metadata)
    held = {}
    card_certifications: dict[str, str] = {}
    for field, (block_name, _) in genus.BLOCKS.items():
        block = metadata.get(block_name)
        value = block.get(field) if isinstance(block, dict) else None
        if value is not None:
            computation = genus.name("0012", field)
            certificate_hash = certificates.certification_hash(
                computation, a2, value
            )
            card_certifications[f"{block_name}.{field}"] = certificate_hash
            held[computation] = certificates.Certificate(
                hash=certificate_hash, by="SageMath"
            )
    metadata["certifications"] = card_certifications
    (tmp_path / "lattices" / "0012.md").write_text(
        records.record_text(metadata, source.content)
    )
    loaded = corpus.load(tmp_path)
    [request] = genus.requests(loaded, held, ("0012",), seconds=60)
    assert "genus_symbol" not in request["fields"]
    assert "genus_class_count" not in request["fields"]
    assert "automorphism_group_order" not in request["fields"]
    assert request["fields"]

    path = tmp_path / "lattices" / "0012.md"
    changed = frontmatter.load(str(path))
    changed.metadata["integral"]["genus_class_count"] = 2
    path.write_text(records.record_text(corpus.front_matter(changed), changed.content))
    loaded = corpus.load(tmp_path)
    [request] = genus.requests(loaded, held, ("0012",), seconds=60)
    assert "genus_class_count" in request["fields"]

    changed.metadata["integral"]["genus_class_count"] = 1
    path.write_text(records.record_text(corpus.front_matter(changed), changed.content))
    loaded = corpus.load(tmp_path)
    del held[genus.name("0012", "genus_class_count")]
    [request] = genus.requests(loaded, held, ("0012",), seconds=600)
    assert "genus_class_count" in request["fields"]

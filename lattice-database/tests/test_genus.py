"""`latticedb certify` computes the pending genus invariants with SageMath, writes the missing ones and refuses a stored value that differs."""

import shutil
from pathlib import Path

import frontmatter
from latticedb import certificates, corpus, genus
from latticedb.model import Yaml

REPOSITORY = Path(__file__).resolve().parent.parent
LOADED = corpus.load(REPOSITORY)
A2 = next(entry.lattice for entry in LOADED.entries if entry.lattice.tag == "0012")


def test_sagemath_computes_the_invariants_of_a2() -> None:
    # A2 (record 0012) has rank 2, so no spinor genera are computed. It is alone in its genus, and O(A2) is the dihedral group of order 12 (Conway and Sloane, SPLAG, Chapter 4, Section 6.1).
    # O(A2) = W(A2) x {1, -1}, and -1 acts on A_L = Z/3 by -1 while W(A2) acts trivially, so O~(A2) = W(A2): it is simply transitive on the 6 roots,
    # its rotations of order 3 have 2 orbits on them, and so do SO~ = O~ n SO. The norms of A2 are 2, 6, 8, ..., so c(1) = c(3) = c(4) = 0.
    one = {"constant": 0, "z": [0, 1, 0, 0], "w": [0, 0, 0, 0]}
    two = {"constant": 0, "z": [0, 2, 0, 0], "w": [0, 0, 0, 0]}
    [values] = genus.computed(genus.requests(LOADED, {}, ("0012",), seconds=60), seconds=60)
    assert {field: values[field] for field in genus.BLOCKS if field in values} == {
        "genus_symbol": "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)",
        "automorphism_group_order": 12,
        "genus_class_count": 1,
        "hyperbolic_index": 0,
        "primitive_orbits": {"O": one, "SO": one, "Otilde": one, "SOtilde": two, "O+": one, "SO+": one, "Otilde+": two, "SOtilde+": two},
    }


def test_a_computed_series_of_orbits_fills_the_coefficients_that_a_record_does_not_state(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    document = frontmatter.load(str(path))
    document.metadata["integral"]["primitive_orbits"] = {"O": {"z": [None, 1]}}
    path.write_text(frontmatter.dumps(document))
    assert genus.store(path, {"primitive_orbits": {"O": {"constant": 0, "z": [0, 1, 0, 0], "w": [0, 0, 0, 0]}}}) == {}
    assert frontmatter.load(str(path)).metadata["integral"]["primitive_orbits"] == {"O": {"z": [0, 1, 0, 0], "constant": 0, "w": [0, 0, 0, 0]}}
    expected = f"{path}: integral.primitive_orbits.O.z[1] is 1, and SageMath computes 2"
    assert genus.store(path, {"primitive_orbits": {"O": {"z": [0, 2]}}}) == {"primitive_orbits": expected}


def test_sagemath_computes_the_hyperbolic_index() -> None:
    # U + U + E8(-1) has hyperbolic index 2; U(2) + <-2> has 0, because its discriminant group (Z/2)^3 needs rank 3;
    # I_{1,1} is odd unimodular and U is even, so it has 0; I_{2,1} is U + <1>.
    plane = [[0, 1], [1, 0]]
    e8 = next(entry.lattice for entry in LOADED.entries if entry.lattice.tag == "0094")
    negative_e8: list[list[int]] = [[-int(x) for x in row] for row in e8.gram_tensor]
    grams: dict[str, list[list[int]]] = {
        "U+U+E8(-1)": block_sum(plane, plane, negative_e8),
        "U(2)+<-2>": block_sum([[0, 2], [2, 0]], [[-2]]),
        "I_{1,1}": block_sum([[1]], [[-1]]),
        "I_{2,1}": block_sum([[1]], [[1]], [[-1]]),
    }
    chosen: list[dict[str, Yaml]] = [{"tag": tag, "gram": gram, "sign": 0, "fields": ["hyperbolic_index"]} for tag, gram in grams.items()]
    computed = {str(values["tag"]): values["hyperbolic_index"] for values in genus.computed(chosen, seconds=60)}
    assert computed == {"U+U+E8(-1)": 2, "U(2)+<-2>": 0, "I_{1,1}": 0, "I_{2,1}": 1}


def test_sagemath_computes_the_orbits_of_an_even_lattice_that_contains_two_hyperbolic_planes() -> None:
    # U + U + <-2> has A_L = Z/2 with q(a) = -1/2, and O(q_L) = 1. A primitive v has v* + L = 0 when div(v) = 1, which needs b(v, v) even,
    # and v* + L = a when div(v) = 2, which needs b(v, v) / 4 = -1/2 mod 2: of norms in [-4, 4] only -2. So c(-2) = 2 and c(n) = 1 for the other even n.
    plane = [[0, 1], [1, 0]]
    [values] = genus.computed([{"tag": "U+U+<-2>", "gram": block_sum(plane, plane, [[-2]]), "sign": 0, "fields": ["primitive_orbits"]}], seconds=60)
    series = {"constant": 1, "z": [0, 1, 0, 1], "w": [0, 2, 0, 1]}
    assert values["primitive_orbits"] == dict.fromkeys(("O", "SO", "Otilde", "SOtilde", "O+", "SO+", "Otilde+", "SOtilde+"), series)


def test_the_orbits_of_an_indefinite_lattice_are_computed_only_when_it_is_even_and_contains_two_hyperbolic_planes() -> None:
    # Record 0036 is U + U(2), even with no stored hyperbolic index; record 0015 is the odd lattice I_{1,1}.
    by_tag = {entry.lattice.tag: entry.lattice for entry in LOADED.entries}
    assert genus.applies("primitive_orbits", by_tag["0036"], 2)
    assert not genus.applies("primitive_orbits", by_tag["0036"], 1)
    assert not genus.applies("primitive_orbits", by_tag["0015"], 2)
    assert genus.applies("primitive_orbits", A2, 0)


def test_sagemath_computes_the_spinor_genera() -> None:
    # SPLAG, Chapter 15, Section 9.6: the genus of A2 + <18> has two spinor genera, one with the form and one with a second representative.
    # Genus(G).representatives() finds two classes, so each spinor genus holds one.
    # SPLAG, Chapter 15, Section 11: the genus of diag(-1, 64, 2) has two spinor genera and hence two classes.
    chosen: list[dict[str, Yaml]] = [
        {"tag": "SPLAG 9.6", "gram": [[2, 1, 0], [1, 2, 0], [0, 0, 18]], "sign": 1, "fields": ["genus_class_count", "spinor_genus_count", "spinor_genera"]},
        {"tag": "SPLAG 11", "gram": [[-1, 0, 0], [0, 64, 0], [0, 0, 2]], "sign": 0, "fields": ["genus_class_count", "spinor_genus_count", "spinor_genera"]},
    ]
    computed = {str(values.pop("tag")): values for values in genus.computed(chosen, seconds=60)}
    expected = {"genus_class_count": 2, "spinor_genus_count": 2, "spinor_genera": [1, 1]}
    assert {tag: {field: values[field] for field in expected} for tag, values in computed.items()} == {"SPLAG 9.6": expected, "SPLAG 11": expected}


def block_sum(*blocks: list[list[int]]) -> list[list[int]]:
    size = sum(len(block) for block in blocks)
    rows: list[list[int]] = []
    offset = 0
    for block in blocks:
        rows.extend([0] * offset + row + [0] * (size - offset - len(row)) for row in block)
        offset += len(block)
    return rows


def test_a_certified_value_is_not_requested() -> None:
    inputs = certificates.gram_digest(A2)
    held = {genus.name("0012", field): certificates.Certificate(inputs=inputs, by="SageMath") for field in genus.BLOCKS}
    assert genus.requests(LOADED, held, ("0012",), seconds=60) == []
    # A computation that did not finish within 60 seconds is requested again only with a larger time limit.
    held[genus.name("0012", "genus_class_count")] = certificates.Certificate(inputs=inputs, by="SageMath", seconds=60)
    assert genus.requests(LOADED, held, ("0012",), seconds=60) == []
    [request] = genus.requests(LOADED, held, ("0012",), seconds=600)
    assert request["fields"] == ["genus_class_count"]


def test_a_missing_value_is_written(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    document = frontmatter.load(str(path))
    del document.metadata["integral"]["genus_class_count"]
    path.write_text(frontmatter.dumps(document))
    assert genus.store(path, {"genus_class_count": 1}) == {}
    assert frontmatter.load(str(path)).metadata["integral"]["genus_class_count"] == 1


def test_a_stored_value_that_differs_is_refused(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    expected = f"{path}: definite.automorphism_group_order is 12, and SageMath computes 6"
    assert genus.store(path, {"automorphism_group_order": 6}) == {"automorphism_group_order": expected}

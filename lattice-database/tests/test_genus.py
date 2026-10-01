"""`latticedb certify` computes the pending genus invariants with SageMath, writes the missing ones and refuses a stored value that differs."""

import shutil
from pathlib import Path

import frontmatter
from latticedb import certificates, corpus, genus

REPOSITORY = Path(__file__).resolve().parent.parent
LOADED = corpus.load(REPOSITORY)
A2 = next(entry.lattice for entry in LOADED.entries if entry.lattice.tag == "0012")


def test_sagemath_computes_the_invariants_of_a2() -> None:
    # A2 (record 0012) is alone in its genus, and O(A2) is the dihedral group of order 12 (Conway and Sloane, SPLAG, Chapter 4, Section 6.1).
    [values] = genus.computed(genus.requests(LOADED, {}, ("0012",), seconds=60), seconds=60)
    assert {field: values[field] for field in genus.BLOCKS} == {
        "genus_symbol": "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)",
        "automorphism_group_order": 12,
        "genus_class_count": 1,
    }


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

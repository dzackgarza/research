"""Fast checks on `genus.store` that need no corpus and spawn no SageMath.

Every test that loads the full corpus or that spawns SageMath lives in
`tests/validation/test_genus_validation.py` and runs only as
`just test-validation` and in CI.
"""

import shutil
from pathlib import Path

import frontmatter

from latticedb import genus

REPOSITORY = Path(__file__).resolve().parent.parent


def test_a_computed_series_of_orbits_fills_the_coefficients_that_a_record_does_not_state(
    tmp_path: Path,
) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    document = frontmatter.load(str(path))
    document.metadata["integral"]["primitive_orbits"] = {"O": {"z": [None, 1]}}
    path.write_text(frontmatter.dumps(document))
    genus.store(
        path,
        {
            "primitive_orbits": {
                "O": {"constant": 0, "z": [0, 1, 0, 0], "w": [0, 0, 0, 0]}
            }
        },
    )
    assert frontmatter.load(str(path)).metadata["integral"]["primitive_orbits"] == {
        "O": {"z": [0, 1, 0, 0], "constant": 0, "w": [0, 0, 0, 0]}
    }
    genus.store(path, {"primitive_orbits": {"O": {"z": [0, 2]}}})
    assert frontmatter.load(str(path)).metadata["integral"]["primitive_orbits"]["O"]["z"] == [0, 2, 0, 0]


def test_a_missing_value_is_written(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    document = frontmatter.load(str(path))
    del document.metadata["integral"]["genus_class_count"]
    path.write_text(frontmatter.dumps(document))
    genus.store(path, {"genus_class_count": 1})
    assert frontmatter.load(str(path)).metadata["integral"]["genus_class_count"] == 1


def test_a_stored_value_that_differs_is_replaced(tmp_path: Path) -> None:
    path = tmp_path / "0012.md"
    shutil.copy(REPOSITORY / "lattices" / "0012.md", path)
    genus.store(path, {"automorphism_group_order": 6})
    assert frontmatter.load(str(path)).metadata["definite"]["automorphism_group_order"] == 6


def test_orbit_certificate_value_excludes_source_only_tail_and_reference() -> None:
    stored = {
        "O": {
            "constant": 0,
            "z": [0, 1, 0, 0, 7, 8],
            "w": [0, 0, 0, 0, 9],
            "reference": {"citation": "A source."},
        }
    }
    assert genus.certified_value("primitive_orbits", stored) == {
        "O": {
            "constant": 0,
            "z": [0, 1, 0, 0],
            "w": [0, 0, 0, 0],
        }
    }

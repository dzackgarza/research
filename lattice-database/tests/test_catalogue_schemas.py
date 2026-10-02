"""The additional catalogues retain their mathematical links to existing records."""

from pathlib import Path
from fractions import Fraction

import frontmatter
import pytest

from latticedb import corpus
from latticedb.geometric import GeometricObject
from pydantic import ValidationError

ROOT = Path(__file__).parent.parent


def _record(path: Path, metadata: dict[str, str | int | bool | list[str] | list[int] | list[list[int]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter.dumps(frontmatter.Post("", **metadata)))


def test_group_orbit_and_genus_links_use_the_existing_lattice_records(tmp_path: Path) -> None:
    for name in ("lattices", "morphisms", "geometric-objects", "geometric-families"):
        (tmp_path / name).symlink_to(ROOT / name, target_is_directory=True)
    for name in ("families.yaml", "retired-tags.yaml"):
        (tmp_path / name).symlink_to(ROOT / name)
    source = frontmatter.load(str(ROOT / "morphisms" / "02BG-02BG.md"))
    generators = [entry["name"] for entry in source.metadata["morphisms"]]
    group_path = tmp_path / "orthogonal-subgroups" / "leech-q8.md"
    _record(group_path, {
        "slug": "leech-q8", "lattice": "02BG", "name": "Leech pointwise stabilizer",
        "defining_property": "source_defined", "generator_morphisms": generators, "order": 8,
    })
    orbit_path = tmp_path / "vector-orbits" / "leech-q8-e1.md"
    _record(orbit_path, {
        "slug": "leech-q8-e1", "lattice": "02BG", "subgroup": "leech-q8",
        "representative": [1] + [0] * 16, "square": 4, "divisibility": 1,
    })
    _record(tmp_path / "genera" / "a2.md", {
        "slug": "a2", "signature": [2, 0], "determinant": 3, "parity": "even",
        "symbol": "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)",
        "representative_tags": ["0012"], "class_number": 1,
        "representatives_complete": True, "mass": "1/12",
    })
    loaded = corpus.load(tmp_path)
    assert loaded.orthogonal_subgroups[0].value.order == 8
    assert loaded.genera[0].value.mass == Fraction(1, 12)

    _record(orbit_path, {
        "slug": "leech-q8-e1", "lattice": "02BG", "subgroup": "leech-q8",
        "representative": [1] + [0] * 16, "square": 6, "divisibility": 1,
    })
    with pytest.raises(corpus.CorpusInvalid, match="representative has square 4, not 6"):
        corpus.load(tmp_path)


def test_complete_intersection_configuration_has_the_stated_dimension() -> None:
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    source.metadata["slug"] = "quartic-k3"
    source.metadata["name"] = "Smooth quartic K3 surface"
    source.metadata["construction"] = {
        "kind": "calabi_yau_complete_intersection",
        "ambient_projective_dimensions": [3],
        "equation_multidegrees": [[4]],
    }
    GeometricObject.model_validate(source.metadata)
    source.metadata["construction"]["equation_multidegrees"] = [[3]]
    with pytest.raises(ValidationError, match="equation degrees sum to n_i"):
        GeometricObject.model_validate(source.metadata)


def test_modularity_requires_the_scaled_dual_isometry(tmp_path: Path) -> None:
    for name in ("families.yaml", "retired-tags.yaml"):
        (tmp_path / name).symlink_to(ROOT / name)
    lattice_dir = tmp_path / "lattices"
    lattice_dir.mkdir()
    source = frontmatter.load(str(ROOT / "lattices" / "0012.md"))
    source.metadata["related"] = []
    source.metadata["integral"]["modular_scale"] = 3
    (lattice_dir / "0012.md").write_text(frontmatter.dumps(source))
    dual_path = tmp_path / "morphisms" / "dual" / "a2-duality.md"
    _record(dual_path, {
        "slug": "a2-duality", "lattice": "0012", "scale": 3,
        "matrix": [[1, 0], [0, -1]],
    })
    corpus.load(tmp_path)
    _record(dual_path, {
        "slug": "a2-duality", "lattice": "0012", "scale": 3,
        "matrix": [[1, 0], [0, 1]],
    })
    with pytest.raises(corpus.CorpusInvalid, match="matrix must give the stated isometry"):
        corpus.load(tmp_path)

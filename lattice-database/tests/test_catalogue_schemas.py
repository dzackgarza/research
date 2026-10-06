"""The additional catalogues retain their mathematical links to existing records."""

from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
from pydantic import TypeAdapter, ValidationError

from latticedb import checks, corpus
from latticedb.catalogues import LatticeFamily
from latticedb.geometric import GeometricObject

ROOT = Path(__file__).parent.parent


def _record(
    path: Path,
    metadata: dict[str, str | int | bool | list[str] | list[int] | list[list[int]]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter.dumps(frontmatter.Post("", **metadata)))


def test_group_orbit_and_genus_links_use_the_existing_lattice_records(
    tmp_path: Path,
) -> None:
    lattices = tmp_path / "lattices"
    lattices.mkdir()
    for tag in ("0012",):
        (lattices / f"{tag}.md").symlink_to(ROOT / "lattices" / f"{tag}.md")
    morphisms = tmp_path / "morphisms"
    morphisms.mkdir()
    (morphisms / "02BG-02BG.md").symlink_to(ROOT / "morphisms" / "02BG-02BG.md")
    for name in ("families.yaml", "retired-tags.yaml"):
        (tmp_path / name).symlink_to(ROOT / name)
    source = frontmatter.load(str(ROOT / "morphisms" / "02BG-02BG.md"))
    generators = [entry["name"] for entry in source.metadata["morphisms"]]
    # The subgroup data lives on the lattice card itself, in its `groups` block.
    lattice = frontmatter.load(str(ROOT / "lattices" / "02BG.md"))
    lattice.metadata["groups"] = {
        "leech-q8": {
            "generator_morphisms": generators,
            "cardinality": 8,
            "orbits": [{"square": 4, "representatives": [[1] + [0] * 16]}],
        }
    }
    (lattices / "02BG.md").write_text(frontmatter.dumps(lattice))
    _record(
        tmp_path / "genera" / "a2.md",
        {
            "slug": "a2",
            "signature": [2, 0],
            "determinant": 3,
            "parity": "even",
            "symbol": "II_{2,0} (2: 1^-2; 3: 1^-1 3^-1)",
            "representative_tags": ["0012"],
            "class_number": 1,
            "representatives_complete": True,
            "mass": "1/12",
        },
    )
    loaded = corpus.load(tmp_path)
    by_tag = {entry.lattice.tag: entry.lattice for entry in loaded.entries}
    assert by_tag["02BG"].groups["leech-q8"].cardinality == 8
    assert loaded.genera[0].value.mass == Fraction(1, 12)

    # A representative whose square disagrees with its key is a problem.
    lattice.metadata["groups"]["leech-q8"]["orbits"] = [
        {"square": 6, "representatives": [[1] + [0] * 16]}
    ]
    (lattices / "02BG.md").write_text(frontmatter.dumps(lattice))
    assert any(
        "representative has square 4, not 6" in problem
        for problem in checks.report(tmp_path)
    )


def test_complete_intersection_configuration_has_the_stated_dimension() -> None:
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    source.metadata["slug"] = "quartic-k3"
    source.metadata["name"] = "Smooth quartic K3 surface"
    source.metadata["construction"] = {
        "kind": "calabi_yau_complete_intersection",
        "ambient_projective_dimensions": [3],
        "equation_multidegrees": [[4]],
    }
    adapter = TypeAdapter(GeometricObject)
    adapter.validate_python(source.metadata)
    source.metadata["construction"]["equation_multidegrees"] = [[3]]
    with pytest.raises(ValidationError, match="equation degrees sum to n_i"):
        adapter.validate_python(source.metadata)


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
    _record(
        dual_path,
        {
            "slug": "a2-duality",
            "lattice": "0012",
            "scale": 3,
            "matrix": [[1, 0], [0, -1]],
        },
    )
    corpus.load(tmp_path)
    _record(
        dual_path,
        {
            "slug": "a2-duality",
            "lattice": "0012",
            "scale": 3,
            "matrix": [[1, 0], [0, 1]],
        },
    )
    assert any(
        "matrix must give the stated isometry" in problem
        for problem in checks.report(tmp_path)
    )
def _family(**overrides: object) -> dict[str, object]:
    """The split OG6 family with overrides applied."""
    record: dict[str, object] = {
        "slug": "og6-polarized-split",
        "name": "Polarized OG6 lattices, split case",
        "parameter": "d",
        "minimum": 1,
        "rank": 7,
        "signature": [2, 5],
        "gram_template": [
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, -2, 0, 0],
            [0, 0, 0, 0, 0, -2, 0],
            [0, 0, 0, 0, 0, 0, "-2*d"],
        ],
    }
    record.update(overrides)
    return record


def test_the_shipped_lattice_families_validate() -> None:
    for slug in (
        "og6-polarized-split",
        "og6-polarized-nonsplit-4t-1",
        "og6-polarized-nonsplit-4t-2",
    ):
        document = frontmatter.load(str(ROOT / "lattice-families" / f"{slug}.md"))
        family = LatticeFamily.model_validate(document.metadata)
        assert (family.rank, tuple(family.signature)) == (7, (2, 5))


def test_a_lattice_family_rejects_a_malformed_template() -> None:
    base = _family()
    # Not square.
    with pytest.raises(ValidationError, match="rank rows"):
        LatticeFamily.model_validate(
            base | {"gram_template": base["gram_template"][:6]}
        )
    # Not symmetric.
    rows = [list(row) for row in base["gram_template"]]
    rows[0][1] = 0
    with pytest.raises(ValidationError, match="symmetric"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # An unknown name.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "-2*e"
    with pytest.raises(ValidationError, match="nothing else"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # Not arithmetic.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "2**d"
    with pytest.raises(ValidationError, match="integer arithmetic"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # The parameter never occurs.
    plain = [
        [0 if value == "-2*d" else value for value in row]
        for row in base["gram_template"]
    ]
    with pytest.raises(ValidationError, match="occurs in the template"):
        LatticeFamily.model_validate(base | {"gram_template": plain})
    # Degenerate at a probe point.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "0*d"
    with pytest.raises(ValidationError, match="nonsingular"):
        LatticeFamily.model_validate(base | {"gram_template": rows})
    # The stated signature is not the signature.
    with pytest.raises(ValidationError, match="stated signature"):
        LatticeFamily.model_validate(base | {"signature": [3, 4]})
    # The parameter is not an identifier.
    with pytest.raises(ValidationError, match="identifier"):
        LatticeFamily.model_validate(base | {"parameter": "2d"})


def test_the_corpus_loads_lattice_families_and_checks_their_slugs(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    (tmp_path / "lattices" / "0012.md").symlink_to(ROOT / "lattices" / "0012.md")
    (tmp_path / corpus.FAMILIES_FILE).symlink_to(ROOT / corpus.FAMILIES_FILE)
    (tmp_path / corpus.RETIRED_FILE).symlink_to(ROOT / corpus.RETIRED_FILE)
    families = tmp_path / "lattice-families"
    families.mkdir()
    for slug in (
        "og6-polarized-split",
        "og6-polarized-nonsplit-4t-1",
        "og6-polarized-nonsplit-4t-2",
    ):
        (families / f"{slug}.md").symlink_to(ROOT / "lattice-families" / f"{slug}.md")
    loaded = corpus.load(tmp_path)
    assert [entry.value.slug for entry in loaded.lattice_families] == [
        "og6-polarized-nonsplit-4t-1",
        "og6-polarized-nonsplit-4t-2",
        "og6-polarized-split",
    ]
    assert [
        problem
        for problem in checks.report(tmp_path)
        if 'lattice-families' in problem
    ] == []

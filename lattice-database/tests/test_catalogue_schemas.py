"""The additional catalogues retain their mathematical links to existing records."""

from fractions import Fraction
from pathlib import Path

import frontmatter
import pytest
import yaml
from pydantic import TypeAdapter, ValidationError

from latticedb import checks, corpus
from latticedb.catalogues import ArithmeticGroup, LatticeFamily, LieGroup
from latticedb.geometric import GeometricObject

ROOT = Path(__file__).parent.parent


def test_shipped_group_cards_have_first_class_lie_and_arithmetic_owners() -> None:
    lie = [
        LieGroup.model_validate(frontmatter.load(str(path)).metadata)
        for path in (ROOT / "lie-groups").glob("*.md")
    ]
    arithmetic = [
        ArithmeticGroup.model_validate(frontmatter.load(str(path)).metadata)
        for path in (ROOT / "arithmetic-groups").glob("*.md")
    ]
    by_slug = {group.slug: group for group in lie}
    assert by_slug["o-2-10"].orthogonal_signature == (2, 10)
    assert by_slug["o-2-10"].dimension == 66
    assert by_slug["o-2-10"].real_rank == 2
    assert all(group.ambient_lie_group in by_slug for group in arithmetic)
    enriques = frontmatter.load(str(ROOT / "lattices" / "029J.md")).metadata
    assert enriques["orthogonal_group"] == "o-t-en"
    assert "gamma-en-2" in enriques["arithmetic_groups"]
    assert next(group for group in arithmetic if group.slug == "o-t-en").standard_name == "O"


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
    for name in ("families.yaml", "retired-tags.yaml"):
        (tmp_path / name).symlink_to(ROOT / name)
    lattice = frontmatter.load(str(ROOT / "lattices" / "02BG.md"))
    generators = [
        entry["name"]
        for entry in lattice.metadata["morphisms"]
        if entry["target"] == "02BG"
    ]
    lattice.metadata["morphisms"] = [
        entry for entry in lattice.metadata["morphisms"] if entry["target"] == "02BG"
    ]
    lattice.metadata["arithmetic_groups"] = ["leech-q8"]
    (lattices / "02BG.md").write_text(frontmatter.dumps(lattice))
    for tag in ("0012", "02BG"):
        document = frontmatter.load(str(lattices / f"{tag}.md"))
        p, q = sorted(document.metadata["signature"])
        path = tmp_path / "lie-groups" / f"o-{p}-{q}.md"
        path.parent.mkdir(exist_ok=True)
        path.symlink_to(ROOT / "lie-groups" / path.name)
    p, q = sorted(lattice.metadata["signature"])
    group_path = tmp_path / "arithmetic-groups" / "leech-q8.md"
    _record(
        group_path,
        {
            "slug": "leech-q8",
            "name": "Leech Q8",
            "latex": "Q_8",
            "lattice": "02BG",
            "ambient_lie_group": f"o-{p}-{q}",
            "data": {
                "generator_morphisms": generators,
                "cardinality": 8,
                "orbits": [{"square": 4, "representatives": [[1] + [0] * 16]}],
            },
        },
    )
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
    assert loaded.arithmetic_groups[0].value.data.cardinality == 8
    assert loaded.genera[0].value.mass == Fraction(1, 12)


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
    changed = adapter.validate_python(source.metadata)
    assert changed.construction is not None
    assert changed.construction.equation_multidegrees == [[3]]


def test_dual_lattice_data_lives_on_the_owning_lattice_card() -> None:
    a2 = frontmatter.load(str(ROOT / "lattices" / "0012.md")).metadata
    assert a2["dual_gram_tensor"] == [["2/3", "1/3"], ["1/3", "2/3"]]
    assert not (ROOT / "lattices" / "0017.md").exists()
    retired = yaml.safe_load((ROOT / "retired-tags.yaml").read_text())
    assert "dual is stored on lattice card 0012" in retired["0017"]
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
    with pytest.raises(ValidationError, match="occurs in gram_template"):
        LatticeFamily.model_validate(base | {"gram_template": plain})
    # Mathematical claims are accepted by the schema and checked through the preamble in CI.
    rows = [list(row) for row in base["gram_template"]]
    rows[6][6] = "0*d"
    LatticeFamily.model_validate(base | {"gram_template": rows})
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

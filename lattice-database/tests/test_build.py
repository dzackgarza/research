"""The site that `build` writes from the corpus of this repository."""

import json
from pathlib import Path

import pytest
from latticedb import corpus, site

ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="module")
def built(tmp_path_factory: pytest.TempPathFactory) -> Path:
    target = tmp_path_factory.mktemp("site") / "_site"
    site.build(ROOT, target)
    return target


@pytest.fixture(scope="module")
def rows(built: Path) -> dict[str, site.Row]:
    return {row["tag"]: row for row in json.loads((built / "lattices.json").read_text())["rows"]}


def sections(built: Path, tag: str) -> set[str]:
    """The sections of the page of a lattice that come from the blocks of its record."""
    html = (built / "tag" / f"{tag}.html").read_text()
    return {block for block in ("integral", "definite", "indefinite", "hyperbolic") if f'<h2 id="{block}">' in html}


def test_the_database_has_one_row_and_one_page_for_each_record(built: Path, rows: dict[str, site.Row]) -> None:
    tags = {entry.lattice.tag for entry in corpus.load(ROOT / "lattices")}
    assert set(rows) == tags
    assert {path.stem for path in (built / "tag").glob("*.html")} == tags


def test_the_row_of_e8_states_its_invariants(rows: dict[str, site.Row]) -> None:
    e8 = rows["0094"]
    assert e8["rank"] == 8
    assert e8["signature"] == "(8, 0)"
    assert e8["determinant"] == "1"
    assert e8["definiteness"] == "positive definite"
    assert e8["properties"] == ["integral", "even", "unimodular", "root lattice"]
    assert e8["discriminant_group"] == "0"
    assert e8["kissing_number"] == 240
    assert e8["automorphism_group_order"] == "696729600"
    assert e8["root_system"] == "E8"


def test_a_page_has_a_section_exactly_for_each_block_of_its_record(built: Path) -> None:
    assert sections(built, "0094") == {"integral", "definite"}
    assert sections(built, "0138") == {"integral", "indefinite", "hyperbolic"}


def test_the_page_of_a_lattice_shows_the_components_of_its_gram_tensor(built: Path) -> None:
    html = (built / "tag" / "0094.html").read_text()
    assert "[[2,0,-1,0,0,0,0,0]," in html.replace(" ", "")


def test_a_collection_page_links_exactly_the_lattices_that_satisfy_its_conditions(built: Path, rows: dict[str, site.Row]) -> None:
    html = (built / "collection" / "even-unimodular.html").read_text()
    lattices = [entry.lattice for entry in corpus.load(ROOT / "lattices")]
    members = {lattice.tag for lattice in lattices if lattice.integral is not None and lattice.integral.parity == "even" and lattice.is_unimodular}
    assert members
    assert {tag for tag in rows if f'href="../tag/{tag}.html"' in html} == members


def test_the_root_lattice_collection_lists_the_lattices_that_their_roots_generate(built: Path) -> None:
    html = (built / "collection" / "root-lattices.html").read_text()
    e8, negative_e8, doubled_e8, z10 = "0094", "0104", "0095", "0120"
    assert {tag for tag in (e8, negative_e8, doubled_e8, z10) if f'href="../tag/{tag}.html"' in html} == {e8, negative_e8}


def test_the_page_of_z10_states_the_index_of_the_sublattice_that_its_roots_generate(built: Path) -> None:
    html = (built / "tag" / "0120.html").read_text()
    assert "rank 10, index 2 in" in html


def test_the_fields_page_defines_every_property_of_the_database(built: Path) -> None:
    html = (built / "fields.html").read_text()
    labels = {label for entry in corpus.load(ROOT / "lattices") for label in site.properties(entry.lattice)}
    assert labels
    for label in labels:
        assert f'<th scope="row">{"p-elementary" if label.endswith("-elementary") else label}</th>' in html


def test_the_fields_page_documents_every_field_of_a_record(built: Path) -> None:
    html = (built / "fields.html").read_text()
    for _, _, model in site.fields():
        for field in model.model_fields:
            assert f"<code>{field}</code>" in html

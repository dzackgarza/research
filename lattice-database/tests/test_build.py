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
    tags = {entry.lattice.tag for entry in corpus.load(ROOT).entries}
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
    lattices = [entry.lattice for entry in corpus.load(ROOT).entries]
    members = {lattice.tag for lattice in lattices if lattice.integral is not None and lattice.integral.parity == "even" and lattice.is_unimodular}
    assert members
    assert {tag for tag in rows if f'href="../tag/{tag}.html"' in html} == members


def test_the_root_lattice_collection_lists_the_lattices_that_their_roots_generate(built: Path) -> None:
    html = (built / "collection" / "root-lattices.html").read_text()
    e8, negative_e8, doubled_e8, z10 = "0094", "0104", "0095", "0120"
    zero_form, doubled_u, u, u_plus_doubled_e8 = "0010", "0013", "0016", "0124"
    listed = {tag for tag in (e8, negative_e8, doubled_e8, z10, zero_form, doubled_u, u, u_plus_doubled_e8) if f'href="../tag/{tag}.html"' in html}
    assert listed == {e8, negative_e8, doubled_e8, z10}


def test_the_page_of_a_root_lattice_states_norms_of_roots_that_generate_it(built: Path) -> None:
    assert r"S = \{4\}" in (built / "tag" / "0095.html").read_text()
    assert r"S = \{1\}" in (built / "tag" / "0120.html").read_text()
    assert r"S = \{-2\}" in (built / "tag" / "0104.html").read_text()
    assert r"\(S = " not in (built / "tag" / "0016.html").read_text()


def test_the_row_of_a_definite_root_lattice_states_the_type_of_its_roots_and_the_lattice_that_they_generate(rows: dict[str, site.Row]) -> None:
    # E8 is even and unimodular, so its roots are its 240 vectors with b(r, r) = 2.
    e8 = rows["0094"]
    assert (e8["phi_type"], e8["root_span"], e8["root_span_rank"], e8["root_span_index"], e8["root_span_primitive"]) == ("E8", "E8", 8, 1, "yes")
    # The roots of Z^10 are the vectors +-e_i and +-e_i +-e_j: type B10. The vectors with b(r, r) = 2 alone are of type D10.
    z10 = rows["0120"]
    assert (z10["root_system"], z10["phi_type"], z10["root_span"], z10["root_span_index"]) == ("D10", "B10", "Z^10", 1)
    # E8(2) has the roots of E8, with b(r, r) = 4, and no vector with b(r, r) = 2.
    doubled_e8 = rows["0095"]
    assert (doubled_e8["root_system"], doubled_e8["phi_type"], doubled_e8["root_span"]) == ("", "E8", "E8(2)")


def test_the_row_of_a_lattice_that_is_not_a_root_lattice_states_the_index_and_that_the_root_sublattice_is_not_primitive(rows: dict[str, site.Row]) -> None:
    # The roots of U are +-(1, 1) and +-(1, -1), with b(r, r) = 2 and -2; they generate the vectors with even coordinate sum.
    u = rows["0016"]
    assert "not a root lattice" in u["properties"]
    assert (u["root_span"], u["root_span_rank"], u["root_span_index"], u["root_span_primitive"]) == ("<2> + <-2>", 2, 2, "no")
    # The roots of D12+ are the 264 roots of D12, which has index 2.
    d12_plus = rows["0151"]
    assert (d12_plus["phi_type"], d12_plus["root_span"], d12_plus["root_span_index"], d12_plus["root_span_primitive"]) == ("D12", "D12", 2, "no")
    # <0> has no roots: the sublattice 0 is primitive, and its index is not finite.
    zero_form = rows["0010"]
    assert (zero_form["root_span"], zero_form["root_span_rank"], zero_form["root_span_index"], zero_form["root_span_primitive"]) == ("0", 0, None, "yes")


def test_each_record_decides_whether_it_is_a_root_lattice(rows: dict[str, site.Row]) -> None:
    for row in rows.values():
        assert ("root lattice" in row["properties"]) != ("not a root lattice" in row["properties"]), row["tag"]
        assert row["root_span_primitive"] in {"yes", "no"}, row["tag"]


def test_the_page_of_a_lattice_writes_its_roots_in_the_basis_of_the_record(built: Path) -> None:
    # The record of E8 is in a basis of simple roots, so the simple root alpha_j is e_j.
    e8 = (built / "tag" / "0094.html").read_text()
    for index in range(1, 9):
        assert rf"<td>\(\alpha_{{{index}}}\)</td>" in e8
        assert rf"<td>\(e_{{{index}}}\)</td>" in e8
    # The roots of U are e_1 + e_2 and e_1 - e_2; they generate a sublattice that is isometric to <2> + <-2>.
    u = (built / "tag" / "0016.html").read_text()
    assert r"\(e_{1} + e_{2}\)" in u
    assert r"\(e_{1} - e_{2}\)" in u
    assert 'href="../tag/0002.html"' in u
    assert 'href="../tag/0008.html"' in u


def test_the_page_of_a_sum_states_the_orthogonal_decomposition_that_its_basis_gives(built: Path) -> None:
    # U + E8(-2): e_1, e_2 are the basis of U, and e_3, ..., e_10 the basis of E8(-2).
    html = (built / "tag" / "0124.html").read_text()
    assert r"\(\mathbb{Z}\{e_{1}, e_{2}\}\) \(\oplus\) \(\mathbb{Z}\{e_{3}, \dots, e_{10}\}\)" in html
    # E8 is not an orthogonal sum of two sublattices that its basis vectors generate.
    assert "The record fixes an orthogonal decomposition" not in (built / "tag" / "0094.html").read_text()


def test_the_page_of_z10_states_the_index_of_the_sublattice_that_its_roots_generate(built: Path) -> None:
    html = (built / "tag" / "0120.html").read_text()
    assert "rank 10, index 2 in" in html


def test_the_fields_page_defines_every_property_of_the_database(built: Path) -> None:
    html = (built / "fields.html").read_text()
    labels = {label for entry in corpus.load(ROOT).entries for label in site.properties(entry.lattice)}
    assert labels
    for label in labels:
        assert f'<th scope="row">{"p-elementary" if label.endswith("-elementary") else label}</th>' in html


def test_the_fields_page_lists_every_family_with_its_meaning_and_its_number_of_lattices(built: Path) -> None:
    html = (built / "fields.html").read_text()
    loaded = corpus.load(ROOT)
    assert loaded.families
    for family, meaning in loaded.families.items():
        count = sum(family in entry.lattice.families for entry in loaded.entries)
        assert f'<th scope="row"><code>{family}</code></th>' in html
        assert f'href="./database.html?family={family}">{count}</a>' in html
        assert meaning.split("$")[0].split("`")[0].strip() in html


def test_the_fields_page_documents_every_field_of_a_record(built: Path) -> None:
    html = (built / "fields.html").read_text()
    for _, _, model in site.fields():
        for field in model.model_fields:
            assert f"<code>{field}</code>" in html

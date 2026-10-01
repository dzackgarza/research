"""The site that `build` writes from the corpus of this repository."""

import json
from pathlib import Path

import pytest
from latticedb import corpus, site
from markupsafe import escape

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
    assert sections(built, "0233") == {"integral", "indefinite", "hyperbolic"}


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
    e8, z10, u_plus_negative_e8 = "0094", "0120", "0128"
    k12, u, u_plus_doubled_u, u_plus_doubled_e8 = "0150", "0016", "0036", "0124"
    listed = {tag for tag in (e8, z10, u_plus_negative_e8, k12, u, u_plus_doubled_u, u_plus_doubled_e8) if f'href="../tag/{tag}.html"' in html}
    assert listed == {e8, z10, u_plus_negative_e8}


def test_the_page_of_a_root_lattice_states_norms_of_roots_that_generate_it(built: Path) -> None:
    assert r"S = \{2\}" in (built / "tag" / "0094.html").read_text()
    assert r"S = \{1\}" in (built / "tag" / "0120.html").read_text()
    assert r"S = \{-2, 2\}" in (built / "tag" / "0128.html").read_text()
    assert r"\(S = " not in (built / "tag" / "0016.html").read_text()


def test_the_row_of_a_definite_root_lattice_states_the_type_of_its_roots_and_the_lattice_that_they_generate(rows: dict[str, site.Row]) -> None:
    # E8 is even and unimodular, so its roots are its 240 vectors with b(r, r) = 2.
    e8 = rows["0094"]
    assert (e8["phi_type"], e8["root_span"], e8["root_span_rank"], e8["root_span_index"], e8["root_span_primitive"]) == ("E8", "E8", 8, 1, "yes")
    # The roots of I_{10,0} are the vectors +-e_i and +-e_i +-e_j: type B10. The vectors with b(r, r) = 2 alone are of type D10.
    i10 = rows["0120"]
    assert (i10["root_system"], i10["phi_type"], i10["root_span"], i10["root_span_index"]) == ("D10", "B10", "I_{10,0}", 1)
    # Lambda9 has minimum 4, so no vector with b(r, r) = 2; its roots are of type D8, with b(r, r) = 4, and A1, with b(r, r) = 8.
    laminated_9 = rows["0110"]
    assert (laminated_9["root_system"], laminated_9["phi_type"], laminated_9["root_span"], laminated_9["root_span_index"]) == ("", "D8 A1", "D8(2) + <8>", 4)


def test_the_row_of_a_lattice_that_is_not_a_root_lattice_states_the_index_and_that_the_root_sublattice_is_not_primitive(rows: dict[str, site.Row]) -> None:
    # The roots of U are +-(1, 1) and +-(1, -1), with b(r, r) = 2 and -2; they generate the vectors with even coordinate sum.
    u = rows["0016"]
    assert "not a root lattice" in u["properties"]
    assert (u["root_span"], u["root_span_rank"], u["root_span_index"], u["root_span_primitive"]) == ("<2> + <-2>", 2, 2, "no")
    # The roots of D12+ are the 264 roots of D12, which has index 2.
    d12_plus = rows["0151"]
    assert (d12_plus["phi_type"], d12_plus["root_span"], d12_plus["root_span_index"], d12_plus["root_span_primitive"]) == ("D12", "D12", 2, "no")
    # K12 has minimum 4 and no roots: the sublattice 0 is primitive, and its index is not finite.
    k12 = rows["0150"]
    assert (k12["root_span"], k12["root_span_rank"], k12["root_span_index"], k12["root_span_primitive"]) == ("0", 0, None, "yes")


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
    assert 'href="../tag/0001.html"' in u
    assert r"\langle 2 \rangle" in u
    assert r"\langle -2 \rangle" in u


def test_the_page_of_a_sum_states_the_orthogonal_decomposition_that_its_basis_gives(built: Path) -> None:
    # U + E8(-2): e_1, e_2 are the basis of U, and e_3, ..., e_10 the basis of E8(-2).
    html = (built / "tag" / "0124.html").read_text()
    assert r"\(\mathbb{Z}\{e_{1}, e_{2}\}\) \(\oplus\) \(\mathbb{Z}\{e_{3}, \dots, e_{10}\}\)" in html
    # E8 is not an orthogonal sum of two sublattices that its basis vectors generate.
    assert "The record fixes an orthogonal decomposition" not in (built / "tag" / "0094.html").read_text()


def test_the_pages_of_z10_and_u_state_the_index_of_the_sublattice_that_the_roots_generate(built: Path) -> None:
    # The roots +-e_i of Z^10 generate it; the roots of U generate the vectors with even coordinate sum.
    assert r'<th scope="row">\([L : R(L)]\)</th><td>1</td>' in (built / "tag" / "0120.html").read_text()
    assert r'<th scope="row">\([L : R(L)]\)</th><td>2</td>' in (built / "tag" / "0016.html").read_text()


def test_the_fields_page_defines_every_property_of_the_database(built: Path) -> None:
    html = (built / "fields.html").read_text()
    labels = {label for entry in corpus.load(ROOT).entries for label in site.properties(entry.lattice)}
    assert labels
    for label in labels:
        page, anchor, _ = site.PROPERTY_MEANINGS["p-elementary" if label.endswith("-elementary") else label]
        name = "p-elementary" if label.endswith("-elementary") else label
        assert f'<th scope="row"><a class="theory-link" href="./theory/{page}.html#{anchor}">{name}</a></th>' in html


def test_the_fields_page_lists_every_family_with_its_meaning_and_its_number_of_lattices(built: Path) -> None:
    html = (built / "fields.html").read_text()
    loaded = corpus.load(ROOT)
    assert loaded.families
    for family, meaning in loaded.families.items():
        count = sum(family in entry.lattice.families for entry in loaded.entries)
        assert f'<th scope="row"><code>{family}</code></th>' in html
        assert f'href="./database.html?family={family}">{count}</a>' in html
        assert escape(meaning.split("$")[0].split("`")[0].strip()) in html


def test_the_fields_page_documents_every_field_of_a_record(built: Path) -> None:
    html = (built / "fields.html").read_text()
    for _, _, model in site.fields():
        for field in model.model_fields:
            assert f"<code>{field}</code>" in html


def test_each_morphism_file_has_a_page_linked_from_the_index_and_from_the_pages_of_its_lattices(built: Path) -> None:
    files = corpus.load(ROOT).morphisms
    assert files
    index = (built / "morphisms.html").read_text()
    for entry in files:
        record = entry.morphisms
        link = f"morphism/{record.source}-{record.target}.html"
        assert (built / link).exists()
        assert link in index
        for tag in (record.source, record.target):
            assert link in (built / "tag" / f"{tag}.html").read_text()


def test_a_morphism_page_draws_the_lines_of_each_matrix(built: Path) -> None:
    html = (built / "morphism" / "0128-027E.html").read_text()
    assert r"\begin{array}{rr|rrrrrrrr}" in html
    assert html.count(r"\hline") == 4


def test_the_theory_index_links_each_theory_page_and_a_lattice_page_links_the_theory_it_uses(built: Path) -> None:
    slugs = {path.stem for path in (ROOT / "theory").glob("*.md")}
    assert {path.stem for path in (built / "theory").glob("*.html")} == slugs
    index = (built / "theory.html").read_text()
    assert all(f'href="./theory/{slug}.html"' in index for slug in slugs)
    e8 = (built / "tag" / "0094.html").read_text()
    assert 'href="../theory/roots.html#roots"' in e8
    assert 'href="../theory/definite-lattices.html#theta-series"' in e8


def test_the_link_check_reports_a_missing_page_and_a_missing_anchor(tmp_path: Path) -> None:
    (tmp_path / "theory").mkdir()
    (tmp_path / "theory" / "roots.html").write_text('<h2 id="roots">Roots</h2>')
    (tmp_path / "index.html").write_text('<a href="theory/roots.html#roots">a</a><a href="theory/roots.html#record">b</a><a href="theory/morphisms.html">c</a>')
    assert site.broken_links(tmp_path) == ["index.html: theory/roots.html#record", "index.html: theory/morphisms.html"]

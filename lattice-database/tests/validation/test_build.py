"""The site that `build` writes from the corpus of this repository.

Validation subtree: every test here builds the full site from the full corpus,
so this module runs only as `just test-validation` and in CI, never as
`just test`. Fast coverage of the same site logic on fixtures lives in
`tests/test_geometric.py` and `tests/test_catalogue_schemas.py`.
"""

import json
from pathlib import Path

import pytest
from markupsafe import escape

from latticedb import corpus, site

ROOT = Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="module")
def built(tmp_path_factory: pytest.TempPathFactory) -> Path:
    target = tmp_path_factory.mktemp("site") / "_site"
    site.build(ROOT, target)
    return target


@pytest.fixture(scope="module")
def rows(built: Path) -> dict[str, site.Row]:
    return {
        row["tag"]: row
        for row in json.loads((built / "lattices.json").read_text())["rows"]
    }


def sections(built: Path, tag: str) -> set[str]:
    """The sections of the page of a lattice that come from the blocks of its record."""
    html = (built / "tag" / f"{tag}.html").read_text()
    return {
        block
        for block in ("integral", "definite", "indefinite", "hyperbolic")
        if f'<h2 id="{block}">' in html
    }


def test_the_database_has_one_row_and_one_page_for_each_record(
    built: Path, rows: dict[str, site.Row]
) -> None:
    tags = {entry.lattice.tag for entry in corpus.load(ROOT).entries}
    assert set(rows) == tags
    assert {path.stem for path in (built / "tag").glob("*.html")} == tags


def test_the_row_of_e8_states_its_invariants(rows: dict[str, site.Row]) -> None:
    e8 = rows["0094"]
    assert e8["rank"] == 8
    assert e8["signature"] == "(8, 0)"
    assert e8["determinant"] == "1"
    assert e8["definiteness"] == "positive definite"
    assert e8["properties"] == ["integral", "even", "root lattice"]
    assert e8["discriminant_group"] == "0"
    assert e8["kissing_number"] == 240
    assert e8["automorphism_group_order"] == "696729600"
    assert e8["root_system"] == "E8"


def test_a_page_has_a_section_exactly_for_each_block_of_its_record(built: Path) -> None:
    assert sections(built, "0094") == {"integral", "definite"}
    assert sections(built, "0233") == {"integral", "indefinite", "hyperbolic"}


def test_the_page_of_a_lattice_shows_the_components_of_its_gram_tensor(
    built: Path,
) -> None:
    html = (built / "tag" / "0094.html").read_text()
    assert "[[2,0,-1,0,0,0,0,0]," in html.replace(" ", "")


def test_a_collection_page_links_exactly_the_lattices_that_satisfy_its_conditions(
    built: Path, rows: dict[str, site.Row]
) -> None:
    html = (built / "collection" / "even-unimodular.html").read_text()
    lattices = [entry.lattice for entry in corpus.load(ROOT).entries]
    members = {
        lattice.tag
        for lattice in lattices
        if "even-unimodular" in lattice.families
    }
    assert members
    assert {tag for tag in rows if f'href="../tag/{tag}.html"' in html} == members


def test_the_root_lattice_collection_lists_the_lattices_that_their_roots_generate(
    built: Path,
) -> None:
    html = (built / "collection" / "root-lattices.html").read_text()
    e8, z10, u_plus_negative_e8 = "0094", "0120", "0128"
    k12, u, u_plus_doubled_u, u_plus_doubled_e8 = "0150", "0016", "0036", "0124"
    listed = {
        tag
        for tag in (
            e8,
            z10,
            u_plus_negative_e8,
            k12,
            u,
            u_plus_doubled_u,
            u_plus_doubled_e8,
        )
        if f'href="../tag/{tag}.html"' in html
    }
    assert listed == {e8, z10, u_plus_negative_e8}


def test_the_page_of_a_root_lattice_states_norms_of_roots_that_generate_it(
    built: Path,
) -> None:
    assert r"S = \{2\}" in (built / "tag" / "0094.html").read_text()
    assert r"S = \{1\}" in (built / "tag" / "0120.html").read_text()
    assert r"S = \{-2, 2\}" in (built / "tag" / "0128.html").read_text()
    assert r"\(S = " not in (built / "tag" / "0016.html").read_text()


def test_rows_render_only_stored_root_type_and_root_span_data(
    rows: dict[str, site.Row],
) -> None:
    e8 = rows["0094"]
    assert (e8["phi_type"], e8["root_span"]) == ("E8", "E8")

    i10 = rows["0120"]
    assert (i10["root_system"], i10["phi_type"], i10["root_span"]) == (
        "D10",
        "B10",
        "I_{10,0}",
    )

    laminated_9 = rows["0110"]
    assert (
        laminated_9["root_system"],
        laminated_9["phi_type"],
        laminated_9["root_span"],
    ) == ("", "D8 A1", "D8(2) + <8>")

    assert rows["0016"]["root_span"] == "<2> + <-2>"
    assert (rows["0151"]["phi_type"], rows["0151"]["root_span"]) == ("D12", "D12")
    assert rows["0150"]["root_span"] == "0"


def test_the_page_of_a_lattice_writes_its_roots_in_the_basis_of_the_record(
    built: Path,
) -> None:
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


def test_the_fields_page_defines_every_property_of_the_database(built: Path) -> None:
    html = (built / "fields.html").read_text()
    labels = {
        label
        for entry in corpus.load(ROOT).entries
        for label in site.properties(entry.lattice)
    }
    assert labels
    for label in labels:
        page, anchor, _ = site.PROPERTY_MEANINGS[
            "p-elementary" if label.endswith("-elementary") else label
        ]
        name = "p-elementary" if label.endswith("-elementary") else label
        assert (
            f'<th scope="row"><a class="theory-link" href="./theory/{page}.html#{anchor}">{name}</a></th>'
            in html
        )


def test_the_fields_page_lists_every_family_with_its_meaning_and_its_number_of_lattices(
    built: Path,
) -> None:
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


def test_each_stored_morphism_is_rendered_on_its_source_and_backlinked_from_its_target(
    built: Path,
) -> None:
    entries = corpus.load(ROOT).entries
    stored = [
        (entry.lattice, morphism)
        for entry in entries
        for morphism in entry.lattice.morphisms
    ]
    assert stored
    for source, morphism in stored:
        source_html = (built / "tag" / f"{source.tag}.html").read_text()
        target_html = (built / "tag" / f"{morphism.target}.html").read_text()
        assert str(site.inline_markup(morphism.name)) in source_html
        assert f'href="../tag/{source.tag}.html#morphisms"' in target_html


def test_a_source_lattice_page_draws_the_lines_of_its_morphism_matrices(built: Path) -> None:
    html = (built / "tag" / "0128.html").read_text()
    assert r"\begin{array}{rr|rrrrrrrr}" in html
    assert html.count(r"\hline") == 4


def test_the_theory_index_links_each_theory_page_and_a_lattice_page_links_the_theory_it_uses(
    built: Path,
) -> None:
    slugs = {path.stem for path in (ROOT / "theory").glob("*.md")}
    assert {path.stem for path in (built / "theory").glob("*.html")} == slugs
    index = (built / "theory.html").read_text()
    assert all(f'href="./theory/{slug}.html"' in index for slug in slugs)
    e8 = (built / "tag" / "0094.html").read_text()
    assert 'href="../theory/roots.html#roots"' in e8
    assert 'href="../theory/definite-lattices.html#theta-series"' in e8


def test_the_link_check_reports_a_missing_page_and_a_missing_anchor(
    tmp_path: Path,
) -> None:
    (tmp_path / "theory").mkdir()
    (tmp_path / "theory" / "roots.html").write_text('<h2 id="roots">Roots</h2>')
    (tmp_path / "index.html").write_text(
        '<a href="theory/roots.html#roots">a</a><a href="theory/roots.html#record">b</a><a href="theory/morphisms.html">c</a>'
    )
    assert site.broken_links(tmp_path) == [
        "index.html: theory/roots.html#record",
        "index.html: theory/morphisms.html",
    ]


def test_real_orthogonal_groups_are_first_class_cards_with_lattice_backlinks(
    built: Path, rows: dict[str, site.Row]
) -> None:
    html = (built / "lie-groups.html").read_text()
    signatures = {
        (min(row["n_plus"], row["n_minus"]), max(row["n_plus"], row["n_minus"]))
        for row in rows.values()
        if row["n_plus"] is not None
        and row["n_minus"] is not None
        and row["rank"] is not None
        and row["n_plus"] + row["n_minus"] == row["rank"]
    }
    assert signatures
    for p, q in signatures:
        slug = f"o-{p}-{q}"
        assert (built / "lie-group" / f"{slug}.html").exists()
        assert f'href="./lie-group/{slug}.html"' in html

    lattice_html = (built / "tag" / "029J.html").read_text()
    assert 'href="../lie-group/o-2-10.html"' in lattice_html
    assert 'href="../arithmetic-group/o-t-en.html"' in lattice_html
    arithmetic_html = (built / "arithmetic-group" / "gamma-en-2.html").read_text()
    assert 'href="../tag/029J.html"' in arithmetic_html
    assert 'href="../lie-group/o-2-10.html"' in arithmetic_html
    # The lattice reaches its ambient real group through the stored arithmetic-group card.
    assert "I_{" not in table
